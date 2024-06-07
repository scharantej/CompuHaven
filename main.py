
# Import necessary modules.
from flask import Flask, render_template, request, redirect, url_for

# Create a Flask application.
app = Flask(__name__)

# Define the route for the landing page.
@app.route('/')
def index():
    return render_template('index.html')

# Define the route for the product details page.
@app.route('/product/<product_id>')
def product_details(product_id):
    return render_template('product_details.html', product_id=product_id)

# Define the route for the 'About Us' page.
@app.route('/about-us')
def about_us():
    return render_template('about_us.html')

# Define the route for the 'Contact Us' page.
@app.route('/contact-us')
def contact_us():
    return render_template('contact_us.html')

# Run the Flask application.
if __name__ == '__main__':
    app.run(debug=True)
