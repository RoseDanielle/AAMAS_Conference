import os

for morph in range(1,2):
	for diff in range(1,4):

		maxValue = 0
		maxRun = 0

		for run in range(1,11):

			curDir = "/home/ruben/Masters_2017/AAMAS_Conference/Raw_Experiment_Results/AAMAS_Evo_Results/AAMAS_Conference/HyperNEATNovelty/Morphology_" + str(morph) + "/Level_" + str(diff) + "/Run_" + str(run)
			fileDir = curDir + "/info.txt"
			myFile = open(fileDir, 'r')
			myLine = myFile.read()
			value = float(myLine[myLine.index("fitness: ") + len("fitness: "):len(myLine)])
			if value > maxValue:
				maxValue = value
				maxRun = run
			myFile.close()

		sourceDir = "/home/ruben/Masters_2017/AAMAS_Conference/Raw_Experiment_Results/AAMAS_Evo_Results/AAMAS_Conference/HyperNEATNovelty/Morphology_" + str(morph) + "/Level_" + str(diff) + "/Run_" + str(run) + "/network.ser" 
		destinationDir = "/home/ruben/Masters_2017/AAMAS_Conference/Raw_Experiment_Results/AAMAS_Evo_Results/AAMAS_Conference/HyperNEATNovelty/Morphology_" + str(morph) + "/Level_" + str(diff) + "/BestOfAll/"

		os.system("cp " + sourceDir + " " + destinationDir)
		#print "Max value = " + str(maxValue)
		#print "Max run = " + str(maxRun)