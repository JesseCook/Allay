# Overall Testing Notes
During the course of creating our application we have gone through multiple iterations of how we aimed to actually implement our vision. Originally, we had three main models we created in order to allow users to track various symptoms, and input data each day about whatever they were tracking. These three models were Symptom, Day, and DayLog. Each model went through full testing before moving forward after coding them, but in the end we only have a day model which enveloped the functionality of both Symptom and DayLog. Due to these changes, there is code missing from our home/tests.py file, but it can be found by looking in previous commits. Beyond this, we did a lot of manual testing for things like making sure no symptom can have two entries for the same day, and various user features. We also used CircleCI as a way to continuously integrate our application. CircleCI would build and run our app every time we committed code, so we could be assured that all of our tests still passed.

## Day Model Tests
In the unit tests for the Day model we first create a test user, so that we have a user to link the day to. Then we create two Day objects, one for anxiety and one for depression. We use these objects for all tests of our Day models. We split the day tests in to the following categories:
* Rating Tests:
  * In the rating test for our day model we ensure that we can access the rating given to a certain day. This will allow us to call the rating when needed for displaying information on the anxiety overview page.
* User Tests:
  * We tested the user foreign key of the Day by making sure that we could call the user each day is linked to, and then also calling the user id of said user. This was a necesssary feature to test because we used that information to filter the database query results when deciding which days to display for each user.
* Day Tests:
  * In the day tests for the Day model we print out the day that each Day was created. Also, we make sure that we can override the current day by creating a Day isntance for any day we want. We used this feature for testing reasons.
* Log Tests:
  * These log tests were written in order to get back the log that the user wrote for that day. This was needed to make sure that we can show the log for a user when displaying the data of the Day.

## Day Form Tests
In our unit tests for the DayForm form we intialize Day objects for both anxiety and depression, and then run basic tests foraccessing the data from the form.
* DayForm Tests:
  * In our DayForm tests we first initalize forma based off of the Day objects that we created in the setup. Then, we go through the forms and check whether the forms are valid. Finally, we print out the cleaned data from the forms in order to make sure everything has run properly.
