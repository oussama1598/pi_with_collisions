from manimlib.imports import *
from app.modules.simulation import Simulation


class SimulationScene(Scene):
    CONFIG = {
        'include_sound': True,
        'collision_sound': 'clack_sound.wav',
        'min_time_between_sounds': 0.004,
        'scene_duration': 10,
        'simulation_config': {
            'scene_margin': {
                'top': 1,
                'bottom': 1,
                'left': 1,
                'right': 0
            },
            'blocks': [
                {
                    'mass': int(1e6),
                    'velocity': -2,
                    'distance': 7
                },
                {
                    'mass': 1,
                    'velocity': 0,
                    'distance': 3,
                }
            ]
        }
    }

    def setup(self):
        self._add_simulation()

    def construct(self):
        self.wait(self.scene_duration)

    def _add_simulation(self):
        self.simulation = Simulation(**self.simulation_config)

        self.add(self.simulation)

    def _add_collisions_sound(self):
        last_time = 0

        for time in self.simulation.collisions_time:
            if time - last_time < self.min_time_between_sounds:
                continue
            last_time = time

            self.add_sound(
                self.collision_sound,
                time_offset=time - self.get_time(),
                gain=-20,
            )

    def tear_down(self):
        # add clack sounds when the animation finishes
        self._add_collisions_sound()

        super().tear_down()
