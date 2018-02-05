from flask import Flask, jsonify, abort, make_response, request, render_template
from flask.ext.script import Manager
# manager = Manager(app)
import html
app = Flask(__name__)
tasks = [
  {
    'id': 1,
    'title': u'Buy groceries',
    'description': u'Milk, Cheese, Pizza, Fruit, Tylenol',
    'done': False
  },
  {
    'id': 2,
    'title': u'Learn Python',
    'description': u'Need to find a good Python tutorial on the web',
    'done': False
  }
]

@app.errorhandler(404)
def not_found(error):
  return make_response(jsonify({'error': 'not found'}), 404)


@app.route('/')
@app.route('/index')
def index ():
  user = { 'name': '许道斌' }
  return 'hell0'

@app.route('/todo/api/v1.0/tasks/<int:task_id>', methods=['GET'])
def get_tasks(task_id):
  task = []
  for item in tasks:
    if item['id'] == task_id:
      task.append(item)
  if len(task) == 0:
    abort(404)
  return jsonify({'tasks': task[0]})

@app.route('/todo/api/v1.0/tasks', methods=['POST'])
def create_task():
  if not request.json or not 'title' in request.json:
    abort(400)
  task = {
    'id': 0,
    'title': request.json['title'],
    'description': request.json.get('description', ""),
    'done': False
  }
  try:
    task['id'] = tasks[-1]['id'] + 1
  except:
    task['id'] = 1
  tasks.append(task)
  return jsonify({'task': tasks}), 200


@app.route('/todo/api/v1.0/tasks/<int:task_id>', methods=['PUT'])
def update_task(task_id):
  task = []
  for item in tasks:
    if item['id'] == task_id:
      task.append(item)
  if len(task) == 0:
    abort(404)
  if not request.json:
    abort(400)
  if not 'title' in request.json:
    abort(400)
  if not 'description' in request.json:
    abort(400)
  if not 'done' in request.json or type(request.json['done']) != bool:
    abort(400)
    
  task[0]['title'] = request.json['title']
  task[0]['description'] = request.json['description']
  task[0]['done'] = request.json['done']
  return jsonify({'task':task[0]})

@app.route('/todo/api/v1.0/tasks/<int:task_id>', methods=['DELETE'])
def delte_task (task_id):
  if not task_id:
    abort(404)
  for item in tasks:
    if task_id == item['id']:
      tasks.remove(item)
  return jsonify({'tasks': tasks})

if __name__ == '__main__':
  app.run(debug=True)