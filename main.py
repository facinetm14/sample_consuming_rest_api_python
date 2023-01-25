import json
import requests
#import pprint

base_url = "https://fakestoreapi.com"

def get_product():
    headers_dict = {'Content-Type': 'application/json'}
    parameters = {'limit': 3}
    response = requests.get(f"{base_url}/products", params=parameters, headers = headers_dict)

    if (response.status_code == 200):
        return response.json()
    return {}

def creat_product(new_product):
    response = requests.post(f"{base_url}/products", json=new_product)
    return response.json()


def edit_product(id):
    updated_product = {
        "title": 'updated_product',
        "category": 'clothing'
    }
    response = requests.put(f"{base_url}/products/{id}", json=updated_product)
    return response.json()

def updat_one_field_product(id):
    updated_product = {
        "category": "electronic"
    }
    response = requests.patch(f"{base_url}/products/{id}", json=updated_product)
    return response.json()

def delete_product(id):
    response = requests.delete(f"{base_url}/products/{id}")
    return response.json()

new_product = {
    "title": 'new_product',
    "price": 100,
    "description": 'lorem ipsum set',
    "category": 'nothing'
}

print(get_product())
print(creat_product(new_product))
print(edit_product(3))   
print(updat_one_field_product(3))
print(delete_product(3))
