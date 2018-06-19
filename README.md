# Flask Webapp

Following along Miguel Grinberg's tutorial on creating a Flask webapp.
Would like to eventually learn enough to create a Flask backend that a Vue.js frontend connects to.

Also using this to improve python skills.

This is now hosted on Herokuat https://flask-nanoblog.herokuapp.com/

* Had to make some changes to the model to fit longer email addresses. Involved putting flask db migrate and flask db upgrade into the Procfile
* Made some changes to the ELASTICSEARCH_URL. By default the elasticsearch module connects to port 9200, had to explicitly specify port 80 in the config
