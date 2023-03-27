import json
import sys

with open(sys.argv[1]) as f:
    game_map = json.load(f)

# Setting the starting location
current_location = game_map[0]

# Player inventory
inventory = []

# Valid commands
command_list = ["go", "get", "look", "inventory", "quit", "help", "drop"]

while True:
    print("> " + current_location["name"])
    print()
    print(current_location["desc"])
    print()
    if "items" in current_location:
        print("Items:", ", ".join(current_location["items"]))
        print()

    print("Directions:", " ".join(current_location["direction"].keys()))
    print()

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
        if "items" in current_location and item_name in current_location["items"]:
            inventory.append(item_name)
            current_location["items"].remove(item_name)
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

    elif command == "help":
        print("You can run the following commands:")
        for i in command_list:
            print("\t" + i)

        command = input("What would you like to do? ").strip().lower()
        if command == "quit":
            print("Goodbye!")
            sys.exit()
