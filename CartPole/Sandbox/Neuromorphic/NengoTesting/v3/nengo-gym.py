#
# The following code liberally taken from the OpenAI gym/examples/random_agent.py source
#

import argparse
import logging
import sys
import random

import numpy as np
import nengo

import gymnasium as gym
from gymnasium import wrappers


#************** Agent Classes *****************


class NengoAgent(object):
    """The world's simplest agent!"""
    def __init__(self, action_space):
        self.action_space = action_space

    def act(self, observation, reward, done):
        return self.action_space.sample()


class NengoGymCartPole(object):
      
    def __init__(self):
        #super(NengoGymCartPole, self).__init__(self.step)
        #self.name = name
        print("Gym Init")        
        
        self.feedback = []
        self.controls = []
        # self.size_in = size_in
        # self.size_out = size_out
        
        self.env = gym.make("CartPole-v1", render_mode="human")
        
        print("Action Space:")
        print(self.env.action_space)
     
        
        print("Observation Space:")
        print(self.env.observation_space)
        print(self.env.observation_space.high)
        print(self.env.observation_space.low)
        
        
        self.reward = 0
        self.total_reward = 0
        self.steps = 0
        # self.output = []
        self.state, _ = self.env.reset()


    #handles the environment state and possible reward value passed back
    #reinforce heuristics based on reward     
    def handle_input(values):
        return 0 #nothing for now


    def handle_output(self):
        return 0 #nothing for now
        
    # def heuristic(self,state):
    #     action = 0
    #     #PID controller for trajectory optimizatio
    #     #Engine control based on Pontryagin's maximum principle (full thrust on/off)
        
    #     angle_targ = state[0]*0.5 + state[2]*1.0         # angle should point towards center (state[0] is horizontal coordinate, state[2] hor speed)
    #     if angle_targ >  0.4: angle_targ =  0.4  # more than 0.4 radians (22 degrees) is bad
    #     if angle_targ < -0.4: angle_targ = -0.4
    #     hover_targ = 0.55*np.abs(state[0])           # target y should be proporional to horizontal offset
    
    #     # PID controller: state[4] angle, state[5] angularSpeed
    #     angle_todo = (angle_targ - state[4])*0.5 - (state[5])*1.0
    #     #print("angle_targ=%0.2f, angle_todo=%0.2f" % (angle_targ, angle_todo))
    
    #     # PID controller: state[1] vertical coordinate state[3] vertical speed
    #     hover_todo = (hover_targ - state[1])*0.5 - (state[3])*0.5
    #     #print("hover_targ=%0.2f, hover_todo=%0.2f" % (hover_targ, hover_todo))
    
    #     if state[6] or state[7]: # legs have contact
    #         angle_todo = 0
    #         hover_todo = -(state[3])*0.5  # override to reduce fall speed, that's all we need after contact
        
    #     if hover_todo > np.abs(angle_todo) and hover_todo > 0.05: action = 2
    #     elif angle_todo < -0.05: action = 3
    #     elif angle_todo > +0.05: action = 1

    #     return action
        
    def __call__(self, t, controls):
        #pre-processing sensor/feedback data        
        #self.handle_input( values )
        # print("Node _Call_")  
        
        #send next action event to the environment, receive feedback:
        #state [vector] : of agent object in the environment (position, condition, etc)
        #reward [scalar] : scalar feedback on meeting defined goal/error conditions
        #done [bool] : if environment is finished running
        #info [str] : debug info
        
        #action = self.heuristic(self.state) #static thrust for now
        action = np.argmax(controls)

        self.state, self.reward, done, _, _ = self.env.step(action) #
        #wait(200)
        #env.step(action) 

        self.env.render() #one frame
        
        #tally reward for epoch updates
        self.total_reward += self.reward
        #total_reward += 1
    
        
        #newstate[4] = newstate[4]/6
        #newstate[5] = newstate[5]/6        
        
        #preliminary reward function logging
        # if self.steps % 20 == 0 or done:
        #     print(["{:+0.2f}".format(x) for x in self.state])
        #     print("step {} total_reward {:+0.2f}".format(self.steps, self.total_reward))
        # 
         #preliminary reward function logging
        if self.steps % 20 == 0 or done:
            print(["{:+0.2f}".format(x) for x in self.state])
            print("step {} total_reward {:+0.2f}".format(self.steps, self.total_reward))       
        #increment counter for learning rate
        self.steps += 1
        
        #check to see if we have crashed, landed, etc
        if done:
            #env.render(close=True)
            #raise Exception("Simulation done")
            self.steps = 0
            self.state = self.env.reset()
            self.total_reward = 0
        

        
        return self.state
        

class NengoGymNode(nengo.Node):       

    def __init__(self, **kwargs):
        self.env = NengoGymCartPole(**kwargs)
        
        def func(t, x):
            return self.env.step(x[0])
        
        super(NengoGymNode, self).__init__(size_in=1, size_out=1)


def heuristic(observation):
    TTHRESH = .25
    if abs(observation[2]) < TTHRESH:
        parameters = np.array([\
                [ 0, 0, -.3, -1],
                [ 0, 0, .3, 1]
                ])
    else:
        parameters = np.array([\
                [ 0, 0, -1, -.3],
                [ 0, 0, 1, .3]
                ])
    actions = np.zeros(2) 
    actions[0] = np.matmul(parameters[0], observation)
    actions[1] = np.matmul(parameters[1], observation)
    return actions

# def decision(observation):
#     TTHRESH = .03
#     if abs(observation[2]) < TTHRESH:
#         action = 0 if observation[3] < 0 else 1
#     else:
#         action = 0 if observation[2] < 0 else 1
#     return np.array([1, -1]) if action == 0 else np.array([-1, 1])
#     # return action

model = nengo.Network()
with model:
 
   #pid = PIDNode(dimensions=1)
    environment = NengoGymCartPole()

    env = nengo.Node(environment, size_in=2, size_out=4)
    #correction = nengo.Node(None, size_in=1, size_out=4)
   
    sensors = nengo.Ensemble(n_neurons=500, dimensions=4)                       
    #sensors = nengo.Ensemble(n_neurons=500, dimensions=4)
    controls = nengo.Ensemble(n_neurons=500, dimensions=2,  neuron_type=nengo.Direct())
    
    nengo.Connection(env, sensors, synapse=None)
    nengo.Connection(sensors, controls, function=heuristic, synapse=0.02)
    nengo.Connection(controls, env, synapse=None)
    #nengo.Connection(correction, env)
    
    manual = nengo.Node(0)
    #nengo.Connection(manual,env)
    

sim = nengo.Simulator(model)
sim.run(5)