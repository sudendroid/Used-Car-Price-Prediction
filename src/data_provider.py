import pickle
import numpy as np
import json

__used_car_data_columns = None
__used_car_brands = None
__used_car_variants = None
__used_car_cities = None
__used_car_evaluation_model = None


def evaluate_used_car(km_driven, reg_year, owner_type, variant_name, location):
    print("km driven = {}, reg year = {}, owner type = {}, variant name = {}, location = {}".format(km_driven, reg_year,
                                                                                                    owner_type,
                                                                                                    variant_name,
                                                                                                    location))
    # convert owner type to actual column name
    owner_dict = {1: 'first', 2: 'second', 3: 'third', 4: 'fourth & above'}

    owner_type = owner_dict[owner_type]
    years_old = 2020 - reg_year

    try:
        loc_index_name = __used_car_data_columns.index(variant_name.lower())
        loc_index_location = __used_car_data_columns.index(location.lower())
        loc_index_owner = __used_car_data_columns.index(owner_type.lower())
    except:
        loc_index_name = -1
        loc_index_location = -1
        loc_index_owner = -1

    x = np.zeros(len(__used_car_data_columns))
    x[0] = km_driven
    x[1] = years_old
    if loc_index_name >= 0:
        x[loc_index_name] = 1
    if loc_index_location >= 0:
        x[loc_index_location] = 1
    if loc_index_owner >= 0:
        x[loc_index_owner] = 1

    return round(__used_car_evaluation_model.predict([x])[0], 2)


def get_used_car_names():
    load_saved_artifacts()
    return __used_car_variants


def get_used_car_cities():
    load_saved_artifacts()
    return __used_car_cities


def load_saved_artifacts():
    print("loading saved artifacts...start")
    global __used_car_data_columns
    global __used_car_brands
    global __used_car_variants
    global __used_car_cities

    with open("model/used_car_columns_info.json", "r") as f:
        column_json = json.load(f)
        __used_car_data_columns = column_json['data_columns']
        __used_car_brands = column_json['brand_names']
        __used_car_variants = column_json['variant_names']
        __used_car_cities = column_json['locations']

    global __used_car_evaluation_model
    if __used_car_evaluation_model is None:
        with open('model/used_car_evaluation_model.pickle', 'rb') as f:
            __used_car_evaluation_model = pickle.load(f)
    print("loading saved artifacts...done")
