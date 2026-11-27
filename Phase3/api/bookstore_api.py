import requests 
from dotenv import load_dotenv
import os

load_dotenv()

API_URL = os.getenv("API_URL")



def get_books():

    # 1. Get all the books
    print("****************************GET ALL THE BOOKS****************************")

    

    try:
        getAllBooks = requests.get(API_URL)
        print("Status Code: ", getAllBooks.status_code)
        getAllBooks.raise_for_status()
        apiResponse = getAllBooks.json()
        print("Books we Received: ",apiResponse )
    except requests.exceptions.HTTPError as httperror:
        print("HTTP GET ERROR: ", httperror)



def add_book(book):

    # 2. Creating a new Book
    print("\n")
    print("****************************CREATING A NEW BOOK****************************")
    addNewBook = {
        "id": "6",
        "title": "The Douthe",
        "author": "Joseph",
        "rating": "9"


    }

    try:
        apiResponseNewBook = requests.post(API_URL,json=book)
        print("Status Code: ",apiResponseNewBook.status_code)
        apiResponseNewBook.raise_for_status()
        print(apiResponseNewBook.text)
    except requests.exceptions.HTTPError as httperror:
        print("HTTP GET ERROR: ", httperror)




def update_book(id,book):
    
    # 3. Update a Book
    print("\n")
    print("****************************UPADATE A BOOK****************************")

    replaceBook = {
        "id": "1",
        "title": "Data Science",
        "author": "Techie",
        "rating": "10"


    }

    try:
        apiResponseUpdate = requests.put(API_URL + "/" + str(id),json=book)
        print("Status Code: ",apiResponseUpdate.status_code)
        apiResponseUpdate.raise_for_status()
        print(apiResponseUpdate.text)
    except requests.exceptions.HTTPError as httperror:
        print("HTTP GET ERROR: ", httperror)







def delete_book(id):
    
    # 3. Delete a Book
    print("\n")
    print("****************************DELETE A BOOK****************************")

   

    try:
        apiResponseDelete = requests.delete(API_URL + "/"+ str(id))
        print("Status Code: ",apiResponseDelete.status_code)
        apiResponseDelete.raise_for_status()
        reponse = apiResponseDelete.json()
        print("Deleted Book:",reponse)
    except requests.exceptions.HTTPError as httperror:
        print("HTTP GET ERROR: ", httperror)




get_books()