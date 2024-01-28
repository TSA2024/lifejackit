from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.metrics import dp
from kivy.uix.accordion import AccordionItem
from kivy.uix.label import Label

from data import faq


class StartingScreen(Screen):
    pass


class MainScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.ids.box.clear_widgets()
        for q in faq:
            a = AccordionItem(
                title=q,
            )
            self.ids.box.add_widget(a)
            height = dp(50)
            a.add_widget(
                Label(
                    text=faq[q],
                    text_size=(self.width*3.4, None),
                    halign="left",
                    color=(0, 0, 0, 1),
                    height=height,
                )
            )
            self.ids.box.height += height



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
