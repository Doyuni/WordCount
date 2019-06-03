from django.shortcuts import render

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def result(request):
    fulltext = request.GET['fulltext'] # 입력 text 전체
    fulltext = fulltext.lower() # 모두 소문자로 변경
    for i in range(0, len(fulltext)):
        if fulltext[i].isalnum() == False:
            fulltext = fulltext.replace(fulltext[i], ' ') # 특수문자 공백처리
    words = fulltext.split() # tokenizing
    words_count = { word : words.count(word) for word in words } # comprehension
    words_list = sorted(words_count.items(), key=lambda x: x[1], reverse=True) # sorting
    return render(request, 'result.html', {'full': fulltext, 'length': len(words), 'countList' : words_list}) 