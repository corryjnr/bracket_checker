from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.label import Label
from kivy.uix.popup import Popup
from kivy.uix.filechooser import FileChooserListView
from kivy.core.window import Window
from kivy.uix.scrollview import ScrollView
from bracket_checker import balance
Window.size = (500, 700)

class MyApp(App):
    def build(self):
        self.title = "Check nesting"
        self.root = root = BoxLayout(orientation="vertical")
        self.text = text = TextInput(font_size=20, size_hint_y=None, height=Window.height * 0.9)
        self.scroll = ScrollView(size_hint=(1, None), size=(Window.width, Window.height))
        self.scroll.add_widget(self.text)
        root.add_widget(self.scroll)
        self.button_open = Button(text="Select file")
        self.button_open.bind(on_release=self.open_file)
        root.add_widget(self.button_open)
        self.button_check = Button(text="Check brackets")
        self.button_check.bind(on_release=self.check_brackets)
        root.add_widget(self.button_check)
        return root

    def open_file(self, obj):
        content = BoxLayout(orientation="vertical")
        self.filechooser = filechooser = FileChooserListView(path="*.java")
        content.add_widget(filechooser)
        self.button_ok = Button(text="OK")
        self.button_ok.bind(on_release=self.select_file)
        content.add_widget(self.button_ok)
        self.popup = Popup(title="Select file", content=content, size_hint=(0.9, 0.9))
        self.popup.open()

    def select_file(self, obj):
        if self.filechooser.selection:
            with open(self.filechooser.selection[0], 'r') as f:
                self.text.text = f.read()
        self.popup.dismiss()

    def check_brackets(self, obj):
        program = self.text.text
        status = balance(program)
        content = BoxLayout(orientation="vertical")
        content.add_widget(Label(text=status))
        self.popup = Popup(title="Check brackets", content=content, size_hint=(0.5, 0.5))
        self.popup.open()

if __name__ == "__main__":
    MyApp().run()
 