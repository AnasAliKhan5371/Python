# IMPORTING
from flask import Flask, render_template

# INTERACTION
app = Flask(__name__)

# MAPPING
@app.route('/')

#INPUTS
def first():
    return render_template("home.html")

#MAPPING
@app.route('/second')

#INPUTS
def second():
    return render_template("second.html")
# MAIN
if __name__ == "__main__":
    app.run(debug=True)  #debug-->auto. reload page