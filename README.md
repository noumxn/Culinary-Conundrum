# Culinary-Conundrum

## Project for CS-515

**Nouman Syed** [nsyed1@stevens.edu](mailto:nsyed1@stevens.edu)  

GitHub URL : [Link](https://github.com/noumxn/Culinary-Conundrum)

Estimated Time Spent: 
> 12-15 hours

A description of how you tested your code:
> Unit Tests: Tested each commands functionality on its own extensively.

> Integration Tests: Tested the full functionality of the game engine several times with all possible variations.

> Acceptance Tests: Shared the application with a couple of my friends so they can test it out as end users.

Any bugs or issues you could not resolve:
> To my knowledge, there are no known bugs or issues in this application.

An example of a difficult issue or bug and how you resolved:
> I initially found it very difficult to get started on my own idea straight away. So I first implemented the example given in the Project specs. After I had a working application for the base map, I chipped away parts of the application that I did not need and added all the new components I would require for implementing my own idea.

A list of the three extensions you’ve chosen to implement, with appropriate detail on them for the CAs to evaluate:
> Assist: This command allows you to assist someone who needs your help. There is an ingredient on the recipe that you won't ba able to find on the map. You can acquire this ingredient only by helping out someone in need. (Spoiler: The user sees their neighbor John struggling with their pet hen which has escaped. You use the "assist" key to help out John, who in return gives you fresh eggs as a token of thanks.)

> Money: There are several ingredients that the player needs to find for completing their recipe. However, they won't be able to pick any of the ingredients at the Marketplace or the Dairy Store if they don't have any money on them. Also, each time they buy an item, the game shows how much money was spent on the item the player just picked up. 
>(Spoiler: The user needs to first go into the bedroom and collect the "purse" item. This enables them to use money)

> Prepare: This is the command the user runs when they have acquired all the ingredients in the recipe. They are only allowed to run this command when they are in the Kitchen, where they would actually prepare their ingredients. Also, the user can't run this command without actually acquiring all ingredients. They would get an error message displaying all the ingerdients that are missing.