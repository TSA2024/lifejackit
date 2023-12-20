from kivymd.app import MDApp
from kivy.core.window import Window
from kivy.uix.screenmanager import FadeTransition

from screens import *
from database import create_tables


class LifeJackIt(MDApp):
    sm = None

    def build(self):
        Window.size = (400, 600)
        self.sm = ScreenManager(transition=FadeTransition(duration=.5))
        self.sm.add_widget(StartingScreen(name='starting'))
        self.sm.add_widget(MainScreen(name='main'))
        self.sm.add_widget(CreateAccountScreen(name='account'))
        return self.sm


if __name__ == '__main__':
    create_tables()
    LifeJackIt().run()
