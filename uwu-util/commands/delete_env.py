# SPDX-License-Identifier: BSD-3-Clause

from shutil import rmtree

from ..config import *
from ..utility import *

COMMAND_NAME = 'delete'
COMMAND_DESC = 'delete an environment'

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

	cached_env_id = None

	for env_id, env in envs.items():
		if env['name'] == args.name:
			cached_env_id = env_id
			break

	if cached_env_id is not None:
		env = envs[cached_env_id]
		log(f'Deleting environment {env["name"]}')
		inf(f'env cache is at {env["location"]}')
		rmtree(env["location"])

		del envs[cached_env_id]
	else:
		err(f'Unable to find environment with name {args.name}')
		return 1

	return 0
