import simpy
import random
import blobWorld

blob_list = []

def day():
	print("Day : ")
	tempBlobList = blob_list.copy()
	blob_list = []
	for blob in tempBlobList:
		if(blob.energy == 0 or blob.days == 0):
			pass
		else:
			blob_list.append(blob)

		blob.hunt()

	list_of_borrowers = blob_list.copy()
	list_of_borrowers = sorted(list_of_borrowers, key = lambda x: x.friendliness, reverse = True)

	for blob in blob_list:
		if(blob.getEnergy() <= 4):
			for bf in list_of_borrowers:
				if(bf.friendliness > 6 and bf.energy >= 10 - blob.getEnergy()):
					bf.setEnergy(bf.getEnergy() - 5 + blob.getEnergy())
					blob.setEnergy(5)

					blob.setProductivity(-1)
					bf.setProductivity(1)

	for blob in blob_list:
		reproduced = blob.reproduce()
		if(reproduced != None):
			blob_list.append(reproduced)


	for blob in blob_list:
		blob.setEnergy(blob.getEnergy() - 4)
		blob.days -= 1


			

def generateBlobs():
	friendliness = random.randint(1, 10)
	greediness = random.randint(1, 10)
	productivity = random.randint(1,3)
	motivation = random.randint(1, 10)
	energy = 10
	return blobWorld.Blob(friendliness,greediness,productivity,motivation,energy)



def main():
	#Creating a list of blobs//print("hi")
	max_blobs = 10
	num_simulations = 14
	for i in range(max_blobs):
		blob_list.append(generateBlobs())

	
	i = 0
	while(i<=50):
		day()
		i+=

	

if __name__ == "__main__":
    main()
