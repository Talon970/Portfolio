from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.button import Button

class MyLayout(App):
    def build(self):
        # BoxLayout
        box = BoxLayout(orientation='vertical')
        box.add_widget(Button(text='Button 1'))
        box.add_widget(Button(text='Button 2'))

        # GridLayout
        grid = GridLayout(cols=2)
        grid.add_widget(Button(text='Button 3'))
        grid.add_widget(Button(text='Button 4'))

        # AnchorLayout
        anchor = AnchorLayout(anchor_x='center', anchor_y='center')
        anchor.add_widget(Button(text='Centered Button'))

        # Kombinieren der Layouts
        main_layout = BoxLayout(orientation='vertical')
        main_layout.add_widget(box)
        main_layout.add_widget(grid)
        main_layout.add_widget(anchor)

        return main_layout

if __name__ == "__main__":
    MyLayout().run()
