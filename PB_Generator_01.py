import random

MyList = []
i = 0

while i < 1001:
	'-- Create List of five random Guesses'
	Num_Possibilities = list(range(1,70))
	Guesses = random.sample(Num_Possibilities, k=5)

	'-- Guess PowerBall Number'
	PB = list(range(1,27))
	Single_PB = random.sample(PB, k=1)

	print (i, " Guesses:" , Guesses, "  PowerBall: ", Single_PB)

	MyList.append(Guesses)
	#final_string = '\n'.join(MyList)

	i += 1

#print(MyList)