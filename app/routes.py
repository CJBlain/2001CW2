from flask import Blueprint

# Define the blueprint
main = Blueprint('main', __name__)

@main.route('/')
def home():
    return 'Hello, Flask!'