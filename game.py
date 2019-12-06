# from pygame.mixer import *
# import time
# import random
# from assets import Assets

# def game(screen,screen_width,screen_height):
def game():
    #Music & sound effects
        #your codes here
    
    #Background
        #your codes here
    
    #Sprites
        #your codes here

    #Buttons & signs
        #your codes here
    
    #Data structure
    congklak_data = [[["pos1"],0],[["pos2"],5],[["pos3"],5],[["pos4"],5],[["pos5"],5]
                    ,[["pos6"],5],[["pos7"],5],[["pos8"],5],[["pos9"],0],[["pos10"],5]
                    ,[["pos11"],5],[["pos12"],5],[["pos13"],5],[["pos14"],5],[["pos15"],5]
                    ,[["pos16"],5]]
    p1 = [True, 0, 0, "p1"]
    p2 = [False, 0, 0, "p2"]
    playing = [] #for in-game
    not_playing = [] #for in-game

    #entar untuk sprites maybe tiap lubang buat jadi 1 grup, instead of 1 whole big group(?)
    
    running = True
    while running:
        small_holes = 0 #total number of shells in all small holes
        
        index_hole = 0
        while index_hole <= 15: #to sum up small holes
            if index_hole == 0 or index_hole == 8:
                pass
            else:
                small_holes += congklak_data[index_hole][1]
            index_hole += 1
        
        if small_holes == 0: #winning check
            if congklak_data[0][1] > congklak_data[8][1]:
                p1[2] = 1
                print("Player 1 wins")
            elif congklak_data[0][1] == congklak_data[8][1]:
                p1[2] = 1
                p2[2] = 1
                print("Draw")
            else:
                p2[2] = 1
                print("Player 2 wins")
            running = False
        
        else:
            if p1[0]: #to check which player goes for this turn
                playing = p1
                not_playing = p2
            else:
                playing = p2
                not_playing = p1

            print(playing[3])

            index_not_allowed = True
            while index_not_allowed: #to check if the taken hole is valid
                chosen_index = int(input("Choose which small hole you want to take: ")) - 1
                if chosen_index <= 15:
                    if congklak_data[chosen_index][1] > 0 and chosen_index != 0 and chosen_index != 8:
                        playing[1] = congklak_data[chosen_index][1]
                        congklak_data[chosen_index][1] = 0
                        index_not_allowed = False
                    else:
                        print("This hole is empty/can't be chosen, choose another one")
                else:
                    print("index hole is out of bound")
            
            while playing[1] > 0: #to spread the shells in hand until none left
                chosen_index += 1
                if chosen_index > 15:
                    chosen_index = 0
                congklak_data[chosen_index][1] += 1
                playing[1] -= 1

            #to switch player on the next turn
            playing[0] = False
            not_playing[0] = True

game()
