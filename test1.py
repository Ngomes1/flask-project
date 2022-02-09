from flask import Flask,render_template,request
import sqlite3
 
app = Flask(__name__)
 
@app.route('/home')
def form():
    return render_template('home.html')
 
@app.route('/data/', methods = ['POST', 'GET'])
def bmr_app():
    if request.method == 'GET':
        return f"The URL /data is accessed directly. Try going to '/form' to submit form"
    if request.method == 'POST':
        form_data = request.form
        bmr = form_data["gender"]
        weight = form_data["weight"]
        height = form_data["height"]
        age = form_data["age"]
        activity = form_data["activity"]
    if bmr == "male":
        malebmr = 66 + (6.3 * int(weight )) + (12.9 * int(height)) - (6.8 * int(age))
#creating a variable that would determine how many calories someone is currently expending in a day.
        if activity=="unactive":
          calories_needed= malebmr * 1.2
        elif  activity=="lightly active":
          calories_needed = malebmr * 1.375
        elif activity=="moderately active":
          calories_needed  = malebmr * 1.375
        elif activity=="moderately active":
          calories_needed = malebmr * 1.55
        elif activity=="active":
          calories_needed  = malebmr * 1.725
        elif activity=="very active":
          calories_needed = malebmr * 1.9
        else:
            if bmr == "female":
                femalebmr = 655 + (4.3 * int(weight)) + (4.7 * int(height)) - (4.7 * int(age))
            if activity=="unactive":
                calories_needed= femalebmr * 1.2
            elif  activity=="lightly active":
                calories_needed = femalebmr * 1.375
            elif activity=="moderately active":
                calories_needed = femalebmr * 1.55
            elif activity=="active":
                calories_needed  = femalebmr * 1.725
            elif activity=="very active":
                calories_needed = femalebmr * 1.9
        return render_template('caloric_esitmate.html',form_data = round(calories_needed, 2))

@app.route('/data',method=["GET","POST"])
def users():
    if request.method == 'POST':
        form_data = request.form
        conn = sqlite3.connect("bmr.db")
        c = conn.cursor()
    
        ssql = "INSERT INTO users (first,last,calories,weight,goal,goalprogress,timestamp)VALUES('"
        ssql = ssql + form_data["firstname"] + "', '" + form_data["lastname"] + "', '" + form_data["calories"] +"', '" + form_data["weight"] + "', '" + form_data["goal"] + "', '" + form_data["goal_progress"] + "', '" + form_data["timestamp"] +"')"
        c.execute(ssql)
        conn.commit()
        c.close()
        conn.close()
    return render_template('tracker.html',form_data = ssql)


 
 
app.run(host='localhost', port=5000)