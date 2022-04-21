from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse

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
    response_data = f"""
        <ul>
            {"".join([f'<li><a href="{reverse("month-challenge", args=[month])}">{month.capitalize()}</a></li>' for month in list(months.keys())])}
        </ul>
    """
    return HttpResponse(response_data)


def monthly_challenge_by_number(request, month):
    try:
        forward_month = list(months.keys())[month - 1]
        redirect_path = reverse('month-challenge', args=[forward_month])  # tries to match one of the paths inside it
        return HttpResponseRedirect(redirect_path)  # redirect to the path found
    except IndexError as e:
        return HttpResponseNotFound(f'Invalid request: {e}')


def monthly_challenge(request, month):  # month is a keyword argument that got sent from the original path
    try:
        return HttpResponse(months[month])
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