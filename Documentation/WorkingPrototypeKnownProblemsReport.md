# Working Prototype Known Problems Report
## Allay
12/2018

### List of functions notworking correctly
* When a user is entering a day log, text box errors can occur when they enter single words with a substantially large number of chargers in that word. This error does not occur when writing regular length words in long sentences.
* If a user successfully logs in, and then goes to the previous page (taking them to the login page) and they try to log in as a different user without refreshing the page or logging out they will get a system error saying "CSRF verification failed. Request aborted."
