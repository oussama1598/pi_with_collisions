import moderngl_window as mglw
from moderngl_window.context.pyglet.window import Window as PygletWindow
from moderngl_window.timers.clock import Timer

from manimlib.constants import DEFAULT_PIXEL_WIDTH
from manimlib.constants import DEFAULT_PIXEL_HEIGHT
from manimlib.utils.config_ops import digest_config


class Window(PygletWindow):
    size = (DEFAULT_PIXEL_WIDTH, DEFAULT_PIXEL_HEIGHT)
    fullscreen = False
    resizable = True
    gl_version = (3, 3)
    vsync = True
    samples = 1
    cursor = True

    def __init__(self, scene, **kwargs):
        digest_config(self, kwargs)
        super().__init__(**kwargs)
        self.scene = scene
        self.title = str(scene)
        # Put at the top of the screen
        self.position = (self.position[0], 0)

        mglw.activate_context(window=self)
        self.timer = Timer()
        self.config = mglw.WindowConfig(ctx=self.ctx, wnd=self, timer=self.timer)
        self.timer.start()

    # Delegate event handling to scene
    def pixel_coords_to_space_coords(self, px, py, relative=False):
        return self.scene.camera.pixel_coords_to_space_coords(px, py, relative)

    def on_mouse_motion(self, x, y, dx, dy):
        super().on_mouse_motion(x, y, dx, dy)
        point = self.pixel_coords_to_space_coords(x, y)
        d_point = self.pixel_coords_to_space_coords(dx, dy, relative=True)
        self.scene.on_mouse_motion(point, d_point)

    def on_mouse_drag(self, x, y, dx, dy, buttons, modifiers):
        super().on_mouse_drag(x, y, dx, dy, buttons, modifiers)
        point = self.pixel_coords_to_space_coords(x, y)
        d_point = self.pixel_coords_to_space_coords(dx, dy, relative=True)
        self.scene.on_mouse_drag(point, d_point, buttons, modifiers)

    def on_mouse_press(self, x: int, y: int, button, mods):
        super().on_mouse_press(x, y, button, mods)
        point = self.pixel_coords_to_space_coords(x, y)
        self.scene.on_mouse_press(point, button, mods)

    def on_mouse_release(self, x: int, y: int, button, mods):
        super().on_mouse_release(x, y, button, mods)
        point = self.pixel_coords_to_space_coords(x, y)
        self.scene.on_mouse_release(point, button, mods)

    def on_mouse_scroll(self, x, y, x_offset: float, y_offset: float):
        super().on_mouse_scroll(x, y, x_offset, y_offset)
        point = self.pixel_coords_to_space_coords(x, y)
        offset = self.pixel_coords_to_space_coords(x_offset, y_offset, relative=True)
        self.scene.on_mouse_scroll(point, offset)

    def on_key_release(self, symbol, modifiers):
        super().on_key_release(symbol, modifiers)
        self.scene.on_key_release(symbol, modifiers)

    def on_key_press(self, symbol, modifiers):
        super().on_key_press(symbol, modifiers)
        self.scene.on_key_press(symbol, modifiers)

    def on_resize(self, width: int, height: int):
        super().on_resize(width, height)
        self.scene.on_resize(width, height)

    def on_show(self):
        super().on_show()
        self.scene.on_show()

    def on_hide(self):
        super().on_hide()
        self.scene.on_hide()

    def on_close(self):
        super().on_close()
        self.scene.on_close()
