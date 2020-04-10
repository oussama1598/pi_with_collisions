from manimlib.imports import *


class DescriptionScene(Scene):
    CONFIG = {
        'digits': 1
    }

    def setup(self):
        self._add_description()

    def construct(self):
        self.play(
            VFadeIn(self.text))

        self.wait(1)

        self.play(
            VFadeOut(self.text)
        )

    def _add_description(self):
        s = '' if self.digits < 2 else 's'

        self.text = TextMobject(f'Calculting {self.digits} digit{s} of PI')
