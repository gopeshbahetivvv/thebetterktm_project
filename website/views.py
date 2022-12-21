from typing import final
from django.shortcuts import render, get_object_or_404
from .models import Problem
from .forms import ProblemForm
from django.http import HttpResponseRedirect, JsonResponse
from django.contrib import messages
from django.urls import reverse
from django.views import View
from django.db.models import F
import json
# Create your views here.

class HomeView(View):

    def get(self, request):
        all_problems =  Problem.objects.all().order_by('-upvote')
        return render(request, 'index.html', {'all_p': all_problems})

    def post(self, request):
        # if 'item.id' in request.POST:
        #         count = ''
        #         solution_id = request.POST.get('item.id')
        #         if request.method == 'POST':
        #             solution = Problem.objects.get(pk=solution_id)
        #             solution.upvote = solution.upvote + 1
        #             count = solution.upvote
        #             solution.save()
        #             print(count)
        #             return JsonResponse({'count': count})
        #             # return HttpResponseRedirect("home")
        #         else:
        #             return HttpResponseRedirect("home")
        # else:
            if request.method == 'POST':
                form = ProblemForm(request.POST or None)
                if form.is_valid():
                    form.save()
                    success= "DONE"
                    return HttpResponseRedirect("home")
            else:  
                return HttpResponseRedirect("home")

def solution_page(request, solution_id):
    user_ip_group = request.META.get('HTTP_X_FORWARDED_FOR')  
    if user_ip_group:
        user_ip= user_ip_group.split(',')[-1].strip()
    else:
        user_ip= request.META.get('REMOTE_ADDR')

    count=''
    soluid= solution_id
    solution = Problem.objects.get(pk=solution_id)
    count= int(solution.upvote)
    
    li = list(solution.iptracker.split(", "))
    # print(li)
    if user_ip in li:
        pass
    else:
        solution.upvote = solution.upvote + 1
        solution.iptracker= solution.iptracker + ", "+ user_ip
        count = int(solution.upvote)
        solution.save()
    return JsonResponse({'count': count})
    # solution = Problem.objects.get(pk=solution_id)
    # user_id_database =  User.objects.all()
    # hello = "127.123.23.45"
    # print(user_id_database)
    # for userips in user_id_database:
    #     print(userips)
    #     if str(userips)== hello:
    #         print("Found")
    # new_user_ip = User()
    # new_user_ip.userip = "127.168.1.1"
    # new_user_ip.save()
    # arr= []
    

    # if user_ip in user_id_database:
    #     print('hello')
    # else:
    #     user_id_database.append(user_ip)
    # print(user_id_database)    
    # if user_ip not in arr:
    #     arr.append(user_ip)
    # print(arr)
    
    # return render(request, 'solution.html', {'solution': solution})

# def vote(request):
        # if request.method == 'POST':
        #     solution_id = request.object.GET("item.id")
        #     print(solution_id)
            # solution = Problem.objects.get(pk=solution_id)
            # solution.upvote = F('upvote') + 1
            # solution.save()
    # if request.POST.get('action') == 'post':
    #     count= ''
    #     id = request.POST.get('solutionid')
    #     print(id)
    #     post = get_object_or_404(Problem, id=id)
    #     post.upvote = post.upvote + 1
    #     count = post.upvote
    #     print(count)
    #     post.save()
    #     return JsonResponse({'count': count})     
            
# def upvote(request, solution_id):
#     if request.method == 'POST':
#         solution = Problem.objects.get(pk=solution_id)
#         solution.upvote = F('upvote') + 1
#         solution.save()
    

# def home(request):
#     try:
#         all_problems =  Problem.objects.all
#         return render(request, 'home.html', {'all_p': all_problems})
       
#     finally:   
#         if request.method == "POST":
#             form = ProblemForm(request.POST or None)
#             if form.is_valid():
#                 form.save()
#                 return HttpResponseRedirect(reverse("home"))
                                 
#         else:
#             HttpResponseRedirect(reverse("home"))



