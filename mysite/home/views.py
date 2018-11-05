from django.shortcuts import render

posts = [
    {
        'author': 'CoreyMS',
        'title': 'Blog Post 1',
        'content': 'First post content',
        'date_posted': 'August 27, 2018'
    },
    {
        'author': 'Jane Doe',
        'title': 'Blog Post 2',
        'content': 'Second post content',
        'date_posted': 'August 28, 2018'
    }
]

# Want it so when user enters website, it immediately goes 
# to login screen. May have a "rememember me" function or not later
def home(request):
    context = {
            'posts': posts
    }
    return render(request, 'users/login.html', context)

def about(request):
    return render(request, 'home/about.html')


