#!/usr/bin/env python3

from person import Person
from person import fib

def main():
	f = Person(5)
	print(f.get())
	f.set(7)
	print(f.get())
	print(fib())

if __name__ == '__main__':
	main()
