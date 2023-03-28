import json
import sys
import time

with open(sys.argv[1]) as f:
    game_map = json.load(f)

print("  ______      _ _                             ______                            _                   ")
print(" / _____)    | (_)                           / _____)                          | |                  ")
print("| /     _   _| |_ ____   ____  ____ _   _   | /      ___  ____  _   _ ____   _ | | ____ _   _ ____  ")
print("| |    | | | | | |  _ \ / _  |/ ___) | | |  | |     / _ \|  _ \| | | |  _ \ / || |/ ___) | | |    \ ")
print("| \____| |_| | | | | | ( ( | | |   | |_| |  | \____| |_| | | | | |_| | | | ( (_| | |   | |_| | | | |")
print(" \______)____|_|_|_| |_|\_||_|_|    \__  |   \______)___/|_| |_|\____|_| |_|\____|_|    \____|_|_|_|")
print("                                   (____/                                                           ")
print("\n\033[1mWELCOME TO THE GAME!\033[0m\n")


# Setting the starting location
current_location = game_map[0]

# Player inventory
inventory = []

# Player money
money = 20

# Valid commands
command_list = ["go", "get", "drop", "look",
                "inventory", "assist", "prepare",
                "bake", "quit", "help"]

acquired_ingredients = True
prep = False

while True:
    try:
        acquired_ingredients = True

        # Prints name and descreption of the location player is at
        print("> \033[1m" + current_location["name"] + "\033[0m\n")

        if current_location == game_map[3] and current_location["flag"] == "false":
            print("\033[3m" + current_location["desc2"] + "\033[0m\n")
        else:
            print("\033[3m" + current_location["desc"] + "\033[0m\n")

        if current_location == game_map[0] and current_location["flag"] == "true":
            print('\033[3m{}\033[0m'.format(current_location["goal"]))
            current_location["flag"] = "false"

        if current_location == game_map[0]:
            print('\033[3m{}\033[0m'.format(current_location["recipe"]))

        # Items available at the location
        if "items" in current_location:
            print("Items:", ", ".join(current_location["items"]) + "\n")

        print("Directions:", " ".join(current_location["direction"].keys()))
        print()

        # Displays the amount of money player has for buying ingredients,
        # only if they have the purse in their inventory
        if "purse" in inventory:
            print("Money: $" + str(money) + "\n")

        command = input("What would you like to do? ").strip().lower()

        # command validation
        if command == '' or command.split()[0] not in command_list:
            print("Sorry, I don't understand that.")
            print("Type 'Help' to see valid command list.\n")

        # quit command
        if command == "quit":
            print("Goodbye!")
            sys.exit()

        # inventory command
        elif command == "inventory":
            if len(inventory) == 0:
                print("You're not carrying anything.\n")
            else:
                print("Inventory:")
                for item in list(set(inventory)):
                    print(" ", item)
                print()

        # go ... command
        elif command.startswith("go "):
            direction = command[3:].strip()
            if direction in current_location["direction"]:
                next_location = game_map[current_location["direction"][direction]]
                print("You go", direction + ".\n")
                current_location = next_location
            else:
                print("There's no way to go", direction + ".\n")

        # look command
        elif command == "look":
            pass

        # get ... command
        elif command.startswith("get "):
            item_name = command[4:].strip()
            if item_name in game_map[12] and "purse" not in inventory:
                print("Uh oh! You can't pick this item without paying for it.\n")
                continue

            if "items" in current_location and item_name in current_location["items"]:
                inventory.append(item_name)
                current_location["items"].remove(item_name)
                if item_name in game_map[12]:
                    money = money - game_map[12][item_name]
                    game_map[12][item_name] = 0
                print("You pick up the", item_name + ".\n")
            else:
                print("There's no", item_name, "here.\n")

        # drop command
        elif command.startswith("drop "):
            item_name = command[5:]
            if item_name in inventory:
                current_location["items"].append(item_name)
                inventory.remove(item_name)
                print("You dropped the", item_name + ".\n")
            else:
                print("There's no", item_name, "in your inventory.\n")

        # assist command
        elif command == "assist":
            if current_location != game_map[3]:
                print("Looks like nobody needs any assistance right now.\n")
                continue
            print(current_location["help_message"])
            inventory.append(current_location["gift"])
            current_location["flag"] = "false"

        # help command
        elif command == "help":
            print("You can run the following commands:")
            for i in command_list:
                print("\t" + i)
            # command = input("What would you like to do? ").strip().lower()
            # if command == "quit":
            #     print("Goodbye!")
            #     sys.exit()
            # if command == "assist":
            #     if current_location != game_map[3]:
            #         print("Nobody needs your help here.\n")
            #         continue
            #     print(current_location["help_message"])
            #     inventory.append(current_location["gift"])
            #     current_location["flag"] = "false"

        # prepare command
        elif command == "prepare":
            if current_location == game_map[0]:
                for i in game_map[13]:
                    # if i not in current_location["items"]:
                    if i not in inventory and i not in current_location["items"]:
                        print(i + " is missing from the recipe.")
                        acquired_ingredients = False
                print()

            if current_location == game_map[0] and acquired_ingredients == True:
                print("Perfect! Looks like you have all the recipe items.")
                print("Mixing recipe items.")
                time.sleep(0.6)
                print(".")
                time.sleep(0.6)
                print(".")
                time.sleep(0.6)
                print(".")
                print("Everything is ready. This just needs to go in the oven!\n")
                prep = True
            else:
                print("You need to be in the Kitchen to prepare your ingredients.\n")

        # bake command
        elif command == "bake":
            if prep != True:
                print("You still haven't prepared all your ingredients for baking.\n")
            else:
                print("Dish goes in to the oven.")
                time.sleep(0.6)
                print(".")
                time.sleep(0.6)
                print(".")
                time.sleep(0.6)
                print(".")
                print("Not gonna lie, this smells amazing!")
                time.sleep(0.6)
                print(".")
                time.sleep(0.6)
                print(".")
                time.sleep(0.6)
                print(".")
                print(
                    "Ding!Ding!Ding!\nLooks like the cake is ready!\nYou've completed this map.\nTreat yourself to some cake.\n")
                print("Thanks for playing!")
                print("Goodbye!")
                sys.exit()

    except KeyboardInterrupt:
        print("\n\t...")
        print("KeyboardInterrupt")

    except EOFError:
        print("\n\t...")
        print("Use 'quit' to exit.")
