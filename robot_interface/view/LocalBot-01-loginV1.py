from kivymd.uix.label import MDLabel
from kivymd.uix.screenmanager import MDScreenManager

from rocket_kitchens_local_bot.robot_interface.model.credentials import passport as ps

def credential():
    dict_credential = {
        "ahmd@rocketkitchens.com": "ahmd123",
        "hassan@rocketkitchens.com": "hassan123",
        "accounts@rocketkitchens.com": "accounts123",
        "marwan@rocketkitchens.com": "marwan123",
        "gustavo@rocketkitchens.com": "gustavo123"
    }
    return dict_credential


cred = ps.credential()

# main.py

from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput

from kivymd.uix.screen import MDScreen
# from kivymd.tools.hotreload.app import MDApp
from kivymd.app import MDApp
from kivymd.uix.card import MDCard



class LoginScreen(MDScreen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        layout = BoxLayout(orientation='vertical')

        self.username_input = TextInput(hint_text='Username')
        layout.add_widget(self.username_input)

        self.password_input = TextInput(hint_text='Password', password=True)
        layout.add_widget(self.password_input)

        login_button = Button(text='Login', on_press=self.login)
        layout.add_widget(login_button)

        self.add_widget(layout)

        #================================

    def login(self, instance):
        username = self.username_input.text
        password = self.password_input.text

        # Check login credentials
        if cred.get(username) == password:
            # Login successful, go to main screen
            self.manager.current = 'main_page'
        else:
            # Login failed
            self.username_input.text = ''
            self.password_input.text = ''
            self.username_input.hint_text = 'Invalid username or password'
            self.password_input.hint_text = 'Invalid username or password'


class MainScreen(MDScreen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.add_widget(MDLabel(text='Welcome to the main screen!'))


class ScreenManagementApp(MDApp):
    def build(self):
        self.screen_manager = MDScreenManager()

        self.login_screen = LoginScreen(name='login_screen')
        self.main_screen = MainScreen(name='main_page')

        self.screen_manager.add_widget(self.login_screen)
        self.screen_manager.add_widget(self.main_screen)

        return self.screen_manager


if __name__ == '__main__':
    ScreenManagementApp().run()
