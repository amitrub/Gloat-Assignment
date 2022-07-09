# Gloat-Assignment

The Srever is writen in Python useing Django web framework

## Quick Start

- clone the git project to your local device:

```
git clone https://github.com/amitrub/Gloat-Assignment.git
```

- enter to the main app dir.

```
cd to $MAIN_DIR/Gloat-Assignment/matcher
```

### With Docker and MySql

you need to have on your device installed - docker.
- run the app by docker compose:

```
docker compose up
```

### With Local and Sqlite

you need to have on your device installed - python, pip, and if you are using MySql you need to install it too.
- to setup app configuration run:
```
./setup
```
- after setup if you want to run the app again run:
```
python manage.py runserver
```
## Use The Server
enter to the url - http://127.0.0.1:8000/

![main screen](https://user-images.githubusercontent.com/48449311/178037490-0542229d-0a9e-4c51-998e-6be3e3f29e06.png)

- get all skills:

| 	Request Method  | 	Request URL |
| ------------- | ------------- |
| GET  | http://127.0.0.1:8000/skills/  |

- get all jobs: 

| 	Request Method  | 	Request URL |
| ------------- | ------------- |
| GET  | http://127.0.0.1:8000/jobs/  |

- get all candidates:

| 	Request Method  | 	Request URL |
| ------------- | ------------- |
| GET  | http://127.0.0.1:8000/candidates/  |


![Skill List2](https://user-images.githubusercontent.com/48449311/178098988-d3116263-d93f-4e3e-9ff5-3428f6a6f82c.PNG)
![Candidate List2](https://user-images.githubusercontent.com/48449311/178098998-265fc274-44b5-4af3-8b67-a5725d5e5fd5.PNG)
![Job List2](https://user-images.githubusercontent.com/48449311/178099003-f29fff28-694e-411f-ad31-08d17fa02c6a.PNG)

### Candidate Filter By Job
to filter candidate by job select the filter button

![filter select](https://user-images.githubusercontent.com/48449311/178099195-26a967ed-5dc2-4868-926f-ce758f2ff8bc.png)

### Filter Parameters
 there are 3 parameters to filter the candidates:
 - **job_id**: number, the job id to filter by.
 - **limit_number**: number, limit the output number of candidates, if empty retur all.
 - **title_match**: full/partial, choose whether you want to filter by all or just part of the title, defult is by full title.

![filter window](https://user-images.githubusercontent.com/48449311/178100263-58734c80-df5b-417d-b5c5-d7eb34bdc29e.PNG)

### Request Example
- get 2 candidates that match job with id-1 by full ttle match:

| 	Request Method  | 	Request URL |
| ------------- | ------------- |
| GET  | http://127.0.0.1:8000/candidates/?title_match=full&limit_number=2&job_id=1  |

## Filter Function Location
- Most of the functionality and models are at job_matcher packege.
path - Gloat-Assignment\matcher\job_matcher

 ![job_matcher packege](https://user-images.githubusercontent.com/48449311/178101383-ee7911f8-681a-488e-a51b-a051d16296ca.PNG)
 
 - The query of filtering candidates by jobs is in function **filter_queryset** in:
 path - Gloat-Assignment\matcher\job_matcher\filters 
 
 ![filter_queryset1](https://user-images.githubusercontent.com/48449311/178101636-25a70569-78b6-4cd6-9684-23934232202b.PNG)


