from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput

class ConnectPage(GridLayout):
	def __init__(self,**kwargs):
		super().__init__(**kwargs)

		self.cols = 2

		self.add_widget(Label(text = "IP : "))
		self.ip = TextInput(multiline = True)
		self.add_widget(self.ip)

		self.add_widget(Label(text = "PORT : "))
		self.port = TextInput(multiline = True)
		self.add_widget(self.port)

		self.add_widget(Label(text = "Username : "))
		self.username = TextInput(multiline = True)
		self.add_widget(self.username)

class EpicApp(App):
    def build(self):
        return ConnectPage()

if __name__ == '__main__':
	EpicApp().run()