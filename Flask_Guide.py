from flask import Flask

app = Flask(__name__)

@app.route('/') # route() used to bind URL to a function 

# @app.route('/<name>')
# variables can be added to pass the parameter, in thsi case, it will be <name>
# ex: %s ' %'variable name' 


def hello_world():
   return "Hello World"

if __name__ == '__main__':
   app.debug = True
   app.run(host="0.0.0.0", port = 5000, debug = True) # runs the app on particular development server 
  # app.run (host, ports, options)

# Host: Hostname to listen on. Defaults to 127.0.0.1 (localhost). Set to ‘0.0.0.0’ to have server available externally

# Port: Defaults to 5000

# Debug:Defaults to false. If set to true, provides a debug information

# Options:To be forwarded to underlying Werkzeug server.

