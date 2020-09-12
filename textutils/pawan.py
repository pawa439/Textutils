from django.http import HttpResponse
from django.shortcuts import render
def index(request):
    return render(request,'index.html')
def analyze(request):
    djtext = request.POST.get('text','default')
    removepunc = request.POST.get('removepunc','off')
    fullcaps = request.POST.get('fullcaps','off')
    print(removepunc)
    print(djtext)
    if removepunc == "on":
      punctuations = '''!()-[]{};:'"\,<>./@#$%^&*_~!'''
      analyzed = ""
      for char in djtext:
         if char not in punctuations:
              analyzed = analyzed + char
         params = {'purpose': 'Removed Punctuations', 'analyzed_text': analyzed}
         return render(request, 'Analyze.html', params)
    elif(fullcaps=="on"):
        analyzed = ""
        for char in djtext:
                analyzed = analyzed + char.upper()
                params = {'purpose': 'changed to uppercase', 'analyzed_text': analyzed}
        return render(request, 'Analyze.html', params)
    else:
        return HttpResponse("Error")

