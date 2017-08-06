# GraphQL and Django example

This project is an example of GraphQL and Django, using [graphene-django](https://github.com/graphql-python/graphene-django).
You can read the post explaining this project [here]().

## Installation
### 1. Download
Now, you need the *graphql-django-example* project files in your workspace:
```bash
$ git clone https://github.com/joaorafaelm/graphql-django-example;
$ cd graphql-django-example;
```
### 2. Virtualenv
You should already know what is [virtualenv](http://www.virtualenv.org/) at this stage. So, simply create it for the project:
```bash
$ virtualenv venv;
$ source venv/bin/activate;
```
### 3. Requirements
You will find the *requirements.txt* file that has django and the graphene-django. To install them, simply type:
```bash
$ pip install -r requirements.txt
```
#### Initialize the database
```bash
./manage.py migrate
```
#### Load some data
```bash
./manage.py loaddata books.json
```
If you wish to add more data, run `./manage.py createsuperuser`, and you can use the admin interface.

### Ready? Go!
```bash
./manage.py runserver
```
