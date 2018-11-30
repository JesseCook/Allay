# System and Unit Test Report
## Allay
12/2018

### Sprint 1
* User Story:
  * As someone first coming to the webapp, I want an easy way to make a profile.
  
* Scenario:
  1. Start Allay App, and select Sign Up at bottom of page.
  2. Fill out fields as:
    * username = "TestUser"
    * email = "TestUser@test.com"
    * password = "CMPS115Scenario"
    * password confirmation = "CMPS115Scenario"
   3. User should be redirected to login page.
### Sprint 2
* User Story:
  * As someone first coming to the webapp, I want an easy way to make a profile.
  
* Scenario:

  (Assuming the user has successfully created an account)
  1. Start Allay App, and remain on login page.
  2. Fill out fields as:
    * username = "TestUser"
    * password = "CMPS115Scenario"
  3. If username and password match, and they're a registered user, they will be redirected to the home page.
  4. If username and password don't match, or they aren't a registered user, they will see an error saying "Your username and password didn't match. Please try again.

### Sprint 3
* User Story:
   * As someone with depression and/or anxiety, I want a way to be able to track my symptoms, so that I can objectively look at what helps and what does not.
 
* Scenario:
  1. Start Allay App, and log in as registered user.
  2. Be redirected to home page.
  3. If the user wants to look at their anxiety logs, click on the anxiety button. If the user clicked on the anxity button, they should be redirected to the anxiety overview page.
  5. If the user wants to look at their depression logs, click on the depression button. If the user clicked on the depression button, they should be redirected to the depression overview page.
  6. At this point, both the anxiety overview and depression overview pages should have no days logged.

### Sprint 4
* User Story:
   * As someone with depression and/or anxiety, I want a way to be able to track my symptoms, so that I can objectively look at what helps and what does not.
   
* Scenario:

   (Assuming the user has successfully navigated to the anxiety or depression overview pages)
   1. Once the user has reached an overview page, they should see a populated list of days they have logged entires. Each log should display the date, the rating they gave that symptom in that entry, and the log which displays their thoughts for that day.
   2. Click the "+" symbol near the top right of the page.
   3. The user will see a new page that says "How are you feeling?" near the top of the page. They will also see two areas where they can input data. One is a text box for their log, the other is a box for entering their rating.
   4. Click on the text box and enter text.
   5. Under the label "Enter symptom severity rating below", enter a value ranging from 1-10. If a value less than 0 or greater than 10 is entered text will display telling the user to enter a correct value.
   6. Click submit. If no entry for that day has been added then the user will be redirected to the previous overview. If an entry for that day has already been submitted, the user will see an error saying "An entry for this symptom was already input today." and they can return home by clicking the "Return Home" button at the bottom of the page.
   
