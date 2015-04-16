from django import forms
from votreg.models import ChooseState, Category

MY_CHOICES = (
    ('1', 'Alabama'),
    ('2', 'Alaska'),
    ('3', 'Arizona'),
    ('3', 'Arkansas'),
    ('3', 'California'),
    ('3', 'Colorado'),
    ('3', 'Connecticut'),
    ('3', 'Delaware'),
    ('3', 'Florida'),
    ('3', 'Georgia'),
    ('3', 'Hawaii'),
    ('3', 'Idaho'),
    ('3', 'Illinois'),
    ('3', 'Indiana'),
    ('3', 'Iowa'),
    ('3', 'Kansas'),
    ('3', 'Kentuky'),
    ('3', 'Louisiana'),
    ('3', 'Maine'),
    ('3', 'Maryland'),
    ('3', 'Massachusetts'),
    ('3', 'Michigan'),
    ('3', 'Minnesota'),
    ('3', 'Mississippi'),
    ('3', 'Missouri'),
    ('3', 'Montana'),
    ('3', 'Nebraska'),
    ('3', 'Nevada'),
    ('3', 'New Hampshire'),
    ('3', 'New Jersey'),
    ('3', 'New Mexico'),
    ('3', 'New York'),
    ('3', 'North Carolina'),
    ('3', 'North Dakota'),
    ('3', 'Ohio'),
    ('3', 'Oklahoma'),
    ('3', 'Oregon'),
    ('3', 'Pennsylvania'),
    ('3', 'Rhode Island'),
    ('3', 'South Carolina'),
    ('3', 'South Dakota'),
    ('3', 'Tennessee'),
    ('3', 'Texas'),
    ('3', 'Utah'),
    ('3', 'Vermont'),
    ('3', 'Virginia'),
    ('3', 'Washington'),
    ('3', 'West Virginia'),
    ('3', 'Wisconsin'),
    ('3', 'Wyoming'),
    
)
    
class MyForm(forms.Form):
    my_choice_field = forms.ChoiceField(choices=MY_CHOICES)