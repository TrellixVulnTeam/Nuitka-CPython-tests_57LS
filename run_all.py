#!/usr/bin/env python3.7

import os, sys

# Find nuitka package relative to us.
sys.path.insert(
    0,
    os.path.normpath(
        os.path.join(
            os.path.dirname(os.path.abspath(__file__)),
            "..",
            ".."
        )
    )
)

from nuitka.tools.testing.Common import (
    my_print,
    setup,
    reportSkip,
    compareWithCPython,
    createSearchMode
)

python_version = setup(needs_io_encoding = True)

search_mode = createSearchMode()

def checkPath(dirname, filename):
    global active

    extra_flags = [
        "remove_output",
        # Import test_support which won't be included and potentially others.
        "binary_python_path",
        # We mean to compile only that one module
        "recurse_none",
        # Keep us informed about timing, even if concurrent runs spoil the
        # accuracy.
        "timing",
        # Use the original __file__ value, at least one case warns about things
        # with filename included.
        "original_file"
    ]

    # TODO: Segfaulting due to reference counting issue.
    if filename == "test_asyncgen.py":
        my_print("Skipping (KNOWN BUGGY)", filename)
        return

    # TODO: This deadlocks, likely a threading problem.
    if python_version >= "3.4" and \
       filename == "test_concurrent_futures.py":
        reportSkip("Skipping (due to threading issue)", dirname, filename)
        return

    if dirname == "doctest_generated":
        if python_version >= "3.7":
            extra_flags.append("expect_success")

        if filename == "test_generators.py":
            extra_flags.append("ignore_stderr")

            # On Windows with 32 bit, the MemoryError breaks the test
            if os.name == "nt":
                reportSkip("not enough memory with 32 bits on Windows", dirname, filename)

                return

    if filename in ("test_platform.py",):
        extra_flags.append("ignore_stderr")

    compareWithCPython(
        dirname     = dirname,
        filename    = filename,
        extra_flags = extra_flags,
        search_mode = search_mode,
        needs_2to3  = False
    )


def checkDir(dirname):
    for filename in sorted(os.listdir(dirname)):
        if not filename.endswith(".py") or not filename.startswith("test_"):
            continue

        if filename == "test_support.py":
            continue

        active = search_mode.consider(dirname, filename)

        if active:
            checkPath(dirname, filename)
        else:
            my_print("Skipping", os.path.join(dirname, filename))

checkDir("test")
checkDir("doctest_generated")
