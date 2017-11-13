import os

fileDir = "/home/ruben/Masters_2017/AAMAS_Conference/Raw_Experiment_Results/AAMAS_Conference_Evo_Results/BestNetworks/"
os.chdir(fileDir)

for num in range(1,21):
    os.system("mkdir Run_" + str(num))
