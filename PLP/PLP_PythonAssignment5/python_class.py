# Create a class representing anything you like (a Smartphone, Book, or even a Superhero!).
# Add attributes and methods to bring the class to life!
# Use constructors to initialize each object with unique values.
# Add an inheritance layer to explore polymorphism or encapsulation.

class Movie:
    #class attribute
    genre = "Unknown"

    def __init__(self, title, cast, releaseDate):
        self.title = title  # these are instance attributes
        self.cast = cast
        self.__releaseDate = releaseDate

#methods of the class, Movie
    def Cinema(self):
        print("These are cinema movies")

    def Youtube(self):
        print("These are youtube movies")

    def Effect(self):
        print("How do you feel after seeing the movie")

    #Exploring encapsulation
    #returns the private property
    @property
    def releaseDate(self):
        return self.__releaseDate
    
    #sets the private property
    @releaseDate.setter
    def releaseDate(self, value):
        self.__releaseDate = value

 #Exploring polymorphism in subclasses
class Comedy(Movie):
    def Effect(self):
        print("I laughed as I am seeing the movie")
class Horror(Movie):
    def Effect(self):
        print("I am scared after seeing the movie")
class Romance(Movie):
    def Effect(self):
        print("I feel loved after seeing the movie")

#create the object 
movie = Movie("Straw", "Kate Henshaw", 2025)
movie.releaseDate = 2026 #this calls setter automatically
print(movie.releaseDate)  #this calls getter automatically 2026 

comedy1 = Comedy("What Happened to Monday", "Jim Iyke", 2020)
horror1 = Horror("The Nun", "Vera Farmiga", 2018)
romance1 = Romance("Titanic", "Leonardo DiCaprio & Kate Winslet", 1997)
for x in (comedy1, horror1, romance1):
    x.Effect()

#  Create a program that includes animals or vehicles 
# with the same action (like move()). 
# However, make each class define move() differently
#  (for example, Car.move() prints "Driving" 🚗, 
# while Plane.move() prints "Flying" ✈️).   

class Car:
    def move(self):
        print("🚗 Driving on the road")

class Plane:
    def move(self):
        print("✈️ Flying in the sky")

class Boat:
    def move(self):
        print("⛵ Sailing on water")

# Polymorphism in action
vehicles = [Car(), Plane(), Boat()]

for v in vehicles:
    v.move()



