from flask import Flask, request, jsonify
import pandas as pd
from routes import routes

app = Flask(__name__)
app.register_blueprint(routes.route)





app.run(debug=True, host='0.0.0.0')