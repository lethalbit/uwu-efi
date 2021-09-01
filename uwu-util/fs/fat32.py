#!/usr/bin/env python
# SPDX-License-Identifier: BSD-3-Clause

from io import BytesIO, SEEK_END, SEEK_SET

from construct import *


fat32_media_type = 'FAT32 Media Type' / Enum(Int8ul,
	Media8singleSided   = 0xE5,
	Media525DoubleSided = 0xED,
	MediaNonStandard    = 0xEE,
	MediaSuperFloppy    = 0xEF,
	Media0              = 0xF0,
	Media1              = 0xF4,
	Media2              = 0xF5,
	Media3              = 0xF8,
	Media4              = 0xF9,
	Media5              = 0xFA,
	Media6              = 0xFB,
	Media7              = 0xFC,
	Media8              = 0xFD,
	Media9              = 0xFE,
	Media10             = 0xFF,
)

fat32_boot_param_block = 'FAT32 Boot Parameter Block' / Struct (
	'sector_size'         / Hex(Int16ul),
	'sectors_per_cluster' / Hex(Int8ul),
	'reserved_sectors'    / Hex(Int16ul),
	'fat_count'           / Hex(Int8ul),
	'dir_entries'         / Hex(Int16ul),
	'sectors'             / Hex(Int16ul),
	'media'               / Hex(fat32_media_type),
	'sectors_per_fat'     / Hex(Int16ul),
	'sectors_per_track'   / Hex(Int16ul),
	'head_count'          / Hex(Int16ul),
	'hidden_sectors'      / Hex(Int32ul),
	'total_sectors'       / Hex(Int32ul),
	# FAT32 Extended Parameters
	'length'              / Hex(Int32ul),
	'flags'               / Hex(Int16ul),
	'version'             / Struct(
		'major'     / Hex(Int8ul),
		'minor'     / Hex(Int8ul)      ),
	'root_cluster'        / Hex(Int32ul),
	'info_sector'         / Hex(Int16ul),
	'backup_boot'         / Hex(Int16ul),
	'reserved'            / Hex(Bytes(12)),
	'drive_number'        / Hex(Int8ul),
	'mount_state'         / Hex(Bytes(1)),
	'boot_signature'      / Hex(Int8ul),
	'volume_id'           / Hex(Bytes(4)),
	'volume_label'        / PaddedString(11, 'ascii'),
	'fs_type'             / Hex(Bytes(8)),

)

fat32_boot_sector = 'FAT32 Boot Sector' / Struct(
	'jmp'       / Hex(Bytes(3)),
	'name'      / PaddedString(8, 'ascii'),
	'params'    / fat32_boot_param_block,
	'boot_code' / Bytes(0x1FE - (11 + fat32_boot_param_block.sizeof())),
	'boot_sig'  / Hex(Const(b'\x55\xAA')),
)

fat32_fsinfo_sector = 'FAT32 Filesystem Info Sector' / Struct(
	'fsinfo_sig'    / Hex(Const(b'\x52\x52\x61\x41')),
	'reserved'      / Bytes(480),
	'fsinfo_sig2'   / Hex(Const(b'\x72\x72\x41\x61')),
	'last_known_fc' / Hex(Int32ul),
	'recent_fc'     / Hex(Int32ul),
	'reserved2'     / Bytes(12),
	'fsinfo_sig3'   / Hex(Const(b'\x00\x00\x55\xAA')),
)

fat32_reserved_sectors = 'FAT32 Reserved Sectors' / Struct(
	'boot'   / fat32_boot_sector,                  # FAT32 Boot Sector
	'fsinfo' / fat32_fsinfo_sector,                # FAT32 FS Info Sector
	           Lazy(Bytes(
	           		(  this.boot.params.sector_size
	           		 * this.boot.params.reserved_sectors)
	           		- (fat32_boot_sector.sizeof() + fat32_fsinfo_sector.sizeof())
	           ))
)


fat32_allocation_table = 'FAT32 File Allocation Table' / Struct(
	'table_size'	/ Computed(
		(	this._.reserved_sectors.boot.params.length
		* this._.reserved_sectors.boot.params.sector_size
		) // 4),
	'tables'    	/ Array(
		this._.reserved_sectors.boot.params.fat_count,
		'table' / LazyArray(
			this.table_size,
			BitsSwapped(BitStruct(
				'cluster_address' / BitsInteger(28),
				'reserved'        / BitsInteger(4))
		)),
	),
)

fat32_directory_entry = 'FAT32 Directory Entry' / Struct(
	'short_name'	/ PaddedString(8, 'ascii'),
	'short_ext'		/ PaddedString(3, 'ascii'),
	'file_attrs'	/ BitsSwapped(BitStruct(
		'read_only'		/ Flag,
		'hidden'		/ Flag,
		'system'		/ Flag,
		'volume_label'	/ Flag,
		'subdirectory'	/ Flag,
		'archive'		/ Flag,
		'device'		/ Flag,
		'reserved'		/ Flag,
	)),
	'wtf_microsoft'		/ Bytes(1),
	'timespamp_garbage'	/ Bytes(7),
	'fc_high'			/ Hex(Int16ul),
	'lm_time'			/ Bytes(2),
	'lm_date'			/ Bytes(2),
	'fc_low'			/ Hex(Int16ul),
	'file_size'			/ Hex(Int32ul),

)

fat32_directory_table = 'FAT32 Directory Table' / Struct(
	'volume_label'	/ fat32_directory_entry,
	'dir_entries' 	/ Array(8, fat32_directory_entry),
)

fat32_data_region = 'FAT32 Data Region' / Struct(
	'root_dir_table'  / fat32_directory_table,
	'nya?'            / GreedyBytes
)

fat32_fs_image = 'FAT32 Filesystem' / Struct(
	'reserved_sectors' 		/ fat32_reserved_sectors,
	'file_allocation_table' / fat32_allocation_table,
	'data_region'           / fat32_data_region,
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

		self._fs_image = fat32_fs_image.parse_stream(self._data)

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
