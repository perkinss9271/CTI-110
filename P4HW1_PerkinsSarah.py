#CTI-110
#P4HW1 - Score List
#Sarah Perkins
#November 22, 2023
#

#Get user input and place in list via loop#

my_list = []
Total_scores = int(input('How many scores do you want to enter?\n'))

num = 0
score = 1

while score <= Total_scores:
	print(f'Enter score #', score, ':\n')
	num = float(input())
	    
	if num < 0 or num > 100:
		print('INVALID Score entered!!!!')
		print('Score should be between 0 and 100')
		print('Enter score #', score, 'again:')
		num = float(input())
		my_list.append(num)
		score = score + 1
			
	else:
	    my_list.append(num)
	    score = score + 1

#Drop lowest score, find average of remaining and determine and display letter grade#

lowest = min(my_list)

print(' ')
print('------------Results------------')
print(f'Lowest Grade:       {min(my_list)}')

my_list.remove(min(my_list))

print(f'Modified List:      {my_list}')

Sum = float(sum(my_list))
Length = float(len(my_list))
Average_Grade = Sum / Length
print(f'Scores Average:            {Average_Grade:.2f}')

Grade = "F"

if Average_Grade >= 90.0:
	Grade = "A"
elif Average_Grade >= 80.0:
	Grade = "B"
elif Average_Grade >= 70.0:
	Grade = "C"
elif Average_Grade >= 60.0:
	Grade = "D"
else:
	Grade = "F"
	
print(f'Grade         : {Grade}')
print('----------------------------------------')
