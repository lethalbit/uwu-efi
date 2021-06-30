# SPDX-License-Identifier: BSD-3-Clause
project(
	'uwu-efi',
	'cpp',
	default_options: [
		'warning_level=3',
		'cpp_std=c++17',
		'b_ndebug=if-release',
		'b_lto=true',
	],
	license: 'BSD-3-Clause',
	version: '0.0.1',
	subproject_dir: 'deps'
)

cxx_c = meson.get_compiler('cpp', native: true)
cxx_n = meson.get_compiler('cpp', native: false)

extended_warnings = [
	'-Wdouble-promotion',
	'-Wformat=2',
	'-Wformat-overflow=2',
	'-Wformat-signedness',
	'-Wformat-truncation',
	'-Wnull-dereference',
	'-Wmissing-attributes',
	'-Wmissing-braces',
	'-Wsequence-point',
	'-Wreturn-type',
	'-Wunused',
	'-Wunused-local-typedefs',
	'-Wunused-const-variable=2',
	'-Wmaybe-uninitialized',
	'-Wunknown-pragmas',
	'-Wstrict-aliasing',
	'-Wstrict-overflow=3',
	'-Wstring-compare',
	'-Wstringop-overflow',
	'-Warith-conversion',
	'-Wvla-parameter',
	'-Wduplicated-branches',
	'-Wshadow=local',
	'-Wunsafe-loop-optimizations',
	'-Wbad-function-cast',
	'-Wcast-qual',
	'-Wcast-align=strict',
	'-Wcast-function-type',
	'-Wconversion',
	'-Wdangling-else',
	'-Wsign-conversion',
	'-Wfloat-conversion',
	'-Wpacked',
	'-Wpadded',
	'-Wredundant-decls',
	'-Winline',
	'-Wvla',
	'-Wstack-protector',
	'-Wunsuffixed-float-constant',
	'-Wimplicit-fallthrough',
]

add_project_arguments(
	cxx_c.get_supported_arguments(extended_warnings),
	language: 'cpp'
)

add_project_arguments(
	cxx_n.get_supported_arguments(extended_warnings),
	language: 'cpp'
)

py = import('python')
py_modules = [
	'jinja2',
	'construct',
]

py_inst = py.find_installation(
	'python3',
	required: true,
	modules: py_modules,
)

uwuefi_inc = include_directories('.')

subdir('etc')
subdir('uwu-efi')

if get_option('build_uwuasm')
	subdir('uwu-asm')
endif

subdir('examples')

if not meson.is_subproject()
	pkgconfig = import('pkgconfig')
	pkgconfig.generate(
		subdirs: '.',
		name: 'uwu-efi',
		filebase: 'uwu-efi',
		libraries: [ libuwuefi ],
		version: meson.project_version(),
		description: 'A clean, modern C++ 17 SDK for writing UEFI applications.'
	)
endif

uwuefi_dep = declare_dependency(
	include_directories: [
		uwuefi_inc,
		uwuefi_arch,
	],
	link_with: libuwuefi,
	version: meson.project_version()
)
