from django.shortcuts import render,redirect
from django.http import HttpResponse, HttpResponseRedirect
from .models import ToDoList, Item
from .forms import CreateNewList

# Create your views here.

def index(response,id):
    #ls = ToDoList.objects.get(id=id)
    #item = ls.item_set.get(id=2)
    # return HttpResponse("<h1>%s</h1><br><h2>%s</h2>"%(ls.name,str(item.text)))

    return render(response,"main/base.html",{})


def home(response):


    return render(response,"main/home.html",{})

def list(response,id):


    list = ToDoList.objects.get(id=id)
    return render(response,"main/list.html",{"list":list})


def create(response):


    if response.method == "POST":

        form = CreateNewList(response.POST)

        #check if the inputs are valid, such as no null and email address is address

        if form.is_valid():


            #cleaned_data returns dictionary

            name = form.cleaned_data["name"]
            t = ToDoList(name=name)
            t.save()

            # adds todolist to the user

            response.user.todolist.add(t)

        return HttpResponseRedirect("/list/%i"%t.id)




    #create instance

    else:

        form = CreateNewList();

    return render(response,"main/form.html",{"form":form})


def edit(response,id):

    list = ToDoList.objects.get(id=id)
    items = list.item_set.all()

    if list == response.user.todolist.all():

         if response.method == "POST":
        
            if response.POST.get("save"):

                for item in items:

                    if response.POST.get("c"+str(item.id)) == "checked":

                        item.completion = True

                    else:
                    
                        item.completion = False
                
                item.save()

            if response.POST.get("saveNewItem"):

                 if len(response.POST.get("newItem"))>3:

                     t=ToDoList(id=id)

                     t.item_set.create(text=response.POST.get("newItem"),completion=False)

                 else:

                     print("Please Enter Something Longer")
            

    

            return render(response,"main/edit.html",{"list":list,"items":items})


    return redirect("/view")


def view(response):


    return render(response,"main/view.html",{})


