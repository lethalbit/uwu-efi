# SPDX-License-Identifier: BSD-3-Clause
from datetime import datetime

from jinja2 import Template, Environment

__all__ = (
	'env',

	'QEMU_LAUNCH_WRAPPER_TEMPLATE'
)

env = Environment(trim_blocks = True, lstrip_blocks = True)
env.globals['now'] = datetime.utcnow

QEMU_LAUNCH_WRAPPER_TEMPLATE =  env.from_string("""\
#!/usr/bin/env bash
# SPDX-License-Identifier: BSD-3-Clause
# !!! DO NOT EDIT THIS FILE DIRECTLY, ALL CHANGES WILL BE LOST !!!
# This file was generated by `uwu-util.py` on {{ now() }}
# `uwu-util.py` is part of uwu-efi <https://github.com/lethalbit/uwu-efi>

# This is a QEMU wrapper script for launching an uwu-efi development environment
#
# Environment Details:
#
#         Name: {{ opts['env']['name'] }}
#           ID: {{ opts['env']['id'] }}
# Architecture: {{ opts['env']['arch']['name'] }}
#   Created On: {{ opts['env']['created_date'] }}
#

ENV_LOC="{{opts['env']['location']}}"
OVMF_LOC="{{opts['ovmf']['location']}}"

qemu-system-{{opts['env']['arch']['name']}} -cpu {{opts['env']['arch']['cpu']}} \\
	-drive if=pflash,format=raw,unit=0,file="$OVMF_LOC/ovmf_code.fd",readonly=on \\
	-drive if=pflash,format=raw,unit=1,file="$ENV_LOC/ovmf_vars.fd" \\
	{% if not opts['env']['net']['enabled'] %}
	-net none \\
	{% else %}
	-net nic \\
	{% endif %}
	-nographic -serial mon:stdio \\
	{% if opts['env']['gdb']['enabled'] %}
	-S -gdb tcp::{{opts['env']['gdb']['port']}} \\
	{% endif %}
	-debugcon file:ovmf-debug.log -global isa-debugcon.iobase=0x402 \\
	-drive file="$ENV_LOC/root.img",if=ide,format=raw

""")
