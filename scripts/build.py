#!/usr/bin/env python
# coding=utf-8

import sys
import os
import zipfile


def zip_directory(directory_path, output_filename):
    # Check if the directory exists
    if not os.path.exists(directory_path):
        print(f"Error: Directory '{directory_path}' does not exist.")
        return

    # Create the directory path for the output file if it doesn't exist
    output_dir = os.path.dirname(output_filename)
    if output_dir and not os.path.exists(output_dir):
        os.makedirs(output_dir)
        print(f"Created directory: {output_dir}")

    # Create a ZipFile object
    with zipfile.ZipFile(output_filename, "w", zipfile.ZIP_DEFLATED) as zipf:
        # Walk through the directory
        for root, _, files in os.walk(directory_path):
            for file in files:
                # Create the full file path
                file_path = os.path.join(root, file)
                # Calculate the archive name (path relative to the directory being zipped)
                arcname = os.path.relpath(file_path, directory_path)
                # Add the file to the zip
                zipf.write(file_path, arcname)

    print(f"Directory '{directory_path}' has been zipped to '{output_filename}'.")


if __name__ == "__main__":
    # Check if a directory path is provided as a command-line argument
    if len(sys.argv) < 2:
        print("Usage: python script.py <directory_path> [output_path]")
        sys.exit(1)

    # Get the directory path from command-line argument
    directory_path = sys.argv[1]

    # Get the output path from command-line argument or use default
    if len(sys.argv) > 2:
        output_path = sys.argv[2]
    else:
        output_path = os.getcwd()  # Current working directory

    # Create the output zip filename
    output_filename = os.path.join(
        output_path, os.path.basename(directory_path) + ".zip"
    )

    # Zip the directory
    zip_directory(directory_path, output_filename)
