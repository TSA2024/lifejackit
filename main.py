from kaki.app import App
from os import getcwd, path
from kivy.factory import Factory

# from kivymd.app import MDApp
from kivymd.tools.hotreload.app import MDApp
from kivy.core.window import Window
from kivy.uix.screenmanager import ScreenManager, FadeTransition

from screens import *


class AcaReady(App, MDApp):
    KV_FILES = [
        path.join(getcwd(), "acaready.kv")
    ]
    CLASSES = {
        "MainScreen": "screens",
    }
    AUTORELOADER_PATHS = [
        (".", {"recursive": True}),
    ]

    def build_app(self, first=False):  # Previously build.
        print("build_app called.")
        Window.size = (600, 850)
        self.sm = ScreenManager(transition=FadeTransition(duration=.5))
        self.sm.add_widget(MainScreen(name='main'))
        return Factory.MainScreen()


if __name__ == '__main__':
    AcaReady().run()
