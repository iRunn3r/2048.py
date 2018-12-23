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

def rotate_board(dir):
	global BOARD
	if dir == "right":
		BOARD = np.rot90(BOARD, 2)
	elif dir == "up":
		BOARD = np.rot90(BOARD, 1)
	elif dir == "down":
		BOARD = np.rot90(BOARD, 3)

def rotate_back():
	global BOARD
	if dir == "right":
		BOARD = np.rot90(BOARD, 2)
	elif dir == "up":
		BOARD = np.rot90(BOARD, 3)
	elif dir == "down":
		BOARD = np.rot90(BOARD, 1)

os.system('cls')
print(BOARD)
insert_number()

while True:
	dir = input()
	rotate_board(dir)
	shift_board()
	rotate_back()
	insert_number()
	os.system('cls')
	print(BOARD)
