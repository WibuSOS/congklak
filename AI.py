from copy import deepcopy
from math import inf as infinity

class AI_Minimax:
    depth = int()
    maximizingPlayer = bool()
    expandedNode = 0
    pruning = bool()
    
    def __init__(self, depth, maximizingPlayer=True, pruning=False):
        self.depth = depth
        self.maximizingPlayer = maximizingPlayer
        self.pruning = pruning

    def checkLegalMoves(self, node, maximizingPlayer):
        node_data = []
        
        if maximizingPlayer:
            index_hole = 1
            while index_hole < 8: # to sum up small holes
                if node[index_hole][1] > 0:
                    node_data.append(index_hole)
                index_hole += 1
        else:
            index_hole = 9
            while index_hole <= 15: # to sum up small holes
                if node[index_hole][1] > 0:
                    node_data.append(index_hole)
                index_hole += 1
        
        return len(node_data), node_data
    
    def checkFreeTurn(self, child, lastIndex, maximizingPlayer):
        if lastIndex == 0 or lastIndex == 8: # posisi awal di lubang besar milik pribadi
            possible_child, child_data = self.checkLegalMoves(child, maximizingPlayer)
            if possible_child == 0:
                childFreeTurn = False
            else:
                childFreeTurn = True
        elif child[lastIndex][1] - 1 > 0: # posisi awal di lubang kecil yang ada bijinya
            child_data = [lastIndex]
            possible_child = len(child_data)
            childFreeTurn = True
        elif child[lastIndex][1] - 1 <= 0: # posisi awal di lubang kecil yang mengakhiri giliran
            child_data = []
            possible_child = len(child_data)
            childFreeTurn = False
        
        return childFreeTurn, possible_child, child_data

    def terminalCheck(self, depth, node):
        small_holes = 0 # total number of shells in all small holes
        index_hole = 0

        while index_hole <= 15: # to sum up small holes
            if index_hole == 0 or index_hole == 8:
                pass
            else:
                small_holes += node[index_hole][1]
            index_hole += 1
        
        if depth == 0 or small_holes == 0:
            return True
        else:
            return False
    
    def heuristicNode(self, node, maximizingPlayer):
        if maximizingPlayer:
            return node[0][1]
        else:
            return -node[8][1]
    
    def commitMove(self, node):
        print("AI thinking...")
        childFreeTurn = False
        child_data = []
        child_possibilities = len(child_data)
        bestValue, bestDirection = self.minimax(node, self.depth, self.maximizingPlayer, childFreeTurn, [child_possibilities, child_data])
        print("commitMove:", bestValue, bestDirection)
        return bestDirection.pop(0)
    
    def getExpandedNode(self):
        return self.expandedNode
    
    def debugPrint(self, maximizingPlayer, depth):
        if maximizingPlayer:
            print("P1 turn")
        else:
            print("P2 turn")
        print("Depth:", depth, "\n")
        print("Expanded node:", self.expandedNode)
    
    def minimax(self, node, depth, maximizingPlayer, freeTurn, freeTurnData, alpha=-infinity, beta=infinity):
        self.expandedNode += 1
        self.debugPrint(maximizingPlayer, depth)
        if self.terminalCheck(depth, node):
            return self.heuristicNode(node, self.maximizingPlayer), [None] # the heuristic value of node
        
        if maximizingPlayer:
            bestValue = -infinity
            bestDirection = []

            if freeTurn:
                possible_child, node_data = freeTurnData[0], freeTurnData[1]
            else:
                possible_child, node_data = self.checkLegalMoves(node, maximizingPlayer)
                if possible_child == 0:
                    isMax = False
                    childFreeTurn = False
                    child_data = []
                    child_possibilities = len(child_data)
                    if self.pruning:
                        val, direction = self.minimax(node, depth, isMax, childFreeTurn, [child_possibilities, child_data], alpha, beta)
                    else:
                        val, direction = self.minimax(node, depth, isMax, childFreeTurn, [child_possibilities, child_data])
                    bestValue = val
                    bestDirection += direction
            
            for index in range(possible_child): # each child of node
                child = deepcopy(node)
                lastIndex = node_data[index]
                hand = child[lastIndex][1]
                child[lastIndex][1] = 0
                
                while hand > 0: # to spread the shells in hand until none left
                    lastIndex += 1
                    if lastIndex > 15:
                        lastIndex = 0
                    
                    # to check if the current index is at enemy's home index
                    if lastIndex == 8:
                        continue
                    
                    if hand == 1 and 0 < lastIndex < 8 and child[lastIndex][1] == 0:
                        child[0][1] = child[0][1] + hand + child[-abs(lastIndex)][1]
                        hand = 0
                        child[lastIndex][1] = 0
                        child[-abs(lastIndex)][1] = 0
                        continue

                    child[lastIndex][1] += 1
                    hand -= 1
                
                childFreeTurn, child_possibilities, child_data = self.checkFreeTurn(child, lastIndex, maximizingPlayer)
                
                if childFreeTurn: # here is a small change
                    isMax = True
                else:
                    isMax = False
                
                if self.pruning:
                    val, direction = self.minimax(child, depth - 1, isMax, childFreeTurn, [child_possibilities, child_data], alpha, beta)
                else:
                    val, direction = self.minimax(child, depth - 1, isMax, childFreeTurn, [child_possibilities, child_data])
                
                if val > bestValue:
                    del bestDirection[:]
                    bestDirection = bestDirection + [node_data[index]] + direction
                
                bestValue = max(bestValue, val)
                if self.pruning:
                    alpha = max(alpha, bestValue)
                    if beta <= alpha:
                        break
            
            return bestValue, bestDirection
        else:
            bestValue = infinity
            bestDirection = []
            
            if freeTurn:
                possible_child, node_data = freeTurnData[0], freeTurnData[1]
            else:
                possible_child, node_data = self.checkLegalMoves(node, maximizingPlayer)
                if possible_child == 0:
                    isMax = True
                    childFreeTurn = False
                    child_data = []
                    child_possibilities = len(child_data)
                    if self.pruning:
                        val, direction = self.minimax(node, depth, isMax, childFreeTurn, [child_possibilities, child_data], alpha, beta)
                    else:
                        val, direction = self.minimax(node, depth, isMax, childFreeTurn, [child_possibilities, child_data])
                    bestValue = val
                    bestDirection += direction
            
            for index in range(possible_child): # each child of node
                child = deepcopy(node)
                lastIndex = node_data[index]
                hand = child[lastIndex][1]
                child[lastIndex][1] = 0

                while hand > 0: # to spread the shells in hand until none left
                    lastIndex += 1
                    if lastIndex > 15:
                        lastIndex = 0
                    
                    # to check if the current index is at enemy's home index
                    if lastIndex == 0:
                        continue
                    
                    if hand == 1 and 8 < lastIndex <= 15 and child[lastIndex][1] == 0:
                        child[8][1] = child[8][1] + hand + child[len(child) - lastIndex][1]
                        hand = 0
                        child[lastIndex][1] = 0
                        child[len(child) - lastIndex][1] = 0
                        continue

                    child[lastIndex][1] += 1
                    hand -= 1
                
                childFreeTurn, child_possibilities, child_data = self.checkFreeTurn(child, lastIndex, maximizingPlayer)
                
                if childFreeTurn: # here is a small change
                    isMax = False
                else:
                    isMax = True
                if self.pruning:
                    val, direction = self.minimax(child, depth - 1, isMax, childFreeTurn, [child_possibilities, child_data], alpha, beta)
                else:
                    val, direction = self.minimax(child, depth - 1, isMax, childFreeTurn, [child_possibilities, child_data])
                
                if val < bestValue:
                    del bestDirection[:]
                    bestDirection = bestDirection + [node_data[index]] + direction
                
                bestValue = min(bestValue, val)
                if self.pruning:
                    beta = min(beta, bestValue)
                    if beta <= alpha:
                        break
            
            return bestValue, bestDirection

class AI_Negamax(AI_Minimax):
    player = int()

    def __init__(self, depth, player=1, pruning=False):
        self.player = player
        if player == 1:
            maximizingPlayer = True
        elif player == -1:
            maximizingPlayer = False
        super().__init__(depth, maximizingPlayer=maximizingPlayer, pruning=pruning)
    
    def commitMove(self, node):
        print("AI thinking...")
        childFreeTurn = False
        child_data = []
        child_possibilities = len(child_data)
        bestValue, bestDirection = self.negamax(node, self.depth, self.player, childFreeTurn, [child_possibilities, child_data])
        print("commitMove:", bestValue, bestDirection)
        return bestDirection.pop(0)
    
    def heuristicNode(self, node, maximizingPlayer):
        if maximizingPlayer:
            return node[0][1]
        else:
            return node[8][1]
    
    def negamax(self, node, depth, player, freeTurn, freeTurnData, α=-infinity, β=infinity):
        if player == 1:
            maximizingPlayer = True
        elif player == -1:
            maximizingPlayer = False
        
        self.expandedNode += 1
        self.debugPrint(maximizingPlayer, depth)
        if self.terminalCheck(depth, node):
            return player * self.heuristicNode(node, self.maximizingPlayer), [None] # the heuristic value of node
        
        bestValue = -infinity
        bestDirection = []
        # child = orderMoves(childNodes)
        
        if freeTurn:
                possible_child, node_data = freeTurnData[0], freeTurnData[1]
        else:
            possible_child, node_data = self.checkLegalMoves(node, maximizingPlayer)
            if possible_child == 0:
                childFreeTurn = False
                child_data = []
                child_possibilities = len(child_data)
                if self.pruning:
                    value, direction = self.negamax(node, depth, -player, childFreeTurn, [child_possibilities, child_data], -α, -β)
                else:
                    value, direction = self.negamax(node, depth, -player, childFreeTurn, [child_possibilities, child_data])
                bestValue = -value
                bestDirection += direction
        
        for index in range(possible_child):
            child = deepcopy(node)
            lastIndex = node_data[index]
            hand = child[lastIndex][1]
            child[lastIndex][1] = 0

            while hand > 0: # to spread the shells in hand until none left
                lastIndex += 1
                if lastIndex > 15:
                    lastIndex = 0
                
                if maximizingPlayer:
                    if lastIndex == 8: # to check if the current index is at enemy's home index
                        continue
                    
                    if hand == 1 and 0 < lastIndex < 8 and child[lastIndex][1] == 0:
                        child[0][1] = child[0][1] + hand + child[-abs(lastIndex)][1]
                        hand = 0
                        child[lastIndex][1] = 0
                        child[-abs(lastIndex)][1] = 0
                        continue
                else:
                    if lastIndex == 0: # to check if the current index is at enemy's home index
                        continue

                    if hand == 1 and 8 < lastIndex <= 15 and child[lastIndex][1] == 0:
                        child[8][1] = child[8][1] + hand + child[len(child) - lastIndex][1]
                        hand = 0
                        child[lastIndex][1] = 0
                        child[len(child) - lastIndex][1] = 0
                        continue
                
                child[lastIndex][1] += 1
                hand -= 1
            
            childFreeTurn, child_possibilities, child_data = self.checkFreeTurn(child, lastIndex, maximizingPlayer)

            if childFreeTurn: # here is a small change
                if self.pruning:
                    value, direction = self.negamax(child, depth - 1, player, childFreeTurn, [child_possibilities, child_data], α, β)
                else:
                    value, direction = self.negamax(child, depth - 1, player, childFreeTurn, [child_possibilities, child_data])
            else:
                if self.pruning:
                    value, direction = self.negamax(child, depth - 1, -player, childFreeTurn, [child_possibilities, child_data], -α, -β)
                else:
                    value, direction = self.negamax(child, depth - 1, -player, childFreeTurn, [child_possibilities, child_data])
                value = -value
            
            if value > bestValue:
                del bestDirection[:]
                bestDirection = bestDirection + [node_data[index]] + direction
            
            bestValue = max(bestValue, value)
            if self.pruning:
                α = max(α, bestValue)
                if α >= β:
                    break # (* cut-off *)
        
        return bestValue, bestDirection
