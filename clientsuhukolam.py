import random,redis,time

ip = '127.0.0.1'
port = 6379
#s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
#s.connect((ip,port))
n = 25
sensor = []
r = redis.Redis(ip)
##############GENERATING 100 TEMPERATURE SENSOR VALUE###############
while True:
	for i in range(n):
		random.seed(30)
		value = random.randint(1,50)
		sensor.append(value)
		value = random.randint(1,50)
		sensor.append(value)
		random.seed(35)
		value = random.randint(1,50)
		sensor.append(value)
		value = random.randint(1,50)
		sensor.append(value)
	for i in range (100):
		r.set("kolam"+str(i),sensor[i])
	print(sensor)
	time.sleep(300)