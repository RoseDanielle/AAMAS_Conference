#this script is to iterate over the best network results for each Run in a specific experiment, find the best fo 20 runs

import os

for morph in range(1,4):
	for diff in range(1,4):

		maxVal = 0
		maxRun = 0

		for run in range(1,20):

			detailsFile = "/home/ruben/Masters_2017/AAMAS_Conference/Raw_Experiment_Results/AAMAS_Conference_Evo_Results/BestNetworks/Morphology_" + str(morph) + "/Level_" + str(diff) + "/Run_" + str(run)
			tempDir = detailsFile + "/"
			for subdir, dirs, files in os.walk(detailsFile):
				for dir in dirs:
					tempDir = tempDir + dir
			fileDir = tempDir + "/info.txt"
			myFile = open(fileDir, "r")
			fileContent = myFile.read()
			value = fileContent[fileContent.index('.')-1:len(fileContent)]
			myFile.close()

			if value > maxVal:
				maxVal = value
				maxRun = run

		
		bestNetworkDir = "/home/ruben/Masters_2017/AAMAS_Conference/Raw_Experiment_Results/AAMAS_Conference_Evo_Results/BestNetworks/Morphology_" + str(morph) + "/Level_" + str(diff) + "/Run_" + str(maxRun)
		destDir = "/home/ruben/Masters_2017/AAMAS_Conference/Raw_Experiment_Results/AAMAS_Conference_Evo_Results/BestNetworks/Morphology_" + str(morph) + "/Level_" + str(diff) + "/BestOfAll/"

		os.system("cp -r " + bestNetworkDir + " " + destDir)
