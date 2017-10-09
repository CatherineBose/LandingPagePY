from flask import Flask, render_template  # Import Flask to allow us to create our app, and import
                                          # render_template to allow us to render index.html.
app = Flask(__name__)                     # Global variable __name__ tells Flask whether or not we
                                          # are running the file directly or importing it as a module.
@app.route('/')    
        
def home_page():
  return render_template('index.html')    

@app.route('/ninjas')
def about():
  return render_template('ninja.html')

@app.route('/dojos/new')
def projets():
  return render_template('dojo.html')
app.run(debug=True)                             
