'''
@author: Suyash Srivastava
file to run application in blocking mode
'''
from app import app_trigger

if __name__ == '__main__':
    app_trigger.run(host='127.0.0.1', debug=True)
