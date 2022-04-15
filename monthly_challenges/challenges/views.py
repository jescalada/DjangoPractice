from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
# VIEWS ARE RESPONSIBLE FOR PROCESSING REQUESTS AND CREATING RESPONSES

months = {
    'january': "Do some exercise.",
    'february': "Practice Django.",
    'march': "Read about Agile Development.",
    'april': "Practice some 日本語.",
    'may': "Do some leetcode exercises.",
}


def monthly_challenge(request, month):  # month is a keyword argument that got sent from the original path
    return HttpResponse(months[month])
