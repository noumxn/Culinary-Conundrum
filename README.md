# Culinary-Conundrum

## Project for CS-515

**Nouman Syed** [nsyed1@stevens.edu](mailto:nsyed1@stevens.edu)

GitHub URL : [Culinary Conundrum](https://github.com/noumxn/Culinary-Conundrum)

Estimated Time Spent: 
> ~15 hours

A description of how you tested your code:
> Unit Tests: Tested each commands functionality on it's own extensively on different variations of maps.

> Integration Tests: Tested the full functionality of the game engine, first, only for the base requirement commands, and later along with each added extension.

> Acceptance Tests: Asked some friends to use the application to get better end user perspective.

Any bugs or issues you could not resolve:
> To my knowledge, there are no known bugs or issues in this application.

An example of a difficult issue or bug and how you resolved:
> I initially found it very difficult to get started on my own idea straight away. So I first implemented a program that would work for the example map given in the Project specs. After I had a working application for the base map, I improved the program to be able to run all the base requirement commands on any given map. Finally, when I had this ready, I carefully added each extension one by one.

A list of the three extensions you’ve chosen to implement, with appropriate detail on them for the CAs to evaluate:
> The `drop` verb: This extension is implemented exactly as demonstrated in the project specs. A user can `drop <item_name>`  to remove items from their inventory and add them to the room they are currently in. Dropped items get added to the `items` list of that specific room. If the player tries to drop something they don't have in their inventory, a `There's no <item_name> in your inventory.` error message is displayed. If the player just runs the command `drop` without specifying what needs to be dropped, a `Sorry, you need to 'drop' something.` message is displayed.

> Money: This is my take on the `locked doors` and `interactions` idea given in the specs for the project. Since the goal of this game is for the player to go around and buy items to bake whatever item the map corrosponds to, the player is required to have money for `get`ting any items they need. Before the player goes out and about, they need to `get` the `purse` item from the bedroom. If they don't do this, and attept to `get` ie purchase an item, they see a `Uh oh! You can't pick this item without paying for it.` message. Also once they do get the purse, `Money: $25` is displayed just below the the exits for each room. This amount reduces after each purchase the player makes based on fixed costs for items in the recipe specified in the map.

> The `bake` verb: This is my take on the `win condition` extension idea given. This is a command that the player runs once they have completed collecting all the items they need for their recipe. However, they can only run this command once they are back in their kitchen, where they started off. If they run this command in any other location, a `You need to be in the Kitchen to bake.` message is displayed. Also, if they are in the kitchen, but have not yet acquired all the necessary ingredients yet, a `<item_name> is missing from the recipe.` message is displayed for each item that is missing. If the user has acquired all ingredients for the specific map, and is also present in the kitchen, the player has completed the map and the following text is displayed:
```
Perfect! Looks like you have all the recipe items.
Mixing recipe items.
.
.
.
Everything is ready. This just needs to go in the oven!
.
.
.
Not gonna lie, this smells amazing!
.
.
.
Ding!Ding!Ding!
Looks like the cake is ready!
You've completed this map.
Treat yourself to some cake.

Thanks for playing!
Goodbye!
```