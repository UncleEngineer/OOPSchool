# -*- coding: utf-8 -*-
# newschool.py

import school
from school import Student,SpecialStudent
from school import * # * is import all

def Test():
	'''
	นี่คือตัวอย่างการเขียนโปรแกรมโดยใช้แพ็คเกจนี้
	st1 = school.Student('Albert','Einstein')
	print(st1)

	st2 = Student('Bill','Gates')
	print([st2])

	stp1 = SpecialStudent('T','E','P')

	teacher1 = Teacher('Ada')
	print(teacher1.fullname)
	'''
	st1 = school.Student('Albert','Einstein')
	print(st1)

	st2 = Student('Bill','Gates')
	print([st2])

	stp1 = SpecialStudent('T','E','P')

	teacher1 = Teacher('Ada')
	print(teacher1.fullname)