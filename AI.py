# import sklearn
class AI:
    # game_node = []
    
    def __init__(self):
        pass

    def checkLegalMoves(self, node): # TODO Selesaikan fungsi checkLegalMoves
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
    
    def commitMove(self, parameter_list): # TODO Selesaikan fungsi commitMove
        pass
    
    def checkFreeTurn(self, child): # TODO Selesaikan argumen if-else
        if True: # posisi awal di lubang kecil yang ada bijinya
            child_data = []
            possible_child = len(child_data)
            childFreeTurn = True
        elif True: # posisi awal di lubang besar milik pribadi
            possible_child, child_data = self.checkLegalMoves(child)
            if possible_child == 0:
                childFreeTurn = False
            else:
                childFreeTurn = True
        else: # posisi awal di lubang yang mengakhiri giliran
            child_data = []
            possible_child = len(child_data)
            childFreeTurn = False
        
        return childFreeTurn, possible_child, child_data

    def heuristicNode(self, node):
        pass
    
    def minimax(self, node, depth, maximizingPlayer, freeTurn, freeTurnData):
        if depth == 0: # TODO Definisikan node akhir itu seperti apa: kalau semua lumbung kecil tidak ada biji
            return self.heuristicNode(node), [None] # the heuristic value of node
        
        if maximizingPlayer:
            bestValue = None
            bestDirection = []

            if freeTurn:
                possible_child, node_data = freeTurnData[0], freeTurnData[1]
            else:
                possible_child, node_data = self.checkLegalMoves(node)
                if possible_child == 0:
                    isMax = False
                    childFreeTurn = False
                    child_data = []
                    child_possibilities = len(child_data)
                    val, direction = minimax(node, depth, isMax, childFreeTurn, [child_possibilities, child_data])
                    bestValue = val
                    bestDirection += direction

            for i in range(possible_child): # each child of node
                child = node.copy()
                # TODO implementation of child node here
                childFreeTurn, child_possibilities, child_data = self.checkFreeTurn(child)
                
                if childFreeTurn: # here is a small change
                    isMax = True
                else:
                    isMax = False
                
                val, direction = minimax(child, depth - 1, isMax, childFreeTurn, [child_possibilities, child_data])

                if bestValue is None:
                    bestValue = val
                    bestDirection = bestDirection + ["Direction ke anak ini"] + direction
                else:
                    if val > bestValue:
                        del bestDirection[:]
                        bestDirection = bestDirection + ["Direction ke anak ini"] + direction
                    
                    bestValue = max(bestValue, val)
            
            return bestValue, bestDirection
        else:
            bestValue = None
            bestDirection = []
            
            if freeTurn:
                possible_child, node_data = freeTurnData[0], freeTurnData[1]
            else:
                possible_child, node_data = self.checkLegalMoves(node)
                if possible_child == 0:
                    isMax = True
                    childFreeTurn = False
                    child_data = []
                    child_possibilities = len(child_data)
                    val, direction = minimax(node, depth, isMax, childFreeTurn, [child_possibilities, child_data])
                    bestValue = val
                    bestDirection += direction

            for i in range(possible_child): # each child of node
                # do implementation of child node here
                child = node.copy()
                childFreeTurn, child_possibilities, child_data = self.checkFreeTurn(child)

                if childFreeTurn: # here is a small change
                    isMax = False
                else:
                    isMax = True
                
                val, direction = minimax(child, depth - 1, isMax, childFreeTurn, [child_possibilities, child_data])

                if bestValue is None:
                    bestValue = val
                    bestDirection = bestDirection + ["Direction ke anak ini"] + direction
                else:
                    if val < bestValue:
                        del bestDirection[:]
                        bestDirection = bestDirection + ["Direction ke anak ini"] + direction
                
                    bestValue = min(bestValue, val)
            
            return bestValue, bestDirection