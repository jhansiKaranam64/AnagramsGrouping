from django.shortcuts import render
from itertools import groupby

from .models import Word

def home(request):
    return render(request,'home.html')
def group_anagrams(request):
    if request.method == 'POST':
        words_input = request.POST.get('words', '')
        words_list = words_input.split()
        sorted_words = sorted(words_list, key=lambda w: sorted(w))
        grouped_anagrams = [list(group) for _, group in groupby(sorted_words, key=lambda w: sorted(w))]

        return render(request, 'group_anagrams.html', {'anagrams': grouped_anagrams, 'input': words_input})
    else:
        return render(request, 'group_anagrams.html')
