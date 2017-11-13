import os

#method to find the max epoch or the best netowrk out of all the evolutionary runs
def findMaxEpoch(mydir):
	max = 0
	for subdir, dirs, files in os.walk(mydir):
		for dir in dirs: #iterating over all the folders in the directory, checking all the saved networks
			newNum = dir[6:len(dir)]
			if newNum > max:
				max = newNum

	return max

morphIndex = [1, 3, 5]

for run in range(1,20):
	for morphNum in range(1,4):
		for difficulty in range(1,4):

			currentDir = "/home/ruben/Masters_2017/AAMAS_Conference/Raw_Experiment_Results/AAMAS_Conference_Evo_Results/Run_" + str(run) + "/results/Morphology_" + str(morphIndex[morphNum-1]) + "/Level_" + str(difficulty) + "/best networks"
			m = findMaxEpoch(currentDir)
			curD = currentDir = "/home/ruben/Masters_2017/AAMAS_Conference/Raw_Experiment_Results/AAMAS_Conference_Evo_Results/Run_" + str(run) + "/results/Morphology_" + str(morphIndex[morphNum-1]) + "/Level_" + str(difficulty) + "/best\ networks"
			curD = curD + "/epoch-" + str(m)
			destinationDir = "/home/ruben/Masters_2017/AAMAS_Conference/Raw_Experiment_Results/AAMAS_Conference_Evo_Results/BestNetworks/Morphology_" + str(morphNum) + "/Level_" + str(difficulty) + "/Run_" + str(run)
			os.system("cp -r " + curD + " " + destinationDir)
				