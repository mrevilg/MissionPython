
planets = { "Mercury": "The smallest planet, nearest the Sun",
            "Venus": "Venus takes 243 days to rotate",
            "Earth": "The only planet known to have native life",
            "Mars": "The Red Planet is the second smallest planet",
            "Jupiter": "The largest planet, Jupiter is a gas giant",
            "Saturn": "The second largest planet is a gas giant",
            "Uranus": "An ice giant with a ring system",
            "Neptune": "An ice giant and farthest from the Sun",
            "Pluto": "The largest dwarf planet in the Solar System"
            }

while True:
   query = input("Which planet would you like information on? ")
   print(planets[query])