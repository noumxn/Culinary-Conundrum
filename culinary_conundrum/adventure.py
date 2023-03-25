import json
import sys

with open(sys.argv[1]) as f:
    game_map = json.load(f)

# Setting the starting location
current_location = game_map[0]

# Player inventory
inventory = []

while True:
    print("> " + current_location["name"])
    print()
    print(current_location["desc"])
    print()

    print("Exits:", " ".join(current_location["exits"].keys()))
    print()

    command = input("What would you like to do? ").strip().lower()

    if command == "quit":
        print("Goodbye!")
        sys.exit()

    elif command == "inventory":
        if len(inventory) == 0:
            print("You're not carrying anything.")
        else:
            print("Inventory:")
            for item in inventory:
                print(" ", item)

    elif command.startswith("go "):
        direction = command[3:]
        if direction in current_location["exits"]:
            next_location = game_map[current_location["exits"][direction]]
            print("You go", direction + ".")
            current_location = next_location
        else:
            print("There's no way to go", direction + ".")

    elif command == "look":
        pass

    elif command.startswith("get "):
        item_name = command[4:]
        if "items" in current_location and item_name in current_location["items"]:
            inventory.append(item_name)
            current_location["items"].remove(item_name)
            print("You pick up the", item_name + ".")
        else:
            print("There's no", item_name, "here.")

    else:
        print("Sorry, I don't understand that.")
