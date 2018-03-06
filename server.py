from flask import Flask
from flask_cors import CORS
import simplejson as json
app = Flask(__name__)
CORS(app) 

project_list = ['let']
global query_dict
query_dict = {}

def load():
    try:
        global query_dict
        query_dict = dict([(_, json.loads(file(_ + '/server.preload.json', 'rb').read())) for _ in project_list])
    except Exception as e:
        print e

@app.route("/")
def hello():
    return "Hello World!"

@app.route("/reload")
def reload():
    load()
    return 'ok'

@app.route("/all")
def all():
    import json2html 
    global query_dict
    load()
    return json2html.json2html.convert(json=json.dumps(query_dict))

@app.route('/query/<project>/<username>')
def show_user_profile(project, username):
    global query_dict
    if project in project_list:
    # show the user profile for that user
        print json.dumps(query_dict[project].get(username, {}))
        return json.dumps(query_dict[project].get(username, {}))
    else:
        return '{}'
load()
app.run(host='0.0.0.0', port=8080)
