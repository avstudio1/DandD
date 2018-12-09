# DandD: A playground application for learning how to code games like D & D.

This application started as a clone of the '[Getting Started with Python on Heroku](https://devcenter.heroku.com/articles/getting-started-with-python)'.

Deployment to Heroku is supported. You will need to install the [Heroku CLI](https://devcenter.heroku.com/articles/heroku-cli), as well as [Postgres](https://devcenter.heroku.com/articles/heroku-postgresql#local-setup).


## Running Locally

Runs with Python 3.7 

```sh
$ git clone https://github.com/avstudio1/DandD.git
$ cd DandD

$ python3 -m venv DandD
$ pip install -r requirements.txt

$ createdb DandD

$ python manage.py migrate
$ python manage.py collectstatic

$ heroku local
```

Your app should now be running on [localhost:5000](http://localhost:5000/).

## Deploying to Heroku

```sh
$ heroku create
$ git push heroku master

$ heroku run python manage.py migrate
$ heroku open
```