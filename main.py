from kivymd.app import MDApp
from kivy.core.window import Window
from kivy.uix.screenmanager import FadeTransition, ScreenManager

from screens import *


class LifeJackIt(MDApp):
    sm = None

    def build(self):
        Window.size = (400, 600)
        self.sm = ScreenManager(transition=FadeTransition(duration=.5))
        self.sm.add_widget(StartingScreen(name='starting'))
        self.sm.add_widget(MainScreen(name='main'))
        self.sm.add_widget(CreateAccountScreen(name='account'))
        self.sm.add_widget(LogInScreen(name='login'))
        self.sm.add_widget(Course1Screen(name='c1'))
        self.sm.add_widget(Course2Screen(name='c2'))
        self.sm.add_widget(Course3Screen(name='c3'))
        self.sm.add_widget(Course4Screen(name='c4'))
        self.sm.add_widget(BMICalculatorScreen(name='BMI'))
        return self.sm


if __name__ == '__main__':
    LifeJackIt().run()

