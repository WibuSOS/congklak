# import sklearn
class AI:
    # game_node = []
    
    def __init__(self):
        pass

    def checkLegalMoves(self, node):
        node_data = []
        # self.game_node = node
        small_holes = 0 #total number of shells in all small holes

        index_hole = 0
        while index_hole <= 15: #to sum up small holes
            if index_hole == 0 or index_hole == 8:
                pass
            else:
                small_holes += node[index_hole][1]
            index_hole += 1

        if small_holes == 0: #winning check
            if node[0][1] > node[8][1]:
                p1[2] = 1
                print("Player 1 wins")
            elif node[0][1] == node[8][1]:
                p1[2] = 1
                p2[2] = 1
                print("Draw")
            else:
                p2[2] = 1
                print("Player 2 wins")
            running = False
        
        return len(node_data), node_data
    
    def commitMove(self, parameter_list):
        pass
    
    def checkFreeTurn(self, child):
        if True: # posisi awal di lubang kecil yang ada bijinya
            child_data = []
            possible_child = len(child_data)
            childFreeTurn = True
        elif True: # posisi awal di lubang besar milik pribadi
            possible_child, child_data = self.checkLegalMoves(child)
            childFreeTurn = True
        else: # posisi awal di lubang yang mengakhiri giliran
            child_data = []
            possible_child = len(child_data)
            childFreeTurn = False
        
        return childFreeTurn, possible_child, child_data

    def heuristicNode(self, node):
        pass
    
    def minimax(self, node, depth, maximizingPlayer, freeTurn, freeTurnData):
        if depth == 0: # or node is a terminal node
            return self.heuristicNode(node) # the heuristic value of node
        
        if maximizingPlayer:
            bestValue = int
            if freeTurn:
                possible_child, node_data = freeTurnData[0], freeTurnData[1]
            else:
                possible_child, node_data = self.checkLegalMoves(node)

            for i in range(possible_child): # each child of node
                # do implementation of child node here
                child = node.copy()
                childFreeTurn, child_possibilities, child_data = self.checkFreeTurn(child)
                
                if childFreeTurn: # here is a small change
                    isMax = True
                else:
                    isMax = False
                
                val = minimax(child, depth - 1, isMax, childFreeTurn, [child_possibilities, child_data])
                bestValue = max(bestValue, val)
            
            return bestValue
        else:
            bestValue = int
            if freeTurn:
                possible_child, node_data = freeTurnData[0], freeTurnData[1]
            else:
                possible_child, node_data = self.checkLegalMoves(node)

            for i in range(possible_child): # each child of node
                # do implementation of child node here
                child = node.copy()
                childFreeTurn, child_possibilities, child_data = self.checkFreeTurn(child)

                if childFreeTurn: # here is a small change
                    isMax = False
                else:
                    isMax = True
                
                val = minimax(child, depth - 1, isMax, childFreeTurn, [child_possibilities, child_data])
                bestValue = min(bestValue, val)
            
            return bestValue