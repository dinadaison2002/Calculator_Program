student_name = input("Enter your name :")
subject_1 =int(input("Enter your mark in subject_1 :"))
subject_2 =int(input("Enter your mark in subject_2 :"))
subject_3 =int(input("Enter your mark in subject_3 :"))

if((0<=subject_1<=100)and(0<=subject_2<=100)and(0<=subject_3<=100)):
  total = subject_1+subject_2+subject_3
  percentage = (total/300)*100
  if percentage >=75:
   grade = "A"
  elif percentage >=60:
   grade = "B"
  elif percentage >=40:
   grade = "C"
  else:
   grade = "F"

  print(student_name)
  print(f"Total : {total} / 300")
  print(f"Percentage : {percentage:.1f}%")
  print("Grade :", grade)
else:
 print("please enter your mark between 0 to 100")


