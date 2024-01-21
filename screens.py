from kivy.core.window import Window
from kivy.metrics import dp
from kivy.uix.screenmanager import Screen, ScreenManager

from kivymd.app import MDApp
from kivymd.uix.menu import MDDropdownMenu
from kivymd.uix.snackbar import Snackbar

from database import query, update


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
        username = self.ids.username
        password = self.ids.password
        self.box_is_filled = not (self.check_username_length(username)
                              or self.check_password_length(password))
        if self.box_is_filled:
            if query("SELECT * FROM users WHERE username = %s", (username.text,)).fetchone() is None:
                update("INSERT INTO users (username, password) VALUES (%s, %s)", (username.text, password.text))
            else:
                username.helper_text = "Username is taken."
                username.error = True
                self.box_is_filled = False

    def check_username_length(self, instance_textfield):
        # TODO: Maybe one day make sure there are no spaces in the username.
        username = instance_textfield.text
        instance_textfield.error = not (0 < len(username) <= 20)
        return instance_textfield.error

    def check_password_length(self, instance_textfield):
        password = instance_textfield.text
        instance_textfield.error = not(0 < len(password) <= 50)
        return instance_textfield.error


class LogInScreen(Screen):
    box_is_filled_login = False

    def take_username(self):
        username = self.ids.username_login
        password = self.ids.password_login
        self.box_is_filled_login = not (self.check_username_length(username)
                              or self.check_password_length(password))
        if self.box_is_filled_login:
            if query("SELECT * FROM users WHERE username = %s AND password = %s", (username.text, password.text)).fetchone() is None:
                username.error = True
                password.helper_text = "Invalid login."
                password.error = True
                self.box_is_filled_login = False

    def check_username_length(self, instance_textfield):
        username = instance_textfield.text
        instance_textfield.error = not (0 < len(username) <= 20)
        return instance_textfield.error

    def check_password_length(self, instance_textfield):
        password = instance_textfield.text
        instance_textfield.error = not(0 < len(password) <= 50)
        return instance_textfield.error
