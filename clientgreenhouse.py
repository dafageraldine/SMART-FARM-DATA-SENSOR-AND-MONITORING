	import random,redis,json
	from datetime import datetime
	from time import sleep

	#########ipportvm
	# ip = ''
	# port = 
	n = 25
	sensor = []
	sensorp = []
	r = redis.Redis()
	m = [] #arrayforjson

	#########GENERATING 100 TEMPERATURE SENSOR VALUE#########
	while True:
		now = datetime.now()
		time = now.strftime("%d/%m/%Y %H:%M:%S")
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
	#############GENERATING 100 PH SENSOR VALUE##############
		for i in range(n):
			random.seed(5)
			value2 = random.randint(1,7)
			sensorp.append(value2)
			value2 = random.randint(1,7)
			sensorp.append(value2)
			random.seed(3)
			value2 = random.randint(1,7)
			sensorp.append(value2)
			random.seed(1)
			value2 = random.randint(1,7)
			sensorp.append(value2)
	######################MAKINGJSONFILE#####################
		for i in range(100):
			x = {
			"sid"   : "gh"+str(i+1),
			"val1"  : sensor[i],
			"val2"  : sensorp[i],
			"ts"    : time
			}
			y = json.dumps(x)
			#GH means gHouse
			r.set("GH"+str(i+1),y)
		#l = json.loads(r.get("GH5"))##ifyouwanttoloadthejson
		#print(l["ts"])#printvalueofval1fromloadedjson
		sleep(300)