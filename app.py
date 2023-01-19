# Importing flask module from Flask package.
from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)  # Intialising App

app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///todo.db" # Intialising Sequel Alchemy
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app) # Creating Database using class for telling Flask what we are storing.

class Todo(db.Model): # Creating our tables columns.
    sno = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    desc = db.Column(db.String(500), nullable=False)
    date_created = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self) -> str:
        return f"{self.sno} - {self.title}"

# Creating Routes
@app.route("/", methods=['GET', 'POST']) # If we post by any route we have to provide method
def hello_world():
    if request.method=='POST':
        
        title = request.form['title'] # print("post")
        desc = request.form['desc']

        todo = Todo(title=title, desc = desc)
        db.session.add(todo) # Data will be written into the database successfully.
        db.session.commit()
    
    allTodo = Todo.query.all() # Displaying Todo's
    return render_template('index.html', allTodo = allTodo) # Rendering Html and displaying our Templates

@app.route("/about",methods=['GET'])
def about():
    return render_template('about.html')

# @app.route("/lis",methods=['GET']')
@app.route("/lis",methods=['GET'])
def lis():
    return render_template('LostinSpace.html')

@app.route("/flappybird",methods=['GET'])
def fb():
    return render_template('FlappyBird.html')

@app.route("/taskAssistant",methods=['GET'])
def ta():
    return render_template('week0.html')

# routes of weeks for Task Assistant

@app.route("/taskAssistant/week1")
def week1():
    return render_template('week1.html')

@app.route("/taskAssistant/week2")
def week2():
    return render_template('week2.html')

@app.route("/taskAssistant/week3")
def week3():
    return render_template('week3.html')

@app.route("/taskAssistant/week4")
def week4():
    return render_template('week4.html')

@app.route("/taskAssistant/week5")
def week5():
    return render_template('week5.html')

@app.route("/taskAssistant/week6")
def week6():
    return render_template('week6.html')

@app.route("/taskAssistant/week7")
def week7():
    return render_template('week7.html')

@app.route("/taskAssistant/week8")
def week8():
    return render_template('week8.html')

@app.route("/taskAssistant/week9")
def week9():
    return render_template('week9.html')

@app.route("/taskAssistant/week10")
def week10():
    return render_template('week10.html')

@app.route("/taskAssistant/week11")
def week11():
    return render_template('week11.html')

# Creating Post Requests
@app.route("/show") # /show is used to show the todo's
# def products():
#     allTodo = Todo.query.all() # Printing Todo's
#     print(allTodo)
#     return "<p>This is products page.</p>"

@app.route("/videos")
def products():
    return redirect("/static/best_animation.mp4")

@app.route('/update/<int:sno>', methods=['GET', 'POST']) # /update is used to edit the todo's
def update(sno):
    if request.method=='POST':
        title = request.form['title'] # print("post")
        desc = request.form['desc']
        todo = Todo.query.filter_by(sno=sno).first() 
        todo.title = title
        todo.desc = desc
        db.session.add(todo) # Data will be written into the database successfully.
        db.session.commit()
        return redirect("/")

    todo = Todo.query.filter_by(sno=sno).first()  # Editing To-do
    return render_template('update.html', todo=todo) 
    

@app.route("/delete/<int:sno>") # /delete is used to complete the todo's and will do so by take S. no.
def delete(sno): #and then deleting it.
    todo = Todo.query.filter_by(sno=sno).first() # Completing Todo's, .first() selecting first record for deleting
    db.session.delete(todo)
    db.session.commit()
    return redirect("/")



# Running our Web App
if __name__ == "__main__":
    app.run(debug=True, port=8000)
