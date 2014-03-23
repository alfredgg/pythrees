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
            _drag_value(values, r, c, incr, incc, changes)
            #_bring_values(values, r, c, incr, incc)
    changes = [chg for chg in changes if chg[1] != ()]
    return values

def _bring_values(values, row, col, incr, incc, first=True):
    currow = row + incr
    curcol = col + incc
    is_margin = currow == -1 or currow == len(values) or curcol == -1 or curcol == len(values[0])
    should_drag =  not first and values[row][col] != 0 
    if is_margin or should_drag:
        return values[row][col]
    value = _bring_values(values, currow, curcol, incr, incc, False)
    curval = values[row][col]
    dont_touch = value != curval and first
    nothing_to_do = value == 0 or dont_touch
    if nothing_to_do:
        return 0
    drag_more = first and curval == 0
    merge = first and curval == value
    values[currow][curcol] = 0
    if drag_more:
        values[row][col] = value
        _bring_values(values, currow, curcol, incr, incc, False)
    elif merge:
        values[row][col] = value + 1
        

def _drag_value (values, row, col, incr, incc, changes, level=0):
    currow = row + incr
    curcol = col + incc
    
    is_margin = currow == -1 or currow == len(values) or curcol == -1 or curcol == len(values[0])
    should_drag =  level != 0 and values[row][col] != 0
    if is_margin or should_drag:
        changes.append([(row, col), (), False])
        return values[row][col]
    
    value = _drag_value(values, currow, curcol, incr, incc, changes, level+1)
    
    nothing_to_do = value == 0
    drag_more = values[row][col] == 0 and value != 0
    merge_values = values[row][col] == value
    
    if nothing_to_do:
        return 0
    elif drag_more:
        values[row][col] = value
        values[currow][curcol] = 0
        changes[-1][1] = (row, col)
        _drag_value(values, row, col, incr, incc, changes, level)
    elif merge_values:
        values[row][col] = value + 1
        values[currow][curcol] = 0
        changes[-1][1] = (row, col)
        changes[-1][2] = True          
    return values[row][col]
    