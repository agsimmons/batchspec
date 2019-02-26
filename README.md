# batchspec
A wrapper around SoX to generate spectrogram images for all lossless audio files in a directory

# Requirements
* Python 3.3+
* SoX executable must be in your PATH

# Usage
```
usage: batchspec.py [-h] source_directory [dest_directory]

Batch create spectogram images from files in specified directory

positional arguments:
  source_directory  Location of audio files
  dest_directory    Location to output spectrogram images. Defaults to ./

optional arguments:
  -h, --help        show this help message and exit
```
