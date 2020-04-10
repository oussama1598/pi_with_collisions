from app.scenes.simulation_scene import SimulationScene
from app.scenes.description_scene import DescriptionScene
from app.scenes.thanks_scene import ThanksScene


class Digits_1_DescriptionScene(DescriptionScene):
    CONFIG = {
        'digits': 1
    }


class Digits_1_SimulationScene(SimulationScene):
    CONFIG = {
        'digits': 1
    }


class Digits_2_DescriptionScene(DescriptionScene):
    CONFIG = {
        'digits': 2
    }


class Digits_2_SimulationScene(SimulationScene):
    CONFIG = {
        'digits': 2
    }


class Digits_3_DescriptionScene(DescriptionScene):
    CONFIG = {
        'digits': 3
    }


class Digits_3_SimulationScene(SimulationScene):
    CONFIG = {
        'digits': 3,
        'scene_duration': 15
    }


class Digits_4_DescriptionScene(DescriptionScene):
    CONFIG = {
        'digits': 4
    }


class Digits_4_SimulationScene(SimulationScene):
    CONFIG = {
        'digits': 4
    }


class ThanksScene(ThanksScene):
    pass


SCENES = [
    Digits_1_DescriptionScene,
    Digits_1_SimulationScene,
    Digits_2_DescriptionScene,
    Digits_2_SimulationScene,
    Digits_3_DescriptionScene,
    Digits_3_SimulationScene,
    Digits_4_DescriptionScene,
    Digits_4_SimulationScene,
    ThanksScene
]
