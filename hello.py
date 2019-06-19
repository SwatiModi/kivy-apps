import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button

class ConnectPage(GridLayout):
    def __init__(self,**kwargs):
    	super().__init__(**kwargs)
    	self.cols = 2
    	
    	self.add_widget(Label(text = "Name : "))
    	self.name = TextInput(multiline = True)
    	self.add_widget(self.name)
    	self.hello = Button(text = 'Greet Me')
    	self.add_widget(self.hello)
    	self.hello.bind(on_press = self.say_hello)
    	self.message = Label()

    	self.add_widget(self.message)

    def say_hello(self,instance):
    	self.update_display_msg(self.name.text)

    def update_display_msg(self,message):
    	self.hello.text = ''
    	self.message.text = 'Hello ' + message + ', Welcome to my first Kivy App'

class TestApp(App):
	def build(self):
		return ConnectPage()

if __name__ == '__main__':
	TestApp().run()