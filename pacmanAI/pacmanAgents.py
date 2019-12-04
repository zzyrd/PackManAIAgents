# pacmanAgents.py
# ---------------
# Licensing Information:  You are free to use or extend these projects for
# educational purposes provided that (1) you do not distribute or publish
# solutions, (2) you retain this notice, and (3) you provide clear
# attribution to UC Berkeley, including a link to http://ai.berkeley.edu.
#
# Attribution Information: The Pacman AI projects were developed at UC Berkeley.
# The core projects and autograders were primarily created by John DeNero
# (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# Student side autograding was added by Brad Miller, Nick Hay, and
# Pieter Abbeel (pabbeel@cs.berkeley.edu).


from pacman import Directions
from game import Agent
from heuristics import *
import random
import heapq
import math
import sys

class RandomAgent(Agent):
    # Initialization Function: Called one time when the game starts
    def registerInitialState(self, state):
        return;

    # GetAction Function: Called with every frame
    def getAction(self, state):
        # get all legal actions for pacman
        actions = state.getLegalPacmanActions()
        # returns random action from all the valide actions
        return actions[random.randint(0,len(actions)-1)]

class OneStepLookAheadAgent(Agent):
    # Initialization Function: Called one time when the game starts
    def registerInitialState(self, state):
        return;

    # GetAction Function: Called with every frame
    def getAction(self, state):
        # get all legal actions for pacman
        legal = state.getLegalPacmanActions()
        # get all the successor state for these actions
        successors = [(state.generatePacmanSuccessor(action), action) for action in legal]
        # evaluate the successor states using scoreEvaluation heuristic
        scored = [(admissibleHeuristic(state), action) for state, action in successors]
        # get best choice
        bestScore = min(scored)[0]
        # get all actions that lead to the highest score
        bestActions = [pair[1] for pair in scored if pair[0] == bestScore]
        # return random action from the list of the best actions
        return random.choice(bestActions)

class BFSAgent(Agent):
    # Initialization Function: Called one time when the game starts
    def registerInitialState(self, state):
        return;

    # GetAction Function: Called with every frame
    def getAction(self, state):
        # TODO: write BFS Algorithm instead of returning Directions.STOP

        # We don't need visited set to track of all states we generated since all generated states are different.
        # keep track of (state, action, depth) in queue, (cost, action) in leaves
        # Create queue, put all legal moves to the queue based on current state
        queue = []
        while queue:

            # pop the first element of queue
            # check if terminal state, if yes, return
            # get action based on current state
            # state checking if reaches to leaf node, save it as later use
            # put new state back to queue
        leaves.sort()
        return leaves

class DFSAgent(Agent):
    # Initialization Function: Called one time when the game starts
    def registerInitialState(self, state):
        return;

    # GetAction Function: Called with every frame
    def getAction(self, state):
        # TODO: write DFS Algorithm instead of returning Directions.STOP
        # Unlike BFS, we use stack to implement DFS.
        # keep track of (state, action, depth) in stack
        stack = []
        leaves = []
        while stack:
            # pop the last element of stack
            # check if terminal state, if yes, return
            # get action based on current state
            # state checking if reaches to leaf node, save it as later use
            # put new state back to stack
        leaves.sort()
        return leaves

class AStarAgent(Agent):
    # Initialization Function: Called one time when the game starts
    def registerInitialState(self, state):
        return;

    # GetAction Function: Called with every frame
    def getAction(self, state):
        # TODO: write A* Algorithm instead of returning Directions.STOP
        # f(n) = g(n) + h(n):  f is total cost, g is depth, h is heuristic
        # use minheap to implement Priority Queue, sorted by cost, which is depth + heuristic()
        # keep track of (depth + heuristic(), state, action) in PQ
        PQ = []
        leaves = []
        while PQ:
            # pop the min state out of PQ
            # check if terminal state, if yes, return
            # get action based on current state
            # state checking if reaches to leaf node, save it as later use
            # put new state back to PQ
        leaves.sort()
        return leaves


class HillClimberAgent(Agent):
    # Initialization Function: Called one time when the game starts
    def registerInitialState(self, state):
        self.SIZE = 5
        return
    # GetAction Function: Called with every frame
    def getAction(self, state):
        # check if state is a terminal state

        # get all possible actions for our action list
        posisbleMove = state.getAllPossibleActions()
        actions = allpossibleMoves

        while True:
            # create a new sequence for later comparison use.  # 50/50 chance to change the action
            new sequence = []
            # search state by using sequence of actions and store it in the state_list as we climb the hill
            List_state = [startState]
            # loop through all action 
            for action in new sequence:
                # check for terminal state, if not reached, add current state to state_list

            # compare the last reached state with our startstate, and know its evaluation
            v = gameEvaluation(startState, state_list[-1])
            # after searching, if we have higher evaluation, that means this sequence is a better sequence
 
            # reached the limit, return the first action of current best sequence.
            return best action

class GeneticAgent(Agent):
    # Initialization Function: Called one time when the game starts
    def registerInitialState(self, state):
        self.P_SIZE = 8
        self.C_SIZE = 5
    # GetAction Function: Called with every frame
    def getAction(self, state):
        # check if state is a terminal state
        # initalize population: action is gene, 5 actions form a chromosome

        # compute fitness on each gene in each chromosome in the initial randomized popuplation
        fit = fitness of first population

        while True:
            # select parents based on fit evaluation

            # reproduce next generation
            # do mutation on new generation if random test result is less (or equal) to 10%
    
            # compute fit on new generation, and loop again to find the next gen based on current one

        return best population

    def fit(self):
        return

    def select(self):
        return

    def reproduce(self):
        return

class TreeNode:
    pass


class MCTSAgent(Agent):
    # Initialization Function: Called one time when the game starts
    def registerInitialState(self, state):
        return;
    # GetAction Function: Called with every frame
    def getAction(self, state):
        # check if state is a terminal state
        root = TreeNode()

        while True:
            # Tree Policy part: selection and expansion
            self.select()
            self.expand()
            # Default Policy part: do simulation on new added node
            self.rollout()
            # Backpropagation part: update reward, visited_times to all nodes along the path from current to root
            self.backpropagation()
        # return the action associated with the most visited node (Break ties randomly).

        return best child acation

    def select(self):
        return

    def expand(self):
        return

    # simulation
    def rollout(self):
        return

    # backpropagation
    def backpropagation(self):
        return
                


