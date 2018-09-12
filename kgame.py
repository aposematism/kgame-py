#
# NWEN 241 Programming Assignment 5
# kgame.py Python Source File
#
# Name:
# Student ID:
# 
# IMPORTANT: Implement the functions specified in kgame.h here. 
# You are free to implement additional functions that are not specified in kgame.h here.
#

import random

# This is the title of the game 
KGAME_TITLE = "The K-Game (Python Edition)"

# This is the file name of the saved game state 
KGAME_SAVE_FILE = "kgame.sav"

# Number of tiles per side 
KGAME_SIDES = 4

# Output buffer size in bytess 
KGAME_OUTPUT_BUFLEN = ((18*40)+1)

# Arrow keys 
dirs = { 'UP': 1, 'DOWN': 2, 'LEFT': 3, 'RIGHT': 4 }

# Keys accepted by game 
inputs = { 'LOAD': 5, 'SAVE': 6, 'EXIT': 7} 


def kgame_init(game):
    game['score'] = 0
    game['board'] = [[' ' for x in range(KGAME_SIDES)] for y in range(KGAME_SIDES)] 

#adds a new tile if there is space.
#Altered to check whether there is free space first.
def kgame_add_random_tile(game):    
    freeSpace = False
    for i in range(len(game['board'])):
        for j in range(len(game['board'][i])):
            if(game['board'][i][j] == ' '):
                freeSpace = True
    
    while freeSpace:
        row = random.randint(0, KGAME_SIDES-1)
        col = random.randint(0, KGAME_SIDES-1)
        if game['board'][row][col] == ' ':
            break

    # place to the random position 'A' or 'B' tile
    if(freeSpace):
        game['board'][row][col] = 'A' 
        if random.randint(0, 2) == 1:
            game['board'][row][col] = 'B'

#This renders the game.
def kgame_render(game):
    intermediary = '+-+-+-+-+\n'
    output_buffer = intermediary
    for i in game['board']:
        for a in i:
            output_buffer += '|'+a
        output_buffer += '|\n' + intermediary
    output_buffer += '\n Score: '
    output_buffer += str(game['score'])
    return output_buffer

#Checks for whether game has been won.
def kgame_is_won(game):
    for i in game['board']:
        for a in i:
            if(a == 'K'):
                return True;
    return False

#This checks if a move is possible.
def kgame_is_move_possible(game):
    for i in range(len(game['board'])):
        for j in range(len(game['board'][i])):
            if(i+1 < KGAME_SIDES):
                if(game['board'][i+1][j] == ' '):
                    return True
            if(-1 < i-1):
                if(game['board'][i-1][j] == ' '):
                    return True
            if(j+1 < KGAME_SIDES):
                if(game['board'][i][j+1] == ' '):
                    return True
            if(-1 < j-1):
                if(game['board'][i][j-1] == ' '):
                    return True
    return False

#This is the hard stuff.
#This method first checks the matching letters then it does the empty spaces.
def kgame_update(game, direction):
    tempArray = [[' ' for x in range(KGAME_SIDES)] for y in range(KGAME_SIDES)] 
    for i in range(len(game['board'])):
        for j in range(len(game['board'][i])):
            tempArray[i][j] = game['board'][i][j]
    if(direction == 1):#Up
        for z in range(0, 4):
            for i in range(len(game['board'])-1, 0, -1):#First do the matching letters
                for j in range(len(game['board'][i])):
                    if(-1 < i-1):
                        if(game['board'][i][j] != ' ' and game['board'][i-1][j] == game['board'][i][j]):
                            value = ord(game['board'][i-1][j]) - ord('A')
                            value += 1 #This is for the case where A and A match to give 2.
                            game['score']  += 2 ** value
                            game['board'][i-1][j] = chr(ord(game['board'][i][j]) + 1) #This increments the character. From 
                            game['board'][i][j] = ' '
            
            for i in range(len(game['board'])-1, 0, -1):#Now the empty space.
                for j in range(len(game['board'][i])):
                    if(-1 < i-1):
                        if(game['board'][i][j] != ' ' and game['board'][i-1][j] == ' '):
                            game['board'][i-1][j] = game['board'][i][j]
                            game['board'][i][j] = ' '
                        
    if(direction == 2):#Down
        for z in range(0, 4):
            for i in range(len(game['board'])): #First do the matching letters
                for j in range(len(game['board'][i])):
                    if(i+1 < KGAME_SIDES):
                        if(game['board'][i][j] != ' ' and game['board'][i+1][j] == game['board'][i][j]):
                            value = ord(game['board'][i+1][j]) - ord('A')
                            value += 1 #This is for the case where A and A match to give 2.
                            game['score']  += 2 ** value
                            game['board'][i+1][j] = chr(ord(game['board'][i][j]) + 1) #This increments the character. From 
                            game['board'][i][j] = ' '
            
            for i in range(len(game['board'])): #Now the empty spaces.
                for j in range(len(game['board'][i])):
                    if(i+1 < KGAME_SIDES):
                        if(game['board'][i][j] != ' ' and game['board'][i+1][j] == ' '):
                            game['board'][i+1][j] = game['board'][i][j]
                            game['board'][i][j] = ' '
                        
    if(direction == 3):#Left
        for z in range(0, 4):
            for i in range(len(game['board'])):#First do the matching letters
                for j in range(len(game['board'][i])-1, 0, -1):
                    if(-1 < j-1):
                        if(game['board'][i][j] != ' ' and game['board'][i][j-1] == game['board'][i][j]):
                            value = ord(game['board'][i][j-1]) - ord('A')
                            value += 1 #This is for the case where A and A match to give 2.
                            game['score']  += 2 ** value
                            game['board'][i][j-1] = chr(ord(game['board'][i][j]) + 1) #This increments the character. From 
                            game['board'][i][j] = ' '
            
            for i in range(len(game['board'])):#Now the empty spaces.
                for j in range(len(game['board'][i])-1, 0, -1):
                    if(-1 < j-1):
                        if(game['board'][i][j] != ' ' and game['board'][i][j-1] == ' '):
                            game['board'][i][j-1] = game['board'][i][j]
                            game['board'][i][j] = ' '

    if(direction == 4):#Right
        for z in range(0, 4):
            for i in range(len(game['board'])):
                for j in range(len(game['board'][i])):
                    if(j+1 < KGAME_SIDES):
                        if(game['board'][i][j] != ' ' and game['board'][i][j+1] == game['board'][i][j]):
                            value = ord(game['board'][i][j+1]) - ord('A')
                            value += 1 #This is for the case where A and A match to give 2.
                            game['score']  += 2 ** value
                            game['board'][i][j+1] = chr(ord(game['board'][i][j]) + 1) #This increments the character. From 
                            game['board'][i][j] = ' '
            
            for i in range(len(game['board'])):
                for j in range(len(game['board'][i])):
                    if(j+1 < KGAME_SIDES):
                        if(game['board'][i][j] != ' ' and game['board'][i][j+1] == ' '):
                            game['board'][i][j+1] = game['board'][i][j]
                            game['board'][i][j] = ' '
    kgame_add_random_tile(game)#add a tile.
    for i in range(len(game['board'])):#check for a change.
        for j in range(len(game['board'][i])):
            if(tempArray[i][j] != game['board'][i][j]):
                return True
    return False;    

#This writes the file.
def kgame_save(game):
    toWrite = ""
    try:
        with open(KGAME_SAVE_FILE, "w+") as f:
            for i in range(0, len(game['board']), 1):
                for j in range(0, len(game['board'][i]), 1):
                    if(j == ' '):
                        toWrite += '-'
                    else:
                        toWrite += game['board'][i][j]
            toWrite += ' '
            toWrite += str(game['score'])
            f.write(toWrite)
            f.close()
    except IOError:
        return False    
    return True

#This reads the file.
def kgame_load(game):
    try:
        with open(KGAME_SAVE_FILE, "r") as f:
            for i in range(0, 16, 1):
                p = f.read(1)
                for z in range(ord('A'), ord('A')+10, 1):
                    if(p == '-')
                        pass
                    elif(p == chr(z)){
                        break
                    }
            
            f.close()
    except IOError:
        return False
    
    try:
        with open(KGAME_SAVE_FILE, "r") as f:
            for i in range(0, len(game['board']), 1):
                for j in range(0, len(game['board'][i]), 1):
                    p = f.read(1)
                    if(p == '-'):
                        game['board'][i][j] = ' '
                    else:
                        game['board'][i][j] = p
            f.read(1)
            game['score'] =int( f.read())
            f.close()
    except IOError:
        return False
    return True
