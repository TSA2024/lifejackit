from kivymd.app import MDApp
from kivy.core.window import Window
from kivy.uix.screenmanager import FadeTransition

from screens import *


class LifeJackIt(MDApp):
    sm = None

    def build(self):
        Window.size = (400, 600)
        self.sm = ScreenManager(transition=FadeTransition(duration=.5))
        self.sm.add_widget(StartingScreen(name='starting'))
        self.sm.add_widget(MainScreen(name='main'))
        return self.sm


if __name__ == '__main__':
    LifeJackIt().run()
