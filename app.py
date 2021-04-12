import random, pprint

import json

import flask

from flask import Flask, render_template, request

from flask_wtf import FlaskForm

from wtforms import StringField


app = Flask(__name__)
app.debug = True


with open('teachers.json', 'r', encoding='utf-8') as f:
    teachers = json.load(f)
    id_teacher_list = [i for i in teachers if i['id'] == 4][0]
    print(id_teacher_list['id'])


with open('dayname.json', 'r', encoding='utf-8') as f:
    dayname = json.load(f)
    eng_dayname = list(dayname.keys())
    print(eng_dayname)


p = "12:00"
p = p.partition(':')[0]
print(p)
for s in id_teacher_list['free'].keys():
    print(s)

time = "02:00"
if time[0] == '0':
    time = time[1]
    print(time)
else:
    time = time[0] + time[1]
    print(time)

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
#for tutor_dict in
def tutor_page(id_tutor):
    with open('teachers.json', 'r', encoding='utf-8') as f:
        teachers = json.load(f)
        id_teacher_list = [i for i in teachers if i['id'] == id_tutor][0]
        print(id_teacher_list['free'].keys())

    return render_template('profile.html',
                           id_tutor=id_tutor,
                           id_teacher_list=id_teacher_list,
                           dayname=dayname,
                           eng_dayname=eng_dayname)


# tutor selection request page
@app.route('/request/')
def tutor_selection_request():
    return render_template('request.html')


# tutor selection DONE
@app.route('/request_done/')
def tutor_selection_done():
    return render_template('request_done.html')


# contains and handle form of tutor booking
@app.route('/booking/<int:id_tutor>/<day_name_link>/<booking_time>/', methods=["GET", "POST"])
def booking_form(id_tutor, day_name_link, booking_time):
    teacher_name = [i for i in teachers if i['id'] == id_tutor][0]['name']
    ru_dayname = dayname[day_name_link]

    return render_template('booking.html',
                           id_tutor=id_tutor,
                           day_name_link=day_name_link,
                           ru_dayname=ru_dayname,
                           teacher_name=teacher_name,
                           booking_time=booking_time)


# shows us booking done status
@app.route('/booking_done/', methods=["GET", "POST"])
def booking_done_pg():
    cWeekday = request.form["clientWeekday"]
    cTime = request.form["clientTime"]
    cTeacher = request.form["clientTeacher"]
    clientName = request.form["clientName"]
    clientPhone = request.form["clientPhone"]
    print(f'weekday is {cWeekday}\n  time {cTime} \n teacher id is {cTeacher}\n  '
          f'my name is {clientName}\n  tel is {clientPhone}')
    return render_template('booking_done.html',
                           dayname=dayname,
                           cWeekday=cWeekday,
                           cTime=cTime,
                           cTeacher=cTeacher,
                           clientName=clientName,
                           clientPhone=clientPhone)


app.run(debug=True)
