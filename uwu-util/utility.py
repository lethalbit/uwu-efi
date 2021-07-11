# SPDX-License-Identifier: BSD-3-Clause
import sys

from .config import *

__all__ = (
	'_init_directories',
	'aquire_file',
	'exec_cmd',
	'get_ovmf',

	'log', 'err', 'wrn', 'inf', 'dbg',

	'known_env', 'pretty_print_env',
)


def _init_directories():
	dirs = (
		# Core Directories
		DATA_DIR,
		CACHE_DIR,
		OVMF_DIR,
		ENV_DIR,
	)

	for d in dirs:
		if not path.exists(d):
			mkdir(d)

def log(str, end = '\n', file = sys.stdout):
	print(f'\x1B[35m[*]\x1B[0m {str}', end = end, file = file)

def err(str, end = '\n', file = sys.stderr):
	print(f'\x1B[31m[!]\x1B[0m {str}', end = end, file = file)

def wrn(str, end = '\n', file = sys.stderr):
	print(f'\x1B[33m[~]\x1B[0m {str}', end = end, file = file)

def inf(str, end = '\n', file = sys.stdout):
	print(f'\x1B[36m[~]\x1B[0m {str}', end = end, file = file)

def dbg(str, end = '\n', file = sys.stdout):
	print(f'\x1B[34m[~]\x1B[0m {str}', end = end, file = file)

def aquire_file(url, download_dir, file_name = None):
	import requests
	fname = file_name if file_name is not None else url.rsplit('/', 1)[1]
	tgt_file = path.join(download_dir, fname)

	if path.exists(tgt_file):
		return True

	log(f'\tAcquiring {tgt_file} from {url}')

	with requests.get(url, allow_redirects=True) as r:
		if not r.ok:
			err(f'Unable to download {fname}: {r.status_code}')
			return False
		log('\t  => Downloading')
		with open(tgt_file, 'wb') as f:
			for chk in r.iter_content(chunk_size = 8192):
				f.write(chk)
	return True

def exec_cmd(cmd, cwd, env = None):
	from subprocess import run, PIPE
	from os import environ

	res = run(
			cmd,
			stdout = PIPE, stderr = PIPE,
			shell = True, cwd = cwd,
			env = env if env is not None else environ
		)

	if res.returncode != 0:
		err(f'{res.stderr.decode("UTF-8")}')
		with open(f'{path.join(cwd, "uwu-util.stdout")}', 'w') as stdout:
			stdout.write(res.stdout.decode('UTF-8'))
		with open(f'{path.join(cwd, "uwu-util.stderr")}', 'w') as stderr:
			stderr.write(res.stderr.decode('UTF-8'))


	return res.returncode

def get_ovmf():
	log(f'Collecting OVMF files if needed')

	for arch, imgs in OVMF_IMGS.items():
		arch_dir = path.join(OVMF_DIR, str(arch))

		if not path.exists(arch_dir):
			mkdir(arch_dir)

		for rel, files in imgs.items():
			rel_dir = path.join(arch_dir, rel)

			if not path.exists(rel_dir):
				mkdir(rel_dir)

			aquire_file(f'{OVMF_BUILD_URL}/{files["code"]}', rel_dir, 'ovmf_code.fd')
			aquire_file(f'{OVMF_BUILD_URL}/{files["vars"]}', rel_dir, 'ovmf_vars.fd')

def known_env(envs, name):
	for env_id, env in envs.items():
		if env['name'] == name:
			return True
	return False

def pretty_print_env(env):
	inf(f'          Name: {env["name"]}')
	inf(f'            Id: {env["id"]}')
	inf(f'  Architecture: {env["arch"]["name"]}')
	inf(f'    Networking: {env["net"]["enabled"]}')
	inf(f'           GDB: {env["gdb"]["enabled"]}')
	if env["gdb"]["enabled"]:
		inf(f'               GDB Port: {env["gdb"]["port"]}')
