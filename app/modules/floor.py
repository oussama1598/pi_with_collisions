from manimlib.imports import *


class Floor(VGroup):
    CONFIG = {
        'margin': {
            'top': 0,
            'right': 0,
            'bottom': 0,
            'left': 0
        },
        'tick_frequency': 1,
        'tick_length': .25
    }

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self._setup_floor()
        # self._setup_ticks()
        self._setup_ticks_labels()

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

    def _setup_ticks_labels(self):
        width = self.get_width() - 1
        number_of_ticks = int(
            width / self.tick_frequency
        )
        tick_offset = width / number_of_ticks

        ticks = VGroup()
        labels = VGroup()

        for i, num in zip(range(number_of_ticks + 1), np.arange(0, width + 1, self.tick_frequency)):
            label = TextMobject(f'{num}', color=BLUE)
            label.set_height(tick_offset)
            label.scale(.3)
            label.shift(i * tick_offset * RIGHT)

            tick = Line(
                start=np.zeros(3),
                end=np.array([0, -self.tick_length, 0])
            )
            tick.shift(i * tick_offset * RIGHT)

            labels.add(label)
            ticks.add(tick)

        labels.move_to(self.get_corner(DL), UL)
        labels.shift((self.tick_length + 0.05) * DOWN)
        labels.shift(.1 * LEFT)

        ticks.move_to(self, UL)

        self.add(labels)
        self.add(ticks)
