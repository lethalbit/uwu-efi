#!/usr/bin/env python
# SPDX-License-Identifier: BSD-3-Clause

if __name__ == '__main__':
	from guids import GPT_PART_TYPES
else:
	from .guids import GPT_PART_TYPES


from construct import *

guid = Padded(16, Struct(
	'data0' / Int32ul,
	'data1' / Int16ul,
	'data2' / Int16ul,
	'data3' / Int16ul,
	'data4' / Bytes(6)
))

partition_record = Struct(
	'boot_indicator' / Bytes(1), 		#	Boot indicator: 0x80 for bootable
	'starting_chs'   / Bytes(3),		#	Start of partition in CHS format
	'os_type'        / Bytes(1),		#	OS Type (0xEF or 0xEE)
	'ending_chs'     / Bytes(3),		# 	End of partition in CHS format
	'starting_lba'   / Int32ul,			# 	Starting LBA of the partition
	'size_in_lba'    / Int32ul,			#	Size of partition in LBA units
)

protective_mbr = Struct(
	'boot_code'      / Bytes(440),						# boot code for non-UEFI system
	'disk_signature' / Const(b'\x00\x00\x00\x00'),		# Unused, must be 0
	'reserved'       / Const(b'\x00\x00'),				# Unused, must be 0
	'part_records'   / Array(4, partition_record),		# Partition Records (*4)
	'signature'      / Const(b'\x55\xAA'),				# Boot signature
)

gpt_header = Padded(int(512), Struct(
	'signature'     / Const(b'\x54\x52\x41\x50\x20\x49\x46\x45'),
	'revision'      / Const(b'\x00\x01\x00\x00'),
	'header_size'   / Int32ul,
	'crc32'         / Int32ul,
	Padding(4),
	'my_lba'        / Int64ul,
	'alt_lba'       / Int64ul,
	'fusable_lba'   / Int64ul,
	'luseable_lba'  / Int64ul,
	'disk_guid'     / guid,
	'part_count'    / Int32ul,
	'part_ent_size' / Int32ul,
	'part_ents_crc' / Int32ul,
))



gpt_entry = Struct(
	'type_guid' / guid,
	'part_guid' / guid,
	'start_lba' / Int64ul,
	'end_lba'   / Int64ul,
	'name'      / PaddedString(72, 'utf8'),
)

gpt_disk_image = Struct(
	'mbr' / protective_mbr, # Guard MBR for GPT image
)

def mk_protective_mbr(*, lba_count, lba_size = 4096, last_block = b'\xFF\xFF\xFF', nest = False, pad = True):
	lba_padded_mbr = Padded(lba_size, protective_mbr)

	mbr_dict = {
		'boot_code': b'\x00' * 440,
		'part_records': [
			mk_protective_rec(
				lba_count  = lba_count,
				lba_size   = lba_size,
				last_block = last_block,
				nest       = True
			),
			mk_protective_rec(
				lba_count  = lba_count,
				lba_size   = lba_size,
				last_block = last_block,
				nest       = True
			),
			mk_protective_rec(
				lba_count  = lba_count,
				lba_size   = lba_size,
				last_block = last_block,
				nest       = True
			),
			mk_protective_rec(
				lba_count  = lba_count,
				lba_size   = lba_size,
				last_block = last_block,
				nest       = True
			),
		]
	}

	if not nest:
		if pad:
			return lba_padded_mbr.build(mbr_dict)
		else:
			return protective_mbr.build(mbr_dict)
	else:
		return mbr_dict

def mk_protective_rec(*, lba_count, lba_size = 4096, last_block = b'\xFF\xFF\xFF', nest = False):
	rec_dict = {
		'boot_indicator' : b'\x00',
		'starting_chs'   : b'\x00\x02\x00',
		'os_type'        : b'\xEE',
		'ending_chs'     : last_block,
		'starting_lba'   : 1,
		'size_in_lba'    : lba_count * lba_size
	}

	if not nest:
		return partition_record.build(rec_dict)
	else:
		return rec_dict



# def make_empty_gpt_image(*, lba_count, lba_size = 4096)


if __name__ == '__main__':
	def dump_img(file_name):
		return 0

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
