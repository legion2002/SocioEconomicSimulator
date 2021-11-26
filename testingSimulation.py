import simpy
import random
#import blobWorld.py

def generateBlobs():
	friendliness = randint(1, 10)
	greediness = randint(1, 10)
	productivity = randint(1,3)
	motivation = randint(1, 10)
	energy = 10
	return Blob(friendliness,greediness,productivity,motivation,energy)


def main():
	#Creating a list of blobs

	blob_list = []

	max_blobs = 100
	num_simulations = 14
	for i in range(max_blobs):
		blob_list.append(generateBlobs())

