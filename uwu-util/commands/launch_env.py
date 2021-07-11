# SPDX-License-Identifier: BSD-3-Clause

from ..config import *
from ..utility import *

COMMAND_NAME = 'launch'
COMMAND_DESC = 'launch an environment'

def parser_init(parser):
	parser.add_argument(
		'name',
		type = str,
		help = 'name of the environment',
	)

def command_main(args, envs = None):
	if envs is None or len(envs) == 0:
		err('There are no environments, use new to add one')
		return 1

	if not known_env(envs, args.name):
		err(f'The environment \'{args.name}\' does not exist')
		return 1

	return 0
