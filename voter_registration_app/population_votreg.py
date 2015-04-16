import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'voter_registration_app.settings')

import django
django.setup()

from votreg.models import State, Page


def populate():
	states_name = ["ALABAMA", "ALASKA", "ARIZONA", "ARKANSAS", "CALIFORNIA", "COLORADO", "CONNECTICUT", "DELAWARE", "FLORIDA", "GEORGIA", "HAWAII", "IDAHO", "ILLINOIS", "INDIANA", "IOWA", "KANSAS", "KENTUCKY", "LOUISIANA", "MAINE", "MARYLAND", "MASSACHUSETTS", "MICHIGAN", "MINNESOTA", "MISSISSIPPI", "MISSOURI", "MONTANA", "NEBRASKA", "NEVADA", "NEW HAMPSHIRE", "NEW JERSEY","NEW MEXICO", "NEW YORK", "NORTH CAROLINA", "NORTH DAKOTA", "OHIO", "OKLAHOMA", "OREGON", "PENNSYLVANIA","RHODE ISLAND", "SOUTH CAROLINA", "SOUTH DAKOTA", "TENNESSEE", "TEXAS", "UTAH", "VERMONT", "VIRGINIA", "WASHINGTON", "WEST VIRGINIA", "WISCONSIN", "WYOMING"]
	# import pdb; pdb.settrace()
	for s in states_name:
		
		c = create_state(s)
		create_page(states=c, title = "Registration Information")
		create_page(states=c, title = "Military and Overseas User")
		create_page(states=c, title = "Absentee Ballot")
		create_page(states=c, title = "FAQs")


def create_page(states, title):
	p = Page.objects.get_or_create(states=states, title = title)[0]
	p.save()
	return p
def create_state(name):
	c = State.objects.get_or_create(name=name)[0]
	return c

# if __name__ = '__main__':
# 	print "Starting VotReg population script..."
populate()