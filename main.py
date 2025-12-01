from flask import Flask, render_template, request, redirect, url_for, flash

app = Flask(__name__)

# Secret key is required for session management (used by flash messages)
app.secret_key = 'your_secret_key_here'

@app.route('/')
def index():
    """Renders the main homepage."""
    return render_template('index.html')

@app.route('/submit_contact', methods=['POST'])
def submit_contact():
    """
    Handles the contact form submission.
    In a real app, you would save this to a database or send an email.
    """
    if request.method == 'POST':
        # Extract data from form
        full_name = request.form.get('full_name')
        service = request.form.get('service')
        
        # Flash a success message to the user
        flash(f"Thanks, {full_name}! We received your request for the '{service}' package. We will call you shortly.", "success")
        
        # Redirect back to the homepage
        return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)