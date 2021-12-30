from django.shortcuts import redirect, render
from django.http import Http404, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse

monthly_challenges = {
    'january': 'Eat no meat for entire month',
    'february': 'Walk for 20 minutes.',
    'march': 'Learn Django'
}

# Create your views here.


def index(request):
    months = list(monthly_challenges.keys())
    return render(request, 'challenges/index.html', {
        'months': months
    })


def monthly_challenge_by_number(request, month):
    try:
        months = list(monthly_challenges.keys())
        redirect_month = months[month - 1]
        redirect_path = reverse('month-challenge', args=[redirect_month])
        return HttpResponseRedirect(redirect_path)
    except:
        return HttpResponseNotFound('Unsupported month')


def monthly_challenge(request, month):
    try:
        response = monthly_challenges[month]
        return render(request, 'challenges/challenge.html', {
            'month': month,
            'text': response
        })
    except:
        raise Http404()
