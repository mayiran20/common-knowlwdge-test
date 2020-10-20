print("Title of program: Common Knowledge Test")
print()

counter = 0
score = 0
total_num_of_qn = 3


counter +=1
tracker = 0

while tracker !=1:
  
  print("Q"+str(counter)+") "+ "Who is the man on our money notes?")
  print("   a) Sir Stamford Raffles")
  print("   b) Mr Lee Hsien Loong?")
  print("   c) Yusof Ishak")
  print("   d) Donald Trump")
  answer = input("Your answer: ")
  answer = answer.lower()
  if answer == "a":
    output = "Wrong. He founded our nation ."
    score -=1
  elif answer == "b":
    output = "Wrong. He is our prime minister."
    score -=1
  elif answer == "c":
    output = "Yes, that's right!"
    tracker =1
    score +=1
  elif answer == "d":
    output = "Wrong. That's the president of USA!"
    score -=1
  else:
    output = "Please choose a, b, c or d only."
  
  print()
  print(output)
  print()
  print("Your current score: " + str(round((score/total_num_of_qn*100),1)) + "%"  )
  print()
  print()
  
counter +=1
tracker = 0

while tracker !=1:
  
  print("Q"+str(counter)+") "+ "What is the name of a baby kangaroo?")
  print("   a) child")
  print("   b) joey")
  print("   c) cub")
  print("   d) foal")
  answer = input("Your answer: ")
  answer = answer.lower()
  if answer == "a":
    output = "Wrong. Are you sure this is a name of a baby kangaroo?"
    tracker =1
    score -=1
  elif answer == "b":
    output = "Yes, that's right!"
    score +=1
  elif answer == "c":
    output = "Wrong. This name reminds me of something more furry."
    score -=1
    
  elif answer == "d":
    output = "Wrong. Are you sure this is a name of a baby kangaroo?"
    score -=1
  else:
    output = "Please choose a, b, c or d only."

  print()
  print(output)
  print()
  print("Your current score: " + str(round((score/total_num_of_qn*100),1)) + "%"  )
  print()
  print()
 
print("End of quiz!")
