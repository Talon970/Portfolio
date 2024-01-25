from kivy.app import App
from kivy.uix.boxlayout import BoxLayout

class MyWidget(BoxLayout):
    def change_label_text(self, *args):
        self.ids.my_label.text = "Text geändert!"

class MyApp(App):
    def build(self):
        return MyWidget()

if __name__ == '__main__':
    MyApp().run()
