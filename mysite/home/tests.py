from django.test import TestCase
from home.models import *
from home.forms import *
from django.contrib.auth.models import User
from django.test import Client

# Create your tests here.
class SymptomAverageTestCase(TestCase):

    # Sets up our Symptom objects for testing.
    def setUp(self):

        print("\n----------------------------------------------------------------------")

        self.user = User.objects.create_user(username='test',password='1234')

        Symptom.objects.create(user=self.user, symptom=Symptom.Anxiety,average_rating=10)

        Symptom.objects.create(user=self.user, symptom=Symptom.Depression,average_rating=20)

    # Checks to make sure we can get the average rating for each symptom.
    def test_Symptom_average_tests(self):

        print("Tests For Getting symptom.average From Symtpom Objects:\n")

        self.anxiety_average = Symptom.objects.get(symptom='Anxiety')

        self.depression_average = Symptom.objects.get(symptom='Depression')

        print('anxiety_average.average_rating:',self.anxiety_average.symptom+":", self.anxiety_average.average_rating)

        print('depression_average.average_rating:', self.depression_average.symptom+":", self.depression_average.average_rating)


    # Checks to make sure we can get the user, and user_id, for each symptom.
    def test_Symptom_user_tests(self):
        print("Tests For Working With symptom.user From Symptom Objects:\n")

        self.anxiety_average = Symptom.objects.get(symptom='Anxiety')

        self.depression_average = Symptom.objects.get(symptom='Depression')

        print('anxiety_average.user:', self.anxiety_average.user)

        print('depression_average.user:', self.depression_average.user)

        print('anxiety_average.user_id:', self.anxiety_average.user_id)

        print('depression_average.user_id:', self.depression_average.user_id)

        print("----------------------------------------------------------------------")

class DayTestCase(TestCase):

    # Sets up out Day objects for testing.
    def setUp(self):

        self.user = User.objects.create_user(username='test', password='1234')

        self.symptomAnxiety = Symptom.objects.create(user=self.user, symptom=Symptom.Anxiety,average_rating=30)

        self.symptomDepression = Symptom.objects.create(user=self.user, symptom=Symptom.Depression,average_rating=40)

        Day.objects.create(symptom=self.symptomAnxiety, rating=50)

        Day.objects.create(symptom=self.symptomDepression,rating=60)


    # Checks to make sure we can get the rating from each Day.
    def test_Day_rating_tests(self):

        self.test_anxiety = Day.objects.get(symptom=self.symptomAnxiety.id)

        self.test_depression = Day.objects.get(symptom=self.symptomDepression.id)

        print("--------------------------------------------------------------------")

        print("Tests For Getting day.rating From Day Objects\n")

        print('test_anxiety.rating: ',self.test_anxiety.rating)

        print('test_depression.rating: ',self.test_depression.rating)

        print("--------------------------------------------------------------------")

    # Checks to make sure that we can get the symptom, and symptom_id, that each Day is linked to.
    def test_Day_symptom_tests(self):

        self.test_anxiety = Day.objects.get(symptom=self.symptomAnxiety.id)

        self.test_depression = Day.objects.get(symptom=self.symptomDepression.id)

        print("Tests For Working With day.symptom For A Day Object:\n")

        print('test_anxiety.symptom: ', self.test_anxiety.symptom)

        print('test_depression.symptom: ',  self.test_depression.symptom)

        print('test_anxiety.symptom_id: ', self.test_anxiety.symptom_id)

        print('test_depression.symptom_id: ', self.test_depression.symptom_id)

        print("---------------------------------------------------------------------")


    # Checks to mae sure that we can get the user, and user_id, that each Day is linked to.
    def test_Day_user_tests(self):

        self.test_anxiety = Day.objects.get(symptom=self.symptomAnxiety.id)

        self.test_depression = Day.objects.get(symptom=self.symptomDepression.id)

        print("---------------------------------------------------------------------")

        print("Test For Getting The user.id And user From A User Linked To A Day :\n")

        print('The user.id of test_anxiety: ', self.test_anxiety.symptom.user.id)

        print('The user.id of test_depression: ', self.test_depression.symptom.user.id)

        print('The user of test_anxiety: ', self.test_anxiety.symptom.user)

        print('The user of test_depression: ', self.test_depression.symptom.user)


class SymptomFormTest(TestCase):

    def setUp(self):
       self.user = User.objects.create_user(username='test', password='1234')

       self.symptomAnxiety = Symptom.objects.create(user=self.user, symptom=Symptom.Anxiety, average_rating=8.0)

       self.symptomDepression = Symptom.objects.create(user=self.user, symptom=Symptom.Depression, average_rating=7.6)

    def test_SymptomForm_tests(self):
        form_data = {'symptom':Symptom.Anxiety,'average_rating': 10}

        test_form = SymptomForm(data=form_data)
        self.assertTrue(test_form.is_valid())

        anxiety_symptom_form = SymptomForm({'symptom': self.symptomAnxiety.symptom,'average_rating':self.symptomAnxiety.average_rating}, instance= self.symptomAnxiety)

        print(anxiety_symptom_form.is_bound)

        self.assertTrue(anxiety_symptom_form.is_valid())

        #for value in anxiety_symptom_form.fields.values(): print(value)

        print(anxiety_symptom_form.cleaned_data)

class DayFormTest(TestCase):

    def setUp(self):

        self.user = User.objects.create_user(username='test', password='1234')

        self.symptomAnxiety = Symptom.objects.create(user=self.user, symptom=Symptom.Anxiety,average_rating=30)

        self.symptomDepression = Symptom.objects.create(user=self.user, symptom=Symptom.Depression,average_rating=40)

        self.dayAnxiety = Day.objects.create(symptom=self.symptomAnxiety, rating=5.0)

        self.dayDepression = Day.objects.create(symptom=self.symptomDepression,rating=6.0)

    def test_DayForm_tests(self):

        anxiety_day_form = DayForm({'rating':self.dayAnxiety.rating},instance=self.dayAnxiety)

        depression_day_from = DayForm({'rating':self.dayDepression.rating},instance=self.dayDepression)

        self.assertTrue(anxiety_day_form.is_valid())

        self.assertTrue(depression_day_from.is_valid())

        print(anxiety_day_form.cleaned_data)

        print(depression_day_from.cleaned_data)





        
