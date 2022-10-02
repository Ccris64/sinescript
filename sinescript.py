import pysine
import sys

if len(sys.argv) < 2:
    print("Please specify a txt file with sinescript format. Example: sinescript myscript.sines")
    exit()

f = open(sys.argv[1],"r")

for line in f:
    freq = line.split(" ")[0]
    dur = line.split(" ")[1].replace("\n","")
    pysine.sine(frequency=int(freq),duration=float(dur))
f.close()