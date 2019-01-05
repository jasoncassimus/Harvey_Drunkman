import unittest
from walk import Direction, Harvey, Map


class CreateWalkTest(unittest.TestCase):
    def setUp(self):
        self.walk = Map()

    def test_island(self):
        for x in range(self.walk.island_boundary, self.walk.width - self.walk.island_boundary):
            for y in range(self.walk.island_boundary, self.walk.length - self.walk.island_boundary):
                if x != self.walk.walkway:
                    self.assertEqual(self.walk.TileValue.START_FLOWER, self.walk.island[x][y])

    def test_top_row(self):
        for y in range(0, self.walk.length):
            self.assertEqual(self.walk.TileValue.WATER, self.walk.island[0][y])

    def test_exit(self):
        for i in range(self.walk.island_boundary, self.walk.length - 2):
            self.assertEqual(self.walk.TileValue.EMPTY, self.walk.island[self.walk.walkway][i])
        self.assertEqual(self.walk.TileValue.EXIT, self.walk.island[self.walk.walkway][0])
        self.assertEqual(self.walk.TileValue.EXIT, self.walk.island[self.walk.walkway][self.walk.length - 1])

class WalkSimulationTest(unittest.TestCase):
    def setUp(self):
        self.walk


class HarveyTest(unittest.TestCase):
    def setUp(self):
        self.island = Map()
        self.harvey = Harvey(self.island)

    def test_walk(self):
        self.harvey.walk(Direction.EAST)
        self.assertEqual((self.island.walkway, 2), self.harvey.pos)

