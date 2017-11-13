import os

fileDir = "/home/p/pttand010/Desktop/AAMAS_Experiments/Results/AAMAS_Conference/HyperNEATNovelty/"
os.chdir(fileDir)

for num in range(1,21):
    os.system("mkdir Run_" + str(num))
