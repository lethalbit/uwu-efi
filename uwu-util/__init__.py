#!/usr/bin/env python
# SPDX-License-Identifier: BSD-3-Clause
import sys
import json

from os import path, mkdir, getcwd, environ, symlink, chmod
from shutil import copyfile



from .config import *
from .utility import *


def _collect_commands():
	import pkgutil
	from . import commands

	cmds = []

	for _, name, is_pkg in pkgutil.iter_modules(path = getattr(commands, '__path__')):
		if not is_pkg:
			__import__(f'{getattr(commands, "__name__")}.{name}')
			if not hasattr(getattr(commands, name), 'DONT_LOAD'):
				cmds.append({
					'name': getattr(commands, name).COMMAND_NAME,
					'description': getattr(commands, name).COMMAND_DESC,
					'parser_init': getattr(commands, name).parser_init,
					'main': getattr(commands, name).command_main,
				})

	return cmds


def main():
	from argparse import ArgumentParser, ArgumentDefaultsHelpFormatter

	known_envs = {}

	parser = ArgumentParser(
		prog = __package__,
		formatter_class = ArgumentDefaultsHelpFormatter,
		description = 'uwu-efi helper utility'
	)

	global_options = parser.add_argument_group('Global Options')

	action_parser = parser.add_subparsers(
		dest = 'action',
		required = True
	)

	COMMANDS = _collect_commands()

	for cmd in COMMANDS:
		ap = action_parser.add_parser(
			cmd['name'],
			help = cmd['description']
		)

		cmd['parser_init'](ap)

	args = parser.parse_args()

	if not path.exists(ENV_CACHE):
		with open(ENV_CACHE, 'w') as ec:
			json.dump(known_envs, ec)
	else:
		with open(ENV_CACHE, 'r') as ec:
			known_envs = json.load(ec)



	cmd = list(filter(lambda c: c['name'] == args.action, COMMANDS))[0]

	ret_code = cmd['main'](args, known_envs)

	with open(ENV_CACHE, 'w') as ec:
		json.dump(known_envs, ec)

	return ret_code


if __name__ == '__main__':
	_init_directories()
	sys.exit(main())
