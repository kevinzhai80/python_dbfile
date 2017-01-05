bob = {'name':'Bill','age':46,'pay':1000000,'job':'ceo'}
sue = {'name':'Sue','age':32,'pay':100000,'job':'dev'}
kevin = {'name':'Kevin','age':36,'pay':200000,'job':'hardware'}

db = {}
db['bob'] = bob
db['sue'] = sue
db['kevin'] = kevin

if __name__ == '__main__':
	for key in db:
		print(key,'=>',db[key])
