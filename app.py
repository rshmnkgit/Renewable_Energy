from flask import Flask, render_template
from flask import jsonify
from flask import request
from flask_pymongo import PyMongo

app = Flask(__name__)

app.config['MONGO_DBNAME'] = 'renewable_energy'
app.config['MONGO_URI'] = 'mongodb://localhost:27017/renewable_energy'

mongo = PyMongo(app)


@app.route('/', methods=['GET'])
def index():
    energysrc = mongo.db.energysource
    output = []
    for row in energysrc.find():
        output.append({'country': row['Country'],
                       'year': row['Year'],
                       'solar': row['Solar'],
                       'hydro': row['Hydro'],
                       'wind': row['Wind'],
                       'biofuels': row['Biofuels']
                       })
    energy_json = jsonify({'result': output})
    # return energy_json;
    return render_template("index.html", energy_html=energy_json)


if __name__ == "__main__":
    app.run(debug=True)
