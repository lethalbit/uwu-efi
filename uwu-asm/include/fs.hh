/* SPDX-License-Identifier: BSD-3-Clause */
/* fs.hh - Filesystem wrapper */
#pragma once
#if !defined(UWUASM_FS_HH)
#define UWUASM_FS_HH

#include <config.hh>

#if defined(UWUASM_CPPFS_EXPERIMENTAL)
	#include <experimental/filesystem>
	namespace uwuefi::internal {
		namespace fs = std::experimental::filesystem;
	}
#else
	#include <filesystem>
	namespace uwuefi::internal {
		namespace fs = std::filesystem;
	}
#endif

#endif /* UWUASM_FS_HH */
