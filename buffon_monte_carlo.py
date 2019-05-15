# buffon monte carlo simulation
# simulation of buffon's needle to estimate the value of pi

# imports
import matplotlib.pyplot as plt
import numpy as np
import random as rd
import pandas as pd

# sample size

sample_size = 10000

# initializing plot
fig = plt.figure(figsize=[9, 9])

fig.suptitle('Buffon\'s Needle Simulation with {} samples'.format(sample_size))

fig.subplots_adjust(hspace=.4)

# plotting needles on the board

board = fig.add_subplot(1, 1, 1)

# defining the dataframe

needles = pd.DataFrame({'x_point':[],'y_point':[],'x_end_point':[],'y_end_point':[],'crossed_line':[]})

# generating some needles

for n in range(0,sample_size):
    # establishing the first point and the angle

    x = rd.randrange(1000,4000)/1000
    y = rd.randrange(1000, 4000) / 1000
    theta = rd.randrange(0,360000) / 1000

    # defining end point

    x_end = x + np.sin(np.rad2deg(theta))
    y_end = y + np.cos(np.rad2deg(theta))

    board.plot([x, x_end], [y, y_end])

    # checking if it crossed a yard line
    if abs(int(x)-int(x_end))==1:
        crossed = True
    else:
        crossed = False

    new_needle = [x,y,x_end,y_end,crossed]

    needles.loc[n]=new_needle

# saving the dataframe

needles.to_csv('buffons_needle_sim.csv')

# adding yard lines

yard_lines = [[[1,1],[0,5]],[[2,2],[0,5]],[[3,3],[0,5]],[[4,4],[0,5]]]

for n in range(0,4):
    board.plot(yard_lines[n][0],yard_lines[n][1],'k--')

# calculating pi

crossed_count = len(needles[needles['crossed_line']==True])

pi_est = (2*sample_size)/crossed_count

diff=pi_est-np.pi

text = 'Estimated value of pi: {}, Actual Value of pi: {}, Diff ={}'.format(pi_est, np.pi, diff)
fig.text(.01, .9, text)

# calling the plot
plt.show()
