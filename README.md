# awm-ca1
Assignment 1 for Advanced Web Mapping

## The web application contains these pages:
home
login
signup
map

### Home Page:
The index of the web app. This website will prompt users who haven't logged in to either log in or sign up. 

### Login:
The user can enter their log in details and using the 'auth' functionality in django, it will check if that user exists
and log them in.

### Signup:
Users can enter their username, email, their password and confirmation of their password. This new user will be logged 
in the database, given that their password isn't too common and that a user of the same username does not already
exist.

### Map:
Visiting this page displays a map of the user's current location. The location is logged into the database, in the
user-profile table's 'location' column, the moment the location has been found.


Attempts had been made to deploy the project on docker, after purchasing the domain http://niamhk.online/ 
A digital ocean droplet was also created.

![image](https://user-images.githubusercontent.com/71713529/200890651-46e32c25-35de-4053-b446-ca24c3dac9a9.png)

However, there were some issues while attempting to deploy the docker containers.
