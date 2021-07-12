#!/usr/bin/env python
# SPDX-License-Identifier: BSD-3-Clause

from zlib import crc32
from uuid import uuid4

if __name__ == '__main__':
	from guids import GPT_PART_TYPES
else:
	from .guids import GPT_PART_TYPES


from construct import *

ASSUMED_BLOCK_SIZE = 512

"""

"""
guid = 'GUID' / Padded(16, Struct(
	'data0' / Hex(Int32ul),                        # ???
	'data1' / Hex(Int16ul),                        # ???
	'data2' / Hex(Int16ul),                        # ???
	'data3' / Hex(Int16ub),                        # ???
	'data4' / Bytes(6)                             # ???
))

"""

"""
partition_record = 'Partition Record' / Struct(
	'boot_indicator' / Const(b'\x00'),             # Boot indicator: 0x00
	'starting_chs'   / Hex(Bytes(3)),	           # Start of partition in CHS format
	'os_type'        / Hex(Bytes(1)),	           # Indicated Partition type
	'ending_chs'     / Hex(Bytes(3)),	           # End of partition in CHS format
	'starting_lba'   / Hex(Int32ul),	           # Starting LBA of the partition
	'size_in_lba'    / Hex(Int32ul),	           # Size of partition in LBA units
)

"""

"""
protective_mbr = 'Protective MBR' / Padded(ASSUMED_BLOCK_SIZE, Struct(
	'boot_code'      / Bytes(440),				   # boot code for non-UEFI system
	'disk_signature' / Const(b'\x00\x00\x00\x00'), # Unused, must be 0
	'reserved'       / Const(b'\x00\x00'),		   # Unused, must be 0
	'part_records'   / Array(4, partition_record), # Partition Records (*4)
	'signature'      / Const(b'\x55\xAA'),		   # Boot signature
))

"""

"""
gpt_header = 'GPT Header' / Padded(ASSUMED_BLOCK_SIZE, Struct(
	'signature'     / Const(b'EFI PART'),          # GPT Magic Signature
	'revision'      / Const(b'\x00\x00\x01\x00'),  # GPT Version
	'header_size'   / Hex(Int32ul),				   # 92 < GPT Header Size <=LBA Size
	'crc32'         / Hex(Int32ul),				   # CRC of header w/ this set to 0
	'reserved'      / Padding(4),                  # 4-byte reserved field
	'my_lba'        / Hex(Int64ul),				   # LBA of this header
	'alt_lba'       / Hex(Int64ul),                # LBA of backup header
	'fusable_lba'   / Hex(Int64ul),				   # First Usable LBA
	'luseable_lba'  / Hex(Int64ul),				   # Last Usable LBA
	'disk_guid'     / guid,						   # Disk GUID
	'part_end_lba'  / Hex(Int64ul),				   # Starting LBA of Partition table
	'part_count'    / Hex(Int32ul),				   # Number of Partition Entries
	'part_ent_size' / Hex(Int32ul),				   # Size of Partition Entries
	'part_ents_crc' / Hex(Int32ul),				   # Partition Array CRC32
))

"""

"""
gpt_entry = 'GPT Entry' / Struct(
	'type_guid'  / guid,						   # Partition Type GUID
	'part_guid'  / guid,						   # Partition GUID
	'start_lba'  / Hex(Int64ul),				   # Starting LBA for partition
	'end_lba'    / Hex(Int64ul),				   # Ending LBA for partition
	'attributes' / BitStruct(					   # Attributes bitfield
		'required'    / Flag,					   #  * This partition is required for platform to function
		'no_block_io' / Flag,                      #  * Firmware can not EFI_BLOCK_IO_PROTOCOL
		'legacy_boot' / Flag,                      #  * Possibly allow legacy boot?
		'reserved'    / Padding(45),               #  * Reserved for future flags
		'guid_res'    / BitsInteger(16)),          #  * Partition Type GUID specific use
	'name'       / PaddedString(72, 'utf16'),      # Partition Name
)

"""

"""
gpt_disk_image = 'GPT Disk Image' / Struct(
	'protective_mbr'   / protective_mbr,           # Guard MBR for GPT image        | LBA0
	'primary_pheader'  / gpt_header,               # Primary partition table header | LBA1
	'primary_pentries' / Array(
		this.primary_pheader.part_count,
		Padded(
			this.primary_pheader.part_ent_size,
			gpt_entry
		)
	),                                             # Partition Entries
	'disk_data' / LazyArray(
		(this.primary_pheader.luseable_lba + 1) - this.primary_pheader.fusable_lba,
		Bytes(ASSUMED_BLOCK_SIZE)
	),                                             # Disk Data

	'backup_pentries' / Array(
		this.primary_pheader.part_count,
		Padded(
			this.primary_pheader.part_ent_size,
			gpt_entry
		)
	),                                             # Backup Partition Entries
	'backup_pheader' / gpt_header                  # Backup GPT Header | LBAn
)



if __name__ == '__main__':
	def dump_img(file_name):
		with open(file_name, 'rb') as f:
			print(gpt_disk_image.parse(f.read()))

	import sys
	from os import path
	from argparse import ArgumentParser, ArgumentDefaultsHelpFormatter

	parser = ArgumentParser(
		prog = 'nya_umu',
		formatter_class = ArgumentDefaultsHelpFormatter,
		description = 'GPT test runner'
	)

	global_options = parser.add_argument_group('Global Options')

	global_options.add_argument(
		'--file', '-f',
		type = str,
		required = True,
		help = 'GPT image file to operate on',
	)

	global_options.add_argument(
		'--dump', '-d',
		action = 'store_true',
		default = False,
		help = 'Dump out the details of a GPT disk image'
	)

	args = parser.parse_args()

	if not path.exists(args.file):
		print(f'Unable to open file \'{args.file}\' does it exist?')
		sys.exit(1)

	if args.dump:
		sys.exit(dump_img(args.file))


	print('??? nya?')
	sys.exit(1)
