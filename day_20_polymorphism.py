class Ramu:
    def __init__(self, profession):
     self.profession = profession

    def character(self):
       print(f"He works as a {self.profession} and very honest")

class Remo:
    def __init__(self, profession):
     self.profession = profession

    def character(self):
       print(f"He is a {self.profession} and flirts girl")

class Aparichithudu:     
    def character(self):
       print(f"He identify the corruption")

def identify_person(obj):
   obj.character()

identify_person(Ramu('Lawyer'))