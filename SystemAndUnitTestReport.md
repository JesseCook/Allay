# System and Unit Test Report
## Allay
12/2018

### Sprint 1
* User Story:
  * As someone first coming to the webapp, I want an easy way to make a profile.
* Scenario:
  1. Start Allay App, and select Sign Up at bottom of page.
  2. Fill out fields as:
    * username = <TestUser>
    * email = <TestUser@test.com>
    * password = <CMPS115Scenario>
    * password confirmation = <CMPS115Scenario>
    * User should be redirected to login page.
### Sprint 2
* User Story:
  As someone first coming to the webapp, I want an easy way to make a profile.
* Scenario:
(Assuming the user has successfully created an account)
  1. Start Allay App, and remain on login page.
  2. Fill out fields as:
    * username = <TestUser>
    * password = <CMPS115Scenario>
  3. If username and password match, and they're a registered user, they will be redirected to the home page.
  4. If username and password don't match, or they aren't a registered user, they will see an error saying "Your username and password didn't match. Please try again.
