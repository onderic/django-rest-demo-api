import pytest
from myapp.models import User
from django.db import models



def test_max_char_length_name():
    field = User._meta.get_field('name')
    assert field.max_length == 250

def test_field_type():
    field = User._meta.get_field('email')
    assert isinstance(field, models.EmailField)