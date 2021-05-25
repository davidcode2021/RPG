from flask import Flask 
app = Flask(__name__)

@app.route ("/")
def hello_world():
    return"<b> welcome home </b> "

@app.route("/product")
def my_product():
    return"<b> This is our product. Abeg patronize us </b>"

@app.route("/services")
def our_services ():
    return"<b> we offer the best services, in the world </b>"

@app.route("/contact")
def our_contact():
    return"<b> you can meet us at Amadu bello way, Jos<b>"
    
@app.route("/aboutus")
def know_us():
    return"<b> we are who we are</b>"