#!/usr/bin/env python
__author__      = "hygoh2k@gmail.com"

from random import randint




def main():

	_number_of_guess = 1000000
	_number_of_first_guess_failed = 0
	_number_of_remain_hit = 0
	_number_of_remain_miss = 0
	_number_of_switch_hit = 0
	_number_of_switch_miss = 0

	print("montly hall simulation")
	print("guess  " + str(_number_of_guess) + " times...")

	for x in xrange(0,_number_of_guess ):
		
		door_has_car = randint(1,3)
		randomly_selected_door = random_open_a_door();
		randomly_selected_another_door = random_choose_a_door_with_exception(randomly_selected_door)

		print(door_has_car)
		print(randomly_selected_door)
		print(randomly_selected_another_door)
		if(randomly_selected_another_door == door_has_car):
			print("car is in other door, no luck in your first draw.")
			_number_of_first_guess_failed = _number_of_first_guess_failed + 1

		else:
			print ("looks like you have chance! now we test for 2 approaches!")
			if(randomly_selected_door == door_has_car):
				print("consistency is the key!")
				_number_of_remain_hit = _number_of_remain_hit + 1
			else:
				print("why don't you just change!")
				_number_of_remain_miss = _number_of_remain_miss + 1

			choice = [1,2,3]
			choice.remove(randomly_selected_door)
			choice.remove(randomly_selected_another_door)
			print("switch the door to " + str(choice))
			if(choice[0]== door_has_car):
				print("switch works!")
				_number_of_switch_hit = _number_of_switch_hit + 1
			else:
				print("switch doesn't work!")
				_number_of_switch_miss = _number_of_switch_miss + 1



	print("summary:")
	print("total guess:" + str(_number_of_guess))
	print("first guess failed:" + str(_number_of_first_guess_failed))
	print("remain hit:" + str(_number_of_remain_hit))
	print("remain missed:" + str(_number_of_remain_miss))
	print("switch hit:" + str(_number_of_switch_hit))
	print("switch miss:" + str(_number_of_switch_miss))
	





def random_open_a_door():
	random_guess = randint(1,3)
	return random_guess;

def random_choose_a_door_with_exception(exception_number):
	choice = [1,2,3]
	choice.remove(exception_number)
	return choice[randint(0,1)]


def second_guess_with_switch(exception_number):
	return random_choose_a_door_with_exception(exception_number)




if __name__ == "__main__":
	main()

