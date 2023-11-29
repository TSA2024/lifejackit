from os import getcwd, path
from kivy.factory import Factory

from kivymd.tools.hotreload.app import MDApp
from kivy.core.window import Window
from kivy.uix.screenmanager import ScreenManager, FadeTransition

from screens import *

# Make sure you set DEBUG=1 in your PyCharm run configuration environment variables. Maybe.


class AcaReady(MDApp):
    KV_FILES = [
        path.join(getcwd(), "acaready.kv"),
    ]
    CLASSES = {
        "MainScreen": "screens",
    }
    AUTORELOADER_PATHS = [
        (".", {"recursive": True}),
    ]
    sm = None

    def build_app(self, first=False):  # Previously build.
        Window.size = (600, 850)
        if self.sm is None:
            self.sm = ScreenManager(transition=FadeTransition(duration=.5))
            self.sm.add_widget(MainScreen(name='main'))
        return Factory.MainScreen()


if __name__ == '__main__':
    AcaReady().run()
