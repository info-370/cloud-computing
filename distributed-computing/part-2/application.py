from flask import Flask, request
import processing as p
application = Flask(__name__)

@application.route("/")
def index():
    return "<h1>Welcome to lab!</h1>"

# /average_pop?city
@application.route("/average_pop")
def process():
    cityname = request.args.get('city')
    if cityname == None:
        return "No city name"
    avg = p.get_avg_pop(cityname)
    return str(avg)

if __name__ == "__main__":
    application.run(port=80)
