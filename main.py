from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.lang import Builder

users = {"SeanM066":"Sean070706"}

Builder.load_file("LoginPage.kv")
class LoginPageApp(App):
    def build(self):
        return LoginManager()

class LoginManager(ScreenManager):
     pass

class LoginScreen(Screen):
    def user_input(self, text):
        if text in users:
            self.manager.current = "welcome"
        else:
            self.ids.wrong.text = "Username not found"

    def advance(self):
        self.manager.current = "new user"


class NewUserScreen(Screen):
    def user_input(self, text):
        if text in users:
            self.ids.NotNewUser.text = "User already exists"
        else:
            users[self.ids.new_user.text] = [self.ids.new_pass.text]
            self.manager.current = "login page"

    def advance(self):
        self.manager.current = "login page"

class WelcomeScreen(Screen):
    def advance(self):
        self.manager.current = "login page"

LoginPageApp().run()







#
# Builder.load_file("QuizPage.kv")
# class QuizPageApp(App):
#     def build(self):
#         return QuizManager()
#
# class QuizManager(ScreenManager):
#     pass
#
# class Question1Screen(Screen):
#     def answer_question(self, bool):
#         if bool:
#             self.manager.current = "correct"
#         else:
#             self.manager.current = "incorrect"
#
#
#
# class Question2Screen(Screen):
#     def answer_question(self, text):
#         if text == "4":
#             self.manager.current = "correct"
#             #self.ids.test.text = "correct"
#             #self.ids.test.font_size = 50
#         elif text.lower() == "four":
#             self.manager.current = "correct"
#         else:
#             self.manager.current = "incorrect"
#
#
# class CorrectScreen(Screen):
#     def advance(self):
#         self.manager.current = "question two"
#
# class IncorrectScreen(Screen):
#     def advance(self):
#         self.manager.current = "question two"
#
# QuizPageApp().run()