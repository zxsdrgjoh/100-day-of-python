
#challenges in
#https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Hurdle%204&url=worlds%2Ftutorial_en%2Fhurdle4.json
def turn_right():
     turn_left()
     turn_left()
     turn_left()
while not at_goal():
    if wall_in_front() and wall_on_right():
        turn_left()       
    if right_is_clear():
        turn_right()
        move()
        turn_right()
    if front_is_clear():
        move()
    



#Maze 
def turn_right():
     turn_left()
     turn_left()
     turn_left()
while not at_goal():
     if front_is_clear():
          move()
     if wall_in_front() and wall_on_right():
          turn_left() 
     if right_is_clear():
           turn_right()