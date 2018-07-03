from flask import Flask, render_template, render_template_string, request
import os
from flask_restful import abort, Api, fields, marshal_with, reqparse, Resource 
from datetime import datetime
from pytz import utc

app = Flask(__name__)
api = Api(app)
from api.api import TodoSimple
api.add_resource(TodoSimple, '/api/<string:todo_id>')
from api.api import HelloWorld
api.add_resource(HelloWorld, '/api')
from api.api import Car
api.add_resource(Car, '/api/cars')

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/upload/<filename>", methods=["POST"])
def upload(filename):
    print(request.files['source'].save(os.getwd().join("/static"), "photo1"))

    return render_template_string(filename)
##@app.route("download/<filename>"), methods=[""]

extra_dirs = [os.getcwd()+"/templates/",os.getcwd()+"/static/"]
extra_files = extra_dirs[:]
for extra_dir in extra_dirs:
    for dirname, dirs, files in os.walk(extra_dir):
        for filename in files:
            filename = os.path.join(dirname, filename)
            if os.path.isfile(filename):
                extra_files.append(filename)
            
                
if __name__ == '__main__':
    # This is used when running locally. Gunicorn is used to run the
    # application on Google App Engine. See entrypoint in app.yaml.
    app.run(host='127.0.0.1', port=8080, debug=True, threaded=True, extra_files=extra_files)
