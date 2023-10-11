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
    def uppercase(self, text):
        upper = "ABCDEFGHIJKLMNOPQESTUVWXYZ"
        istrue = False
        for letter in text:
            if letter in upper:
                istrue = True
        return istrue
    def lowercase(self, text):
        lower = "abcdefghijklmnopqrstuvwxyz"
        istrue = False
        for letter in text:
            if letter  in lower:
                istrue = True
        return istrue
    def number(self, text):
        num = "1234567890"
        istrue = False
        for letter in text:
            if letter in num:
                istrue = True
        return istrue
    def special_char(self, text):
        special_char = "!@#$%^&*()?"
        istrue = False
        for letter in text:
            if letter in special_char:
                istrue = True
        return istrue

    def user_input(self, text):
        if text in users:
            self.ids.NotNewUser.text = "User already exists"
        elif text == "":
            self.ids.NotNewUser.text = "Please enter a username and password"
        elif self.uppercase(text) and self.lowercase(text) and self.number(text) and self.special_char(text) == True:
            users[self.ids.new_user.text] = [self.ids.new_pass.text]
            self.manager.current = "login page"
        else:
            self.ids.NotNewUser.text = "Password does not follow parameters."
        # else:
        #     users[self.ids.new_user.text] = [self.ids.new_pass.text]
        #     self.manager.current = "login page"

    # def good_pass(self, username, password):
        # for text in self.ids.new_pass.text:
        # if self.uppercase(password) and self.lowercase(password) and self.number(password) and self.special_char(password) == True:
        #     users[self.ids.new_user.text] = [self.ids.new_pass.text]
        #     self.manager.current = "login page"
        # else:
        #     self.NotNewUser.text = "Password does not follow parameters."

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