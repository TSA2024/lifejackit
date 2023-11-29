from kivymd.app import MDApp
from kivy.core.window import Window
from kivy.uix.screenmanager import ScreenManager, FadeTransition

from screens import *


class AcaReady(MDApp):
    sm = None

    def build(self):
        Window.size = (600, 850)
        self.sm = ScreenManager(transition=FadeTransition(duration=.5))
        self.sm.add_widget(MainScreen(name='main'))
        return self.sm


if __name__ == '__main__':
    AcaReady().run()
