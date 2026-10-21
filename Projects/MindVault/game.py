from models import Suspect, Evidence
from utilities import get_choice, show_section
from logger import log_event
from database import save_result


class Investigation:

    def __init__(self, player):
        self.player = player
        self.score = 0
        self.clues = []
        self.questioned = []
        self.solved = False
        self.puzzle_solved = False

        # Create people
        self.suspects = [
            Suspect(
                "Swaroop",
                "Chef",
                "I was in the kitchen until 8 PM."
            ),

            Suspect(
                "Sindhu",
                "Security Guard",
                "I left the building at 8 PM."
            ),

            Suspect(
                "Manjul",
                "Researcher",
                "I was working in the library."
            )
        ]

        # Create clues
        self.evidence = [
            Evidence(
                "Security Log",
                "Sindhu was recorded entering the library "
                "at 8:15 PM."
            ),

            Evidence(
                "Wet Footprints",
                "Wet footprints lead from the greenhouse "
                "to the library."
            ),

            Evidence(
                "Torn Note",
                "The note says: Meet me in the library "
                "after eight."
            )
        ]

        # Locations and their clue indexes
        self.locations = {
            "Kitchen": [2],
            "Greenhouse": [1],
            "Library": [0, 2]
        }

    # Generator
    def evidence_generator(self):
        for clue in self.evidence:
            yield clue

    # Explore locations
    @show_section
    def explore_locations(self):

        locations = list(self.locations.keys())

        for number, location in enumerate(
            locations, start=1
        ):
            print(number, location)

        choice = get_choice(
            "Choose a location: ",
            1,
            len(locations)
        )

        location = locations[choice - 1]

        print("\nExploring:", location)

        found = False

        for index in self.locations[location]:
            clue = self.evidence[index]

            if clue.name not in [
                item.name for item in self.clues
            ]:
                self.clues.append(clue)
                self.score += 10

                clue.display()

                print("New clue collected! +10 points")

                log_event(
                    self.player + " collected " + clue.name
                )

                found = True

        if not found:
            print("No new clues found here.")

    # Question people
    @show_section
    def question_suspects(self):

        for number, suspect in enumerate(
            self.suspects, start=1
        ):
            print(number, suspect.name)

        choice = get_choice(
            "Choose a person to question: ",
            1,
            len(self.suspects)
        )

        suspect = self.suspects[choice - 1]

        suspect.display()

        if not suspect.questioned:
            suspect.questioned = True
            self.questioned.append(suspect.name)
            self.score += 5

            print("You earned 5 points.")

            log_event(
                self.player + " questioned " + suspect.name
            )

        else:
            print("You have already questioned this person.")

    # View collected clues
    @show_section
    def view_evidence(self):

        if not self.clues:
            print("Collect some clues before viewing them.")
            return

        for clue in self.evidence_generator():

            if clue.name in [
                item.name for item in self.clues
            ]:
                clue.display()

    # Solve puzzle
    @show_section
    def solve_puzzle(self):

        if self.puzzle_solved:
            print("You have already solved this puzzle.")
            return

        print("Sindhu says she left at 8:00 PM.")
        print("The security log records her entering")
        print("the library at 8:15 PM.")
        print("How many minutes later was she recorded?")

        answer = get_choice(
            "Your answer in minutes: ",
            0,
            120
        )

        if answer == 15:
            print("Correct! You solved the puzzle.")

            self.score += 20
            self.puzzle_solved = True

            log_event(
                self.player + " solved the puzzle"
            )

        else:
            print("Incorrect. Check the times again.")

    # Identify the responsible person
    @show_section
    def identify_person_responsible(self):

        if self.solved:
            print("The mystery is already solved.")
            return

        if len(self.clues) < len(self.evidence):
            print("Collect all three clues first.")
            return

        print("Who do you think is responsible?")

        for number, suspect in enumerate(
            self.suspects, start=1
        ):
            print(number, suspect.name)

        choice = get_choice(
            "Enter the person's number: ",
            1,
            len(self.suspects)
        )

        suspect = self.suspects[choice - 1]

        if suspect.name == "Sindhu":
            print("\nCorrect! Sindhu's statement conflicts")
            print("with the security log.")
            print("You solved the mystery!")

            self.score += 50
            self.solved = True

            log_event(
                self.player
                + " identified the person responsible"
            )

        else:
            print("That answer is incorrect.")
            print("Review the clues and try again.")

            self.score = max(0, self.score - 10)

    # View score
    def view_score(self):

        print("\nPlayer:", self.player)
        print("Score:", self.score)
        print("Clues collected:", len(self.clues), "/ 3")
        print("People questioned:", len(self.questioned), "/ 3")
        print("Puzzle solved:", self.puzzle_solved)
        print("Mystery solved:", self.solved)

    # Save progress
    def save_progress(self):

        with open("player.txt", "w") as file:
            file.write(self.player + "\n")
            file.write(str(self.score) + "\n")
            file.write(str(self.solved) + "\n")

        save_result(
            self.player,
            self.score,
            self.solved
        )

        log_event(self.player + " saved progress")

        print("Progress saved in player.txt.")
