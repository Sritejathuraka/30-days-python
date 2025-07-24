import requests

base_url = "http://localhost:3000/pantry"
#GET METHOD
def get_method_request(url):
    response = requests.get(url)
    print("GET RESULTS", response.json())

#POST METHOD
def post_method_request(url):
    new_item = {
    "id": "8",
    "category": "vegetables",
    "items": {
      "tomatoes": "500 grams",
      "carrots": "250 grams",
      "green pepper": "100 grams"
    }
  }
    post_results = requests.post(url, json=new_item )  
    print("POST RESULTS", post_results.json())
#PUT METHOD
def put_method_request(url):
    new_item = {
    "id": "6",
    "category": "spices",
    "items": {
      "chillipowder": "500 grams",
      "pepper powder": "250 grams"
    }
  }
    put_results = requests.put(f"{url}/6", json=new_item )  
    print("PUT RESULTS", put_results.json())
#DEL METHOD
def delete_method_request(url):
    del_results = requests.delete(f"{url}/6") 
    print("DEL RESULTS", del_results.json())

#get_method_request(base_url)
#post_method_request(url=base_url)

#put_method_request(base_url)
#delete_method_request(base_url)