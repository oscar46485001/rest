from flask_restful import abort, Api, fields, marshal_with, reqparse, Resource
from flask import request
class HelloWorld(Resource):
    def get(self):
        return {'hello': 'world'}

todos = {'todo1':'Example1'}

class TodoSimple(Resource):
    def get(self, todo_id):
        return {todo_id: todos[todo_id]}

    def put(self, todo_id):
        todos[todo_id] = request.form['data']
        return {todo_id: todos[todo_id]}

cars = [{'plate': '6MBV006'},
          {'plate': '5BBM299'},
          {'plate': '5AOJ231'}]

class Car(Resource):
    def get(self):
        print("GET")
        return cars

    def put(self):
        cars.append(request.form['data'])
        return request.form['data']

    def post(self):
        print("POST")
        print(request.get_json())
        cars.append(request.get_json())
        print("Added")
        return "Car Added"

