from django.shortcuts import render,HttpResponse,redirect
#from django.views.generic import View
from bewellapp.models import post

# Create your views here.
def home(request):
    return redirect('/webpage')

def welcome(request):
    return HttpResponse("Welcome to Dajano from Home")

def itvedant(request):
    return HttpResponse("Chennai ITV")

def add(request):
    a=10
    b=50
    c=a+b
    return HttpResponse(c)

def combine(request,data):
    return HttpResponse ("Good Morning"+data)

def mul(request,x,y):
    return HttpResponse(x*y)

#Class based View
#class New(View):
    #def display(self,request):
        #return HttpResponse("Msg From Class")

def index(request):
    return render(request,'index.html')
def ent(request):
    return render(request,'ent.html')
def ortho(request):
    return render(request,'ortho.html')
def cardio(request):
    return render(request,'cardio.html')
def dentist(request):
    return render(request,'dentist.html')
def emergency(request):
    return render(request,'emergency.html')


def tem(request):
    c='''
    <html>
    <head>
    <title>example</title>
    </head>
    <body>
    <h1>Welcome</h1>
    </body>
    </html>
    '''
    return HttpResponse(c)

def firstpage(request):
    return HttpResponse("First Page")

def view_html(request):
    d={}
    d['name']='Itvedant'
    return render(request,'index.html',d)

def datadtl(request):
    data={'name':'ITvedant','location':'Chennai','Batch':'Django'}
    #data=['charu','mathi','B.sc']
    return render(request,'index.html',data)

def loop(request):
    d={}
    d['a']=[100,200,300,400,500]
    return render(request,'loop.html',d)

def abe(request):
    return render(request,'about.html')
def index(request):
    return render(request,'index.html')

def po(request):
    return render(request,'post.html')

def contact(request):
    return render(request,'contact.html')

#def cpost(request):
    #return render(request,'create_post.html')

def create_post(request):
    if request.method=="POST":
       
        #print("In post Section")
        a=request.POST['pname']
        b=request.POST['pphoneno']
        f=request.POST['pdate']
        g=request.POST['ptime']
        c=request.POST['location']
        d=request.POST['gender']
        e=request.POST['det']
        
        p=post.objects.create(name=a,phoneno=b, date=f, time=g, location=c,gender=d,message=e)
        p.save

        return redirect('/appform')

        #print("Title: ",title)
        #print("Samll Des: ",small)
        #print("Detail: ",detail)
        #print("Category: ",category)
        #print("Status: ",act)

    else:
        print("In get Section")

    return render(request,'create_post.html')
#def table(request):
    #d={}
    #d['x']={ for i in range(1,11)}
    #return render(request,'table.html')

#def test(request):
    #data={'name':'Charumathi','RollNo':8001, 'contact':8939815838, 'email':'charumurugan19@gmail.com'}
    #data=['charu','mathi','B.sc']
    #return render(request,'about.html',data)

def func(request):
    #d={}
    #d['x']=100
    #d['y']=200
    rec=post.objects.all()
    #print(rec)
    content={}
    content['data']=rec
    return render(request,'udash.html',content)

def delete(request,rid):
    #return HttpResponse("Id is to be deleted: "+rid)
    p=post.objects.get(id=rid)
    p.delete()
    return redirect("/udash",p)

def edit(request,rid):
   if request.method=="POST":
       
        #print("In post Section")
        ea=request.POST['pname']
        eb=request.POST['pphoneno']
        ec=request.POST['location']
        ed=request.POST['gender']
        ee=request.POST['det']
    #return HttpResponse(" Id is to be Edit: "+rid)
        p=post.objects.filter(id=rid)
        p.update(name=ea,phoneno=eb, location=ec,gender=ed,message=ee)
        return redirect('/udash')
   else:
       p=post.objects.filter(id=rid)
       con={}
       con['data']=p
       return render(request,'edit.html',con)

def appform(request):
   #d={}
    #d['x']=100
    #d['y']=200
    rec=post.objects.all()
    #print(rec)
    content={}
    content['data']=rec
    return render(request,'appoinform.html',content)