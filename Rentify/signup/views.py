import pwd
from django.shortcuts import render
import mysql.connector as sql
fn=''
ln=''
g=''
em=''
pwd=''

# Create your views here.
def signaction(request):
    global fn, ln, s, em, pwd
    if request.method==="POST":
        m=sql.connect(host='localhost', user='root', passwd='Nahid@Mysql_1!', database='rentify')
        cursor=m.cursor()
        d=request.POST
        for key,value in d.items():
            if key=="first_name":
                fn=value
            if key=="last_name":
                ln=value
            if key=="gender":
                g=value
            if key=="email":
                em=value
            if key=="password":
                pwd=value

        c = "inert into users Values ('{}','{}','{}','{}','{}')".format(fn,ln,g,em,pwd)
        cursor.execute(c)
        m.commit()

    return render(request, 'signup.html')
