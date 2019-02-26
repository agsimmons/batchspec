# batchspec
A wrapper around SoX to generate spectrogram images for all lossless audio files in a directory

# Requirements
* Python 3.5+

# Usage
```
usage: batchspec.py [-h] [--sox_path SOX_PATH] source_directory [dest_directory]

Batch create spectogram images from files in specified directory

positional arguments:
  source_directory     Location of audio files
  dest_directory       Location to output spectrogram images. Defaults to CWD

optional arguments:
  -h, --help           show this help message and exit
  --sox_path SOX_PATH  Path to SoX executable. Will use sox or sox.exe in PATH by default
```
