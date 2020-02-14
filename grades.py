hw = int(input("please enter homework grade"))
ass = int(input("please enter assesment grade"))
exam = int(input("please enter exam grade"))
name = input("enter your name")

total = hw + ass + exam

def get_grade(mark):
	if mark> 125:
		return "A"
	elif mark >100:
		return "B"
	elif mark >75:
		return "C"
	else:
		return "fail"
print("%s got the following grade %s" %(name, get_grade(total)))
	

