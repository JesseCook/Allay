from django.forms import DecimalField, ModelForm
from home.models import Symptom
from home.models import DayLog
from home.models import Day
from django.contrib.auth.models import User

# This class creates a form for our Symptom model.
class SymptomForm(ModelForm):


    average_rating = DecimalField(
        max_value= 10.0,
        min_value= 0.0,
        max_digits= 3,
        decimal_places= 1
        )

    class Meta:
        model = Symptom
        fields = ['symptom','average_rating']

# This class creates a form for our Day model.
class DayForm(ModelForm):

    # This makes it so users can only enter ratings between 0.0 and 10.0
    rating = DecimalField(
        max_value=10.0,
        min_value=0.0,
        max_digits=3,
        decimal_places=1
    )

    class Meta:
        model = Day
        fields = ['symptom','rating']

# This class creates a form for our DayLog model.
class DayLogForm(ModelForm):

    # This makes it so users can only enter ratings between 0.0 and 10.0
    rating = DecimalField(
        max_value=10.0,
        min_value=0.0,
        max_digits=3,
        decimal_places=1
    )

    class Meta:
        model = DayLog
        fields = ['day','rating','log']
