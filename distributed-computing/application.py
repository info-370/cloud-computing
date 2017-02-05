from flask import Flask, request
import processing as p
app = Flask(__name__)

@app.route("/")
def index():
    return "Welcom to lab!"

# /average_pop?city
@app.route("/average_pop")
def process():
    cityname = request.args.get('city')
    if cityname == None:
        return "No city name"
    avg = p.get_avg_pop(cityname)
    return str(avg)

if __name__ == "__main__":
    app.run()
