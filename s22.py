class convert_temp:
    def __init__(self,t):
        self.t=t
    def fc(self):
        f=self.t
        c=(f-32)*5/9
        return c
    def cf(self):
        c=self.t
        f=(c*9/5)+32
        return f
    def fk(self):
        f=self.t
        k=(f+459.67)*5/9
        return k
    def kf(self):
        k=self.k
        f=(k*9/5)-456.67
        return f
    def kc(self):
        k=self.t
        c=k-273.15
        return c
    def ck(self):
        c=self.t
        k=c+273.15
        return k
    def RaC(self):
        ra=self.t
        c=(ra-32-459.67)/1.8
        return c
    def RaF(self):
        ra=self.t
        f=ra-459.67
        return f
    def RaK(self):
        ra=self.t
        k=ra/1.8
        return k
    def CRa(self):
        c=self.t
        ra=c*1.8+32+459.67
        return ra
    def FRa(self):
        f=self.t
        ra=f+459.67
        return ra
    def KRa(self):
        k=self.t
        ra=k*1.8
        return ra
        

class convert_len:
    def __init__(self,l):
        self.l=l
    def m_cm(self):
        m=self.l
        cm=m*100
        return cm
    def m_mm(self):
        m=self.l
        mm=m*1000
        return mm
    def cm_m(self):
        cm=self.l
        m=cm/100
        return m
    def cm_mm(self):
        cm=self.l
        mm=cm*10
        return mm
    def mm_cm(self):
        mm=self.l
        cm=mm/10
        return cm
    def mm_m(self):
        mm=self.l
        m=mm/1000
        return m
    def inch_m(self):
        inch=self.l
        m=inch*0.0254
        return m
    def inch_cm(self):
        inch=self.l
        cm=inch*2.54
        return cm
    def inch_mm(self):
        inch=self.l
        mm=inch*25.4
        return mm
    def m_inch(self):
        m=self.l
        inch=m*39.37
        return inch
    def cm_inch(self):
        cm=self.l
        inch=cm*0.3937
        return inch
    def mm_inch(self):
        mm=self.l
        inch=mm*0.03937
        return inch

class convert_pressure:
    def __init__(self,p):
        self.p=p
    def pa_mmhg(self):
        pa=self.p
        mmhg=pa*0.0075
        return mmhg
    def pa_bar(self):
        pa=self.p
        bar=pa*0.001
        return bar
    def mmhg_pa(self):
        mmhg=self.p
        pa=mmhg*133.63
        return pa
    def mmhg_bar(self):
        mmhg=self.p
        bar=mmhg*0.001333
        return bar
    def bar_pa(self):
        bar=self.p
        pa=bar*100000
        return pa
    def bar_mmhg(self):
        bar=self.p
        mmhg=bar*750.062
        return mmhg


    

def main():    
 k=int(input("convert_temp=1 or convert_len=2 or convert_pressure=3 : "))
 if k==1:
    t=float(input("temprature = "))
    s=int(input("fc:1 , cf:2 , fk:3 , kf:4 , kc:5 , ck:6 , RaC:7 , RaF:8 , RaK:9 , CRa:10 , FRa:11 , KRa:12 : "))
    convert=convert_temp(t)
    if s==1:
        print(convert.fc())
    elif s==2:
        print(convert.cf())
    elif s==3:
        print(convert.fk())
    elif s==4:
        print(convert.kf())
    elif s==5:
        print(convert.kc())
    elif s==6:
        print(convert.ck())
    elif s==7:
        print(convert.RaC())
    elif s==8:
        print(convert.RaF())
    elif s==9:
        print(convert.RaK())
    elif s==10:
        print(convert.CRa())
    elif s==11:
        print(convert.FRa())
    elif s==12:
        print(convert.KRa())    

 elif k==2:
    l=float(input("length = "))
    s=int(input("m_cm:1 , m_mm:2 , cm_m:3 , cm_mm:4 , mm_cm:5 , mm_m:6 , inch_m:7 , inch_cm:8 , inch_mm:9 , m_inch:10 , cm_inch:11 , mm_inch:12 : "))
    convert=convert_len(l)
    if s==1:
        print(convert.m_cm())
    elif s==2:
        print(convert.m_mm())
    elif s==3:
        print(convert.cm_m())
    elif s==4:
        print(convert.cm_mm())
    elif s==5:
        print(convert.mm_cm())
    elif s==6:
        print(convert.mm_m())
    elif s==7:
        print(convert.inch_m())
    elif s==8:
        print(convert.inch_cm())
    elif s==9:
        print(convert.inch_mm())
    elif s==10:
        print(convert.m_inch())
    elif s==11:
        print(convert.cm_inch())
    elif s==12:
        print(convert.mm_inch())    

 elif k==3:
    p=float(input("pressure = "))
    s=int(input(" pa_mmhg:1 , pa_bar:2 , mmhg_pa:3 , mmhg_bar:4 , bar_pa:5 , bar_mmhg:6 : "))
    convert=convert_pressure(p)
    if s==1:
        print(convert.pa_mmhg())
    elif s==2:
        print(convert.pa_bar())
    elif s==3:
        print(convert.mmhg_pa())
    elif s==4:
        print(convert.mmhg_bar())
    elif s==5:
        print(convert.bar_pa())
    elif s==6:
        print(convert.bar_mmhg())    
    
        
 restart=input("Do you want to convert again? (y/n)")
 if restart=="y":
     main()
     
main()     


























        
















    
