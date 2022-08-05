from flask import Flask
import view

# SERVER
app = Flask(__name__)

# Create secrete key 'The secret key is needed to keep the client-side sessions secure.'
app.secret_key = "secret key"

# Register views
app.register_blueprint(view.router)

# Inicialize server
if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True) 

    