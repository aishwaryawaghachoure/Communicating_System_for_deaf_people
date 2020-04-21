import speech_recognition as sr
import sys;
r=sr.Recognizer();
import time
import zmq

context = zmq.Context()
#print("cotext")
socket = context.socket(zmq.REP)
socket.bind("tcp://*:5555")
#print("craeted socket")
	

"""if len(sys.argv)==2:
    filename = sys.argv[1];
    with sr.AudioFile(filename) as source:
        audio=r.listen(source);
else:
    with sr.Microphone() as source:
        audio=r.listen(source);
try:
    print(r.recognize_google(audio));
except Exception as e:
    pass"""


from sys import byteorder
from array import array
from struct import pack

import pyaudio
import wave

THRESHOLD = 1000
CHUNK_SIZE = 1024
FORMAT = pyaudio.paInt16
RATE = 44100
from pymongo import MongoClient
connection = MongoClient("localhost", 27017)
if connection:
	#print("connection established successfully")
	db = connection.textimagesdb                        
	if db:
		print('connected to database textimagesdb')

def is_silent(snd_data):
    "Returns 'True' if below the 'silent' threshold"
    return max(snd_data) < THRESHOLD

def normalize(snd_data):
    "Average the volume out"
    MAXIMUM = 16384
    times = float(MAXIMUM)/max(abs(i) for i in snd_data)

    r = array('h')
    for i in snd_data:
        r.append(int(i*times))
    return r

def trim(snd_data):
    "Trim the blank spots at the start and end"
    def _trim(snd_data):
        snd_started = False
        r = array('h')

        for i in snd_data:
            if not snd_started and abs(i)>THRESHOLD:
                snd_started = True
                r.append(i)

            elif snd_started:
                r.append(i)
        return r

    # Trim to the left
    snd_data = _trim(snd_data)

    # Trim to the right
    snd_data.reverse()
    snd_data = _trim(snd_data)
    snd_data.reverse()
    return snd_data

def add_silence(snd_data, seconds):
    "Add silence to the start and end of 'snd_data' of length 'seconds' (float)"
    r = array('h', [0 for i in xrange(int(seconds*RATE))])
    r.extend(snd_data)
    r.extend([0 for i in xrange(int(seconds*RATE))])
    return r

def record():
    
    p = pyaudio.PyAudio()
    stream = p.open(format=FORMAT, channels=1, rate=RATE,
        input=True, output=True,
        frames_per_buffer=CHUNK_SIZE)

    num_silent = 0
    snd_started = False

    r = array('h')

    while 1:
        # little endian, signed short
        snd_data = array('h', stream.read(CHUNK_SIZE))
        if byteorder == 'big':
            snd_data.byteswap()
        r.extend(snd_data)

        silent = is_silent(snd_data)

        if silent and snd_started:
            num_silent += 1
        elif not silent and not snd_started:
            snd_started = True

        if snd_started and num_silent > 80:
            break

    sample_width = p.get_sample_size(FORMAT)
    stream.stop_stream()
    stream.close()
    p.terminate()

    #r = normalize(r)
    #r = trim(r)
    r = add_silence(r, 0.5)
    return sample_width, r

def record_to_file(path):
    "Records from the microphone and outputs the resulting data to 'path'"
    sample_width, data = record()
    data = pack('<' + ('h'*len(data)), *data)

    wf = wave.open(path, 'wb')
    wf.setnchannels(1)
    wf.setsampwidth(sample_width)
    wf.setframerate(RATE)
    wf.writeframes(data)
    wf.close()

def performspeechtosign():
	while True:
		message = socket.recv()
		#print("Received request: %s" % message)
		
		print("please speak a word into the microphone")
		record_to_file('demo.wav')
		#print("done - result written to demo.wav")
		with sr.AudioFile('demo.wav') as source:
			audio=r.listen(source);
		try:
			spokenwords=r.recognize_google(audio)
			print(spokenwords);
			socket.send(bytes(spokenwords))
		except Exception as e:
			print("exception"+e);
			#socket.send(bytes(e))
		#socket.send(bytes("abc"))
		message = socket.recv()
		#print("Received request: %s" % message)
		urls=[]
		try:
			words=spokenwords.split(" ")
			for word in words:
				print(word+" ")
				results = db.ISL.find({'word':word},{'url':1,'_id':0});
				for i in results: 
					url=str(i)[11:-2]
					print(url)
					urls.append(url)
		except Exception as e:
			print("exception"+e);
			socket.send(bytes(e))
		#print("sending")
		#socket.send(bytes("asdf"))
		#msg=socket.recv()
		socket.send(bytes(urls))
		return	

performspeechtosign()


