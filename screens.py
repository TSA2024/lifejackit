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
        self.box_is_filled = (self.check_username_length(self.ids.username)
                              and self.check_password_length(self.ids.password))
        if not self.box_is_filled:
            return

    def check_username_length(self, instance_textfield):
        username = instance_textfield.text
        instance_textfield.error = not (0 < len(username) <= 20)
        return instance_textfield.error

    def check_password_length(self, instance_textfield):
        password = self.ids.password.text
        instance_textfield.error = not(0 < len(password) <= 50)
        return instance_textfield.error


class LogInScreen(Screen):
    box_is_filled_login = False

    def take_username(self):
        username_login = self.ids.username_login.text
        password_login = self.ids.password_login.text
        if 0 < len(username_login) <= 20 and 0 < len(password_login) <= 50:
            self.box_is_filled_login = True
        else:
            self.box_is_filled_login = False
