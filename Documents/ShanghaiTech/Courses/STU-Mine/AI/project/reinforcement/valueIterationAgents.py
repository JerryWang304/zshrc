# valueIterationAgents.py
# -----------------------
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


# valueIterationAgents.py
# -----------------------
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


import mdp, util

from learningAgents import ValueEstimationAgent
import collections

class ValueIterationAgent(ValueEstimationAgent):
    """
        * Please read learningAgents.py before reading this.*

        A ValueIterationAgent takes a Markov decision process
        (see mdp.py) on initialization and runs value iteration
        for a given number of iterations using the supplied
        discount factor.
    """
    def __init__(self, mdp, discount = 0.9, iterations = 100):
        """
          Your value iteration agent should take an mdp on
          construction, run the indicated number of iterations
          and then act according to the resulting policy.

          Some useful mdp methods you will use:
              mdp.getStates()
              mdp.getPossibleActions(state)
              mdp.getTransitionStatesAndProbs(state, action)
              mdp.getReward(state, action, nextState)
              mdp.isTerminal(state)
        """
        self.mdp = mdp
        self.discount = discount
        self.iterations = iterations
        self.values = util.Counter() # A Counter is a dict with default 0
        self.runValueIteration()

    def runValueIteration(self):
        # Write value iteration code here
        "*** YOUR CODE HERE ***"
        for k in range(self.iterations):
            temp = util.Counter()
            for state in self.mdp.getStates():
                if self.mdp.isTerminal(state):
                    temp[state] = 0 # termial state
                    continue
                # find the max value 
                MAX = float("-inf")
                for action in self.mdp.getPossibleActions(state):
                    q = self.computeQValueFromValues(state, action)
                    if q > MAX:
                        MAX = q
                temp[state] = MAX
            self.values = temp 

    def getValue(self, state):
        """
          Return the value of the state (computed in __init__).
        """
        return self.values[state]


    def computeQValueFromValues(self, state, action):
        """
          Compute the Q-value of action in state from the
          value function stored in self.values.
        """
        "*** YOUR CODE HERE ***"
        transitions = self.mdp.getTransitionStatesAndProbs(state, action)
        ret = 0
        # sumation
        for next_state, p in transitions:
            reward = self.mdp.getReward(state, action, next_state)
            ret += p*(reward +self.discount*self.values[next_state])
        return ret 

    def computeActionFromValues(self, state):
        """
          The policy is the best action in the given state
          according to the values currently stored in self.values.

          You may break ties any way you see fit.  Note that if
          there are no legal actions, which is the case at the
          terminal state, you should return None.
        """
        "*** YOUR CODE HERE ***"
        # values are numbers in 
        #print "values = "
        #print self.values
        # where are actions  ... 
        ret = None
        actions = self.mdp.getPossibleActions(state)
        # if len(actions) <= 0:
        #     return ret 
        if self.mdp.isTerminal(state):
            return None
        MAX = float("-inf")
        # Wrong !   if  MAX = 1e-9  !!!! 
        for action in actions:
            v = self.getQValue(state,action)
            #print "v = ", v
            if MAX < v:
                MAX = v
                ret = action 
        # print action
        return ret 

    def getPolicy(self, state):
        return self.computeActionFromValues(state)

    def getAction(self, state):
        "Returns the policy at the state (no exploration)."
        return self.computeActionFromValues(state)

    def getQValue(self, state, action):
        return self.computeQValueFromValues(state, action)

class AsynchronousValueIterationAgent(ValueIterationAgent):
    """
        * Please read learningAgents.py before reading this.*

        An AsynchronousValueIterationAgent takes a Markov decision process
        (see mdp.py) on initialization and runs cyclic value iteration
        for a given number of iterations using the supplied
        discount factor.
    """
    def __init__(self, mdp, discount = 0.9, iterations = 1000):
        """
          Your cyclic value iteration agent should take an mdp on
          construction, run the indicated number of iterations,
          and then act according to the resulting policy. Each iteration
          updates the value of only one state, which cycles through
          the states list. If the chosen state is terminal, nothing
          happens in that iteration.

          Some useful mdp methods you will use:
              mdp.getStates()
              mdp.getPossibleActions(state)
              mdp.getTransitionStatesAndProbs(state, action)
              mdp.getReward(state)
              mdp.isTerminal(state)
        """
        ValueIterationAgent.__init__(self, mdp, discount, iterations)

    def runValueIteration(self):

        num = len(self.mdp.getStates())

        for k in range(self.iterations):
            temp = self.values 
            index = 0 
            # update only one state 
            state = self.mdp.getStates()[k%num]
            if self.mdp.isTerminal(state):
                temp[state] = 0 # termial state
            else:
                # if not terminal then update it as before 
                MAX = float("-inf")
                for action in self.mdp.getPossibleActions(state):
                    q = self.computeQValueFromValues(state, action)
                    if q > MAX:
                        MAX = q
                temp[state] = MAX

            self.values = temp 

class PrioritizedSweepingValueIterationAgent(AsynchronousValueIterationAgent):
    """
        * Please read learningAgents.py before reading this.*

        A PrioritizedSweepingValueIterationAgent takes a Markov decision process
        (see mdp.py) on initialization and runs prioritized sweeping value iteration
        for a given number of iterations using the supplied parameters.
    """
    def __init__(self, mdp, discount = 0.9, iterations = 100, theta = 1e-5):
        """
          Your prioritized sweeping value iteration agent should take an mdp on
          construction, run the indicated number of iterations,
          and then act according to the resulting policy.
        """
        self.theta = theta
        ValueIterationAgent.__init__(self, mdp, discount, iterations)
    
    def getMaxQValue(self, state):
        max_q_value = float('-inf')
        # valus = []
        # print "state = ", state
        actions = self.mdp.getPossibleActions(state)
        for action in actions:
            v = self.getQValue(state, action)
            if max_q_value < v:
                max_q_value = v
        return max_q_value

    def runValueIteration(self):
        "*** YOUR CODE HERE ***"
        queue = util.PriorityQueue()
        states = self.mdp.getStates()

        predecessors = {}
        # initial predecessors for each state
        for s in states:
            predecessors[s] = set()

        for state in states:
            # predecessors[state] = set()
            if self.mdp.isTerminal(state):
                continue 
            else:
                actions = self.mdp.getPossibleActions(state)
                # find adjacent states
                for action in actions:
                    for next_state, p in self.mdp.getTransitionStatesAndProbs(state,action):
                    # if p< 0:    print "next_state" 
                        if p > 0:
                            predecessors[next_state].add(state) 
                # the highest Q-value across all possible actions from state
                # print "state = ", state
                max_q_value = self.getMaxQValue(state)
                #max(self.getQValue(state, action) for action in actions)
                diff = abs(max_q_value-self.values[state])
                queue.push(state, -diff)
        # iterations
        for k in range(self.iterations):
            if queue.isEmpty():
                break
            s = queue.pop()
            if not self.mdp.isTerminal(s):
                # print "s = ",s
                self.values[s] = self.getMaxQValue(s)
                #max(self.getQValue(s, action) for action in self.mdp.getPossibleActions(s))
                # each predecessors
            for pre_state in predecessors[s]:
                max_q_value = self.getMaxQValue(pre_state)
                # max_q_value = max([self.getQValue(next_state, action) for action in self.mdp.getPossibleActions(next_state)])
                diff = abs(self.values[pre_state] -  max_q_value)
                if diff > self.theta:
                    # wrong: queue.add(pre_state, -diff)
                    queue.update(pre_state, -diff)
