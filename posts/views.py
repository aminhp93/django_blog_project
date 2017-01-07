from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def post_create(request):
	return HttpResponse("create")

def post_detail(request):
	return HttpResponse("detail")

def post_list(request):
	return HttpResponse("list")

def post_update(request):
	return HttpResponse("update")

def post_delete(request):
	return HttpResponse("delete")	