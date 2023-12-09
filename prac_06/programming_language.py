
class ProgrammingLanguage:
    def __init__(self, name, typing, reflection, year):
        """Collecting ProgrammingLanguage details."""
        self.name = name
        self.typing = typing
        self.reflection = reflection
        self.year = year

    def __str__(self):
        """Return string representation of ProgrammingLanguage."""
        return f'{self.name}, {self.typing} Typing, Reflection={self.reflection}, First appeared in {self.year}'

    def is_dynamic(self):
        """To check if it is dynamic typing."""
        return self.typing == 'Dynamic'
