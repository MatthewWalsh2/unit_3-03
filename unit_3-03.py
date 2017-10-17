# Created by Matthew Walsh
# Created on oct 2017
# Created for ICS3U
# this program plays rock paper scissors

import ui
from numpy import random




computer_choice = random.randint(1, 3)


def check_answer_button(sender):
	
	selected_control = view['user_answer_control'].selected_index
	
	if selected_control == 0:
		user_answer = str('rock')
	elif selected_control == 1:
		user_answer = str('paper')
	elif selected_control == 2:
		user_answer = str('scisors')
	
	#print user_answer
	
	if computer_choice == 1:
	  computer_answer = str('rock')
	elif computer_choice == 2:
	  computer_answer = str('paper')
	elif computer_choice == 3:
	  computer_answer = str('scisors')
	
	#print computer_answer
	
	if computer_answer == user_answer:
		view['answer_label'].text = "You have tied"
	elif user_answer == str('rock') and computer_answer == str('scisors'):
		view['answer_label'].text = "You have won"
	elif user_answer == str('paper') and computer_answer == str('rock'):
		view['answer_label'].text = "You have won"
	elif user_answer == str('scisors') and computer_answer == str('paper'):
		view['answer_label'].text = "You have won"
	elif user_answer == str('paper') and computer_answer == str('scisors'):
		view['answer_label'].text = "You have lost"
	elif user_answer == str('rock') and computer_answer == str('paper'):
		view['answer_label'].text = "You have lost"
	elif user_answer == str('scisors') and computer_answer == str('rock'):
		view['answer_label'].text = "You have lost"



view = ui.load_view()
view.present('full_screen')
