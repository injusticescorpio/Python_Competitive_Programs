
# Unfair Game
# Time limit: 1000 ms
# Memory limit: 128 MB

# Alex and Ben have a set of NN integers, so they decided to play a game. The two players take turns playing, Alex being the first to move. This game is asymmetrical, as follows:

# When it's Alex's turn, he chooses any non-empty subset of numbers and removes them from the set.
# When it's Ben's turn, he chooses exactly one number and removes it from the set.
# The game ends when there are no numbers left in the set. Alex's goal is to maximize the sum of the numbers he chooses, while Ben just tries to minimize Alex's sum. Considering that both of them play optimally, you should compute the outcome of the game.

# Standard input
# The first line contains a single integer NN, the size of the set.

# The second line contains the NN values in the set.

# Standard output
# The output should contain a single number representing Alex's sum if they both play optimally.

# Constraints and notes
# 1 \leq N \leq 10^51≤N≤10 
# 5
 
# The values of the array will be between -10^9−10 
# 9
#   and 10^910 
# 9


# Input	Output	Explanation
# 5
# -1 2 10 -10 3
#14
# Alex chooses -1 2 3 10
# Ben chooses −10.
#5
# -5 2 -10 4 -7
# -1
# Alex chooses 2 and 4.
# Ben chooses −5.
# Alex chooses −7.
# Ben chooses −10.


def odd_even_index(li):
    odd_even_sum=[]
    p=sum(li[::2])
    q=sum(li[1::2])
    odd_even_sum.append(p)
    odd_even_sum.append(q)
    return odd_even_sum

def even_length(list1):
    if len(list1)%2==0:
        return True
    else:
        return False
m=int(input(''))
alex_score=[]

li=[int(i) for i in input().strip().split(' ')][:m]
sorted_li=sorted(li)[::-1]
sorted_li.append(0)

if (str(sorted_li).count('-')==len(sorted_li)-1):
    if even_length(sorted_li):
        negative_sum=sum(sorted_li[0:2])
        rest_of_numbers=sorted_li[2:]
        sum_of_restnumbers=odd_even_index(rest_of_numbers)
        for i in sum_of_restnumbers:
            alex_score.append(negative_sum+i)
    else:
        negative_sum=sorted_li[0]
        rest_of_numbers=sorted_li[1:]
        sum_of_restnumbers=odd_even_index(rest_of_numbers)
        for i in sum_of_restnumbers:
            alex_score.append(negative_sum+i)
else:
    positive_number_sum=sum(list(filter(lambda x:x>0,sorted_li)))
    rest_of_numbers=list(filter(lambda x:x<=0,sorted_li))
    if even_length(rest_of_numbers):
        new_positive_sum=positive_number_sum
        new_rest_of_numbers=rest_of_numbers
        sum_of_restnumbers=odd_even_index(new_rest_of_numbers)
        for i in sum_of_restnumbers:
            alex_score.append(new_positive_sum+i)
    else:
        new_positive_sum=positive_number_sum+rest_of_numbers[0]
        new_rest_of_numbers=rest_of_numbers[1:]
        sum_of_new_restnumbers=odd_even_index(new_rest_of_numbers)
        for i in sum_of_new_restnumbers:
            alex_score.append(new_positive_sum+i)

print(max(alex_score))

    




