#Imports
from django import forms
from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required 
from .models import Profile,Tag,Startup,Teammember
from django.db.models import Q
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login,logout
from django.http import HttpResponse
from .forms import SignUpForm,StartupForm
from django.urls import reverse_lazy
from django.views.generic import ListView, TemplateView

# Created views are here.
def update_user_data(user):
    Profile.objects.update_or_create(user=user, defaults={'mob':user.profile.mob,'name':user.profile.name,'typee':user.profile.typee,})

def landing(request):
    return render(request,'core/landing.html')
def signin(request):
    if request.method =='POST':
        username=request.POST.get('username')
        password=request.POST.get('password')

        try:
            user=User.objects.get(username=username)
        except:
            messages.error(request, 'User does not exist')

        user=authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            if (user.profile.typee=="investor"):
                #print("chackpoint3")
                return redirect('explore')
            else:
                return redirect('profile')
            
        else:
            messages.error(request, 'Invalid credentials')    

    context={}
    return render(request, 'core/signin.html', context)
   
def signup(request):
    form=SignUpForm(request.POST, request.FILES)
    if request.method=='POST':
        #print("chackpoint1")
        form=SignUpForm(request.POST,request.FILES)
        
        #print("chackpoint2")
        user=form.save()
      
        user.refresh_from_db()
        user.profile.mob = form.cleaned_data.get('mob')
        update_user_data(user) 
        user.profile.name = form.cleaned_data.get('name')
        update_user_data(user) 
        #if(form.cleaned_data.get('typee')):
            #print("checkpoint3")
        user.profile.typee = form.cleaned_data.get('typee')
        update_user_data(user) 
        user.profile.dp = form.cleaned_data.get('dp')
        if(form.cleaned_data.get('dp')):
            print("bhnjkl")
        update_user_data(user) 
      
        user.save()
        raw_password = form.cleaned_data.get('password1')
        user=authenticate(username=user.username, password=raw_password)
        login(request,user)
        
        if (user.profile.typee=="investor"):
            print("chackpoint3")
            return redirect('explore')
        else:
            return redirect('profile')
    
    return render(request,'core/signup.html',{'form':form})

@login_required(login_url='login')
def explore(request):
    #filterr=''
    if request.method=='POST':
        filterr=request.POST['filterr']
        #redirect
    
        q = request.GET.get('q') if request.GET.get('q') != None else ''
        if q=='':
            startups= Startup.objects.all().order_by(filterr)
        else:
            startups= Startup.objects.filter(tags__name=q).order_by(filterr)
        
 
    else:
        q = request.GET.get('q') if request.GET.get('q') != None else ''
        if q=='':
            startups= Startup.objects.all()
        else:
            startups= Startup.objects.filter(tags__name=q)

    tags= Tag.objects.all()
    context={'startups': startups,'tags':tags,'q':q}
    return render(request,'core/explore.html',context)

@login_required(login_url='login')
def listt(request):
    
    
    if request.method == 'POST':
       
        StartupForm1 = StartupForm(request.POST, request.FILES)
        if StartupForm1.is_valid():
            startup= Startup()
            startup.owner=request.user
            startup.name=StartupForm1.cleaned_data['name']
            startup.site=StartupForm1.cleaned_data['site']
            startup.email=StartupForm1.cleaned_data['email']
            startup.problem=StartupForm1.cleaned_data['problem']
            startup.bio=StartupForm1.cleaned_data['bio']
            startup.solution=StartupForm1.cleaned_data['solution']
            startup.edge=StartupForm1.cleaned_data['edge']
            startup.RModel=StartupForm1.cleaned_data['RModel']
            startup.use_of_funds=StartupForm1.cleaned_data['use_of_funds']
            startup.equity=StartupForm1.cleaned_data['equity']
            startup.investment=StartupForm1.cleaned_data['investment']
            startup.valuation=StartupForm1.cleaned_data['valuation']
            startup.pfy=StartupForm1.cleaned_data['pfy']
            startup.revenue_pfy=StartupForm1.cleaned_data['revenue_pfy']
            startup.revenue_total=StartupForm1.cleaned_data['revenue_total']
            startup.team=StartupForm1.cleaned_data['team']
            startup.image=StartupForm1.cleaned_data['image']
            startup.teamimage=StartupForm1.cleaned_data['teamimage']
            startup.net_margin=StartupForm1.cleaned_data['net_margin']
            startup.gross_margin=StartupForm1.cleaned_data['gross_margin']
            startup.short_term_debt=StartupForm1.cleaned_data['short_term_debt']
            startup.profit_pfy=StartupForm1.cleaned_data['profit_pfy']
            startup.profit_total=StartupForm1.cleaned_data['profit_total']
            startup.save()
            return redirect('redirectt')
    else:
        #print("gonein")
        StartupForm1=StartupForm()


        #print("Inside if 2")
        '''
        Startup.objects.create(
            owner=request.user,
            name=request.POST.get('name'),
            site=request.POST.get('site'),
            email=request.POST.get('email'),
            problem=request.POST.get('problem'),
            bio=request.POST.get('bio'),
            solution=request.POST.get('solution'),
            edge=request.POST.get('edge'),
            RModel=request.POST.get('RModel'),
            use_of_funds=request.POST.get('use_of_funds'),
            equity=request.POST.get('equity'),
            investment=request.POST.get('investment'),
            valuation=request.POST.get('valuation'),
            pfy=request.POST.get('pfy'),
            revenue_pfy=request.POST.get('revenue_pfy'),
            revenue_total=request.POST.get('revenue_total'),
            team=request.POST.get('team'),
            image=request.POST.get('image'),
            teamimage=request.POST.get('teamimage'),

        )
        '''
       
         
    
    return render(request, 'core/listt.html',{'StartupForm1': StartupForm1})
    #return render(request,'core/listt.html')

"""
class listt2(TemplateView):
    template_name = "core/listt2.html"

    def get(self, *args, **kwargs):
        print("cp2")
        formset = TeammemberFormSet(queryset=Teammember.objects.all())
        return self.render_to_response({'Teammember_formset': formset})

    # Define method to handle POST request
    def post(self, *args, **kwargs):
        print("cp1")
        formset = TeammemberFormSet(data=self.request.POST)

        # Check if submitted forms are valid
        if formset.is_valid():
            formset.save()
            return redirect(reverse_lazy("Teammember_list"))

        return self.render_to_response({'Teammember_formset': formset})
"""

@login_required(login_url='login')
def info(request, pk):
    if(request.user.profile.typee=='business'):
        en=1
    else:
        en=0
    
    startup=Startup.objects.get(id=pk)
    tags = startup.tags.all()
    context={'startup':startup, 'tags':tags, 'en':en}
    return render(request, 'core/info.html', context)

@login_required(login_url='login')
def profile(request):
    q=request.user
    startups=Startup.objects.filter(owner=q)

    context={
        'user':request.user,
        'startups':startups
    }
    return render(request, 'core/profile.html', context)

@login_required(login_url='login')
def logoutuser(request):
    logout(request)
    return redirect('landing')

@login_required(login_url='login')
def redirectt(request):
    return render(request, 'core/redirectt.html')

@login_required(login_url='login')
def delete(request, pk):
    startup = Startup.objects.get(id=pk)
    if request.method == 'POST':
        startup.delete()
        return redirect('profile')
    return render(request, 'core/delete.html')

#The below view will be ready in the future allowing owners to update the details of startup.
'''
def update(request, pk):
    startup=Startup.objects.get(id=pk)
    print(startup)
    StartupForm1=SignUpForm(instance=startup)
    print(StartupForm1)
   

    if request.method =='POST':
        StartupForm1=SignUpForm(request.POST, request.FILES,instance=startup)
        if StartupForm1.is_valid():
            startup= Startup()
            startup.owner=request.user
            startup.name=StartupForm1.cleaned_data['name']
            startup.site=StartupForm1.cleaned_data['site']
            startup.email=StartupForm1.cleaned_data['email']
            startup.problem=StartupForm1.cleaned_data['problem']
            startup.bio=StartupForm1.cleaned_data['bio']
            startup.solution=StartupForm1.cleaned_data['solution']
            startup.edge=StartupForm1.cleaned_data['edge']
            startup.RModel=StartupForm1.cleaned_data['RModel']
            startup.use_of_funds=StartupForm1.cleaned_data['use_of_funds']
            startup.equity=StartupForm1.cleaned_data['equity']
            startup.investment=StartupForm1.cleaned_data['investment']
            startup.valuation=StartupForm1.cleaned_data['valuation']
            startup.pfy=StartupForm1.cleaned_data['pfy']
            startup.revenue_pfy=StartupForm1.cleaned_data['revenue_pfy']
            startup.revenue_total=StartupForm1.cleaned_data['revenue_total']
            startup.team=StartupForm1.cleaned_data['team']
            startup.image=StartupForm1.cleaned_data['image']
            startup.teamimage=StartupForm1.cleaned_data['teamimage']
            startup.net_margin=StartupForm1.cleaned_data['net_margin']
            startup.gross_margin=StartupForm1.cleaned_data['gross_margin']
            startup.short_term_debt=StartupForm1.cleaned_data['short_term_debt']
            startup.profit_pfy=StartupForm1.cleaned_data['profit_pfy']
            startup.profit_total=StartupForm1.cleaned_data['profit_total']
            startup.save()
            Take.objects.filter(id=pk).update(
                roll=request.user,
                name=request.POST.get('name'),
                description=request.POST.get('description'),
                auth=request.POST.get('auth'),
                contact=em,
                mob=mn,
                course=request.POST.get('course'),
                cname=request.user.profile.cname,
            )
       
            return redirect('profile')                 
    context={'StartupForm1': StartupForm1, 'startup':startup,}
    return render(request, 'core/listt.html', context)
'''