#!/usr/bin/python
# -*- coding: utf-8 *-*

from random import choice
from copy import deepcopy

UP_MOVEMENT = 0
RIGHT_MOVEMENT = 1
DOWN_MOVEMENT = 2
LEFT_MOVEMENT = 3

def ini_tiles (rows=4, cols=4):
    return [[0] * cols for _ in xrange(rows)]

def get_free_tiles (values):
    ftiles = []
    for y, r in enumerate(values):
        for x, c in enumerate(r):
            if (c == 0):
                ftiles.append((y, x))
    return ftiles

def set_new_value (values, newvals=None):
    tiles = get_free_tiles(values)
    if len(tiles) == 0:
        return None
    r,c = choice(tiles)
    if newvals is None:
        newvals = [1]
    value = choice(newvals)
    values[r][c] = value
    return (r, c)
    
def move_tiles (values, move):
    watch_cols = []
    watch_rows = []
    incc = incr = 0
    if (move == UP_MOVEMENT):
        watch_cols = range(0, len(values[0]))
        watch_rows = range(0, len(values)-1)
        incr = 1
    elif (move == RIGHT_MOVEMENT):
        watch_cols = range(len(values[0])-1, 0, -1)
        watch_rows = range(0, len(values))
        incc = -1
    elif (move == DOWN_MOVEMENT):
        watch_cols = range(0, len(values[0]))
        watch_rows = range(len(values)-1, 0, -1)
        incr = -1
    elif (move == LEFT_MOVEMENT):
        watch_cols = range(0, len(values[0])-1)
        watch_rows = range(0, len(values))
        incc = 1
    else:
        return
    return _change_values(values, watch_cols, watch_rows, incr, incc)

def _change_values (oldvalues, watch_cols, watch_rows, incr, incc):
    values = deepcopy(oldvalues)
    changes = []
    for c in watch_cols:
        for r in watch_rows:
            if values[r][c] == 0:
                _, pos_ini, pos_fin = _bring_values(values, r, c, incr, incc)
                changes.append([pos_ini, pos_fin, False])
            if values[r][c] == 0:
                continue
            v, pos_ini, pos_fin = _bring_values(values, r+incr, c+incc, incr, incc)
            bringing_nothing = v == 0
            if bringing_nothing:
                continue
            merge = v == values[r][c]
            changes.append([pos_ini, pos_fin, merge])
            if merge:
                values[r+incr][c+incc] = 0
                values [r][c] = v + 1
    changes = [c for c in changes if not c[0] is None]
    return values, changes

def _bring_values (values, row, col, incr, incc):
    is_margin = row <= -1 or row >= len(values) or col <= -1 or col >= len(values[0])
    if is_margin:
        return 0, None, None
    theres_something = values[row][col] != 0
    if theres_something:
        return values[row][col], (row, col), (row, col)
    v, pos_ini, _ = _bring_values(values, row+incr, col+incc, incr, incc)
    bringing_nothing = v == 0
    if bringing_nothing:
        return 0, None, None
    values[row][col] = v
    values[row+incr][col+incc] = 0
    return v, pos_ini, (row, col)
    