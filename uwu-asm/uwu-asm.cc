/* SPDX-License-Identifier: BSD-3-Clause */
/* uwu-asm.cc - uwu-efi UEFI Bytecode assembler */
#include <config.hh>

#include <fs.hh>

#include <string>

#include <cstdint>
#include <getopt.h>
#include <unistd.h>

#include <substrate/utility>
#include <substrate/console>
#include <substrate/conversions>

using namespace std::literals::string_view_literals;
using namespace uwuefi::internal;

static struct option lopts[] = {
	{ "help",    no_argument,       0, 'h' },
	{ "version", no_argument,       0, 'v' },
	{ "debug",   no_argument,       0, 'd' },
	{ "output",  required_argument, 0, 'o' },

	{ 0, 0, 0, 0 }
};

void print_banner();
void print_help();
void print_version();

int main(int argc, char** argv) {
	substrate::console = {stdout, stderr};
	substrate::console.showDebug(false);
	fs::path output_file{"uwu.bin"};
	fs::path input_file{};

	int o;
	int opt_idx{0};
	while((o = getopt_long(argc, argv, "hvdo:", lopts, &opt_idx)) != -1) {
		switch(o) {
			 case 'h': {
				print_help();
				exit(1);
			} case 'v': {
				print_version();
				exit(1);
			} case 'd': {
				substrate::console.showDebug(true);
				break;
			} case 'o': {
				output_file = optarg;
				break;
			} case '?': {
				exit(1);
			} default: {
				exit(1);
			}
		}
	}

	if (argv[optind] == nullptr) {
		substrate::console.error("Missing input file, see uwu-asm --help for usage"sv);
		return 1;
	} else {
		input_file = argv[optind];
	}

	if (!fs::exists(input_file)) {
		substrate::console.error("The input file '"sv, input_file.c_str(), "' could not be opened, does it exist?"sv);
		return 1;
	}

	print_banner();

	return {};
}

void print_banner() {
	substrate::console.writeln(
		"uwu-asm v"sv, uwuefi::config::version
		," ("sv,       uwuefi::config::compiler
		," "sv,        uwuefi::config::compiler_version
		," "sv,        uwuefi::config::build_system
		,"-"sv,        uwuefi::config::build_arch
		,")"sv
	);

	substrate::console.writeln("uwu-asm is part of the uwu-efi project <https://github.com/lethalbit/uwu-efi>"sv);
	substrate::console.writeln("uwu-asm is licensed under the BSD-3-Clause <https://spdx.org/licenses/BSD-3-Clause.html>"sv);
	substrate::console.writeln("\nPlease report bugs at <"sv, uwuefi::config::bugreport_url, ">"sv);
}

void print_help() {
	print_banner();

	substrate::console.writeln("Usage:"sv);
	substrate::console.writeln("\nuwu-asm [options] <INPUT FILE>\n"sv);
	substrate::console.writeln("  --help,    -h       Print this help text and exit"sv);
	substrate::console.writeln("  --version, -v       Print version and exit"sv);
	substrate::console.writeln("  --debug,   -d       Prints debug output THIS WILL GENERATE A LOT OF MESSAGGES"sv);

	substrate::console.writeln("  --output,  -o       The output file to assemble to. (default: uwu.bin)"sv);


	substrate::console.writeln("\nPlease report bugs at <"sv, uwuefi::config::bugreport_url, ">"sv);
}

void print_version() {
	substrate::console.writeln("uwu-asm v"sv, uwuefi::config::version);
}
