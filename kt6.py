


#transfer statement
#break 
numbers = [1,2,3,4,5]
for  number in numbers:
  if number == 4:
    break 
print(number)

for i in range (1, 4):
  for j in range (1,4):
    if i == 2 and j == 3:
      break
    print(i,j)
    print("inner loop ended")



    
#continue 

for i in range (1, 4):
  for j in range (1, 4):
    if i == j:
      continue #skip when i and j are equal 
    print(i, j)


    found_iteam = False
    iteams = ["apple", "grape", "cherry"]
    search_iteam = "grape"
for iteam  in iteams :
  if iteam == search_iteam:
    found_iteam = True
    break #exit the loop if the iteam is found
  else:
    continue # skip to the next iteam if not found
  if found_iteam:
    print("iteam found!")
else:
  print("iteam not found")





#pass
for i in range (1,4):
  if i == 3:
   pass #skip something when i is 3
  else:
    print(i)  
    


