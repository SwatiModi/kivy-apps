from kivy.app import App

from kivy.uix.button import Button

class TestApp(App):

    def build(self):

        return Button(text="Hello world, from a nice blog")

TestApp().run()