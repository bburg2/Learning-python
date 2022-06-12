# modules are essentialy .py files with different functionality. you can import the functions using "import"

# game.py
# import the draw module
# here only an object is imported from a module
from draw import draw_game

def main():
    result = play_game()
    draw_game(result)
    
# game.py
# import the draw module
# here all object from the module are imported
from draw import *

def main():
    result = play_game()
    draw_game(result)
    
    
# game.py
# import the draw module
# with the help of "as" you can rename an object to something else
if visual_mode:
    # in visual mode, we draw using graphics
    import draw_visual as draw
else:
    # in textual mode, we print out text
    import draw_textual as draw

def main():
    result = play_game()
    # this can either be visual or textual depending on visual_mode
    draw.draw_game(result)

# using "PYTHONPATH" you can specify the path of the module
PYTHONPATH=/foo python game.py

# you can also use the following function to expand where to import function looks for modules
sys.path.append("/foo")

# the urllib module enables you to create data from an url
# import the library
import urllib

# to see wich functions are installed in a module
dir(urllib)

# with the help function we can find out more about a function
help(urllib.urlopen)

# a package in pytohn is a directory wich must contain __init__.py, this file can be empty an indicates that the directory its in is a pytoh package so it can be imported the same way as a module
