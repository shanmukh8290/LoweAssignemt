from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _
import re

def checkNull(value):
    if(value == "" or value == None):
        raise ValidationError(
            _('%(value)s should not be null')
        )

def emailValidation(email):
    regex = r"^(\w|\.|\_|\-)+[@](\w|\_|\-|\.)+[.]\w{2,3}$"
    if(not re.search(regex, email)):
        raise ValidationError(
            _('%(value)s is not an valid email'),
            params={'value': email},
        )

def phoneNumberValidation(phn):
    # 1) Begins with 0 or 91
    # 2) Then contains 7 or 8 or 9.
    # 3) Then contains 9 digits
    Pattern = re.compile("(0/91)?[7-9][0-9]{9}")
    if not Pattern.match(str(phn)):
        raise ValidationError('Invalid Phone Number')