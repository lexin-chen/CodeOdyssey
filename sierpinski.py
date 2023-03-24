# Lexin Chen
# IAE 101
# Fall 2020
# Project 2 - Sierpinski Triangle

import pygame

# This is a list of predefined pygame Color objects
colors = [pygame.Color(0, 0, 0, 255),       # Black
          pygame.Color(255, 0, 0, 255),     # Red
          pygame.Color(0, 255, 0, 255),     # Green
          pygame.Color(0, 0, 255, 255),     # Blue
          pygame.Color(255, 255, 255, 255)] # White

# Each of these constants is the index to the corresponding pygame Color object
# in the list, colors, defined above.
BLACK = 0
RED = 1
GREEN = 2
BLUE = 3
WHITE = -1

# This function draws a triangle using the polygon function from pygames draw
# module.
# p1 - is the coordinates of the first vertext of the triangle
# p2 - is the coordinates of the second vertex of the triangle
# p3 - is the coordinates of the third vertex of the triangle
# All coordinates are given as a list of two floats, [x, y] that specify a
# position on the pygame screen.
# color - is an integer constant used to index into the colors list to select a
# pygame Color object to assign a color to this triangle.
# line_width - is an integer that determines the thickness of the lines used to
# draw the triangle. The larger the integer the thicker the line.
# If line-width is set to 0, then pygame will fill the triangle in with the 
# chosen color.
# screen - This variables stores a reference to the pygame screen object upon
# which the program will draw.
# This function has no return value.
def draw_triangle(p1, p2, p3, color, line_width, screen):
    # Study the documentation of the pygame draw module to see how this works.
    pygame.draw.polygon(screen, colors[color], [p1, p2, p3], line_width)
    # The flip() function causes the drawn image to appear on the screen.
    pygame.display.flip()

# THIS FUNCTION MUST BE COMPLETED BY THE STUDENT.
# This function returns a point that lies at the midpoint between the input
# points.
# p1 - the coordinates of the first point
# p2 - the coordinates of the second point
# Each point is a list of two floats, [x, y]
# The function should return coordinates--a list of two floats--that locate the
# point that is midway between p1 and p2.
def find_midpoint(p1, p2):
    mid = []
    mid.append((p1[0] + p2[0]) / 2)
    mid.append((p1[1] + p2[1]) / 2)
    return mid

# THIS FUNCTION MUST BE COMPLETED BY THE STUDENT
# This function draw a tringle, and then recursively calls it self to ensure
# that three smaller triangles are drawn within the new triangle, as described
# by the Sierpinski Triangle algorithm.
# degree - This describes the depth of recursion remaining--how many more levels
# of triangles are going to be drawn in this image.
# p1 - the coordinates of the first vertex of the new triangle
# p2 - the coordinates of the second vertex of the new triangle
# p3 - the coordinates of the third vertex of the new triangle
# color - the color of the new triangle
# line_width - The width of the line used to draw the triangle.
# screen - The pygame surface upon which the Sierpinski triangle will be drawn
def sierpinski(degree, p1, p2, p3, color, line_width, screen):
    line_width = 3
    m1 = find_midpoint (p1, p2)
    m2 = find_midpoint (p2, p3)
    m3 = find_midpoint (p3, p1)
    draw_triangle(p1, p2, p3, color, line_width, screen)
    if degree > 0:
        sierpinski(degree -1, p1, m1, m3, color, line_width, screen)
        sierpinski(degree -1, m1, p2, m2, color, line_width, screen)
        sierpinski(degree -1, m3, m2, p3, color, line_width, screen)

def main():
    # This call is necessary to initialize the resources in the pygame library.
    pygame.init()

    width = 640 # The size of the drawing surface in the horizontal dimension (y)
    height = 640 # The size of the drawing surface in the vertical dimension (x)
    # The size value is used by pygame to create the surface; it is a list of 
    # the values for the width and the height (in that order).
    size = [width, height] 

    # These coordinates identify the vertices of the first, outermost triangle.
    # They are set to center the triangle in the drawing surface, and set 5
    # pixels from the borders on each side.
    p1 = [5, height - 5]
    p2 = [(width - 10) / 2, 5]
    p3 = [width - 5, height - 5]
    initial_color = BLACK # The initial color assigned to the triangle.
    initial_line_width = 1 # The initial line_width assigned to the triangle.
                           # Set to 1 to tell pygame to draw the triangle with
                           # the thinnest possible line and leave the triangle
                           # unfilled.

    degree = 5 # The degree of the Sierpinski triangle. This indicates how many
               # levels of recursion to go down while drawing the triangle.
    
    # Sets a caption describing the contents of the drawing surface in the title
    # bar.
    pygame.display.set_caption("Sierpinski Triangle")
    
    # Creates the drawing surface of the specified size. A reference to that
    # surface is stored in the variable screen
    screen = pygame.display.set_mode(size)
    
    # Colors the background of the drawing surface white.
    screen.fill(WHITE)
    pygame.display.flip()
    
    # Initial call to the recursive function. This will draw the first,
    # outermost triangle (the degree 0 triangle).
    sierpinski(degree, p1, p2, p3, initial_color, initial_line_width, screen)

    # DON'T CHANGE THE CODE HERE
    # DON'T TOUCH THIS LOOP
    done = False
    count = 0
    while not done:
        count = count + 1
        if count % 1000000 == 0:
            print(".", end = "")
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True

    print("\nNow Quitting")
    pygame.quit()
    # DON'T CHANGE THE CODE HERE
    
# DON'T CHANGE THIS EITHER
if __name__ == "__main__":
    main()
