import zipfile, os

def main(branchDir, extendedExtractPath):
	# BranchDir is a string
	print(branchDir)
	
	# count number of folders in the directory
	Numfolders = len(next(os.walk(branchDir))[1])
	#sum(os.path.isdir(i) for i in os.listdir(branchDir))
	print("Numfolder: ", Numfolders)
	
	for folder in range(0, Numfolders):
		print("Folder: ", folder)
		listFolders = os.listdir(branchDir)
		print("listFolders: ", listFolders)
		extractPlace = listFolders[folder] + extendedExtractPath #"\\arcgis\\rest\\directories\\arcgisoutput\\Download_GPServer"
		print("extractionFolder: ", branchDir + "\\" + extractPlace)
		zipFile = ""
		#select .zip folder
		for file in os.listdir(branchDir + "\\" + extractPlace):
			if file.endswith(".zip"):
				zipFile = os.path.join(branchDir + "\\" + extractPlace, file)
				print("zipFile: ", zipFile)
			
		
		with zipfile.ZipFile(zipFile, "r") as zip_ref:
			zip_ref.extractall(branchDir + "\\" + extractPlace)
			print("extracted")
	print("Done main")
main(input("Put in the branch of where the folders of zips are: "), input("If the extraction place is within this folder, where is the path inside that folder you want to extract to (Must be same path for all folders)? "))

