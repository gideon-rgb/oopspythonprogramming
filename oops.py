# Guestion 1: Create a class
class Superhero:
    def __init__(self, name, superpower, city):
        # Question 3: Use constructors to initialize each object with unique values
        self.name = name
        self.superpower = superpower
        self.city = city

    # Question 2: Add methods to bring the class to life
    def fight_crime(self):
        return f"{self.name} is fighting crime in {self.city}!"

    def save_people(self):
        return f"{self.name} is saving people with their {self.superpower}!"

    def display_info(self):
        return f"Superhero: {self.name}, Superpower: {self.superpower}, City: {self.city}"


# Question 4: Add an inheritance layer
class FlyingSuperhero(Superhero):
    def __init__(self, name, superpower, city, wing_span):
        super().__init__(name, superpower, city)  # Call the constructor of the parent class
        self.wing_span = wing_span  # Additional attribute for FlyingSuperhero

    def fly(self):
        return f"{self.name} is flying with a wingspan of {self.wing_span} meters!"

    def display_info(self):
        # Override the display_info method to include wing_span
        base_info = super().display_info()
        return f"{base_info}, Wing Span: {self.wing_span} meters"


# usage
hero1 = Superhero("Captain Valor", "Super Strength", "Metropolis")
print(hero1.display_info())
print(hero1.fight_crime())
print(hero1.save_people())

flying_hero = FlyingSuperhero("Sky Guardian", "Flight", "Sky City", 15)
print(flying_hero.display_info())
print(flying_hero.fly())