from django.core.exceptions import ValidationError
import re

def validate_email(value):
	pattern = "^\S+@\S+\.\S+$"
	objs = re.search(pattern, value)
	if objs == None:
		raise ValidationError("Email is not valid")
	return value

def validate_message(value):
	pattern = r".{1,100}$"
	objs = re.match(pattern, value)
	if objs == None:
		raise ValidationError("Message can't be blank or bigger than 100 chars")
	return value