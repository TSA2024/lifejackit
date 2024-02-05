from kivy.core.window import Window
from kivy.metrics import dp
from kivy.properties import StringProperty, NumericProperty
from kivy.clock import Clock

from kivy.uix.widget import WidgetException
from kivy.uix.accordion import AccordionItem
from kivy.uix.label import Label
from kivy.uix.popup import Popup
from kivy.uix.screenmanager import Screen
from kivy.uix.textinput import TextInput
from kivy.uix.textinput import TextInput

from kivymd.uix.button import MDRaisedButton
from kivymd.uix.card import MDCard
from kivymd.uix.floatlayout import MDFloatLayout
from kivymd.uix.list import OneLineAvatarIconListItem
from kivymd.uix.tab import MDTabsBase
from kivymd.uix.textfield import MDTextField
from kivymd.uix.menu import MDDropdownMenu
from kivymd.uix.pickers import MDDatePicker

from data import faq, quotes, aspirations, appointment_people
from database import query, update

from datetime import date


times = [
    "08:00 AM",
    "09:00 AM",
    "01:00 PM",
    "02:00 PM",
    "03:00 PM",
    "04:00 PM",
    "05:00 PM",
    "07:00 PM",
    "08:00 PM",
    "09:00 PM",
    "10:00 PM",
]


class Tab(MDFloatLayout, MDTabsBase):
    pass


class StartingScreen(Screen):
    pass


class MainScreen(Screen):
    aspiration_popup_i = 0
    appointments = []
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
                    text_size=(self.width * 3.4, None),
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
                person="Dr. Orr",
                date="02/15/2024",
                time="12:00 PM"
            )
        )
        self.add_appointment(
            AppointmentCard(
                person="Dr. Haber",
                date="02/23/2024",
                time="11:00 AM"
            )
        )

    def make_appointment(self):
        # TODO:
        AppointmentPopup(self).open()

    def add_appointment(self, appointment):
        if appointment in self.appointments:
            return
        self.appointments.append(appointment)
        self.appointments = sorted(self.appointments, key=lambda x: (x.date[-4:], x.date, x.time[-2:], x.time))
        if appointment.time in times:
            times.remove(appointment.time)
        self.reset_appointments()

    def delete_appointment(self, appointment):
        if appointment not in self.appointments:
            return
        self.appointments.remove(appointment)
        self.reset_appointments()
        # TODO: Make time available again.

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

        self.ids.no_appointments.text = "[i]No appointments yet.[/i]" if len(self.appointments) == 0 else ""

        self.ids.quote_label.text = quotes[0] if quotes else "No quotes available"

        # Schedule the function to update the quote every 30 seconds
        Clock.schedule_interval(self.update_quote, 30)
        Clock.schedule_interval(self.clear_text, 30)

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

        self.ids.no_appointments.text = "[i]No appointments yet.[/i]" if len(
            self.appointments) == 0 else "Your Appointments:"

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

    def update_quote(self, dt):
        # This function is called at regular intervals (every 30 seconds)
        current_index = quotes.index(self.ids.quote_label.text)
        next_index = (current_index + 1) % len(quotes)
        self.ids.quote_label.text = quotes[next_index]

    def clear_text(self, dt):
        # Access the MDTextField with id "reflection" and clear its text
        # This function is called at regular intervals (every 30 seconds)
        reflection_textfield = self.ids.reflection
        reflection_textfield.text = ""


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


class AppointmentPopup(Popup):
    date = StringProperty()
    time = StringProperty()
    person = StringProperty()

    inactive_color = (0.5, 0.5, 0.5, 1)
    active_color = (82/255, 1, 82/255, 1)

    def __init__(self, main_screen, **kwargs):
        super().__init__(**kwargs)
        self.main_screen = main_screen
        self.date = ""
        self.time = ""
        self.person = ""
        self.date_picker = None
        self.time_picker = None

        self.ids.date_button.md_bg_color = self.inactive_color
        self.ids.time_button.md_bg_color = self.inactive_color
        self.ids.confirm.md_bg_color = self.inactive_color

        self.people_menu = MDDropdownMenu(
            caller=self.ids.person_dropdown,
            items=[
                {
                    "text": name,
                    "viewclass": "OneLineListItem",
                    "on_release": lambda x=name: self.set_appointment_person(x)
                } for name in appointment_people
            ],
            width_mult=4,
            max_height=dp(300)
        )

    def set_appointment_person(self, person):
        self.person = person
        self.people_menu.dismiss()
        self.ids.person_dropdown.text = person
        self.ids.date_button.md_bg_color = self.active_color

    def show_date_picker(self):
        if self.person == "":
            return
        # TODO: Minimum date stuff.
        self.date_picker = MDDatePicker(
            min_date=date.today(),
            max_date=date(date.today().year + 4, 12, 31)
        )
        self.date_picker.bind(on_save=self.on_date_save)
        Window.size = (Window.size[0]-1, Window.size[1])
        Window.size = (Window.size[0]+1, Window.size[1])
        self.date_picker.open()

    def on_date_save(self, instance, value, date_range):
        self.date = value.strftime("%m/%d/%Y")
        self.ids.time_button.md_bg_color = self.active_color
        self.ids.date_label.text = self.date
        self.date_picker.dismiss()

    def show_time_selector(self):
        if self.date == "":
            return
        self.time_picker = TimePopup(times=times, on_save=self.on_time_save_selector)
        self.time_picker.open()

    def on_time_save(self, instance, value):
        # Don't use anymore.
        self.time = value.strftime("%I:%M %p")
        self.ids.time_label.text = self.time
        self.ids.confirm.md_bg_color = self.active_color
        self.time_picker.dismiss()

    def on_time_save_selector(self, instance, value):
        self.time = value
        self.ids.time_label.text = self.time
        self.ids.confirm.md_bg_color = self.active_color

    def confirm_appointment(self):
        if self.time == "":
            return
        self.main_screen.add_appointment(
            AppointmentCard(
                person=self.person,
                date=self.date,
                time=self.time
            )
        )
        self.dismiss()


class TimePopup(Popup):
    on_save = None
    default_color = (82/255, 148/255, 1, 1)
    inactive_color = (0.5, 0.5, 0.5, 1)
    active_color = (82/255, 1, 82/255, 1)

    def __init__(self, times, on_save, **kwargs):
        super().__init__(**kwargs)
        self.on_save = on_save
        self.selected = None

        for time in times:
            self.ids.time_grid.add_widget(MDRaisedButton(text=time, on_release=self.on_time_button, md_bg_color=self.default_color))

    def on_time_button(self, instance):
        if self.selected is not None:
            self.selected.md_bg_color = self.default_color
        else:
            self.ids.confirm.md_bg_color = self.active_color
        instance.md_bg_color = self.active_color
        self.selected = instance

    def on_save_button(self):
        if self.selected is None:
            return
        self.on_save(self, self.selected.text)
        self.dismiss()
