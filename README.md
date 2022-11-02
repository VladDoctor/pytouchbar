#Button

#A button the user can click, that will call actions.

def function(button):
  print ('Button clicked!')

button = PyTouchBar.TouchBarItems.Button(title = 'Click me!', action = function)

#Parameters:

#title (String or None, get & set) : The string that will be displayed in the button
#color (tuple or None, get & set) : The button background color. Formatted as (r, g, b, a) where values are decimal numbers between 0 and 1. You can use #the color constants.
#image (String or None, get & set) : A path to an image file that will be shown on the button
#image_position (ImagePosition) : The position of the image relative to the title. Image positions are defined in constants.
#image_scale (ImageScale) : The image scaling. Image scales are defined in constants.
#action (function taking button as argument) : The function that will be called when the user touchs the button

ВЗЯЛ ОТСЮДА: https://github.com/Maxmad68/PyTouchBar/wiki/Populate-TouchBar#Button
