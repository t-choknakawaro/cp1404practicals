from kivy.app import App
from kivy.lang import Builder
from kivy.uix.label import Label


class DynamicLabelsApp(App):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.list_of_names = ['Troy', 'Sky', 'Baicha', 'Minhye']

    def build(self):
        self.title = 'Dynamic Labels'
        self.root = Builder.load_file('dynamic_labels.kv')
        self.create_labels()
        return self.root

    def create_labels(self):
        for name in self.list_of_names:
            label_name = Label(text=name)
            self.root.ids.main.add_widget(label_name)


DynamicLabelsApp().run()
