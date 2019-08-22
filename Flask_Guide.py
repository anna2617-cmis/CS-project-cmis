from flask import Flask, render_template 
app = Flask(__name__) # variable 

planners = [
    {
        'due_date': 'A day',
        'reminder_time': 'D day', 
        'subject': 'Chemistry', 
        'content': 'work book'
    }, 
    {
        'due_date': 'A day',
        'reminder_time': 'D day', 
        'subject': 'English', 
        'content': 'essay'
    }

]
@app.route('/') # route() used to bind URL to a function 
@app.route('/home') 
# @app.route('/<name>')
# variables can be added to pass the parameter, in thsi case, it will be <name>
# ex: %s ' %'variable name' 
def home():
   return  render_template('home.html', planners = planners)#html source code 

@app.route('/about')
def about():
    return render_template('about.html', title = 'Anna')

if __name__ == '__main__':
   app.run(debug = True) # runs the app on particular development server 
  # app.run (host, ports, options)

# Host: Hostname to listen on. Defaults to 127.0.0.1 (localhost). Set to ‘0.0.0.0’ to have server available externally

# Port: Defaults to 5000

# Debug:Defaults to false. If set to true, provides a debug information

# Options:To be forwarded to underlying Werkzeug server.


