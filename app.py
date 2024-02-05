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
            if is_even(session['username']):
                return render_template('index.html', show_question_completion=True, question=lions, q_no=1, problem_bottom=data_dict["binary"][0]["problem_bottom"], problem_hint=data_dict["binary"][0]["problem_hint"], problem_top=data_dict["binary"][0]["problem_top"])
            else:
                return render_template('index.html', show_question_completion=True, question=parking, q_no=1, problem_bottom=data_dict["caesar"][0]["problem_bottom"], problem_hint=data_dict["caesar"][0]["problem_hint"], problem_top=data_dict["caesar"][0]["problem_top"])

        else:
            return render_template('login.html', show_question_completion=False)

    return redirect(url_for('login'))

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username') 
        password = request.form.get('password')
        
        if authenticate_team(username, password):
            session['username'] = username
            session['show_question_completion'] = True
            return redirect(url_for('index'))
        else:
            return jsonify({'success': False, 'message': 'Invalid credentials. Please try again.'})

    return render_template('login.html')

@app.route('/logout')
def logout():
    session.pop('username', None)
    session.pop('show_question_completion', None)
    return redirect(url_for('login'))

@app.route('/reduce_points', methods=['POST'])
def reduce_points(player_id):
    team = request.form.get('team') 
    records.update_one({"team": team}, {"$inc": {"point": -10}})

    return jsonify({'success': True, 'message': f'Reduced 10 points for Player {player_id}'})

if __name__ == '__main__':
    app.run(debug=True, port="0825")