"""
CP1404/CP5632 Practical

"""

HEX_COLOURS = {"DarkOrchid4": "#68228b", "DeepPink1": "#ff1493", "black": "	#000000", "cyan1": "#00ffff",
               "firebrick2": "#ee2c2c", "GhostWhite": "#f8f8ff", "green1": "#00ff00", "yellow1": "#ffff00",
               "SlateBlue4": "#473c8b", "orange1": "#ffa500"}

colour = input("Enter colour: ")
while colour != "":
    if colour in HEX_COLOURS:
        print(f"{colour}: {HEX_COLOURS[colour]}")
    else:
        print("colour not in dictionary.")
    colour = input("Enter colour: ")