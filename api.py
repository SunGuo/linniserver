#-*-coding:utf8 -*-


from flask import Flask,request, jsonify
from flask_restful import reqparse, abort, Api, Resource
from models import users

app = Flask(__name__)
api = Api(app)

TODOS = {
 'todo1' : {'task':'build an API'},
 'todo2' : {'task' :  '????'},
 'todo3' : {'task' : 'profit'}
}

def test():
    pass

def abort_if_todo_doesnt_exist(todo_id):
    if todo_id not in TODOS:
        abort(404, message = "Todo {} doest`t exist".format(todo_id))

parser = reqparse.RequestParser()
parser.add_argument('task')

class todo(Resource):
    def get(self, todo_id):
        abort_if_todo_doesnt_exist(todo_id)
        return TODOS[todo_id]

    def delete(self, todo_id):
        abort_if_todo_doesnt_exist(todo_id)
        del TODOS[todo_id]
        return '', 204
    def put(self, todo_id):
        args  = parser.parse_args()
        task = {'task' : args['task']}
        TODOS[todo_id] = task
        return task, 201

class todo_list(Resource):
    def get(self):
        return TODOS

    def post(self):
        args = parser.parse_args()
        todo_id = int(max(TODOS.keys()).lstrip('todo')) + 1
        todo_id = 'todo%i' % todo_id
        TODOS[todo_id] = {'task': args['task']}
        return TODOS[todo_id], 201


class users_action(Resource):

    def get(self):
        users1 = users.User.query.all()
        return jsonify(users = [u1.to_json() for u1 in users1])

class user_login(Resource):
    def get(self, username):
        users1 = users.User.query.filter_by(username = username).first()
        if users1 is not None:
            return {'flag': True}
        else:
            return {'flag': False}

    def put(self):
        pass


class user_register(Resource):
    def put(self, phonenum, pwd):
        try:
            user = users.User(username = phonenum, phonenum = phonenum, pwd)
            users.db.session.add(user)
            users.db.session.commit()
            return {'flag' : True}
        except Exception, e:
            return {'flag' : False}



api.add_resource(todo_list, '/todos')
api.add_resource(todo, '/todos/<todo_id>')
api.add_resource(users_action, '/users')
api.add_resource(user_login, '/users/<username>')
api.add_resource(user_register, '/users/')

#api.add_resource(helloworld, '/')

if __name__ == '__main__':
    app.run(debug = True)
