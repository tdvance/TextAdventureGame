#database of rooms

#name, description, short description, help message, direction, room, direction, room, ...

Rooftop, You are on the roof of a tall building, a rooftop, The rooftop is very gritty, Down, StreetTallBuilding
StreetTallBuilding, You are on a trash-strewn street at the base of a tall building, a street, The street is potholed and trashy, West, ApartmentBuilding, South, StreetTheater
ApartmentBuilding, You are on a street near an apartment building with an open window just above you, outside an apartment building, The apartment building is a slum, East, StreetTallBuilding, Up, InsideApartment
StreetTheater, You are on a street in front of a decrepit theater and near a window into an apartment, outside a theater, It appears to be an X-rated theater, North, StreetTallBuilding, East, InsideTheater, Up, ApartmentRoom
InsideTheater, You are inside a run-down theater, a theater, It appears to be abandoned, West, StreetTheater
InsideApartment, You are inside a ratty apartment. The street is down below from a window, an apartment, There are stains on the carpet and the plaster is crumbling, Down, ApartmentBuilding, South, ApartmentRoom
ApartmentRoom, You are inside a ratty apartment.  The street is down below from a window, an apartment room, This room looks no better than the other room, Down, StreetTheater, North, InsideApartment

