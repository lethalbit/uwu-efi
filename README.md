# uwu-efi

A clean, modern C++ 17 SDK for writing UEFI applications.

uwu-efi is designed to be a fully UEFI 2.8 w/ Errata A standards compliant SDK for writing UEFI applications in either modern C++, or some support for UEFI Bytecode.


## Supported Platforms

uwu-efi is planned to fully support the following platforms,

|  Platform  |     Status     |
|------------|----------------|
| `aarch64`  | `Planned`      |
| `amd64`    | `In Progress`  |
| `rv64`     | `Planned`      |


## Configuring and Building

The following steps describe how to build the uwu-efi package

### Prerequisites

To build uwu-efi, ensure you have the following dependencies:
 * git
 * meson
 * ninja
 * g++ >= 8.4.0 or clang++ >= 8.0.1

Some support scripts that uwu-efi uses need the following:
 * Python >= 3.7
 * python-construct
 * python-jinja2

### Configuring

You can build uwu-efi with the default options, all of which can be found in [`meson_options.txt`](meson_options.txt). You can change these by specifying `-D<OPTION_NAME>=<VALUE>` at initial meson invocation time, or with `meson configure` in the build directory post initial configure.

To change the install prefix, which is `/usr/local` by default ensure to pass `--prefix <PREFIX>` when running meson for the first time.

In either case, simply running `meson build` from the root of the repository will be sufficient and place all of the build files in the `build` subdirectory.

### Building

Once you have configured uwu-efi appropriately, to simply build and install simply run the following:

```
$ ninja -C build
$ ninja -C build install
```

This will build and install uwu-efi into the default prefix which is `/usr/local`, to change that see the configuration steps above.

### Notes to Package Maintainers

If you are building uwu-efi for inclusion in a distributions package system then ensure to set `DESTDIR` prior to running meson install.

There is also a `bugreport_url` configuration option that is set to this repositories issues tracker by default, it is recommended to change it to your distributions bug tracking page.


## Using uwu-efi and Documentation

TODO

## License

uwu-efi is licensed under the [BSD-3-Clause](https://spdx.org/licenses/BSD-3-Clause.html) license, the full text of which can be found in the [`LICENSE`](./LICENSE) file
