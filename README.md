# TextAdventureGame

An experimental framework for text adventure games using Python (ultimately: Unity 5)


##"Parts of speech" or Categories

* Room: location in game
* Direction: (Room, Direction) points to another Room
* Command: an action verb, like go, quit, etc.
* Item: something that can be picked up, moved, etc.
* Actor: something autonomous, e.g. an enemy.
* Structure: something like a wall, etc. that can be changed (blown up, etc.)

##properties of game entities
* Each entity in the game is uniquely specified by its name and its category
* A name, which is a string, is by convention, is a single CamelCase word.
    + for example, a Room might be named StreetNextToPawnShop
* However, when a name must be typed, such as a direction, command, or item, 
it is case insensitive and if unambiguous, can be abbreviated
* Any name can be assigned a Synonym.  E.g.  the Name-Category pari (W, Direction) 
could be a Synonym for (West, Direction)

##List of Command entities (can be extended at will) 
* Go _Direction_
    + Synonym: G _Direction_
    + Can also just type _Direction_ with no verb
* Get _Item_
    + Synonym: Take _Item_
    + Synonym: T _Item_
* Drop _Item_
    + Synonym: Dr _Item_
* Quit
    + Synonym: Q
* Save _Name_
    + Saves the game under the specified name
* Load _Name_
    + Loads the previously-saved game having the specified name    
* Examine _optional argument: Item or Actor or Structure or Room_
    + Synonym: Ex
    + Synonym: Look
    + Synonym: L
    + If no argument given, assume current room 
    + If room argument given, must be a room already encountered or current room
    + If Item or Actor or Structure given, the entity must exist in the current room

## List of Direction entities (can be extended at will)
* North
    + Synonym: N
* South
    + Synonym: S
* East
    + Synonym: E
* West
    + Synonym: W
* NorthWest
    + Synonym: NW
* NorthEast
    + Synonym: ME
* SouthWest
    + Synonym: SW
* SouthEast
    + Synonym: SE
* Up
    + Synonym: U
* Down
    + Synonym: D

##Resources
* Game entities in a given category are stored in a CSV file of the name Resources/_Category_.csv 

    
