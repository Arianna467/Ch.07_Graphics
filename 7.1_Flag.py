'''
FLAG PROJECT
---------------
Make your flag 260 pixels tall
Use the scaling image on the website to determine other dimensions
The hexadecimal colors for the official flag are red: #BF0A30 and blue: #002868
Title the window, "The Stars and Stripes"
You can use a draw_text command and used 20 pt. asterisks for the stars.
We will have a competition to see who can make this flag in the least lines of code.
The record is 16! You will have to use some loops to achieve this.
CHALLENGE: Can you make the entire flag parametrically? This means if I change the hoist to 520px the flag will resize accordingly.
'''
import arcade
arcade.open_window(494,260)
arcade.set_background_color(arcade.color.WHITE)
arcade.start_render()

#Strips
for i in range(10,400,40):
    arcade.draw_line(0,i,510,i,(191,10,48),20)

#Blue
arcade.draw_rectangle_filled(0,400,375.44,560,(0,40,104))

#Stars
for i in range(120,300,30):
    arcade.draw_text("*",8,i,arcade.color.WHITE)
for i in range(120, 300, 30):
    arcade.draw_text("*", 41, i, arcade.color.WHITE)
for i in range(120, 300, 30):
    arcade.draw_text("*", 74, i, arcade.color.WHITE)
for i in range(120, 300, 30):
    arcade.draw_text("*", 107, i, arcade.color.WHITE)
for i in range(120, 300, 30):
    arcade.draw_text("*", 140, i, arcade.color.WHITE)
for i in range(120, 300, 30):
    arcade.draw_text("*", 173, i, arcade.color.WHITE)
for i in range(135, 330, 30):
    arcade.draw_text("*", 157.5, i, arcade.color.WHITE)
for i in range(135, 330, 30):
    arcade.draw_text("*", 23.5, i, arcade.color.WHITE)
for i in range(135, 330, 30):
    arcade.draw_text("*", 56.5, i, arcade.color.WHITE)
for i in range(135, 330, 30):
    arcade.draw_text("*", 89.5, i, arcade.color.WHITE)
for i in range(135, 330, 30):
    arcade.draw_text("*", 122.5, i, arcade.color.WHITE)

arcade.finish_render()
arcade.run()