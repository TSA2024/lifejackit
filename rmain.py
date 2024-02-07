from os import getcwd, path

from kivy.core.window import Window
from kivy.factory import Factory

from screens import *

from kivymd.tools.hotreload.app import MDApp
from kivy.uix.screenmanager import ScreenManager, FadeTransition

# from database import create_tables

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
        "LogInScreen": "screens",
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
            self.sm.add_widget(LogInScreen(name='login'))
            self.sm.add_widget(Course1Screen(name='c1'))
            self.sm.add_widget(Course2Screen(name='c2'))
            self.sm.add_widget(Course3Screen(name='c3'))
            self.sm.add_widget(Course4Screen(name='c4'))
            sm = self.sm
        return Factory.MainScreen()


if __name__ == '__main__':
    # create_tables()
    LifeJackIt().run()

