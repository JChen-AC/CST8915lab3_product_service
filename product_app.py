from flask import Flask, jsonify, request, abort
from flask_cors import CORS  # Enable Cross-Origin Resource Sharing for client apps
import os
from dotenv import load_dotenv


# referenced CST8916 assignment 1 for reference

app = Flask(__name__)
CORS(app)

products = [
    {"id":1, "name":"Dog Food", "price": 19.99 },
    { "id": 2, "name": "Cat Food", "price": 34.99 },
    { "id": 3, "name": "Bird Seeds", "price": 10.99 },
    { "id": 4, "name": "Fish Seeds", "price": 2.99 }
]

@app.route("/health", methods=['GET'])
def health_check():
    return jsonify({"status": "healthy"}), 200  # Return HTTP status 200 OK

@app.route("/products", methods=['GET'])
def get_products():    
    return jsonify(products), 200

#host ip : 192.168.2.71
if __name__ == '__main__':

    # used stack overflow and other sites 
    # https://stackoverflow.com/questions/8570636/change-folder-name-during-clone
    # https://dev.to/jakewitcher/using-env-files-for-environment-variables-in-python-applications-55a1 
    load_dotenv()    
    port_num = os.getenv("Port") 
    if not port_num:
        port_num = "3030"
    

    # https://www.geeksforgeeks.org/python/changing-host-ip-address-in-flask/
    app.run(host='0.0.0.0', port=port_num) 

# need to check to see if os needs to be put in requirements file . probably not 
# need to fix folder implmentation 
    