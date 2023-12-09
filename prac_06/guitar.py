CURRENT_YEAR = 2023
VINTAGE_YEAR = 50


class Guitar:
    """Representing Guitar Class"""
    def __init__(self, name='', year=0, cost=0):
        """Give parameters for each car details."""
        self.name = name
        self.year = year
        self.cost = cost

    def __str__(self):
        """Return string about guitar details."""
        return f'{self.name} ({self.year}) : ${self.cost}'

    def get_age(self):
        """Return guitar age."""
        return CURRENT_YEAR - self.year

    def is_vintage(self):
        """Check if guitar is vintage."""
        return self.get_age() >= VINTAGE_YEAR

    def __lt__(self, other):
        """Less than, used for sorting Guitars - by year released."""
        return self.year < other.year or (self.year == other.year and self.name < other.name)
