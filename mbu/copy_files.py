import os
import sys
import shutil
import argparse

#!/usr/bin/env python3


def copy_files(input_dir, output_dir, samples_file, file_suffix):
    if not os.path.isdir(input_dir):
        print(f"Error: Input directory '{input_dir}' does not exist.")
        sys.exit(1)
    if not os.path.exists(output_dir):
        print(f"Output directory '{output_dir}' does not exist. Creating it.")
        os.makedirs(output_dir)
    try:
        with open(samples_file, 'r') as f:
            samples = [line.strip() for line in f if line.strip()]
    except Exception as e:
        print(f"Error reading samples file '{samples_file}': {e}")
        sys.exit(1)
    if not samples:
        print(f"No sample names found in '{samples_file}'.")
        sys.exit(1)
    for sample in samples:
        matching_files = [f for f in os.listdir(input_dir)
                          if f.startswith(sample) and f.endswith(file_suffix)]
        if not matching_files:
            print(f"No files found for sample '{sample}' with suffix '{file_suffix}'.")
            continue
        for filename in matching_files:
            src = os.path.join(input_dir, filename)
            dest = os.path.join(output_dir, filename)
            try:
                shutil.copy2(src, dest)
                print(f"Copied '{src}' to '{dest}'.")
            except Exception as e:
                print(f"Error copying '{src}' to '{dest}': {e}")

def main():
    parser = argparse.ArgumentParser(description='Copy files based on sample names and file suffix.')
    parser.add_argument('-i', '--input_dir', required=True, help='Input directory containing files.')
    parser.add_argument('-o', '--output_dir', required=True, help='Output directory to copy files to.')
    parser.add_argument('-s', '--samples_file', required=True, help='File containing sample names.')
    parser.add_argument('-f', '--file_suffix', required=True, help='File suffix to match.')
    args = parser.parse_args()

    copy_files(args.input_dir, args.output_dir, args.samples_file, args.file_suffix)

if __name__ == '__main__':
    main()