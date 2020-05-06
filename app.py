import random
from flask import Flask, render_template
from data import title, subtitle, description, departures as tour_departures, tours as tours_data

app = Flask(__name__)


@app.route('/')
def main():
    selected_tours = dict(random.sample(tours_data.items(), 6))
    return render_template('index.html', title=title, subtitle=subtitle, description=description, tours=selected_tours,
                           departures=tour_departures)


@app.route('/departures/<departure>/')
def departures(departure):
    direction = tour_departures[departure].replace("Из", "из")
    tour = {}
    for k, v in tours_data.items():
        if v['departure'] == departure:
            tour.update({k: v})
    prices = [price['price'] for price in tour.values()]
    nights = [night['nights'] for night in tour.values()]
    return render_template('departure.html', direction=direction, departures=tour_departures, tour=tour,
                           price=prices, night=nights)


@app.route('/tours/<int:tour_id>/')
def tours(tour_id):
    tour = tours_data[tour_id]
    return render_template("tour.html", tour=tour, departures=tour_departures)


if __name__ == '__main__':
    app.run()
