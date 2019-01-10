'''
helper methods
'''
import traceback
from app import app_trigger

def create_response(data):
    '''
    method to create response
    @param[in] query response
    @returns response dictionary
    '''
    response = {}
    try:
        data = data.split('\n')
        response['headers'] = [data[0]]
        response['data_type'] = [data[1]]
        row_data = []
        for val in data[2:]:
            if val:
                row_data.append(val)
        response['values'] = row_data
    except Exception as ex:
        print(ex)
        print("----------------")
        print(traceback.print_exc())
    return response
