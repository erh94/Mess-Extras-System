from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect, HttpResponse
from django.conf import settings
from django.contrib.auth import authenticate, login, logout
from django.views.generic.edit import FormView, UpdateView, DeleteView
import requests
from requests.auth import HTTPBasicAuth
import base64
import json
from datetime import datetime
from django.core.exceptions import ObjectDoesNotExist
from .forms import GuestBookEntryForm

from django.contrib.auth import get_user_model
User = get_user_model()

baseurl =  settings.OAUTH_BASE_URL

SSO_TOKEN_URL = 'https://gymkhana.iitb.ac.in/sso/oauth/token/'
SSO_PROFILE_URL = 'https://gymkhana.iitb.ac.in/sso/user/api/user/?fields=first_name,last_name,insti_address,mobile,roll_number'

def index(req):
    url = 'login/'
    return render(req,'guestBook/login.html',{'url':url})

class MessEntryView(FormView):
    form_class = GuestBookEntryForm
    template_name = 'guestBook/entry.html'
    success_url = '/logout/'
    login_url = '/mess/home'

    def get(self,request,*args,**kwargs):
        next_ = self.success_url

        if request.user.is_authenticated:
            return render(request, self.template_name,
            {'form':self.form_class,'user':user})
        else:
            return HttpResponseRedirect(self.login_url)

    def post(self,request,*args,**kwargs):
        form = self.form_class(request.POST)
        next_ = self.success_url

        if form.is_valid():
            extra = form.cleaned_data['extra']   
            cost = form.cleaned_data['cost']
            quantity = form.cleaned_data['quantity']
            amount = cost * quantity
            hostel = request.user.hostel
            newEntry = GuestBookEntryForm(user=request.user,extra=extra,cost=cost,quantity=quantity,amount=amount)
            
            try:
                newEntry.save()
                return render(request,'guestBook/print.html')
            except Exception as e:
                errorCode = 1
                errorMsg = "Unable to save object. Please Logout and Try Again"
                return render(request,'guestBook/error.html',{'errorCode':errorCode,'errormsg':errorMsg})

def client_login(req):
     
     authorize = settings.AUTHORISE_URL
     client_id =  settings.CLIENT_ID
     state = 200
     redirect_uri = settings.REDIRECT_URI_1
     scope = "profile%20ldap%20insti_address%20send_mail%20program"
    #  scope = "basic"     
     url = '{}{}?client_id={}&response_type=code&scope={}&state={}'.format(baseurl,authorize,client_id,scope,state)
    #  print(url)

     return redirect(url)

def authenticated(req):
    state = req.GET.get('state')
    authCode = req.GET.get('code')
    error = req.GET.get('error','')


    usrPass = "{}:{}".format(settings.CLIENT_ID,settings.CLIENT_SECRET)
    authenticationToken = base64.b64encode(usrPass.encode('utf-8')).decode('utf-8')
    headers = {'Authorization':'Basic {}'.format(authenticationToken),'Content-type': 'application/x-www-form-urlencoded'}
    data = 'code=' + authCode + '&redirect_uri=' + settings.REDIRECT_URI_1 + '&grant_type=authorization_code'
    response = requests.post(
        SSO_TOKEN_URL,
        data=data,
        headers= headers,
        verify=False
    )
    response_json = response.json()
    # print(response_json)


    # get profile
    profile_response = requests.get(
        SSO_PROFILE_URL,
        headers={"Authorization": "Bearer " + response_json['access_token']}, verify=False)

    profile_json = profile_response.json()

    roll_number = profile_json['roll_number']
    first_name = profile_json['first_name']
    last_name = profile_json['last_name']
    room = profile_json['insti_address']['room']
    hostel = profile_json['insti_address']['hostel']
    hostel_name = profile_json['insti_address']['hostel_name']

    params = [roll_number,first_name,last_name,room,hostel,hostel_name]

    checkEmpty(params)

    try:
        user = User.objects.get(username=profile_json['roll_number'])
        print('User Present')

    except ObjectDoesNotExist:
        print("New User")
        user = User.objects.create_user(username=roll_number,first_name=first_name,last_name=last_name,email='{}@iitb.ac.in'.format(roll_number),hostel=hostel,hostel_name=hostel_name,room=room)
        user.save()

    login(req,user)
    print(req.user.is_authenticated)
    return HttpResponseRedirect('/mess/entry')

def checkEmpty(params):
    for parameter in params:
        if parameter is '':
            return redirect('https://gymkhana.iitb.ac.in/sso/user/')


def LoginRequest(request):
    print(request.user.is_authenticated)
    print(request.user.username)
    print(request.user.first_name)
    print(request.user.last_name)
    print(request.user.hostel)
    print(request.user.hostel_name)
    print(request.user.email)
    return render(request,'guestBook/mess.html')