import sqlite3
#The code bellow creates the connection between a database and the existing file (aka the bmr file)
conn = sqlite3.connect('bmr.db')
#creating a "cursor" in order to execute sqlite commands to the database.
c = conn.cursor()
# the capital letters tells sqlite what to do after
# after running it feel free to commit out the c.excute creating table function or you will run into an error saying it already exists...

#c.execute("""CREATE TABLE users (
        #first text,
        #last text,
        #calories real
        #)""")
#c.execute
#altering table by using the ALTER command replacing the create in order to add more rows.
#c.execute("""ALTER table users (
        #ADD COLUMN weight real,
        #ADD COLUMN goal text,
        #ADD COLUMN goal_progress real,
        #ADD COULMN timestamp real
        #)""")

# 'committing' the changes with the next step *crucial to do this step* then 'closing' the connection
#creating information to Store onto the table.
#c.execute(" INSERT INTO users VALUES ('Nick' , 'Gomes', 3028.26, 220, 'weight loss', 0, '1/17/2022')") 
#<-- (had to be hash taged out in order for it to not throw the error already exists.)
#c.execute("INSERT INTO users VALUES ('Daffy', 'Duck', 4000)")
#c.execute("SELECT * FROM users")

#print(c.fetchone())
#print(c.fetchall())

conn.commit()
conn.close()

