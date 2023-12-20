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
