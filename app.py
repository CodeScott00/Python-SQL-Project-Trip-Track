from flask import Flask, render_template
# from controllers import travel_blueprint


# app.register_blueprint(travel_blueprint)
#import blueprint?

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')



if __name__ == '__main__':
    app.run(debug=True)
