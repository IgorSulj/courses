from django.forms import *


class GitForm(Form):
    login = CharField(max_length=150)
