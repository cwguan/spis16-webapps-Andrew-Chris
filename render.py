import os
from flask import Flask, url_for, render_template, request

app = Flask(__name__)

@app.route('/')
def render_main():
    return render_template('home.html')



@app.route('/generator')
def render_generator():
    return render_template('generator.html')
    
@app.route('/muscle-group-checklist') #fix this
def render_muscle_group_checklist():
    return render_template('muscle-group-checklist.html')

@app.route('/your-workout') #fix this
def your_workout():
    try:
        bis_result = request.form['bis']
        tris_result = request.form['tris']
        delts_result = request.form['delts']
        pecs_result = request.form['pecs']
        lats_result = request.form['lats']
        core_result = request.form['core']
        quads_result = request.form['quads']
        hammies_result = request.form['hammies']
        workout_result =  workout(bis_result, tris_result, delts_result, pecs_result, lats_result, core_result, quads_result, hammies_result)
        return render_template('your-workout.html', workout=workout_result)
    except ValueError:
        return "Sorry: something went wrong."



@app.route('/exercises') #This one will be a dropdown, need to fix
def render_exercises():
    return render_template('exercises.html')



@app.route('/search')
def render_search():
    return render_template('search.html')
    

    
if __name__=="__main__":
    app.run(debug=False, port=54321)
