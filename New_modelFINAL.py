import random
import operator
import tkinter
import matplotlib
matplotlib.use('TkAgg') 
import matplotlib.pyplot
import agentframework
import rastergrid
import csv
import matplotlib.animation

import requests
import bs4

r = requests.get('http://www.geog.leeds.ac.uk/courses/computing/practicals/python/agent-framework/part9/data.html')
content = r.text
soup = bs4.BeautifulSoup(content, 'html.parser')
td_ys = soup.find_all(attrs={"class" : "y"})
td_xs = soup.find_all(attrs={"class" : "x"})
print(td_ys)
print(td_xs) 

# for popup window
#%matplotlib qt
#to move inline in the Plots
#%matplotlib inline

# Use %gui tk on IPython Console as there is an error with picking Tkinter 
# as the Graphic backend - PROBLEM RESOLVED
#%gui tk


# random.seed(1)

num_of_agents = 10
num_of_iterations = 5
neighbourhood = 20
#reading raster grid python file
environment = rastergrid.readEnvironment()
agents = []

#figure size
fig = matplotlib.pyplot.figure(figsize=(7, 7))
#ax = fig.add_axes([0, 0, 1, 1])

#ax.set_autoscale_on(False)

#Trying to use random shuffle
#random.shuffle(agents, num_of_iterations)



# Make the agents depending on how many chosen.
for i in range(num_of_agents):
    y = int(td_ys[i].text)
    x = int(td_xs[i].text)
    agents.append(agentframework.Agent(environment, agents, y, x))
    
# for i in range(num_of_agents):
#     print(agents[i])
    
 
    def update (frame_number):
        fig.clear()
            
        # Move the agents.
        for j in range(num_of_iterations):
            #print(j)
            for i in range(num_of_agents):
                agents[i].move()
        #Make agents eat the environment that is passed through from agentframework
                agents[i].eat()
                agents[i].share(neighbourhood)
                #agents[i].birth()
                agents[i].get_store()
    
            
            for i in range(num_of_agents):
                   matplotlib.pyplot.scatter(agents[i].x,agents[i].y, c='white', s=20)
                   matplotlib.pyplot.imshow(environment)                    
                   # matplotlib.pyplot.show()

#animate the model with certain parameters chosen like how many frames is run (num_of_iterations)
def run():
    animation = matplotlib.animation.FuncAnimation(fig, update, repeat=False, frames=num_of_iterations)
    canvas.draw()    

# create Tk root widget, with "Model" as title 
root = tkinter.Tk()
root.wm_title("Model")
canvas = matplotlib.backends.backend_tkagg.FigureCanvasTkAgg(fig, master=root)
canvas._tkcanvas.pack(side=tkinter.TOP, fill=tkinter.BOTH, expand=1) 

# Menu components
menu_bar = tkinter.Menu(root)
root.config(menu=menu_bar)
model_menu = tkinter.Menu(menu_bar)
menu_bar.add_cascade(label="Model", menu=model_menu)
model_menu.add_command(label="Run model", command=run)

# Run 
tkinter.mainloop() 

# matplotlib.pyplot.xlim(0,300)
# matplotlib.pyplot.ylim(0,300)
# for i in range(num_of_agents):
#     matplotlib.pyplot.scatter(agents[i].x,agents[i].y)
#     matplotlib.pyplot.imshow(environment) 
# matplotlib.pyplot.show()
    
#for agents_row_a in agents:
    #for agents_row_b in agents:
        #distance = distance_between(agents_row_a, agents_row_b) 