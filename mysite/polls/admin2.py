from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.models import User

from .models import Question, Choice

import djadmin2

class UserAdmin2(djadmin2.ModelAdmin2):
    # Replicates the traditional admin for django.contrib.auth.models.User
    create_form_class = UserCreationForm
    update_form_class = UserChangeForm


#  Register each model with the admin
djadmin2.default.register(Question)
djadmin2.default.register(Choice)
djadmin2.default.register(User, UserAdmin2)
