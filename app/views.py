'''
@author: Suyash
This file contains all the view functions linked to urls
'''
from flask_restful import Resource, Api, reqparse
from flask import request, jsonify
from app import app_trigger

api = Api(app_trigger)
parser = reqparse.RequestParser()

# all url handlers goes here

class AppHealth(Resource):
    '''
    AppHealth health method
    '''
    def get(self):
        '''
        HTTP GET method
        '''
        return {"Alive": True}

# url handlers end here

from app.urls import APIClass
APIClass()
