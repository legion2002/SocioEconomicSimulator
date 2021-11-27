import simpy
import random
import blobWorld
import matplotlib.pyplot as plt
import numpy as np

a_g = 0
a_ng = 0
na_g = 0
na_ng = 0
offset = 1


daily_produce = 0
blob_list = []
counter = 0
def day():
	global a_g,a_ng,na_g,na_ng
	global offset
	global blob_list
	global counter
	global daily_produce
	a_g = 0
	a_ng = 0
	na_g = 0
	na_ng = 0
	daily_produce = 0
	print("Day : "  , counter)
	tempBlobList = blob_list.copy()
	blob_list = []
	for blob in tempBlobList:
		if(blob.energy == 0 or blob.days == 0):
			pass
		else:
			blob_list.append(blob)

		a = blob.hunt()
		if(a is not None):
			daily_produce += a

	list_of_borrowers = blob_list.copy()
	list_of_borrowers = sorted(list_of_borrowers, key = lambda x: x.friendliness, reverse = True)

	for blob in blob_list:
		if(blob.getEnergy() <= 4):
			for bf in list_of_borrowers:
				if(bf.friendliness > 6 and bf.energy >= 10 + offset - blob.getEnergy()):
					bf.setEnergy(bf.getEnergy() - 5 + blob.getEnergy() - offset)
					blob.setEnergy(5 + offset)

					blob.setProductivity(-1)
					bf.setProductivity(1)
	if(counter%4 == 0):
		for blob in blob_list:
			reproduced = blob.reproduce()
			if(reproduced != None):
				blob_list.append(reproduced)


	for blob in blob_list:
		blob.setEnergy(blob.getEnergy() - 4 - offset)
		blob.days -= 1
		if(blob.greediness > 5 and blob.friendliness > 5):
			a_g += 1
		elif(blob.greediness > 5 and blob.friendliness < 5):
			a_ng += 1
		elif(blob.greediness < 5 and blob.friendliness > 5):
			na_g += 1
		else:
			na_ng +=1
   

		
	
	counter +=1

def calamityDay():
	global a_g,a_ng,na_g,na_ng
	global offset
	global counter
	global blob_list
	global daily_produce
	a_g = 0
	a_ng = 0
	na_g = 0
	na_ng = 0
	daily_produce = 0
	print("Day : " , counter)
	tempBlobList = blob_list.copy()
	blob_list = []
	for blob in tempBlobList:
		if(blob.energy <= 3 or blob.days == 0):
			pass
		else:
			blob_list.append(blob)

		a = blob.hunt2()
		if(a is not None):
			daily_produce += a

	list_of_borrowers = blob_list.copy()
	list_of_borrowers = sorted(list_of_borrowers, key = lambda x: x.friendliness, reverse = True)

	for blob in blob_list:
		if(blob.getEnergy() <= 4):
			for bf in list_of_borrowers:
				if(bf.friendliness >= 9 and bf.energy >= 10 - blob.getEnergy() + offset):
					bf.setEnergy(bf.getEnergy() - 5 + blob.getEnergy() - offset)
					blob.setEnergy(5 + 1 )

					blob.setProductivity(-1)
					bf.setProductivity(1)

	for blob in blob_list:
		blob.setEnergy(blob.getEnergy() - 4 - offset)
		blob.days -= 1
		if(blob.greediness > 5 and blob.friendliness > 5):
			a_g += 1
		elif(blob.greediness > 5 and blob.friendliness < 5):
			a_ng += 1
		elif(blob.greediness < 5 and blob.friendliness > 5):
			na_g += 1
		else:
			na_ng +=1

	counter +=1
			

def generateBlobsAG():
	friendliness = random.randint(1, 5)
	greediness = random.randint(6, 10)
	productivity = random.randint(1,3)
	motivation = random.randint(1, 5)
	energy = 10
	return blobWorld.Blob(friendliness,greediness,productivity,motivation,energy)

def generateBlobsNAG():
	friendliness = random.randint(1, 5)
	greediness = random.randint(1, 5)
	productivity = random.randint(1,3)
	motivation = random.randint(1, 5)
	energy = 10
	return blobWorld.Blob(friendliness,greediness,productivity,motivation,energy)

def generateBlobsANG():
	friendliness = random.randint(6, 10)
	greediness = random.randint(6, 10)
	productivity = random.randint(1,3)
	motivation = random.randint(1, 5)
	energy = 10
	return blobWorld.Blob(friendliness,greediness,productivity,motivation,energy)

def generateBlobsNANG():
	friendliness = random.randint(6, 10)
	greediness = random.randint(1, 5)
	productivity = random.randint(1,3)
	motivation = random.randint(1, 5)
	energy = 10
	return blobWorld.Blob(friendliness,greediness,productivity,motivation,energy)



def main():
	global offset
	#Creating a list of blobs//print("hi")
	max_blobs = 40
	num_simulations = 14
	for i in range(max_blobs // 4):
		blob_list.append(generateBlobsAG())
		blob_list.append(generateBlobsANG())
		blob_list.append(generateBlobsNANG())
		blob_list.append(generateBlobsNAG())
  
		#print("testing")

	population_list = []
	daily_produce_list = []
	ag =[]
	ang=[]
	nag=[]
	nang=[]
	i = 1
	while(i<=1000):

		if(i%70 == 2):
			calamityDay()
		else:
			day()
		i+=1
		population_list.append(len(blob_list))
		daily_produce_list.append(daily_produce)
		ag.append(a_g)
		ang.append(a_ng)
		nag.append(na_g)
		nang.append(na_ng)

		if(daily_produce_list[-1] >= 10000):
			offset = 2
		else:
			offset = 1
		

	days = [i for i in range(1,1001)] #for the x axis
	y = [population_list, daily_produce_list]

	plt.plot(days,population_list,color='green')
	plt.plot(days,daily_produce_list,color='orange')
	plt.show(block=True)

	plt.plot(days,ag,color='red') #Doesnt repro and gives
	plt.plot(days,ang,color='green') #Doesnt repro and doesnt give
	plt.plot(days,nag,color='darkblue')  #repro and gives
	plt.plot(days,nang,color='orange') #repro and doesnt give
	plt.show(block=True)

	


if __name__ == "__main__":
    main()

