from flask import Flask, jsonify, request
from app import app
from models import bugs, Bug
from datetime import datetime, timedelta
import random

request_counter = 0

def _get_bug_dict(bug):
    bug_info = {
        'bug_id': bug.bug_id,
        'created_by': bug.created_by,
        'created_on': bug.created_on.strftime('%Y-%m-%d %H:%M:%S'),
        'updated_on': bug.updated_on.strftime('%Y-%m-%d %H:%M:%S'),
        'priority': bug.priority,
        'severity': bug.severity,
        'title': bug.title,
        'description': bug.description
    }

    return bug_info

@app.route('/', methods=['GET'])
def welcome():
    return "Welcome to the Bug Tracking API!"

@app.route('/bugs', methods=['GET'])
def get_bugs():
    
    bug_list = []
    
    for bug in bugs:
        bug_list.append(_get_bug_dict(bug))
    
    return jsonify(bug_list), 200


@app.route('/bugs/<int:bug_id>', methods=['GET'])
def get_bug(bug_id):
    bug = next((b for b in bugs if b.bug_id == bug_id), None)
    
    if bug:
        return jsonify(_get_bug_dict(bug)), 200
    else:
        return jsonify({'error': 'Bug not found'}), 404

@app.route('/bugs', methods=['POST'])
def create_bug():
    data = request.json

    new_bug = Bug(
        data['created_by'], 
        data['priority'], 
        data['severity'], 
        data['title'], 
        data['description']
    )
    bugs.append(new_bug)

    return jsonify(_get_bug_dict(new_bug)), 201

@app.route('/bugs/<int:bug_id>', methods=['PUT'])
def update_bug(bug_id):
    bug = next((b for b in bugs if b.bug_id == bug_id), None)
    if not bug:
        return jsonify({'error': 'Bug not found'}), 404

    data = request.json
    bug.created_by = data.get('created_by', bug.created_by)
    bug.priority = data.get('priority', bug.priority)
    bug.severity = data.get('severity', bug.severity)
    bug.title = data.get('title', bug.title)
    bug.description = data.get('description', bug.description)
    bug.updated_on = datetime.utcnow()

    return jsonify(_get_bug_dict(bug)), 200


@app.route('/bugs/<int:bug_id>', methods=['DELETE'])
def delete_bug(bug_id):
    bug = next((b for b in bugs if b.bug_id == bug_id), None)
    if not bug:
        return jsonify({'error': 'Bug not found'}), 404

    deleted_bug_id = bug.bug_id
    bugs.remove(bug)

    deleted_bug = {
        'message': 'Bug deleted',
        'bug_id': deleted_bug_id
    }

    return jsonify(deleted_bug), 200

