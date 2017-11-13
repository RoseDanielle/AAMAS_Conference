import os

morphIndexArr = [1,3,5]

myFile = open("/home/p/pttand010/Desktop/AAMAS_Experiments/Results/AAMAS_Conference/HyperNEATNovelty/MissingRuns.txt", 'a')

for run in range(1,21):
	checked = False
	for morph in range(1,4):
		for diff in range(1,4):

			sourceDirPython = "/home/p/pttand010/Desktop/AAMAS_Experiments/HyperNEATNovelty/Run_" + str(run) + "/AAMAS_Conference/results/Morphology_" + str(morphIndexArr[morph-1]) + "/Level_" + str(diff) + "/best networks/" #the folder where the experiments were run
			sourceDirConsole = "/home/p/pttand010/Desktop/AAMAS_Experiments/HyperNEATNovelty/Run_" + str(run) + "/AAMAS_Conference/results/Morphology_" + str(morphIndexArr[morph-1]) + "/Level_" + str(diff) + "/best\ networks/"
			
			destDir = "/home/p/pttand010/Desktop/AAMAS_Experiments/Results/AAMAS_Conference/HyperNEATNovelty/Morphology_" + str(morph) + "/Level_" + str(diff) + "/Run_" + str(run) #the folder with the git repo for all the RAW results
			
			if os.path.isdir(sourceDirPython):
				os.system("cp -r " + sourceDirConsole + " " + destDir)
			else:
				myFile.write("Run = " + str(run) + " Morphology = " + str(morphIndexArr[morph-1]) + " Level = " + str(diff) + " \n" )
				checked = True
			#os.system("cp -r " + sourceDir + " " + destDir)
	if(checked):
		myFile.write("\n") #printing a new line between each experiment run
myFile.close()