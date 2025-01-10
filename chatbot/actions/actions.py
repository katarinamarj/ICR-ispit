# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


#This is a simple example for a custom action which utters "Hello World!"

from email import message
from typing import Dict, List
from rasa_sdk import Action
from rasa_sdk.executor import CollectingDispatcher
import re
from rasa_sdk.events import SlotSet


class ActionHelloWorld(Action):

    def name(self) -> str:
        return "action_hello_world"

    def run(self, dispatcher: CollectingDispatcher, tracker, domain) -> list:
        dispatcher.utter_message(text="Hello World!")
        return []


class ActionShowAllPets(Action):
    def name(self) -> str:
        return "action_show_all_pets"

    def run(self, dispatcher: CollectingDispatcher, tracker, domain) -> list:
        products = [
           {
        'id': 1, 
        'name': 'Rex', 
        'type': 'Dog', 
        'color': 'Orange',
        'age': '3', 
        'size': 'Large', 
        'origin': 'Germany', 
        'price': 100, 
        'review': '5 stars', 
        'image': 'https://thumbs.dreamstime.com/b/beautiful-happy-reddish-havanese-puppy-dog-sitting-frontal-looking-camera-isolated-white-background-46868560.jpg', 
        'details_link': 'http://localhost:4200/first'
    },
    {
        'id': 2, 
        'name': 'Fluffy', 
        'type': 'Hamster', 
        'color': 'Brown',
        'age': '1', 
        'size': 'Small', 
        'origin': 'USA', 
        'price': 10, 
        'review': '4 stars', 
        'image': 'https://img.pikbest.com/origin/09/29/39/52WpIkbEsTqAj.png!sw800', 
        'details_link': 'http://localhost:4200/second'
    },
    {
        'id': 3, 
        'name': 'Whiskers', 
        'type': 'Cat', 
        'color': 'Orange',
        'age': '2', 
        'size': 'Medium', 
        'origin': 'France', 
        'price': 80, 
        'review': '5 stars', 
        'image': 'https://img.freepik.com/free-photo/red-white-cat-i-white-studio_155003-13189.jpg?w=360', 
        'details_link': 'http://localhost:4200/third'
    },
    {
        'id': 4, 
        'name': 'Bubbles', 
        'type': 'Fish', 
        'color': 'Gold',
        'age': '1', 
        'size': 'Small', 
        'origin': 'Australia', 
        'price': 20, 
        'review': '4 stars', 
        'image': 'https://thumbs.dreamstime.com/b/summer-tropical-reef-fish-collection-isolated-white-background-41688673.jpg', 
        'details_link': 'http://localhost:4200/fourth'
    },
    {
        'id': 5, 
        'name': 'Sunny', 
        'type': 'Parrot', 
        'color': 'Yellow',
        'age': '4', 
        'size': 'Medium', 
        'origin': 'Brazil', 
        'price': 150, 
        'review': '5 stars', 
        'image': 'https://img.freepik.com/premium-vector/free-parrot-png-photo-white-background-generated-ai_1043838-2955.jpg', 
        'details_link': 'http://localhost:4200/fifth'
    },
    {
        'id': 6, 
        'name': 'Thumper', 
        'type': 'Rabbit', 
        'color': 'Grey',
        'age': '2', 
        'size': 'Small', 
        'origin': 'Canada', 
        'price': 30, 
        'review': '4 stars', 
        'image': 'https://media.istockphoto.com/id/959866606/photo/rabbit-4-months-old-sitting-against-white-background.jpg?s=612x612&w=0&k=20&c=8yRFVDIgoXj3gCh7ckkF4gCh8JjWN967r244PQ4vFUU=', 
        'details_link': 'http://localhost:4200/sixth'
    },
    {
        'id': 7, 
        'name': 'Max', 
        'type': 'Dog', 
        'color': 'Brown',
        'age': '5', 
        'size': 'Medium', 
        'origin': 'USA', 
        'price': 120, 
        'review': '5 stars', 
        'image': 'https://www.bil-jac.com/media/sy5jgj4k/dog-leo-min.png?&format=webp&width=400&mode=max&quality=80', 
        'details_link': 'http://localhost:4200/seventh'
    },
    {
        'id': 8, 
        'name': 'Nibbles', 
        'type': 'Hamster', 
        'color': 'Brown',
        'age': '1', 
        'size': 'Small', 
        'origin': 'USA', 
        'price': 15, 
        'review': '4 stars', 
        'image': 'https://st4.depositphotos.com/10614052/41661/i/450/depositphotos_416618198-stock-photo-funny-hamster-white-background.jpg', 
        'details_link': 'http://localhost:4200/eighth'
    },
    {
        'id': 9, 
        'name': 'Socks', 
        'type': 'Cat',
        'color': 'White', 
        'age': '3', 
        'size': 'Small', 
        'origin': 'UK', 
        'price': 60, 
        'review': '5 stars', 
        'image': 'https://thumbs.dreamstime.com/b/turkish-angora-cat-white-background-portrait-animal-themes-front-view-145390427.jpg', 
        'details_link': 'http://localhost:4200/ninth'
    },
    {
        'id': 10, 
        'name': 'Sky', 
        'type': 'Parrot', 
        'color': 'Blue',
        'age': '3', 
        'size': 'Medium', 
        'origin': 'Mexico', 
        'price': 140, 
        'review': '5 stars', 
        'image': 'https://thumbs.dreamstime.com/b/colorful-orange-parrot-macaw-isolated-white-background-35613998.jpg', 
        'details_link': 'http://localhost:4200/tenth'
    },
    {
        'id': 11, 
        'name': 'Splash', 
        'type': 'Fish', 
        'color': 'Gold', 
        'age': '2', 
        'size': 'Small', 
        'origin': 'China', 
        'price': 25, 
        'review': '4 stars', 
        'image': 'https://s7d2.scene7.com/is/image/PetSmart/5176556', 
        'details_link': 'http://localhost:4200/eleventh'
    },
    {
        'id': 12, 
        'name': 'Cuddles', 
        'type': 'Rabbit', 
        'color': 'Gray', 
        'age': '2', 
        'size': 'Small', 
        'origin': 'Germany', 
        'price': 35, 
        'review': '4 stars', 
        'image': 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRI-a4PNsfOOfJcgEiDfL3QJ5t6NzP8COK_ghmWyG431p6OQz4-V2zUmKfgnAectbgIYXc&usqp=CAU', 
        'details_link': 'http://localhost:4200/twelfth'
    },
    {
        'id': 13, 
        'name': 'Mittens', 
        'type': 'Cat', 
        'color': 'White', 
        'age': '4', 
        'size': 'Medium', 
        'origin': 'USA', 
        'price': 70, 
        'review': '5 stars', 
        'image': 'https://mascotasya.com/images/mascopedia/224-angora_turco_gato.jpg', 
        'details_link': 'http://localhost:4200/thirteenth'
    },
    {
        'id': 14, 
        'name': 'Bolt', 
        'type': 'Dog', 
        'color': 'Brown', 
        'age': '2', 
        'size': 'Large', 
        'origin': 'Canada', 
        'price': 110, 
        'review': '4 stars', 
        'image': 'https://publish.purewow.net/wp-content/uploads/sites/2/2021/01/low-maintenance-dog-breeds-broholmer.jpg?fit=680%2C860', 
        'details_link': 'http://localhost:4200/fourteenth'
    },
    {
        'id': 15, 
        'name': 'Slither', 
        'type': 'Snake', 
        'color': 'Brown', 
        'age': '1', 
        'size': 'Small', 
        'origin': 'Egypt', 
        'price': 90, 
        'review': '4 stars', 
        'image': 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRoeLjwuXK-08Bt7tJwDmVuHp1qvdJG_9nDtA&s', 
        'details_link': 'http://localhost:4200/fifteenth'
    },
    {
        'id': 16, 
        'name': 'Rio', 
        'type': 'Parrot', 
        'color': 'Red', 
        'age': '5', 
        'size': 'Large', 
        'origin': 'Brazil', 
        'price': 160, 
        'review': '5 stars', 
        'image': 'https://img.freepik.com/premium-photo/beautiful-parrot-white-background_41532-184.jpg', 
        'details_link': 'http://localhost:4200/sixteenth'
    },
    {
        'id': 17, 
        'name': 'Fin', 
        'type': 'Fish', 
        'color': 'Silver', 
        'age': '3', 
        'size': 'Medium', 
        'origin': 'Japan', 
        'price': 30, 
        'review': '4 stars', 
        'image': 'https://allergy-web-staging.s3.ap-southeast-2.amazonaws.com/wp-content/uploads/Fish_600px_NoBKG.png', 
        'details_link': 'http://localhost:4200/seventeenth'
    },
    {
        'id': 18, 
        'name': 'Flopsy', 
        'type': 'Rabbit', 
        'color': 'White', 
        'age': '1', 
        'size': 'Medium', 
        'origin': 'Australia', 
        'price': 40, 
        'review': '4 stars', 
        'image': 'https://media.istockphoto.com/id/959866606/photo/rabbit-4-months-old-sitting-against-white-background.jpg?s=612x612&w=0&k=20&c=8yRFVDIgoXj3gCh7ckkF4gCh8JjWN967r244PQ4vFUU=', 
        'details_link': 'http://localhost:4200/eighteenth'
    },
    {
        'id': 19, 
        'name': 'Zippy', 
        'type': 'Hamster', 
        'color': 'Grey', 
        'age': '2', 
        'size': 'Small', 
        'origin': 'Canada', 
        'price': 18, 
        'review': '4 stars', 
        'image': 'https://thumbs.dreamstime.com/b/hamster-20009706.jpg', 
        'details_link': 'http://localhost:4200/nineteenth'
    },
    {
        'id': 20, 
        'name': 'Sam', 
        'type': 'Dog', 
        'color': 'Brown', 
        'age': '6', 
        'size': 'Large', 
        'origin': 'Australia', 
        'price': 140, 
        'review': '5 stars', 
        'image': 'https://www.petlandindependence.com/wp-content/uploads/2022/06/Rhodesian-Ridgeback.png', 
        'details_link': 'http://localhost:4200/twentieth'
    },
    {
        'id': 21, 
        'name': 'Cloud', 
        'type': 'Parrot', 
        'color': 'Yellow', 
        'age': '2', 
        'size': 'Medium', 
        'origin': 'South Africa', 
        'price': 150, 
        'review': '5 stars', 
        'image': 'https://st2.depositphotos.com/2808973/5494/i/450/depositphotos_54941687-stock-photo-bule-gold-yellow-macaw-isolated.jpg', 
        'details_link': 'http://localhost:4200/twenty-first'
    },
    {
        'id': 22, 
        'name': 'Shadow', 
        'type': 'Snake', 
        'color': 'Black', 
        'age': '4', 
        'size': 'Medium', 
        'origin': 'Africa', 
        'price': 120, 
        'review': '4 stars', 
        'image': 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQa0BH38ggAsyHrj2I9gPtCifwMyTAr_wxM0hLEsENY2A1EIju6FmcrJwpNXiTJtfWXyFE&usqp=CAU', 
        'details_link': 'http://localhost:4200/twenty-second'
    },
    {
        'id': 23, 
        'name': 'Chester', 
        'type': 'Hamster', 
        'color': 'Brown', 
        'age': '3', 
        'size': 'Small', 
        'origin': 'UK', 
        'price': 12, 
        'review': '5 stars', 
        'image': 'https://static3.depositphotos.com/1003283/157/i/450/depositphotos_1574217-stock-photo-hamster.jpg', 
        'details_link': 'http://localhost:4200/twenty-third'
    },
    {
        'id': 24, 
        'name': 'Thistle', 
        'type': 'Rabbit', 
        'color': 'Orange', 
        'age': '1', 
        'size': 'Small', 
        'origin': 'New Zealand', 
        'price': 35, 
        'review': '4 stars', 
        'image': 'https://www.collinsdictionary.com/images/full/rabbit_274039655.jpg', 
        'details_link': 'http://localhost:4200/twenty-fourth'
    },
    {
        'id': 25, 
        'name': 'Fire', 
        'type': 'Parrot', 
        'color': 'Green', 
        'age': '2', 
        'size': 'Medium', 
        'origin': 'Costa Rica', 
        'price': 155, 
        'review': '5 stars', 
        'image': 'https://st.depositphotos.com/1578496/4368/i/450/depositphotos_43686969-stock-photo-beautiful-green-parrot.jpg', 
        'details_link': 'http://localhost:4200/twenty-fifth'
    },
    {
        'id': 26, 
        'name': 'Star', 
        'type': 'Fish', 
        'color': 'Blue', 
        'age': '1', 
        'size': 'Small', 
        'origin': 'USA', 
        'price': 20, 
        'review': '5 stars', 
        'image': 'https://img.freepik.com/free-psd/swimming-fish-isolated_23-2151359680.jpg', 
        'details_link': 'http://localhost:4200/twenty-sixth'
    },
    {
        'id': 27, 
        'name': 'Flare', 
        'type': 'Cat', 
        'color': 'Gray', 
        'age': '2', 
        'size': 'Medium', 
        'origin': 'India', 
        'price': 80, 
        'review': '5 stars', 
        'image': 'https://i.pinimg.com/550x/c1/c4/4a/c1c44a54126f793241da90e3d4c147e3.jpg', 
        'details_link': 'http://localhost:4200/twenty-seventh'
    },
    {
        'id': 28, 
        'name': 'Buddy', 
        'type': 'Dog', 
        'color': 'Brown', 
        'age': '3', 
        'size': 'Large', 
        'origin': 'France', 
        'price': 100, 
        'review': '5 stars', 
        'image': 'https://img.freepik.com/free-psd/cute-brown-white-dog-scene_23-2150179279.jpg?semt=ais_hybrid', 
        'details_link': 'http://localhost:4200/twenty-eighth'
    },
    {
        'id': 29, 
        'name': 'Viper', 
        'type': 'Snake', 
        'color': 'Brown', 
        'age': '3', 
        'size': 'Large', 
        'origin': 'India', 
        'price': 130, 
        'review': '4 stars', 
        'image': 'https://img.freepik.com/premium-psd/brown-snake-white-background-isolated-white-transparent-png-generative-ai_130745-271.jpg', 
        'details_link': 'http://localhost:4200/twenty-ninth'
    },
    {
        'id': 30, 
        'name': 'Charlie', 
        'type': 'Parrot', 
        'color': 'Blue', 
        'age': '4', 
        'size': 'Large', 
        'origin': 'Australia', 
        'price': 160, 
        'review': '5 stars', 
        'image': 'https://i.pinimg.com/236x/06/38/c3/0638c356c1f44f73337824c31307090b.jpg', 
        'details_link': 'http://localhost:4200/thirtieth'
    }
        ]
        
        if products:
            message = ""
            for pet in products:
                dispatcher.utter_message(text=
                            f"<b>Pet Name:</b> {pet['name']}<br>"
                            f"<b>Type:</b> {pet['type']}<br>"
                            f"<b>Age:</b> {pet['age']} years<br>"
                            f"<b>Size:</b> {pet['size']}<br>"
                            f"<b>Origin:</b> {pet['origin']}<br>"
                            f"<b>Price:</b> ${pet['price']}<br>"
                            f"<b>Review:</b> {pet['review']}<br>"
                            f"Click <b><a href='{pet['details_link']}' target='_blank'>here</a></b> for details.<br><br>")
        else:
             dispatcher.utter_message(text=message)
        return []

class ActionShowCats(Action):
    def name(self) -> str:
        return "action_show_cats"

    def run(self, dispatcher: CollectingDispatcher, tracker, domain) -> list:
        products = [
           {
        "id": 3,
        "name": "Whiskers",
        "type": "Cat",
        "color": "Orange",
        "age": "2",
        "size": "Medium",
        "origin": "France",
        "price": 80,
        "review": "5 stars",
        "image": "https://img.freepik.com/free-photo/red-white-cat-i-white-studio_155003-13189.jpg?w=360",
        "details_link": "http://localhost:4200/third"
    },
    {
        "id": 9,
        "name": "Socks",
        "type": "Cat",
        "color": "White",
        "age": "3",
        "size": "Small",
        "origin": "UK",
        "price": 60,
        "review": "5 stars",
        "image": "https://thumbs.dreamstime.com/b/turkish-angora-cat-white-background-portrait-animal-themes-front-view-145390427.jpg",
        "details_link": "http://localhost:4200/ninth"
    },
    {
        "id": 13,
        "name": "Mittens",
        "type": "Cat",
        "color": "White",
        "age": "4",
        "size": "Medium",
        "origin": "USA",
        "price": 70,
        "review": "5 stars",
        "image": "https://mascotasya.com/images/mascopedia/224-angora_turco_gato.jpg",
        "details_link": "http://localhost:4200/thirteenth"
    },
    {
        "id": 27,
        "name": "Flare",
        "type": "Cat",
        "color": "Gray",
        "age": "2",
        "size": "Medium",
        "origin": "India",
        "price": 80,
        "review": "5 stars",
        "image": "https://i.pinimg.com/550x/c1/c4/4a/c1c44a54126f793241da90e3d4c147e3.jpg",
        "details_link": "http://localhost:4200/twenty-seventh"
    }
        ]
        
        cats = [pet for pet in products if pet['type'].lower() == 'cat']
        
        if cats:
            message = ""
            for cat in cats:
                dispatcher.utter_message(text=
                            f"<b>Pet Name:</b> {cat['name']}<br>"
                            f"<b>Type:</b> {cat['type']}<br>"
                            f"<b>Age:</b> {cat['age']} years<br>"
                            f"<b>Size:</b> {cat['size']}<br>"
                            f"<b>Origin:</b> {cat['origin']}<br>"
                            f"<b>Price:</b> ${cat['price']}<br>"
                            f"<b>Review:</b> {cat['review']}<br>"
                            f"Click <b><a href='{cat['details_link']}' target='_blank'>here</a></b> for details.<br><br>")
            dispatcher.utter_message(text=message)
        else:
            dispatcher.utter_message(text="Sorry, no cats available at the moment.")
        
        return []

from rasa_sdk import Action
from rasa_sdk.executor import CollectingDispatcher

class ActionShowDogs(Action):
    def name(self) -> str:
        return "action_show_dogs"

    def run(self, dispatcher: CollectingDispatcher, tracker, domain) -> list:
        products = [
            {
                "id": 1,
                "name": "Rex",
                "type": "Dog",
                "color": "Orange",
                "age": "3",
                "size": "Large",
                "origin": "Germany",
                "price": 100,
                "review": "5 stars",
                "image": "https://thumbs.dreamstime.com/b/beautiful-happy-reddish-havanese-puppy-dog-sitting-frontal-looking-camera-isolated-white-background-46868560.jpg",
                "details_link": "http://localhost:4200/first"
            },
            {
                "id": 7,
                "name": "Max",
                "type": "Dog",
                "color": "Brown",
                "age": "5",
                "size": "Medium",
                "origin": "USA",
                "price": 120,
                "review": "5 stars",
                "image": "https://www.bil-jac.com/media/sy5jgj4k/dog-leo-min.png?&format=webp&width=400&mode=max&quality=80",
                "details_link": "http://localhost:4200/seventh"
            },
            {
                "id": 14,
                "name": "Bolt",
                "type": "Dog",
                "color": "Brown",
                "age": "2",
                "size": "Large",
                "origin": "Canada",
                "price": 110,
                "review": "4 stars",
                "image": "https://publish.purewow.net/wp-content/uploads/sites/2/2021/01/low-maintenance-dog-breeds-broholmer.jpg?fit=680%2C860",
                "details_link": "http://localhost:4200/fourteenth"
            },
            {
                "id": 20,
                "name": "Sam",
                "type": "Dog",
                "color": "Brown",
                "age": "6",
                "size": "Large",
                "origin": "Australia",
                "price": 140,
                "review": "5 stars",
                "image": "https://www.petlandindependence.com/wp-content/uploads/2022/06/Rhodesian-Ridgeback.png",
                "details_link": "http://localhost:4200/twentieth"
            },
            {
                "id": 28,
                "name": "Buddy",
                "type": "Dog",
                "color": "Brown",
                "age": "3",
                "size": "Large",
                "origin": "France",
                "price": 100,
                "review": "5 stars",
                "image": "https://img.freepik.com/free-psd/cute-brown-white-dog-scene_23-2150179279.jpg?semt=ais_hybrid",
                "details_link": "http://localhost:4200/twenty-eighth"
            }
        ]
        
        message = ""
        
        for dog in products:
            message += (f"<b>Pet Name:</b> {dog['name']}<br>"
                        f"<b>Type:</b> {dog['type']}<br>"
                        f"<b>Age:</b> {dog['age']} years<br>"
                        f"<b>Size:</b> {dog['size']}<br>"
                        f"<b>Origin:</b> {dog['origin']}<br>"
                        f"<b>Price:</b> ${dog['price']}<br>"
                        f"<b>Review:</b> {dog['review']}<br>"
                        f"Click <b><a href='{dog['details_link']}' target='_blank'>here</a></b> for details.<br><br>")
        
        if message:
            dispatcher.utter_message(text=message)
        else:
            dispatcher.utter_message(text="Sorry, no dogs available at the moment.")
        
        return []

class ActionShowRabbits(Action):
    def name(self) -> str:
        return "action_show_rabbits"

    def run(self, dispatcher: CollectingDispatcher, tracker, domain) -> list:
        products = [
            {
        "id": 6,
        "name": "Thumper",
        "type": "Rabbit",
        "color": "Grey",
        "age": "2",
        "size": "Small",
        "origin": "Canada",
        "price": 30,
        "review": "4 stars",
        "image": "https://media.istockphoto.com/id/959866606/photo/rabbit-4-months-old-sitting-against-white-background.jpg?s=612x612&w=0&k=20&c=8yRFVDIgoXj3gCh7ckkF4gCh8JjWN967r244PQ4vFUU=",
        "details_link": "http://localhost:4200/sixth"
    },
    {
        "id": 12,
        "name": "Cuddles",
        "type": "Rabbit",
        "color": "Gray",
        "age": "2",
        "size": "Small",
        "origin": "Germany",
        "price": 35,
        "review": "4 stars",
        "image": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRI-a4PNsfOOfJcgEiDfL3QJ5t6NzP8COK_ghmWyG431p6OQz4-V2zUmKfgnAectbgIYXc&usqp=CAU",
        "details_link": "http://localhost:4200/twelfth"
    },
    {
        "id": 18,
        "name": "Flopsy",
        "type": "Rabbit",
        "color": "White",
        "age": "1",
        "size": "Medium",
        "origin": "Australia",
        "price": 40,
        "review": "4 stars",
        "image": "https://media.istockphoto.com/id/959866606/photo/rabbit-4-months-old-sitting-against-white-background.jpg?s=612x612&w=0&k=20&c=8yRFVDIgoXj3gCh7ckkF4gCh8JjWN967r244PQ4vFUU=",
        "details_link": "http://localhost:4200/eighteenth"
    },
    {
        "id": 24,
        "name": "Thistle",
        "type": "Rabbit",
        "color": "Orange",
        "age": "1",
        "size": "Small",
        "origin": "New Zealand",
        "price": 35,
        "review": "4 stars",
        "image": "https://www.collinsdictionary.com/images/full/rabbit_274039655.jpg",
        "details_link": "http://localhost:4200/twenty-fourth"
    }
        ]
        
        rabbits = [pet for pet in products if pet['type'].lower() == 'rabbit']
        
        if rabbits:
            for rabbit in rabbits:
                dispatcher.utter_message(text=
                            f"<b>Pet Name:</b> {rabbit['name']}<br>"
                            f"<b>Type:</b> {rabbit['type']}<br>"
                            f"<b>Age:</b> {rabbit['age']} years<br>"
                            f"<b>Size:</b> {rabbit['size']}<br>"
                            f"<b>Origin:</b> {rabbit['origin']}<br>"
                            f"<b>Price:</b> ${rabbit['price']}<br>"
                            f"<b>Review:</b> {rabbit['review']}<br>"
                            f"Click <b><a href='{rabbit['details_link']}' target='_blank'>here</a></b> for details.<br><br>")

        else:
            dispatcher.utter_message(text="Sorry, no rabbits available at the moment.")
        
        return []


class ActionShowFish(Action):
    def name(self) -> str:
        return "action_show_fishes"

    def run(self, dispatcher: CollectingDispatcher, tracker, domain) -> list:
        products = [
            {
        "id": 4,
        "name": "Bubbles",
        "type": "Fish",
        "color": "Gold",
        "age": "1",
        "size": "Small",
        "origin": "Australia",
        "price": 20,
        "review": "4 stars",
        "image": "https://thumbs.dreamstime.com/b/summer-tropical-reef-fish-collection-isolated-white-background-41688673.jpg",
        "details_link": "http://localhost:4200/fourth"
    },
    {
        "id": 11,
        "name": "Splash",
        "type": "Fish",
        "color": "Gold",
        "age": "2",
        "size": "Small",
        "origin": "China",
        "price": 25,
        "review": "4 stars",
        "image": "https://s7d2.scene7.com/is/image/PetSmart/5176556",
        "details_link": "http://localhost:4200/eleventh"
    },
    {
        "id": 17,
        "name": "Fin",
        "type": "Fish",
        "color": "Silver",
        "age": "3",
        "size": "Medium",
        "origin": "Japan",
        "price": 30,
        "review": "4 stars",
        "image": "https://allergy-web-staging.s3.ap-southeast-2.amazonaws.com/wp-content/uploads/Fish_600px_NoBKG.png",
        "details_link": "http://localhost:4200/seventeenth"
    },
    {
        "id": 26,
        "name": "Star",
        "type": "Fish",
        "color": "Blue",
        "age": "1",
        "size": "Small",
        "origin": "USA",
        "price": 20,
        "review": "5 stars",
        "image": "https://img.freepik.com/free-psd/swimming-fish-isolated_23-2151359680.jpg",
        "details_link": "http://localhost:4200/twenty-sixth"
    }
        ]
        
        fish = [pet for pet in products if pet['type'].lower() == 'fish']
        
        if fish:
            for f in fish:
                dispatcher.utter_message(text=(
                            f"<b>Pet Name:</b> {f['name']}<br>"
                            f"<b>Type:</b> {f['type']}<br>"
                            f"<b>Age:</b> {f['age']} years<br>"
                            f"<b>Size:</b> {f['size']}<br>"
                            f"<b>Origin:</b> {f['origin']}<br>"
                            f"<b>Price:</b> ${f['price']}<br>"
                            f"<b>Review:</b> {f['review']}<br>"
                            f"Click <b><a href='{f['details_link']}' target='_blank'>here</a></b> for details.<br><br>"
                ))

        else:
            dispatcher.utter_message(text="Sorry, no fish available at the moment.")
        
        return []


class ActionShowParrots(Action):
    def name(self) -> str:
        return "action_show_parrots"

    def run(self, dispatcher: CollectingDispatcher, tracker, domain) -> list:
        products = [
           {
        "id": 5,
        "name": "Sunny",
        "type": "Parrot",
        "color": "Yellow",
        "age": "4",
        "size": "Medium",
        "origin": "Brazil",
        "price": 150,
        "review": "5 stars",
        "image": "https://img.freepik.com/premium-vector/free-parrot-png-photo-white-background-generated-ai_1043838-2955.jpg",
        "details_link": "http://localhost:4200/fifth"
    },
    {
        "id": 10,
        "name": "Sky",
        "type": "Parrot",
        "color": "Blue",
        "age": "3",
        "size": "Medium",
        "origin": "Mexico",
        "price": 140,
        "review": "5 stars",
        "image": "https://thumbs.dreamstime.com/b/colorful-orange-parrot-macaw-isolated-white-background-35613998.jpg",
        "details_link": "http://localhost:4200/tenth"
    },
    {
        "id": 16,
        "name": "Rio",
        "type": "Parrot",
        "color": "Red",
        "age": "5",
        "size": "Large",
        "origin": "Brazil",
        "price": 160,
        "review": "5 stars",
        "image": "https://img.freepik.com/premium-photo/beautiful-parrot-white-background_41532-184.jpg",
        "details_link": "http://localhost:4200/sixteenth"
    },
    {
        "id": 21,
        "name": "Cloud",
        "type": "Parrot",
        "color": "Yellow",
        "age": "2",
        "size": "Medium",
        "origin": "South Africa",
        "price": 150,
        "review": "5 stars",
        "image": "https://st2.depositphotos.com/2808973/5494/i/450/depositphotos_54941687-stock-photo-bule-gold-yellow-macaw-isolated.jpg",
        "details_link": "http://localhost:4200/twenty-first"
    },
    {
        "id": 25,
        "name": "Fire",
        "type": "Parrot",
        "color": "Green",
        "age": "2",
        "size": "Medium",
        "origin": "Costa Rica",
        "price": 155,
        "review": "5 stars",
        "image": "https://st.depositphotos.com/1578496/4368/i/450/depositphotos_43686969-stock-photo-beautiful-green-parrot.jpg",
        "details_link": "http://localhost:4200/twenty-fifth"
    },
    {
        "id": 30,
        "name": "Charlie",
        "type": "Parrot",
        "color": "Blue",
        "age": "4",
        "size": "Large",
        "origin": "Australia",
        "price": 160,
        "review": "5 stars",
        "image": "https://i.pinimg.com/236x/06/38/c3/0638c356c1f44f73337824c31307090b.jpg",
        "details_link": "http://localhost:4200/thirtieth"
    }
        ]
        
        parrots = [pet for pet in products if pet['type'].lower() == 'parrot']
        
        if parrots:
            for bird in parrots:
                dispatcher.utter_message(text=
                            f"<b>Pet Name:</b> {bird['name']}<br>"
                            f"<b>Type:</b> {bird['type']}<br>"
                            f"<b>Age:</b> {bird['age']} years<br>"
                            f"<b>Size:</b> {bird['size']}<br>"
                            f"<b>Origin:</b> {bird['origin']}<br>"
                            f"<b>Price:</b> ${bird['price']}<br>"
                            f"<b>Review:</b> {bird['review']}<br>"
                            f"Click <b><a href='{bird['details_link']}' target='_blank'>here</a></b> for details.<br><br>")
        else:
            dispatcher.utter_message(text="Sorry, no parrots available at the moment.")
        
        return []


class ActionShowHamsters(Action):
    def name(self) -> str:
        return "action_show_hamsters"

    def run(self, dispatcher: CollectingDispatcher, tracker, domain) -> list:
        products = [
            {
        "id": 2,
        "name": "Fluffy",
        "type": "Hamster",
        "color": "Brown",
        "age": "1",
        "size": "Small",
        "origin": "USA",
        "price": 10,
        "review": "4 stars",
        "image": "https://img.pikbest.com/origin/09/29/39/52WpIkbEsTqAj.png!sw800",
        "details_link": "http://localhost:4200/second"
    },
    {
        "id": 8,
        "name": "Nibbles",
        "type": "Hamster",
        "color": "Brown",
        "age": "1",
        "size": "Small",
        "origin": "USA",
        "price": 15,
        "review": "4 stars",
        "image": "https://st4.depositphotos.com/10614052/41661/i/450/depositphotos_416618198-stock-photo-funny-hamster-white-background.jpg",
        "details_link": "http://localhost:4200/eighth"
    },
    {
        "id": 19,
        "name": "Zippy",
        "type": "Hamster",
        "color": "Grey",
        "age": "2",
        "size": "Small",
        "origin": "Canada",
        "price": 18,
        "review": "4 stars",
        "image": "https://thumbs.dreamstime.com/b/hamster-20009706.jpg",
        "details_link": "http://localhost:4200/nineteenth"
    },
    {
        "id": 23,
        "name": "Chester",
        "type": "Hamster",
        "color": "Brown",
        "age": "3",
        "size": "Small",
        "origin": "UK",
        "price": 12,
        "review": "5 stars",
        "image": "https://static3.depositphotos.com/1003283/157/i/450/depositphotos_1574217-stock-photo-hamster.jpg",
        "details_link": "http://localhost:4200/twenty-third"
    }
        ]
        
        hamsters = [pet for pet in products if pet['type'].lower() == 'hamster']
        
        if hamsters:
            message = " "
            for hamster in hamsters:
                dispatcher.utter_message(text=
                            f"<b>Pet Name:</b> {hamster['name']}<br>"
                            f"<b>Type:</b> {hamster['type']}<br>"
                            f"<b>Age:</b> {hamster['age']} years<br>"
                            f"<b>Size:</b> {hamster['size']}<br>"
                            f"<b>Origin:</b> {hamster['origin']}<br>"
                            f"<b>Price:</b> ${hamster['price']}<br>"
                            f"<b>Review:</b> {hamster['review']}<br>"
                            f"Click <b><a href='{hamster['details_link']}' target='_blank'>here</a></b> for details.<br><br>")

            dispatcher.utter_message(text=message)
        else:
            dispatcher.utter_message(text="Sorry, no hamsters available at the moment.")
        
        return []


class ActionShowSnakes(Action):
    def name(self) -> str:
        return "action_show_snakes"

    def run(self, dispatcher: CollectingDispatcher, tracker, domain) -> list:
        products = [
            {
                "id": 15,
                "name": "Slither",
                "type": "Snake",
                "color": "Brown",
                "age": "1",
                "size": "Small",
                "origin": "Egypt",
                "price": 90,
                "review": "4 stars",
                "image": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRoeLjwuXK-08Bt7tJwDmVuHp1qvdJG_9nDtA&s",
                "details_link": "http://localhost:4200/fifteenth"
            },
            {
                "id": 22,
                "name": "Shadow",
                "type": "Snake",
                "color": "Black",
                "age": "4",
                "size": "Medium",
                "origin": "Africa",
                "price": 120,
                "review": "4 stars",
                "image": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQa0BH38ggAsyHrj2I9gPtCifwMyTAr_wxM0hLEsENY2A1EIju6FmcrJwpNXiTJtfWXyFE&usqp=CAU",
                "details_link": "http://localhost:4200/twenty-second"
            },
            {
                "id": 29,
                "name": "Viper",
                "type": "Snake",
                "color": "Brown",
                "age": "3",
                "size": "Large",
                "origin": "India",
                "price": 130,
                "review": "4 stars",
                "image": "https://img.freepik.com/premium-psd/brown-snake-white-background-isolated-white-transparent-png-generative-ai_130745-271.jpg",
                "details_link": "http://localhost:4200/twenty-ninth"
            }
        ]
        
        snakes = [pet for pet in products if pet['type'].lower() == 'snake']
        
        if snakes:
            for snake in snakes:
                dispatcher.utter_message(text=(
                            f"<b>Pet Name:</b> {snake['name']}<br>"
                            f"<b>Type:</b> {snake['type']}<br>"
                            f"<b>Age:</b> {snake['age']} years<br>"
                            f"<b>Size:</b> {snake['size']}<br>"
                            f"<b>Origin:</b> {snake['origin']}<br>"
                            f"<b>Price:</b> ${snake['price']}<br>"
                            f"<b>Review:</b> {snake['review']}<br>"
                            f"Click <b><a href='{snake['details_link']}' target='_blank'>here</a></b> for details.<br><br>"
                ))

        else:
            dispatcher.utter_message(text="Sorry, no snakes available at the moment.")
        
        return []


import re
from rasa_sdk import Action
from rasa_sdk.events import SlotSet
from rasa_sdk.executor import CollectingDispatcher

class ActionShowDogsByAge(Action):

    def name(self) -> str:
        return "action_show_dogs_by_age"

    def run(self, dispatcher: CollectingDispatcher, tracker, domain) -> list:
        dogs = [
            { 
                'id': 1, 
                'name': 'Rex', 
                'type': 'Dog', 
                'color': 'Orange', 
                'age': 3, 
                'size': 'Large', 
                'origin': 'Germany', 
                'price': 100, 
                'review': '5 stars', 
                'image': 'https://thumbs.dreamstime.com/b/beautiful-happy-reddish-havanese-puppy-dog-sitting-frontal-looking-camera-isolated-white-background-46868560.jpg', 
                'details_link': 'http://localhost:4200/first'
            },
            { 
                'id': 7, 
                'name': 'Max', 
                'type': 'Dog', 
                'color': 'Brown', 
                'age': 5, 
                'size': 'Medium', 
                'origin': 'USA', 
                'price': 120, 
                'review': '5 stars', 
                'image': 'https://www.bil-jac.com/media/sy5jgj4k/dog-leo-min.png?&format=webp&width=400&mode=max&quality=80', 
                'details_link': 'http://localhost:4200/seventh' 
            },
            { 
                'id': 14, 
                'name': 'Bolt', 
                'type': 'Dog', 
                'color': 'Brown', 
                'age': 2, 
                'size': 'Large', 
                'origin': 'Canada', 
                'price': 110, 
                'review': '4 stars', 
                'image': 'https://publish.purewow.net/wp-content/uploads/sites/2/2021/01/low-maintenance-dog-breeds-broholmer.jpg?fit=680%2C860', 
                'details_link': 'http://localhost:4200/fourteenth'
            },
            { 
                'id': 20, 
                'name': 'Sam', 
                'type': 'Dog', 
                'color': 'Brown', 
                'age': 6, 
                'size': 'Large', 
                'origin': 'Australia', 
                'price': 140, 
                'review': '5 stars', 
                'image': 'https://www.petlandindependence.com/wp-content/uploads/2022/06/Rhodesian-Ridgeback.png', 
                'details_link': 'http://localhost:4200/twentieth' 
            },
            { 
                'id': 28, 
                'name': 'Buddy', 
                'type': 'Dog', 
                'color': 'Brown', 
                'age': 3, 
                'size': 'Large', 
                'origin': 'France', 
                'price': 100, 
                'review': '5 stars', 
                'image': 'https://img.freepik.com/free-psd/cute-brown-white-dog-scene_23-2150179279.jpg?semt=ais_hybrid', 
                'details_link': 'http://localhost:4200/twenty-eighth'
            }
        ]

        user_input = tracker.latest_message.get("text", "")
        years_match = re.search(r"\d{1,2}", user_input)  

        if years_match:
            age_requested = int(years_match.group(0))  

            filtered_dogs = [dog for dog in dogs if dog['age'] == age_requested]

            if not filtered_dogs:
                dispatcher.utter_message(text=f"Sorry, no dogs found that are {age_requested} years old.")
                return []

            for dog in filtered_dogs:
                dispatcher.utter_message(
                    text=   f"<b>Pet Name:</b> {dog['name']}<br>"
                            f"<b>Type:</b> {dog['type']}<br>"
                            f"<b>Age:</b> {dog['age']} years<br>"
                            f"<b>Size:</b> {dog['size']}<br>"
                            f"<b>Origin:</b> {dog['origin']}<br>"
                            f"<b>Price:</b> ${dog['price']}<br>"
                            f"<b>Review:</b> {dog['review']}<br>"
                            f"Click <b><a href='{dog['details_link']}' target='_blank'>here</a></b> for details.<br><br>")

            return []

        else:
            dispatcher.utter_message(text="Please specify the age of the dog you are looking for.")
            return []
        

class ActionShowCatsByAge(Action):

    def name(self) -> str:
        return "action_show_cats_by_age"

    def run(self, dispatcher: CollectingDispatcher, tracker, domain) -> list:
        products = [
            { 
                'id': 3, 
                'name': 'Whiskers', 
                'type': 'Cat', 
                'color': 'Orange', 
                'age': '2', 
                'size': 'Medium', 
                'origin': 'France', 
                'price': 80, 
                'review': '5 stars', 
                'image': 'https://img.freepik.com/free-photo/red-white-cat-i-white-studio_155003-13189.jpg?w=360', 
                'details_link': 'http://localhost:4200/third'
            },
            { 
                'id': 9, 
                'name': 'Socks', 
                'type': 'Cat', 
                'color': 'White', 
                'age': '3', 
                'size': 'Small', 
                'origin': 'UK', 
                'price': 60, 
                'review': '5 stars', 
                'image': 'https://thumbs.dreamstime.com/b/turkish-angora-cat-white-background-portrait-animal-themes-front-view-145390427.jpg', 
                'details_link': 'http://localhost:4200/ninth'
            },
            { 
                'id': 13, 
                'name': 'Mittens', 
                'type': 'Cat', 
                'color': 'White', 
                'age': '4', 
                'size': 'Medium', 
                'origin': 'USA', 
                'price': 70, 
                'review': '5 stars', 
                'image': 'https://mascotasya.com/images/mascopedia/224-angora_turco_gato.jpg', 
                'details_link': 'http://localhost:4200/thirteenth'
            },
            { 
                'id': 27, 
                'name': 'Flare', 
                'type': 'Cat', 
                'color': 'Gray', 
                'age': '2', 
                'size': 'Medium', 
                'origin': 'India', 
                'price': 80, 
                'review': '5 stars', 
                'image': 'https://i.pinimg.com/550x/c1/c4/4a/c1c44a54126f793241da90e3d4c147e3.jpg', 
                'details_link': 'http://localhost:4200/twenty-seventh'
            }
        ]

        user_input = tracker.latest_message.get("text", "")
        years_match = re.search(r"\d{1,2}", user_input)  

        if years_match:
            age_requested = int(years_match.group(0))  

            filtered_cats = [cat for cat in products if cat['type'] == 'Cat' and int(cat['age']) == age_requested]

            if not filtered_cats:
                dispatcher.utter_message(text=f"Sorry, no cats found that are {age_requested} years old.")
                return []

            for cat in filtered_cats:
                dispatcher.utter_message(
                    text=
                            f"<b>Pet Name:</b> {cat['name']}<br>"
                            f"<b>Type:</b> {cat['type']}<br>"
                            f"<b>Age:</b> {cat['age']} years<br>"
                            f"<b>Size:</b> {cat['size']}<br>"
                            f"<b>Origin:</b> {cat['origin']}<br>"
                            f"<b>Price:</b> ${cat['price']}<br>"
                            f"<b>Review:</b> {cat['review']}<br>"
                            f"Click <b><a href='{cat['details_link']}' target='_blank'>here</a></b> for details.<br><br>")

            return []
        else:
            dispatcher.utter_message(text="Please specify the age of the cat you are looking for.")
            return []


import re

import re
from typing import List

class ActionShowPetsBySize(Action):
    def name(self) -> str:
        return "action_show_pets_by_size"

    def run(self, dispatcher: CollectingDispatcher, tracker, domain) -> List:
        products = [
            { 
                'id': 1, 
                'name': 'Rex', 
                'type': 'Dog', 
                'color': 'Orange', 
                'age': '3', 
                'size': 'Large', 
                'origin': 'Germany', 
                'price': 100, 
                'review': '5 stars', 
                'image': 'https://thumbs.dreamstime.com/b/beautiful-happy-reddish-havanese-puppy-dog-sitting-frontal-looking-camera-isolated-white-background-46868560.jpg', 
                'details_link': 'http://localhost:4200/first'
            },
            { 
                'id': 7, 
                'name': 'Max', 
                'type': 'Dog', 
                'color': 'Brown', 
                'age': '5', 
                'size': 'Large', 
                'origin': 'USA', 
                'price': 120, 
                'review': '5 stars', 
                'image': 'https://www.bil-jac.com/media/sy5jgj4k/dog-leo-min.png?&format=webp&width=400&mode=max&quality=80', 
                'details_link': 'http://localhost:4200/seventh' 
            },
            { 
                'id': 14, 
                'name': 'Bolt', 
                'type': 'Dog', 
                'color': 'Brown', 
                'age': '2', 
                'size': 'Large', 
                'origin': 'Canada', 
                'price': 110, 
                'review': '4 stars', 
                'image': 'https://publish.purewow.net/wp-content/uploads/sites/2/2021/01/low-maintenance-dog-breeds-broholmer.jpg?fit=680%2C860', 
                'details_link': 'http://localhost:4200/fourteenth'
            },
            { 
                'id': 20, 
                'name': 'Sam', 
                'type': 'Dog', 
                'color': 'Brown', 
                'age': '6', 
                'size': 'Large', 
                'origin': 'Australia', 
                'price': 140, 
                'review': '5 stars', 
                'image': 'https://www.petlandindependence.com/wp-content/uploads/2022/06/Rhodesian-Ridgeback.png', 
                'details_link': 'http://localhost:4200/twentieth' 
            },
            { 
                'id': 28, 
                'name': 'Sam', 
                'type': 'Dog', 
                'color': 'Brown', 
                'age': '6', 
                'size': 'Large', 
                'origin': 'Australia', 
                'price': 140, 
                'review': '5 stars', 
                'image': 'https://www.petlandindependence.com/wp-content/uploads/2022/06/Rhodesian-Ridgeback.png', 
                'details_link': 'http://localhost:4200/twenty-eighth' 
            }
        ]

        user_input = tracker.latest_message.get("text", "")
        size_match = re.search(r"(large|small)", user_input, re.IGNORECASE)  

        if size_match:
            size_requested = size_match.group(0).lower()  

            filtered_pets = [pet for pet in products if pet['size'].lower() == size_requested]

            if not filtered_pets:
                dispatcher.utter_message(text=f"Sorry, no pets found that are {size_requested} size. We currently only have large pets available.")
                return []

            for pet in filtered_pets:
                dispatcher.utter_message(
                    text=f"<b>Pet Name:</b> {pet['name']}<br>"
                            f"<b>Type:</b> {pet['type']}<br>"
                            f"<b>Age:</b> {pet['age']} years<br>"
                            f"<b>Size:</b> {pet['size']}<br>"
                            f"<b>Origin:</b> {pet['origin']}<br>"
                            f"<b>Price:</b> ${pet['price']}<br>"
                            f"<b>Review:</b> {pet['review']}<br>"
                            f"Click <b><a href='{pet['details_link']}' target='_blank'>here</a></b> for details.<br><br>")

            return []
        else:
            dispatcher.utter_message(text="Please specify the size (large or small) of the pet you are looking for.")
            return []


class ActionShowCatsByColor(Action):

    def name(self) -> str:
        return "action_show_cats_by_color"

    def run(self, dispatcher: CollectingDispatcher, tracker, domain) -> list:
        products = [
            { 
                'id': 3, 
                'name': 'Whiskers', 
                'type': 'Cat', 
                'color': 'Orange', 
                'age': '2', 
                'size': 'Medium', 
                'origin': 'France', 
                'price': 80, 
                'review': '5 stars', 
                'image': 'https://img.freepik.com/free-photo/red-white-cat-i-white-studio_155003-13189.jpg?w=360', 
                'details_link': 'http://localhost:4200/third'
            },
            { 
                'id': 9, 
                'name': 'Socks', 
                'type': 'Cat', 
                'color': 'White', 
                'age': '3', 
                'size': 'Small', 
                'origin': 'UK', 
                'price': 60, 
                'review': '5 stars', 
                'image': 'https://thumbs.dreamstime.com/b/turkish-angora-cat-white-background-portrait-animal-themes-front-view-145390427.jpg', 
                'details_link': 'http://localhost:4200/ninth'
            },
            { 
                'id': 13, 
                'name': 'Mittens', 
                'type': 'Cat', 
                'color': 'White', 
                'age': '4', 
                'size': 'Medium', 
                'origin': 'USA', 
                'price': 70, 
                'review': '5 stars', 
                'image': 'https://mascotasya.com/images/mascopedia/224-angora_turco_gato.jpg', 
                'details_link': 'http://localhost:4200/thirteenth'
            },
            { 
                'id': 27, 
                'name': 'Flare', 
                'type': 'Cat', 
                'color': 'Gray', 
                'age': '2', 
                'size': 'Medium', 
                'origin': 'India', 
                'price': 80, 
                'review': '5 stars', 
                'image': 'https://i.pinimg.com/550x/c1/c4/4a/c1c44a54126f793241da90e3d4c147e3.jpg', 
                'details_link': 'http://localhost:4200/twenty-seventh'
            }
        ]

        user_input = tracker.latest_message.get("text", "")
        color_match = re.search(r"(orange|white|gray)", user_input, re.IGNORECASE)  

        if color_match:
            color_requested = color_match.group(0).lower() 

            filtered_cats = [cat for cat in products if cat['color'].lower() == color_requested]

            if not filtered_cats:
                dispatcher.utter_message(text=f"Sorry, no cats found that are {color_requested} color.")
                return []

            for cat in filtered_cats:
                dispatcher.utter_message(
                    text=f"<b>Pet Name:</b> {cat['name']}<br>"
                            f"<b>Type:</b> {cat['type']}<br>"
                            f"<b>Age:</b> {cat['age']} years<br>"
                            f"<b>Size:</b> {cat['size']}<br>"
                            f"<b>Origin:</b> {cat['origin']}<br>"
                            f"<b>Price:</b> ${cat['price']}<br>"
                            f"<b>Review:</b> {cat['review']}<br>"
                            f"Click <b><a href='{cat['details_link']}' target='_blank'>here</a></b> for details.<br><br>")

            return []
        else:
            dispatcher.utter_message(text="Please specify the color (orange, white, gray) of the cat you are looking for.")
            return []
               
        
import re

class ActionShowDogsByColor(Action):

    def name(self) -> str:
        return "action_show_dogs_by_color"

    def run(self, dispatcher: CollectingDispatcher, tracker, domain) -> list:
        dogs = [
            { 
                'id': 1, 
                'name': 'Rex', 
                'type': 'Dog', 
                'color': 'Orange', 
                'age': 3, 
                'size': 'Large', 
                'origin': 'Germany', 
                'price': 100, 
                'review': '5 stars', 
                'image': 'https://thumbs.dreamstime.com/b/beautiful-happy-reddish-havanese-puppy-dog-sitting-frontal-looking-camera-isolated-white-background-46868560.jpg', 
                'details_link': 'http://localhost:4200/first'
            },
            { 
                'id': 7, 
                'name': 'Max', 
                'type': 'Dog', 
                'color': 'Brown', 
                'age': 5, 
                'size': 'Medium', 
                'origin': 'USA', 
                'price': 120, 
                'review': '5 stars', 
                'image': 'https://www.bil-jac.com/media/sy5jgj4k/dog-leo-min.png?&format=webp&width=400&mode=max&quality=80', 
                'details_link': 'http://localhost:4200/seventh'
            },
            { 
                'id': 14, 
                'name': 'Bolt', 
                'type': 'Dog', 
                'color': 'Brown', 
                'age': 2, 
                'size': 'Large', 
                'origin': 'Canada', 
                'price': 110, 
                'review': '4 stars', 
                'image': 'https://publish.purewow.net/wp-content/uploads/sites/2/2021/01/low-maintenance-dog-breeds-broholmer.jpg?fit=680%2C860', 
                'details_link': 'http://localhost:4200/fourteenth'
            },
            { 
                'id': 20, 
                'name': 'Sam', 
                'type': 'Dog', 
                'color': 'Brown', 
                'age': 6, 
                'size': 'Large', 
                'origin': 'Australia', 
                'price': 140, 
                'review': '5 stars', 
                'image': 'https://www.petlandindependence.com/wp-content/uploads/2022/06/Rhodesian-Ridgeback.png', 
                'details_link': 'http://localhost:4200/twentieth'
            },
            { 
                'id': 28, 
                'name': 'Buddy', 
                'type': 'Dog', 
                'color': 'Brown', 
                'age': 3, 
                'size': 'Large', 
                'origin': 'France', 
                'price': 100, 
                'review': '5 stars', 
                'image': 'https://img.freepik.com/free-psd/cute-brown-white-dog-scene_23-2150179279.jpg?semt=ais_hybrid', 
                'details_link': 'http://localhost:4200/twenty-eighth'
            }
        ]

        user_input = tracker.latest_message.get("text", "")
        color_match = re.search(r"(orange|brown)", user_input, re.IGNORECASE)  

        if color_match:
            color_requested = color_match.group(0).lower()  

            filtered_dogs = [dog for dog in dogs if dog['color'].lower() == color_requested]

            if not filtered_dogs:
                dispatcher.utter_message(text=f"Sorry, no dogs found that are {color_requested} color.")
                return []

            for dog in filtered_dogs:
                dispatcher.utter_message(
                    text=f"<b>Pet Name:</b> {dog['name']}<br>"
                            f"<b>Type:</b> {dog['type']}<br>"
                            f"<b>Age:</b> {dog['age']} years<br>"
                            f"<b>Size:</b> {dog['size']}<br>"
                            f"<b>Origin:</b> {dog['origin']}<br>"
                            f"<b>Price:</b> ${dog['price']}<br>"
                            f"<b>Review:</b> {dog['review']}<br>"
                            f"Click <b><a href='{dog['details_link']}' target='_blank'>here</a></b> for details.<br><br>")
            return []
        else:
            dispatcher.utter_message(text="Please specify the color (orange, brown) of the dog you are looking for.")
            return []

class ActionShowFishByColor(Action):

    def name(self) -> str:
        return "action_show_fish_by_color"

    def run(self, dispatcher: CollectingDispatcher, tracker, domain) -> list:
        fish = [
            { 
                'id': 4, 
                'name': 'Bubbles', 
                'type': 'Fish', 
                'color': 'blue', 
                'age': '1', 
                'size': 'Small', 
                'origin': 'Australia', 
                'price': 20, 
                'review': '4 stars', 
                'image': 'https://thumbs.dreamstime.com/b/summer-tropical-reef-fish-collection-isolated-white-background-41688673.jpg', 
                'details_link': 'http://localhost:4200/fourth'
            },
            { 
                'id': 11, 
                'name': 'Splash', 
                'type': 'Fish', 
                'color': 'Gold', 
                'age': '2', 
                'size': 'Small', 
                'origin': 'China', 
                'price': 25, 
                'review': '4 stars', 
                'image': 'https://s7d2.scene7.com/is/image/PetSmart/5176556', 
                'details_link': 'http://localhost:4200/eleventh'
            },
            { 
                'id': 17, 
                'name': 'Fin', 
                'type': 'Fish', 
                'color': 'Silver', 
                'age': '3', 
                'size': 'Medium', 
                'origin': 'Japan', 
                'price': 30, 
                'review': '4 stars', 
                'image': 'https://allergy-web-staging.s3.ap-southeast-2.amazonaws.com/wp-content/uploads/Fish_600px_NoBKG.png', 
                'details_link': 'http://localhost:4200/seventeenth'
            },
            { 
                'id': 26, 
                'name': 'Star', 
                'type': 'Fish', 
                'color': 'Blue', 
                'age': '1', 
                'size': 'Small', 
                'origin': 'USA', 
                'price': 20, 
                'review': '5 stars', 
                'image': 'https://img.freepik.com/free-psd/swimming-fish-isolated_23-2151359680.jpg', 
                'details_link': 'http://localhost:4200/twenty-sixth'
            }
        ]

        user_input = tracker.latest_message.get("text", "")
        color_match = re.search(r"(gold|silver|blue)", user_input, re.IGNORECASE)  

        if color_match:
            color_requested = color_match.group(0).lower() 

            filtered_fish = [fish_item for fish_item in fish if fish_item['color'].lower() == color_requested]

            if not filtered_fish:
                dispatcher.utter_message(text=f"Sorry, no fish found that are {color_requested} color.")
                return []

            for fish_item in filtered_fish:
                dispatcher.utter_message(
                    text=f"<b>Pet Name:</b> {fish_item['name']}<br>"
                            f"<b>Type:</b> {fish_item['type']}<br>"
                            f"<b>Age:</b> {fish_item['age']} years<br>"
                            f"<b>Size:</b> {fish_item['size']}<br>"
                            f"<b>Origin:</b> {fish_item['origin']}<br>"
                            f"<b>Price:</b> ${fish_item['price']}<br>"
                            f"<b>Review:</b> {fish_item['review']}<br>"
                            f"Click <b><a href='{fish_item['details_link']}' target='_blank'>here</a></b> for details.<br><br>")
            return []
        else:
            dispatcher.utter_message(text="Please specify the color (gold, silver, blue) of the fish you are looking for.")
            return []


class ActionShowAnimalsByPrice(Action):

    def name(self) -> str:
        return "action_show_animals_by_price"

    def run(self, dispatcher: CollectingDispatcher, tracker, domain) -> List[Dict]:
        animals = {
            'fish': [
                { 
                    'id': 4, 
                    'name': 'Bubbles', 
                    'type': 'Fish', 
                    'color': 'Gold', 
                    'age': '1', 
                    'size': 'Small', 
                    'origin': 'Australia', 
                    'price': 20, 
                    'review': '4 stars', 
                    'image': 'https://thumbs.dreamstime.com/b/summer-tropical-reef-fish-collection-isolated-white-background-41688673.jpg', 
                    'details_link': 'http://localhost:4200/forth'
                },
                { 
                    'id': 11, 
                    'name': 'Splash', 
                    'type': 'Fish', 
                    'color': 'Gold', 
                    'age': '2', 
                    'size': 'Small', 
                    'origin': 'China', 
                    'price': 25, 
                    'review': '4 stars', 
                    'image': 'https://s7d2.scene7.com/is/image/PetSmart/5176556', 
                    'details_link': 'http://localhost:4200/eleventh'
                },
                { 
                    'id': 17, 
                    'name': 'Fin', 
                    'type': 'Fish', 
                    'color': 'Silver', 
                    'age': '3', 
                    'size': 'Medium', 
                    'origin': 'Japan', 
                    'price': 30, 
                    'review': '4 stars', 
                    'image': 'https://allergy-web-staging.s3.ap-southeast-2.amazonaws.com/wp-content/uploads/Fish_600px_NoBKG.png', 
                    'details_link': 'http://localhost:4200/seventeenth'
                },
                { 
                    'id': 26, 
                    'name': 'Star', 
                    'type': 'Fish', 
                    'color': 'Blue', 
                    'age': '1', 
                    'size': 'Small', 
                    'origin': 'USA', 
                    'price': 20, 
                    'review': '5 stars', 
                    'image': 'https://img.freepik.com/free-psd/swimming-fish-isolated_23-2151359680.jpg', 
                    'details_link': 'http://localhost:4200/twenty-sixth'
                }
            ],
            'dogs': [
                { 
        'id': 1, 
        'name': 'Rex', 
        'type': 'Dog', 
        'color': 'Orange', 
        'age': '3', 
        'size': 'Small', 
        'origin': 'Germany', 
        'price': 100, 
        'review': '5 stars', 
        'image': 'https://thumbs.dreamstime.com/b/beautiful-happy-reddish-havanese-puppy-dog-sitting-frontal-looking-camera-isolated-white-background-46868560.jpg', 
        'details_link': 'http://localhost:4200/first' 
    },
    { 
        'id': 7, 
        'name': 'Max', 
        'type': 'Dog', 
        'color': 'Brown', 
        'age': '5', 
        'size': 'Large', 
        'origin': 'USA', 
        'price': 120, 
        'review': '5 stars', 
        'image': 'https://www.bil-jac.com/media/sy5jgj4k/dog-leo-min.png?&format=webp&width=400&mode=max&quality=80', 
        'details_link': 'http://localhost:4200/seventh'
    },
    { 
        'id': 14, 
        'name': 'Bolt', 
        'type': 'Dog', 
        'color': 'Brown', 
        'age': '2', 
        'size': 'Large', 
        'origin': 'Canada', 
        'price': 110, 
        'review': '4 stars', 
        'image': 'https://publish.purewow.net/wp-content/uploads/sites/2/2021/01/low-maintenance-dog-breeds-broholmer.jpg?fit=680%2C860', 
        'details_link': 'http://localhost:4200/fourteenth' 
    },
    { 
        'id': 20, 
        'name': 'Sam', 
        'type': 'Dog', 
        'color': 'Brown', 
        'age': '6', 
        'size': 'Large', 
        'origin': 'Australia', 
        'price': 140, 
        'review': '5 stars', 
        'image': 'https://www.petlandindependence.com/wp-content/uploads/2022/06/Rhodesian-Ridgeback.png', 
        'details_link': 'http://localhost:4200/twentieth'
    },
    { 
        'id': 28, 
        'name': 'Buddy', 
        'type': 'Dog', 
        'color': 'Brown', 
        'age': '3', 
        'size': 'Large', 
        'origin': 'France', 
        'price': 100, 
        'review': '5 stars', 
        'image': 'https://img.freepik.com/free-psd/cute-brown-white-dog-scene_23-2150179279.jpg?semt=ais_hybrid', 
        'details_link': 'http://localhost:4200/twenty-eighth'
    }
            ],
            'cats': [
                { 
        'id': 3, 
        'name': 'Whiskers', 
        'type': 'Cat', 
        'color': 'Orange', 
        'age': '2', 
        'size': 'Medium', 
        'origin': 'France', 
        'price': 80, 
        'review': '5 stars', 
        'image': 'https://img.freepik.com/free-photo/red-white-cat-i-white-studio_155003-13189.jpg?w=360', 
        'details_link': 'http://localhost:4200/third'
    },
    { 
        'id': 9, 
        'name': 'Socks', 
        'type': 'Cat', 
        'color': 'White', 
        'age': '3', 
        'size': 'Small', 
        'origin': 'UK', 
        'price': 60, 
        'review': '5 stars', 
        'image': 'https://thumbs.dreamstime.com/b/turkish-angora-cat-white-background-portrait-animal-themes-front-view-145390427.jpg', 
        'details_link': 'http://localhost:4200/ninth'
    },
    { 
        'id': 13, 
        'name': 'Mittens', 
        'type': 'Cat', 
        'color': 'White', 
        'age': '4', 
        'size': 'Medium', 
        'origin': 'USA', 
        'price': 70, 
        'review': '5 stars', 
        'image': 'https://mascotasya.com/images/mascopedia/224-angora_turco_gato.jpg', 
        'details_link': 'http://localhost:4200/thirteenth'
    },
    { 
        'id': 27, 
        'name': 'Flare', 
        'type': 'Cat', 
        'color': 'Gray', 
        'age': '2', 
        'size': 'Medium', 
        'origin': 'India', 
        'price': 80, 
        'review': '5 stars', 
        'image': 'https://i.pinimg.com/550x/c1/c4/4a/c1c44a54126f793241da90e3d4c147e3.jpg', 
        'details_link': 'http://localhost:4200/twenty-seventh'
    }
            ],
            'hamsters': [
                {
        "id": 2,
        "name": "Fluffy",
        "type": "Hamster",
        "color": "Brown",
        "age": "1",
        "size": "Small",
        "origin": "USA",
        "price": 10,
        "review": "4 stars",
        "image": "https://img.pikbest.com/origin/09/29/39/52WpIkbEsTqAj.png!sw800",
        "details_link": "http://localhost:4200/second"
    },
    {
        "id": 8,
        "name": "Nibbles",
        "type": "Hamster",
        "color": "Brown",
        "age": "1",
        "size": "Small",
        "origin": "USA",
        "price": 15,
        "review": "4 stars",
        "image": "https://st4.depositphotos.com/10614052/41661/i/450/depositphotos_416618198-stock-photo-funny-hamster-white-background.jpg",
        "details_link": "http://localhost:4200/eighth"
    },
    {
        "id": 19,
        "name": "Zippy",
        "type": "Hamster",
        "color": "Grey",
        "age": "2",
        "size": "Small",
        "origin": "Canada",
        "price": 18,
        "review": "4 stars",
        "image": "https://thumbs.dreamstime.com/b/hamster-20009706.jpg",
        "details_link": "http://localhost:4200/nineteenth"
    },
    {
        "id": 23,
        "name": "Chester",
        "type": "Hamster",
        "color": "Brown",
        "age": "3",
        "size": "Small",
        "origin": "UK",
        "price": 12,
        "review": "5 stars",
        "image": "https://static3.depositphotos.com/1003283/157/i/450/depositphotos_1574217-stock-photo-hamster.jpg",
        "details_link": "http://localhost:4200/twenty-third"
    }
            ],
            'rabbits': [
                { 
                'id': 6, 
                'name': 'Thumper', 
                'type': 'Rabbit', 
                'color': 'Grey', 
                'age': '2', 
                'size': 'Small', 
                'origin': 'Canada', 
                'price': 30, 
                'review': '4 stars', 
                'image': 'https://media.istockphoto.com/id/959866606/photo/rabbit-4-months-old-sitting-against-white-background.jpg?s=612x612&w=0&k=20&c=8yRFVDIgoXj3gCh7ckkF4gCh8JjWN967r244PQ4vFUU=', 
                'details_link': 'http://localhost:4200/sixth'
            },
            { 
                'id': 12, 
                'name': 'Cuddles', 
                'type': 'Rabbit', 
                'color': 'Gray', 
                'age': '2', 
                'size': 'Small', 
                'origin': 'Germany', 
                'price': 35, 
                'review': '4 stars', 
                'image': 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRI-a4PNsfOOfJcgEiDfL3QJ5t6NzP8COK_ghmWyG431p6OQz4-V2zUmKfgnAectbgIYXc&usqp=CAU', 
                'details_link': 'http://localhost:4200/twelfth'
            },
            { 
                'id': 18, 
                'name': 'Flopsy', 
                'type': 'Rabbit', 
                'color': 'White', 
                'age': '1', 
                'size': 'Medium', 
                'origin': 'Australia', 
                'price': 40, 
                'review': '4 stars', 
                'image': 'https://media.istockphoto.com/id/959866606/photo/rabbit-4-months-old-sitting-against-white-background.jpg?s=612x612&w=0&k=20&c=8yRFVDIgoXj3gCh7ckkF4gCh8JjWN967r244PQ4vFUU=', 
                'details_link': 'http://localhost:4200/eighteenth'
            },
            {
    "id": 24,
    "name": "Thistle",
    "type": "Rabbit",
    "color": "Orange",
    "age": "1",
    "size": "Small",
    "origin": "New Zealand",
    "price": 35,
    "review": "4 stars",
    "image": "https://www.collinsdictionary.com/images/full/rabbit_274039655.jpg",
    "details_link": "http://localhost:4200/twenty-fourth"
}

            ],
            'parrots': [
                {
        "id": 5,
        "name": "Sunny",
        "type": "Parrot",
        "color": "Yellow",
        "age": "4",
        "size": "Medium",
        "origin": "Brazil",
        "price": 150,
        "review": "5 stars",
        "image": "https://img.freepik.com/premium-vector/free-parrot-png-photo-white-background-generated-ai_1043838-2955.jpg",
        "details_link": "http://localhost:4200/fifth"
    },
    {
        "id": 10,
        "name": "Sky",
        "type": "Parrot",
        "color": "Blue",
        "age": "3",
        "size": "Medium",
        "origin": "Mexico",
        "price": 140,
        "review": "5 stars",
        "image": "https://thumbs.dreamstime.com/b/colorful-orange-parrot-macaw-isolated-white-background-35613998.jpg",
        "details_link": "http://localhost:4200/tenth"
    },
    {
        "id": 16,
        "name": "Rio",
        "type": "Parrot",
        "color": "Red",
        "age": "5",
        "size": "Large",
        "origin": "Brazil",
        "price": 160,
        "review": "5 stars",
        "image": "https://img.freepik.com/premium-photo/beautiful-parrot-white-background_41532-184.jpg",
        "details_link": "http://localhost:4200/sixteenth"
    },
    {
        "id": 21,
        "name": "Cloud",
        "type": "Parrot",
        "color": "Yellow",
        "age": "2",
        "size": "Medium",
        "origin": "South Africa",
        "price": 150,
        "review": "5 stars",
        "image": "https://st2.depositphotos.com/2808973/5494/i/450/depositphotos_54941687-stock-photo-bule-gold-yellow-macaw-isolated.jpg",
        "details_link": "http://localhost:4200/twenty-first"
    },
    {
        "id": 25,
        "name": "Fire",
        "type": "Parrot",
        "color": "Green",
        "age": "2",
        "size": "Medium",
        "origin": "Costa Rica",
        "price": 155,
        "review": "5 stars",
        "image": "https://st.depositphotos.com/1578496/4368/i/450/depositphotos_43686969-stock-photo-beautiful-green-parrot.jpg",
        "details_link": "http://localhost:4200/twenty-fifth"
    },
    {
        "id": 30,
        "name": "Charlie",
        "type": "Parrot",
        "color": "Blue",
        "age": "4",
        "size": "Large",
        "origin": "Australia",
        "price": 160,
        "review": "5 stars",
        "image": "https://i.pinimg.com/236x/06/38/c3/0638c356c1f44f73337824c31307090b.jpg",
        "details_link": "http://localhost:4200/thirtieth"
    }
            ],
            'snakes': [
    {
        "id": 15,
        "name": "Slither",
        "type": "Snake",
        "color": "Brown",
        "age": "1",
        "size": "Small",
        "origin": "Egypt",
        "price": 90,
        "review": "4 stars",
        "image": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRoeLjwuXK-08Bt7tJwDmVuHp1qvdJG_9nDtA&s",
        "details_link": "http://localhost:4200/fifteenth"
    },
    {
        "id": 22,
        "name": "Shadow",
        "type": "Snake",
        "color": "Black",
        "age": "4",
        "size": "Medium",
        "origin": "Africa",
        "price": 120,
        "review": "4 stars",
        "image": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQa0BH38ggAsyHrj2I9gPtCifwMyTAr_wxM0hLEsENY2A1EIju6FmcrJwpNXiTJtfWXyFE&usqp=CAU",
        "details_link": "http://localhost:4200/twenty-second"
    },
    {
        "id": 29,
        "name": "Viper",
        "type": "Snake",
        "color": "Brown",
        "age": "3",
        "size": "Large",
        "origin": "India",
        "price": 130,
        "review": "4 stars",
        "image": "https://img.freepik.com/premium-psd/brown-snake-white-background-isolated-white-transparent-png-generative-ai_130745-271.jpg",
        "details_link": "http://localhost:4200/twenty-ninth"
    }
]

        }

        user_input = tracker.latest_message.get("text", "").lower()

        if "fish" in user_input:
            animal_type = "fish"
        elif "dog" in user_input:
            animal_type = "dogs"
        elif "cat" in user_input:
            animal_type = "cats"
        elif "hamster" in user_input:
            animal_type = "hamsters"
        elif "snake" in user_input:
            animal_type = "snakes"
        elif "rabbit" in user_input:
            animal_type = "rabbits"
        elif "parrot" in user_input:
            animal_type = "parrots"
        else:
            animal_type = None

        if "above 100" in user_input:
            filter_condition = "above_100"
        elif "less than 100" in user_input:
            filter_condition = "less_than_100"
        elif "price is 100" in user_input:
            filter_condition = "equal_100"
        else:
            dispatcher.utter_message(text="Please specify the price range (above 100, less than 100, or exactly 100).")
            return []

        if animal_type:
            animals_to_filter = animals.get(animal_type, [])
        else:
            animals_to_filter = [animal for animal_list in animals.values() for animal in animal_list]

        filtered_animals = [animal for animal in animals_to_filter if self._filter_price(animal['price'], filter_condition)]

        if not filtered_animals:
            dispatcher.utter_message(text=f"Sorry, no {animal_type if animal_type else 'animals'} found with the price condition {filter_condition.replace('_', ' ')}.")
            return []

        for animal in filtered_animals:
            dispatcher.utter_message(
                text=f"<b>Pet Name:</b> {animal['name']}<br>"
                            f"<b>Type:</b> {animal['type']}<br>"
                            f"<b>Age:</b> {animal['age']} years<br>"
                            f"<b>Size:</b> {animal['size']}<br>"
                            f"<b>Origin:</b> {animal['origin']}<br>"
                            f"<b>Price:</b> ${animal['price']}<br>"
                            f"<b>Review:</b> {animal['review']}<br>"
                            f"Click <b><a href='{animal['details_link']}' target='_blank'>here</a></b> for details.<br><br>")


        return []

    def _filter_price(self, price, condition):
        if condition == "above_100":
            return price > 100
        elif condition == "less_than_100":
            return price < 100
        elif condition == "equal_100":
            return price == 100
        return False
    
from rasa_sdk import Action
from rasa_sdk.executor import CollectingDispatcher

class ActionOrderPets(Action):
    def name(self) -> str:
        return "action_order_pets"

    def run(self, dispatcher: CollectingDispatcher, tracker, domain) -> list:
        dispatcher.utter_message(
            text="If you want to order, follow these steps: <br>"
                 "1. Go to the catalog. <br><a href='http://localhost:4200/catalog' target='_blank'>Click here</a><br>"
                 "2. Use the search bar to find your pet.<br>"
                 "3. Click 'Add to Cart' button.<br><a href='http://localhost:4200/catalog' target='_blank'>Click here</a><br>"
                 "4. Go to your cart.<br>"
                 "5. Complete your purchase."
        )

        return []

class ActionExplainPaymentForm(Action):
    def name(self) -> str:
        return "action_explain_payment_form"

    def run(self, dispatcher: CollectingDispatcher, tracker, domain) -> list:
        dispatcher.utter_message(
            text="To complete your payment, follow these steps: <br>"
                 "1. Enter the name and surname as it appears on the front of your card. <br>"
                 "2. Write the 16-digit number found on the front of your card. <br>"
                 "3. Enter the expiration date (MM/YY) located on the front of your card. <br>"
                 "4. Type the 3-digit security code (CVV) found on the back of your card. <br>"
                 "5. Make sure all the details are correct before submitting. <br>"
                 "Once you've entered all the required information, click 'Submit' to complete your payment."
        )

        return []


from rasa_sdk import Action
from rasa_sdk.events import SlotSet

class ActionShowCatsBestForKids(Action):
    def name(self):
        return "action_show_cats_best_for_kids"

    def run(self, dispatcher, tracker, domain):
        cats_best_for_kids = [
    {
        "id": 9,
        "name": "Socks",
        "type": "Cat",
        "color": "White",
        "age": "3",
        "size": "Small",
        "origin": "UK",
        "price": 60,
        "review": "5 stars",
        "image": "https://thumbs.dreamstime.com/b/turkish-angora-cat-white-background-portrait-animal-themes-front-view-145390427.jpg",
        "details_link": "http://localhost:4200/ninth",
        "temperament": "gentle"
    },
    {
        "id": 13,
        "name": "Mittens",
        "type": "Cat",
        "color": "White",
        "age": "4",
        "size": "Medium",
        "origin": "USA",
        "price": 70,
        "review": "5 stars",
        "image": "https://mascotasya.com/images/mascopedia/224-angora_turco_gato.jpg",
        "details_link": "http://localhost:4200/thirteenth",
        "temperament": "friendly"
    }
        ]
    
        dispatcher.utter_message("For our opinion, these cats is the best for your children because thay are friendly and thay have a lot of patience for our little ones")
        
        for cat in cats_best_for_kids:
             dispatcher.utter_message(
                text=f"<b>Pet Name:</b> {cat['name']}<br>"
                            f"<b>Type:</b> {cat['type']}<br>"
                            f"<b>Age:</b> {cat['age']} years<br>"
                            f"<b>Size:</b> {cat['size']}<br>"
                            f"<b>Origin:</b> {cat['origin']}<br>"
                            f"<b>Price:</b> ${cat['price']}<br>"
                            f"<b>Review:</b> {cat['review']}<br>"
                            f"Click <b><a href='{cat['details_link']}' target='_blank'>here</a></b> for details.<br><br>"
                            
                            )
            

class ActionShowDogsHealthStatus(Action):
    def name(self) -> str:
        return "action_show_dogs_health_status"

    def run(self, dispatcher: CollectingDispatcher, tracker, domain) -> list:
        dispatcher.utter_message(
            text="Something you should know about our dogs: <br>"
                 "1. They are all vaccinated on time.<br>"
                 "2. Some of them are sterilized.<br>"
                 "3. All of them are potty trained.<br>"
                 "4. All of them are good and polite.<br>"
        )
        return []


class ActionShowSterelizedDogs(Action):
    def name(self) -> str:
        return "action_show_sterelized_dogs"

    def run(self, dispatcher: CollectingDispatcher, tracker, domain) -> list:
        sterelized_dogs = [
            {
                "name": "Buddy",
                "age": 2,
                "breed": "Golden Retriever",
                "image": "https://example.com/buddy.jpg",
                "details_link": "http://localhost:4200/buddy"
            },
            {
                "name": "Luna",
                "age": 3,
                "breed": "Labrador",
                "image": "https://example.com/luna.jpg",
                "details_link": "http://localhost:4200/luna"
            }
        ]

        dispatcher.utter_message(text="Here are some of our sterilized dogs:")
        for dog in sterelized_dogs:
            dispatcher.utter_message(
                text=f"<b>Dog Name:</b> {dog['name']}<br>"
                     f"<b>Age:</b> {dog['age']} years<br>"
                     f"<b>Breed:</b> {dog['breed']}<br>"
                     f"<b>Details:</b> <a href='{dog['details_link']}' target='_blank'>Click here</a><br><br>"
            )
        return []


class ActionShowAnimalsBestForAllergies(Action):
    def name(self) -> str:
        return "action_show_animals_best_for_allergies"

    def run(self, dispatcher: CollectingDispatcher, tracker, domain) -> list:
        allergy_friendly_pets = [
            {
                "name": "Poodle",
                "type": "Dog",
                "reason": "Hypoallergenic coat.",
                "image": "https://example.com/poodle.jpg",
                "details_link": "http://localhost:4200/poodle"
            },
            {
                "name": "Siberian Cat",
                "type": "Cat",
                "reason": "Produces less allergenic proteins.",
                "image": "https://example.com/siberian.jpg",
                "details_link": "http://localhost:4200/siberian"
            }
        ]

        dispatcher.utter_message(text="Here are some animals suitable for people with allergies:")
        for pet in allergy_friendly_pets:
            dispatcher.utter_message(
                text=f"<b>Pet Name:</b> {pet['name']}<br>"
                     f"<b>Type:</b> {pet['type']}<br>"
                     f"<b>Why Suitable:</b> {pet['reason']}<br>"
                     f"<b>Details:</b> <a href='{pet['details_link']}' target='_blank'>Click here</a><br><br>"
            )
        return []
