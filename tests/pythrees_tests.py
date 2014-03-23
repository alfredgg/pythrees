#!/usr/bin/python
# -*- coding: utf-8 *-*

from unittest import TestCase
import pythrees

class TestMovement(TestCase):
    def test_up_00 (self):
        ini = [[0], [1], [0]]
        current, _ = pythrees.move_tiles(ini, pythrees.UP_MOVEMENT)
        expected = [[1], [0], [0]]
        self.assertEqual(expected, current)

    def test_right_00 (self):
        ini = [[1,0,0]]
        current, _ = pythrees.move_tiles(ini, pythrees.RIGHT_MOVEMENT)
        expected = [[0,0,1]]
        self.assertEqual(expected, current)

    def test_down_00 (self):
        ini = [[1,0,0], [0,0,0], [0,0,0]]
        current, _ = pythrees.move_tiles(ini, pythrees.DOWN_MOVEMENT)
        expected = [[0,0,0], [0,0,0], [1,0,0]]
        self.assertEqual(expected, current)
    
    def test_left_00 (self):
        ini = [[0,0,1], [0,0,0], [0,0,0]]
        current, _ = pythrees.move_tiles(ini, pythrees.LEFT_MOVEMENT)
        expected = [[1,0,0], [0,0,0], [0,0,0]]
        self.assertEqual(expected, current)

class TestMerge (TestCase):
    def test_merge_00(self):
        ini = [[1], [1], [0]]
        current, _ = pythrees.move_tiles(ini, pythrees.UP_MOVEMENT)
        expected = [[2], [0], [0]]
        self.assertEqual(expected, current)
    
    def test_merge_01(self):
        ini = [[2], [1], [0]]
        current, _ = pythrees.move_tiles(ini, pythrees.UP_MOVEMENT)
        expected = [[2], [1], [0]]
        self.assertEqual(expected, current)

    def test_merge_02(self):
        ini = [[2], [1], [1]]
        current, _ = pythrees.move_tiles(ini, pythrees.UP_MOVEMENT)
        expected = [[2], [2], [0]]
        self.assertEqual(expected, current)
    
    def test_merge_03(self):
        ini = [[2], [2], [1], [1]]
        current, _ = pythrees.move_tiles(ini, pythrees.UP_MOVEMENT)
        expected = [[3], [2], [0], [0]]
        self.assertEqual(expected, current)

    def test_merge_04(self):
        ini = [[0], [1], [1]]
        current, _ = pythrees.move_tiles(ini, pythrees.UP_MOVEMENT)
        expected = [[2], [0], [0]]
        self.assertEqual(expected, current)

    def test_merge_05(self):
        ini = [[3], [1], [1]]
        current, _ = pythrees.move_tiles(ini, pythrees.UP_MOVEMENT)
        expected = [[3], [2], [0]]
        self.assertEqual(expected, current)

    def test_merge_06(self):
        ini = [[2], [0], [0], [2]]
        current, _ = pythrees.move_tiles(ini, pythrees.UP_MOVEMENT)
        expected = [[3], [0], [0], [0]]
        self.assertEqual(expected, current)

    def test_merge_07(self):
        ini = [[2], [0], [1], [1]]
        current, _ = pythrees.move_tiles(ini, pythrees.UP_MOVEMENT)
        expected = [[2], [2], [0], [0]]
        self.assertEqual(expected, current)
        
    def test_merge_08(self):
        ini = [[2], [2], [2], [0]]
        current, _ = pythrees.move_tiles(ini, pythrees.UP_MOVEMENT)
        expected = [[3], [2], [0], [0]]
        self.assertEqual(expected, current)
        
class TestChanges (TestCase):
    def test_changes_00(self):
        ini = [[2], [2], [2], [0]]
        _, current = pythrees.move_tiles(ini, pythrees.UP_MOVEMENT)
        expected = [[(1,0), (0,0), True], [(2,0), (1,0), False]]
        self.assertEqual(expected, current)
'''        
    def test_changes_01(self):
        ini = [[2, 0, 0], [2, 0, 0], [2, 0, 1]]
        _, current = pythrees.move_tiles(ini, pythrees.UP_MOVEMENT)
        expected = [[(1,0), (0,0), True], [(2,0), (1,0), False], [(2,2), (2,0), False]]
        self.assertEqual(expected, current)
'''    