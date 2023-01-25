import json
import requests
import pprint

base_url = "https://fakestoreapi.com"

def getProduct():
    headers_dict = {'Content-Type': 'application/json'}
    parameters = {'limit': 3}
    response = requests.get(f"{base_url}/products", params=parameters, headers = headers_dict)

    if (response.status_code == 200):
        return response.json()
    return {}

def creatProduct(new_product):
    response = requests.post(f"{base_url}/products", json=new_product)
    return response.json()


def editProduct(id):
    updated_product = {
        "title": 'updated_product',
        "category": 'clothing'
    }
    response = requests.put(f"{base_url}/products/{id}", json=updated_product)
    return response.json()

def updatOneFieldProduct(id):
    updated_product = {
        "category": "electronic"
    }
    response = requests.patch(f"{base_url}/products/{id}", json=updated_product)
    return response.json()

def deleteProduct(id):
    response = requests.delete(f"{base_url}/products/{id}")
    return response.json()

new_product = {
    "title": 'new_product',
    "price": 100,
    "description": 'lorem ipsum set',
    "category": 'nothing'
}

print(getProduct())
print(creatProduct(new_product))
print(editProduct(3))   
print(updatOneFieldProduct(3))
print(deleteProduct(3))
