#--------------------------------------------------------------
#	Description: This is an example taken out of the book
# 	"Introduction to Automata Theory Languages and Computation 
#	2nd Edition"# John E. Hopcroft et al. and translated to python.
#	
#	It is an example of a function that may never print out
#	the string "hello, world" for certain. 
#	The way the program works is that it looks for solutions to
#	the problem x^n + y^n = z^n. If it finds one, it prints the
#	message "hello, world".
#	
#	We know for certain that given the input n = 2, the program
#	will output the message (many times). One such time it will
#	output the message is when it gets to x = 56, y = 90, and 
#	z = 106, because 56^2 + 90^2 = 11,236 and so does 106^2.
#	
#	However, if n > 2, the program never finds a triple (x, y, z)
#	of integers that satisfies the equation x^n + y^n = z^n.
#
#	The claim that there are no solutions to the equation
#	x^n + y^n = z^n for n > 2 was made by Pierre de Fermat
#	over 300 years ago: https://en.wikipedia.org/wiki/Fermat%27s_Last_Theorem.
#	
#	The proof to Fermat's last theorem was found somewhat recently.
#--------------------------------------------------------------

import math
import pdb

def main():
	# the n in x^n + y^n = z^n
	n = int(input("Enter a number: "));
	# total is divided by the integers x, y, and z
	total = 3
	while True:
		# start with x = 1
		x = 1;
		# x goes up to total minus 2
		while x <=total-2:
			y = 1;
			# y goes up to one less than what x has not 
			#  already taken from total
			while y <= total - x - 1:
				# z is what remains (between 1 and total
				#  minus 2)
				z = total-x-y
				a = math.pow(x,n)
				b = math.pow(y,n)
				c = math.pow(z, n)
				if (a + b == c):
					print "hello, world"
					print "x: %d" % x
					print "y: %d" % y
					print "z: %d" % z
					print "total: %d" % total
				y+=1
			x+=1
		total+=1;

if __name__ == "__main__":
    main()
#----------------------------------
# Example tables of how this works:
#	
# total: 3 (the least possible because, x, y, z are integers
#  greater than 0 and total is divided up between them)
# 	x 	y 	z
#	1	1	1
#
# total: 4
#	x 	y 	z
# 	1	1	2
#	1	2	1
#	2	1	1
#
# total: 5
#	x 	y 	z
# 	1 	1 	3
# 	1 	2 	2
# 	1 	3 	1
# 	2 	1 	2
# 	2 	2 	1
#	3 	1 	1
