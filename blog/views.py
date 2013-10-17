from django.http import HttpResponse
from django.shortcuts import render
from blog.models import Post

from blog.forms import ContactForm
from django.core.mail import send_mail
from django.http import HttpResponseRedirect


def Main(request):
	lastest_posts = Post.objects.filter(display=True).order_by("-pub_date",) [:2]
	return render(request, "main.html", {"lastest_posts": lastest_posts, })

def Posts(request): # list of Posts in blog
	posts = Post.objects.all().order_by("-pub_date")
	return render(request, "blog.html", {"posts" : posts,})

def post(request, slug):
	post = Post.objects.get(slug=slug) ## Atvaizduoja atitinkama posta pagal slug.
										## Apparently skirtinguose viewsuose galima
										## naudoti vienodus vardus.
	return render(request, "post.html", {"post" : post})

def About(request):
	post = Post.objects.get(title = "About")
	return render(request, "about.html", {"post" : post})


def Contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            send_mail(
                cd['subject'],
                cd['message'],
                cd.get('email', 'noreply@example.com'),
                ['eimantas.stonys@gmail.com'],
            )
            return HttpResponseRedirect('/contact/thanks/')
    else:
        form = ContactForm()
    return render(request, 'contact.html', {'form': form})

def Thanks(request):
    return render(request, "thanks.html",)

