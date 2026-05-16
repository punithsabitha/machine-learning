import nltk
from nltk.chat.util import Chat, reflections

pairs = [

    [
        r"(.*) machine learning ?",
        ["Machine Learning is a technology where computers learn from data."]
    ],

    [
        r"(.*) examples ?",
        ["Face Recognition, Voice Assistant, Spam Detection, Self Driving Cars and Recommendation Systems are examples."]
    ],

    [
        r"(.*) face recognition ?",
        ["Face Recognition helps identify people using images and videos."]
    ],

    [
        r"(.*) voice assistant ?",
        ["Voice assistants like Siri and Alexa use Machine Learning."]
    ],

    [
        r"(.*) spam detection ?",
        ["Spam Detection filters unwanted emails automatically."]
    ],

    [
        r"(.*) recommendation system ?",
        ["Recommendation systems suggest movies, songs and products."]
    ],

    [
        r"(.*) self driving cars ?",
        ["Self driving cars learn road conditions using Machine Learning."]
    ],

    [
        r"hi|hello|hey",
        ["Hello!", "Hi there!"]
    ],

    [
        r"how are you ?",
        ["I am fine. Thank you!"]
    ],

    [
        r"quit",
        ["Bye! Have a nice day."]
    ]

]

def chat():
    print("Hi! I am a Machine Learning Chatbot.")
    chatbot = Chat(pairs, reflections)
    chatbot.converse()

if __name__ == "__main__":
    chat()