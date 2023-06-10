from turtle import Turtle, Screen




class Snake:
    def __init__(self):
        positions_list = [0, -20, -40]
        segments = []
        for x in range(0, 3):
            new_segment = Turtle()
            new_segment.penup()
            new_segment.color("white")
            new_segment.shape("square")
            new_segment.goto(positions_list[x], 0)
            segments.append(new_segment)

        self.snake_segments = segments
        self.head = segments[0]

    def move_snake(self):
        for seg_num in range(len(self.snake_segments) - 1, 0, -1):
            x_cor = self.snake_segments[seg_num - 1].xcor()
            y_cor = self.snake_segments[seg_num - 1].ycor()
            self.snake_segments[seg_num].goto(x_cor, y_cor)

        self.head.forward(20)

    def add_seg(self):
        seg = Turtle()
        seg.penup()
        seg.color("white")
        seg.shape("square")

        self.snake_segments.append(seg)











