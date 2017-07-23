

# Create your views here.

from django.shortcuts import render, render_to_response
def main(request):
    return render_to_response("index.html")
def sk1(request):
    return render_to_response("sk1.html")
def kp1(request):
    return render_to_response("kp1.html")