hackers-job-apply
=================

Reduce the spam you get for your job posting by setting up a micro challenge. 

Companies very often include emails on the job page. As a result, you have browse through spam from recruiters
and incompetent people. To filter them out set up a tiny task. Here is an example:

```
What is the largest 3 digit prime number?
POST json to the server with the answer -> { 'answer': 'xxx' }
```

## How to use it?

1. Use heroku deploy button 

[![Deploy to Heroku](https://www.herokucdn.com/deploy/button.png)](https://heroku.com/deploy)

1. Change JOB_EMAIL to yours. Change ANSWER and QUESTION if you want to use different challenge.

## Deploying to Heroku (command line)

Make sure you have the [Heroku Toolbelt](https://toolbelt.heroku.com/) installed.

```
git clone git@github.com:lukasz-madon/hackers-job-apply.git
heroku create
git push heroku master
heroku config:set JOB_EMAIL='dev.job@MYCOMPANY.COM'
heroku open
```

## Running Locally

Use `foreman start` or `python server.py`. Your app should now be running on [localhost:5000](http://localhost:5000/).


## Test:

```
curl -H "Content-Type: application/json" -d '{"answer":"997"}' http://hackers-job-apply.herokuapp.com/
```

result

```
dev.job@example.com
```

## TODO:
- no deployment for user -> webapp with login?

