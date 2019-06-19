from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.screenmanager import ScreenManager, Screen
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

		with open('prev_details.txt','w') as f:
			f.write(f'{ip},{port},{username}')

		info = f'Attempting to join {ip}:{port} as {username}'
		chat_app.infopage.update_info(info)        	# update the msg to be displayed on infopage

		chat_app.screenmanager.current = 'Info'		# change screen of the app

class InfoPage(GridLayout):
	def __init__(self,**kwargs):
		super().__init__(**kwargs)
		self.cols = 1

		self.message = Label(halign = 'center',valign = 'middle',font_size = 30)
		self.message.bind(width = self.update_text)
		self.add_widget(self.message)

	def update_info(self,message):
		self.message.text = message	

	def update_text(self,*_):
		self.message.text_size = (self.message.width*0.9, None)


class EpicApp(App):
    def build(self):
        self.screenmanager = ScreenManager()

        self.connectpage = ConnectPage()
        self.screen = Screen(name ='Connect')
        self.screen.add_widget(self.connectpage)
        self.screenmanager.add_widget(self.screen)

        self.infopage = InfoPage()
        self.screen = Screen(name ='Info')
        self.screen.add_widget(self.infopage)
        self.screenmanager.add_widget(self.screen)

        return self.screenmanager

if __name__ == '__main__':
	chat_app =  EpicApp()		# create instance so we can use it for referencing stuff
	chat_app.run()