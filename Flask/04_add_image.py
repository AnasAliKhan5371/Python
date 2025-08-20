# IMPORTING
from flask import Flask, render_template
import os

# INTERACTION
app = Flask(__name__)

picfolder=os.path.join('static')

app.config['UPLOAD_FOLDER']=picfolder

# MAPPING
@app.route('/')

#INPUTS
def first():
    pic=os.path.join(app.config['UPLOAD_FOLDER'], 'nature.jpg')
    return render_template("image.html", user_image=pic)

#MAPPING
@app.route('/second')

#INPUTS
def second():
    return render_template("second.html")
# MAIN
if __name__ == "__main__":
    app.run(debug=True)  #debug-->auto. reload page