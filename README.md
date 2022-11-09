# awm-ca1
Assignment 1 for Advanced Web Mapping

## The web application contains these pages:
home
login
signup
map

### Home Page:
The index of the web app. This website will prompt users who haven't logged in to either log in or sign up. 

When user isn't logged in:

![image](https://user-images.githubusercontent.com/71713529/200953838-2ae53656-1307-40f6-b265-e4a3caa252f3.png)

When user is logged in:

![image](https://user-images.githubusercontent.com/71713529/200954260-603b577c-08e5-4d51-801d-89035c79d0e7.png)


### Login:
The user can enter their log in details and using the 'auth' functionality in django, it will check if that user exists
and log them in.

![image](https://user-images.githubusercontent.com/71713529/200954426-95159efb-2c86-424f-9bcd-b5fc8424fb37.png)


### Signup:
Users can enter their username, email, their password and confirmation of their password. This new user will be logged 
in the database, given that their password isn't too common and that a user of the same username does not already
exist.

![image](https://user-images.githubusercontent.com/71713529/200954483-3b07a5b8-a81b-41f9-afa9-3b0a834b698c.png)


### Map:
Visiting this page displays a map of the user's current location. The location is logged into the database, in the
user-profile table's 'location' column, the moment the location has been found.

![image](https://user-images.githubusercontent.com/71713529/200955076-0030fbb8-c8ec-47fc-854f-115930017de2.png)


Attempts had been made to deploy the project on docker, after purchasing the domain http://niamhk.online/ 

![image](https://user-images.githubusercontent.com/71713529/200956017-40b064ee-b572-4945-8647-9dfd73d8f46c.png)

A digital ocean droplet was also created.

![image](https://user-images.githubusercontent.com/71713529/200890651-46e32c25-35de-4053-b446-ca24c3dac9a9.png)

However, there were some issues while attempting to deploy the docker containers.
What was achieved was that the niamhk.online domain was registered to get SSL cert using certbot, Nginx server was installed, and 2 docker containers were created in the Digital Ocean droplet.

![image](https://user-images.githubusercontent.com/71713529/200956488-c0dc15ce-6c5d-470d-b466-5fb55122de07.png)
![image](https://user-images.githubusercontent.com/71713529/200956771-7dfdb90c-8c10-454a-9447-790639ba7502.png)
