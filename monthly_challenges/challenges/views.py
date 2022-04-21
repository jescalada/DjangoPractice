from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse
from django.template.loader import render_to_string
from django.shortcuts import render

# Create a connection using MongoClient. You can import MongoClient or use pymongo.MongoClient
from pymongo import MongoClient

# Create your views here.
# VIEWS ARE RESPONSIBLE FOR PROCESSING REQUESTS AND CREATING RESPONSES

months = {
    'january': "Do some exercise.",
    'february': "Practice Django.",
    'march': "Read about Agile Development.",
    'april': "Practice some 日本語.",
    'may': "Do some leetcode exercises.",
}


def index(request):
    month_list = list(months.keys())
    return render(request, "challenges/index.html", {
        'months': month_list
    })


def monthly_challenge_by_number(request, month):
    try:
        forward_month = list(months.keys())[month - 1]
        redirect_path = reverse('month-challenge', args=[forward_month])  # tries to match one of the paths inside it
        return HttpResponseRedirect(redirect_path)  # redirect to the path found
    except IndexError as e:
        return HttpResponseNotFound(f'Invalid request: {e}')


def monthly_challenge(request, month):  # month is a keyword argument that got sent from the original path
    try:
        return render(request, 'challenges/challenge.html', {
            'month': month,  # We don't capitalize it here because we restrict it to the core business logic
            'text': months[month],
        })
    except KeyError as e:
        return HttpResponseNotFound(f'Invalid request: {e}')


def display_unicorns(request):
    dbname = get_database()

    # Create a new collection
    collection_name = dbname["unicorns"]

    item_details = collection_name.find()
    return HttpResponse(item_details)


def get_database():
    # Provide the mongodb atlas url to connect python to mongodb using pymongo
    CONNECTION_STRING = "mongodb+srv://juan:Rocco123@cluster0.nxfhi.mongodb.net/"

    client = MongoClient(CONNECTION_STRING)

    # Create the database for our example (we will use the same database throughout the tutorial
    return client['A3']