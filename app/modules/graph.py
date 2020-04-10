from manimlib.imports import *


class Graph(VGroup):
    CONFIG = {
        'name': 'Test',
        'width': 2,
        'height': 2,
        'update_frequency': 1 / 60,
        'y_min': 0,
        'y_max': 10,
        'y_axis_config': {
            'tick_frequency': 1,
        },
        'x_min': 0,
        'x_max': 10,
        'x_axis_config': {
            'tick_frequency': 1,
        },
        'axis_config': {
            'include_tip': False,
        },
    }

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self._setup_axes()
        self._setup_labels()
        self._setup_graph_name()
        self._setup_dot()

    def _setup_axes(self):
        self.axes = Axes(
            y_min=self.y_min,
            y_max=self.y_max,
            y_axis_config=self.y_axis_config,
            x_min=self.x_min,
            x_max=self.x_max,
            x_axis_config=self.x_axis_config,
            axis_config=self.axis_config
        )
        origin = self.axes.c2p(0, 0)

        self.axes.x_axis.set_width(
            self.width, about_point=origin, stretch=True)
        self.axes.y_axis.set_height(
            self.height, about_point=origin, stretch=True)

        self.add(self.axes)

    def _setup_x_labels(self):
        x_range = np.abs(self.x_max - self.x_min)
        x_number_of_labels = int(
            x_range / self.x_axis_config['tick_frequency']
        )
        x_tick_offset = self.height / x_number_of_labels
        self.x_labels = VGroup()

        for i, num in zip(range(x_number_of_labels + 1), np.arange(self.x_min, self.x_max + 1, self.x_axis_config['tick_frequency'])):
            label = Integer(num, color=BLUE)
            label.set_height(x_tick_offset)
            label.scale(.6)
            label.shift(i * x_tick_offset * RIGHT)

            self.x_labels.add(label)

        self.x_labels.move_to(np.array([
            self.x_labels.get_center()[0],
            self.get_bottom()[1] - .1,
            0
        ]))

        self.add(self.x_labels)

    def _setup_y_labels(self):
        y_range = np.abs(self.y_max - self.y_min)
        y_number_of_labels = int(
            y_range / self.y_axis_config['tick_frequency']
        )
        y_tick_offset = self.height / y_number_of_labels
        y_labels = VGroup()

        for i, num in zip(range(y_number_of_labels + 1), np.arange(self.y_min, self.y_max + 1, self.y_axis_config['tick_frequency'])):
            label = Integer(num, color=BLUE)
            label.set_height(y_tick_offset)
            label.scale(.6)
            label.shift(i * y_tick_offset * UP)

            y_labels.add(label)

        y_labels.move_to(np.array([
            self.get_left()[0] - .1,
            y_labels.get_center()[1],
            0
        ]))

        self.add(y_labels)

    def _setup_labels(self):
        self._setup_x_labels()
        self._setup_y_labels()

    def _setup_graph_name(self):
        graph_name = TextMobject(self.name, color=RED)

        graph_name.set_width(self.get_height())
        graph_name.rotate_about_origin(np.pi / 2)
        graph_name.move_to(self.get_corner(
            UL) + self.x_labels.get_height() * LEFT, UR)

        self.add(graph_name)

    def _setup_dot(self):
        self.dot = Dot(
            self.axes.c2p(0, 0),
            radius=(self.get_height() / self.get_width()) / 18,
            fill_color=YELLOW,
        )

        self.add(self.dot)

    def add_line_at(self, start_point, end_point, stroke_width=1, stroke_color=WHITE):
        line = Line(
            self.axes.c2p(*start_point),
            self.axes.c2p(*end_point),
            stroke_width=stroke_width,
            stroke_color=stroke_color
        )

        self.add(line)

    def update_point_position(self, position=(0, 0)):
        x, y = position

        self.dot.move_to(
            self.axes.c2p(x, y)
        )
