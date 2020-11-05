from django.shortcuts import render
from .models import Search
from django.contrib import messages

from django.utils.datastructures import MultiValueDictKeyError


def home(request):
    return render(request, 'search.html')


def search(request):

        try:
            query = request.GET['query']
        except MultiValueDictKeyError:
            query = False

        # srchs = Search.objects.all()
        srchs = Search.objects.filter(search_str__icontains=query)
        print(srchs)

        if Search.objects.filter(search_str__icontains=query).exists():
            return render(request, 'result.html', {'srchs': srchs})

        else:
            messages.info(request, "Please check the spelling you have entered. ")
            return render(request, 'search.html')


        # search_val = request.POST['search_str']
        #
        # if search_val == "sachin":
        #     return render(request, 'sachin.html')
        # elif search_val == "dhoni":
        #     return render(request, 'dhoni.html')
        # elif search_val == "dravid":
        #     return render(request, 'dravid.html')
        #
        # else:
        #     return messages.info(request, "Please enter sachin or dhoni or dravid")

# Create your views here.
