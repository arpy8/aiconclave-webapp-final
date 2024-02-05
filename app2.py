from termcolor import colored
from flask import Flask, render_template, request, redirect, url_for, session, jsonify

from consts import *
from mongo_functions import *

# AIC297 lion->parking
# AIC792 parking->lion

app = Flask(__name__)
app.config['SECRET_KEY'] = '825'

@app.route('/')
def index():
    if 'username' in session:
        show_question_completion = session.pop('show_question_completion', False)
        
        if show_question_completion:
            if session['username'] is not None:
                if is_even(session['username']):
                    if str(session['code']).strip().lower()=="aic792":
                        return render_template('index.html', show_question_completion=True, question=lions, q_no=2, problem_bottom=data_dict["binary"][0]["problem_bottom"], problem_hint=data_dict["binary"][0]["problem_hint"], problem_top=data_dict["binary"][0]["problem_top"])
                    elif str(session['code']).strip().lower()=="aic297":
                        return render_template('index.html', show_question_completion=True, question=parking, q_no=2, problem_bottom=data_dict["cesar"][0]["problem_bottom"], problem_hint=data_dict["cesar"][0]["problem_hint"], problem_top=data_dict["cesar"][0]["problem_top"])
                    else:
                        return jsonify({'success': False, 'message': 'Invalid code.'})
        else:
            return render_template('login2.html', show_question_completion=False)

    return redirect(url_for('login'))

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username') 
        code = request.form.get('code')

        print(colored(f'username: {username}, code: {code}', 'green'))

        if get_team(username)["login_count"]==-1:
            return jsonify({'success': False, 'message': 'Team already logged out.'})
            
        if code is not None:
            code = code.strip()
        else:
            return jsonify({'success': False, 'message': 'Code is required in the form data.'})
        
        if code.lower().strip() not in ['aic297', 'aic792']:
            return jsonify({'success': False, 'message': f'Invalid code: {code}'})

        elif code.lower().strip() in ['aic297', 'aic792']:
            session['username'] = username
            session['show_question_completion'] = True
            session['code'] = code
            
            modify_place_visited(username, 'lion' if code.lower().strip()=="aic297" else 'parking', True)
            
            if len(place_visited(username)) == 2:
                return render_template('proceed_to_3.html')
            
            elif len(place_visited(username)) == 1:
                return redirect(url_for('index'))
            
            return redirect(url_for('login'))
        
        else:
            return jsonify({'success': False, 'message': 'Invalid credentials. Please try again.'})

    return render_template('login2.html')


@app.route('/reduce_points', methods=['POST'])
def reduce_points():
    team = request.form['team']
    records.update_one({"team": team}, {"$inc": {"point": -10}})

    return render_template('end.html', message=f'Reduced 10 points for Team {team}')

@app.route('/the_road_not_taken', methods=['GET', 'POST'])
def the_choice():
    session['choice'] = True
    return render_template('left_right.html')

@app.route('/end', methods=['GET', 'POST'])
def end():
    if not session['choice']:
        team = request.form['team']
        session['choice'] = False
        records.update_one({"team": team}, {"$inc": {"point": 10}})
        updated_points = records.find_one({"team": team})["point"]
        
        records.update_one({"team": session['username']}, {"$set": {"login_count": -1}})
        
        return render_template('end.html', message=f'Increased 10 points for Team {team}. Updated points: {updated_points}')
    
    return render_template('end.html')

@app.route('/scoreboard', methods=['GET', 'POST'])
def scoreboard():
    return render_template('scoreboard.html', leaderboard_data=records.find().sort("point", -1))

@app.route('/logout')
def logout():
    session.pop('username', None)
    session.pop('show_question_completion', None)
    records.update_one({"team": session['username']}, {"$set": {"login_count": -1}})
    
    return redirect(url_for('login'))


if __name__ == '__main__':
    app.run(debug=True, port="0825")