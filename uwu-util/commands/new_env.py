# SPDX-License-Identifier: BSD-3-Clause
import stat

from os import path, mkdir, getcwd, environ, symlink, chmod
from shutil import copyfile
from uuid import uuid4
from datetime import datetime

from ..config import *
from ..utility import *

from ..fs import *
from ..templates import *

from jinja2 import Template

COMMAND_NAME = 'new'
COMMAND_DESC = 'create a new environment'

def parser_init(parser):
	parser.add_argument(
		'name',
		type = str,
		help = 'name of the environment',
	)

	parser.add_argument(
		'--architecture', '-a',
		type = UEFIArchitecture.from_string,
		choices = list(UEFIArchitecture),
		default = UEFIArchitecture['x86_64'],
		help = 'The architecture to use'
	)

	parser.add_argument(
		'--enable-net', '-n',
		default = False,
		action = 'store_true',
		help = 'Enable QEMU networking'
	)

	parser.add_argument(
		'--enable-gdb', '-g',
		default = False,
		action = 'store_true',
		help = 'Enable QEMUs GDB server',
	)

	parser.add_argument(
		'--gdb-port', '-p',
		type = int,
		default = 6969,
		help = 'The port on which to tell the GDB server to listen'
	)

def command_main(args, envs = None):
	get_ovmf()

	if known_env(envs, args.name):
		err(f'The environment \'{args.name}\' already exists')
		return 1
	inf(f'Creating environment \'{args.name}\'')

	env_id = str(uuid4())
	env_loc = path.join(ENV_DIR, env_id)
	env_launch_script = path.join(env_loc, 'launch.bash')

	envs[env_id] = {
		'id': env_id,
		'name': args.name,
		'created_date': str(datetime.utcnow()),
		'location': env_loc,
		'arch': {
			'name': str(args.architecture),
			'cpu': 'qemu64'
		},
		'gdb': {
			'enabled': args.enable_gdb,
			'port': args.gdb_port
		},
		'net': {
			'enabled': args.enable_net,
		},
		'launch_script': env_launch_script,
	}

	if not path.exists(env_loc):
		mkdir(env_loc)

	ovmf_arch_dir = path.join(OVMF_DIR, str(args.architecture))

	copyfile(path.join(ovmf_arch_dir, 'debug/ovmf_vars.fd'), path.join(env_loc, 'ovmf_vars.fd'))

	with open(env_launch_script, 'w') as ls:
		ls.write(QEMU_LAUNCH_WRAPPER_TEMPLATE.render(
			opts = {
				'env': envs[env_id],
				'ovmf': {
					'location': path.join(ovmf_arch_dir, 'debug')
				}
			}
		))
		ls.write('\n')

	chmod(env_launch_script, stat.S_IEXEC | stat.S_IREAD | stat.S_IRWXU)

	# make_root_fs_image(envs[env_id])

	log(f'Created environment:')
	pretty_print_env(envs[env_id])


	return 0
