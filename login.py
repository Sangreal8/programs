import sys
check = True

choice = raw_input("Select option 1 to login." + "\n" + "Select option 2 to create an account." +"\n")

if float(choice) == 1:
	print "Login woo"

#account creation process
elif float(choice) == 2:
	with open('users.txt', 'a') as f:
		#opens file for appending to it
		username = raw_input("Please enter a user name:" + "\n")
		password = raw_input("Please enter a password:" + "\n")
		
		with open('users.txt', 'r') as check:
			#opens file to read current users & passwords
			lines = check.readlines()
			for token in lines:
				token = token.split(".")
				if username != token[0]:
					check = True
					pass
				elif username == token[0]:
					print "Please enter a unique user name."
					check = False
					break		
			if check == True:			
				f.write(username)
				f.write(".")
				f.write(password)
				f.write("\n")
				print "Your account has been created!"

elif float(choice) != 1 and 2:
	print "Please select either 1 or 2."

