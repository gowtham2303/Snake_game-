from turtle import Turtle 

STANDARD_POSITIONS =[(0,0) ,(-20,0),(-40,0)]
MOVEMENT =20

class Snake ():
    
    def __init__(self) :
        self.segmemts=[]
        self.create_snake()
        self.head = self.segmemts[0]

    def create_snake(self):
        for position in STANDARD_POSITIONS:
            new_segment= Turtle("square")
            new_segment.color("white")
            new_segment.penup()
            new_segment.goto(position)
            self.segmemts.append(new_segment)
    
    def extend(self):
        new_segment= Turtle("square")
        new_segment.color("white")
        new_segment.penup()
        #self.segment[-1].position()
        xaxis = self.segmemts[len(self.segmemts)-1].xcor()
        yaxis = self.segmemts[len(self.segmemts)-1].ycor()
        new_segment.goto(xaxis, yaxis)
        self.segmemts.append(new_segment)

    def move (self):
        for seg in range((len(self.segmemts)-1) ,0 ,-1):
            xaxis= self.segmemts[seg-1].xcor()
            yaxis= self.segmemts[seg-1].ycor()
            self.segmemts[seg].goto(xaxis,yaxis)
        self.head.forward(MOVEMENT)
     
    def up (self):
        if self.head.heading() != 270 :
            self.head.setheading(90)

    def down (self):
        if self.head.heading() != 90:
            self.head.setheading(270)

    def left (self):
        if self.head.heading() != 0:
            self.head.setheading(180)

    def right (self):
        if self.head.heading() != 180:
             self.head.setheading(0)


        

        

          
     

         
         
        


 



