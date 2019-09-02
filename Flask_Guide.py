from flask import Flask, render_template, redirect, url_for, request
app = Flask(__name__) # variable 

@app.route('/admin') # route() used to bind URL to a function ; instance of the class 
def hello_world():
    return 'hello world' 
#app.add_url_rule('/', 'hello',hello_world) another way to bind url 


@app.route('/hello/<guest>') 
# variables can be added to pass the parameter, in thsi case, it will be <name>
# ex: %s ' %'variable name' 
def hello_guest(guest):
    return render_template('hello.html', name = guest)
    #return  render_template('home.html', planners = planners)#html source code 

@app.route('/user/<name>')
def hello_user(name): 
    if name == 'admin': 
        return redirect(url_for('hello_world')) #redirects the url 
    else: 
        return redirect(url_for('hello_guest', guest = name))

@app.route('/login', methods = ['POST', 'GET'])
def login(): 
    if request.method == 'POST': 
        user = request.form['nm']
        return redirect(url_for('hello_guest', guest = user))
    else: 
        user = request.args.get('nm')
        return redirect(url_for('hello_guest', guest = user))

@app.route('/result')
def result():
   dict = {'phy':50,'che':60,'maths':70}
   return render_template('result.html', result = dict)

if __name__ == '__main__':
   app.run(debug = True) # runs the app on particular development server 
  # app.run (host, ports, options)

# Host: Hostname to listen on. Defaults to 127.0.0.1 (localhost). Set to ‘0.0.0.0’ to have server available externally

# Port: Defaults to 5000

# Debug:Defaults to false. If set to true, provides a debug information

# Options:To be forwarded to underlying Werkzeug server.


