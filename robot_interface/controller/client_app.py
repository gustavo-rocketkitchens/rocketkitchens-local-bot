import psycopg2
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput


class CRUDApp(App):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.conn = None
        self.cur = None

    def connect(self):
        self.conn = psycopg2.connect(
            host="localhost",
            port="5432",
            dbname="rocket",
            user="rocket",
            password="123"
        )
        self.cur = self.conn.cursor()

    def disconnect(self):
        self.cur.close()
        self.conn.close()

    def create(self, name):
        self.cur.execute("INSERT INTO users(name) VALUES (%s)", (name,))
        self.conn.commit()

    def read(self):
        self.cur.execute("SELECT * FROM mytable;")
        rows = self.cur.fetchall()
        return rows

    def update(self, id, name):
        self.cur.execute("UPDATE users SET name = %s WHERE id = %s", (name, id))
        self.conn.commit()

    def delete(self, id):
        self.cur.execute("DELETE FROM users WHERE id = %s", (id,))
        self.conn.commit()

    def build(self):
        self.connect()
        layout = BoxLayout(orientation='vertical')

        # Create
        create_layout = BoxLayout(orientation='horizontal')
        create_label = Label(text='Name: ')
        create_input = TextInput()
        create_button = Button(text='Create')

        def create_callback(instance):
            self.create(create_input.text)
            create_input.text = ''

        create_button.bind(on_press=create_callback)
        create_layout.add_widget(create_label)
        create_layout.add_widget(create_input)
        create_layout.add_widget(create_button)
        layout.add_widget(create_layout)

        # Read
        read_label = Label(text='Users:')
        layout.add_widget(read_label)

        for row in self.read():
            row_layout = BoxLayout(orientation='horizontal')
            id_label = Label(text=str(row[0]))
            name_label = Label(text=row[1])
            row_layout.add_widget(id_label)
            row_layout.add_widget(name_label)
            layout.add_widget(row_layout)

        # Update
        update_layout = BoxLayout(orientation='horizontal')
        update_id_label = Label(text='ID: ')
        update_id_input = TextInput()
        update_name_label = Label(text='Name: ')
        update_name_input = TextInput()
        update_button = Button(text='Update')

        def update_callback(instance):
            self.update(update_id_input.text, update_name_input.text)
            update_id_input.text = ''
            update_name_input.text = ''

        update_button.bind(on_press=update_callback)
        update_layout.add_widget(update_id_label)
        update_layout.add_widget(update_id_input)
        update_layout.add_widget(update_name_label)
        update_layout.add_widget(update_name_input)
        update_layout.add_widget(update_button)
        layout.add_widget(update_layout)

        # Delete
        delete_layout = BoxLayout(orientation='horizontal')
        delete_id_label = Label(text='ID: ')
        delete_id_input = TextInput()
        delete_button = Button(text='Delete')

        def delete_callback(instance):
            self.delete(delete_id_input.text)
            delete_id_input.text = ''

        delete_button.bind(on_press=delete_callback)
        delete_layout.add_widget(delete_id_label)
        delete_layout.add_widget(delete_id_input)
        delete_layout.add_widget(delete_button)
        layout.add_widget(delete_layout)  # <-- add this line to add delete_layout to the main layout

CRUDApp().run()