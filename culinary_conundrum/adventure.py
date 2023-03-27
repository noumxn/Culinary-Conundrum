import json
import sys

with open(sys.argv[1]) as f:
    game_map = json.load(f)

print("  ______      _ _                             ______                            _                   ")
print(" / _____)    | (_)                           / _____)                          | |                  ")
print("| /     _   _| |_ ____   ____  ____ _   _   | /      ___  ____  _   _ ____   _ | | ____ _   _ ____  ")
print("| |    | | | | | |  _ \ / _  |/ ___) | | |  | |     / _ \|  _ \| | | |  _ \ / || |/ ___) | | |    \ ")
print("| \____| |_| | | | | | ( ( | | |   | |_| |  | \____| |_| | | | | |_| | | | ( (_| | |   | |_| | | | |")
print(" \______)____|_|_|_| |_|\_||_|_|    \__  |   \______)___/|_| |_|\____|_| |_|\____|_|    \____|_|_|_|")
print("                                   (____/                                                           ")
print("\n\033[1mWelcome to the game!\033[0m\n")


# Setting the starting location
current_location = game_map[0]

# Player inventory
inventory = []

# Player money
money = 20

# Valid commands
command_list = ["go", "get", "look", "inventory",
                "quit", "help", "drop", "assist", "prepare"]

prices = {
    "milk": 4,
    "salt": 1,
    "sugar": 2,
    "vanilla essence": 4,
    "baking powder": 2,
    "flour": 2,
    "butter": 3
}

while True:
    print("> \033[1m" + current_location["name"] + "\033[0m\n")
    if current_location["name"] == "John's Front Yard" and current_location["flag"] == "false":
        print("\033[3m" + current_location["desc2"] + "\033[0m\n")
    else:
        print("\033[3m" + current_location["desc"] + "\033[0m\n")
    if "items" in current_location:
        print("Items:", ", ".join(current_location["items"]) + "\n")

    print("Directions:", " ".join(current_location["direction"].keys()))
    print()

    if "purse" in inventory:
        print("Money: $" + str(money) + "\n")

    command = input("What would you like to do? ").strip().lower()

    if command.split()[0] not in command_list:
        print("Sorry, I don't understand that.")
        print("Type 'Help' to see valid command list.\n")

    if command == "quit":
        print("Goodbye!")
        sys.exit()

    elif command == "inventory":
        if len(inventory) == 0:
            print("You're not carrying anything.\n")
        else:
            print("Inventory:")
            for item in inventory:
                print(" ", item)
            print()

    elif command.startswith("go "):
        direction = command[3:]
        if direction in current_location["direction"]:
            next_location = game_map[current_location["direction"][direction]]
            print("You go", direction + ".\n")
            current_location = next_location
        else:
            print("There's no way to go", direction + ".\n")

    elif command == "look":
        pass

    elif command.startswith("get "):
        item_name = command[4:]
        if item_name in prices and "purse" not in inventory:
            print("Uh oh! You can't pick this item without paying for it.\n")
            continue

        if "items" in current_location and item_name in current_location["items"]:
            inventory.append(item_name)
            current_location["items"].remove(item_name)
            if item_name in prices:
                money = money - prices[item_name]
            print("You pick up the", item_name + ".\n")
        else:
            print("There's no", item_name, "here.\n")

    elif command.startswith("drop "):
        item_name = command[5:]
        if item_name in inventory:
            current_location["items"].append(item_name)
            inventory.remove(item_name)
            print("You dropped the", item_name + ".\n")
        else:
            print("There's no", item_name, "in your inventory.\n")

    elif command == "assist":
        print("Awesome job! You've helped John get his hen back in the coop.")
        print("John gives you some eggs as a token on his appriciation.\n")
        inventory.append("eggs")
        current_location["flag"] = "false"

    elif command == "help":
        print("You can run the following commands:")
        for i in command_list:
            print("\t" + i)

        command = input("What would you like to do? ").strip().lower()
        if command == "quit":
            print("Goodbye!")
            sys.exit()
        if command == "assist":
            print("Awesome job! You've helped John get his hen back in the coop.")
            print("John gives you some eggs as a token on his appriciation.\n")
            inventory.append("eggs")
            current_location["flag"] = "false"

    elif command == "prepare":
        if current_location == game_map[0]:
            if ["eggs", "milk", "butter", "flour", "baking powder", "salt", "sugar", "vanilla essence"] not in current_location["items"]:
                print("Left")
            else:
                print("Done")
        else:
            print("You need to be in the Kitchen to prepare your ingredients.\n")
