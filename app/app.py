import os
from flask import Flask, json, jsonify, request
from flask_sqlalchemy import SQLAlchemy
# from models import User
from flasgger import Swagger

project_dir = os.path.dirname(os.path.abspath(__file__))
database_file = "sqlite:///{}".format(os.path.join(project_dir, "ardb.db"))

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = database_file
swagger = Swagger(app)
db = SQLAlchemy(app)
db.create_all()


@app.route('/')
def index():
    """Endpoint returning a blank index file
    ---
    responses:
     200:
       description: The index of app
   """


    return ("index")

@app.route('/hello/<hello>')
def hello(hello = None):
    """Endpoint returning a blank index file
    ---
     parameters:
     - name: hello
       in: path
       type: string
       required: false
       default: World!
       responses:
        200:
       description: A Hello World message

    """

    print(hello)
    user = User(userID=hello, assetsCollected='1,2,3,4,5')
    db.session.add(user)
    db.session.commit()
    return ("Hello"+ hello)

@app.route('/healthcheck')
def healthcheck():
    """Endpoint returning a blank index file
    ---
    responses:
      200:
       description: A healthcheck

    """

    return ("healthcheck")

@app.route('/user/settings/<userid>')
def userSettings(userid=None):
    """
        This is the endpoint to handle user settings configuration
    ---
    parameters:
      - in: path
        name: userid
        type: string
    responses:
      200:
        description: User settings updated
    """
    response = {}
    response["status"] = 200
    response["body"] = " User settings updated for UserID :" + userid
    response["userid"] = userid
    responseJSON = jsonify(response)
    return responseJSON

@app.route('/search/<lat>/<lon>')
def search(lat = None, lon = None):
    """Endpoint returning a blank index file
    ---
    parameters:
     - name: lat
       in: path
       type: string
       required: true
       default: None
     - name: lon
       in: path
       type: string
       required: true
       default: None
    responses:
     200:
       description: The latitude and longitude"

    """
    return ("search:"+ lat + "," + lon)

@app.route('/place/lat/lon')
def place():
    """Endpoint returning a blank index file
    """
    return "place/lat/lon"

@app.route('/collect/<userid>/<itemid>')
def collect(userid=None, itemid=None):
    """
        This is the endpoint to handle adding an item to a users collection
    ---
    parameters:
      - in: path
        name: userid
        type: string
      - in: path
        name: itemid
        type: string
    responses:
      200:
        description: The task has been created
    """
    response = {}
    response["status"] = 200
    response["body"] = "UserID :" + userid + " ItemID : " + itemid
    response["userid"] = userid
    response["itemid"] = itemid
    responseJSON = jsonify(response)
    return responseJSON

@app.route('/user/<userID>')
def getUser(userID = None):
    """
        This is the endpoint to handle adding an item to a users collection
    ---
    parameters:
      - in: path
        name: userid
        type: string
      - in: path
        name: itemid
        type: string
    responses:
      200:
        description: The task has been created
    """
    response = {}
    response["status"] = 200
    response["body"] = "UserID :" + userid + " ItemID : " + itemid
    response["userid"] = userid
    response["itemid"] = itemid
    responseJSON = jsonify(response)
    return responseJSON


@app.route('/asset/post')
def postAsset():
    """
        This is the endpoint to handle adding an item to a users collection
    ---
    parameters:
      - in: path
        name: userid
        type: string
      - in: path
        name: itemid
        type: string
    responses:
      200:
        description: The task has been created
    """
    response = {}
    response["status"] = 200
    response["body"] = "UserID :" + userid + " ItemID : " + itemid
    response["userid"] = userid
    response["itemid"] = itemid
    responseJSON = jsonify(response)
    return responseJSON

@app.route('/asset/<assetID>')
def getAsset(assetID=None):
    """
        This is the endpoint to handle adding an item to a users collection
    ---
    parameters:
      - in: path
        name: userid
        type: string
      - in: path
        name: itemid
        type: string
    responses:
      200:
        description: The task has been created
    """
    response = {}
    response["status"] = 200
    response["body"] = "UserID :" + userid + " ItemID : " + itemid
    response["userid"] = userid
    response["itemid"] = itemid
    responseJSON = jsonify(response)
    return responseJSON

@app.route('/collect/<userID>/<assetID>')
def collectAsset(userID=None, assetID=None):
    """
        This is the endpoint to handle adding an item to a users collection
    ---
    parameters:
      - in: path
        name: userid
        type: string
      - in: path
        name: itemid
        type: string
    responses:
      200:
        description: The task has been created
    """
    response = {}
    response["status"] = 200
    response["body"] = "UserID :" + userid + " ItemID : " + itemid
    response["userid"] = userid
    response["itemid"] = itemid
    responseJSON = jsonify(response)
    return responseJSON

@app.route('/asset/nearby/<location>/<radius>')
def getAssetsNearby(location='0.0,0.0', radius=10):
    """
        This is the endpoint to handle adding an item to a users collection
    ---
    parameters:
      - in: path
        name: userid
        type: string
      - in: path
        name: itemid
        type: string
    responses:
      200:
        description: The task has been created
    """
    response = {}
    response["status"] = 200
    response["body"] = "UserID :" + userid + " ItemID : " + itemid
    response["userid"] = userid
    response["itemid"] = itemid
    responseJSON = jsonify(response)
    return responseJSON



@app.route('/user/create')
def createUser():
    """
        This is the endpoint to handle adding an item to a users collection
    ---
    parameters:
      - in: path
        name: userid
        type: string
      - in: path
        name: itemid
        type: string
    responses:
      200:
        description: The task has been created
    """
    response = {}
    response["status"] = 200
    response["body"] = "UserID :" + userid + " ItemID : " + itemid
    response["userid"] = userid
    response["itemid"] = itemid
    responseJSON = jsonify(response)
    return responseJSON


class User(db.Model):
    userID = db.Column(db.String(80), unique=True, nullable=False, primary_key=True)
    assetsCollected = db.Column(db.String(), unique=False, nullable=False, primary_key=False)

    def __repr__(self):
        return "<UserID: {}\n assetsCollected: {}>".format(self.userID, self.assetsCollected)
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port, debug=True)
