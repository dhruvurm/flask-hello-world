# -- Flask Hello - world #

#import the flask class from the flask package
from flask import Flask

# create the application object

app = Flask(__name__)

# error handling
app.config["DEBUG"] = True

#use the decorator pattern to link the view function to the url

@app.route("/")
@app.route("/hello")
@app.route("/test")
@app.route("/name/<name>")
def index(name):
    if name.lower() == "michael":
        return "hello, {}".format(name), 200
    else:
        return "Not found", 404



#define the view using a function, which returns a string

def search():
    return "hello"
def search2():
    return "bye bye"

#start development server using the run method

if __name__ == "__main__":
    app.run()
