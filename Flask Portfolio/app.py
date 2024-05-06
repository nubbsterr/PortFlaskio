# Libraries
from flask import Flask, render_template 

app = Flask(__name__) # New flask application instance/object, __name__ is just to reference this script on its own

@app.route("/") # decorator for function below, calls function when the "/" URL is accessed, which is the homepage of the Flask app
def main():
    return render_template("home.html") # render_template picks a template to render, which is anything specified in our "templates" folder. In this case--our HTML webpage.

if __name__ == "__main__": # verifies if script is run locally and not in a separate file/script
    app.run(debug=False) # starts Flask app
    """
    debug=True enables debugging tools with Flask like auto-reloading the server when changes are made (like Live Server w/ HTML), 
    debug info when errors occur, and other bits of secret info 
    (i.e. don't have debug on when pushing to prod lol)
    """