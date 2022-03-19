# API theme - Pet finder
## Description
The Pet finder API allows the access to a wide database range containing data that revolves around lost pets.
It is a RESTful API, meaning that it uses predictable URLs to access resources (such as informative pet/owner data) and, in case of an error, returns meaningful HTTP response codes. This enables the use of GET/POST requests, and HTTP authentication, the API can be used by sending requests with a specific structure to our servers. In order to maintain security.

The main purpose that we would like to achieve during the development of this project is to support & help people locate, identify and therefore, report lost pets to their owners ASAP throughout this API service.

## Usage
Throughout this project, we will be creating a database - where a pet owner will *submit* a missing 'petX' by entering a list of related information that could help the people within the surroundings to better associate & recognize the missing pet when this latter is seen or found.
Accordingly, they will enter the data related to the pet and if it is perhaps known within our database server, it will provide and come back with contact details of the proprietor so they can be reached, consequently, data will be *retrieved* and the pet would be identified and returned at last.

## TP1 Activity 1
A sample of the *generated* data (can be found in *db.json* file.) - has been created according to our theme needs - that is related to the owner and their pet, respectively, can be showcased down below :
```python 
{"owners": 
[{
"id": "d17d62d9-420e-4de5-9398-0898d5f4e0ed", 
"name": "Ashley Williams",
"email": "edowns@example.com", 
"address": "032 Lee Flats Apt. 046\nAmyberg, OR 94464", "728-050-3443": "728-050-3443"}]}
```
```python
{"pet":
[{"id": 75,
"lost_date": "Dec 26, 2021", 
"image_src": "https://www.petamberalert.com/petphotos/906098889-cat.jpg", 
"pet_name": "Buckley", 
"breed": "American Short Hair", 
"zip_code": "98513", 
"posted_date": "Olympia WA", 
"ownerId": "d6890702-2e41-4e82-9977-7a821f8fc828"}
]}
```
We have imported several python libraries to help us achieve online data retrieval (see *dataGenerator.py* to reveal further activity progression.) for this first activity such as :
```python
import uuid
from bs4 import BeautifulSoup //pet related data
import urllib3
import random
from faker import Faker //owner related data
import json
```
## Resources
When it comes to our project theme, JSON Generator was not the only suitable go-to method to generate random data since the one we are trying to build requires data for a composed object that concerns two essential parts of the database (*Pet/Owner* Combo), hence, we used a web scrapping method (in our case, for educational purposes.) to effectively harvest the rest of the needed data. The Python libraries requests and *Beautiful Soup* are powerful tools we used to achieve this activity.

Concerning the owner data, we used a python package *Faker* to generate fake data that we installed using the pip package management system.

## Answers for the exercise
Proceed to checking *listing2.js* for :

-> question 1 & question 2 functions.

-> question 3 :

Cache control dictates caching behavior for a website, letting browsers know how often to refresh locally stored resources. This directive means that cached versions of the requested resource/data cannot be used without first checking to see if there is an updated version and that's by using an ETag, this token is changed on the origin server whenever the resource is updated.

This process ensures that the user is always getting the most up-to-date version of that resource without requiring unnecessary downloads. When a user returns to a page with a ‘no-cache’ resource, the client will always have to connect to the origin server and compare the ETag on the cached resource with one on the server. If the ETags are identical, the cached resource will be provided to the user. If not, this means that the resource has been updated and the client will need to download a fresh version to provide to the user. 

-> question 4 :

Github accounts were created; 

Public repository 'Alos_act1' was created;

-> question 5 :

URL will be forwarded within the moodle platform.

## References 
here is links to the websites we have used for this activity part :

```python
 https://www.petamberalert.com
```
```python
https://json-generator.com
```