#!/usr/bin/env python
# coding=utf-8

import os
import sys


def create_symlink(package_name, package_path):
    """Creates a symlink from the current directory's package to the Inkscape user extensions directory."""

    inkscape_extensions_dir = os.environ.get("INKSCAPE_EXTENSIONS_DIR")

    # Construct the full paths
    source_dir = os.path.abspath(package_path)
    target_path = os.path.join(inkscape_extensions_dir, package_name)

    # Check if the source directory exists
    if not os.path.isdir(source_dir):
        print(f"Error: Source directory '{source_dir}' does not exist.")
        return

    # Create the symlink
    try:
        os.symlink(source_dir, target_path)
        print("Symlink created successfully:")
        print(f"  Source: {source_dir}")
        print(f"  Target: {target_path}")
    except OSError as e:
        print(f"Error: Failed to create symlink: {e}")


if __name__ == "__main__":
    args = sys.argv
    create_symlink(args[1], args[2])
