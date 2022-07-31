from string import punctuation
from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    params = {'name':'earther', 'place':'Mars'}
    return render (request, 'index.html', params);
    # return HttpResponse("Home")

def analyze(request):
    # Get the text
    djtext = request.POST.get('text', 'default')

    #checkbox value
    removepunc = request.POST.get('removepunc', 'off')
    fullcaps = request.POST.get('fullcaps', 'off')
    newlineremover = request.POST.get('newlineremover', 'off')
    extraspaceremover = request.POST.get('extraspaceremover', 'off')
    charactercounter = request.POST.get('charactercounter', 'off')
    if removepunc == "on":
        punctuation = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        analyzed = ""
        for char in djtext:
            if char not in punctuation:
                analyzed = analyzed + char
        params = {'purpose':'Remove Punctuations', 'analyzed_text': analyzed}
        djtext = analyzed

    if (fullcaps == 'on'):
        analyzed = ""
        for char in djtext:
            analyzed = analyzed + char.upper()
            params = {'purpose':'Change to Uppercase', 'analyzed_text': analyzed}
            djtext = analyzed
        
    if (newlineremover == 'on'):
        analyzed = ""
        for char in djtext:
            if char != "\n":
                analyzed = analyzed + char
            params = {'purpose':'Change to Uppercase', 'analyzed_text': analyzed}
        
        djtext = analyzed
    if (extraspaceremover == 'on'):
        analyzed = ""
        for index, char in enumerate(djtext):
            if not(djtext[index] == " " and djtext[index+1]==" "):
                analyzed = analyzed + char
            params = {'purpose':'Change to Uppercase', 'analyzed_text': analyzed}
        
        djtext = analyzed
    if (charactercounter == 'on'):
        analyzed = "The number of characters are: " + str(len(djtext))
        params = {'purpose':'Character Count', 'analyzed_text': analyzed}

    if(removepunc != "on" and newlineremover != "on" and extraspaceremover != "on" and charactercounter != "on" and fullcaps != "on"):
     return HttpResponse("Please select any operation and try again!")

    return render(request, 'analyze.html', params)
