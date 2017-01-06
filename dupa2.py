from sys import argv
script, filename=argv



txt=open(filename)
infile=txt.read()
print "Here's your file %r" %filename
print "It's this long: %r" %len(infile)
print txt.read()
txt.close()

def pusty_wydruk():
	print "Nic tu nie ma"

pusty_wydruk()