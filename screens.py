from kivy.core.window import Window
from kivy.metrics import dp
from kivy.uix.screenmanager import Screen, ScreenManager
from kivymd.uix.chip import MDChip
from kivymd.uix.card import MDCard
from kivy.uix.popup import Popup
from kivymd.uix.list import OneLineAvatarIconListItem
from kivymd.uix.textfield import MDTextField
from kivy.uix.widget import WidgetException

from kivy.uix.screenmanager import Screen
from kivy.properties import StringProperty, NumericProperty
from kivy.uix.accordion import AccordionItem
from kivy.uix.label import Label
from kivymd.uix.card import MDCard
from kivy.uix.popup import Popup

from kivymd.uix.floatlayout import MDFloatLayout
from kivymd.uix.tab import MDTabsBase

from database import query, update
from data import faq

from kivy.uix.textinput import TextInput


class Tab(MDFloatLayout, MDTabsBase):
    pass


class StartingScreen(Screen):
    pass


class MainScreen(Screen):
    appointments = set()
    keep = []
    confirmation_popup = None

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
        # Appointments stuff.
        # TODO: Put actual appointments later.
        self.add_appointment(
            AppointmentCard(
                person="Dr. Le",
                date="2/15/2024",
                time="12:00 PM"
            )
        )
        self.add_appointment(
            AppointmentCard(
                person="Dr. Misra",
                date="2/23/2024",
                time="11:00 AM"
            )
        )

    def add_appointment(self, appointment):
        if appointment in self.appointments:
            return
        self.appointments.add(appointment)
        self.reset_appointments()

    def delete_appointment(self, appointment):
        if appointment not in self.appointments:
            return
        self.appointments.remove(appointment)
        self.reset_appointments()

    def reset_appointments(self):
        self.keep = [self.ids.a1, self.ids.no_appointments, self.ids.a2, self.ids.make_appointment, self.ids.a3]
        self.ids.appointments.clear_widgets()
        self.ids.appointments.add_widget(self.keep[0])
        self.ids.appointments.add_widget(self.keep[1])
        for appointment in self.appointments:
            try:
                self.ids.appointments.add_widget(appointment)
            except WidgetException:
                continue
        for i in range(2, len(self.keep)):
            self.ids.appointments.add_widget(self.keep[i])
        self.ids.no_appointments.text = "[i]No appointments yet.[/i]" if len(
            self.appointments) == 0 else "Your Appointments:"

    def select(self, text_item):
        self.menu.dismiss()
        # Snackbar(text=text_item).open()
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


class AppointmentCard(MDCard):
    person = StringProperty()
    date = StringProperty()
    time = StringProperty()

    def open_confirmation(self, question):
        self.confirmation_popup = ConfirmationPopup(question=question, on_confirm=lambda: (self.delete_appointment()))
        self.confirmation_popup.open()

    def delete_appointment(self):
        self.parent.parent.parent.parent.parent.parent.parent.parent.parent.parent.parent.parent.delete_appointment(self)


class ConfirmationPopup(Popup):
    question = StringProperty()

    def __init__(self, question, on_confirm, **kwargs):
        super().__init__(**kwargs)
        self.question = question
        self.on_confirm = on_confirm

        def on_press(_):
            on_confirm()
            self.dismiss()

        self.ids.confirm.bind(on_press=on_press)
