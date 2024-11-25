# misc_binfie_utils

## Installation

You will need python installed. Any version > 3.0  will probably work, I used 3.12.7.

```
# Clone the git repo
git clone https://github.com/maxlcummins/misc_binfie_utils.git

# Enter the repo
cd misc_binfie_utils

# Change permissions of scripts
chmod 755 mbu/*

# Use the utilities
mbu/<your_desired_script>.py
```

### mbu/copy_files.py

Often times we end up subsetting our collections and need to copy files for this subset to a new directory for additional analysis. This script will simplify that process.

```
Copies files from the input directory to the output directory based on sample names and file suffix.

This function performs the following steps:
- Checks if the `input_dir` exists; exits if it does not.
- Checks if the `output_dir` exists; creates it if it does not.
- Reads sample names from `samples_file`; exits if the file cannot be read or is empty.
- For each sample name:
    - Finds files in `input_dir` that start with the sample name and end with `file_suffix`.
    - Copies each matching file to `output_dir`.
    - Prints messages for files copied or if no matching files are found.

Example usage:
    For reads:
        copy_files.py -i /path/to/input_dir -o /path/to/output_dir -s /path/to/samples.txt -f '.fastq.gz'

    For assemblies:
        copy_files.py -i /path/to/input_dir -o /path/to/output_dir -s /path/to/samples.txt -f '.fasta'

    For text files:
        copy_files.py -i /path/to/input_dir -o /path/to/output_dir -s /path/to/samples.txt -f '.txt'

Parameters:
        input_dir (str): Path to the input directory containing the files to be copied.
        output_dir (str): Path to the output directory where files will be copied.
        samples_file (str): Path to a text file containing sample names (one per line).
        file_suffix (str): The suffix of the files to be copied (e.g., '.txt').

Exceptions:
        SystemExit: Exits the program with a message if critical errors occur (e.g., missing directories, read errors).
```
