import simpy
import random
import blobWorld
import matplotlib.pyplot as plt
import numpy as np

daily_produce = 0
blob_list = []
counter = 0
def day():
	global blob_list
	global counter
	global daily_produce
  	daily_produce = 0
	print("Day : "  , counter)
	tempBlobList = blob_list.copy()
	blob_list = []
	for blob in tempBlobList:
		if(blob.energy == 0 or blob.days == 0):
			pass
		else:
			blob_list.append(blob)

		
		daily_produce += blob.hunt()

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
	if(counter%4 == 0):
		for blob in blob_list:
			reproduced = blob.reproduce()
			if(reproduced != None):
				blob_list.append(reproduced)


	for blob in blob_list:
		blob.setEnergy(blob.getEnergy() - 4)
		blob.days -= 1
	
	counter +=1

def calamityDay():
	global counter
	global blob_list
	global daily_produce
  	daily_produce = 0
	print("Day : " , counter)
	tempBlobList = blob_list.copy()
	blob_list = []
	for blob in tempBlobList:
		if(blob.energy <= 3 or blob.days == 0):
			pass
		else:
			blob_list.append(blob)

		daily_produce += blob.hunt2()

	list_of_borrowers = blob_list.copy()
	list_of_borrowers = sorted(list_of_borrowers, key = lambda x: x.friendliness, reverse = True)

	for blob in blob_list:
		if(blob.getEnergy() <= 4):
			for bf in list_of_borrowers:
				if(bf.friendliness >= 9 and bf.energy >= 10 - blob.getEnergy()):
					bf.setEnergy(bf.getEnergy() - 5 + blob.getEnergy())
					blob.setEnergy(5)

					blob.setProductivity(-1)
					bf.setProductivity(1)

	# for blob in blob_list:
	# 	reproduced = blob.reproduce()
	# 	if(reproduced != None):
	# 		blob_list.append(reproduced)


	for blob in blob_list:
		blob.setEnergy(blob.getEnergy() - 4)
		blob.setProductivity(1)
		blob.days -= 1

	

	
	counter +=1
			

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
		print("testing")

	population_list = []
 	daily_produce_list = []
	i = 1
	while(i<=56):

		if(i%7 == 0):
			calamityDay()
		else:
			day()
		i+=1
		population_list.append(len(blob_list))
		daily_produce_list.append(daily_produce)

	days = [i for i in range(1,57)] #for the x axis
	y = [population_list, daily_produce_list]
	for i in range(len(y[0])):
		plt.plot(days,[pt[i] for pt in y],label = 'id %s'%i)	
 
 	plt.plot(days,population_list)
	plt.show()
	
	



	#env = simpy.Environment()
	#env.process(day())
	#env.run()

if __name__ == "__main__":
    main()

