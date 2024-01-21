from kivy.uix.screenmanager import Screen, ScreenManager


class StartingScreen(Screen):
    pass


class MainScreen(Screen):
    pass


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
