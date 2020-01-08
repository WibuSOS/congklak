import sys
from pygame import *
from AI import *
from assets import *

def game(screen, screen_width, screen_height, mode="single"):
# def game(mode="single"):
    # Data structure
    congklak_data = [[[145,370],0],[[130,160],5],[[290,160],5],[[460,160],5],[[630,160],5]
                    ,[[790,160],5],[[960,160],5],[[1130,160],5],[[1120,370],0],[[1130,590],5]
                    ,[[960,590],5],[[790,590],5],[[630,590],5],[[460,590],5],[[290,590],5]
                    ,[[130,590],5]]
    if mode == "single":
        p1 = [True, 0, 0, "p1", AI_Minimax(7, maximizingPlayer=True, pruning=True)]
        p2 = [False, 0, 0, "p2"]
    elif mode == "multi":
        p1 = [True, 0, 0, "p1"]
        p2 = [False, 0, 0, "p2"]
    elif mode == "AI":
        p1 = [True, 0, 0, "p1", AI_Negamax(7, player=1, pruning=True)]
        p2 = [False, 0, 0, "p2", AI_Minimax(7, maximizingPlayer=False, pruning=True)]
    playing = [] #for in-game
    not_playing = [] #for in-game

    # Sprites
    sleepTime = 1000
    congklakBoard = Board(screen)
    house0 = Seed('images/bijicongklak.png', congklak_data[0][0])
    hole1 = Seed('images/bijicongklak.png', congklak_data[1][0])
    hole2 = Seed('images/bijicongklak.png', congklak_data[2][0])
    hole3 = Seed('images/bijicongklak.png', congklak_data[3][0])
    hole4 = Seed('images/bijicongklak.png', congklak_data[4][0])
    hole5 = Seed('images/bijicongklak.png', congklak_data[5][0])
    hole6 = Seed('images/bijicongklak.png', congklak_data[6][0])
    hole7 = Seed('images/bijicongklak.png', congklak_data[7][0])
    house8 = Seed('images/bijicongklak.png', congklak_data[8][0])
    hole9 = Seed('images/bijicongklak.png', congklak_data[9][0])
    hole10 = Seed('images/bijicongklak.png', congklak_data[10][0])
    hole11 = Seed('images/bijicongklak.png', congklak_data[11][0])
    hole12 = Seed('images/bijicongklak.png', congklak_data[12][0])
    hole13 = Seed('images/bijicongklak.png', congklak_data[13][0])
    hole14 = Seed('images/bijicongklak.png', congklak_data[14][0])
    hole15 = Seed('images/bijicongklak.png', congklak_data[15][0])

    seed_data = [house0,hole1,hole2,hole3,hole4,hole5,hole6,hole7,house8,hole9,hole10,hole11,hole12,hole13,hole14,hole15]
    congklakSeeds = Group(hole1,hole2,hole3,hole4,hole5,hole6,hole7,hole9,hole10,hole11,hole12,hole13,hole14,hole15)
    score_data = []
    seedScores = Group()

    for data in congklak_data:
        x = data[0][0]
        y = data[0][1] + 40
        score = SeedScore([x,y], data[1])
        score_data.append(score)
        seedScores.add(score)
    
    running = True
    while running:
        screen.fill((255,255,255))
        congklakBoard.blitme()
        congklakSeeds.draw(screen)
        seedScores.draw(screen)
        display.update()

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
            print(congklak_data)
            running = False
        
        else:
            if p1[0]: #to check which player goes for this turn
                playing = p1
                not_playing = p2
            else:
                playing = p2
                not_playing = p1

            playerturn = Player([60,20], playing[3])
            playing_for_turn = True
            while playing_for_turn:
                print("Player:", playing[3])
                screen.fill((255,255,255))
                congklakBoard.blitme()
                congklakSeeds.draw(screen)
                seedScores.draw(screen)
                playerturn.draw(screen)
                display.update()

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
                    screen.fill((255,255,255))
                    congklakBoard.blitme()
                    congklakSeeds.draw(screen)
                    seedScores.draw(screen)
                    playerturn.draw(screen)
                    display.update()

                    if mode == "AI" or (mode == "single" and playing[3] == "p1"):
                        chosen_index = playing[4].commitMove(congklak_data)
                        print("Ori:", congklak_data, "\nChosen index:", chosen_index)
                    elif mode == "multi" or playing[3] == "p2":
                        chosen_index = None
                        for command in event.get():
                            if command.type == QUIT:
                                running = False
                                pygame.quit()
                            
                            if command.type == MOUSEBUTTONDOWN and command.button == 1:
                                if hole1.rect.collidepoint(mouse.get_pos()):
                                    chosen_index = 1
                                if hole2.rect.collidepoint(mouse.get_pos()):
                                    chosen_index = 2
                                if hole3.rect.collidepoint(mouse.get_pos()):
                                    chosen_index = 3
                                if hole4.rect.collidepoint(mouse.get_pos()):
                                    chosen_index = 4
                                if hole5.rect.collidepoint(mouse.get_pos()):
                                    chosen_index = 5
                                if hole6.rect.collidepoint(mouse.get_pos()):
                                    chosen_index = 6
                                if hole7.rect.collidepoint(mouse.get_pos()):
                                    chosen_index = 7
                                if hole9.rect.collidepoint(mouse.get_pos()):
                                    chosen_index = 9
                                if hole10.rect.collidepoint(mouse.get_pos()):
                                    chosen_index = 10
                                if hole11.rect.collidepoint(mouse.get_pos()):
                                    chosen_index = 11
                                if hole12.rect.collidepoint(mouse.get_pos()):
                                    chosen_index = 12
                                if hole13.rect.collidepoint(mouse.get_pos()):
                                    chosen_index = 13
                                if hole14.rect.collidepoint(mouse.get_pos()):
                                    chosen_index = 14
                                if hole15.rect.collidepoint(mouse.get_pos()):
                                    chosen_index = 15
                    
                    if chosen_index == None:
                        print("Wrong mouse position")
                        continue
                    
                    if chosen_index > 15:
                        print("index out of bound")
                        continue

                    if playing[3] == "p1":
                        if congklak_data[chosen_index][1] > 0 and 0 < chosen_index < 8:
                            playing[1] = congklak_data[chosen_index][1]
                            congklak_data[chosen_index][1] = 0
                            score_data[chosen_index].reset()
                            congklakSeeds.remove(seed_data[chosen_index])
                            index_not_allowed = False
                        else:
                            print("This hole is empty/can't be chosen for %s, choose another one" % playing[3])
                    elif playing[3] == "p2":
                        if congklak_data[chosen_index][1] > 0 and 8 < chosen_index <= 15:
                            playing[1] = congklak_data[chosen_index][1]
                            congklak_data[chosen_index][1] = 0
                            score_data[chosen_index].reset()
                            congklakSeeds.remove(seed_data[chosen_index])
                            index_not_allowed = False
                        else:
                            print("This hole is empty/can't be chosen for %s, choose another one" % playing[3])
                
                while playing[1] > 0: #to spread the shells in hand until none left
                    screen.fill((255,255,255))
                    congklakBoard.blitme()
                    congklakSeeds.draw(screen)
                    seedScores.draw(screen)
                    playerturn.draw(screen)
                    display.update()

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
                            score_data[chosen_index].reset()
                            congklakSeeds.remove(seed_data[chosen_index])
                            debug(chosen_index, playing, congklak_data, "test kalo biji jatuh di tempat yang ada bijinya")
                            time.wait(sleepTime)
                            continue
                        elif playing[3] == "p1":
                            if chosen_index > 8 and chosen_index <= 15 and congklak_data[chosen_index][1] == 0: #hole kosong lawan -> end
                                playing_for_turn = False
                                pass
                            elif chosen_index > 0 and chosen_index < 8 and congklak_data[chosen_index][1] == 0:
                                #hole kosong pemain saat ini -> ambil milik lawan seberang -> masukkan ke dalam markas pemain saat ini -> end
                                congklak_data[0][1] = congklak_data[0][1] + playing[1] + congklak_data[-abs(chosen_index)][1]
                                playing[1] = 0
                                congklak_data[chosen_index][1] = 0
                                score_data[chosen_index].reset()
                                congklakSeeds.remove(seed_data[chosen_index])
                                congklak_data[-abs(chosen_index)][1] = 0
                                score_data[-abs(chosen_index)].reset()
                                congklakSeeds.remove(seed_data[-abs(chosen_index)])
                                playing_for_turn = False
                                debug_1(chosen_index, -abs(chosen_index), playing, congklak_data, "test kalo jatuh di hole kecil yang main")
                                time.wait(sleepTime)
                                continue
                            elif chosen_index == 0:
                                #hole terakhir == markas pemain saat ini -> pilih hole untuk bermain lagi -> mulai dari index berikutnya
                                pass
                        elif playing[3] == "p2":
                            if chosen_index > 0 and chosen_index < 8 and congklak_data[chosen_index][1] == 0: #hole kosong lawan -> end
                                playing_for_turn = False
                                pass
                            elif chosen_index > 8 and chosen_index <= 15 and congklak_data[chosen_index][1] == 0:
                                #hole kosong pemain saat ini -> ambil milik lawan seberang -> masukkan ke dalam markas pemain saat ini -> end
                                congklak_data[8][1] = congklak_data[8][1] + playing[1] + congklak_data[len(congklak_data) - chosen_index][1]
                                playing[1] = 0
                                congklak_data[chosen_index][1] = 0
                                score_data[chosen_index].reset()
                                congklakSeeds.remove(seed_data[chosen_index])
                                congklak_data[len(congklak_data) - chosen_index][1] = 0
                                score_data[len(congklak_data) - chosen_index].reset()
                                congklakSeeds.remove(seed_data[len(congklak_data) - chosen_index])
                                playing_for_turn = False
                                debug_1(chosen_index, len(congklak_data) - chosen_index, playing, congklak_data, "test kalo jatuh di hole kecil yang main")
                                time.wait(sleepTime)
                                continue
                            elif chosen_index == 8:
                                #hole terakhir == markas pemain saat ini -> pilih hole untuk bermain lagi -> mulai dari index berikutnya
                                pass
                    
                    congklak_data[chosen_index][1] += 1
                    score_data[chosen_index].plus()
                    if not congklakSeeds.has(seed_data[chosen_index]):
                        congklakSeeds.add(seed_data[chosen_index])
                    playing[1] -= 1
                    debug(chosen_index, playing, congklak_data)
                    time.wait(sleepTime)
            
            #to switch player on the next turn
            playing[0] = False
            not_playing[0] = True
        
        display.update()

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
