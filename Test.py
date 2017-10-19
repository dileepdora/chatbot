import facebookbot as fbbot

def user_input():
	while True:
		user_input = raw_input("Enter something: ")
		if user_input == "quit":
			print "stopping XtremeChamps AI Engine !!! "
			break
		else:
			print "resp ",fb.parse_user_message(user_input)
			

if __name__ == '__main__':
    user_input()




