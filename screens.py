from kivy.uix.screenmanager import Screen, ScreenManager
from kivymd.uix.chip import MDChip
from kivymd.uix.card import MDCard
from kivy.uix.popup import Popup
from kivymd.uix.list import OneLineAvatarIconListItem
from kivymd.uix.textfield import MDTextField


class StartingScreen(Screen):
    pass


class MainScreen(Screen):
    pass


class Popup9(Popup):
    pass


class ClassListItem(OneLineAvatarIconListItem):
    pass


class GradeCarousel(MDCard):
    def open9(self):
        Popup9().open()


class CourseField(MDTextField):
    pass


class CreateAccountScreen(Screen):
    box_is_filled = False

    def take_username(self):
        username = self.ids.username.text
        password = self.ids.password.text
        if 0 < len(username) <= 20 and 0 < len(password) <= 50:
            self.box_is_filled = True
            # TODO: Figure out how to get screen manager elsewhere and change here maybe.


class LogInScreen(Screen):
    box_is_filled_login = False

    def take_username(self):
        username_login = self.ids.username_login.text
        password_login = self.ids.password_login.text
        if 0 < len(username_login) <= 20 and 0 < len(password_login) <= 50:
            self.box_is_filled_login = True
