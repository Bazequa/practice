from django.shortcuts import render,HttpResponseRedirect
from .models import *
from .forms import *
from django.db.models import Avg,Min,Max,Sum,Count
from django.db.models import Q
from datetime import date,time
# Create your views here.
def student(request):
    student_info=Student.objects.all()
    
    if request.method=="POST":
        form=StudentForm(request.POST)
        if form.is_valid():
            name=form.cleaned_data["name"]
            roll=form.cleaned_data["roll"]
            city=form.cleaned_data["city"]
            marks=form.cleaned_data["marks"]
            passdate=form.cleaned_data["passdate"]
            student=Student.objects.create(name=name,roll=roll,city=city,marks=marks,passdate=passdate)
            student.save()
        else:
            return HttpResponseRedirect('/student')
    else:
        form=StudentForm()
    return render(request,'student.html',{"form":form,"student":student_info})
def teacher(request):
    teacher_info=Teacher.objects.all()
    
    if request.method=="POST":
        form=TeacherForm(request.POST)
        if form.is_valid():
            name=form.cleaned_data["name"]
            empnum=form.cleaned_data["empnum"]
            city=form.cleaned_data["city"]
            salary=form.cleaned_data["salary"]
            join_date=form.cleaned_data["join_date"]
            teacher=Teacher.objects.create(name=name,empnum=empnum,city=city,salary=salary,join_date=join_date)
            teacher.save()
    else:
        form=TeacherForm()
        HttpResponseRedirect("/teacher")
    return render(request,'teacher.html',{"form":form,"teacher":teacher_info})

def orm(request):
    student_info=Student.objects.all()
    teacher_info=Teacher.objects.all()
    s_average=student_info.aggregate(Avg("marks"))
    s_max=student_info.aggregate(Max("marks"))
    s_min=student_info.aggregate(Min('marks'))
    s_sum=student_info.aggregate(Sum('marks'))
    s_count=student_info.aggregate(Count('marks'))
    t_max=teacher_info.aggregate(Max('salary'))
    t_min=teacher_info.aggregate(Min('salary'))
    t_average=teacher_info.aggregate(Avg('salary'))
    t_count=teacher_info.aggregate(Count('salary'))
    t_sum=teacher_info.aggregate(Sum('salary'))
    context={"s_max":s_max,"s_min":s_min,"s_average":s_average,"s_count":s_count,"s_sum":s_sum,"t_max":t_max,"t_min":t_min,"t_average":t_average,"t_count":t_count,"t_sum":t_sum}
    return render(request,'orm.html',context)

def orm1(request):
    '''student information'''
    # student_info=Student.objects.all()
    
    # student_info=Student.objects.filter(roll=1)
    
    # student_info=Student.objects.exclude(name="Bazequa Fatima")
    
    # student_info=Student.objects.order_by('passdate')
    
    # student_info=Student.objects.order_by('-marks')
    
    # student_info=Student.objects.order_by('?')
    
    # student_info=Student.objects.order_by('name')
    
    # student_info=Student.objects.order_by("id")[1:4]
    
    # student_info=Student.objects.values()
    
    student_info=Student.objects.values('name','city')
    
    # student_info=Student.objects.values_list()
    # print(student_info)
    
    # student_info=Student.objects.values_list('id','name')
    print(student_info)
    
    # student_info=Student.objects.values_list('id','name',named=True)
    # print(student_info)
    
    # student_info=Student.objects.using('default')
    
    # student_info=Student.objects.dates('passdate','month')
    # print(student_info)
    '''teacher information'''
    teacher_info=Teacher.objects.all()
    
    '''merging  teacher and student'''
    q1=Student.objects.values_list('id','name',named=True)
    q2=Teacher.objects.values_list('id','name',named=True)
    # data=q1.union(q2)
    # data=q1.union(q2,all=True)
    # data=q1.intersection(q2)
    data=q2.difference(q1)
    '''and or operator information'''
    # student_data=Student.objects.filter(id=2)&Student.objects.filter(roll=3)
    # student_data=Student.objects.filter(Q(id=5),Q(roll=1))
    # student_data=Student.objects.filter(Q(id=3)&Q(roll=1))
    # student_data=Student.objects.filter(Q(id=3)|Q(roll=1))
    student_data = Student.objects.filter(~Q(id=6))
    
    print(student_data)
    
    return render(request,"orm1.html",{"student":student_info,"teacher":teacher_info,"data":data,"student_data":student_data})

def orm2(request):
    # student_data=Student.objects.get(pk=3)
    # student_data=Student.objects.first()
    # student_data=Student.objects.last()
    # student_data=Student.objects.order_by('name').last()
    # student_data=Student.objects.earliest('passdate')
    # student_data=Student.objects.latest('passdate')
    # student_data=Student.objects.filter(Q(name="Bazequa Fatima"))
    # student_data=Student.objects.get(pk=3)
    
    # student_data=Student.objects.all()
    # print(student_data.exists())
    # one_data = Student.objects.get(pk=1)
    # print(student_data.filter(pk=one_data.pk).exists())
    
    # student_data=Student.objects.create(name="Mounika",roll=6,city="Pune",marks=78,passdate="2009-11-20")
    # student_data=Student.objects.get_or_create(name="bhagvaan",roll=8,city="Pune",marks=78,passdate="2010-11-20")
    
    # student_data,created=Student.objects.create(name="bhagvaan",roll=8,city="Pune",marks=78,passdate="2010-11-20")
    # print(created)
    
    # student_data,created=Student.objects.get_or_create(name="vadeppa",roll=7,city="Pune",marks=78,passdate="2010-11-20")
    # print(created)
    
    # student_data=Student.objects.filter(id=1).update(name="Fatima",city="Warangal")
    
    # student_data=Student.objects.filter(name="Fatima").update(marks=70,city="Hyderabad")
    
    # student_data,created=Student.objects.update_or_create(name="vadeppa1",roll=7,city="Pune",marks=78,passdate="2010-11-20",defaults={"name":"meduri"})
    # print(created)
    
    
    # objs = [
    # Student(name='Atif', roll=116, city='Dhanbad', marks=70, passdate='2020-5-4'),
    # Student(name='Sahil', roll=117, city='Bokaro', marks=50, passdate='2020-5-6'),
    # Student(name='Kumar', roll=118, city='Dhanbad', marks=30, passdate='2020-5-9'),
    # ]
    # student_data=Student.objects.bulk_create(objs)
    
    # all_student=Student.objects.all()
    # for i in all_student:
    #     i.city="Banglore"
    # student_data=Student.objects.bulk_update(all_student,['city'])
    
    # student_data=Student.objects.in_bulk([1,2])
    # print(student_data)
    
    # student_data=Student.objects.in_bulk([])
    # print(student_data)
    
    student_data=Student.objects.all()
    print(student_data.count())
    
    # student_data=Student.objects.get(pk=11).delete()
    # print(student_data)
    return render(request,"orm2.html",{"student_data":student_data})

def orm3(request):
    # student_data=Student.objects.all()
    # student_data=Student.objects.filter(name__exact="Fatima")
    # student_data=Student.objects.filter(name__iexact="sravani cheripally")
    # student_data=Student.objects.filter(name__contains="u")
    # student_data=Student.objects.filter(name__icontains="u")
    # student_data=Student.objects.filter(id__in=[1,4,3])
    # student_data=Student.objects.filter(marks__in=[70,99,78])       
    # student_data=Student.objects.filter(marks__gt=70)   
    # student_data=Student.objects.filter(marks__lt=70)   
    # student_data=Student.objects.filter(marks__gte=70) 
    # student_data=Student.objects.filter(marks__lte=70)  
    # student_data=Student.objects.filter(marks__gt=70)      
    # student_data=Student.objects.filter(name__startswith='U')
    # student_data=Student.objects.filter(name__endswith='a')      
    # student_data=Student.objects.filter(name__iendswith='A')      
    # student_data=Student.objects.filter(passdate__range=('2020-11-7','2020-11-23'))
    
    '''date time field in models'''
    # student_data=Student.objects.filter(passdate__date=date(2020,11,7))
    # student_data=Student.objects.filter(passdate__date__gt=date(2020,11,7))
    
    '''date field in models'''
    # student_data=Student.objects.filter(passdate__year=2020)
    # student_data=Student.objects.filter(passdate__year__gte=2018)
    # student_data=Student.objects.filter(passdate__month__gte=11)
    # student_data=Student.objects.filter(passdate__year__lte=2018)
    # student_data=Student.objects.filter(passdate__day=7)
    # student_data=Student.objects.filter(passdate__day__gt=7)
    # student_data = Student.objects.filter(passdate__week=14)
    # student_data = Student.objects.filter(passdate__week__gt=14)
    # student_data = Student.objects.filter(passdate__week_day=5)
    # student_data = Student.objects.filter(passdate__week_day__gt=5)
    # student_data = Student.objects.filter(passdate__quarter=2)
    
    '''date time field'''
    # student_data = Student.objects.filter(admdatetime__time__gt=time(21,17))
    # student_data = Student.objects.filter(admdatetime__hour__gt=5)
    # student_data = Student.objects.filter(admdatetime__minute__gt=20)
    # student_data = Student.objects.filter(admdatetime__second__gt=20)
    # student_data = Student.objects.filter(roll__isnull=False)
    
    # student_data=Student.objects.all()[:5]
    # student_data=Student.objects.all()[5:10]
    student_data=Student.objects.all()[::2]
    return render(request,"orm3.html",{"student_data":student_data})