###   Created By Damion Hart AKA Death_Dealer  ###
               ###   12/13/2020   ###

from tkinter import *
from tkinter import filedialog
from tkinter.filedialog import askopenfilename
import os

root = Tk()
root.withdraw()
infile =  filedialog.askopenfilename(title = "Select .gcode to apply Creality Fix to..",
    filetypes = (("Laser G-code","*.gcode"),
    ("all files","*.*")))

infile_name = (os.path.splitext(os.path.basename(infile)))
print(infile_name[0])
infile = open(infile, "r")
######################################
#M106-Set Fan Speed
#G4P1-Dwell
#G1F750-Linear Move
######################################
#ON
M03 = str("M03")
M106 = str('M106')+str('\n')+str('G4P1')+str('\n')+str('G1F750')
#=========
#OFF
M05 = str("M05")
M107 = str('M107')+str('\n')+str('G4P1')+str('\n')+str('G1F7500')

######################################
outfile_name= str(infile_name)+("-Creality_Laser")
outfile = open(outfile_name, "w")
data = infile.read()
data = data.replace('M03', M106)
data = data.replace('M05', M107)
outfile.close()
f = open('Creality.gcode', "wt")
f.write(data)
f.close()

x = input(("Creality Fix applied to file ")+str(infile_name)+str(".gcode"))

#+str("\n")+str("Press any key to exit")
