from flask import Flask

# create the flask app
app = Flask(__name__)

# list of car models
existing_models = ["corolla", "camry", "mustang", "civic"]

# home route
@app.route('/')
def home():
    return "Welcome to Flatiron Cars"

# dynamic route
@app.route('/<model>')
def car_model(model):

    # check if model exists
    if model in existing_models:
        return f"Flatiron {model} is in our fleet!"
    
    # if model does not exist
    return f"No models called {model} exists in our catalog"


# this starts the flask server
if __name__ == "__main__":
    app.run(debug=True)