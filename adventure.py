import json
import sys
import time

with open(sys.argv[1]) as f:
    game_map = json.load(f)

# Setting the starting location
current_location = game_map[0]

# Player inventory
inventory = []

# Player money
money = 25

# Valid commands
command_list = ["go", "get", "drop", "look",
                "inventory", "bake", "quit"]


Flag = False
start = True

while True:
    try:
        acquired_ingredients = True

        if "welcome_text" in game_map[-1] and Flag == False and start == True:
            print(game_map[-1]["welcome_text"])
            start = False

        # Prints name and description of the location player is at
        if Flag == False:
            print("> " + current_location["name"] + "\n")

        if "desc" in current_location and Flag == False:
            print(current_location["desc"] + "\n")

        if "goal" in current_location and Flag == False:
            if "flag" in current_location and current_location["flag"] == "true":
                print(current_location["goal"])
                current_location["flag"] = "false"

        if current_location == game_map[0] and Flag == False:
            if "recipe" in current_location and Flag == False:
                print(current_location["recipe"])

        # Items available at the location
        if "items" in current_location and current_location["items"] != [] and Flag == False:
            print("Items:", ", ".join(current_location["items"]) + "\n")

        if Flag == False:
            print("Exits:", " ".join(current_location["exits"].keys()))
            print()

        # Displays the amount of money player has for buying ingredients,
        # only if they have the purse in their inventory
        if "purse" in inventory and Flag == False:
            print("Money: $" + str(money) + "\n")

        Flag = False
        command = input("What would you like to do? ").strip().lower()

        # command validation
        if command == '' or command.split()[0] not in command_list:
            print("Sorry, I don't understand that.")
            Flag = True
            continue

        # quit command
        if command == "quit":
            print("Goodbye!")
            sys.exit()

        # inventory command
        elif command == "inventory":
            if len(inventory) == 0:
                print("You're not carrying anything.")
                Flag = True
                continue
            else:
                print("Inventory:")
                for item in list(set(inventory)):
                    print(" ", item)
                Flag = True
                continue

        # go ... command
        elif command.startswith("go"):
            direction = command[3:].strip()
            if command == 'go' or (len(command) == 3 and command[:-1] == 'go'):
                print("Sorry, you need to 'go' somewhere.")
                Flag = True
                continue

            if direction in current_location["exits"] and Flag == False:
                next_location = game_map[current_location["exits"][direction]]
                print("You go", direction + ".\n")
                current_location = next_location
            elif Flag == False:
                print("There's no way to go " + direction + ".")
                Flag = True
                continue

        # look command
        elif command == "look":
            pass

        # get ... command
        elif command.startswith("get"):
            item_name = command[4:].strip()
            if command[3:].strip() == '':
                print("Sorry, you need to 'get' something.")
                Flag = True
                continue

            if item_name in game_map[-3] and "purse" not in inventory and Flag == False:
                print("Uh oh! You can't pick this item without paying for it.")
                Flag = True
                continue

            if "items" in current_location and item_name in current_location["items"] and Flag == False:
                inventory.append(item_name)
                current_location["items"].remove(item_name)
                if item_name in game_map[-3] and Flag == False:
                    money = money - game_map[-3][item_name]
                    game_map[-3][item_name] = 0
                print("You pick up the", item_name + ".")
                Flag = True
                continue

            elif Flag == False:
                print("There's no", item_name, "anywhere.")
                Flag = True
                continue

        # drop command
        elif command.startswith("drop"):
            item_name = command[5:].strip()
            if command[5:].strip() == '':
                print("Sorry, you need to 'drop' something.")
                Flag = True
                continue

            if item_name in inventory and Flag == False:
                current_location["items"].append(item_name)
                inventory.remove(item_name)
                print("You dropped the", item_name + ".")
                Flag = True
                continue

            elif Flag == False:
                print("There's no", item_name, "in your inventory.")
                Flag = True
                continue

        # bake command
        elif command == "bake":
            acquired_ingredients = True
            if current_location == game_map[0]:
                for i in game_map[-2]:
                    if i not in inventory and i not in current_location["items"]:
                        print(i + " is missing from the recipe.")
                        acquired_ingredients = False
                print()
            else:
                print("You need to be in the Kitchen to bake.")
                Flag = True
                continue

            if current_location == game_map[0] and acquired_ingredients == True:
                print(game_map[-4]["items_compelete"])
                time.sleep(0.6)
                print(".")
                time.sleep(0.6)
                print(".")
                time.sleep(0.6)
                print(".")
                print(game_map[-4]["oven_prompt"])
                time.sleep(0.6)
                print(".")
                time.sleep(0.6)
                print(".")
                time.sleep(0.6)
                print(".")
                print(game_map[-4]["final_prompt"])
                time.sleep(0.6)
                print(".")
                time.sleep(0.6)
                print(".")
                time.sleep(0.6)
                print(".")
                print(game_map[-4]["win_message"])
                sys.exit()
            else:
                print("You need to be in the Kitchen to bake.")
                Flag = True
                continue

    except KeyboardInterrupt:
        print("\n  ...")
        print("KeyboardInterrupt")
        sys.exit()

    except EOFError:
        print("\nUse 'quit' to exit.")
        Flag = True
