#################################################################
#  CSE 231 Project 4
#
#  Functions
#    Defines functions for 5 different shapes
#    Creates 4 flags using mentioned shapes
#    Asks for a selection
#       If selection is invalid, asks for selection again
#       If selection is valid, runs the corresponding function
#    When finished, can input 'Q' to quit the program
#################################################################

#Import
import turtle

#Input
FLAG = '''
Select one of the following options:
    TUN: Tunisia
    LBY: Libya
    TUR: Turkey
    SGP: Singapore
    ALL: All flags
    Q: Quit
'''

#Rectangle Function
def rectangle(x,y,length,height,color): #Defines function 'rectangle'
    location = (x,y) #Sets location equal to first 2 given variables
    turtle.goto(location) #Goes to location specified above
    turtle.color(color) #Changes fill color to specified color above
    turtle.down() #Puts the pen down
    turtle.pencolor('black') #Changes pen color to black (Outline color)
    turtle.begin_fill() #Begins fill so created rectangle will be filled
    for r in range(2): #Starts a for loop to execute 2 times
        turtle.forward(length) #Moves turtle forward the length specified above
        turtle.left(90) #Turns turtle to left 90 degrees
        turtle.forward(height) #Moves turtle forward the height specified above
        turtle.left(90) #Turns turtle to left 90 degrees again
    turtle.end_fill() #Ends the fill
    turtle.up() #Lifts the pen up

#Circle Function
def circle(x,y,radius,color): #Defines function 'circle'
    location = (x,y) #Sets location equal to first 2 given variables
    turtle.goto(location) #Goes to location specificed above
    turtle.color(color) #Changes fill color to specified color above
    turtle.down() #Puts the pen down
    turtle.begin_fill() #Begins fill so created circle will be filled
    turtle.circle(radius) #Creates a circle with radius specified above
    turtle.end_fill() #Ends the fill
    turtle.up() #Lifts the pen up

#Crescent Function
def crescent(x1,y1,x2,y2,R1,R2,color1,color2): #Defines function 'crescent'
    c1_location = (x1,y1) #Creates variable for location of first circle
    c2_location = (x2,y2) #Creates variable for location of second circle
    turtle.goto(c1_location) #Moves turtle to location for first circle
    turtle.color(color1) #Changes fill color to color for first circle
    turtle.down() #Puts the pen down
    turtle.begin_fill() #Begins fill so created circle will be filled
    turtle.circle(R1) #Creates first circle with the specified radius
    turtle.end_fill() #Ends the fill
    turtle.up() #Lifts the pen up
    turtle.goto(c2_location) #Moves turtle to location for second circle
    turtle.color(color2) #Changes fill color to color for second circle
    turtle.down() #Puts the pen down again
    turtle.begin_fill() #Begins fill so created circle will be filled
    turtle.circle(R2) #Creates second circle with specified radius
    turtle.end_fill() #Ends the fill
    turtle.up() #Lifts pen up

#Star Function
def star(x,y,size,color,theta): #Defines function 'star'
    location = (x,y) #Sets location equal to first 2 given variables
    turtle.up() #Lifts the pen up
    turtle.goto(location) #Goes to location specified above
    turtle.color(color) #Changes fill color to specified color above
    turtle.down() #Puts the pen down
    turtle.begin_fill() #Begins fill so created star will be filled
    turtle.right(200) #Changes starting direction of turtle
    for s in range(5): #Starts a for loop to execute 5 times
        turtle.forward(size) #Moves turtle forward specified amount
        turtle.right(theta) #Turns turtle to the right by specified amount
        turtle.forward(size) #Moves turtle forward again
        turtle.right(72 - theta) #Turns turtle to the right by half the amount
    turtle.end_fill() #Ends the fill
    turtle.up() #Lifts the pen up
    
#Multi_Star Function
def multi_star(x,y,size,color): #Defines function 'multi_star'
    A = 240 #Sets A equal to 240
    location = (x,y) #Sets location equal to first 2 given variables
    turtle.goto(location) #Goes to location specified above
    turtle.color(color) #Changes fill color to color specified above
    turtle.down() #Puts pen down
    turtle.begin_fill() #Begins fill so created stars will be filled
    turtle.right(90) #Turns turtle to right 90 degrees
    star(x+(A/3),y+(A/2)+(A/4)+(A/16),size,color,144) #Creates a star
    turtle.right(90) #Turns turtle to right 90 degrees
    star(x+(A/3)+(A/40),y+(A/2)+(A/6),size,color,144) #Creates a star
    turtle.right(90) #Turns turtle to right 90 degrees
    star(x+(A/3)+(A/6),y+(A/2)+(A/8),size,color,144) #Creates a star
    turtle.right(90) #Turns turtle to right 90 degrees
    star(x+(A/3)+(A/4),y+(A/2)+(A/4),size,color,144) #Creates a star
    turtle.right(90) #Turns turtle to right 90 degrees
    star(x+(A/3)+(A/7),y+(A/2)+((A*2)/5.5),size,color,144) #Creates a star
    turtle.end_fill() #Ends the fill
    turtle.up() #Lifts pen up

#Tunisian Flag Function
def Tun_flag(x,y,height): #Defines function 'Tun_flag'
    A = height #Sets A equal to the height
    rectangle(x,y,A*1.5,height,'red') #Creates the base of the flag
    circle(x+((1.5*A)/2),y+(A/4),A/4,'white') #Creates white circle in middle
    crescent(x+((1.5*A)/2),y+((A/4)+(A/16)),x+(((1.5*A)/2)+(A/20)),\
             y+((A/4)+(A/16)+(A/32)),((3*A)/8)/2,((3*A)/10)/2,'red','white')
             #Creates a crescent in center of flag
    star(x+(((1.5*A)/2)+(A/40)),y+((A/2)-(A/40)),((9*A)/40)/3,'red',144)
             #Creats a star a little to the right of center

#Libya Flag Function
def Lby_flag(x,y,height): #Defines function 'Lby_flag'
    A = height #Sets A equal to the height
    rectangle(x,y,1.5*A,A/4,'green') #Creates the bottom base of the flag
    rectangle(x,y+(A/4),1.5*A,A/2,'black') #Creates the middle base of the flag
    rectangle(x,y+((A*3)/4),1.5*A,A/4,'red') #Creates the top base of the flag
    crescent(x+((1.5*A)/2),y+((A/4)+(A/8)),x+(((1.5*A)/2)+(A/24)),\
             y+((A/4)+(A/8)+(A/32)),(A/4)/2,(A/5)/2,'white','black')
             #Creates a crescent in the center of the flag
    star(x+((1.5*A)+(A/8)-((A*1.5)/2)),y+((A/4)+((2*A)/8)),(A/8)/3,'white',144)
    #Creates a star to the right of the crescent

#Turkey Flag Function
def Tur_flag(x,y,height): #Defines function 'Tur_flag'
    A = height #Sets A equal to the height
    rectangle(x,y,1.5*A,height,'red') #Creates the base of the flag
    rectangle(x,y,A/30,height,'white') #Creates the flag pole on left of flag
    crescent(x+(A/2),y+(A/4),x+((A/2)+(A/16)),y+((A/4)+(A/20)),(A/2)/2,\
             ((2*A)/5)/2,'white','red') #Creates the crescent in center of flag
    star(x+(((2*A)/3)+(A/8)),y+(A/2),(A/4)/3,'white',144)
    #Creates a white star to the right of the crescent
    
#Singapore Flag Function
def Sgp_flag(x,y,height): #Defines function 'Sgp_flag'
    A = height #Sets A equal to the height
    rectangle(x,y,1.5*A,A/2,'white') #Creates the lower base of the flag
    rectangle(x,y+(A/2),1.5*A,A/2,'red') #Creates the upper base of the flag
    crescent(x+(A/3),y+((A/2)+(A/16)),x+((A/3)+(A/10)),y+((A/2)+(A/16)),\
             ((10*A)/27)/2,((2*A)/5)/2,'white','red') #Creates crescent
    multi_star(x,y,((4*A)/45)/3,'white') #Creates 5 stars to left of crescent
    

#Main While Loop
while True:
    selection = input(FLAG).upper() #Asks for user input
    
    if selection == 'Q': #If user inputs 'Q'
        print('Bye') #Tells the user bye
        break #Breaks the while loop
    
    if selection == 'TUN': #If user inputs 'TUN'
        turtle.reset() #Clears previous drawing
        turtle.speed(100) #Sets draw speed to 100
        Tun_flag(0,0,240) #Draws Tunisian Flag
        turtle.hideturtle() #Hides turtle after finishing flag
        
    if selection == 'LBY': #If user inputs 'LBY'
        turtle.reset() #Clears previous drawing
        turtle.speed(100) #Sets draw speed to 100
        Lby_flag(0,0,240) #Draws Libya flag
        turtle.hideturtle() #Hides turtle after finishing flag
        
    if selection == 'TUR': #If user inputs 'TUR'
        turtle.reset() #Clears previous drawing
        turtle.speed(100) #Sets draw speed to 100
        Tur_flag(0,0,240) #Draws Turkey flag
        turtle.hideturtle() #Hides turtle after finishing flag
        
    if selection == 'SGP': #If user inputs 'SGP'
        turtle.reset() #Clears previous drawing
        turtle.speed(100) #Sets draw speed to 100
        Sgp_flag(0,0,240) #Draws Singapore flag
        turtle.hideturtle() #Hides turtle after finishing flag
        
    if selection == 'ALL': #If user inputs 'ALL'
        turtle.reset() #Clears previous drawing
        turtle.speed(100) #Sets draw speed to 100
        Tur_flag(50,50,240) #Draws Turkey flag
        
        turtle.speed(100) #Sets draw speed to 100
        turtle.home() #Sets turtle back to initial position
        Sgp_flag(50,-250,240) #Draws Singapore flag
        
        turtle.speed(100)#Sets draw speed to 100
        turtle.home() #Sets turtle back to inital position
        Lby_flag(-400,-250,240) #Draws Libya flag
        
        turtle.speed(100) #Sets draw speed to 100
        turtle.home() #Sets turtle back to inital position
        Tun_flag(-400,50,240) #Draws Turkey flag
        turtle.hideturtle() #Hides turtle after drawing all 4 flags
        
    else: #If user doesn't input a valid input
        print('Please choose a valid input.') #Asks user to choose valid input
        continue #Continues while loop back to the top

turtle.exitonclick() #Closes turtle window when red 'x' at top right is clicked
turtle.bye() #Closes turtle window