from django.test import TestCase
from home.models import *
from home.forms import *
from django.contrib.auth.models import User
from django.test import Client

class DayTestCase(TestCase):

    # Sets up out Day objects for testing.
    def setUp(self):

        self.user = User.objects.create_user(username='test', password='1234')

        Day.objects.create(user=self.user, symptom=Day.Anxiety, rating=50,day='1999-12-31',log='anxiety test log')

        Day.objects.create(user=self.user, symptom=Day.Depression,rating=60)


    # Checks to make sure we can get the rating from each Day.
    def test_Day_rating_tests(self):
        print('\n')
        self.test_anxiety = Day.objects.get(user=self.user.id,symptom=Day.Anxiety)

        self.test_depression = Day.objects.get(user=self.user.id,symptom=Day.Depression)

        print('test_anxiety.rating: ',self.test_anxiety.rating)

        print('test_depression.rating: ',self.test_depression.rating)


    # Checks to mae sure that we can get the user, and user_id, that each Day is linked to.
    def test_Day_user_tests(self):
        print('\n')
        self.test_anxiety = Day.objects.get(user=self.user.id,symptom=Day.Anxiety)

        self.test_depression = Day.objects.get(user=self.user.id,symptom = Day.Depression)

        print('The user.id of test_anxiety: ', self.test_anxiety.user.id)

        print('The user.id of test_depression: ', self.test_depression.user.id)

        print('The user of test_anxiety: ', self.test_anxiety.user)

        print('The user of test_depression: ', self.test_depression.user)

    def test_Day_day_tests(self):
        print('\n')
        self.test_anxiety = Day.objects.get(user=self.user.id,symptom=Day.Anxiety)

        self.test_depression = Day.objects.get(user=self.user.id,symptom=Day.Depression)

        print('test_anxiety.day: ', self.test_anxiety.day)

        print('test_depression.day: ', self.test_depression.day)

    def test_Day_log_tests(self):
        print('\n')
        self.test_anxiety = Day.objects.get(user=self.user.id,symptom=Day.Anxiety)

        self.test_depression = Day.objects.get(user=self.user.id,symptom=Day.Depression)

        print('test_anxiety.log: ', self.test_anxiety.log)

        print('test_depression.log: ', self.test_depression.log)


class DayFormTest(TestCase):

    def setUp(self):

        self.user = User.objects.create_user(username='test', password='1234')

        self.dayAnxiety =  Day.objects.create(user=self.user, symptom=Day.Anxiety, rating=5.0,day='1999-12-31',log='anxiety test log')

        self.dayDepression = Day.objects.create(user=self.user, symptom=Day.Depression,rating=6.0)

    def test_DayForm_tests(self):
        print('\n')

        anxiety_day_form = DayForm({'rating':self.dayAnxiety.rating,'log':'test_anxiety'},instance=self.dayAnxiety)

        depression_day_from = DayForm({'rating':self.dayDepression.rating,'log':'test_depression'},instance=self.dayDepression)

        self.assertTrue(anxiety_day_form.is_valid())

        self.assertTrue(depression_day_from.is_valid())

        print(anxiety_day_form.cleaned_data)

        print(depression_day_from.cleaned_data)





        
