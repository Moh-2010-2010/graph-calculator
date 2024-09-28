from flask import Flask, render_template

app = Flask(__name__)

# Define the route for the home page
@app.route('/')
def home():
    return render_template('index.html')  # Render the HTML page

# Run the app in debug mode (for development purposes)
if __name__ == '__main__':
    app.run(debug=True)
 