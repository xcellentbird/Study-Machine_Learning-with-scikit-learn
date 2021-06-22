from itertools import product
from pprint import *
from copy import deepcopy

def rot90(key):
    size = len(key)
    ret = [[0] * size for _ in range(size)]
    for i, j in product(range(size), range(size)):
        ret[j][i] = key[-i-1][j]
    return ret

def zero_padding(lock, pad_size):
    side_pad = [[0] * pad_size + row + [0] * pad_size for row in lock]
    return [[0] * (len(lock)+(2*pad_size)) for _ in range(pad_size)] + side_pad + [[0] * (len(lock)+(2*pad_size)) for _ in range(pad_size)]

def move_matching(key, lock):
    key_size = len(key)
    lock_size = len(lock)
    pad_size = len(key)-1
    padded_lock = zero_padding(lock, pad_size)
    
    for move_y in range(len(lock) + pad_size):
        for move_x in range(len(lock) + pad_size):
            copy_lock = deepcopy(padded_lock)

            for j, i in product(range(key_size), range(key_size)):
                copy_lock[j+move_y][i+move_x] += key[j][i]
                if pad_size <= j+move_y < lock_size + pad_size and pad_size <= i+move_x < lock_size + pad_size and copy_lock[j+move_y][i+move_x] != 1:
                    break
            else:
                if sum([sum(copy_lock[row][pad_size:lock_size + pad_size]) for row in range(pad_size, lock_size + pad_size)]) == lock_size**2:
                    return True
            
    return False
    
def solution(key, lock):
    
    if move_matching(key, lock):
        return True
    
    # rotate
    for _ in range(3):
        key = rot90(key)
        if move_matching(key, lock):
            return True
    
    return False
