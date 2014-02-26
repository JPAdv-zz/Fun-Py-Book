"""
A program that gets the second letter from a set of words within a string
and reverses those found letters.

Example:
	input:
		"I would like to order a very good book of Python Fundamentals"
	output:
		"uyfooeroio"

@Author: Jose Padilla
"""

def secondLetterFromWord(word):
	"""
	A function that gets the second letter of a word from a given string.
	"""
	result = "" 
	for w in word.split():
		result += w[1:2]
	return result

def reverse(word):
	"""
	A function that reverses a string.
	"""
	result = ""
	size = len(word) - 1
	while (size >= 0):
		result += word[size]
		size -= 1
	return result

def main():
	"""
	The main program.
	"""
	expected = "uyfooeroio"
	testString = "I would like to order a very good book of Python Fundamentals"
	print "Expected: ", expected
	result = reverse(secondLetterFromWord(testString))
	print "Result:   ", result


if __name__ == '__main__':
	main()