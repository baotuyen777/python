from sys  import argv
script,filename =argv

print "We're going to erase %r." % filename
print "If you don't want that,hit Ctr+C"
print "If you do want that, hit return"

raw_input("?")

print "Opeaning the file..."
target = open(filename,"w")

print "Truncating the file. Goodbye!"
target.truncate()

print "Now I'm going to ask you for three lines."

line1 =raw_input("Line 1: ")
line2=raw_input("line2: ")
line3=raw_input("line3: ")

print "I'm goting to write these to file."

target.write(line1)
target.write("\n")
target.write(line2)
target.write("\n")
target.write(line3)
target.write("\n")


print "And finaly,we close it."
target.close()