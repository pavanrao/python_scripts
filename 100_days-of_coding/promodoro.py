from datetime import datetime
from datetime import timedelta 
import time
'''
100 days of coding - day 1
Script by Pavan Rao

From Wikipedia article on Promodoro technique: 

There are six steps in the original technique:
    Decide on the task to be done.
    Set the pomodoro timer (traditionally to 25 minutes)
    Work on the task.
	End work when the timer rings and put a checkmark on a piece of paper.[5]
    If you have less than four checkmarks, take a short break (3–5 minutes), then go to step 2.
    After four pomodoros, take a longer break (15–30 minutes), reset your checkmark count to zero, then go to step 1.
'''

#TODO: time lengths could be input parameters to the program
#task_length = timedelta(minutes = 25)
#break_length = timedelta(minutes = 5)
#long_break = timedelta(minutes = 15)

task_length, break_length, long_break = (25, 5, 15)

def task_timer(task_length, task_type):
	'''
	Input: lenght of time to sleep, in seconds
	Before going to sleep, user is given an option to exit the program
	'''
	if(input("Press x to exit, any other key to start {0}.\n"\
		.format(task_type)).lower()== "x"): 
		exit(0)
	else:
		while task_length > 0:			
			print("#", end='')			
			task_length -= 1
			time.sleep(1)
		print(" Done! \n")



def progress_bar(length):
	'''
	TODO: Implement a progress bar that increases with each minute
	This method is not used currently
	'''
	#print("\n"*100)
	print("#"*length, end='')
	if length == task_length:
		print(" Done!")
	else: 
		print("\n")

def main():
	print("\n \
		Prodoro timer for {0} minutes \n \
		short break of {1} minutes  \n \
		long break of {2} minutes\n \n \
		".format(task_length, break_length, long_break))


	promodoro_count = 0

	while True:

			promodoro_count+=1
			print("Do you want to start Promodoro no. {0} for {1} mins?"\
				.format(promodoro_count, task_length))
			task_timer(task_length, "task")
			if promodoro_count > 0 and promodoro_count%4 ==0:
				print("Good job! Time for a long break")
				task_timer(long_break, "long break")
			else:
				print("Time for a short break")
				task_timer(break_length, "short break")




if __name__ == '__main__':
	main()
