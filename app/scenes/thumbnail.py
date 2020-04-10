from pydub import AudioSegment
from manimlib.imports import *


class ThanksScene(Scene):
    def construct(self):
        self.file_writer.add_audio_segment(AudioSegment.silent(0))

        self.add(
            TextMobject('Calculating PI using boxes collision')
        )
