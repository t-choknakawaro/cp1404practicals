"""
Distance Converter App
"""

from kivy.app import App
from kivy.lang import Builder
from kivy.properties import StringProperty
from kivy.core.window import Window

MILES_TO_KM = 1.60934


class DistanceConverterApp(App):
    """A class for converting miles to kms."""
    km_output = StringProperty()

    def build(self):
        """Build the UI."""
        self.title = 'Miles to Km'
        Window.size = (400, 300)
        self.root = Builder.load_file('convert_miles_km.kv')
        return self.root

    def check_value(self):
        """Check the validity of input value from the UI."""
        if self.root.ids.miles_input.text == '':
            return 0.0
        else:
            try:
                value = float(self.root.ids.miles_input.text)
                return value
            except ValueError:
                return 0.0

    def handle_increment(self, integer):
        """Handle the increment of the miles input."""
        user_input = self.check_value()
        self.root.ids.miles_input.text = str(user_input + integer)
        self.handle_calculate()

    def handle_calculate(self):
        """Calculate the kilometers from the input that is miles."""
        miles_value = self.check_value()
        km_value = miles_value * MILES_TO_KM
        self.root.ids.km_output.text = str(km_value)


DistanceConverterApp().run()