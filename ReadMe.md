# get started by running:

## Start flask

```cd PayFlask```

```export FLASK_APP=application.py```

```export FLASK_DEBUG=1```

^_ is to allow the flask tor un in debug mode and keep the server refreshing

```flask run```

This will open a localhost:5000

## Start ngrok

```cd Downloads``` Or wherever ngrok was installed

```./ngrok http 5000```

Update the app_url variable inside application.py line 6 to the correct ngrok url