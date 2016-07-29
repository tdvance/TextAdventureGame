# TextAdventureGame

An experimental framework for text adventure games using Python (ultimately: Unity 5)

* game_object -> noun, action, preposition
        + has: name, desc, brief_desc
        + str(game_object) is its name

* noun -> room, item, game, direction

* action -> action
    + has: direct object(noun), indirect objects(nouns with prepositions)
    
* preposition -> 
    
* room -> room
    + has: items, rooms via directions

* item -> item, actor
    + has: items via prepositions
    + can be: spawned, deleted
    
* actor -> actor, player, enemy
    + can do: action
    
* player -> player
    + has: health

* enemy -> enemy
    + has: health

* game -> game
    + manages: game loop, start, stop, etc.
    + has: player, dictionary, items, rooms

* direction -> direction
    

* dictionary -> dictionary
    
