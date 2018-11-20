# Sprint Three Plan
## Allay
Sprint Completed November 5th, 2018

### Goal
Host database and site online for users to access.
Allow users to track symptoms upon logging in to their user profile.

### Task listing, organized by user story
* As someone with depression and/or anxiety, I want a way to be able to track my symptoms, so that I can objectively look at what helps and what does not.
  * Build new UI Components:
    * Home View UI List:
      * Anxiety Button leading to Anxiety Overview
      * Depression Button leading to Depression Overview
    * Anxiety Overview UI List:
      * Button to add new day, leads to blank day log
      * List of days previously added sorted in date format
    * Depression Overview UI List:
      * Button to add new day, leads to blank day log
      * List of days previously added sorted in date format
    * Blank Day log UI List:
      * Blank text box for user to enter how they are feeling
      * Set of 10 bubbles below text box to represent scale of 1 - 10
      * Submit button that adds the day log to the end of the selected illness (currently Anxiety or Depression)
  * Create a list format, where the user can input things they want to track.
  * Maintain user data, so that their list does not disappear when they exit the app.
  * For each item tracked, maintain a list of days where the user can input data about that item.
* As someone who wants to use this web application, I want to be able to access it online.
  * Find hosting for the website and web server.
  * Make necessary changes for web applicationt to successfully run online.
  * Push all future site changes to this server.
  * Only display coming soon page until web application is ready to launch.

### Team Roles
* Jesse Cook: Product Owner, Developer
* Kasia Sayles: Developer
* Kiran Gunasekaran: Developer
* Nicolas Auld: Developer, Scrum Master

### Initial Task Assignment
* Jesse
  * Maintain login information in our database, so that the user can sign in and out.
  * Create a list of symptoms in database to populate list for user to pick from that they want to track.
  * Build symptom card.
  * Build symptom measurement input card.

* Kasia
  * Set up base code that will be built on top of (with front end and back end communicating).
  * Connect measurement value entered by user and current date to database to be accessible for later retrieval.
  * Build main layout of app (color scheme, background).
  * Build tracked symptom history log card.
  
* Kiran
  * Design component piece for symptom cards (i.e Depression, Anxiety, Sadness).
  * Design component when user clicks on symptom to enter measurement.
  * Design component for showing previous symptom measurements.
  
* Nicolas
  * Build login UI component.
  * Build register UI component.
  * Build password reset UI component. 
  * Resend email verification
   
### Initial Burnup Chart
Burnup Chart on [Google Sheets](https://docs.google.com/spreadsheets/d/e/2PACX-1vQT1VhaaO2K0SNnBREjd6a8pjhy_JSWYyzIHHo-ErxgdYlYql5JPvxA1bA6M1QoQHIBf-a9-7EjtFHH/pubchart?oid=81807857&format=image).
 
### Initial Scrum Board
Scrum Board on [Trello](https://trello.com/b/G99wzcH9/sprint-3-scrum-board).
 
### Scrum Times
Tuesday, Thursday, and Friday.
