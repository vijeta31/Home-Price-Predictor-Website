import json
import pickle
import numpy as np

__locations = None
__data_col = None
__model = None


def get_location_names():
    return __locations



def get_estimated_price(location,sqft,bhk,bath):
    try:
        loc_index =__data_col.index(location.lower())
    except:
        loc_index = -1
    z = np.zeros(len(__data_col))
    z[0] = sqft
    z[1] = bath
    z[2] = bhk
    if loc_index >= 0:
        z[loc_index] = 1
    return round(__model.predict([z])[0],2)


def load_saved_artifacts():
    print("Load saved artifacts.... starts......")
    global  __data_col
    global  __locations

    with open("./artifacts/columns.json",'r') as f:
        __data_col=json.load(f)['data_columns']
        __locations= __data_col[3:]

    global __model

    with open("./artifacts/banglore_home_price.pickle",'rb') as f:
        __model = pickle.load(f)
    print("Loading the artifacts is done")



if __name__ == "__main__":
    load_saved_artifacts()
    print(get_location_names())
    print(get_estimated_price('1st Phase JP Nagar',1000,3,3))
    print(get_estimated_price("1st Phase JP Nagar",1000,2,2))
    print(get_estimated_price("Kalhalli",1000,2,2))
    print(get_estimated_price("Ejipura",1000,2,2))