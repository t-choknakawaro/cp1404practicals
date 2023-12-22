from kivy.app import App
from kivy.lang import Builder
from kivy.uix.label import Label


class DynamicLabelsApp(App):
    """A class for creating dynamic labels."""
    def __init__(self, **kwargs):
        """Initialize the class."""
        super().__init__(**kwargs)
        self.list_of_names = ['Troy', 'Jake', 'Jay', 'Niki']

    def build(self):
        """Build the UI."""
        self.title = 'Dynamic Labels'
        self.root = Builder.load_file('dynamic_labels.kv')
        self.create_labels()
        return self.root

    def create_labels(self):
        """Create labels based on the list of the names."""
        for name in self.list_of_names:
            label_name = Label(text=name)
            self.root.ids.main.add_widget(label_name)


DynamicLabelsApp().run()
