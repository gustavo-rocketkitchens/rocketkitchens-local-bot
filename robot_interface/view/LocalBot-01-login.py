from kivymd.app import MDApp
from kivy.lang.builder import Builder
from kivy.core.window import Window

from rocket_kitchens_local_bot.robot_interface.model.credentials import passport as ps
cred = ps.credential()

Window.size = (350, 400)
class MainApp(MDApp):

    def build(self):
        self.theme_cls.theme_style='Dark'
        return Builder.load_file('LocalBot-01-login.kv')

    def login(self, username, password):
        credentials = cred
        if username in credentials and credentials[username] == password:
            # Login successful
            print("Login successful!")
        else:
            # Login failed
            print("Invalid username or password")
MainApp().run()
