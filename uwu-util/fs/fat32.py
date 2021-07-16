#!/usr/bin/env python
# SPDX-License-Identifier: BSD-3-Clause

from io import BytesIO, SEEK_END, SEEK_SET

from construct import *

boot_sector = Struct(
	'jmp'      / Const(b'\xEB\x00\x90'),
	'oem_name' / Bytes(8),
	'params'   / Struct(
		'bpb'             / Struct(
			'sub_bpb'        / Struct(
				'log_sec_bytes'   / Int16ul,
				'log_sec_clust'   / Bytes(1),
				'res_log_sec'     / Int16ul,
				'fat_count'       / Bytes(1),
				'max_roots'       / Int16ul,
				'total_log_sec'   / Int16ul,
				'media_desc'      / Bytes(1),
				'log_sec_per_fat' / Int16ul,
			),
			'phys_sec'       / Int16ul,
			'disk_heads'     / Int16ul,
			'hidden_sect'    / Int32ul,
			'total_log_sect' / Int32ul,
		),
		'logical_sectors' / Int32ul,
		'drive_desc'      / Bytes(2),
		'version'         / Bytes(2),
		'root_cluster_id' / Int32ul,
		'fs_logical_sec'  / Int16ul,
		'first_log_sec'   / Int16ul,
		'reserved'        / Padding(12, pattern=b'\xF6'),
		'drive_num'       / Bytes(1),
		'dunno_lol'       / Bytes(1),
		'ext_boot_sig'    / Bytes(1),
		'vol_id'          / Bytes(4),
		'vol_label'       / Bytes(11),
		'fs_type'         / Bytes(8),
	),
	'phys_drive_num' / Bytes(1),
	'boot_sig'       / Const(b'\x55\xAA')
)
class FAT32Filesystem:
	def __init__(self, *, data_stream):
		if isinstance(data_stream, bytes):
			self._data = BytesIO(data_stream)
		else:
			self._data = data_stream

		self.offset = self._data.tell()
		self._data.seek(0, SEEK_END)
		self.end = self._data.tell()
		self.size = self.end - self.offset
		self._data.seek(self.offset, SEEK_SET)

	def __str__(self):
		return str(self._fs_image)


if __name__ == '__main__':
	def dump_img(file_name):
		with open(file_name, 'rb') as f:
			fs = FAT32Filesystem(data_stream = f)
			print(fs)

	import sys
	from os import path
	from argparse import ArgumentParser, ArgumentDefaultsHelpFormatter

	parser = ArgumentParser(
		prog = 'nya_umu',
		formatter_class = ArgumentDefaultsHelpFormatter,
		description = 'FAT32 test runner'
	)

	global_options = parser.add_argument_group('Global Options')

	global_options.add_argument(
		'--file', '-f',
		type = str,
		required = True,
		help = 'FAT32 image file to operate on',
	)

	global_options.add_argument(
		'--dump', '-d',
		action = 'store_true',
		default = False,
		help = 'Dump out the details of a FAT32 fs image'
	)

	args = parser.parse_args()

	if not path.exists(args.file):
		print(f'Unable to open file \'{args.file}\' does it exist?')
		sys.exit(1)

	if args.dump:
		sys.exit(dump_img(args.file))


	sys.exit(1)
