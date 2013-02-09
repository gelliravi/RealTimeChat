# -*- coding: utf-8 -*-
from django.contrib.auth.decorators import user_passes_test,login_required
from django.shortcuts import get_object_or_404, render, redirect
from django_socketio import broadcast, broadcast_channel, NoSocket
from django.shortcuts import render_to_response
from chat.models import Comments, User, Mess
from django.http import HttpResponse, HttpResponseServerError
from django.contrib.sessions.models import Session
from django.views.decorators.csrf import csrf_exempt

import redis

@login_required
def home(request):
  comments = Comments.objects.select_related().all()[0:100]
  return render(request, 'chat/home.html', locals())

@csrf_exempt
def node_api(request):
    try:

        session = Session.objects.get(session_key=request.POST.get('sessionid'))
        user_id = session.get_decoded().get('_auth_user_id')
        user = User.objects.get(id=user_id)
        r = redis.StrictRedis(host='localhost', port=6379, db=0)                  
                  
        Comments.objects.create(user=user, text=request.POST.get('comment','error get'))
        
        r.publish('chat', user.first_name + " " + user.last_name + ': ' + request.POST.get('comment','error get'))
        
        return HttpResponse("")
    except Exception, e:
        return HttpResponseServerError(str(e))