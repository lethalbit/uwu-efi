# SPDX-License-Identifier: BSD-3-Clause

subdir('include')

libuwuefi_srcs = files([

])


subdir('arch')


libuwuefi = static_library(
	'uwuefi',
	libuwuefi_srcs,
	include_directories: [
		uwuefi_inc,
		uwuefi_arch,
	],
	gnu_symbol_visibility: 'inlineshidden',
	implicit_include_directories: false,
	pic: true,
	install: (not meson.is_subproject()),
)
