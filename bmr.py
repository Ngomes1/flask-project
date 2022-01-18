#importing users.py onto the script
from users import *
# creating bmr for both men and women.
# keeping it virtually the same as original script just making various functions in order to run it on flask.

def bmr_app(calories):
    calories = calories
    bmr = input("Are you a man or women?:")
    if bmr == "man":
        malebmr = 66 + (6.3 * int(input("put your body Weight here: "))) + (12.9 * int(input("insert height here in inches: "))) - (6.8 * int(input("What is your age? ")))
#creating a variable that would determine how many calories someone is currently expending in a day.
    activity = input("How active are you? Write unactive if you dont workout or are relatively seditary, lighlty active if you work out lightly 1-3 days a week, moderately active if your working out or playing sport or work a physicaly demanding job 3-5days a week, active if you are working out 6-7 days a week, or very active if you work out intesively for 7 days a week: ")
    unactive = malebmr * 1.2
    lightly_active = malebmr * 1.375
    moderately_active = malebmr * 1.55
    active = malebmr * 1.725
    very_active = malebmr * 1.9

    if activity == "unactive":
        calories = unactive
        print(str(unactive) + " Is how many calories you currently need to eat to stay the same.")
    elif activity == "lightly active":
        calories = lightly_active
        print(str(lightly_active) + " Is how many calories you currently need to eat to stay the same.")
    elif activity  =="moderately active":
        calories = moderately_active
        print(str(moderately_active) + " Is how many calories you currently need to eat to stay the same.")
    elif activity == "active":
        calories = active
        print(str(active) + " Is how many calories you need to eat to remain the same.")
    elif activity == "very active":
        calories = very_active
        print(str(very_active) + " Is how many calories you need to eat to remain the same.")
    else:
        print("There seems to have been a mistake please try again and write between these options: unactive, lightly active, moderately active, active, or very active.")

    
    
    if bmr == "woman" or "Woman":
        femalebmr = 655 + (4.3 * int(input("put your body Weight here: "))) + (4.7 * int(input("insert height here in inches: "))) - (4.7 * int(input("What is your age? ")))
        activity = input("How active are you? write unactive if you dont workout or are relatively seditary, lighlty active if you work out lightly 1-3 days a week, moderately active if your working out or playing sport or work a physicaly demanding job 3-5days a week, active if you are working out 6-7 days a week, or very active if you work out intesively for 7 days a week: ")
        unactive = femalebmr * 1.2
        lightly_active = femalebmr * 1.375
        moderately_active = femalebmr * 1.55
        active = femalebmr * 1.725
        very_active = femalebmr * 1.9
        
    if activity == "unactive":
        calories = unactive
        print(str(unactive) + " Is how many calories you currently need to eat to stay the same.")
    elif activity == "lightly active":
        calories = lightly_active
        print(str(lightly_active) + " Is how many calories you currently need to eat to stay the same.")
    elif activity  =="moderately active":
        calories = moderately_active
        print(str(moderately_active) + " Is how many calories you currently need to eat to stay the same.")
    elif activity == "active":
        calories = active
        print(str(active) + " Is how many calories you need to eat to remain the same.")
    elif activity == "very active":
        calories = very_active
        print((very_active) + " Is how many calories you need to eat to remain the same.")
    else:
        print("There seems to have been a mistake please try again and write between these options: unactive, lightly active, moderately active, active, or very active.")

def goal():
    goal = input("If you wish to remain the same then eat the recommended calories if you wish to lose or gain wait please put in your goals! Please write weight loss or gain mass depending on your preference!: ")
    if goal == "weight loss":
        print("For rapid weight lose subtract 1000 calories from your recommended caloric intake. This will lead to roughly a loss of 2 lbs of body weight per week,however it will lead to fatigue and likely make you irritable.For more sustanability a deficit of 500 calories perday or 1 lb per week is recommened.")
    elif goal == "gain mass":
        print("Typically it is well documented to gain mass one will need to eat roughly 1000 calories over their recommended caloric intake. Any more will likely lead to obeseness and detere from the over 'look' of gaining muscle.")
    else:
        print("You may have entered something other then what was requested of you please try again!")

def tracking():
    x = input("Well I hope this was of help to some of you out there good luck on your goals!!If you want to save or track progress press: y ")

# need to add the singles quotes before your variable values because you need ' surrounding  text based values
    if x == "y":
        firstname = input("Write your first name: ")
        lastname = input("Write your last name here: ")
        calories = input("What is your current recommened caloric intake?: ")
        weight = input("Please record you current weight: ")
        goal = input("Please write your current goal.: ")
        goal_progress = input("Put your current progress towards your goals in lbs. If this is your first entry simply write 0.: ")
        timestamp = input("Okay now mark the date of this entry: ")
        ssql = "INSERT INTO users (first,last,calories,weight,goal,goalprogress,timestamp)VALUES('"
        ssql = ssql + firstname + "', '" + lastname + "', '" + calories +"', '" + weight + "', '" + goal + "', '" + goal_progress + "', '" + timestamp +"')"
        #print(ssql)
        conn = sqlite3.connect('bmr.db')
        c= conn.cursor()
        c.execute(ssql)
        conn.commit()
        c.close()
        conn.close()

