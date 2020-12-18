
#Question
# Problem Statement-:  You have M questions and N seconds to complete a test. Each question has some points and takes some time to solve (which will be given as input). Find the maximum mark that can be scored by the student within the given time N.

# Sample test case:

# 4 // number of questions
# 10 // Total time to attend the test
# 1 2 // one mark question – 2 seconds to solve.
# 2 3 // two mark question – 3 seconds to solve.
# 3 5 // three mark question – 5 seconds to solve.
# 4 7 // 4 mark question – 7 seconds to solve.




#solution

m=int(input())
n=int(input())
question_with_second=list(tuple(map(int,input().split()))for j in range(m))
sorted_question=sorted(question_with_second)[::-1]
print(sorted_question)
grade=[]
for i in range(len(sorted_question)):
    p=n
    marks=0
    for j in range(i,len(sorted_question)):
        if sorted_question[j][1]<=p:
            marks=marks+sorted_question[j][0]
            p-=sorted_question[j][1]
    grade.append(marks)
print(max(grade))
