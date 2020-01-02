import pygame
import sys
from pygame.mixer import *
# import time
# import random
from assets import *
from settings import Settings
from AI import *

# def game(screen,screen_width,screen_height):
def game(mode="single"):
    
    # Data structure
    congklak_data = [[["pos1"],0],[["pos2"],5],[["pos3"],5],[["pos4"],5],[["pos5"],5]
                    ,[["pos6"],5],[["pos7"],5],[["pos8"],5],[["pos9"],0],[["pos10"],5]
                    ,[["pos11"],5],[["pos12"],5],[["pos13"],5],[["pos14"],5],[["pos15"],5]
                    ,[["pos16"],5]]
    if mode == "single":
        p1 = [True, 0, 0, "p1", AI_Minimax(7, pruning=True)]
    elif mode == "multi":
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

            playing_for_turn = True
            while playing_for_turn:
                print(playing[3])
                
                small_holes = 0 #total number of shells in current player's small holes
                if playing[3] == "p1":
                    index_hole = 1
                    while index_hole < 8: #to sum up small holes
                        small_holes += congklak_data[index_hole][1]
                        index_hole += 1
                elif playing[3] == "p2":
                    index_hole = 9
                    while index_hole <= 15: #to sum up small holes
                        small_holes += congklak_data[index_hole][1]
                        index_hole += 1
                if small_holes == 0:
                    playing_for_turn = False
                    continue
                
                index_not_allowed = True
                while index_not_allowed: #to check if the taken hole is valid
                    if mode == "multi" or playing[3] == "p2":
                        chosen_index = int(input("Choose which small hole you want to take: ")) - 1
                    elif mode == "single" and playing[3] == "p1":
                        print("Ori:", congklak_data)
                        chosen_index = playing[4].commitMove(congklak_data)
                        print("Ori:", congklak_data, "\nChosen index:", chosen_index)

                    if chosen_index > 15:
                        print("index out of bound")
                        continue

                    if playing[3] == "p1":
                        if congklak_data[chosen_index][1] > 0 and 0 < chosen_index < 8:
                            playing[1] = congklak_data[chosen_index][1]
                            congklak_data[chosen_index][1] = 0
                            index_not_allowed = False
                        else:
                            print("This hole is empty/can't be chosen for %s, choose another one" % playing[3])
                    elif playing[3] == "p2":
                        if congklak_data[chosen_index][1] > 0 and 8 < chosen_index <= 15:
                            playing[1] = congklak_data[chosen_index][1]
                            congklak_data[chosen_index][1] = 0
                            index_not_allowed = False
                        else:
                            print("This hole is empty/can't be chosen for %s, choose another one" % playing[3])

                while playing[1] > 0: #to spread the shells in hand until none left
                    chosen_index += 1
                    if chosen_index > 15:
                        chosen_index = 0

                    # to check if the current index is at enemy's home index
                    if playing[3] == "p1" and chosen_index == 8:
                        continue
                    elif playing[3] == "p2" and chosen_index == 0:
                        continue

                    debug(chosen_index, playing, congklak_data)

                    if playing[1] == 1: #action yang dilakukan ketika biji di tangan tersisa 1
                        if congklak_data[chosen_index][1] > 0 and chosen_index != 0 and chosen_index != 8: #lanjut main -> mulai dari index berikutnya
                            playing[1] += congklak_data[chosen_index][1]
                            congklak_data[chosen_index][1] = 0
                            debug(chosen_index, playing, congklak_data, "test kalo biji jatuh di tempat yang ada bijinya")
                            continue
                        elif playing[3] == "p1":
                            if chosen_index > 8 and chosen_index <= 15 and congklak_data[chosen_index][1] == 0: #lubang kosong lawan -> end
                                playing_for_turn = False
                                pass
                            elif chosen_index > 0 and chosen_index < 8 and congklak_data[chosen_index][1] == 0:
                                #lubang kosong pemain saat ini -> ambil milik lawan seberang -> masukkan ke dalam markas pemain saat ini -> end
                                congklak_data[0][1] = congklak_data[0][1] + playing[1] + congklak_data[-abs(chosen_index)][1]
                                playing[1] = 0
                                congklak_data[chosen_index][1] = 0
                                congklak_data[-abs(chosen_index)][1] = 0
                                playing_for_turn = False
                                debug_1(chosen_index, -abs(chosen_index), playing, congklak_data, "test kalo jatuh di lubang kecil yang main")
                                continue
                            elif chosen_index == 0:
                                #lubang terakhir == markas pemain saat ini -> pilih lubang untuk bermain lagi -> mulai dari index berikutnya
                                pass
                        elif playing[3] == "p2":
                            if chosen_index > 0 and chosen_index < 8 and congklak_data[chosen_index][1] == 0: #lubang kosong lawan -> end
                                playing_for_turn = False
                                pass
                            elif chosen_index > 8 and chosen_index <= 15 and congklak_data[chosen_index][1] == 0:
                                #lubang kosong pemain saat ini -> ambil milik lawan seberang -> masukkan ke dalam markas pemain saat ini -> end
                                congklak_data[8][1] = congklak_data[8][1] + playing[1] + congklak_data[len(congklak_data) - chosen_index][1]
                                playing[1] = 0
                                congklak_data[chosen_index][1] = 0
                                congklak_data[len(congklak_data) - chosen_index][1] = 0
                                playing_for_turn = False
                                debug_1(chosen_index, len(congklak_data) - chosen_index, playing, congklak_data, "test kalo jatuh di lubang kecil yang main")
                                continue
                            elif chosen_index == 8:
                                #lubang terakhir == markas pemain saat ini -> pilih lubang untuk bermain lagi -> mulai dari index berikutnya
                                pass

                    congklak_data[chosen_index][1] += 1
                    playing[1] -= 1
                    debug(chosen_index, playing, congklak_data)
            
            #to switch player on the next turn
            playing[0] = False
            not_playing[0] = True

def debug(chosen_index, playing, congklak_data, test_status = "default test"):
    print("\n" + test_status)
    print("index sekarang:", chosen_index)
    print("biji di index sekarang:", congklak_data[chosen_index][1])
    print("biji di tangan pemain %s: %d" %(playing[3], playing[1]))

def debug_1(chosen_index, chosen_index_oposite, playing, congklak_data, test_status = "default test"):
    print("\n" + test_status)
    print("index sekarang:", chosen_index)
    print("index seberang:", chosen_index_oposite)
    print("biji di index sekarang:", congklak_data[chosen_index][1])
    print("biji di index seberang:", congklak_data[chosen_index_oposite][1])
    print("biji di tangan pemain %s: %d" %(playing[3], playing[1]))
    if playing[3] == "p1":
        print("biji di markas pemain %s: %d" %(playing[3], congklak_data[0][1]))
    else:
        print("biji di markas pemain %s: %d" %(playing[3], congklak_data[8][1]))

if __name__ == "__main__":
    game()
