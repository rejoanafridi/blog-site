from django.shortcuts import render, HttpResponse, redirect
from main.models import*
from main.models import Category

# Create your views here.


def index(request):
    all_post = Post.objects.all()
    categories = Category.objects.all()
    context = {
        "blog": all_post,
        "category": categories
    }
    return render(request, 'main/index.html', context)


def details(request):
    return render(request, 'main/blogview.html')


def post(request, slug_text):
    try:
        post = Post.objects.get(slug=slug_text)
    except:
        return HttpResponse("page not found")  

    if request.method == "GET":
        categories = Category.objects.all()
        
        
        # querry.views = querry.views + 1
        context = {
            'post': post,
            'category': categories

        }
        return render(request, 'main/blogview.html', context)
    elif request.method == 'POST':
        name = request.POST['nameInput']
        email = request.POST['emailInput']
        text = request.POST['textDesc']
        commenter = Comments(name=name, email= email, text=text, connection=post)
        commenter.save()
        return redirect('/post2/'+slug_text)





# def comment(request):
# if request.method == "GET":
#         cmshow = Comments.objects.all()
#         context = {
#             'cmnt': cmshow
#         }
#         return render(request, 'main/blogview.html', context)
#     elif request.method == 'POST':
#         name = request.POST['nameInput']
#         email = request.POST['emailInput']
#         text = request.POST['textDesc']
#         commenter = Comments(name=name, email= email, text=text)
#         commenter.save()
#     else:
#         return render(request, 'main/blogview.html')
    
    

    

