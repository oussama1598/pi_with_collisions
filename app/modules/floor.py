from manimlib.imports import *


class Floor(VGroup):
    CONFIG = {
        'margin': {
            'top': 0,
            'right': 0,
            'bottom': 0,
            'left': 0
        }
    }

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self._setup_floor()

    def _setup_floor(self):
        y = (-FRAME_HEIGHT / 2) + self.margin['bottom']

        start = np.array([
            -FRAME_WIDTH / 2 + self.margin['left'],
            y,
            0
        ])

        end = np.array([
            FRAME_WIDTH / 2 - self.margin['right'],
            y,
            0
        ])

        self.floor = Line(start=start, end=end)
        self.add(self.floor)
