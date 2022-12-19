# from django.shortcuts import render
# from django.http import HttpResponse, HttpResponseRedirect
# from django.utils import timezone
# from .models import ToDoList, Item
# from .forms import CreateNewList

# # Create your views here.
# def index(response, id):
# 	ls = ToDoList.objects.get(id=id)

# 	# if ls in response.user.todolist.all():

# 	if response.method == "POST":
# 		if response.POST.get("save"):
# 			for item in ls.item_set.all():
# 				if response.POST.get("c" + str(item.id)) == "clicked":
# 					item.complete = True
# 		else:
# 			item.complete = False
# 			item.save()

# 	elif response.POST.get("newItem"):
# 		txt = response.POST.get("new")

# 		if len(txt) > 2:
# 			ls.item_set.create(text=txt, complete=False)
# 		else:
# 			return render(response, "main/list.html", {"ls":ls})
# 	return render(response, "main/view.html", {})



# def create(response):
# 	if response.method == "POST":
# 		form = CreateNewList(response.POST)

# 		if form.is_valid():
# 			n = form.cleaned_data["name"]
# 			t = ToDoList(name=n)
# 			t.save()
# 			response.user.todolist.add(t)

# 		return HttpResponseRedirect("/%i" %t.id)

# 	else:
# 		form = CreateNewList()

# 	return render(response, "main/create.html", {"form":form})


# def home(request):
# 	return render(request, "main/home.html", {})


# def view(response):
# 	return render(response, "main/view.html", {})



from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.utils import timezone
from .models import ToDoList
from .forms import CreateNewList
# Create your views here.

def index(request, id):
	ls = ToDoList.objects.get(id=id)

	if request.method == "POST":
		if request.POST.get("save"):
			for item in ls.item_set.all():
				p = request.POST
				
				if "clicked" == p.get("c"+str(item.id)):
					item.complete = True
				else:
					item.complete = False

				if "text" + str(item.id) in p:
					item.text = p.get("text" + str(item.id))


				item.save()

		elif request.POST.get("add"):
			newItem = request.POST.get("new")
			if newItem != "":
				ls.item_set.create(text=newItem, complete=False)
			else:
				print("invalid")

	return render(request, "main/index.html", {"ls": ls})


def get_name(request):
	if request.method == "POST":
		form = CreateNewList(request.POST.get)

		if form.is_valid():
			n = form.cleaned_data["name"]
			t = ToDoList(name=n)
			t.save()
			print(t)
			
# 			return HttpResponseRedirect("/%i" %t.id)

# 	else:
# 		form = CreateNewList()

# 	return render(request, "main/create.html", {"form": form})


def home(request):
	return render(request, "main/home.html", {})


def view(request):
	l = ToDoList.objects.all()
	return render(request, "main/view.html", {"lists":l})











	