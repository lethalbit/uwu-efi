# SPDX-License-Identifier: BSD-3-Clause
uwuefi_arch_inc = include_directories('.')

subdir('aarch64')
subdir('amd64')
subdir('ebc')
subdir('rv64')

uwuefi_arch = [
	uwuefi_arch_inc,
	uwuefi_arch_aarch64_inc,
	uwuefi_arch_amd64_inc,
	uwuefi_arch_ebc_inc,
	uwuefi_arch_rv64_inc,
]

uwuefi_arch_headers = files([

])

install_headers(
	uwuefi_arch_headers,
	subdir: 'uwuefi' / 'arch'
)
