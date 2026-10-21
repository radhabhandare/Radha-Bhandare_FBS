class Suspect:
    def __init__(self, name, occupation, statement):
        self.name = name
        self.occupation = occupation
        self.statement = statement
        self.questioned = False

    def display(self):
        print("\nName:", self.name)
        print("Occupation:", self.occupation)
        print("Statement:", self.statement)


class Evidence:
    def __init__(self, name, description):
        self.name = name
        self.description = description

    def display(self):
        print("\nClue:", self.name)
        print("Description:", self.description)