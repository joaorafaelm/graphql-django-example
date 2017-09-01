# GraphQL and Django example

This project is an example of GraphQL and Django, using [graphene-django](https://github.com/graphql-python/graphene-django).
You can read the post explaining this project [here](https://joaorafaelm.github.io/blog/graphql-and-django-in-5-minutes).

## Installation
### 1. Download
First, download the *graphql-django-example* project files to your workspace:
```bash
$ git clone https://github.com/joaorafaelm/graphql-django-example;
$ cd graphql-django-example;
```
### 2. Virtualenv
We're going to use a virtual environment to easily manage dependencies for this demo. If you're not yet familiar with virtual environments for Python, using [virtualenv](http://www.virtualenv.org/), take a moment to learn about them. If you're already familiar with the concep, create one for the project:
```bash
$ virtualenv venv;
$ source venv/bin/activate;
```
### 3. Requirements
The *requirements.txt* file specifies the versions of django, and graphene-django, I'd like you to install. To do this, installing them into your virtual environment, type:
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

### 4. Ready? Go!
```bash
./manage.py runserver
```

Visit the link returned by ```runserver``` and visit the ```graphql``` route. This is likely to look like "[http://127.0.0.1:8000/graphql](http://127.0.0.1:8000/graphql)."
