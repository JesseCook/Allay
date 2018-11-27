from django.db import models
from datetime import date
from django.utils import timezone
from django.contrib.auth.models import User

# This is our main class when it comes to our symptom tracking. They can choose to focus on anxiety, or depression. They can then see the average rating they have given to that symptom. Each symptom may have many days related to it.
class Symptom(models.Model):
    Anxiety = 'Anxiety'
    Depression = 'Depression'

    SYMPTOM_CHOICES = (
        (Anxiety,'Anxiety'),
        (Depression,'Depression')
    )

    
    # Here is where we make sure every symptom is linked to a specific user
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    

    # Here the user can choose whether they would like to track anxiety or depression.
    symptom = models.CharField(
        max_length = 10,
        choices=SYMPTOM_CHOICES,
    )

    # Here we will store the average daily rating for the tracked symptom. This field can have two digits to the left of the decimal, and one to the right.
    average_rating = models.DecimalField(
        max_digits= 3,
        decimal_places= 1,
        default= 0.0,
    )

    # Returns the symptom that any isntance of this object is tracking.
    def __str__(self):
        return self.symptom

    
    # This makes sure that no user can track the same symptom twice.
    class Meta:
       unique_together=("user","symptom")
    
    
# This class will be used for maintaining the actual days the user logs information about any given symptom. They will be able to give the rating that day. No two days can be linked to the same symptom.
class Day(models.Model):

    # This relates the Day relation to the Symptom relation, so that every day is linked to a specific symptom.
    symptom = models.ForeignKey(Symptom, on_delete=models.CASCADE)

    # Here we will store the daily rating for the tracked symptom. This field can have two digits to the left of the decimal, and one to the right.
    rating = models.DecimalField(
        max_digits=3,
        decimal_places=1,
        default=0.0,
    )

    # This sets the day for the object as the current day whenever a new instance is created.
    day = models.DateField(default=date.today)

    # This will be where the user can log their feelings for the day.
    log = models.TextField()

    # This makes it so that no two days can be set for the same symptom.
    class Meta:
        unique_together=("symptom","day")

