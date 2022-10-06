#!/usr/bin/env python3
import argparse
import os
import pathlib

# NOTE: pydub uses ffmpeg
from audiobook import Audiobook
from pydub import AudioSegment
from pydub.playback import play

verbose = False
tracker_path = "~/.local/share/audiobooks"

def main(args):
    startup(args.config)
    if args.verbose:
        verbose = True

    audiobooks = []
    for f in os.listdir('test_files'):
        audiobooks.append(Audiobook())
        file_path = os.path.abspath('test_files/' + f)
        audiobooks[-1].read_raw_file(file_path)

    return True

# NOTE: Startup function reads the config file and all files at that location
def startup(config_path):
    # TODO: implemente
    if config_path == None:
        return
    os.path.file_exists(config_path)

    return


if __name__  == "__main__":
    parser = argparse.ArgumentParser()

    parser.add_argument("-V", "--version", help="Prints the current version")
    parser.add_argument("-v", "--verbose", help="Prints mode infomation of control flow")
    parser.add_argument("-c", "--config", nargs=1, help="Uses specified config file")

    args = parser.parse_args()

    main(args)
