#maths avarage marks for students
student = input("Enter your Name and Surname: ")
mark1 = int(input("Please enter mark one: "))
total = int(input("please entre out of how much: "))
mark2 = int(input("Please enter mark two: "))
total2 = int(input("please entre out of how much: "))
mark3 = int(input("Please enter mark three: "))
total3 = int(input("please entre out of how much: "))

result = ((mark1 / total) + (mark2 / total2) + (mark3 / total3))/3 * 100

if result >= 50:
    print("Test passed")

else:
    print("Test failed")
print(result)

from datetime import datetime, timedelta

today = datetime.today()

#print 10 days ,two weeks apart
for d in range(10):
    new_date = today + timedelta(days=14)
    today = new_date
    print(today.strftime("%Y :%m : %d"))
