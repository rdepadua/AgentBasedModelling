import random
import rastergrid
import matplotlib

#Creating class called Agent
class Agent:
     
        #Adding self instances using the __init__ constructor
        def __init__(self, ia, environment, agents):
            self.id = ia
            self.x = random.randint(0,299)
            self.y = random.randint(0,299)
            self.environment = environment
            self.agents = agents
            self.store = 0 
            
            
        # def __str__(self):
        #     #This shows what the id returns (x value, y value and "store" value)
        #     return "id=" + str(self.id) + ", x=" + str(self.x) + ", y=" + str(self.y) + ", storage=" + str(self.store) 
   
        #create method called move where agents randomly move         
        def move(self):  
            """
            Moves agent using random library. If random number is greater than 0.5 then 
            it moves + 1 in x and y direction, if less than 0.5 agent move -1 in x and 
            y direction

            Returns
            -------
            Agent movement +/- 1

            """               
            if random.random() < 0.5:
                self.x = (self.x + 1) %300
            else: 
                self.x = (self.x - 1) %300
        
            if random.random() < 0.5:
                self.y = (self.y + 1) %300
            else:
                self.y = (self.y - 1) %300
        
        #create method eat where agents eat the environment with conditions of minimum amount of the environment 
        #that could be eaten, how much is being eaten and how much is stored within the agents 
        def eat(self):
            """
            Calculate how much environment can be eaten and how much environment is taken 
            away and how much is stored within the agents

            Returns
            -------
            Reduction from environment
            Adding storage within agents
            """
            if self.environment[self.y][self.x] > 50:
               self.environment[self.y][self.x] -= 75
               self.store += 1
            # else:
            #    print("id=" + str(self.id) + " No more grass to eat") # if environment is less than 75, 
                                                                        # print which agent encountered
            # check storage of agents
            # print("id=" + str(self.id) + ", x=" + str(self.x) + ", y=" + str(self.y) + ", store=" + str(self.store))  
            
           # Agent returning some of its store to the environment if it has more than 100
           # if self.store > 100:
           #    self.environment[self.y][self.x] += 25
           #     self.store = 75
                

            
        def share(self, neighbourhood):
            """
            Calculating how much "environment" is shared but depending if agents 
            are in the same neighbourhood. Also ensures that an agent cannot share with 
            itself 

            Parameters
            ----------
            neighbourhood : defined distance of what constitutes as a neighbourhood
                

            Returns
            -------
            Float 
            Amount of what is shared between agents that are in the same neighbourhood

            """
            #print(len(self.agents))
            #if distance between 2 agents is within neighbourhood then share
            for agent in self.agents:
                distance = self.distance_between(agent)
                if agent.id != self.id:                                    
                    
                    
                    if distance < neighbourhood:
                        average = (agent.store + self.store) /2
                        self.store = average
                        agent.store = average
                        #print(True)
                        #print("sharing " + str(distance) + " " +str(average))
                        #print(neighbourhood)
                      #  print(self.id, agent)
                     #   print("id=" + str(self.id) + ", x=" + str(self.x) + ", y=" + str(self.y) + ", store=" + str(self.store)) 
                    # else:
                    #     print(False)
                        
                        
                        
        def distance_between(self, agent):
            """
            Calculating distance between self and agent

            Parameters
            ----------
            agent : Agent
                One agent
                

            Returns
            -------
            Float
                Distance between the two agents

            """
            return (((self.x - agent.x)**2) +
            ((self.y - agent.y)**2))**0.5
        
    
        #def birth(self):
              #if self.store >= 500:
                 #self.store -= 500
                 
                 
        def get_store(self):
            print("id=" + str(self.id) + ", x=" + str(self.x) + ", y=" + str(self.y) + ", store=" + str(self.store))
            
             
                
