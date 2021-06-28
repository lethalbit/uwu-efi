# SPDX-License-Identifier: BSD-3-Clause

substrate = dependency(
	'substrate',
	required: true,
	version: '>=0.0.1',
	fallback: ['substrate', 'substrate_dep'],
	native: true,
	default_options: [
		'default_library=static',
		'build_tests=false',
	]
)


subdir('include')


uwuasm_srcs = files([
	'uwu-asm.cc',
])


uwuasm = executable(
	'uwu-asm',
	uwuasm_srcs,
	include_directories: [
		uwuasm_inc,
		uwuefi_inc,
	],
	dependencies: [ substrate ],
	native: true,
	install: true,
	build_by_default: true,
)
