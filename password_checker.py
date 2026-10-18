print("Password checker")
password = input("Enter an invented sample password: ")

if password == "":
	print("You entered an empty password.")
else:
	has_uppercase = False
	has_lowercase = False
	has_digit = False
	has_special = False

	for character in password:
		if character.isupper():
			has_uppercase = True
		if character.islower():
			has_lowercase = True
		if character.isdigit():
			has_digit = True
		if not character.isalnum():
			has_special = True

	checks_passed = 0

	if len(password) >= 12:
		print("Passed: at least 12 characters")
		checks_passed += 1
	else:
		print("Failed: at least 12 characters")

	if has_uppercase:
		print("Passed: an uppercase letter")
		checks_passed += 1
	else:
		print("Failed: an uppercase letter")

	if has_lowercase:
		print("Passed: a lowercase letter")
		checks_passed += 1
	else:
		print("Failed: a lowercase letter")

	if has_digit:
		print("Passed: a digit")
		checks_passed += 1
	else:
		print("Failed: a digit")

	if has_special:
		print("Passed: a special character")
		checks_passed += 1
	else:
		print("Failed: a special character")

	print("Score:", checks_passed, "out of 5")
	print("Passing these checks does not guarantee that a password is secure.")
