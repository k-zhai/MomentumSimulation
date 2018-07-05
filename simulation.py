#Kevin Zhai

from visual import *
from math import *

#1. One-dimensional elastic collision with masses and initial velocities as given inputs (you should be able to vary these as directed)
#2. One-dimensional completely inelastic collision with masses and initial velocities as given inputs.
#3. Two-dimensional elastic collision with one object initially stationary with masses and initial velocity as given input.
#4. Two-dimensional elastic collision with both objects initially moving with masses and initial velocities as given input.

frame = box(position=vector(0,0,0), size=(40,40,0))

#Asks for user input
userinput = raw_input("Choose scenario (1,2,3): ")

#Case 1
if userinput == "1":

    #Assigning values to variables
    print "Mass 1 starts at 10 m; mass 2 starts at -10 m"
    velocity1 = raw_input("What is the initial velocity (m/s) of mass 1?")
    velocity2 = raw_input("What is the initial velocity (m/s) of mass 2?")
    v1initial = int(velocity1)
    v2initial = int(velocity2)

    object1 = sphere(pos=(10,0,0), color=color.red)
    object1.m = raw_input("What is mass 1 (kg)?")
    object1.p = int(object1.m) * vector(int(velocity1),0,0)

    object2 = sphere(pos=(-10,0,0), color=color.blue)
    object2.m = raw_input("What is mass 2 (kg)?")
    object2.p = int(object2.m) * vector(int(velocity2),0,0)

    interval = 0.01

    totalp = float(object1.m) * int(velocity1) + int(object2.m) * int(velocity2)

    t = 0

    #Indicates when collision occurs
    indicator = 0 
    TRAIL = True
    TRAIL_COUNT = 10000

    #Updates position every 0.01 s
    while indicator == 0 and t < 10000000:
        rate(100)
        object1.pos = object1.pos + (object1.p / float(object1.m)) * interval
        object2.pos = object2.pos + (object2.p / float(object2.m)) * interval
        #When direction changes
        if float(object1.x) <= float(object2.x) + 1:
            indicator = 1
            velocity1f = float((totalp - float(object2.m) * (float(velocity1) - float(velocity2))) / (float(object1.m) + float(object2.m)))
            velocity2f = float(v1initial + velocity1f - v2initial)
            break
        
    #Final momentum
    object1.p = float(object1.m) * vector(float(velocity1f),0,0)
    object2.p = float(object2.m) * vector(float(velocity2f),0,0)

    print "Final velocity of mass 1: ", velocity1f, " m/s", "\n", "Final velocity of mass 2: ", velocity2f, " m/s"

    #Motion when direction changes
    while indicator == 1 and t < 10:
        rate(100)
        object1.pos = object1.pos + (object1.p / float(object1.m)) * interval
        object2.pos = object2.pos + (object2.p / float(object2.m)) * interval
        t = t + interval

#Case 2
elif userinput == "2":

    #Assigning values to variables
    print "Mass 1 starts at 10 m; mass 2 starts at -10 m"
    velocity1 = raw_input("What is the initial velocity (m/s) of mass 1?")
    velocity2 = raw_input("What is the initial velocity (m/s) of mass 2?")
    
    object1 = sphere(pos=(10,0,0), color=color.red)
    object1.m = raw_input("What is mass 1 (kg)?")
    object1.p = float(object1.m) * vector(float(velocity1),0,0)

    object2 = sphere(pos=(-10,0,0), color=color.blue)
    object2.m = raw_input("What is mass 2 (kg)?")
    object2.p = float(object2.m) * vector(float(velocity2),0,0)

    interval = 0.01

    totalp = float(object1.m) * float(velocity1) + float(object2.m) * float(velocity2)

    vf = float(totalp / (float(object1.m) + float(object2.m)))

    print "Final velocity: ", vf, " m/s"

    t = 0
    indicator = 0
    TRAIL = True
    TRAIL_COUNT = 10000

    #Defines motion of objects before collision
    while indicator == 0 and t < 10000000:
        rate(100)
        object1.pos = object1.pos + (object1.p / float(object1.m)) * interval
        object2.pos = object2.pos + (object2.p / float(object2.m)) * interval
        if float(object1.x) <= float(object2.x) + 1:
            indicator = 1
            break
    #Defines motion of objects after collision
    while indicator == 1 and t < 10:
        rate(100)
        object1.pos = object1.pos + vector(vf,0,0) * interval
        object2.pos = object2.pos + vector(vf,0,0) * interval
        t = t + interval

#Case 3
elif userinput == "3":

    #Defines properties of objects including momentum, mass, etc. 
    print "Mass 1 starts at -10 m; mass 2 starts at 10 m"
    velocity1 = raw_input("What is the initial velocity (m/s) of mass 1?")
    
    object1 = sphere(pos=(-10,0,0), color=color.red)
    object1.m = raw_input("What is mass 1 (kg)?")
    object1.p = float(object1.m) * vector(float(velocity1),0,0)
    
    object2 = sphere(pos=(10,0,0), color=color.blue)
    object2.m = raw_input("What is mass 2 (kg)?")

    totalp = float(object1.m) * float(velocity1)

    theta = raw_input("What is the final angle (degrees) for mass 1?")

    #Constants used to solve quadratic
    constant1 = (float(object1.m) * float(object2.m) + float(object1.m) ** 2) / float(object2.m)
    constant2 = -1 * (2 * float(object1.m) ** 2 * float(velocity1) * cos(float(theta) * pi / 180)) / float(object2.m)
    constant3 = -1 * float(object1.m) * (float(velocity1) ** 2 - float(object1.m) * float(velocity1) ** 2 / float(object2.m))

    object1.vf = ((-1) * constant2 + sqrt(constant2 ** 2 - 4 * constant1 * constant3)) / (2 * constant1)
    object2.vf = sqrt((float(object1.m) * float(velocity1) ** 2 - float(object1.m) * object1.vf ** 2) / float(object2.m))

    #In degrees 
    phi = asin(float(object1.m) * object1.vf * sin(float(theta) * pi / 180) / (float(object2.m) * object2.vf)) * 180 / pi
    
    print "Final angle (degrees) for mass 2: ", phi

    object1.vfx = object1.vf * cos(float(theta) * pi / 180)
    print "x component final velocity (m/s) of mass 1: ", object1.vfx
    object1.vfy = object1.vf * sin(float(theta) * pi / 180)
    print "y component final velocity (m/s) of mass 1: ", object1.vfy
    object2.vfx = object2.vf * cos(float(360 - phi) * pi / 180)
    print "x component final velocity (m/s) of mass 2: ", object2.vfx
    object2.vfy = object2.vf * sin(float(360 - phi) * pi / 180)
    print "y component final velocity (m/s) of mass 2: ", object2.vfy

    interval = 0.01 

    #Indicates when collision occurs
    indicator = 0 
    TRAIL = True
    TRAIL_COUNT = 10000
    t = 0
    
    #Updates position every 0.01 s
    while indicator == 0 and t < 10000000:
        rate(100)
        object1.pos = object1.pos + (object1.p / float(object1.m)) * interval
        #When direction changes
        if float(object2.x) <= float(object1.x) + 1:
            indicator = 1
            break

    #Motion when direction changes
    while indicator == 1 and t < 10:
        rate(100)
        object1.pos = object1.pos + vector(object1.vfx,object1.vfy,0) * interval
        object2.pos = object2.pos + vector(object2.vfx,object2.vfy,0) * interval
        t = t + interval
