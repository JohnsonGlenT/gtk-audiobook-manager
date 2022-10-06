#!/usr/bin/env python3
import mutagen
import os
import pathlib

from pydub import AudioSegment
from pydub.playback import play

class Audiobook():
    def __init__(self):
        # NOTE: is None when not active/selected
        self.stream = None
        self.path = None
        self.files = [None]
        self.name = None
        self.author = None
        self.length = None
        self.chapters = None
        self.playtime = 0.0


    # NOTE: audiobook file should be full system path
    def read_from_file(self, audiobook_file):
        if audiobook_file == None or not os.path.isfile(audiobook_file):
            return

        self.path = + "audiobooks/" + name

        lines = []
        with open(self.path) as f:
           lines = f.readlines()


    def read_raw_file(self, raw_file_path):
        ext = pathlib.Path(raw_file_path).suffix
        metadata = mutagen.File(raw_file_path)
        audio_stream = AudioSegment.from_file(raw_file_path, ext)

        if metadata == {} or metadata == None:
            self.name = pathlib.Path(raw_file_path).name
            self.author = 'Unknown'
        else:
            self.name = metadata.items()[0][1].text[0]
            self.author = metadata.items()[1][1].text[0]

        self.path = raw_file_path
        # TODO batch files for books
        self.files = [None]

        self.length = audio_stream.duration_seconds

        # TODO list chapters in audio book, if provided
        self.chapters = None
        self.playtime = 0.0

    def save_to_file(self, config_path):
        with open(config_path + self.name, 'w') as f:
            f.write(self.path, '\n')
            for f in self.files:
                f.write(f, ',')
            f.write('\n')
            f.write(self.name, '\n')
            f.write(self.author, '\n')
            f.write(self.length, '\n')
            f.write(self.chapters, '\n')
            f.write(self.playtime)

        return
