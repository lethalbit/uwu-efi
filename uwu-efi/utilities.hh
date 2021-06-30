/* SPDX-License-Identifier: BSD-3-Clause */
/* uwu-efi/utilities.hh - Utilities for working with bits and the like */
#pragma once
#if !defined(UWUEFI_UTILITIES_HH)
#define UWUEFI_UTILITIES_HH

#include <type_traits>
#include <limits>
#include <cstdint>

namespace uwuefi {
	namespace bits {
		/* pulled from wegistew-cc (https://github.com/lethalbit/wegistew-cc) */
		template<std::size_t _lsb, std::size_t _msb>
		struct bitspan_t final {
			static constexpr std::size_t size = (_msb - _lsb) + 1;
			static_assert(_lsb <= _msb, "bitspan LSB must be smaller than or equal to the MSB");

			/* Value field machinery */
			template<typename T, std::size_t _msb_ = _msb, std::size_t _lsb_ = _lsb>
			struct field final {
				using value_type = T;
				using vu_type = typename std::make_unsigned_t<value_type>;

				static constexpr auto msb = _msb_;
				static constexpr auto lsb = _lsb_;
				static constexpr std::size_t width = std::numeric_limits<vu_type>::digits;
				static_assert(msb <= width, "MSB must be less than or equal to the width of the bitspan type");
				static constexpr vu_type computed_mask = (((vu_type(1) << (vu_type(msb) + vu_type(1)) - vu_type(lsb)) - vu_type(1)) << vu_type(lsb));


				/* Get the value of this field in the given register */
				template<typename V = vu_type>
				[[nodiscard]]
				static inline constexpr
				std::enable_if_t<!std::is_enum<V>::value, V> get(const V v) noexcept {
					return (vu_type((v) & computed_mask) >> lsb);
				}

				template<typename V = vu_type>
				[[nodiscard]]
				static inline constexpr
				std::enable_if_t<std::is_enum<V>::value, V> get(const V v) noexcept {
					return static_cast<V>(
						vu_type((v) & computed_mask) >> lsb
					);
				}

				/* Set the value of this field in the given register */
				template<typename V>
				[[nodiscard]]
				static inline constexpr
				std::enable_if_t<!std::is_enum<V>::value> set(V& f, const V v) noexcept {

					f = (((f) & ~computed_mask) | ((vu_type(v) << lsb) & computed_mask));
				}

				template<typename V>
				[[nodiscard]]
				static inline constexpr
				std::enable_if_t<std::is_enum<V>::value> set(V& f, const V v) noexcept {
					using Vt = typename std::underlying_type_t<V>;

					f = (((f) & ~computed_mask) | ((vu_type(v) << lsb) & computed_mask));
				}
			};
		};

		/* A "specialization" of genmask_t for a single bit field */
		template<std::size_t idx>
		using bit_t = bitspan_t<idx, idx>;

		namespace {
			template<std::size_t, typename...>
			struct type_at_index_t;

			template<std::size_t N, typename T, typename... U>
			struct type_at_index_t<N, T, U...> {
				using type = typename type_at_index_t<N - 1, U...>::type;
			};

			template<typename T, typename... U>
			struct type_at_index_t<0, T, U...> {
				using type = T;
			};
		}

		template<typename T, typename... U>
		struct bitfield_t final {
			using value_type = T;
			using vu_type = typename std::make_unsigned_t<value_type>;

			static constexpr auto width = std::numeric_limits<T>::digits;
			static constexpr auto size = width;
			static constexpr std::size_t field_count = sizeof... (U);

			/* Returns the field requested by index */
			template<std::size_t idx>
			using field = typename type_at_index_t<idx, U...>::type::template field<T>;

			/* This is functionally equivalent to ::fields<idx>::get() */
			template<std::size_t idx, typename V = vu_type>
			[[nodiscard]]
			static inline constexpr auto get(const V v) noexcept {
				static_assert(idx < field_count, "field index out of range");
				return field<idx>::template get<V>(v);
			}

			/* This is functionally equivalent to ::fields<idx>::set(v) */
			template<std::size_t idx, typename V>
			[[nodiscard]]
			static inline constexpr void set(V& f, const V v) noexcept {
				static_assert(idx < field_count, "field index out of range");
				field<idx>::set(f, v);
			}

		};


		/* endian swapping facilities */
		[[nodiscard]]
		inline constexpr uint16_t swap16(const uint16_t x) noexcept {
			return uint16_t(
				((x & 0x00FFU) << 8U) |
				((x & 0xFF00U) >> 8U)
			);
		}

		[[nodiscard]]
		inline constexpr uint32_t swap32(const uint32_t x) noexcept {
			return uint32_t(
				((x & 0x000000FFU) << 24U) |
				((x & 0x0000FF00U) << 8U ) |
				((x & 0x00FF0000U) >> 8U ) |
				((x & 0xFF000000U) >> 24U)
			);
		}

		[[nodiscard]]
		inline constexpr uint64_t swap64(const uint64_t x) noexcept {
			return uint64_t(
				((x & 0x00000000000000FFU) << 56U) |
				((x & 0x000000000000FF00U) << 40U) |
				((x & 0x0000000000FF0000U) << 24U) |
				((x & 0x00000000FF000000U) << 8U ) |
				((x & 0x000000FF00000000U) >> 8U ) |
				((x & 0x0000FF0000000000U) >> 24U) |
				((x & 0x00FF000000000000U) >> 40U) |
				((x & 0xFF00000000000000U) >> 56U)
			);
		}

		/* rotl/rotr */
		template<typename T>
		[[nodiscard]]
		inline typename std::enable_if<std::is_integral<T>::value && std::is_unsigned<T>::value, T>::type
		rotl(T x, const std::size_t k) noexcept {
			constexpr auto bits = std::numeric_limits<T>::digits;
			return (x << k) | (x >> (bits - k));
		}

		template<typename T>
		[[nodiscard]]
		inline typename std::enable_if<std::is_integral<T>::value && std::is_unsigned<T>::value, T>::type
		rotr(T x, const std::size_t k) noexcept {
			constexpr auto bits = std::numeric_limits<T>::digits;
			return (x >> k) | (x << (bits - k));
		}
	}
}

#endif /* UWUEFI_UTILITIES_HH */
