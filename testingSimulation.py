import simpy
import random
import blobWorld

blob_list = []

def day():
	print("Day : ")
	for blob in blob_list:
		if(blob.energy == 0 or blob.days == 0):
			blob_list.remove(blob)

		blob.hunt()

	list_of_borrowers = blob_list.copy()
	list_of_borrowers = sorted(list_of_borrowers, key = lambda x: x.friendliness, reverse = True)

	for blob in blob_list:
		if(blob.getEnergy() <= 4):
			for bf in list_of_borrowers:
				if(bf.friendliness > 6 and bf.energy >= 10 - blob.getEnergy()):
					bf.setEnergy(bf.getEnergy() - 5 + blob.getEnergy())
					blob.setEnergy(5);

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
	greediness = random.random.randint(1, 10)
	productivity = random.randint(1,3)
	motivation = random.randint(1, 10)
	energy = 10
	return blobWorld.Blob(friendliness,greediness,productivity,motivation,energy)


def main():
	#Creating a list of blobs

	max_blobs = 100
	num_simulations = 14
	for i in range(max_blobs):
		blob_list.append(generateBlobs())
		print("testing")

	print(blob_list)

	#env = simpy.Environment()
	#env.process(day())
	#env.run()
