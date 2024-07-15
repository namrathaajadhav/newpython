#flow control statement 
#conditional statement 
age = 20
if age >= 18:
 print("you are eligible to vote.")  
else:
 print("you are not eligible to vote.") 
 



 grade = 85
 if grade >= 90:
  print("excellent! you earned an A.")
 elif grade >= 80:
  print("great job! you earned a B.")
 else:
  print("you earned a C. study more for next exam.")
  



traffic_light = "red"
if traffic_light == "red":
       print("stop! the light is red.")
elif traffic_light == "yellow":
      print("caution! the light is yello, prepare to stop.") 
else: # assuming "green is the only other valid state"
    print("go! the light is green.")




#transfer statement
#break 
numbers = [1,2,3,4,5]
for  number in numbers:
  if number == 4:
    break 
    print(number)
    


#continue
#pass











#iterative 


user_input = int(input("enter a number:"))
for number in range (1,11):
 print(user_input * number)
 

i = 0
while i <= 5:
 print(i)
i = i + 1
print("finishe")










 


