from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen, FadeTransition
from kivy.lang import Builder
from math import *

def sec(x):
    return 1/cos(x)
def csc(x):
    return 1/sin(x)
def cot(x):
    return 1/tan(x)

def df_subin(df,var,symbol):
    df = list(df)
    var = str(var)
    for i in range(len(df)):
        if df[i] == symbol:
            df[i] = var
        if df[i - 1] + df[i] == '**':
            df[i] = '^'
            df[i - 1] = ''
        if df[i] == 's' and df[i-1] == 'o' and df[i-2] == var:
            df[i-2] = 'c'
        if df[i] == 'n' and df[i-1] == var and df[i-2] == 't':
            df[i-1] = 'a'
            if df[i-3] == var:
                df[i-3] = 'a'
        if df[i] == 'n' and df[i-1] == 'i' and df[i-2] == 's' and df[i-3] == var:
            df[i-3] = 'a'
        if df[i] == 's' and df[i-1] == 'o' and (df[i-2] == 'c' or df[i-2] == var) and df[i-3] == var:
            df[i-3] = 'a'
        if (df[i] == 'c' or df[i] == var) and (df[i-1] == 'e' or df[i-1] == var) and df[i-2] == 's':
            df[i] = 'c'
            df[i-1] = 'e'
        if df[i] == var and df[i-1] == 's' and df[i-2] == var:
            df[i] = 'c'
            df[i-2] = 'c'
        if df[i] == 't' and df[i-1] == 'o' and df[i-2] == var:
            df[i-2] = 'c'
    return ''.join(df)


class ScreenManagement(ScreenManager):
    pass

class MenuScreen(Screen):
    pass

class Information(Screen):
    pass

class OneVar(Screen):
    answer = ''
    sub = ''
    def clear(self):
         self.ids.dfda.text = ''
         self.ids.a.text = ''
         self.ids.Ea.text = ''

    def calculate(self):
        try:
            dfda = self.ids.dfda.text
            a = eval(self.ids.a.text)
            Ea = eval(self.ids.Ea.text)
            ans = round(eval(dfda)*Ea,4)
            dfda = df_subin(dfda,round(a,2),'a')
            OneVar.sub = 'sqrt(('+dfda+')^2*('+str(round(Ea,2))+')^2)'
            OneVar.answer = 'Error f = '+ str(abs(ans))
        except:
            OneVar.answer = 'Please enter valid input'
            OneVar.sub = 'Error'

class Answer1(Screen):
    def show(self):
        self.ids.sub.text = OneVar.sub
        self.ids.ans.text = OneVar.answer
    def clear(self):
        self.ids.sub.text = ''
        self.ids.ans.text = ''


class TwoVar1(Screen):
    dfda = ''
    dfdb = ''
    a = ''
    b = ''
    def clear(self):
        self.ids.dfda.text = ''
        self.ids.dfdb.text = ''
        self.ids.a.text = ''
        self.ids.b.text = ''
    def cont(self):
        TwoVar1.dfda = self.ids.dfda.text
        TwoVar1.dfdb = self.ids.dfdb.text
        TwoVar1.a = self.ids.a.text
        TwoVar1.b = self.ids.b.text
class TwoVar2(Screen):
    answer = ''
    sub = ''
    def clear(self):
        self.ids.Ea.text = ''
        self.ids.Eb.text = ''
        self.ids.ans.text = ''
    def calculate(self):
        try:
            dfda = TwoVar1.dfda
            dfdb = TwoVar1.dfdb
            a = eval(TwoVar1.a)
            b = eval(TwoVar1.b)
            Ea = eval(self.ids.Ea.text)
            Eb = eval(self.ids.Eb.text)
            ans = round(sqrt((eval(dfda)*Ea)**2+(eval(dfdb)*Eb)**2),4)
            dfda = df_subin(dfda, round(a, 2), 'a')
            dfda = df_subin(dfda, round(b, 2), 'b')
            dfdb = df_subin(dfdb, round(a, 2),' a')
            dfdb = df_subin(dfdb, round(b, 2), 'b')
            TwoVar2.sub = 'sqrt(('+dfda+')^2*('+str(round(Ea,2))+')^2+('+dfdb+')^2*('+str(round(Eb,2))+')^2)'
            TwoVar2.answer = 'Error f = '+str(ans)
        except:
            TwoVar2.answer = 'Please enter valid input'
            TwoVar2.sub = 'Error'

class Answer2(Screen):
    def show(self):
        self.ids.sub.text = TwoVar2.sub
        self.ids.ans.text = TwoVar2.answer
    def clear(self):
        self.ids.sub.text = ''
        self.ids.ans.text = ''


class ThreeVar1(Screen):
    dfda = ''
    dfdb = ''
    dfdc = ''
    a = ''
    b = ''
    def clear(self):
        self.ids.dfda.text = ''
        self.ids.dfdb.text = ''
        self.ids.dfdc.text = ''
        self.ids.a.text = ''
        self.ids.b.text = ''
    def cont(self):
        ThreeVar1.dfda = self.ids.dfda.text
        ThreeVar1.dfdb = self.ids.dfdb.text
        ThreeVar1.dfdc = self.ids.dfdc.text
        ThreeVar1.a = self.ids.a.text
        ThreeVar1.b = self.ids.b.text
class ThreeVar2(Screen):
    answer = ''
    sub = ''
    def clear(self):
        self.ids.c.text = ''
        self.ids.Ea.text = ''
        self.ids.Eb.text = ''
        self.ids.Ec.text = ''
    def calculate(self):
        try:
            dfda = ThreeVar1.dfda
            dfdb = ThreeVar1.dfdb
            dfdc = ThreeVar1.dfdc
            a = eval(ThreeVar1.a)
            b = eval(ThreeVar1.b)
            c = eval(self.ids.c.text)
            Ea = eval(self.ids.Ea.text)
            Eb = eval(self.ids.Eb.text)
            Ec = eval(self.ids.Ec.text)
            ans = round(sqrt((eval(dfda) * Ea)**2 + (eval(dfdb) * Eb)**2 + (eval(dfdc) * Ec)**2), 4)
            dfda = df_subin(dfda, round(a, 2), 'a')
            dfda = df_subin(dfda, round(b, 2), 'b')
            dfda = df_subin(dfda, round(c, 2), 'c')
            dfdb = df_subin(dfdb, round(a, 2), 'a')
            dfdb = df_subin(dfdb, round(b, 2), 'b')
            dfdb = df_subin(dfdb, round(c, 2), 'c')
            dfdc = df_subin(dfdc, round(a, 2), 'a')
            dfdc = df_subin(dfdc, round(b, 2), 'b')
            dfdc = df_subin(dfdc, round(c, 2), 'c')
            ThreeVar2.sub = 'sqrt((' + dfda + ')^2*(' + str(round(Ea, 2)) + ')^2+(' + dfdb + ')^2*(' + str(
                round(Eb, 2)) + ')^2+('+dfdc+')^2*('+str(round(Ec,2))+')^2)'
            ThreeVar2.answer = 'Error f = ' + str(ans)
        except:
            ThreeVar2.answer = 'Please enter valid input'
            ThreeVar2.sub = 'Error'

class Answer3(Screen):
    def show(self):
        self.ids.sub.text = ThreeVar2.sub
        self.ids.ans.text = ThreeVar2.answer
    def clear(self):
        self.ids.sub.text = ''
        self.ids.ans.text = ''


class FourVar1(Screen):
    dfda = ''
    dfdb = ''
    dfdc = ''
    dfdd = ''
    a = ''
    def clear(self):
        self.ids.dfda.text = ''
        self.ids.dfdb.text = ''
        self.ids.dfdc.text = ''
        self.ids.dfdd.text = ''
        self.ids.a.text = ''
    def cont(self):
        FourVar1.dfda = self.ids.dfda.text
        FourVar1.dfdb = self.ids.dfdb.text
        FourVar1.dfdc = self.ids.dfdc.text
        FourVar1.dfdd = self.ids.dfdd.text
        FourVar1.a = self.ids.a.text
class FourVar2(Screen):
    b = ''
    c = ''
    d = ''
    Ea = ''
    def clear(self):
        self.ids.b.text = ''
        self.ids.c.text = ''
        self.ids.d.text = ''
        self.ids.Ea.text = ''
    def cont(self):
        FourVar2.b = self.ids.b.text
        FourVar2.c = self.ids.c.text
        FourVar2.d = self.ids.d.text
        FourVar2.Ea = self.ids.Ea.text
class FourVar3(Screen):
    answer = ''
    sub = ''
    def clear(self):
        self.ids.Eb.text = ''
        self.ids.Ec.text = ''
        self.ids.Ed.text = ''
    def calculate(self):
        try:
            dfda = FourVar1.dfda
            dfdb = FourVar1.dfdb
            dfdc = FourVar1.dfdc
            dfdd = FourVar1.dfdd
            a = eval(FourVar1.a)
            b = eval(FourVar2.b)
            c = eval(FourVar2.c)
            d = eval(FourVar2.d)
            Ea = eval(FourVar2.Ea)
            Eb = eval(self.ids.Eb.text)
            Ec = eval(self.ids.Ec.text)
            Ed = eval(self.ids.Ed.text)
            ans = round(sqrt((eval(dfda) * Ea)**2 + (eval(dfdb) * Eb)**2 + (eval(dfdc) * Ec)**2 + (eval(dfdd) * Ed)**2), 4)
            dfda = df_subin(dfda, round(a, 2), 'a')
            dfda = df_subin(dfda, round(b, 2), 'b')
            dfda = df_subin(dfda, round(c, 2), 'c')
            dfda = df_subin(dfda, round(d, 2), 'd')
            dfdb = df_subin(dfdb, round(a, 2), 'a')
            dfdb = df_subin(dfdb, round(b, 2), 'b')
            dfdb = df_subin(dfdb, round(c, 2), 'c')
            dfdb = df_subin(dfdb, round(d, 2), 'd')
            dfdc = df_subin(dfdc, round(a, 2), 'a')
            dfdc = df_subin(dfdc, round(b, 2), 'b')
            dfdc = df_subin(dfdc, round(c, 2), 'c')
            dfdc = df_subin(dfdc, round(d, 2), 'd')
            dfdd = df_subin(dfdd, round(a, 2), 'a')
            dfdd = df_subin(dfdd, round(b, 2), 'b')
            dfdd = df_subin(dfdd, round(c, 2), 'c')
            dfdd = df_subin(dfdd, round(d, 2), 'd')
            FourVar3.sub = 'sqrt((' + dfda + ')^2*(' + str(round(Ea, 2)) + ')^2+(' + dfdb + ')^2*(' + str(
                round(Eb, 2)) + ')^2+\n('+dfdc+')^2*('+str(round(Ec,2))+')^2+('+dfdd+')^2*('+str(round(Ed,2)) + ')^2)'
            FourVar3.answer = 'Error f = ' + str(ans)
        except:
            FourVar3.answer = 'Please enter valid input'
            FourVar3.sub = 'Error'

class Answer4(Screen):
    def show(self):
        self.ids.sub.text = FourVar3.sub
        self.ids.ans.text = FourVar3.answer
    def clear(self):
        self.ids.sub.text = ''
        self.ids.ans.text = ''


class FiveVar1(Screen):
    dfda = ''
    dfdb = ''
    dfdc = ''
    dfdd = ''
    dfde = ''
    def clear(self):
        self.ids.dfda.text = ''
        self.ids.dfdb.text = ''
        self.ids.dfdc.text = ''
        self.ids.dfdd.text = ''
        self.ids.dfde.text = ''
    def cont(self):
        FiveVar1.dfda = self.ids.dfda.text
        FiveVar1.dfdb = self.ids.dfdb.text
        FiveVar1.dfdc = self.ids.dfdc.text
        FiveVar1.dfdd = self.ids.dfdd.text
        FiveVar1.dfde = self.ids.dfde.text
class FiveVar2(Screen):
    a = ''
    b = ''
    c = ''
    d = ''
    e = ''
    def clear(self):
        self.ids.a.text = ''
        self.ids.b.text = ''
        self.ids.c.text = ''
        self.ids.d.text = ''
        self.ids.e.text = ''
    def cont(self):
        FiveVar2.a = self.ids.a.text
        FiveVar2.b = self.ids.b.text
        FiveVar2.c = self.ids.c.text
        FiveVar2.d = self.ids.d.text
        FiveVar2.e = self.ids.e.text
class FiveVar3(Screen):
    answer = ''
    sub = ''
    def clear(self):
        self.ids.Ea.text = ''
        self.ids.Eb.text = ''
        self.ids.Ec.text = ''
        self.ids.Ed.text = ''
        self.ids.Ee.text = ''
    def calculate(self):
        try:
            dfda = FiveVar1.dfda
            dfdb = FiveVar1.dfdb
            dfdc = FiveVar1.dfdc
            dfdd = FiveVar1.dfdd
            dfde = FiveVar1.dfde
            a = eval(FiveVar2.a)
            b = eval(FiveVar2.b)
            c = eval(FiveVar2.c)
            d = eval(FiveVar2.d)
            e = eval(FiveVar2.e)
            Ea = eval(self.ids.Ea.text)
            Eb = eval(self.ids.Eb.text)
            Ec = eval(self.ids.Ec.text)
            Ed = eval(self.ids.Ed.text)
            Ee = eval(self.ids.Ee.text)
            ans = round(sqrt((eval(dfda) * Ea)**2 + (eval(dfdb) * Eb)**2 + (eval(dfdc) * Ec)**2 + (eval(dfdd) * Ed)**2 + (eval(dfde)* Ee)**2), 4)
            dfda = df_subin(dfda, round(a, 2), 'a')
            dfda = df_subin(dfda, round(b, 2), 'b')
            dfda = df_subin(dfda, round(c, 2), 'c')
            dfda = df_subin(dfda, round(d, 2), 'd')
            dfda = df_subin(dfda, round(e, 2), 'e')
            dfdb = df_subin(dfdb, round(a, 2), 'a')
            dfdb = df_subin(dfdb, round(b, 2), 'b')
            dfdb = df_subin(dfdb, round(c, 2), 'c')
            dfdb = df_subin(dfdb, round(d, 2), 'd')
            dfdb = df_subin(dfdb, round(e, 2), 'e')
            dfdc = df_subin(dfdc, round(a, 2), 'a')
            dfdc = df_subin(dfdc, round(b, 2), 'b')
            dfdc = df_subin(dfdc, round(c, 2), 'c')
            dfdc = df_subin(dfdc, round(d, 2), 'd')
            dfdc = df_subin(dfdc, round(e, 2), 'e')
            dfdd = df_subin(dfdd, round(a, 2), 'a')
            dfdd = df_subin(dfdd, round(b, 2), 'b')
            dfdd = df_subin(dfdd, round(c, 2), 'c')
            dfdd = df_subin(dfdd, round(d, 2), 'd')
            dfdd = df_subin(dfdd, round(e, 2), 'e')
            dfde = df_subin(dfde, round(a, 2), 'a')
            dfde = df_subin(dfde, round(b, 2), 'b')
            dfde = df_subin(dfde, round(c, 2), 'c')
            dfde = df_subin(dfde, round(d, 2), 'd')
            dfde = df_subin(dfde, round(e, 2), 'e')
            FiveVar3.sub = '          sqrt((' + dfda + ')^2*(' + str(round(Ea, 2)) + ')^2+(' + dfdb + ')^2*(' + str(
                round(Eb, 2)) + ')^2+\n('+dfdc+')^2*('+str(round(Ec,2))+')^2+('+dfdd+')^2*('+str(round(Ed,2)) + ')^2+('+dfde+')^2*('+str(round(Ee,2)) + ')^2)'
            FiveVar3.answer = 'Error f = ' + str(ans)
        except:
            FiveVar3.answer = 'Please enter valid input'
            FiveVar3.sub = 'Error'

class Answer5(Screen):
    def show(self):
        self.ids.sub.text = FiveVar3.sub
        self.ids.ans.text = FiveVar3.answer
    def clear(self):
        self.ids.sub.text = ''
        self.ids.ans.text = ''


presentation = Builder.load_file("errorPropagation.kv")

class errorPropagationApp(App):
    def build(self):
        return presentation

if __name__=='__main__':
    errorPropagationApp().run()
