from kivy.core.window import Window
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivymd.uix.button import MDIconButton, MDTextButton
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.gridlayout import MDGridLayout

from kivymd.uix.button import MDIconButton

from rocket_kitchens_local_bot import local_bot

import kivymd
from kivymd.app import MDApp


import os


class RobotInterface(MDApp):

    def build(self):
        """
            Rocket Kitchens:: Local bot

            This programs builds the user interface to access
            the robot installed on the local machine.

            The program keeps reading the state of the file
            used to pass the parameters to activate the task process
            --------------------------------------------------------


            return::  User Interface Application


        """

        self.title = "Rocket Kitchens Local bot"

        Window.size = (400, 200)
        layout = MDGridLayout(cols=2,rows=2,padding=2)

        username_input = TextInput()
        password_input = TextInput(password=False)
        usernamelbl = Label(text="Username", size_hint_x=None, width=100)

        passwordlbl = Label(text="Password", size_hint_x=None, width=100)


        layout.add_widget(username_input)
        layout.add_widget(password_input)
        layout.add_widget(usernamelbl)
        layout.add_widget(passwordlbl)


        main_layout = MDBoxLayout(orientation='vertical')
        main_layout.add_widget(layout)

        login_button = MDTextButton(text="Login")
        main_layout.add_widget(login_button)

        return main_layout


if __name__ == "__main__":

    app = RobotInterface()
    app.run()



