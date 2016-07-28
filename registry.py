import sys

class Registry:
    all_rooms = dict()

    @classmethod
    def add_room(cls, name, room):
        if name in cls.all_rooms:
            cls.error("Room %s already exists in registry as %s", name, cls.all_rooms[name])
        cls.all_rooms[name] = room

    @classmethod
    def error(cls, format_str, *args):
        print(format_str % args, file=sys.stderr)
        assert not "Fatal Error"

    @classmethod
    def contains(cls, room_name):
        return room_name in cls.all_rooms

    @classmethod
    def get_room(cls, room_name):
        return cls.all_rooms[room_name]

