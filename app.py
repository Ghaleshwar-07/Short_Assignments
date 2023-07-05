from flask import Flask
from login_routes import login_blueprint

app = Flask(__name__)
app.register_blueprint(login_blueprint)

#We can also run in default Development Server by Using
#mode= "dev"

if __name__ == '__main__':
#    if mode == "dev":
#        app.run(host='0.0.0.0', port=50100, debug=True)
    app.run()
    
