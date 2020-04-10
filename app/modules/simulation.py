from manimlib.imports import *
import numpy as np
from app.modules.wall import Wall
from app.modules.floor import Floor
from app.modules.block import Block


class Simulation(VGroup):
    CONFIG = {
        'scene_margin': {
            'top': 1,
            'bottom': 1,
            'left': 1,
            'right': 1
        },
        'blocks': [
            {
                'mass': int(1e6),
                'velocity': 0,
                'distance': 7
            },
            {
                'mass': 1,
                'velocity': 0,
                'distance': 3,
            }
        ]
    }

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.time = 0
        self.number_of_collisions = 0
        self.collisions_time = []

        self.mass_ratio = self.blocks[1]['mass'] / self.blocks[0]['mass']
        self.theta = np.arctan(np.sqrt(self.mass_ratio))

        self._setup_scene()

        # add the phase point
        self._init_phase_point()

        self._listen_for_updates()

    def _setup_scene(self):
        # Create the wall
        self._setup_wall()

        # Create the floor
        self._setup_floor()

        # Add the block
        self._setup_blocks()

        # add collision count text
        self._setup_collision_count_text()

    def _setup_wall(self):
        self.wall = Wall(margin=self.scene_margin)

        self.add(self.wall)

    def _setup_floor(self):
        self.floor = Floor(margin=self.scene_margin)

        self.add(self.floor)

    def _setup_blocks(self):
        self.block1 = self._add_block(**self.blocks[0])
        self.block2 = self._add_block(**self.blocks[1])

        self.add(self.block1, self.block2)

    def _add_block(self, **kwargs):
        block = Block(**kwargs)

        block.move_to(
            self.floor.get_top() + self.wall.get_right() +
            (kwargs['distance'] * RIGHT),
            DL
        )

        return block

    def _setup_collision_count_text(self):
        self.counter_number = Integer(self.number_of_collisions)

        counter_label = TextMobject('Collision: ')

        self.counter_number.scale(.6)
        counter_label.scale(.6)

        self.counter_number.next_to(
            counter_label, RIGHT
        )

        counter_group = VGroup(
            counter_label,
            self.counter_number,
        )

        counter_group.move_to(
            ((FRAME_WIDTH / 2) - self.scene_margin['left']) * LEFT
            + ((FRAME_HEIGHT / 2) - (self.scene_margin['top'] / 2)) * UP,
            UL
        )

        self.add(counter_group)

    def _init_phase_point(self):
        block1, block2 = self.block1, self.block2

        w2 = block2.get_width()
        s1 = block1.get_left()[0] - self.wall.get_right()[0] - w2
        s2 = block2.get_right()[0] - self.wall.get_right()[0] - w2

        self.phase_point = VectorizedPoint([
            s1 * np.sqrt(block1.mass),
            s2 * np.sqrt(block2.mass),
            0
        ])

        self.phase_point.velocity = np.array([
            np.sqrt(block1.mass) * block1.velocity,
            np.sqrt(block2.mass) * block2.velocity,
            0
        ])

    def _update_blocks_position_from_phase_point(self):
        block1, block2 = self.block1, self.block2

        ps_point = self.phase_point.get_location()
        ps_point_angle = angle_of_vector(ps_point)

        n_clacks = int(ps_point_angle / self.theta)

        if self.number_of_collisions != n_clacks:
            self.collisions_time.append(self.time)
            self.counter_number.set_value(n_clacks)

        reflected_point = rotate_vector(
            ps_point,
            -2 * np.ceil(n_clacks / 2) * self.theta
        )

        reflected_point = np.abs(reflected_point)
        shadow_wall_x = self.wall.get_right()[0] + block2.get_width()

        s1 = reflected_point[0] / np.sqrt(block1.mass)
        s2 = reflected_point[1] / np.sqrt(block2.mass)

        # self.ps.move_to(np.array([
        #     s1,
        #     s2,
        #     0
        # ]))

        block1.move_to(
            (shadow_wall_x + s1) * RIGHT + self.floor.get_top()[1] * UP,
            DL,
        )
        block2.move_to(
            (shadow_wall_x + s2) * RIGHT + self.floor.get_top()[1] * UP,
            DR,
        )

        self.number_of_collisions = n_clacks

    def _listen_for_updates(self):
        self.add_updater(lambda obj, dt: obj._update_time(dt))
        self.add_updater(lambda obj, dt: obj._update_positions(dt))

    def _update_time(self, delta_time):
        self.time += delta_time

    def _update_positions(self, delta_time):
        self.phase_point.shift(
            self.phase_point.velocity * delta_time
        )

        self._update_blocks_position_from_phase_point()
