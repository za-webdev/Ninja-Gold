# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render,HttpResponse,redirect
from time import localtime,strftime
from django.contrib import messages
import random


def index(request):
	if 'total' not in request.session:
		request.session['total']=0
	

	return render(request,"ninja_gold/ninja.html")

def gold_here(request):
	context={}
	
	if request.POST['name']=='farm':
		request.session['gold']=random.randrange(10,20)
		
		request.session['total']+=request.session['gold']
		messages.add_message(request, messages.SUCCESS, 'You earned '+str(request.session['gold'])+' gold(s) from the farm')
		
		

	if request.POST['name']=='cave':
		request.session['gold']=random.randrange(5,10)
		request.session['total']+=request.session['gold']
		
		messages.add_message(request, messages.SUCCESS, 'You earned '+str(request.session['gold'])+' gold(s) from the Cave')
		

	if request.POST['name']=='house':
		request.session['gold']=random.randrange(2,5)
		request.session['total']+=request.session['gold']
		
		messages.add_message(request, messages.SUCCESS, 'You earned '+str(request.session['gold'])+' gold(s) from the House')
		

	if request.POST['name']=='casino':
		request.session['gold']=random.randrange(-50,50)
		request.session['total']+=request.session['gold']

		if request.session['gold']>0:
			messages.add_message(request, messages.SUCCESS, 'You earned '+str(request.session['gold'])+' gold(s) from the Casino')
		else:
			messages.add_message(request, messages.ERROR, 'You lost '+str(request.session['gold'])+' gold(s) from the Casino')

	
	return redirect('/')

def reset(request):

	request.session.clear()

	return redirect('/')
