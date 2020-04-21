import csv
import random
import math
import operator
import subprocess
import urllib2
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import Leap
import json
from sklearn.model_selection import train_test_split
from train import GenerateTrainingSet
from sklearn.naive_bayes import GaussianNB
from sklearn import datasets
from sklearn.neighbors import KNeighborsClassifier
import time
import time
from flask import Flask, render_template, request
import pyttsx3
import webbrowser
import flask
import time
import zmq
"""context = zmq.Context()
print("cotext")
socket = context.socket(zmq.REP)
socket.bind("tcp://*:5555")
print("craeted socket")"""
"""def loadDataset(filename, split, trainingSet=[] , testSet=[]):
	with open(filename, 'rb') as csvfile:
	    lines = csv.reader(csvfile)
	    dataset = list(lines)
	    set=[]
	    #len(dataset)
	    for x in range(0,len(dataset)):
	    	set[:] = []
	        for y in range(0,25):
	            dataset[x][y] = float(dataset[x][y])
	            set.append(dataset[x][y])
	        set.append(dataset[x][-1])
	       	trainingSet.append(set)
	print(trainingSet)
	return trainingSet"""

def texttospeech(text):
	engine = pyttsx3.init()
	engine.say(text)
	engine.setProperty('rate',120)
	engine.setProperty('volume', 0.9)
	engine.runAndWait()


def loadDataset(filename, split, trainingSet=[] , testSet=[]):
	with open(filename, 'rb') as csvfile:
	    lines = csv.reader(csvfile)
	    dataset = list(lines)
	    set=[]
	    for x in range(len(dataset)-1):
	    	set=[]
	        for y in range(25):
	            dataset[x][y] = float(dataset[x][y])
	            set.append(dataset[x][y])
	       	set.append(dataset[x][-1])
	        trainingSet.append(set)

	#print(trainingSet)
	return trainingSet
	        
	        
 
 
def euclideanDistance(instance1, instance2, length):
	
	distance = 0
	
	for x in range(25):
		distance += pow((instance1[x] - instance2[x]), 2)
	return math.sqrt(distance)
 
def getNeighbors(trainingSet, testInstance, k):
	distances = []
	test=[]

	length = len(testInstance)
	

	for x in range(0,25):
		test.append(float(testInstance[x]))

	for x in range(len(trainingSet)):
		dist = euclideanDistance(test, trainingSet[x], length)
		distances.append((trainingSet[x], dist))
	distances.sort(key=operator.itemgetter(1))
	#print(distances)
	neighbors = []
	for x in range(k):
		neighbors.append(distances[x][0])
	#print neighbors  
	return neighbors
 
def getResponse(neighbors):
	classVotes = {}
	#print(neighbors)
	for x in range(len(neighbors)):
		response = neighbors[x][-1]
		
        if response in classVotes:
        	classVotes[response] += 1
        else:
        	classVotes[response] = 1
	sortedVotes = sorted(classVotes.iteritems(), key=operator.itemgetter(1), reverse=True)
	print(sortedVotes)
	return sortedVotes[0][0]
 
def getAccuracy(testSet, predictions):
	correct = 0
	for x in range(len(testSet)):
		if testSet[x][-1] == predictions[x]:
			correct += 1
	return (correct/float(len(testSet))) * 100.0
	
def main():
	# prepare data
	flag=0
	gestureListener = GenerateTrainingSet()
	controller = Leap.Controller()
	controller.add_listener(gestureListener)
	time.sleep(2)
	print("heeyyyyyeyehbg")
	#message = socket.recv()
	#print("Received request: %s" % message)
	trainingSet=[]
	testSet=[]
	split = 0.67
	trainingSet=loadDataset('C:/Users/hp/Desktop/project/unityfinalproject/trainingSet.csv', split, trainingSet, testSet)
	predictions=[]
	k = 3

	"""gestureListener = GenerateTrainingSet()
	controller = Leap.Controller()
	ip1=gestureListener.captureGesture(controller)
	print(ip1)
	ip=[]
	ip=ip1.split(",")
	#print(ip)"""
	result=""
	li=[]
	print("do ur sign :")
	time.sleep(1)
	while result.upper()!="STOP":
		result = gestureListener.captureGesture(controller)
		ip=result.split(",")
		neighbors = getNeighbors(trainingSet, ip, k)
		result = getResponse(neighbors)
		texttospeech(result)
		li.append((result))
		#predictions.append(result)
		finalString="".join(li)
		if(result.upper()!="STOP"):
			print(repr(finalString) )
		else:
			print(repr(finalString[:len(finalString)-4]))
			#socket.send(bytes(repr(finalString[:len(finalString)-4])))
			texttospeech(repr(finalString[:len(finalString)-4]))
			flag=1;
		if flag==1:
			controller.remove_listener(gestureListener)
			return
		print("do ur sign :")
		#time.sleep(2)

		"""accuracy = getAccuracy(testSet, predictions)
		print('Accuracy: ' + repr(accuracy) + '%')"""

main()
