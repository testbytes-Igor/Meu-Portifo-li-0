from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
import json
import os

# --- Telas ---
class WelcomeScreen(Screen):
    pass

class RegisterScreen(Screen):
    def register_user(self, role):
        name = self.ids.name.text
        age = self.ids.age.text
        desc = self.ids.desc.text

        if not name or not age or not desc:
            self.ids.status.text = "Preencha todos os campos!"
            return

        user = {"name": name, "age": age, "desc": desc, "role": role}

        if not os.path.exists("users.json"):
            with open("users.json", "w") as f:
                json.dump([], f)

        with open("users.json", "r") as f:
            users = json.load(f)

        users.append(user)

        with open("users.json", "w") as f:
            json.dump(users, f)

        self.manager.current = "list"

class ListScreen(Screen):
    def on_pre_enter(self):
        self.ids.user_list.clear_widgets()

        role = self.manager.get_screen('register').ids.role.text
        target_role = "Ouvinte" if role == "Apoiado" else "Apoiado"

        with open("users.json", "r") as f:
            users = json.load(f)

        for user in users:
            if user["role"] == target_role:
                self.ids.user_list.add_widget(Label=(text=f'{user["name"]}, {user["age"]} - {user["desc"]}'))
                

class MyApp(App):
    def build(self):
        return Builder.load_file("interface.kv")

if __name__ == "__main__":
    MyApp().run()