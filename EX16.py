from sys import argv

script, filename = argv

print "We're going to erase %r." %filename
print "If you don't want that, hit CTRL-C (^C) ."
print "If you do want that, hit RETURN."

raw_input("?")

print "Opening the file...."
target = open(filename, 'w')

print "Truncating the file.   Goobye!"
target.truncate()

print "Now I'm going to ask you for three lines. "

line1 = raw_input("Line 1:")
line2 = raw_input("Line 2:")
line3 = raw_input("Line 3:")

print "I'm going to write these to te file."

target.write(line1)
target.write("\n")
target.write(line2)
target.write("\n")
target.write(line3)
target.write("\n")


print "And Finally, we close it."
target.close()
