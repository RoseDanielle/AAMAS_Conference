import os

#method to find the max epoch or the best netowrk out of all the evolutionary runs
def findMaxEpoch(mydir):
	max = 0
	for subdir, dirs, files in os.walk(mydir):
		for dir in dirs: #iterating over all the folders in the directory, checking all the saved networks
			newNum = int(dir[6:len(dir)])
			if newNum > max:
				max = newNum

	return max

for morphNum in range(1,4):
	for diff in range(1,4):

		for run in range (1,11):

			currentDir = "/home/ruben/Masters_2017/AAMAS_Conference/Raw_Experiment_Results/AAMAS_Evo_Results/AAMAS_Conference/HyperNEATNovelty/Morphology_" + str(morphNum) + "/Level_" + str(diff) + "/Run_" + str(run) + "/best networks/"
			
			consoleCurrentDir = "/home/ruben/Masters_2017/AAMAS_Conference/Raw_Experiment_Results/AAMAS_Evo_Results/AAMAS_Conference/HyperNEATNovelty/Morphology_" + str(morphNum) + "/Level_" + str(diff) + "/Run_" + str(run) + "/best\ networks/"
			moveToDir = "/home/ruben/Masters_2017/AAMAS_Conference/Raw_Experiment_Results/AAMAS_Evo_Results/AAMAS_Conference/HyperNEATNovelty/Morphology_" + str(morphNum) + "/Level_" + str(diff) + "/Run_" + str(run)
			maxEpoch = findMaxEpoch(currentDir)
			tempDir = consoleCurrentDir + "epoch-" + str(maxEpoch) + "/info.txt"
			#print tempDir
			os.system("cp -r " + tempDir + " " + moveToDir)
				