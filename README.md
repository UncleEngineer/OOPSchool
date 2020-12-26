# (OOP School) ไลบรารี่สำหรับใช้เรียน Python OOP by Uncle Engineer

PyPi: https://pypi.org/project/oopschool/

Python OOP+ วิธีสร้าง Library เป็นของตัวเอง+ อัพโหลด Package ไปยัง PyPI.org

โปรแกรมนี้ลุงใช้สำหรับสอนการเขียนโปรแกรมแบบ OOP สามารถดูตัวอย่างคลิปวิดีโอที่สอนได้ใน: https://youtu.be/1egtTXUJ3-4

### วิธีติดตั้ง

เปิด CMD / Terminal

```python
pip install oopschool
```

### วิธีใช้งานแพ็คเพจนี้

- เปิด IDLE ขึ้นมาแล้วพิมพ์...

```python
from oopschool import Student,Tesla,SpecialStudent,Teacher
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
```

พัฒนาโดย: ลุงวิศวกร สอนคำนวณ
FB: https://www.facebook.com/UncleEngineer
YouTube: https://www.youtube.com/UncleEngineer
