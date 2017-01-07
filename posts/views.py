from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Post

# Create your views here.

def post_create(request):
	return HttpResponse("create")

def post_detail(request, id):
	# instance = Post.objects.get(id=5)
	instance = get_object_or_404(Post, id = id)
	context = {
		"title": "detail",
		"instance": instance
	}
	return render(request, 'post_detail.html', context)

def post_list(request):
	queryset = Post.objects.all()

	context = {
			"object_list": queryset,
			"title": "List"
		}
	# if request.user.is_authenticated():

	# 	context = {
	# 		"title": "My user list"
	# 	}
	# else:
	# 	context = {
	# 		"title": "List"
	# 	}

	return render(request, 'index.html', context)

def post_update(request):
	return HttpResponse("update")

def post_delete(request):
	return HttpResponse("delete")	