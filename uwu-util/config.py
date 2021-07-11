# SPDX-License-Identifier: BSD-3-Clause
from os import path, environ
from enum import Enum, auto, unique

__all__ = (
	'UTIL_NAME', 'UTIL_VERSION',

	'DATA_DIR', 'CACHE_DIR', 'ENV_DIR', 'OVMF_DIR', 'ENV_CACHE',

	'OVMF_BUILD_URL', 'OVMF_IMGS',

	'UEFIArchitecture',
)


UTIL_NAME = 'uwu-efi'
UTIL_VERSION = 'v0.1'

@unique
class UEFIArchitecture(Enum):
	x86_64  = auto()
	aarch64 = auto()

	def __str__(self) -> str:
		return self.name

	@staticmethod
	def from_string(s: str):
		try:
			return UEFIArchitecture[s]
		except KeyError:
			raise ValueError()

XDG_CACHE_DIR = path.join(path.expanduser('~'), '.cache') if 'XDG_CACHE_HOME' not in environ else environ['XDG_CACHE_HOME']
XDG_DATA_HOME = path.join(path.expanduser('~'), '.local/share') if 'XDG_DATA_HOME' not in environ else environ['XDG_DATA_HOME']

DATA_DIR  = path.join(XDG_DATA_HOME, UTIL_NAME)
CACHE_DIR = path.join(XDG_CACHE_DIR, UTIL_NAME)

ENV_DIR   = path.join(CACHE_DIR, 'environments')
OVMF_DIR  = path.join(DATA_DIR, 'ovmf')

ENV_CACHE = path.join(CACHE_DIR, 'environments.json')


OVMF_BUILD_URL = 'https://retrage.github.io/edk2-nightly/bin/'

OVMF_IMGS = {
	UEFIArchitecture.x86_64: {
		'debug': {
			'code': 'DEBUGX64_OVMF_CODE.fd',
			'vars': 'DEBUGX64_OVMF_VARS.fd',
			'both': 'DEBUGX64_OVMF.fd'
		},
		'release': {
			'code': 'RELEASEX64_OVMF_CODE.fd',
			'vars': 'RELEASEX64_OVMF_VARS.fd',
			'both': 'RELEASEX64_OVMF.fd'
		}
	},
	UEFIArchitecture.aarch64: {
		'debug': {
			'code': 'DEBUGAARCH64_QEMU_EFI.fd',
			'vars': 'DEBUGAARCH64_QEMU_VARS.fd',
		},
		'release': {
			'code': 'RELEASEAARCH64_QEMU_EFI.fd',
			'vars': 'RELEASEAARCH64_QEMU_VARS.fd',
		}
	},
}

