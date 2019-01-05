import random
from enum import Enum, auto



def next_direction(chance: int):
    chances = [45, 70, 90, 100]
    chances_map = {
        chances[0]: Direction.EAST,
        chances[1]: Direction.SOUTH,
        chances[2]: Direction.NORTH,
        chances[3]: Direction.WEST,
    }
    for i in chances:
        if chance < i:
            return chances_map[i]
    return None


def simulate():
    island = Map()
    harvey = Harvey(island)
    flowers_destroyed = 0
    while not harvey.is_done():
        chance = random.randint(0, 99)
        direction = next_direction(chance)
        harvey.walk(direction)
        if harvey.stomped_flower():
            flowers_destroyed += 1
            island.kill_flower(harvey.pos)
    return flowers_destroyed, harvey.is_drowning()


class Direction(Enum):
    NORTH = auto()
    SOUTH = auto()
    EAST = auto()
    WEST = auto()


class Harvey:
    neighbor_tiles = {
        Direction.NORTH: (-1, 0),
        Direction.SOUTH: (1, 0),
        Direction.EAST: (0, 1),
        Direction.WEST: (0, -1)
    }

    def __init__(self, island):
        self.pos = (island.walkway, 1)
        self.island = island

    def walk(self, direction: Direction):
        inc_x, inc_y = self.neighbor_tiles[direction]
        curr_x, curr_y = self.pos
        self.pos = (curr_x + inc_x, curr_y + inc_y)

    def is_done(self) -> bool:
        current_tile = self.island.tile_value(self.pos)
        return current_tile == Map.TileValue.EXIT.value or current_tile == Map.TileValue.WATER.value

    def stomped_flower(self) -> bool:
        return self.island.tile_value(self.pos) > 0

    def is_drowning(self) -> bool:

        """
        :return: If he fell in the water
        """

        return self.island.tile_value(self.pos) == Map.TileValue.WATER.value


class Map:
    class TileValue(Enum):
        EXIT = -2
        WATER = -1
        START_FLOWER = 2
        EMPTY = 0

    def __init__(self):
        self.island = []
        self.width = 12
        self.length = 14
        self.island_boundary = 1
        self.walkway = int((self.width - 1) / 2)

        for x in range(0, self.width):
            row = []
            for y in range(0, self.length):
                row.append(self.TileValue.START_FLOWER.value)
            self.island.append(row)

        self.create_water()
        self.create_exit()

    def create_water(self):
        for y in range(0, self.length):
            self.island[0][y] = self.TileValue.WATER.value
            self.island[self.width - 1][y] = self.TileValue.WATER.value

        for x in range(0, self.width):
            self.island[x][0] = self.TileValue.WATER.value
            self.island[x][self.length - 1] = self.TileValue.WATER.value

    def create_exit(self):
        for i in range(0, self.length):
            self.island[self.walkway][i] = self.TileValue.EMPTY.value

        self.island[self.walkway][0] = self.TileValue.EXIT.value
        self.island[self.walkway][self.length - 1] = self.TileValue.EXIT.value

    def tile_value(self, pos: (int, int)) -> TileValue:
        x, y = pos
        return self.island[x][y]

    def kill_flower(self, pos: (int, int)):
        x, y = pos
        self.island[x][y] -= 1



