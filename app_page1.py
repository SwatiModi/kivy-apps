from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
import os

class ConnectPage(GridLayout):
	def __init__(self,**kwargs):
		super().__init__(**kwargs)

		self.cols = 2

		if os.path.isfile('prev_details.txt'):
			with open('prev_details.txt','r') as f:
				data = f.read().split(',')

				prev_ip = data[0]
				prev_port = data[1]
				prev_username = data[2]

		else :

				prev_ip = ''
				prev_port = ''
				prev_username = ''


		self.add_widget(Label(text = "IP : "))
		self.ip = TextInput(text = prev_ip,multiline = True)
		self.add_widget(self.ip)

		self.add_widget(Label(text = "PORT : "))
		self.port = TextInput(text = prev_port,multiline = True)
		self.add_widget(self.port)

		self.add_widget(Label(text = "Username : "))
		self.username = TextInput(text = prev_username,multiline = True)
		self.add_widget(self.username)

		self.submit = Button(text = 'Submit')
		self.add_widget(Label())
		self.submit.bind(on_press = self.submit_details)
		self.add_widget(self.submit)

	def submit_details(self,instance):
		ip = self.ip.text
		port = self.port.text
		username = self.username.text
		print(f'IP is {ip}, PORT is {port} for {username}') 

		with open('prev_details.txt','w') as f:
			f.write(f'{ip},{port},{username}')

class EpicApp(App):
    def build(self):
        return ConnectPage()

if __name__ == '__main__':
	EpicApp().run()