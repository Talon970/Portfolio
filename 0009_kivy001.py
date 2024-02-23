import kivy
from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.boxlayout import BoxLayout

# Definieren Sie die zwei verschiedenen Bildschirme
class FirstScreen(Screen):
    pass

class SecondScreen(Screen):
    pass

# Haupt-App
class MyApp(App):

    def build(self):
        # Erstellen eines ScreenManagers
        self.sm = ScreenManager()

        # Erster Bildschirm
        screen1 = FirstScreen(name='first')
        layout1 = BoxLayout()
        btn1 = Button(text="Hello World")
        # Klicken auf den Button bringt Sie zum zweiten Bildschirm
        btn1.bind(on_press=self.switch_to_second)
        layout1.add_widget(btn1)
        screen1.add_widget(layout1)

        # Zweiter Bildschirm
        screen2 = SecondScreen(name='second')
        layout2 = BoxLayout()
        btn2 = Button(text="Zurück")
        # Klicken auf den Button bringt Sie zum ersten Bildschirm
        btn2.bind(on_press=self.switch_to_first)
        layout2.add_widget(btn2)
        screen2.add_widget(layout2)

        # Fügen Sie beide Bildschirme zum ScreenManager hinzu
        self.sm.add_widget(screen1)
        self.sm.add_widget(screen2)

        return self.sm

    # Methoden zum Wechseln der Bildschirme
    def switch_to_second(self, instance):
        self.sm.current = 'second'

    def switch_to_first(self, instance):
        self.sm.current = 'first'

if __name__ == "__main__":
    MyApp().run()
