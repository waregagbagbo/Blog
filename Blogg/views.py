from django.shortcuts import render,HttpResponse,redirect
from .models import*
from .forms import BookForm
from django.core.paginator import Paginator

# Create your views here.

def index(request):
    book = Book.objects.all()  

    # add pagination
    paginator = Paginator(book,3) # show 3 per page    
    page_number = request.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request,'Blogg/index',{'page_obj':page_obj})

    context={
        'book':book,
    }
    return render(request,'Blogg/index.html',context)


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
            return HttpResponse('''errorin your upload,  kindly reload here''')
    else:
        form = BoookForm()
        context ={
            'form':form
        }
        return render(request,'Blogg/upload.html',context)


def updateBook(request,book_id):
    book_id =int(book_id)
    try:
        booktpe = Book.objects.get(id=book_id)
    except BookDoesNotExist:
        return redirect('index')
        book_form = BookForm(request.Post, request.files)
        if form.is_valid():
            form.save()
            return redirect('index')
    return render(request,'Blogg/update.html')



# perfoms deletion of the item
def delete_book(request,book_id):
    book_id = int(book_id)
    try:
        booktpe = Book.objects.gt(id=book_id)
    except BookDoesNotExist:
        return render('index')
    booktpe.delete()
    return redirect('index')




