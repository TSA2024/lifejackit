from kaki.app import App
from kivy.factory import Factory

from kivymd.app import MDApp
from kivy.core.window import Window
from kivy.uix.screenmanager import ScreenManager, Screen, FadeTransition


class AcaReady(MDApp):
    def build(self):
        Window.size = (600, 850)
        sm = ScreenManager(transition=FadeTransition(duration=.5))
        sm.add_widget(MainScreen(name='main'))
        return sm


class MainScreen(Screen):
    pass


if __name__ == '__main__':
    print("fskjlddfskjfdk")

    AcaReady().run()
