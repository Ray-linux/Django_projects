# i have creat this file
from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return render(request, 'index.html')

# def about(request):
    # return HttpResponse("Rahul")


# def removepunc(request):
#     # get the text
#     djtext= print(request.GET.get('text', 'default'))
#     print(djtext)
#     # Analyze the text
#     return HttpResponse("removepunc")

# def capitalizefirst(request):
#     return HttpResponse("capitalizefirst")

def analyze(request):
    # return render(request, 'analyze.html')
    # get the text
    djtext = request.POST.get('text', 'default')
    removepunc = request.POST.get('removepunc',  'default')
    fullcaps = request.POST.get('fullcaps',  'off')
    newlineremover = request.POST.get('newlineremover', 'off')
    extraspaceremover = request.POST.get('extraspaceremover', 'off')
    # print(removepunc)
    # print(djtext)
    if (removepunc == "on"):
        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        analyzed = ""
        for char in djtext:
            if char not in punctuations:
                analyzed = analyzed + char

        params = {'purpose': 'removed Punctuation', 'analyzed_text': analyzed}
        djtext = analyzed
        # return render(request, 'analyze.html', params)
    if (fullcaps == "on"):
        analyzed = ""
        for char in djtext:
            analyzed = analyzed + char.upper()

        params = {'purpose': 'changed to uppercase', 'analyzed_text': analyzed}
        djtext = analyzed
        # return render(request, 'analyze.html', params)

    if (newlineremover == "on"):
        analyzed = ""
        for char in djtext:
            if char != "\n" and char != "\r":
                analyzed = analyzed + char

        params = {'purpose': 'Removed New Lines', 'analyzed_text': analyzed}
        djtext = analyzed
        # return render(request, 'analyze.html', params)

    if (extraspaceremover == "on"):
        analyzed = ""
        for index, char in enumerate(djtext):
            if not (djtext[index] == " " and djtext[index+1] == " "):
                analyzed = analyzed + char

        params = {'purpose': 'extra space remover', 'analyzed_text': analyzed}

    if(removepunc != "on" and fullcaps != "on" and newlineremover != "on" and extraspaceremover != "on"):
        return HttpResponse("Error")

    return render(request, 'analyze.html', params)

