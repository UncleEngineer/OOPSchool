# school.py

class Student:
	def __init__(self,name,lastname):
		self.name = name
		self.lastname = lastname
		self.exp = 0 # คะแนนประสบการณ์
		self.lesson = 0 # จำนวนคลาสที่เคยเรียน
		self.vehicle = 'รถเมลล์'

	@property
	def fullname(self):
		return '{} {}'.format(self.name, self.lastname)

	def Coding(self):
		'''นี่คือคลาสเรียนวิชาเขียนโปรแกรม'''
		self.AddEXP()
		print('{} กำลังเรียนเขียนโปรแกรม...'.format(self.fullname))

	def ShowEXP(self):
		print('{} ได้คะแนน {} exp (เรียนไป {} ครั้ง )'.format(self.name,self.exp,self.lesson))

	def AddEXP(self):
		self.exp += 10  # self.exp = self.exp + 10
		self.lesson += 1 # self.lesson = self.lesson + 1

	def __str__(self):
		return self.fullname

	def __repr__(self):
		return self.fullname

	def __add__(self,other):
		return self.exp + other.exp


class Tesla:
	def __init__(self):
		self.model = 'Tesla Model S'

	def SelfDriving(self,st):
		print('ระบบขับอัตโนมัติกำลังทำงาน...กำลังพาคุณ{}กลับบ้าน!'.format(st.name))

	def __str__(self):
		return self.model


class SpecialStudent(Student):
	def __init__(self,name,lastname,father):
		super().__init__(name,lastname)

		self.father = father
		self.vehicle = Tesla()
		print('รู้ไหมฉันลูกใคร?..!พ่อฉันชื่อ {}'.format(self.father))

	def AddEXP(self):
		self.exp += 30
		self.lesson += 2


class Teacher:
	def __init__(self,fullname):
		self.fullname = fullname
		self.students = []

	def CheckStudent(self):
		print('----นักเรียนของคุณครู{}----'.format(self.fullname))
		for i,st in enumerate(self.students):
			print('{}-->{} [{} exp][เรียนไป {} ครั้ง]'.format(i+1, st.fullname, st.exp, st.lesson))

	def AddStudent(self,st):
		self.students.append(st)


# print('FILE:', __name__)

if __name__ == '__main__':
	
	# Day 0
	allstudent = []

	teacher1 = Teacher('Ada Lovelace')
	teacher2 = Teacher('Bill Gates')
	print(teacher1.students)

	# Day 1
	print('-----Day 1----')
	st1 = Student('Albert','Einstein')
	allstudent.append(st1) #สมัครเสร็จเก็บไว้ในลิสต์นักเรียนทันที
	teacher2.AddStudent(st1)
	print(st1.fullname)

	# Day 2
	print('-----Day 2----')
	st2 = Student('Steve','Jobs')
	allstudent.append(st2)
	teacher2.AddStudent(st2)
	print(st2.fullname)

	# Day 3
	print('-----Day 3----')
	for i in range(3):
		st1.Coding()

	st2.Coding()
	st1.ShowEXP()
	st2.ShowEXP()

	# Day 4
	print('-----Day 4----')

	stp1 = SpecialStudent('Thomas','Edison','Hitler')
	allstudent.append(stp1)
	teacher1.AddStudent(stp1)
	print(stp1.fullname)
	print('คุณครูครับ ขอคะแนนฟรีสัก 20 คะแนนได้ไหม')
	stp1.exp = 20 # แก้ไขค่าในคลาสได้
	stp1.Coding()
	stp1.ShowEXP()

	# Day 5
	print('-----Day 5----')
	print('นักเรียนกลับบ้านยังไงจ๊ะ?')
	print(allstudent)
	for st in allstudent:
		print('ผม: {} กลับบ้านด้วย {} ครับ'.format(st.name,st.vehicle))
		if isinstance(st,SpecialStudent):
			st.vehicle.SelfDriving(st)
	# Day 6
	print('-----Day 6----')

	teacher1.CheckStudent()
	teacher2.CheckStudent()

	print('รวมพลังของนักเรียน 2 คน ', st1 + st2 )