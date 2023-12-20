from os import getcwd, path
from kivy.factory import Factory

from kivymd.tools.hotreload.app import MDApp
from kivy.core.window import Window
from kivy.uix.screenmanager import ScreenManager, FadeTransition

from screens import *

# Make sure you set DEBUG=1 in your PyCharm run configuration environment variables. Maybe.

sm: ScreenManager


class LifeJackIt(MDApp):
    KV_FILES = [
        path.join(getcwd(), "lifejackit.kv"),
    ]
    CLASSES = {
        "MainScreen": "screens",
        "StartingScreen": "screens",
        "CreateAccountScreen": "screens",
    }
    AUTORELOADER_PATHS = [
        (".", {"recursive": True}),
    ]
    sm = None

    def build_app(self, first=False):  # Previously build.
        global sm
        Window.size = (400, 600)
        if self.sm is None:
            self.sm = ScreenManager(transition=FadeTransition(duration=.5))
            self.sm.add_widget(StartingScreen(name='starting'))
            self.sm.add_widget(MainScreen(name='main'))
            self.sm.add_widget(CreateAccountScreen(name='account'))
            sm = self.sm
        return Factory.CreateAccountScreen()


if __name__ == '__main__':
    LifeJackIt().run()
