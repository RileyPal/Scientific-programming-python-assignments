from vpython import *

# GlowScript 3.0 VPython

# Written by Ruth Chabay, licensed under Creative Commons 4.0.
# All uses permitted, but you must not claim that you wrote it, and
# you must include this license information in any copies you make.
# For details see http://creativecommons.org/licenses/by/4.0

scene.background = color.white
scene.width = 600
scene.height = 600
scene.forward = vector(-.5, -.3, -1)

scene.caption = """To rotate "camera", drag with right button or Ctrl-drag.
To zoom, drag with middle button or Alt/Option depressed, or use scroll wheel.
  On a two-button mouse, middle is left + right.
To pan left/right and up/down, Shift-drag.
Touch screen: pinch/extend to zoom, swipe or two-finger rotate."""

x_axis = cylinder(color=vector(1, 0, 0), pos=vector(0, 0, 0), axis=vector(10, 0, 0), radius=0.3)
y_axis = cylinder(color=vector(0, 1, 0), pos=vector(0, 0, 0), axis=vector(0, 10, 0), radius=0.3)
z_axis = cylinder(color=vector(0, 0, 1), pos=vector(0, 0, 0), axis=vector(0, 0, 10), radius=0.3)

# Numbers for the vector are chosen arbitrarily
a, b, c = 5, 7, 3
vector_arrow = arrow(pos=vector(0, 0, 0), axis=vector(a, b, c), color=color.orange)

# Label the vector
label(pos=vector(a/2, b/2, c/2), text=f'r = {a}x + {b}y + {c}z', color=color.black)