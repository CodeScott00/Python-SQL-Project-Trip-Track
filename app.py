from flask import Flask, render_template
# from controllers import controller
from controllers.controller import travel_blueprint
from controllers.country_controller import country_blueprint #?
from controllers.destination_controller import destination_blueprint

app = Flask(__name__)

app.register_blueprint(destination_blueprint)
app.register_blueprint(travel_blueprint)
app.register_blueprint(country_blueprint)
#import blueprint?



@app.route('/')
def home():
    return render_template('index.html')



if __name__ == '__main__':
    app.run(debug=True)
