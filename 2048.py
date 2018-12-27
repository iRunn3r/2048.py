#!/usr/bin/env python3

import numpy as np
import random
from enum import Enum
import os


BOARD_EDGE = 4
BOARD_SIZE = BOARD_EDGE * BOARD_EDGE
BOARD = np.zeros((BOARD_EDGE, BOARD_EDGE))

def insert_number():
	global BOARD
	cell = random.randint(0, BOARD_SIZE-1)
	while BOARD[int(cell/BOARD_EDGE), cell%BOARD_EDGE] != 0:
		cell = random.randint(0, BOARD_SIZE-1)
	BOARD[int(cell/BOARD_EDGE), cell%BOARD_EDGE] = 2

def shift_board():
	global BOARD
	for c in range(BOARD_EDGE-1, 0, -1):
		for r in range(BOARD_EDGE):
			if BOARD[r,c] == BOARD[r, c-1]:
				BOARD[r, c-1] += BOARD[r, c]
				BOARD[r, c] = 0
			elif BOARD[r, c-1] == 0:
				BOARD[r, c-1] = BOARD[r, c]
				BOARD[r, c] = 0

def rotate_board(dir, undo: bool):
	global BOARD
	if dir == "right":
		BOARD = np.rot90(BOARD, 2)
	elif dir == "up":
		BOARD = np.rot90(BOARD, 3 if undo else 1)
	elif dir == "down":
		BOARD = np.rot90(BOARD, 1 if undo else 3)

def clear_screen():
	os.system("clear" if os.name == "posix" else "cls")

clear_screen()
insert_number()
print(BOARD)
while True:
	dir = input()
	rotate_board(dir, False)
	shift_board()
	rotate_board(dir, True)
	insert_number()
	clear_screen()
	print(BOARD)
