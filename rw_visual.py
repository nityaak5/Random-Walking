import matplotlib.pyplot as plt
from random_walk import RandomWalk

while True:
    rw= RandomWalk(50000)
    rw.fill_walk()
    plt.style.use('seaborn')
    fig, ax= plt.subplots(figsize=(15,9))
    point_numbers= range(rw.num_points)
    ax.scatter(rw.x_values, rw.y_values,s=1, c=point_numbers, cmap=plt.cm.Blues, edgecolors='none')
    
# first and last point
    ax.scatter(0,0,c='green',edgecolors='none',s=90)
    ax.scatter(rw.x_values[-1], rw.y_values[-1], c='red',edgecolors='none',s=90)
# removing axis
    ax.get_xaxis().set_visible(False)
    ax.get_yaxis().set_visible(False)
    
    plt.show()

    keep_running= input("Another walk?(y/n)")
    if keep_running == 'n':
        break
        
