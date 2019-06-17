# Load up the package numpy and make it so you 
# can access it using the label np
import numpy as np
# Since scipy is a pretty large package you want to only
# grab the signal functionality of it and access it using the
# the name sig
import scipy.signal as sig
# Get the pyplot functionality from matplotlib and access it using 
# the name plt
import matplotlib.pyplot as plt

# when you get the plot running, do
# print(plt.style.available) and pick a style you think
# is interesting. your choice
print(plt.style.available)
# Select what you want things within the window to look like
# I'm super super cool and edgy so I choose the dark side
plt.style.use('dark_background')

# This changes the length of the line in the first plot
Tx = np.linspace(0,0.22,5)
# This seems to be an iterator that gets iterated
# at the end of the for loop
i = 0
# Here be a for loop with its weird not c like syntax
for T in Tx:
    # set num to be an array using numpy and populate that array
    # with the expression that is given in the brackets
    num = np.array([10-10*np.exp(-T)])
    # den to be an array using numpy and populate that array
    # with the expression that is given in the brackets
    den = np.array([1, 10-11*np.exp(-T)])

    # set dtf to be a line that gets made using the two expression given
    # in the lines above
    dtf = sig.dlti(num,den)
    # this defines the timestep used in the graphs
    t,y = sig.dstep((dtf),n=1000)

    # define tCirc as a line that creates a circle
    tCirc = np.linspace(0,2*np.pi,100)
    # create the x components of the circle
    xCirc = np.cos(tCirc)
    # create the y components of the circle
    yCirc = np.sin(tCirc)

    # poleLocation is being assigned to the roots of the 
    # equation that was defined for den
    poleLocation = np.roots(den)
    # Set colorIndicator to be blue
    colorIndicator = "b"
    # Set markerIndicator to be the letter o
    markerIndicator = "o"

    # if the absolute value of poleLocation is gregater than 1 ...
    if np.abs(poleLocation)>1:
        # set colorIndicator to be red
        colorIndicator = "r"
        # set the marker indicator to be x
        markerIndicator = "x"
    # print to the console the text pole location 
    # and then the poleLocation
    print("pole location",poleLocation)

    # PYTHON ALLOWS MULTIPLE RETURNS!?!??!
    # set f and xarr to be 2 separate subplots that can
    # be defined later
    f,xarr = plt.subplots(2)

    # setting the title of subplot index 0
    xarr[0].set_title("T = %s"%T)
    # plotting t in subplot 0
    xarr[0].plot(t,y[:][0])
    # plotting the o marker in color green at coordinates 1, 0
    xarr[1].plot(1,0,c="g",marker="o")
    # plotting a circle in subplot 1
    xarr[1].plot(xCirc,yCirc)
    # make a scatter plot using poleLocation and use the color and marker
    # indicators as defined above
    xarr[1].scatter(poleLocation,0,c=colorIndicator, marker=markerIndicator)
    # Set a label for the x axis
    xarr[1].set_xlabel("pole magnitude is %s"%poleLocation)
    # set the bounds for the graphs x axis
    xarr[1].set_xlim([-2,2])

    # when you think you're ready to make the GIF, 
    # uncomment this line
    # plt.savefig('animation%s.png'%i)
    plt.show()
# iterate by 1
i+=1