import random
examScoreDict={}
maxScoreStudentDict={}
roll_no=100
while(roll_no>0):
      examScore = random.randint(1,roll_no)
      examScoreDict[roll_no]=examScore
      roll_no-=1
print("Exam score Dict ",examScoreDict)
all_values = examScoreDict.values()
max_score = max(all_values)
print("Maximum available score in the dict " ,max_score)
for x in examScoreDict:
      if(examScoreDict[x]==max_score):
          maxScoreStudentDict[x]=max_score
print("List of Students with Max score " ,maxScoreStudentDict)
   

