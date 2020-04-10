from pydub import AudioSegment
from manimlib.imports import *


class ThanksScene(Scene):
    CONFIG = {
        'digits': 1
    }

    def construct(self):
        self.file_writer.add_audio_segment(AudioSegment.silent(0))

        text = TextMobject('Thank your for watching.\n Hope you liked it.')

        self.play(
            VFadeIn(text)
        )

        self.wait(1)

        self.play(
            VFadeOut(text)
        )
