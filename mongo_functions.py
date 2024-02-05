import random
import string
from termcolor import colored
from pymongo import MongoClient
import os

mongo_url = os.environ.get('MONGO_URL')
client = MongoClient(mongo_url)

db = client.get_database("aiconclave_team_final")
records = db.team_records

# FUNCTIONS
def generate_random_password():
    return ''.join(random.choices(string.ascii_uppercase + string.digits, k = 6))

def get_team(team):
    return records.find_one({"team": team})

def add_team(team):
    password = ''.join(random.choices(string.ascii_uppercase + string.digits, k = 6))
    index_number = records.find_one(sort=[('_id', -1)])["id"]
    my_dict = {
        "team": team,
        "password": password,
        "lion": False,
        "parking": False,
        "point": 50,
        "id":index_number+1,
        "login_count": 0,
    }
    try:
        records.insert_one(my_dict)
        print(colored("Inserting: ", 'green'), my_dict)
        
        return f"Team Name: {team}, Password: {password}"
    
    except Exception as e:
        print(colored("Error: ", 'red'), e)
        
def drop_team(team):
    records.delete_one({"team": team})
    print(colored("Dropping: ", 'green'), team)
    
    return f"Team {team} has been dropped."

def modify_place_visited(team, place, value):
    records.update_one({"team": team}, {"$set": {place: value}})
    
def count_place_visited(team):
    team = get_team(team)
    return team["parking"]+team["lion"]

def place_visited(team):
    my_list = []
    team = get_team(team)
    if team["lion"] == True:
        my_list.append("lion")
    if team["parking"] == True:
        my_list.append("parking")
    else:
        return "None"
    
    return my_list

def place_not_visited(team):
    my_list = []
    team = get_team(team)
    if team["parking"] == False:
        my_list.append("parking")
    if team["lion"] == False:
        my_list.append("lion")
    else:
        return "None"
    
    return my_list

def authenticate_team(team, password):
    team = get_team(team)
    if team["password"] == password:
        return True
    else:
        return False
    
def is_even(team):
    team_data = get_team(team)
    if team_data and 'id' in team_data:
        return team_data['id'] % 2 == 0
    else:
        return False
    
def increase_login_count(team):
    return records.update_one({"team": team}, {"$inc": {"login_count": 1}})

def return_login_count(team):
    team = get_team(team)
    if team and 'login_count' in team:
        return team["login_count"]
    else:
        return 0
    
def return_last_id():
    return records.find().sort([("id", -1)]).limit(1)[0]["id"]