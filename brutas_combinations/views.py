from django.core.paginator import Paginator
from django.shortcuts import render
from django.http import HttpResponse
from django.utils import timezone

from .models import UserCombination

def generate_user_pass():
    temp_combinations=[]
    for num in range(1, 501):
        num_str = str(num)  # Convert number to string
        temp_combinations.append(num_str)
        # Store the combination and the current datetime in the database
        UserCombination.objects.create(username_str="Temp_UserName", password_str=num_str, created_at=timezone.now())

def generate_combinations(request):
     if request.method == "POST":
        generate_user_pass()

     return render(request, 'gen_combination/generate.html')


def display_combinations(request):
    user_combinations = UserCombination.objects.all()  # Retrieve all records

    paginator = Paginator(user_combinations, 10)  # Adjust the number as needed

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)  # Get the Page object for the requested page

    return render(request, 'user_combinations/display_user_combinations.html', {'page_obj': page_obj})

def selenium_driver():
    return

def web_driver(request):
    if request.method == "POST":
        selenium_driver()
        return render(request, 'web_driver/driver.html', {'success': True})
    
    return render(request, 'web_driver/driver.html')   
