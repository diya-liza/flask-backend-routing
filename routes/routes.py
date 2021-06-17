from flask import Blueprint, jsonify, request,render_template

from dao import watch_list
from controller import controller

route = Blueprint('routes', __name__)

@route.route('/')
def index():
    return render_template('index.html')

@route.route('/add', methods=['POST'])
def add_series_route():
    data = request.get_json()
    controller.add_series(data)

@route.route('/all')
def get_watch_list():
    return jsonify(binge_watch_list=watch_list)


@route.route('/<string:ott_platform>')
def get_series_list_by_ott_route(ott_platform):
    controller.get_series_list_by_ott(ott_platform)

# Update a series in the watch list
@route.route('/update/<string:seriesName>', methods=['PUT'])
def update_ott_by_name_route(seriesName):
    data = request.get_json()['new_ott']
    controller.update_ott_by_name(seriesName,data)

# Pass series name and ott_platform with rating value - query parameters
@route.route('/ratings', methods=['PUT'])
def add_ratings_with_name_and_ott_route():
    query_params = request.args.to_dict()
    controller.add_ratings_with_name_and_ott(query_params)

# Remove a series from watch list
@route.route('/remove/<string:seriesName>', methods=['DELETE'])
def remove_series_route(seriesName):
    controller.remove_series(seriesName)
 
# pass series name and ott_platform and delete that item from watch_list
@route.route('/delete',methods=['DELETE'])
def delete_series_route():
    query_params = request.args.to_dict()
    controller.delete_series(query_params)
    
# Create an end point save, which uses pandas and saves watch_list to csv
@route.route('/save', methods=['POST'])
def save_route():
    controller.save()