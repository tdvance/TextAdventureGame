#Text Adventure Game Framework


## World
A world is like a graph.  Instead of nodes, we have rooms.  Instead of 
edges, we have connections.  From each room are connections to other 
rooms, and each connection is indexed by a direction.
 
## Direction
A direction is a text string, and can be an alias to another direction. 
In addition,  Directions can have text representations like 'to the 
west is'.
 
## Room
 A room is a place in the world.  There are connections between rooms
 and other rooms in the world, indexed by directions.  A room has a 
 description appropriate for when in the room, and a short description
 appropriate for viewing a connection to the room.  The room also has
 a long description for when it is examined.
 
## Connection
A connection is a direction and a source and target room.  It says that 
the target room is connected to the source room and in the given 
direction from the source room.

## Item
An item can be in a room or on the player (if gettable).  An item has
a room description appropriate for when it is visible in a room, a 
player description appropriate for when the player has it, a take 
description shown when it is picked up, a drop description shown when
it is dropped, and a long description for when it is examined.  It
has attributes like visible, gettable, etc.

## Action
An action is something that changes the state of the game.  For example
if a player is in a room, the player can go in a direction to go to a
connecting room, or get an item or drop an item, etc.  Most actions
will correspond to methods.  For example, an action invoked by the
player will be a method of the player.  An action invoked by the player
will have a text string and can be an alias to another action.  It would
have a long description displayed upon running 'help'.

## Player
The first-person player of the game.  The player can be in a room and
can perform an action.

## Actor
An actor is an item, but with the ability to perform actions. 
Typically, an actor will not be gettable.



   