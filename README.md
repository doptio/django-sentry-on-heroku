Django Sentry on Heroku
=======================

Get this up and runnnig by::

    heroku create --stack cedar
    git push heroku
    heroku addons:add shared-database:5mb
    heroku config:add SENTRY_KEY=some-random-access-key
    heroku run sh
    # Run this one command in the Heroku shell, then exit it:
    sentry upgrade --config=sentry_conf.py
    heroku scale web=1
