# awm-ca2
Assignment 2 for Advanced Web Mapping

This assignment contains functionality for 
*login and registering, 
*allows users to create a new profile for their dog by adding its name and a profile picture,
*allows users to view a list of their dogs,
*allows users to access a map where they they can place a marker. By clicking the 'Get Route' button, a route is generated between the marker and
the user's location, from which they can store this route by clicking on the marker and selecting a dog who would enjoy this walking route the most. 
The location position and the marker position are stored along with that dog's data and displayed in the dog list.
*users can also click a button on the map page that will display all nearby pet shops, should the user want to walk their dog to there.
*allows the user to download the page as a PWA.

##Home Screen:
![image](https://user-images.githubusercontent.com/71713529/207007715-8c9673ad-fd00-46e8-8f08-ce9bddd4f157.png)

##My Dogs:
![image](https://user-images.githubusercontent.com/71713529/207008691-d46c68fe-8223-485a-98ba-1712f479268f.png)

##Add a Dog:
![image](https://user-images.githubusercontent.com/71713529/207008744-b7306c54-2fde-448d-88cd-17203fe8a6b8.png)

##Plan a Walk:

![image](https://user-images.githubusercontent.com/71713529/207008857-ebbb01bf-27c9-47e9-b792-c145ddfd69cb.png)
![image](https://user-images.githubusercontent.com/71713529/207008910-d2b14cc0-3524-47e7-a961-e3012e362a45.png)

--Planning a route..
![image](https://user-images.githubusercontent.com/71713529/207009021-8f2e7af4-b766-4623-b206-597ee46ec73a.png)
![image](https://user-images.githubusercontent.com/71713529/207009087-58563fad-7da5-4765-8d11-28d46c06bd5a.png)
 
 --After clicking 'Get Nearest Petshop'
 ![image](https://user-images.githubusercontent.com/71713529/207009227-610f5330-a866-41e6-ad3c-bfe5ad6fbfc1.png)
 
 The Overpass API and the routing machine leaflet plugin were used to achieve these features.
 
 ##PWA
 
![image](https://user-images.githubusercontent.com/71713529/207009584-7e755cbe-bc20-4131-be01-22733cfeafd4.png)

![image](https://user-images.githubusercontent.com/71713529/207009662-768331fe-94a1-49fc-af27-19563752fa68.png)

##Deployment
While a digital ocean droplet was set up and a domain name was purchased on nameCheap (niamhk.online) deployment was not achieved. This was due to an error with the django-pwa package that would occur when attempting to run the built image of the project.
![image](https://user-images.githubusercontent.com/71713529/207026338-010cdb39-ad16-42bc-8ab4-ddf98e5f7a42.png)
Upon investigation this 'django.conf.urls.url()' is deprecated in Django 4, which is what was in use for this assignment. To deploy, this would entail taking the PWA functionality out of the project and rebuilding the image, but as PWA is a requirement for this assignment it was decided that the PWA functionality was more necessary than deployment.


