from project import geuss
from sum import jam


def main():

    while True:

        print("\n===== MAIN MENU =====")
        print("1. Guess Game")
        print("2. Calculator")
        print("3. Exit")

        choice = input("Choose: ")

        if choice == "1":

            while True:

                geuss()

                print("\n===== GAME MENU =====")
                print("1. Again")
                print("2. Exit")

                game_choice = input("Choose: ")

                if game_choice == "1":
                    continue

                elif game_choice == "2":
                    break

                else:
                    print("Invalid choice!")

        elif choice == "2":
            while True:
                jam()

                print("\n===== GAME MENU =====")
                print("1. Again")
                print("2. Exit")

                game_choice = input("Choose: ")

                if game_choice == "1":
                    continue

                elif game_choice == "2":
                    break

                else:
                    print("Invalid choice!")

        elif choice == "3":
            print("Goodbye!")
            break

        else:
            print("Invalid choice!")


main()