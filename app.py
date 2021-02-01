from flask import Flask, render_template
# from controllers import controller
from controllers.controller import travel_blueprint
from controllers import country_controller

app = Flask(__name__)

app.register_blueprint(travel_blueprint)
#import blueprint?



@app.route('/')
def home():
    return render_template('index.html')



if __name__ == '__main__':
    app.run(debug=True)
