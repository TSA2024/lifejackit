from kivy.core.window import Window
from kivy.metrics import dp
from kivy.properties import NumericProperty
from kivy.uix.accordion import AccordionItem
from kivymd.uix.button import MDRaisedButton
from kivy.uix.label import Label
from kivy.uix.popup import Popup
from kivy.uix.screenmanager import Screen
from kivy.uix.textinput import TextInput
from kivymd.uix.card import MDCard
from kivymd.uix.floatlayout import MDFloatLayout
from kivymd.uix.list import OneLineAvatarIconListItem
from kivymd.uix.tab import MDTabsBase
from kivymd.uix.textfield import MDTextField

from data import faq, aspirations
from database import query, update


class Tab(MDFloatLayout, MDTabsBase):
    pass


class StartingScreen(Screen):
    pass


class MainScreen(Screen):
    aspiration_popup_i = 0

    def callback(self, button):
        self.display_menu.caller = button
        self.display_menu.open()

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

    def show_popup(self, title):
        # Create a Popup instance
        self.popup = Popup(title=title, size_hint=(.8, .5))

        # Create content for the Popup
        layout = MDFloatLayout()
        layout.add_widget(Label(text=f'Write "{title}" in the box below', pos_hint={"center_x": 0.5, "center_y": 0.87}))
        self.text_input = TextInput(size_hint=(1, .5), pos_hint={"center_x": 0.5, "center_y": 0.5})
        layout.add_widget(self.text_input)

        self.aspiration_popup_i = int(title.split("#")[-1]) - 1
        self.text_input.text = aspirations[self.aspiration_popup_i]

        # Define the function to be called when the button is pressed
        def submit_button_pressed(instance):
            print(f"{title} entered:", self.text_input.text)
            aspirations[self.aspiration_popup_i] = self.text_input.text
            # Store the text input value
            self.popup.text_value = self.text_input.text
            self.popup.dismiss()

        submit_button = MDRaisedButton(text='Submit', size_hint=(.5, .18), md_bg_color=(113/255, 201/255, 135/255, 1), pos_hint={"center_x": 0.5, "center_y": 0.12})
        submit_button.bind(on_release=submit_button_pressed)
        layout.add_widget(submit_button)

        # Add content to the Popup
        self.popup.content = layout

        # Open the Popup
        self.popup.open()


class ClassListItem(OneLineAvatarIconListItem):
    pass


class GradeCarousel(MDCard):
    program_number = NumericProperty(0)


class CourseField(MDTextField):
    pass


class Course1Screen(Screen):
    pass


class Course2Screen(Screen):
    pass


class Course3Screen(Screen):
    pass


class Course4Screen(Screen):
    pass


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
        instance_textfield.error = not (0 < len(password) <= 50)
        return instance_textfield.error


class LogInScreen(Screen):
    box_is_filled_login = False

    def take_username(self):
        username = self.ids.username_login
        password = self.ids.password_login
        self.box_is_filled_login = not (self.check_username_length(username)
                                        or self.check_password_length(password))
        if self.box_is_filled_login:
            if query("SELECT * FROM users WHERE username = %s AND password = %s",
                     (username.text, password.text)).fetchone() is None:
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
        instance_textfield.error = not (0 < len(password) <= 50)
        return instance_textfield.error
