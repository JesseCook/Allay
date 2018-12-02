# Allay
This repository is dedicated to the CMPS 115 project, Allay. Our application aims to give our users the tools to better manage their anxiety, depression, or whatever else they may be facing. Overall, we seek to truly lessen the suffering of those who choose to use our app.

## Members
* Jesse Cook (Product Owner)
* Nicolas Auld
* Kasia Sayles
* Kiran Gunasekaran

## Documentation
* [Initial Presentation](https://docs.google.com/presentation/d/e/2PACX-1vRtHKA2N8LWFV6sdEfLD3zroUJgq5eGwVA2lcFsgliu1qK_fHVg5U-WTm6bcNbNHrGift_MNBHJdUjd/pub?start=false&loop=false&delayms=3000)

* [Release Plan](https://github.com/JesseCook/Allay/blob/master/Documentation/ReleasePlan.md)

* Sprint One:
  * [Plan](https://github.com/JesseCook/Allay/blob/master/Documentation/SprintOnePlan.md)
  * [Report](https://github.com/JesseCook/Allay/blob/master/Documentation/SprintOneReport.md)
* Sprint Two:
  * [Plan](https://github.com/JesseCook/Allay/blob/master/Documentation/SprintTwoPlan.md)
  * [Report](https://github.com/JesseCook/Allay/blob/master/Documentation/SprintTwoReport.md)
* Sprint Three:
  * [Plan](https://github.com/JesseCook/Allay/blob/master/Documentation/SprintThreePlan.md)
  * [Report](https://github.com/JesseCook/Allay/blob/master/Documentation/SprintThreeReport.md)
* Sprint Four:
  * [Plan](https://github.com/JesseCook/Allay/blob/master/Documentation/SprintFourPlan.md)
  * [Report](https://github.com/JesseCook/Allay/blob/master/Documentation/SprintFourReport.md)
* [System and Unit Test Report](https://github.com/JesseCook/Allay/blob/master/Documentation/SystemAndUnitTestReport.md)
* [Known Problems Report](https://github.com/JesseCook/Allay/blob/master/Documentation/WorkingPrototypeKnownProblemsReport.md)

## Installation
First, install Python 3.7, Django 2.1, and PostgreSQL for database usage. To configure the database so that the application can be run with the current settings, make a database user with name = allayteam, a database with name = allay, and password for the database = raven99dog. This will allow the user to store their information in a local database.

Next, once you have verified that Python 3.7, Django, and PostgreSQL are all working properly, clone the project to your local machine using:
```
git clone https://github.com/JesseCook/Allay.git
```
After you have cloned the project, set your working directory to the mysite folder found directly inside the Allay folder. Once your working directory is set, start the server by running the following command:
```
python manage.py runserver
```
When this command successfully runs, open a web browser (preferably Safari) and set your url as the following entry:
```
localhost:8000
```
Finally, you should see sign in page where you may log in if you already have an account. If this is your first time entering the site, then click on the "Sign Up" link found near the bottom of the page.
