filename = 'people-file'
ENDDB = 'enddb.'
ENDREC = 'endrec.'
RECSEP = '=>'
def storeDB(db, filename=filename):
	dbfile = open(filename,'w')
	if (dbfile == None):
		print("Open database file failed!")
	for key in db:
		print(key,file=dbfile)
		for (name,value) in db[key].items():
			print(name + RECSEP + repr(value),file=dbfile)
		print(ENDREC,file=dbfile)
	print(ENDDB,file=dbfile)
	dbfile.close()

if __name__ == '__main__':
	from initdata import db
	storeDB(db)
