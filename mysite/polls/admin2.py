from .models import Question, Choice

import djadmin2

#  Register each model with the admin
djadmin2.default.register(Question)
djadmin2.default.register(Choice)
