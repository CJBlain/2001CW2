import sys
sys.path.append('./app')  # This tells Python to also look in the 'app' folder for modules

from app import create_app

app = create_app()

if __name__ == "__main__":
    app.run(debug=True)