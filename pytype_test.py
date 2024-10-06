#!/usr/bin/env python3

import os
import sys
import traceback

from pytype import config as pytype_config
from pytype import load_pytd


def main(filenames) -> None:
    typeshed_location = os.getcwd()
    subdir_path = os.path.join(typeshed_location, "stdlib")
    files_to_test = [os.path.join(subdir_path, fn) for fn in filenames]

    bad = []
    errors = 0
    total_tests = len(files_to_test)
    python_version = f"{sys.version_info.major}.{sys.version_info.minor}"
    print(f"pytype with files {filenames}:")

    os.environ["TYPESHED_HOME"] = typeshed_location
    options = pytype_config.Options.create(
        "", parse_pyi=True, python_version=python_version
    )
    loader = load_pytd.create_loader(options, [])

    for f in files_to_test:
        try:
            with pytype_config.verbosity_from(options):
                module_name = os.path.basename(f).replace(".pyi", "")
                ast = loader.load_file(module_name, f)
                loader.finish_and_verify_ast(ast)
        except Exception:
            stderr = traceback.format_exc()
            print(f"\n{stderr}")
            errors += 1
            stacktrace_final_line = stderr.rstrip().rsplit("\n", 1)[-1]
            bad.append(
                (f.split(os.path.sep)[-1], python_version, stacktrace_final_line)
            )

    print(f"Ran pytype with {total_tests:d} pyis, got {errors:d} errors.")
    for f, v, err in bad:
        print(f"\n{f} ({v}): {err}")


if __name__ == "__main__":

    main(["bar.pyi", "foo.pyi"])
    main(["foo.pyi", "bar.pyi"])
    main(["foo.pyi"])
    main(["bar.pyi"])
