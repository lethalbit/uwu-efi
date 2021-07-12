# SPDX-License-Identifier: BSD-3-Clause
__all__ = (
	'guid', 

	'GPT_PART_TYPES',

	'UEFI_CORE_PART_TYPES'  , 'WINDOWS_PART_TYPES'  , 'HPUX_PART_TYPES'      ,
	'LINUX_PART_TYPES'      , 'FREEBSD_PART_TYPES'  , 'DARWIN_PART_TYPES'    ,
	'SOLARIS_PART_TYPES'    , 'NETBSD_PART_TYPES'   , 'CHROMEOS_PART_TYPES'  ,
	'COREOS_PART_TYPES'     , 'HAIKU_PART_TYPES'    , 'MIDNIGHT_PART_TYPES'  ,
	'CEPH_PART_TYPES'       , 'OPENBSD_PART_TYPES'  , 'QNX_PART_TYPES'       ,
	'PLAN9_PART_TYPES'      , 'VMWARE_PART_TYPES'   , 'ANDROID_IA_PART_TYPES',
	'ANDROID_ARM_PART_TYPES', 'ONIE_PART_TYPES'     , 'POWERPC_PART_TYPES'   ,
	'FREEDESKTOP_PART_TYPES', 'ATARI_TOS_PART_TYPES', 'VERACRYPT_PART_TYPES' ,
	'OS2_PART_TYPES'        , 'SPDK_PART_TYPES'     , 'BAREBOX_PART_TYPES'   ,
)

UEFI_CORE_PART_TYPES = {
	'unused' : { # Unused GPT Partition
		'data0': 0x00000000, 'data1': 0x0000,
		'data2': 0x0000    , 'data3': 0x0000,
		'data4': b'\x00\x00\x00\x00\x00\x00'
	},
	'esp'    : { # EFI System Partition
		'data0': 0xC12A7328, 'data1': 0xF81F,
		'data2': 0x11D2    , 'data3': 0xBA4B,
		'data4': b'\x00\xA0\xC9\x3E\xC9\x3B'
	},
	'mbr'    : { # Legacy MBR Partition
		'data0': 0x024DEE41, 'data1': 0x33E7,
		'data2': 0x11D3    , 'data3': 0x9D69,
		'data4': b'\x00\x08\xC7\x81\xF3\x9F'
	},
	'bios'   : { # BIOS boot partition
		'data0': 0x21686148, 'data1': 0x6449,
		'data2': 0x6E6F    , 'data3': 0x744E,
		'data4': b'\x65\x65\x64\x45\x46\x49'
	},
	'iffs'   : { # Intel Fast Flash (iFFS) partition (for Intel Rapid Start technology)
		'data0': 0xD3BFE2DE, 'data1': 0x3DAF,
		'data2': 0x11DF    , 'data3': 0xBA40,
		'data4': b'\xE3\xA5\x56\xD8\x95\x93'
	},
	'sony'   : { # Sony boot partition
		'data0': 0xF4019732, 'data1': 0x066E,
		'data2': 0x4E12    , 'data3': 0x8273,
		'data4': b'\x34\x6C\x56\x41\x49\x4F'
	},
	'lenovo' : { # Lenovo boot partition
		'data0': 0xBFBFAFE7, 'data1': 0xA34F,
		'data2': 0x448A    , 'data3': 0x9A5B,
		'data4': b'\x62\x13\xEB\x73\x6C\x22'
	},
}

WINDOWS_PART_TYPES = {
	'msr'    : { # Microsoft Reserved Partition (MSR)
		'data0': 0xE3C9E316, 'data1': 0x0B5C,
		'data2': 0x4DB8    , 'data3': 0x817D,
		'data4': b'\xF9\x2D\xF0\x02\x15\xAE'
	},
	'bdp'    : { # Basic data partition
		'data0': 0xEBD0A0A2, 'data1': 0xB9E5,
		'data2': 0x4433    , 'data3': 0x87C0,
		'data4': b'\x68\xB6\xB7\x26\x99\xC7'
	},
	'ldmmeta': { # Logical Disk Manager (LDM) metadata partition
		'data0': 0x5808C8AA, 'data1': 0x7E8F,
		'data2': 0x42E0    , 'data3': 0x85D2,
		'data4': b'\xE1\xE9\x04\x34\xCF\xB3'
	},
	'ldm'    : { # Logical Disk Manager data partition
		'data0': 0xAF9B60A0, 'data1': 0x1431,
		'data2': 0x4F62    , 'data3': 0xBC68,
		'data4': b'\x33\x11\x71\x4A\x69\xAD'
	},
	'recover': { # Windows Recovery Environment
		'data0': 0xDE94BBA4, 'data1': 0x06D1,
		'data2': 0x4D40    , 'data3': 0xA16A,
		'data4': b'\xBF\xD5\x01\x79\xD6\xAC'
	},
	'gpfs'   : { # IBM General Parallel File System (GPFS) partition
		'data0': 0x37AFFC90, 'data1': 0xEF7D,
		'data2': 0x4E96    , 'data3': 0x91C3,
		'data4': b'\x2D\x7A\xE0\x55\xB1\x74'
	},
	'sspace' : { # Storage Spaces partition
		'data0': 0xE75CAF8F, 'data1': 0xF680,
		'data2': 0x4CEE    , 'data3': 0xAFA3,
		'data4': b'\xB0\x01\xE5\x6E\xFC\x2D'
	},
	'sreplic': { # Storage Replica partition
		'data0': 0x558D43C5, 'data1': 0xA1AC,
		'data2': 0x43C0    , 'data3': 0xAAC8,
		'data4': b'\xD1\x47\x2B\x29\x23\xD1'
	},
}

HPUX_PART_TYPES = {
	'data'   : { # Data partition
		'data0': 0x75894C1E, 'data1': 0x3AEB,
		'data2': 0x11D3    , 'data3': 0xB7C1,
		'data4': b'\x7B\x03\xA0\x00\x00\x00'
	},
	'service': { # Service partition
		'data0': 0xE2A1E728, 'data1': 0x32E3,
		'data2': 0x11D6    , 'data3': 0xA682,
		'data4': b'\x7B\x03\xA0\x00\x00\x00'
	},
}

LINUX_PART_TYPES = {
	'lfsd'   : { # Linux filesystem data
		'data0': 0x0FC63DAF, 'data1': 0x8483,
		'data2': 0x4772    , 'data3': 0x8E79,
		'data4': b'\x3D\x69\xD8\x47\x7D\xE4'
	},
	'raid'   : { # RAID partition
		'data0': 0xA19D880F, 'data1': 0x05FC,
		'data2': 0x4D3B    , 'data3': 0x0000,
		'data4': b'\x74\x3F\x0F\x84\x91\x1E'
	},
	'rootx32': { # Root partition (x86)
		'data0': 0x44479540, 'data1': 0xF297,
		'data2': 0x41B2    , 'data3': 0x0000,
		'data4': b'\xD1\x31\xD5\xF0\x45\x8A'
	},
	'rootx64': { # Root partition (x86-64)
		'data0': 0x4F68BCE3, 'data1': 0xE8CD,
		'data2': 0x4DB1    , 'data3': 0x0000,
		'data4': b'\xFB\xCA\xF9\x84\xB7\x09'
	},
	'roota32': { # Root partition (32-bit ARM)
		'data0': 0x69DAD710, 'data1': 0x2CE4,
		'data2': 0x4E3C    , 'data3': 0x0000,
		'data4': b'\x21\xA1\xD4\x9A\xBE\xD3'
	},
	'roota64': { # Root partition (64-bit ARM/AArch64)
		'data0': 0xB921B045, 'data1': 0x1DF0,
		'data2': 0x41C3    , 'data3': 0x0000,
		'data4': b'\x4C\x6F\x28\x0D\x3F\xAE'
	},
	'boot'   : { # /boot partition
		'data0': 0xBC13C2FF, 'data1': 0x59E6,
		'data2': 0x4262    , 'data3': 0x0000,
		'data4': b'\xB2\x75\xFD\x6F\x71\x72'
	},
	'swap'   : { # Swap partition
		'data0': 0x0657FD6D, 'data1': 0xA4AB,
		'data2': 0x43C4    , 'data3': 0x0000,
		'data4': b'\x09\x33\xC8\x4B\x4F\x4F'
	},
	'lvm'    : { # Logical Volume Manager (LVM) partition
		'data0': 0xE6D6D379, 'data1': 0xF507,
		'data2': 0x44C2    , 'data3': 0x0000,
		'data4': b'\x23\x8F\x2A\x3D\xF9\x28'
	},
	'home'   : { # /home partition
		'data0': 0x933AC7E1, 'data1': 0x2EB4,
		'data2': 0x4F13    , 'data3': 0x0000,
		'data4': b'\x0E\x14\xE2\xAE\xF9\x15'
	},
	'srv'    : { # /srv (server data) partition
		'data0': 0x3B8F8425, 'data1': 0x20E0,
		'data2': 0x4F3B    , 'data3': 0x0000,
		'data4': b'\x1A\x25\xA7\x6F\x98\xE8'
	},
	'dmcrypt': { # Plain dm-crypt partition
		'data0': 0x7FFEC5C9, 'data1': 0x2D00,
		'data2': 0x49B7    , 'data3': 0x0000,
		'data4': b'\x3E\xA1\x0A\x55\x86\xB7'
	},
	'luks'   : { # LUKS partition
		'data0': 0xCA7D7CCB, 'data1': 0x63ED,
		'data2': 0x4C53    , 'data3': 0x0000,
		'data4': b'\x17\x42\x53\x60\x59\xCC'
	},
	'res'    : { # Reserved
		'data0': 0x8DA63339, 'data1': 0x0007,
		'data2': 0x60C0    , 'data3': 0x0000,
		'data4': b'\x08\x3A\xC8\x23\x09\x08'
	},
}

FREEBSD_PART_TYPES = {
	'boot'   : { # Boot partition
		'data0': 0x83BD6B9D, 'data1': 0x7F41,
		'data2': 0x11DC    , 'data3': 0xBE0B,
		'data4': b'\x00\x15\x60\xB8\x4F\x0F'
	},
	'data'   : { # Data partition
		'data0': 0x516E7CB4, 'data1': 0x6ECF,
		'data2': 0x11D6    , 'data3': 0x8FF8,
		'data4': b'\x00\x02\x2D\x09\x71\x2B'
	},
	'swap'   : { # Swap partition
		'data0': 0x516E7CB5, 'data1': 0x6ECF,
		'data2': 0x11D6    , 'data3': 0x8FF8,
		'data4': b'\x00\x02\x2D\x09\x71\x2B'
	},
	'ufs'    : { # Unix File System (UFS) partition
		'data0': 0x516E7CB6, 'data1': 0x6ECF,
		'data2': 0x11D6    , 'data3': 0x8FF8,
		'data4': b'\x00\x02\x2D\x09\x71\x2B'
	},
	'vinum'  : { # Vinum volume manager partition
		'data0': 0x516E7CB8, 'data1': 0x6ECF,
		'data2': 0x11D6    , 'data3': 0x8FF8,
		'data4': b'\x00\x02\x2D\x09\x71\x2B'
	},
	'zfs'    : { # ZFS partition
		'data0': 0x516E7CBA, 'data1': 0x6ECF,
		'data2': 0x11D6    , 'data3': 0x8FF8,
		'data4': b'\x00\x02\x2D\x09\x71\x2B'
	},
}

DARWIN_PART_TYPES = {
	'hfs'    : { # Hierarchical File System Plus (HFS+) partition
		'data0': 0x48465300, 'data1': 0x0000,
		'data2': 0x11AA    , 'data3': 0xAA11,
		'data4': b'\x00\x30\x65\x43\xEC\xAC'
	},
	'apfs'   : { # Apple APFS container / APFS FileVault volume container
		'data0': 0x7C3457EF, 'data1': 0x0000,
		'data2': 0x11AA    , 'data3': 0xAA11,
		'data4': b'\x00\x30\x65\x43\xEC\xAC'
	},
	'ufs'    : { # Apple UFS container
		'data0': 0x55465300, 'data1': 0x0000,
		'data2': 0x11AA    , 'data3': 0xAA11,
		'data4': b'\x00\x30\x65\x43\xEC\xAC'
	},
	'zfs'    : { # ZFS
		'data0': 0x6A898CC3, 'data1': 0x1DD2,
		'data2': 0x11B2    , 'data3': 0x99A6,
		'data4': b'\x08\x00\x20\x73\x66\x31'
	},
	'araid'  : { # Apple RAID partition
		'data0': 0x52414944, 'data1': 0x0000,
		'data2': 0x11AA    , 'data3': 0xAA11,
		'data4': b'\x00\x30\x65\x43\xEC\xAC'
	},
	'araid_o': { # Apple RAID partition, offline
		'data0': 0x52414944, 'data1': 0x5F4F,
		'data2': 0x11AA    , 'data3': 0xAA11,
		'data4': b'\x00\x30\x65\x43\xEC\xAC'
	},
	'boot'   : { # Apple Boot partition (Recovery HD)
		'data0': 0x426F6F74, 'data1': 0x0000,
		'data2': 0x11AA    , 'data3': 0xAA11,
		'data4': b'\x00\x30\x65\x43\xEC\xAC'
	},
	'label'  : { # Apple Label
		'data0': 0x4C616265, 'data1': 0x6C00,
		'data2': 0x11AA    , 'data3': 0xAA11,
		'data4': b'\x00\x30\x65\x43\xEC\xAC'
	},
	'tv'     : { # Apple TV Recovery partition
		'data0': 0x5265636F, 'data1': 0x7665,
		'data2': 0x11AA    , 'data3': 0xAA11,
		'data4': b'\x00\x30\x65\x43\xEC\xAC'
	},
	'core'   : { # Apple Core Storage Container / HFS+ FileVault volume container
		'data0': 0x53746F72, 'data1': 0x6167,
		'data2': 0x11AA    , 'data3': 0xAA11,
		'data4': b'\x00\x30\x65\x43\xEC\xAC'
	},
	'sr_stat': { # SoftRAID_Status
		'data0': 0xB6FA30DA, 'data1': 0x92D2,
		'data2': 0x4A9A    , 'data3': 0x96F1,
		'data4': b'\x87\x1E\xC6\x48\x62\x00'
	},
	'sr_scra': { # SoftRAID_Scratch
		'data0': 0x2E313465, 'data1': 0x19B9,
		'data2': 0x463F    , 'data3': 0x8126,
		'data4': b'\x8A\x79\x93\x77\x38\x01'
	},
	'sr_vol' : { # SoftRAID_Volume
		'data0': 0xFA709C7E, 'data1': 0x65B1,
		'data2': 0x4593    , 'data3': 0xBFD5,
		'data4': b'\xE7\x1D\x61\xDE\x9B\x02'
	},
	'sr_cach': { # SoftRAID_Cache
		'data0': 0xBBBA6DF5, 'data1': 0xF46F,
		'data2': 0x4A89    , 'data3': 0x8F59,
		'data4': b'\x87\x65\xB2\x72\x75\x03'
	},
}

SOLARIS_PART_TYPES = {
	'boot'   : { # Boot partition
		'data0': 0x6A82CB45, 'data1': 0x1DD2,
		'data2': 0x11B2    , 'data3': 0x99A6,
		'data4': b'\x08\x00\x20\x73\x66\x31'
	},
	'root'   : { # Root partition
		'data0': 0x6A85CF4D, 'data1': 0x1DD2,
		'data2': 0x11B2    , 'data3': 0x99A6,
		'data4': b'\x08\x00\x20\x73\x66\x31'
	},
	'swap'   : { # Swap partition
		'data0': 0x6A87C46F, 'data1': 0x1DD2,
		'data2': 0x11B2    , 'data3': 0x99A6,
		'data4': b'\x08\x00\x20\x73\x66\x31'
	},
	'backup' : { # Backup partition
		'data0': 0x6A8B642B, 'data1': 0x1DD2,
		'data2': 0x11B2    , 'data3': 0x99A6,
		'data4': b'\x08\x00\x20\x73\x66\x31'
	},
	'usr'    : { # /usr partition
		'data0': 0x6A898CC3, 'data1': 0x1DD2,
		'data2': 0x11B2    , 'data3': 0x99A6,
		'data4': b'\x08\x00\x20\x73\x66\x31'
	},
	'var'    : { # /var partition
		'data0': 0x6A8EF2E9, 'data1': 0x1DD2,
		'data2': 0x11B2    , 'data3': 0x99A6,
		'data4': b'\x08\x00\x20\x73\x66\x31'
	},
	'home'   : { # /home partition
		'data0': 0x6A90BA39, 'data1': 0x1DD2,
		'data2': 0x11B2    , 'data3': 0x99A6,
		'data4': b'\x08\x00\x20\x73\x66\x31'
	},
	'alt'    : { # Alternate sector
		'data0': 0x6A9283A5, 'data1': 0x1DD2,
		'data2': 0x11B2    , 'data3': 0x99A6,
		'data4': b'\x08\x00\x20\x73\x66\x31'
	},
	'res1'   : { # Reserved partition
		'data0': 0x6A945A3B, 'data1': 0x1DD2,
		'data2': 0x11B2    , 'data3': 0x99A6,
		'data4': b'\x08\x00\x20\x73\x66\x31'
	},
	'res2'   : { # Reserved partition
		'data0': 0x6A9630D1, 'data1': 0x1DD2,
		'data2': 0x11B2    , 'data3': 0x99A6,
		'data4': b'\x08\x00\x20\x73\x66\x31'
	},
	'res3'   : { # Reserved partition
		'data0': 0x6A980767, 'data1': 0x1DD2,
		'data2': 0x11B2    , 'data3': 0x99A6,
		'data4': b'\x08\x00\x20\x73\x66\x31'
	},
	'res4'   : { # Reserved partition
		'data0': 0x6A96237F, 'data1': 0x1DD2,
		'data2': 0x11B2    , 'data3': 0x99A6,
		'data4': b'\x08\x00\x20\x73\x66\x31'
	},
	'res5'   : { # Reserved partition
		'data0': 0x6A8D2AC7, 'data1': 0x1DD2,
		'data2': 0x11B2    , 'data3': 0x99A6,
		'data4': b'\x08\x00\x20\x73\x66\x31'
	},
}

NETBSD_PART_TYPES = {
	'swap'   : { # Swap partition
		'data0': 0x49F48D32, 'data1': 0xB10E,
		'data2': 0x11DC    , 'data3': 0xB99B,
		'data4': b'\x00\x19\xD1\x87\x96\x48'
	},
	'ffs'    : { # FFS partition
		'data0': 0x49F48D5A, 'data1': 0xB10E,
		'data2': 0x11DC    , 'data3': 0xB99B,
		'data4': b'\x00\x19\xD1\x87\x96\x48'
	},
	'lfs'    : { # LFS partition
		'data0': 0x49F48D82, 'data1': 0xB10E,
		'data2': 0x11DC    , 'data3': 0xB99B,
		'data4': b'\x00\x19\xD1\x87\x96\x48'
	},
	'raid'   : { # RAID partition
		'data0': 0x49F48DAA, 'data1': 0xB10E,
		'data2': 0x11DC    , 'data3': 0xB99B,
		'data4': b'\x00\x19\xD1\x87\x96\x48'
	},
	'cat'    : { # Concatenated partition
		'data0': 0x2DB519C4, 'data1': 0xB10F,
		'data2': 0x11DC    , 'data3': 0xB99B,
		'data4': b'\x00\x19\xD1\x87\x96\x48'
	},
	'enc'    : { # Encrypted partition
		'data0': 0x2DB519EC, 'data1': 0xB10F,
		'data2': 0x11DC    , 'data3': 0xB99B,
		'data4': b'\x00\x19\xD1\x87\x96\x48'
	},
}

CHROMEOS_PART_TYPES = {
	'kernel' : { # Chrome OS kernel
		'data0': 0xFE3A2A5D, 'data1': 0x4F32,
		'data2': 0x41A7    , 'data3': 0xB725,
		'data4': b'\xAC\xCC\x32\x85\xA3\x09'
	},
	'root'   : { # Chrome OS rootfs
		'data0': 0x3CB8E202, 'data1': 0x3B7E,
		'data2': 0x47DD    , 'data3': 0x8A3C,
		'data4': b'\x7F\xF2\xA1\x3C\xFC\xEC'
	},
	'future' : { # Chrome OS future use
		'data0': 0x2E0A753D, 'data1': 0x9E48,
		'data2': 0x43B0    , 'data3': 0x8337,
		'data4': b'\xB1\x51\x92\xCB\x1B\x5E'
	},
}

COREOS_PART_TYPES = {
	'usr'    : { # /usr partition (coreos-usr)
		'data0': 0x5DFBF5F4, 'data1': 0x2848,
		'data2': 0x4BAC    , 'data3': 0xAA5E,
		'data4': b'\x0D\x9A\x20\xB7\x45\xA6'
	},
	'root'   : { # Resizable rootfs (coreos-resize)
		'data0': 0x3884DD41, 'data1': 0x8582,
		'data2': 0x4404    , 'data3': 0xB9A8,
		'data4': b'\xE9\xB8\x4F\x2D\xF5\x0E'
	},
	'oem'    : { # OEM customizations (coreos-reserved)
		'data0': 0xC95DC21A, 'data1': 0xDF0E,
		'data2': 0x4340    , 'data3': 0x8D7B,
		'data4': b'\x26\xCB\xFA\x9A\x03\xE0'
	},
	'rroot'  : { # Root filesystem on RAID (coreos-root-raid)
		'data0': 0xBE9067B9, 'data1': 0xEA49,
		'data2': 0x4F15    , 'data3': 0xB4F6,
		'data4': b'\xF3\x6F\x8C\x9E\x18\x18'
	},
}

HAIKU_PART_TYPES = {
	'bfs'    : { # 	Haiku BFS
		'data0': 0x42465331, 'data1': 0x3BA3,
		'data2': 0x10F1    , 'data3': 0x802A,
		'data4': b'\x48\x61\x69\x6B\x75\x21'
	},
}

MIDNIGHT_PART_TYPES = {
	'boot'   : { # Boot partition
		'data0': 0x85D5E45E, 'data1': 0x237C,
		'data2': 0x11E1    , 'data3': 0xB4B3,
		'data4': b'\xE8\x9A\x8F\x7F\xC3\xA7'
	},
	'data'   : { # Data partition
		'data0': 0x85D5E45A, 'data1': 0x237C,
		'data2': 0x11E1    , 'data3': 0xB4B3,
		'data4': b'\xE8\x9A\x8F\x7F\xC3\xA7'
	},
	'swap'   : { # Swap partition
		'data0': 0x85D5E45B, 'data1': 0x237C,
		'data2': 0x11E1    , 'data3': 0xB4B3,
		'data4': b'\xE8\x9A\x8F\x7F\xC3\xA7'
	},
	'ufs'    : { # Unix File System (UFS) partition
		'data0': 0x0394EF8B, 'data1': 0x237E,
		'data2': 0x11E1    , 'data3': 0xB4B3,
		'data4': b'\xE8\x9A\x8F\x7F\xC3\xA7'
	},
	'vinum'  : { # Vinum volume manager partition
		'data0': 0x85D5E45C, 'data1': 0x237C,
		'data2': 0x11E1    , 'data3': 0xB4B3,
		'data4': b'\xE8\x9A\x8F\x7F\xC3\xA7'
	},
	'zfs'    : { # ZFS partition
		'data0': 0x85D5E45D, 'data1': 0x237C,
		'data2': 0x11E1    , 'data3': 0xB4B3,
		'data4': b'\xE8\x9A\x8F\x7F\xC3\xA7'
	},
}

CEPH_PART_TYPES = {
	'journ'  : { # Journal
		'data0': 0x45B0969E, 'data1': 0x9B03,
		'data2': 0x0000    , 'data3': 0xB4C6,
		'data4': b'\xB4\xB8\x0C\xEF\xF1\x06'
	},
	'djourn' : { # dm-crypt journal
		'data0': 0x45B0969E, 'data1': 0x9B03,
		'data2': 0x4F30    , 'data3': 0xB4C6,
		'data4': b'\x5E\xC0\x0C\xEF\xF1\x06'
	},
	'osd'    : { # OSD
		'data0': 0x4FBD7E29, 'data1': 0x9D25,
		'data2': 0x4F30    , 'data3': 0xAFD0,
		'data4': b'\x06\x2C\x0C\xEF\xF0\x5D'
	},
	'dosd'   : { # dm-crypt OSD
		'data0': 0x4FBD7E29, 'data1': 0x9D25,
		'data2': 0x41B8    , 'data3': 0xAFD0,
		'data4': b'\x5E\xC0\x0C\xEF\xF0\x5D'
	},
	'dic'    : { # Disk in creation
		'data0': 0x89C57F98, 'data1': 0x2FE5,
		'data2': 0x41B8    , 'data3': 0x89C1,
		'data4': b'\xF3\xAD\x0C\xEF\xF2\xBE'
	},
	'ddic'   : { # dm-crypt disk in creation
		'data0': 0x89C57F98, 'data1': 0x2FE5,
		'data2': 0x4DC0    , 'data3': 0x89C1,
		'data4': b'\x5E\xC0\x0C\xEF\xF2\xBE'
	},
	'block'  : { # Block
		'data0': 0xCAFECAFE, 'data1': 0x9B03,
		'data2': 0x4DC0    , 'data3': 0xB4C6,
		'data4': b'\xB4\xB8\x0C\xEF\xF1\x06'
	},
	'blkdb'  : { # Block DB
		'data0': 0x30CD0809, 'data1': 0xC2B2,
		'data2': 0x4F30    , 'data3': 0x8879,
		'data4': b'\x2D\x6B\x78\x52\x98\x76'
	},
	'bwal'   : { # Block write-ahead log
		'data0': 0x5CE17FCE, 'data1': 0x4087,
		'data2': 0x499C    , 'data3': 0xB7FF,
		'data4': b'\x05\x6C\xC5\x84\x73\xF9'
	},
	'dlwkbx' : { # Lockbox for dm-crypt keys
		'data0': 0xFB3AABF9, 'data1': 0xD25F,
		'data2': 0x4169    , 'data3': 0xBF5E,
		'data4': b'\x72\x1D\x18\x16\x49\x6B'
	},
	'mosd'   : { # Multipath OSD
		'data0': 0x4FBD7E29, 'data1': 0x8AE0,
		'data2': 0x47CC    , 'data3': 0xBF9D,
		'data4': b'\x5A\x8D\x86\x7A\xF5\x60'
	},
	'mjourn' : { # Multipath journal
		'data0': 0x45B0969E, 'data1': 0x8AE0,
		'data2': 0x4982    , 'data3': 0xBF9D,
		'data4': b'\x5A\x8D\x86\x7A\xF5\x60'
	},
	'mblock1': { # Multipath block
		'data0': 0xCAFECAFE, 'data1': 0x8AE0,
		'data2': 0x4982    , 'data3': 0xBF9D,
		'data4': b'\x5A\x8D\x86\x7A\xF5\x60'
	},
	'mblock2': { # Multipath block
		'data0': 0x7F4A666A, 'data1': 0x16F3,
		'data2': 0x4982    , 'data3': 0x8445,
		'data4': b'\x15\x2E\xF4\xD0\x3F\x6C'
	},
	'mblkdb' : { # Multipath block DB
		'data0': 0xEC6D6385, 'data1': 0xE346,
		'data2': 0x47A2    , 'data3': 0xBE91,
		'data4': b'\xDA\x2A\x7C\x8B\x32\x61'
	},
	'mbwal'  : { # Multipath block write-ahead log
		'data0': 0x01B41E1B, 'data1': 0x002A,
		'data2': 0x45DC    , 'data3': 0x9F17,
		'data4': b'\x88\x79\x39\x89\xFF\x8F'
	},
	'dblock' : { # dm-crypt block
		'data0': 0xCAFECAFE, 'data1': 0x9B03,
		'data2': 0x0000    , 'data3': 0xB4C6,
		'data4': b'\x5E\xC0\x0C\xEF\xF1\x06'
	},
	'dblkdb' : { # dm-crypt block DB
		'data0': 0x93B0052D, 'data1': 0x02D9,
		'data2': 0x453C    , 'data3': 0xA43B,
		'data4': b'\x33\xA3\xEE\x4D\xFB\xC3'
	},
	'dbwal'  : { # dm-crypt block write-ahead log
		'data0': 0x306E8683, 'data1': 0x4FE2,
		'data2': 0x4F30    , 'data3': 0xB7C0,
		'data4': b'\x00\xA9\x17\xC1\x69\x66'
	},
	'ljourn' : { # dm-crypt LUKS journal
		'data0': 0x45B0969E, 'data1': 0x9B03,
		'data2': 0x4D8A    , 'data3': 0xB4C6,
		'data4': b'\x35\x86\x5C\xEF\xF1\x06'
	},
	'lblock' : { # dm-crypt LUKS block
		'data0': 0xCAFECAFE, 'data1': 0x9B03,
		'data2': 0x4330    , 'data3': 0xB4C6,
		'data4': b'\x35\x86\x5C\xEF\xF1\x06'
	},
	'lblkdb' : { # dm-crypt LUKS block DB
		'data0': 0x166418DA, 'data1': 0xC469,
		'data2': 0x4022    , 'data3': 0xADF4,
		'data4': b'\xB3\x0A\xFD\x37\xF1\x76'
	},
	'lbwal'  : { # dm-crypt LUKS block write-ahead log
		'data0': 0x86A32090, 'data1': 0x3647,
		'data2': 0x40B9    , 'data3': 0xBBBD,
		'data4': b'\x38\xD8\xC5\x73\xAA\x86'
	},
	'losd'   : { # dm-crypt LUKS OSD
		'data0': 0x4FBD7E29, 'data1': 0x9D25,
		'data2': 0x41B8    , 'data3': 0xAFD0,
		'data4': b'\x35\x86\x5C\xEF\xF0\x5D'
	},
}

OPENBSD_PART_TYPES = {
	'data'   : { # Data Partition
		'data0': 0x824CC7A0, 'data1': 0x36A8,
		'data2': 0x11E3    , 'data3': 0x890A,
		'data4': b'\x95\x25\x19\xAD\x3F\x61'
	},
}

QNX_PART_TYPES = {
	'qnx6'   : { # Power-safe (QNX6) Filesystem
		'data0': 0xCEF5A9AD, 'data1': 0x73BC,
		'data2': 0x4601    , 'data3': 0x89F3,
		'data4': b'\xCD\xEE\xEE\xE3\x21\xA1'
	},
}

PLAN9_PART_TYPES = {
	'part'   : { # Plan9 Partition
		'data0': 0xC91818F9, 'data1': 0x8025,
		'data2': 0x47AF    , 'data3': 0x89D2,
		'data4': b'\xF0\x30\xD7\x00\x0C\x2C'
	},
}

VMWARE_PART_TYPES = {
	'core'   : { # vmkcore Coredump partition
		'data0': 0x9D275380, 'data1': 0x40AD,
		'data2': 0x11DB    , 'data3': 0xBF97,
		'data4': b'\x00\x0C\x29\x11\xD1\xB8'
	},
	'vmfs'   : { # VMFS Filesystem Partition
		'data0': 0xAA31E02A, 'data1': 0x400F,
		'data2': 0x11DB    , 'data3': 0x9590,
		'data4': b'\x00\x0C\x29\x11\xD1\xB8'
	},
	'res'    : { # VMWareReserved
		'data0': 0x9198EFFC, 'data1': 0x31C0,
		'data2': 0x11DB    , 'data3': 0x8F78,
		'data4': b'\x00\x0C\x29\x11\xD1\xB8'
	},
}

ANDROID_IA_PART_TYPES = {
	'bootl1'   : { # Android Bootloader 1
		'data0': 0x2568845D, 'data1': 0x2332,
		'data2': 0x4675    , 'data3': 0xBC39,
		'data4': b'\x8F\xA5\xA4\x74\x8D\x15'
	},
	'bootl2' : { # Android Bootloader 2
		'data0': 0x114EAFFE, 'data1': 0x1552,
		'data2': 0x4022    , 'data3': 0xB26E,
		'data4': b'\x9B\x05\x36\x04\xCF\x84'
	},
	'boot'   : { # Android Boot
		'data0': 0x49A4D17F, 'data1': 0x93A3,
		'data2': 0x45C1    , 'data3': 0xA0DE,
		'data4': b'\xF5\x0B\x2E\xBE\x25\x99'
	},
	'recover': { # Android Recovery
		'data0': 0x4177C722, 'data1': 0x9E92,
		'data2': 0x4AAB    , 'data3': 0x8644,
		'data4': b'\x43\x50\x2B\xFD\x55\x06'
	},
	'misc'   : { # Android Miscellaneous
		'data0': 0xEF32A33B, 'data1': 0xA409,
		'data2': 0x486C    , 'data3': 0x9141,
		'data4': b'\x9F\xFB\x71\x1F\x62\x66'
	},
	'meta'   : { # Android Metadata
		'data0': 0x20AC26BE, 'data1': 0x20B7,
		'data2': 0x11E3    , 'data3': 0x84C5,
		'data4': b'\x6C\xFD\xB9\x47\x11\xE9'
	},
	'system' : { # Android System
		'data0': 0x38F428E6, 'data1': 0xD326,
		'data2': 0x425D    , 'data3': 0x9140,
		'data4': b'\x6E\x0E\xA1\x33\x64\x7C'
	},
	'cache'  : { # Android Cache
		'data0': 0xA893EF21, 'data1': 0xE428,
		'data2': 0x470A    , 'data3': 0x9E55,
		'data4': b'\x06\x68\xFD\x91\xA2\xD9'
	},
	'data'   : { # Android Data
		'data0': 0xDC76DDA9, 'data1': 0x5AC1,
		'data2': 0x491C    , 'data3': 0xAF42,
		'data4': b'\xA8\x25\x91\x58\x0C\x0D'
	},
	'persist': { # Android Persistent
		'data0': 0xEBC597D0, 'data1': 0x2053,
		'data2': 0x4B15    , 'data3': 0x8B64,
		'data4': b'\xE0\xAA\xC7\x5F\x4D\xB1'
	},
	'vendor' : { # Android Vendor
		'data0': 0xC5A0AEEC, 'data1': 0x13EA,
		'data2': 0x11E5    , 'data3': 0xA1B1,
		'data4': b'\x00\x1E\x67\xCA\x0C\x3C'
	},
	'config' : { # Android Config
		'data0': 0xBD59408B, 'data1': 0x4514,
		'data2': 0x490D    , 'data3': 0xBF12,
		'data4': b'\x98\x78\xD9\x63\xF3\x78'
	},
	'fact'   : { # Android Factory
		'data0': 0x8F68CC74, 'data1': 0xC5E5,
		'data2': 0x48DA    , 'data3': 0xBE91,
		'data4': b'\xA0\xC8\xC1\x5E\x9C\x80'
	},
	'factalt': { # Android Factory (alt)
		'data0': 0x9FDAA6EF, 'data1': 0x4B3F,
		'data2': 0x40D2    , 'data3': 0xBA8D,
		'data4': b'\xBF\xF1\x6B\xFB\x88\x7B'
	},
	'fboot'  : { # Android Fastboot / Tertiary
		'data0': 0x767941D0, 'data1': 0x2085,
		'data2': 0x11E3    , 'data3': 0xAD3B,
		'data4': b'\x6C\xFD\xB9\x47\x11\xE9'
	},
	'oem'    : { # Android OEM
		'data0': 0xAC6D7924, 'data1': 0xEB71,
		'data2': 0x4DF8    , 'data3': 0xB48D,
		'data4': b'\xE2\x67\xB2\x71\x48\xFF'
	},
}

ANDROID_ARM_PART_TYPES = {
	'meta'   : { # Android Meta
		'data0': 0x19A710A2, 'data1': 0xB3CA,
		'data2': 0x11E4    , 'data3': 0xB026,
		'data4': b'\x10\x60\x4B\x88\x9D\xCF'
	},
	'ext'    : { # Android EXT
		'data0': 0x193D1EA4, 'data1': 0xB3CA,
		'data2': 0x11E4    , 'data3': 0xB075,
		'data4': b'\x10\x60\x4B\x88\x9D\xCF'
	},
}

ONIE_PART_TYPES = {
	'boot'   : { # Boot
		'data0': 0x7412F7D5, 'data1': 0xA156,
		'data2': 0x4B13    , 'data3': 0x81DC,
		'data4': b'\x86\x71\x74\x92\x93\x25'
	},
	'config' : { # Config
		'data0': 0xD4E6E2CD, 'data1': 0x4469,
		'data2': 0x46F3    , 'data3': 0xB5CB,
		'data4': b'\x1B\xFF\x57\xAF\xC1\x49'
	},
}

POWERPC_PART_TYPES = {
	'boot'   : { # PReP boot
		'data0': 0x9E1A2D38, 'data1': 0xC612,
		'data2': 0x4316    , 'data3': 0xAA26,
		'data4': b'\x8B\x49\x52\x1E\x5A\x8B'
	},
}

FREEDESKTOP_PART_TYPES = {
	'boot'   : { # Shared boot loader config
		'data0': 0xBC13C2FF, 'data1': 0x59E6,
		'data2': 0x4262    , 'data3': 0xA352,
		'data4': b'\xB2\x75\xFD\x6F\x71\x72'
	},
}

ATARI_TOS_PART_TYPES = {
	'data'   : { # Basic Data Partition (GME, BGM, F32)
		'data0': 0x734E5AFE, 'data1': 0xF61A,
		'data2': 0x11E6    , 'data3': 0xBC64,
		'data4': b'\x92\x36\x1F\x00\x26\x71'
	},
}

VERACRYPT_PART_TYPES = {
	'data'   : { # Encrypted data partition
		'data0': 0x8C8F8EFF, 'data1': 0xAC95,
		'data2': 0x4770    , 'data3': 0x814A,
		'data4': b'\x21\x99\x4F\x2D\xBC\x8F'
	},
}

OS2_PART_TYPES = {
	'type1'  : { # ArcaOS Type 1
		'data0': 0x90B6FF38, 'data1': 0xB98F,
		'data2': 0x4358    , 'data3': 0xA21F,
		'data4': b'\x48\xF3\x5B\x4A\x8A\xD3'
	},
}

SPDK_PART_TYPES = {
	'block'  : { # SPDK Block Device
		'data0': 0x7C5222BD, 'data1': 0x8F5D,
		'data2': 0x4087    , 'data3': 0x9C00,
		'data4': b'\xBF\x98\x43\xC7\xB5\x8C'
	},
}

BAREBOX_PART_TYPES = {
	'state'  : { # barebox-state
		'data0': 0x4778ed65, 'data1': 0xbf42,
		'data2': 0x45fa    , 'data3': 0x9c5b,
		'data4': b'\x28\x7a\x1d\xc4\xaa\xb1'
	},
}


GPT_PART_TYPES = {
	'uefi'       : { **UEFI_CORE_PART_TYPES   },
	'windows'    : { **WINDOWS_PART_TYPES     },
	'hpux'       : { **HPUX_PART_TYPES        },
	'linux'      : { **LINUX_PART_TYPES       },
	'darwin'     : { **DARWIN_PART_TYPES      },
	'solaris'    : { **SOLARIS_PART_TYPES     },
	'netbsd'     : { **NETBSD_PART_TYPES      },
	'chromeos'   : { **CHROMEOS_PART_TYPES    },
	'coreos'     : { **COREOS_PART_TYPES      },
	'haiku'      : { **HAIKU_PART_TYPES       },
	'midnight'   : { **MIDNIGHT_PART_TYPES    },
	'ceph'       : { **CEPH_PART_TYPES        },
	'openbsd'    : { **OPENBSD_PART_TYPES     },
	'qnx'        : { **QNX_PART_TYPES         },
	'plan9'      : { **PLAN9_PART_TYPES       },
	'vmware'     : { **VMWARE_PART_TYPES      },
	'android_ia' : { **ANDROID_IA_PART_TYPES  },
	'android_arm': { **ANDROID_ARM_PART_TYPES },
	'onie'       : { **ONIE_PART_TYPES        },
	'powerpc'    : { **POWERPC_PART_TYPES     },
	'freedesktop': { **FREEDESKTOP_PART_TYPES },
	'atari_tos'  : { **ATARI_TOS_PART_TYPES   },
	'veracrypt'  : { **VERACRYPT_PART_TYPES   },
	'os2'        : { **OS2_PART_TYPES         },
	'spdk'       : { **SPDK_PART_TYPES        },
	'barebox'    : { **BAREBOX_PART_TYPES     },
}
