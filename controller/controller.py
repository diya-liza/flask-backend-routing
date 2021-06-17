def add_series(data):
    
    watch_list.append(data)
    return {'message': 'Added succefully..'}, 201


def get_series_list_by_ott(ott_platform):
    
    # Retrieve list of series from watch_list based on ott_platform
    ott_list =[series_name['name'] for series_name in watch_list if series_name['ott']==ott_platform]
    return jsonify(ott=ott_list)

def update_ott_by_name(seriesName,data):
    for items in watch_list:
        if(items['name']==seriesName):
            items['ott']=data
    return jsonify(updated="done")

def add_ratings_with_name_and_ott(query_params):
    indexes = [item for item in watch_list if item['name']==query_params['name'] and item['ott']==query_params['ott']]
    for item in watch_list:
        if item==indexes[0]:
            item['ratings']=query_params['rating']
    return jsonify(rating_added="added")

def remove_series(seriesName):
    items = [item for item in watch_list if item['name']==seriesName]
    for item in items:
        watch_list.remove(item)
    return jsonify(item_removed=items)

def delete_series(query_params):
    indexes = [item for item in watch_list if item['name']==query_params['name'] and item['ott']==query_params['ott']]
    watch_list.remove(indexes[0])
    return jsonify(message="removed")

def save():
    DF = pd.DataFrame(watch_list)
    DF.to_csv("data1.csv")
    return jsonify(message="saved")