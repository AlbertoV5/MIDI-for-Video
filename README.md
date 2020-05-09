# MIDI-for-Video
Plot MIDI CSV for video with Python-Matplotlib

Included Dean Town folder with all the individual MIDI .csv and their respective graphs. Separated by folders as that was the easiest way with my current setup.

How to Use:
 1. Get a MIDI to .CSV script/tool, make sure the script reads the column you are interested in (Pitch, Position, Velocity, Length). I'm using beat instead of MIDI ticks for position and length (from a resolution of 1/960). 
 2. Place the parts of the section or instrument in a folder and then use the Sequence function with the desired directory and the color values. It will get all .csv in the path and process them.
 3. You now have .png files that can be used for whatever you like. Like moving them around in Premiere, that's the current scuffed version. Later I'll add some video libraries for generating a video on the spot with tempo/metrics.

I'll upload my MIDI to CSV Lua script for Reaper soon although you can probably make one in Python.
