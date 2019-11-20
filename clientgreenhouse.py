import socket,random,redis,time

#ip = '127.0.0.2'
#port = 3128
#s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
#s.connect((ip,port))
n = 25
sensor = []
r = redis.Redis()

##############GENERATING 100 TEMPERATURE SENSOR VALUE###############
while True:
	for i in range(n):
		random.seed(40)
		value = random.randint(1,50)
		sensor.append(value)
		value = random.randint(1,50)
		sensor.append(value)
		random.seed(40)
		value = random.randint(1,50)
		sensor.append(value)
		random.seed(30)
		value = random.randint(1,50)
		sensor.append(value)
	#GH means gHouse
	for i in range (100):
		r.set("GH"+str(i),sensor[i])
	time.sleep(300)