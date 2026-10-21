from game import Investigation
from utilities import valid_name, get_choice
from logger import log_event


def show_previous_record():
    try:
        with open("player.txt", "r") as file:
            lines = file.readlines()

        if len(lines) >= 3:
            print("\n--- Previous Saved Record ---")
            print("Player:", lines[0].strip())
            print("Score:", lines[1].strip())
            print("Mystery solved:", lines[2].strip())

    except FileNotFoundError:
        print("No previous saved record found.")


def main():
    print("=" * 42)
    print(" MINDVAULT")
    print(" Mystery & Logic Investigation System")
    print("=" * 42)

    show_previous_record()

    while True:
        player = input(
            "\nEnter your detective name: "
        ).strip()

        if valid_name(player):
            break

        print("Use 2-30 letters and spaces only.")

    game = Investigation(player)

    log_event(player + " started an investigation")

    while True:
        print("\n==== MAIN MENU ====")
        print("1. Explore Locations")
        print("2. Question People")
        print("3. View Evidence")
        print("4. Solve Puzzle")
        print("5. Identify Person Responsible")
        print("6. View Score")
        print("7. Save and Exit")

        choice = get_choice(
            "Enter your choice: ", 1, 7
        )

        if choice == 1:
            game.explore_locations()

        elif choice == 2:
            game.question_suspects()

        elif choice == 3:
            game.view_evidence()

        elif choice == 4:
            game.solve_puzzle()

        elif choice == 5:
            game.identify_person_responsible()

        elif choice == 6:
            game.view_score()

        elif choice == 7:
            game.save_progress()
            print("\nThank you for playing MindVault!")
            break


if __name__ == "__main__":
    main()