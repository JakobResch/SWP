import json
from flask import Flask, jsonify, request, render_template
from flask_restful import Resource, Api
import SSP_Resch
import matplotlib.pyplot as plt
import seaborn as sns

app = Flask(__name__, template_folder='templates')
api = Api(app)
class Ausgabe(Resource):
    def get(self):
        with open('data.txt', 'r') as file:
            list2 = json.load(file)
            plt.bar(*zip(*list2.items()))
            plt.savefig("pic.png")
            plt.show()
        return list2
api.add_resource(Ausgabe, "/reschfresh")

if __name__ == '__main__':
    app.run(debug=True)