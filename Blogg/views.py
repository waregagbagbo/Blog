from django.shortcuts import render,HttpResponse,redirect
from .models import*
from .forms import BookForm
from django.core.paginator import Paginator
from django.views.generic import ListView,DetailView


# Create your views here.

def index(request):
    book = Book.objects.all() 
    # add pagination
    paginator = Paginator(book,9) # show 6   per page    
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context={
        'book':book,
        'page_obj':page_obj
    }
    return render(request,'Blogg/index.html',context)


# shows the books detail view part function
def BookDetail(request,id):
    books = Book.objects.get(id=id)
    context={
        'books':books,
    }
    return render(request,'Blogg/book_detail.html',context)



# displays posts lists as per the currently published from the databse
def PostPage(request):
    queryset = Post.objects.filter(status='Pub').order_by('-created_on')

    paginator = Paginator(queryset,4) # show 4 posttings per page    
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {
        'queryset':queryset,
        'page_obj': page_obj
    }
    return render(request,'Blogg/post_page.html',context)

# let us run the post detail section for the posts
def PostDetailPage(request,slug):
    #= Post.objects.get(slug=slug)
    posts = Post.objects.filter(slug=slug)
    context ={
        'posts':posts
    }
    return render(request,'Blogg/post_detail.html',context)



def upload(request):
    #instantiate the form
    form = BookForm()
    #checcks  whether the user is visiting the form for the first time or data is being submitted
    if request.method == 'POST':
        form = BookForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('index')
        else:
            return HttpResponse('''error in your upload,  kindly reload here''')
    else:
        form = BoookForm()
        context ={
            'form':form
        }
        return render(request,'Blogg/upload.html',context)




# displays book detail function view
def updateBook(request,book_id):
    book_id =int(book_id)
    try:
        booktype = Book.objects.get(id=book_id)
    except BookDoesNotExist:
        return redirect('index')
        book_form = BookForm(request.Post, request.files)
        if form.is_valid():
            form.save()
            return redirect('index')
    return render(request,'Blogg/update.html')

# perfoms deletion of the item
"""def delete_book(request,book_id):
    book_id = int(book_id)
    try:
        booktpe = Book.objects.gt(id=book_id)
    except BookDoesNotExist:
        return render('index')
    booktpe.delete()
    return redirect('index')"""

