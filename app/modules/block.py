from manimlib.imports import *
import numpy as np


class Block(VGroup):
    CONFIG = {
        'mass': 1,
        'velocity': 0,
        'colors': [
            LIGHT_GREY,
            BLUE_D,
            BLUE_D,
            BLUE_E,
            BLUE_E,
            DARK_GREY,
            DARK_GREY
        ]
    }

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.width = 1 + 0.25 * np.log10(self.mass)
        self.color = self.colors[
            min(int(np.log10(self.mass)), len(self.colors) - 1)
        ]

        self._setup_block()
        self._add_mass_text()

    def _setup_block(self):
        self.block = Square(side_length=self.width)
        self.block.set_style(
            fill_opacity=1,
            fill_color=self.color,
            stroke_width=3,
            stroke_color=WHITE,
            sheen_factor=.5,
            sheen_direction=UR
        )

        self.add(self.block)

    def _add_mass_text(self):
        text = TextMobject(f'{self.mass:,} Kg')
        text.scale(.8)
        text.next_to(self, UP, SMALL_BUFF)

        self.add(text)
