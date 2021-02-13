import ipaddress
mini_list=[line.rstrip() for line in open("mini.txt")]
main_list=[line.rstrip() for line in open("main.txt")]

mini_list_ipv4object =[]
main_list_ipv4object =[]

for items in mini_list:
	if "/" in items:
		mini_list_ipv4object.append(ipaddress.ip_network(items))
	else: #FRR classful networklerde subnet bilgisini vermiyor
		if  int(items.split(".")[0]) >= 192:
			items = items+"/24"
		elif int(items.split(".")[0]) >= 128 and  int(items.split(".")[0]) <= 191:
			items=items+"/16"
		elif int(items.split(".")[0]) <= 126:
			items=items+"/16"
		else:
			continue
		mini_list_ipv4object.append(ipaddress.ip_network(items))

for items in main_list:
	if "/" in items:
		main_list_ipv4object.append(ipaddress.ip_network(items))
	else: #FRR classful networklerde subnet bilgisini vermiyor
		if  int(items.split(".")[0]) >= 192:
			items = items+"/24"
		elif int(items.split(".")[0]) >= 128 and  int(items.split(".")[0]) <= 191:
			items=items+"/16"
		elif int(items.split(".")[0]) <= 126:
			items=items+"/16"
		else:
			continue
		main_list_ipv4object.append(ipaddress.ip_network(items))
		
in_list=[]
not_in_list=[]

for mini in mini_list_ipv4object:
	success=0
	for main in main_list_ipv4object:
		if mini.subnet_of(main):
			success=1
			continue
	if success==1: 
		in_list.append(mini.with_prefixlen)
	else:
		not_in_list.append(mini.with_prefixlen)
			
print ("------MINI LIST PREFIXES THAT ARE FOUND IN MAIN LIST--------")			
for item in in_list:
	print (item)
print ("-------MINI LIST PREFIXES THAT ARE NOT FOUND IN MAIN LIST----------")
for item in not_in_list:
	print (item)
			