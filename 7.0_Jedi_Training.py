#Sign your name: Arianna Lear

'''
Recreate, exactly the Test Picture from the website. The arcade colors used in this picture in no particular order are:
BLACK, ALMOND, PHLOX, BLUSH, RED, BLUE, WISTERIA, AMBER, BRICK_RED and YELLOW.
The picture is 500px wide and 400px tall. Look up ARC in the documentation to do the PAC-MAN.
'''
import arcade
arcade.open_window(500,400,"My Drawing")
arcade.set_background_color(arcade.color.ALMOND)

#Grid
arcade.start_render()
for i in range(0,510,20):
    arcade.draw_line(i,0,i,400,arcade.color.BLACK,1)
for i in range(0,410,20):
    arcade.draw_line(0,i,510,i,arcade.color.BLACK,1)

#Purple Rectangle
arcade.draw_lrtb_rectangle_filled(20,80,380,360,arcade.color.PHLOX)

#Tilted Rectangle
arcade.draw_rectangle_filled(200,260,20,40,arcade.color.BLUSH,40)

#Pac-Man
arcade.draw_arc_filled(400,320,120,120,arcade.color.YELLOW,30,330)

#Purple Circle
arcade.draw_circle_filled(260,200,40,arcade.color.WISTERIA)

#Orange Ellipse
arcade.draw_ellipse_filled(100,100,120,40,arcade.color.AMBER)

#Text
arcade.draw_text("I love you. I know.",20,180,arcade.color.BRICK_RED,20)

#Line
arcade.draw_line(80,20,120,60,arcade.color.BLUE)

#Dot
arcade.draw_point(460,10,arcade.color.RED,5)

arcade.finish_render()
arcade.run()