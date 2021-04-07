import flask

from flask import Flask, render_template, request


app = Flask(__name__)
app.debug = True


# main page
@app.route('/')
def render_index():
    return render_template('index.html',)


# show us page with all tutors
@app.route('/all/')
def all_page():
    return render_template('all.html')


# show us page with tutors, what depends on var /<goal>
@app.route('/goals/<goal>/')
def goal_page(goal):
    return render_template('goal.html',
                           goal=goal)


# personal tutor page
@app.route('/profiles/<int:id_tutor>/')
def tutor_page(id_tutor):
    return render_template('profile.html',
                           id_tutor=id_tutor)


# tutor selection request page
@app.route('/request/')
def tutor_selection_request():
    return render_template('request.html')


# tutor selection DONE
@app.route('/request_done/')
def tutor_selection_done():
    return render_template('request_done.html')


# contains and handle form of tutor booking
@app.route('/booking/<int:id_tutor>/<day_name>/<booking_time>/')
def booking_form(id_tutor, day_name, booking_time):
    return render_template('booking.html',
                           id_tutor=id_tutor,
                           day_name=day_name,
                           booking_time=booking_time)


# shows us booking done status
@app.route('/booking_done/')
def booking_done_pg():
    return render_template('booking_done.html')


app.run(debug=True)
