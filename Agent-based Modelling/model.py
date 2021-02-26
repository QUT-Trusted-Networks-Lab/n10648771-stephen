from importagent import *
from mesa import Agent, Model
from mesa.time import RandomActivation
import random
%matplotlib inline
# The below is needed for both notebooks and scripts
import matplotlib.pyplot as plt
import numpy as np
from mesa.space import MultiGrid
import networkx as nx
from mesa.space import NetworkGrid
import time, enum, math
from mesa.datacollection import DataCollector
from mesa import Agent, Model
from mesa.time import RandomActivation
import random
%matplotlib inline
# The below is needed for both notebooks and scripts
import matplotlib.pyplot as plt
import numpy as np
from mesa.space import MultiGrid
import networkx as nx
from mesa.space import NetworkGrid
import time, enum, math
from mesa.datacollection import DataCollector
from model import *




class NetworkInfectionModel(Model):
    """A model for infection spread."""

    def __init__(self, N=10, pcontact=0.4, ptrans=0.5, avg_node_degree=3,
                 progression_period=3, progression_sd=2, recovery_rate=0.0193, recovery_days=1/0.0193,
                 recovery_sd=7, incubation_time = 6 , incubation_time_sd = 2, rate_infected = 1/6):
        #My shit here:
        self.num_nodes = N  
        self.pcontact=pcontact
        n = 100
        self.A_prob = np.random.rand(N,N)
        self.A = (self.A_prob<pcontact).astype('int')
        #----------------------------#
        #           Myshit
        #
        #----------------------------#
        
        
        
        
        #self.num_nodes = N  
        #self.pcontact=pcontact
        """All parameters"""
        prob = avg_node_degree / self.num_nodes

        self.initial_outbreak_size = 1
        self.incubation_time = incubation_time
        self.incubation_time_sd = incubation_time_sd
        self.rate_infected = rate_infected
        self.recovery_sd = recovery_sd
        self.ptrans = ptrans
        self.recovery_rate = recovery_rate
        self.recovery_days = recovery_days
        self.G = nx.Graph(self.A)
        self.grid = NetworkGrid(self.G)

        self.schedule = RandomActivation(self) #activate the step of Agents in random orders
        self.running = True
        #self.dead_agents = []
        """2 types of agents: intra-agent and out-agent"""
        
        # Create out_agents: 
        
        # Create intra-agents
        for i, node in enumerate(self.G.nodes()):
            a = CovidAgent(i+1, self)
            self.G.add_node(a)
            #add agent
            self.grid.place_agent(a, node)
            self.A_prob = np.random.rand(N+i,N+i)
            self.A = (self.A_prob<pcontact).astype('int')
            #make some agents infected at start
            infected = np.random.choice([0,1], p=[0.99,0.01])
            if infected == 1:
                a.state = State.INFECTED
                a.recovery_time = self.get_recovery_time()

        self.datacollector = DataCollector(            
            agent_reporters={"State": 'state'})

    def get_recovery_time(self):
        return int(self.random.normalvariate(self.recovery_days,self.recovery_sd))

    def step(self):
        self.datacollector.collect(self)
        self.schedule.step()