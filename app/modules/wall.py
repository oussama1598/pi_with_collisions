from manimlib.imports import *


class Wall(VGroup):
    CONFIG = {
        'tick_spacing': .5,
        'tick_length': .25,
        'stroke_width': 1,
        'stroke_color': WHITE,
        'margin': {
            'top': 0,
            'right': 0,
            'bottom': 0,
            'left': 0
        }
    }

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.height = 0

        self._setup_wall()
        self._setup_ticks()

    def _setup_wall(self):
        x = -FRAME_WIDTH / 2 + self.margin['left']

        start = np.array([
            x,
            (FRAME_HEIGHT / 2) - self.margin['top'],
            0
        ])

        end = np.array([
            x,
            (-FRAME_HEIGHT / 2) + self.margin['bottom'],
            0
        ])

        self.height = start[1] - end[1]
        self.wall = Line(start=start, end=end)

        self.add(self.wall)

    def _setup_ticks(self):
        ticks_count = int(self.height / self.tick_spacing)
        ticks = VGroup()

        for i in range(ticks_count):
            tick = Line(
                start=np.zeros(3),
                end=np.array([self.tick_length, self.tick_spacing / 2, 0])
            )
            tick.shift(np.array([
                0,
                i * self.tick_spacing,
                0
            ]))

            tick.set_style(
                stroke_width=self.stroke_width,
                stroke_color=self.stroke_color
            )

            ticks.add(tick)

        ticks.move_to(self.wall, UR)

        self.wall.add(ticks)
