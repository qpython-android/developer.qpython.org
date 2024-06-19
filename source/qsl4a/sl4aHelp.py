from WinGui.ListCmd import *
from WinGui.LongHtml import *
from androidhelper import *
droid = Android()
droid.cipherInit(b's'*16)
droid.documentTreeShowOpen()
droid.batteryStartMonitoring()
droid.batteryStopMonitoring()
droid.startSensingTimed(5,100)
droid.stopSensing()
droid.checkBluetoothState()
p1='/storage/emulated/0/Download/QSL4A/'
p2=p1+'qsl4a/%s.html'
p3=p1+'qsl4a.html'
open(p3,'w').write('<head><title>QSL4A Functions</title></head><body>\n')
Functions = ['R.id','R.layout','R.style','provider.Settings']
for i in dir(droid):
    if i[0]!='_':
        Functions.append(i)
Functions.sort()
o='</font><br>按 <font color=#000000><big>确认</big></font> 调用 百度翻译url 成 简体中文，只提示一次</font>'
def Text2Html(s,u=None):
    t=['<font color=#007f00>']
    r=t.append
    firstLine=True
    for i in s:
        j=ord(i)
        if j==10:
            if firstLine:
                if len(t)==1:
                    continue
                r('</font>')
                firstLine=False
            r('<br><br>')
        elif j==32:
            r('&nbsp;')
        elif j<256 and not (i.isalpha() or i.isdigit()):
            r('&#');r(str(j));r(";")
        else:
            r(i)
    t=''.join(t)
    if u:
        t=t.replace(u,"<b>"+u+"</b>")
    return t
def sl4aHelp(Title):
    global o,Functions
    for a in Functions:
        #c=ListCmd('%s:%s个'%(Title,len(Functions)),Functions)
        #if None==c:
            #break
        #a=Functions[c]
        if a.split('.',1)[0] in ('R','provider','Intent'):
            try:
                b=open(eval(f'droid.{a}.__file__')).read()
            except:
                b=eval(f'droid.{a}.__doc__')
        else:
            b=eval(f'droid.{a}.__doc__')
        #Functions=Functions[c:]+Functions[:c]
        h1=Text2Html(a)+o
        h2=Text2Html(b,a)
        #a=LongHtml(h1,h2)
        open(p2%a,'w').write(f'<head><title>{a}</title></head><body><p>{h2}</p><a href="../qsl4a.html">&#60;back&#62;</a></body>')
        open(p3,'a').write(f'<a href="qsl4a/{a}.html">{a}</a><br>\n')
        if o:
            o=''
        if a==None and len(a)>0:
            a=bytes(b,'utf-8')
            b=[];d=-1
            for c in a:
                if 65<=c<=90 and ( 97<=d<=122 or 48<=d<=57 ):
                    b.append('%20')
                d=c
                c=hex(c)
                if len(c)==4:
                    b.append('%'+c[2:])
                else:
                    b.append('%0'+c[2:])
            b=''.join(b)
            droid.viewHtml('https://fanyi.baidu.com/?tpltype=sigma#en/zh/'+b)
open(p3,'a').write('</body>')
#by 乘着船 Bilibili
