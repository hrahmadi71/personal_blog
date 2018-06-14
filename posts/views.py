from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from json import JSONEncoder
from django.views.decorators.csrf import csrf_exempt
from posts.models import User, Token, Post, Comment
from datetime import datetime

# Create your views here.

def index(request):
    latest_posts_list = Post.objects.order_by('-date')[:10]
    output = ', '.join(['Title: {} --- Text: {}'.format(p.title, p.text) for p in latest_posts_list])
    return HttpResponse(output)


@csrf_exempt
def new_post(request):
    #TODO: validate token, user, and checking the title and text to have values.
    this_token = request.POST['token']
    this_user = User.objects.get(token__token = this_token)
    now = datetime.now()
    p = Post(user=this_user, title=request.POST['title'], text=request.POST['text'], date=now)
    p.save()
    return JsonResponse({
        'status': 'ok'
    }, encoder=JSONEncoder)


@csrf_exempt
def leave_a_comment(request):
    #TODO: validate post, and checking the email and other variables to have values.
    post_id = request.POST['post_id']
    p = Post.objects.get(pk=post_id)

    full_name = request.POST['full_name']
    email = request.POST['email']
    score = request.POST['score']
    text = request.POST['text']
    now = datetime.now()

    cmnt = Comment(post=p,
                    full_name=full_name,
                    email=email,
                    score=score,
                    text=text,
                    display=False,
                    date=now)
    cmnt.save()
    return JsonResponse({
        'status': 'ok'
    }, encoder=JSONEncoder)

