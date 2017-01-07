from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib import messages
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, HttpResponseRedirect
from .models import Post
from .forms import PostForm

# Create your views here.

def post_create(request):
	form = PostForm(request.POST or None)
	if form.is_valid():
		instance = form.save(commit=False)
		print(form.cleaned_data.get("title"))
		instance.save()
		messages.success(request, "Successfully Created", extra_tags="some-tag")
		return HttpResponseRedirect(instance.get_absolute_url())

	# if request.method == "POST":
	# 	print(request.POST)
	# 	print(request.POST.get("title"))
		# Post.objects.create(title=title)
	context = {
		"form": form,
	}	
	return render(request, "post_form.html", context)

def post_detail(request, id=None):
	# instance = Post.objects.get(id=5)
	instance = get_object_or_404(Post, id = id)
	context = {
		"title": "detail",
		"instance": instance
	}
	return render(request, 'post_detail.html', context)

def post_list(request):
	queryset_list = Post.objects.all().order_by("-timestamp")
	paginator = Paginator(queryset_list, 3) # Show 25 contacts per page
	page_request_var = "hello"
	page = request.GET.get(page_request_var)
	try:
		queryset = paginator.page(page)
	except PageNotAnInteger:
        # If page is not an integer, deliver first page.
		queryset = paginator.page(1)
	except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
		queryset = paginator.page(paginator.num_pages)

	context = {
			"object_list": queryset,
			"title": "List",
			"page_request_var": page_request_var,
		}
	# if request.user.is_authenticated():

	# 	context = {
	# 		"title": "My user list"
	# 	}
	# else:
	# 	context = {
	# 		"title": "List"
	# 	}

	return render(request, 'post_list.html', context)



def post_update(request, id=None):
	instance = get_object_or_404(Post, id = id)

	form = PostForm(request.POST or None, instance = instance)
	if form.is_valid():
		instance = form.save(commit =False)
		instance.save()

		messages.success(request, "Successfully saved")
		return HttpResponseRedirect(instance.get_absolute_url())

	context = {
		"title": instance.title,
		"instance": instance,
		"form": form,
	}

	return render(request, 'post_form.html', context)

def post_delete(request, id=None):
	instance = get_object_or_404(Post, id=id)
	instance.delete()
	messages.success(request, "Successfully deleted")
	return redirect("posts:list")





	


