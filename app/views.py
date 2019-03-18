"""
Flask Documentation:     http://flask.pocoo.org/docs/
Jinja2 Documentation:    http://jinja.pocoo.org/2/documentation/
Werkzeug Documentation:  http://werkzeug.pocoo.org/documentation/
This file creates your application.
"""


import os
from flask import render_template, request, redirect, url_for, flash
from app import app, db
from app import models
from app.forms import ProfileForm
import datetime
from werkzeug.utils import secure_filename

@app.route('/')
def home():
    """Render website's home page."""
    return render_template('home.html')
    
@app.route('/about/')
def about():
    """Render the website's about page."""
    return render_template('about.html') 
    
@app.route("/profile", methods=["GET", "POST"])
def profile():
    newProfileForm = ProfileForm()
    
    if request.method == "POST":
        if newProfileForm.validate_on_submit():
            firstname = newProfileForm.firstname.data
            lastname = newProfileForm.lastname.data
            gender = newProfileForm.gender.data
            email = newProfileForm.email.data
            location = newProfileForm.location.data
            bio = newProfileForm.bio.data
            created_on = str(datetime.datetime.now()).split()[0]
                
            photo = newProfileForm.photo.data
            photo_name = secure_filename(photo.filename)
                
            user = ProfileForm(firstname, lastname, gender, email, location, bio, created_on, photo_name)
                
            db.session.add(user)
            db.session.commit()
                
            photo.save(os.path.join(app.config['UPLOAD_FOLDER'],photo_name))
                
            flash("Profile Added", "success")
            return redirect(url_for("profiles"))
        return render_template("profile.html", newProfileForm = newProfileForm)



@app.route("/profiles")
def profiles():
    users = ProfileForm().query.all()
    profiles = []
    
    for user in users:
        profiles.append({"pro_pic": users.photo, "f_name":users.firstname, "l_name": users.lastname, "gender": users.gender, "location":users.location, "id":users.id})
    
    return render_template("profiles.html", profiles = profiles)

@app.route('/profile/<userid>', methods=["GET"])
def view_profile(userid):
    
    #connect to database and fectch user profile
    user = ProfileForm().query.filter_by(id=userid).first()
    return render_template('profile.html', user=user)
    

###################################################################
def flash_errors(form):
    for field, errors in form.errors.items():
        for error in errors:
            flash(u"Error in the %s field - %s" % (
                getattr(form, field).label.text,error), 'danger')

@app.route('/<file_name>.txt')
def send_text_file(file_name):
    """Send your static text file."""
    file_dot_text = file_name + '.txt'
    return app.send_static_file(file_dot_text)


@app.after_request
def add_header(response):
    """
    Add headers to both force latest IE rendering engine or Chrome Frame,
    and also tell the browser not to cache the rendered page. If we wanted
    to we could change max-age to 600 seconds which would be 10 minutes.
    """
    response.headers['X-UA-Compatible'] = 'IE=Edge,chrome=1'
    response.headers['Cache-Control'] = 'public, max-age=0'
    return response


@app.errorhandler(404)
def page_not_found(error):
    """Custom 404 page."""
    return render_template('404.html'), 404


if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port="8080")
