from kivy.core.window import Window
from kivy.metrics import dp
from kivy.uix.screenmanager import Screen, ScreenManager
from kivymd.app import MDApp
from kivymd.uix.menu import MDDropdownMenu
from kivymd.uix.snackbar import Snackbar


class StartingScreen(Screen):
    pass


class MainScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.display_menu = MDDropdownMenu(
            items=[
                {
                    "text": option,
                    "on_release": lambda x=option: self.select(x)
                } for option in ("Item 1", "Item 2", "Item 3")
            ],
            width_mult=3,
            max_height=dp(150),
        )

    def select(self, text_item):
        self.menu.dismiss()
        #Snackbar(text=text_item).open()
        print(text_item)

    def new_data_table_size(self):
        new_values = (
                ("", max(Window.width * 0.099, dp(55))),
                ("", max(Window.width * 0.099, dp(55))),
                ("", max(Window.width * 0.099, dp(55))),
        )
        return new_values

    def callback(self, button):
        self.display_menu.caller = button
        self.display_menu.open()



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






