from kivy.uix.screenmanager import Screen, ScreenManager
from kivymd.uix.menu import MDDropdownMenu
from kivy.metrics import dp


class StartingScreen(Screen):
    pass


class MainScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        questions = ["Is it too late to start using LifeJackit after freshmen year?", "What's the purpose of this app?",
                     "How do I start turning my life around today?"]
        menu_items = [
            {
                "text": question,
                "viewclass": "OneLineListItem",
                "on_release": lambda x=question: self.menu_callback(x),
            } for question in questions
        ]
        self.help_menu = MDDropdownMenu(
            caller=self.ids.help_button,
            items=menu_items,
            width_mult=8,
            max_height=dp(200),
            position="center",


        )

    def menu_callback(self, text_item):
        print(text_item)


class CreateAccountScreen(Screen):
    box_is_filled = False

    def take_username(self):
        username = self.ids.username.text
        password = self.ids.password.text
        if 0 < len(username) <= 20 and 0 < len(password) <= 50:
            self.box_is_filled = True
        else:
            self.box_is_filled = False
            # TODO: Figure out how to get screen manager elsewhere and change here maybe.


class LogInScreen(Screen):
    box_is_filled_login = False

    def take_username(self):
        username_login = self.ids.username_login.text
        password_login = self.ids.password_login.text
        if 0 < len(username_login) <= 20 and 0 < len(password_login) <= 50:
            self.box_is_filled_login = True
        else:
            self.box_is_filled_login = False
