import argparse
import os
import shutil
import sys
import pathlib
import subprocess

LOSSLESS_EXTENSIONS = ['.flac', '.wav']

SOX_PATH = None
if os.name == 'posix':
    SOX_PATH = shutil.which('sox')
elif os.name == 'nt':
    SOX_PATH = shutil.which('sox.exe')

if not SOX_PATH:
    print('ERROR: SoX not found in path')
    sys.exit(1)


def _parse_args():
    parser = argparse.ArgumentParser(description='Batch create spectogram images from files in specified directory')
    parser.add_argument('source_directory', help='Location of audio files')
    parser.add_argument('dest_directory', help='Location to output spectrogram images. Defaults to CWD',
                        nargs='?',
                        default=os.getcwd())

    return parser.parse_args()


def main(source_directory, dest_directory):
    source_directory = pathlib.Path(source_directory)
    dest_directory = pathlib.Path(dest_directory)

    # Validate paths
    if not source_directory.is_dir():
        print('ERROR: Source directory is not valid')
        sys.exit(1)
    if not dest_directory.is_dir():
        print('ERROR: Destination directory is not valid')
        sys.exit(1)

    audio_files = [file for file in source_directory.glob('*') if file.is_file() and file.suffix.lower() in LOSSLESS_EXTENSIONS]

    for file in audio_files:
        file_output_path = dest_directory / (file.stem + '.png')

        print('Processing {}'.format(file.name))
        subprocess.run([SOX_PATH, file.absolute(), '-n', 'spectrogram', '-o', file_output_path])

    print('DONE')


if __name__ == '__main__':
    args = _parse_args()

    main(args.source_directory, args.dest_directory)
