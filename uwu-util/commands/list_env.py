# SPDX-License-Identifier: BSD-3-Clause

from ..config import *
from ..utility import *

COMMAND_NAME = 'list'
COMMAND_DESC = 'list known environments'

def parser_init(parser):
	pass

def command_main(args, envs = None):
	if envs is None or len(envs) == 0:
		err('There are no environments, use new to add one')
		return 1

	for env_id, env in envs.items():
		print('')
		pretty_print_env(env)

	print('')
	return 0
