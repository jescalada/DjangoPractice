from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect

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
        return HttpResponseRedirect(f'/challenges/{forward_month}')
    except IndexError as e:
        return HttpResponseNotFound(f'Invalid request: {e}')


def monthly_challenge(request, month):  # month is a keyword argument that got sent from the original path
    try:
        return HttpResponse(months[month])
    except KeyError as e:
        return HttpResponseNotFound(f'Invalid request: {e}')
