from kivymd.app import MDApp
from kivy.core.window import Window
from kivy.uix.screenmanager import FadeTransition, ScreenManager

from screens import *
from kivy.uix.popup import Popup
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput

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
        return self.sm

    class LifeJackIt(MDApp):
        def show_popup(self, title):
            # Create a Popup instance
            popup = Popup(title=title, size_hint=(None, None), size=(400, 400))

            # Create content for the Popup
            layout = GridLayout(cols=1)
            layout.add_widget(Label(text=f'Write "{title}" in the box below'))
            text_input = TextInput()
            layout.add_widget(text_input)

            # Define the function to be called when the button is pressed
            def submit_button_pressed(instance):
                print(f"{title} entered:", text_input.text)
                popup.dismiss()

            submit_button = Button(text='Submit')
            submit_button.bind(on_release=submit_button_pressed)
            layout.add_widget(submit_button)

            # Add content to the Popup
            popup.content = layout

            # Open the Popup
            popup.open()

if __name__ == '__main__':
    LifeJackIt().run()

KV = '''
MDBoxLayout:
    orientation: "vertical"

    MDTopAppBar:
        title: "MDTopAppBar"
        left_action_items: [["menu", lambda x: app.callback(x)]]
        right_action_items: [["dots-vertical", lambda x: app.callback(x)]]

    MDLabel:
        text: "Content"
        halign: "center"
'''



