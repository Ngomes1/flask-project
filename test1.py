from flask import Flask,render_template,request
 
app = Flask(__name__)
 
@app.route('/form')
def form():
    return render_template('form.html')
 
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
        return render_template('data1.html',form_data = round(calories_needed, 2))
 
 
app.run(host='localhost', port=5000)