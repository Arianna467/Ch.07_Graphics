'''
PYCASSO PROJECT
---------------
Your job is to make a cool picture.
You must use multiple colors.
You must have a coherent picture. No abstract art with random shapes.
You must use multiple types of graphic functions (e.g. circles, rectangles, lines, etc.)
Somewhere you must include a WHILE or FOR loop to create a repeating pattern.
Do not just redraw the same thing in the same location 10 times. 
You can contain multiple drawing commands in a loop, so you can draw multiple train cars for example.
Please use comments and blank lines to make it easy to follow your program. 
If you have 5 lines that draw a robot, group them together with blank lines above and below. 
Then add a comment at the top telling the reader what you are drawing.
IN THE WINDOW TITLE PLEASE PUT YOUR NAME.
When you are finished Pull Request your file to your instructor.
'''

import arcade
arcade.open_window(500,500,"Arianna Lear")
arcade.set_background_color(arcade.color.TAN)
arcade.start_render()

#Leaf Pattern: Top
for i in range(75,450,85):
    arcade.draw_circle_filled(i,463,13.5,arcade.color.GUPPIE_GREEN)
for i in range(52,450,85):
    arcade.draw_arc_filled(i,450,50,50,arcade.color.GUPPIE_GREEN,1,60)
for i in range(52,450,85):
    arcade.draw_line(i,450,i+35,470,arcade.color.BLACK,1)
for i in range(75,450,85):
    arcade.draw_arc_outline(i,463,28,28,arcade.color.BLACK,1,190,3,300)
for i in range(51,450,85):
    arcade.draw_line(i,450,i+15,474,arcade.color.BLACK,2)
for i in range(51,450,85):
    arcade.draw_line(i,450,i+30.5,450,arcade.color.BLACK,2)

#Leaf Pattern: Bottom
for i in range(75,450,85):
    arcade.draw_circle_filled(i,75,13.5,arcade.color.GUPPIE_GREEN)
for i in range(52,450,85):
    arcade.draw_arc_filled(i,62.5,50,50,arcade.color.GUPPIE_GREEN,1,60)
for i in range(52,450,85):
    arcade.draw_line(i,62.5,i+35,80,arcade.color.BLACK,1)
for i in range(75,450,85):
    arcade.draw_arc_outline(i,75,28,28,arcade.color.BLACK,1,190,3,300)
for i in range(51,450,85):
    arcade.draw_line(i,62.5,i+15,86,arcade.color.BLACK,2)
for i in range(51,450,85):
    arcade.draw_line(i,62.5,i+30.5,62.5,arcade.color.BLACK,2)

#Base Green
arcade.draw_rectangle_filled(220,395,60,10,arcade.color.GUPPIE_GREEN)
arcade.draw_rectangle_filled(255,385,150,10,arcade.color.GUPPIE_GREEN)
arcade.draw_rectangle_filled(245,375,190,10,arcade.color.GUPPIE_GREEN)
arcade.draw_rectangle_filled(230,365,240,10,arcade.color.GUPPIE_GREEN)
arcade.draw_rectangle_filled(225,355,250,10,arcade.color.GUPPIE_GREEN)
arcade.draw_rectangle_filled(230,345,260,10,arcade.color.GUPPIE_GREEN)
arcade.draw_rectangle_filled(230,335,260,10,arcade.color.GUPPIE_GREEN)
arcade.draw_rectangle_filled(225,325,270,10,arcade.color.GUPPIE_GREEN)
arcade.draw_rectangle_filled(225,315,270,10,arcade.color.GUPPIE_GREEN)
arcade.draw_rectangle_filled(220,305,280,10,arcade.color.GUPPIE_GREEN)
arcade.draw_rectangle_filled(225,295,290,10,arcade.color.GUPPIE_GREEN)
arcade.draw_rectangle_filled(225,285,290,10,arcade.color.GUPPIE_GREEN)
arcade.draw_rectangle_filled(225,275,290,10,arcade.color.GUPPIE_GREEN)
arcade.draw_rectangle_filled(230,265,280,10,arcade.color.GUPPIE_GREEN)
arcade.draw_rectangle_filled(235,255,270,10,arcade.color.GUPPIE_GREEN)
arcade.draw_rectangle_filled(250,245,260,10,arcade.color.GUPPIE_GREEN)
arcade.draw_rectangle_filled(265,235,230,10,arcade.color.GUPPIE_GREEN)
arcade.draw_rectangle_filled(275,225,210,10,arcade.color.GUPPIE_GREEN)
arcade.draw_rectangle_filled(265,215,230,10,arcade.color.GUPPIE_GREEN)
arcade.draw_rectangle_filled(250,205,260,10,arcade.color.GUPPIE_GREEN)
arcade.draw_rectangle_filled(165,195,70,10,arcade.color.GUPPIE_GREEN)
arcade.draw_rectangle_filled(165,185,50,10,arcade.color.GUPPIE_GREEN)
arcade.draw_rectangle_filled(330,195,100,10,arcade.color.GUPPIE_GREEN)
arcade.draw_rectangle_filled(300,185,40,10,arcade.color.GUPPIE_GREEN)
arcade.draw_rectangle_filled(295,175,50,10,arcade.color.GUPPIE_GREEN)
arcade.draw_rectangle_filled(300,165,60,10,arcade.color.GUPPIE_GREEN)
arcade.draw_rectangle_filled(360,185,20,10,arcade.color.GUPPIE_GREEN)
arcade.draw_rectangle_filled(360,175,20,10,arcade.color.GUPPIE_GREEN)
arcade.draw_rectangle_filled(350,165,20,10,arcade.color.GUPPIE_GREEN)
arcade.draw_rectangle_filled(310,155,80,10,arcade.color.GUPPIE_GREEN)
arcade.draw_rectangle_filled(310,145,60,10,arcade.color.GUPPIE_GREEN)
arcade.draw_rectangle_filled(315,135,30,10,arcade.color.GUPPIE_GREEN)

#Rainbow Pattern
arcade.draw_rectangle_filled(285,345,30,10,arcade.color.PASTEL_RED)
arcade.draw_rectangle_filled(290,330,20,40,arcade.color.PASTEL_RED)
arcade.draw_rectangle_filled(280,310,20,20,arcade.color.PASTEL_RED)
arcade.draw_rectangle_filled(285,300,10,20,arcade.color.PASTEL_RED)
arcade.draw_rectangle_filled(325,315,10,50,arcade.color.PASTEL_ORANGE)
arcade.draw_rectangle_filled(335,310,10,40,arcade.color.PASTEL_ORANGE)
arcade.draw_rectangle_filled(345,310,10,20,arcade.color.PASTEL_ORANGE)
arcade.draw_rectangle_filled(365,280,10,20,arcade.color.DARK_PASTEL_BLUE)
arcade.draw_rectangle_filled(355,275,10,10,arcade.color.DARK_PASTEL_BLUE)

#Medium Green
arcade.draw_rectangle_filled(195,385,30,10,arcade.color.DARK_PASTEL_GREEN)
arcade.draw_rectangle_filled(215,375,10,10,arcade.color.DARK_PASTEL_GREEN)
arcade.draw_rectangle_filled(255,385,10,10,arcade.color.DARK_PASTEL_GREEN)
arcade.draw_rectangle_filled(245,365,10,30,arcade.color.DARK_PASTEL_GREEN)
arcade.draw_rectangle_filled(280,365,60,10,arcade.color.DARK_PASTEL_GREEN)
arcade.draw_rectangle_filled(320,355,20,10,arcade.color.DARK_PASTEL_GREEN)
arcade.draw_rectangle_filled(335,345,10,10,arcade.color.DARK_PASTEL_GREEN)
arcade.draw_rectangle_filled(345,335,10,10,arcade.color.DARK_PASTEL_GREEN)
arcade.draw_rectangle_filled(355,365,10,10,arcade.color.DARK_PASTEL_GREEN)
arcade.draw_rectangle_filled(180,365,40,10,arcade.color.DARK_PASTEL_GREEN)
arcade.draw_rectangle_filled(155,355,10,10,arcade.color.DARK_PASTEL_GREEN)
arcade.draw_rectangle_filled(205,355,10,10,arcade.color.DARK_PASTEL_GREEN)
arcade.draw_rectangle_filled(125,365,10,10,arcade.color.DARK_PASTEL_GREEN)
arcade.draw_rectangle_filled(115,355,10,10,arcade.color.DARK_PASTEL_GREEN)
arcade.draw_rectangle_filled(105,345,10,10,arcade.color.DARK_PASTEL_GREEN)
arcade.draw_rectangle_filled(85,295,10,10,arcade.color.DARK_PASTEL_GREEN)
arcade.draw_rectangle_filled(115,285,50,10,arcade.color.DARK_PASTEL_GREEN)
arcade.draw_rectangle_filled(175,275,70,10,arcade.color.DARK_PASTEL_GREEN)
arcade.draw_rectangle_filled(215,285,10,10,arcade.color.DARK_PASTEL_GREEN)
arcade.draw_rectangle_filled(255,330,10,20,arcade.color.DARK_PASTEL_GREEN)
arcade.draw_rectangle_filled(245,315,10,10,arcade.color.DARK_PASTEL_GREEN)
arcade.draw_rectangle_filled(250,255,20,10,arcade.color.DARK_PASTEL_GREEN)
arcade.draw_rectangle_filled(255,265,10,10,arcade.color.DARK_PASTEL_GREEN)
arcade.draw_rectangle_filled(265,245,10,10,arcade.color.DARK_PASTEL_GREEN)
arcade.draw_rectangle_filled(250,235,20,10,arcade.color.DARK_PASTEL_GREEN)
arcade.draw_rectangle_filled(235,225,10,10,arcade.color.DARK_PASTEL_GREEN)
arcade.draw_rectangle_filled(245,215,10,10,arcade.color.DARK_PASTEL_GREEN)
arcade.draw_rectangle_filled(180,215,20,10,arcade.color.DARK_PASTEL_GREEN)
arcade.draw_rectangle_filled(185,225,10,10,arcade.color.DARK_PASTEL_GREEN)
arcade.draw_rectangle_filled(185,195,30,10,arcade.color.DARK_PASTEL_GREEN)
arcade.draw_rectangle_filled(165,185,10,10,arcade.color.DARK_PASTEL_GREEN)
arcade.draw_rectangle_filled(305,210,50,40,arcade.color.DARK_PASTEL_GREEN)
arcade.draw_rectangle_filled(315,235,10,10,arcade.color.DARK_PASTEL_GREEN)
arcade.draw_rectangle_filled(295,235,10,10,arcade.color.DARK_PASTEL_GREEN)
arcade.draw_rectangle_filled(290,180,20,20,arcade.color.DARK_PASTEL_GREEN)
arcade.draw_rectangle_filled(305,165,30,10,arcade.color.DARK_PASTEL_GREEN)
arcade.draw_rectangle_filled(315,155,70,10,arcade.color.DARK_PASTEL_GREEN)
arcade.draw_rectangle_filled(285,145,10,10,arcade.color.DARK_PASTEL_GREEN)
arcade.draw_rectangle_filled(325,145,30,10,arcade.color.DARK_PASTEL_GREEN)
arcade.draw_rectangle_filled(320,135,20,10,arcade.color.DARK_PASTEL_GREEN)
arcade.draw_rectangle_filled(345,165,10,10,arcade.color.DARK_PASTEL_GREEN)
arcade.draw_rectangle_filled(360,185,20,10,arcade.color.DARK_PASTEL_GREEN)
arcade.draw_rectangle_filled(365,175,10,10,arcade.color.DARK_PASTEL_GREEN)
arcade.draw_rectangle_filled(345,195,10,10,arcade.color.DARK_PASTEL_GREEN)
arcade.draw_rectangle_filled(355,205,10,30,arcade.color.DARK_PASTEL_GREEN)
arcade.draw_rectangle_filled(340,215,20,10,arcade.color.DARK_PASTEL_GREEN)
arcade.draw_rectangle_filled(365,230,10,40,arcade.color.DARK_PASTEL_GREEN)
arcade.draw_rectangle_filled(375,245,10,10,arcade.color.DARK_PASTEL_GREEN)
arcade.draw_rectangle_filled(355,255,10,10,arcade.color.DARK_PASTEL_GREEN)
arcade.draw_rectangle_filled(335,265,10,10,arcade.color.DARK_PASTEL_GREEN)
arcade.draw_rectangle_filled(325,255,10,10,arcade.color.DARK_PASTEL_GREEN)
arcade.draw_rectangle_filled(295,265,10,10,arcade.color.DARK_PASTEL_GREEN)
arcade.draw_rectangle_filled(280,275,20,10,arcade.color.DARK_PASTEL_GREEN)

#Light Green
arcade.draw_rectangle_filled(220,395,60,10,arcade.color.TEA_GREEN)
arcade.draw_rectangle_filled(245,385,10,10,arcade.color.TEA_GREEN)
arcade.draw_rectangle_filled(180,375,60,10,arcade.color.TEA_GREEN)
arcade.draw_rectangle_filled(140,365,20,10,arcade.color.TEA_GREEN)
arcade.draw_rectangle_filled(125,355,10,10,arcade.color.TEA_GREEN)
arcade.draw_rectangle_filled(115,345,10,10,arcade.color.TEA_GREEN)
arcade.draw_rectangle_filled(105,335,10,10,arcade.color.TEA_GREEN)
arcade.draw_rectangle_filled(95,320,10,20,arcade.color.TEA_GREEN)
arcade.draw_rectangle_filled(85,305,10,10,arcade.color.TEA_GREEN)
arcade.draw_rectangle_filled(275,375,50,10,arcade.color.TEA_GREEN)
arcade.draw_rectangle_filled(315,385,30,10,arcade.color.TEA_GREEN)
arcade.draw_rectangle_filled(335,375,10,10,arcade.color.TEA_GREEN)
arcade.draw_rectangle_filled(345,360,10,20,arcade.color.TEA_GREEN)
arcade.draw_rectangle_filled(355,340,10,20,arcade.color.TEA_GREEN)
arcade.draw_rectangle_filled(355,310,10,20,arcade.color.TEA_GREEN)
arcade.draw_rectangle_filled(365,295,10,10,arcade.color.TEA_GREEN)
arcade.draw_rectangle_filled(345,325,10,10,arcade.color.TEA_GREEN)
arcade.draw_rectangle_filled(335,335,10,10,arcade.color.TEA_GREEN)
arcade.draw_rectangle_filled(320,345,20,10,arcade.color.TEA_GREEN)
arcade.draw_rectangle_filled(280,355,60,10,arcade.color.TEA_GREEN)
arcade.draw_rectangle_filled(245,330,10,20,arcade.color.TEA_GREEN)
arcade.draw_rectangle_filled(235,315,10,10,arcade.color.TEA_GREEN)
arcade.draw_rectangle_filled(265,255,10,10,arcade.color.TEA_GREEN)
arcade.draw_rectangle_filled(275,245,10,10,arcade.color.TEA_GREEN)
arcade.draw_rectangle_filled(265,235,10,10,arcade.color.TEA_GREEN)
arcade.draw_rectangle_filled(295,250,10,20,arcade.color.TEA_GREEN)
arcade.draw_rectangle_filled(355,245,10,10,arcade.color.TEA_GREEN)
arcade.draw_rectangle_filled(315,180,10,20,arcade.color.TEA_GREEN)
arcade.draw_rectangle_filled(305,185,10,10,arcade.color.TEA_GREEN)
arcade.draw_rectangle_filled(325,165,10,10,arcade.color.TEA_GREEN)

#Dark Green
arcade.draw_rectangle_filled(305,175,10,10,arcade.color.OFFICE_GREEN)
arcade.draw_rectangle_filled(295,165,10,10,arcade.color.OFFICE_GREEN)
arcade.draw_rectangle_filled(315,155,30,10,arcade.color.OFFICE_GREEN)

#Light Brown
arcade.draw_rectangle_filled(145,195,30,10,arcade.color.PULLMAN_BROWN)
arcade.draw_rectangle_filled(160,205,20,10,arcade.color.PULLMAN_BROWN)
arcade.draw_rectangle_filled(215,215,50,10,arcade.color.PULLMAN_BROWN)
arcade.draw_rectangle_filled(225,225,10,10,arcade.color.PULLMAN_BROWN)
arcade.draw_rectangle_filled(300,205,40,10,arcade.color.PULLMAN_BROWN)
arcade.draw_rectangle_filled(375,215,10,10,arcade.color.PULLMAN_BROWN)

#Medium Dark Brown
arcade.draw_rectangle_filled(150,185,20,10,arcade.color.LIGHT_BROWN)
arcade.draw_rectangle_filled(165,195,10,10,arcade.color.LIGHT_BROWN)
arcade.draw_rectangle_filled(205,205,70,10,arcade.color.LIGHT_BROWN)

#Medium Light Brown
arcade.draw_rectangle_filled(135,205,30,10,arcade.color.GOLDEN_BROWN)
arcade.draw_rectangle_filled(160,215,20,10,arcade.color.GOLDEN_BROWN)
arcade.draw_rectangle_filled(365,215,10,10,arcade.color.GOLDEN_BROWN)
arcade.draw_rectangle_filled(375,225,10,10,arcade.color.GOLDEN_BROWN)
arcade.draw_rectangle_filled(305,215,50,10,arcade.color.GOLDEN_BROWN)
arcade.draw_rectangle_filled(365,215,10,10,arcade.color.GOLDEN_BROWN)
arcade.draw_rectangle_filled(375,225,10,10,arcade.color.GOLDEN_BROWN)

#Dark Brown
arcade.draw_rectangle_filled(205,225,30,10,arcade.color.SADDLE_BROWN)
arcade.draw_rectangle_filled(230,235,20,10,arcade.color.SADDLE_BROWN)
arcade.draw_rectangle_filled(250,245,20,10,arcade.color.SADDLE_BROWN)
arcade.draw_rectangle_filled(295,195,30,10,arcade.color.SADDLE_BROWN)
arcade.draw_rectangle_filled(355,195,10,10,arcade.color.SADDLE_BROWN)
arcade.draw_rectangle_filled(370,205,20,10,arcade.color.SADDLE_BROWN)

#Light Yellow
arcade.draw_rectangle_filled(225,295,30,10,arcade.color.YELLOW)
arcade.draw_rectangle_filled(230,285,20,10,arcade.color.YELLOW)
arcade.draw_rectangle_filled(230,275,40,10,arcade.color.YELLOW)
arcade.draw_rectangle_filled(245,265,10,10,arcade.color.YELLOW)
arcade.draw_rectangle_filled(180,265,80,10,arcade.color.YELLOW)
arcade.draw_rectangle_filled(125,275,30,10,arcade.color.YELLOW)

#Medium Yellow
arcade.draw_rectangle_filled(85,285,10,10,arcade.color.TITANIUM_YELLOW)
arcade.draw_rectangle_filled(95,275,30,10,arcade.color.TITANIUM_YELLOW)
arcade.draw_rectangle_filled(115,265,50,10,arcade.color.TITANIUM_YELLOW)
arcade.draw_rectangle_filled(165,255,150,10,arcade.color.TITANIUM_YELLOW)
arcade.draw_rectangle_filled(230,265,20,10,arcade.color.TITANIUM_YELLOW)
arcade.draw_rectangle_filled(170,245,100,10,arcade.color.TITANIUM_YELLOW)

#Dark Yellow
arcade.draw_rectangle_filled(185,235,70,10,arcade.color.DARK_YELLOW)
arcade.draw_rectangle_filled(230,245,20,10,arcade.color.DARK_YELLOW)

#Black Outline
arcade.draw_rectangle_filled(75,290,10,40,arcade.color.BLACK)
arcade.draw_rectangle_filled(85,320,10,20,arcade.color.BLACK)
arcade.draw_rectangle_filled(95,345,10,30,arcade.color.BLACK)
arcade.draw_rectangle_filled(105,365,10,10,arcade.color.BLACK)
arcade.draw_rectangle_filled(130,375,40,10,arcade.color.BLACK)
arcade.draw_rectangle_filled(165,385,30,10,arcade.color.BLACK)
arcade.draw_rectangle_filled(185,395,10,10,arcade.color.BLACK)
arcade.draw_rectangle_filled(220,405,60,10,arcade.color.BLACK)
arcade.draw_rectangle_filled(255,395,10,10,arcade.color.BLACK)
arcade.draw_rectangle_filled(280,385,40,10,arcade.color.BLACK)
arcade.draw_rectangle_filled(315,395,30,10,arcade.color.BLACK)
arcade.draw_rectangle_filled(335,385,10,10,arcade.color.BLACK)
arcade.draw_rectangle_filled(345,375,10,10,arcade.color.BLACK)
arcade.draw_rectangle_filled(355,360,10,20,arcade.color.BLACK)
arcade.draw_rectangle_filled(365,325,10,50,arcade.color.BLACK)
arcade.draw_rectangle_filled(375,275,10,50,arcade.color.BLACK)
arcade.draw_rectangle_filled(385,220,10,60,arcade.color.BLACK)
arcade.draw_rectangle_filled(375,180,10,20,arcade.color.BLACK)
arcade.draw_rectangle_filled(365,165,10,10,arcade.color.BLACK)
arcade.draw_rectangle_filled(355,155,10,10,arcade.color.BLACK)
arcade.draw_rectangle_filled(345,145,10,10,arcade.color.BLACK)
arcade.draw_rectangle_filled(335,135,10,10,arcade.color.BLACK)
arcade.draw_rectangle_filled(315,125,30,10,arcade.color.BLACK)
arcade.draw_rectangle_filled(290,135,20,10,arcade.color.BLACK)
arcade.draw_rectangle_filled(275,145,10,10,arcade.color.BLACK)
arcade.draw_rectangle_filled(265,165,10,30,arcade.color.BLACK)
arcade.draw_rectangle_filled(275,185,10,10,arcade.color.BLACK)
arcade.draw_rectangle_filled(315,195,10,10,arcade.color.BLACK)
arcade.draw_rectangle_filled(335,195,10,10,arcade.color.BLACK)
arcade.draw_rectangle_filled(325,180,10,20,arcade.color.BLACK)
arcade.draw_rectangle_filled(345,180,10,20,arcade.color.BLACK)
arcade.draw_rectangle_filled(335,165,10,10,arcade.color.BLACK)
arcade.draw_rectangle_filled(275,205,10,10,arcade.color.BLACK)
arcade.draw_rectangle_filled(260,195,20,10,arcade.color.BLACK)
arcade.draw_rectangle_filled(245,205,10,10,arcade.color.BLACK)
arcade.draw_rectangle_filled(220,195,40,10,arcade.color.BLACK)
arcade.draw_rectangle_filled(195,185,10,10,arcade.color.BLACK)
arcade.draw_rectangle_filled(160,175,60,10,arcade.color.BLACK)
arcade.draw_rectangle_filled(135,185,10,10,arcade.color.BLACK)
arcade.draw_rectangle_filled(125,195,10,10,arcade.color.BLACK)
arcade.draw_rectangle_filled(115,205,10,10,arcade.color.BLACK)
arcade.draw_rectangle_filled(135,215,30,10,arcade.color.BLACK)
arcade.draw_rectangle_filled(160,225,20,10,arcade.color.BLACK)
arcade.draw_rectangle_filled(135,235,30,10,arcade.color.BLACK)
arcade.draw_rectangle_filled(110,245,20,10,arcade.color.BLACK)
arcade.draw_rectangle_filled(95,255,10,10,arcade.color.BLACK)
arcade.draw_rectangle_filled(85,265,10,10,arcade.color.BLACK)
arcade.draw_rectangle_filled(180,330,40,20,arcade.color.BLACK)
arcade.draw_rectangle_filled(180,345,20,10,arcade.color.BLACK)
arcade.draw_rectangle_filled(180,315,20,10,arcade.color.BLACK)

#White
arcade.draw_rectangle_filled(175,325,10,10,arcade.color.WHITE)

arcade.finish_render()
arcade.run()
