from django.shortcuts import render,HttpResponse,redirect

# Create your views here.


from books import models


def book(request):
    book_list = models.Book.objects.all()  # queryset [obj,....]


    return render(request,"book.html",{"book_list":book_list})


def add_book(request):
    if request.method == "POST":
        print(request.POST)
        title = request.POST.get("title")
        price = request.POST.get("price")
        pub_date = request.POST.get("pub_date")
        publish = request.POST.get("publish")
        is_pub = request.POST.get("is_pub")

        obj = models.Book.objects.create(title=title, price=price, publish=publish, pub_date=pub_date,
                                         is_pub=is_pub)
        print(obj.title)

        return redirect("/book/")

    return render(request, "addBook.html")
def del_book(request,id):
    models.Book.objects.filter(id=id).delete()

    return redirect("/book/")


def mod_book(request,id):

    book_i = models.Book.objects.filter(id=id)
    if request.method == "POST":
        print(request.POST)
        title = request.POST.get("title")
        price = request.POST.get("price")
        pub_date = request.POST.get("pub_date")
        publish = request.POST.get("publish")
        is_pub = request.POST.get("is_pub")

        models.Book.objects.filter(id=id).update(title=title,price=price,pub_date=pub_date,publish=publish,is_pub=is_pub)
        return redirect('/book/')
    return render(request, "modify.html", {"book_i": book_i.first()})
