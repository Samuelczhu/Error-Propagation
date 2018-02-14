from __future__ import division
from __future__ import absolute_import
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
    var = unicode(var)
    for i in xrange(len(df)):
        if df[i] == symbol:
            df[i] = var
        if df[i - 1] + df[i] == u'**':
            df[i] = u'^'
            df[i - 1] = u''
        if df[i] == u's' and df[i-1] == u'o' and df[i-2] == var:
            df[i-2] = u'c'
        if df[i] == u'n' and df[i-1] == var and df[i-2] == u't':
            df[i-1] = u'a'
            if df[i-3] == var:
                df[i-3] = u'a'
        if df[i] == u'n' and df[i-1] == u'i' and df[i-2] == u's' and df[i-3] == var:
            df[i-3] = u'a'
        if df[i] == u's' and df[i-1] == u'o' and (df[i-2] == u'c' or df[i-2] == var) and df[i-3] == var:
            df[i-3] = u'a'
        if (df[i] == u'c' or df[i] == var) and (df[i-1] == u'e' or df[i-1] == var) and df[i-2] == u's':
            df[i] = u'c'
            df[i-1] = u'e'
        if df[i] == var and df[i-1] == u's' and df[i-2] == var:
            df[i] = u'c'
            df[i-2] = u'c'
        if df[i] == u't' and df[i-1] == u'o' and df[i-2] == var:
            df[i-2] = u'c'
    return u''.join(df)


class ScreenManagement(ScreenManager):
    pass

class MenuScreen(Screen):
    pass

class Information(Screen):
    pass

class OneVar(Screen):
    answer = u''
    sub = u''
    def clear(self):
         self.ids.dfda.text = u''
         self.ids.a.text = u''
         self.ids.Ea.text = u''

    def calculate(self):
        try:
            dfda = self.ids.dfda.text
            a = eval(self.ids.a.text)
            Ea = eval(self.ids.Ea.text)
            ans = round(eval(dfda)*Ea,4)
            dfda = df_subin(dfda,round(a,2),u'a')
            OneVar.sub = u'sqrt(('+dfda+u')^2*('+unicode(round(Ea,2))+u')^2)'
            OneVar.answer = u'Error f = '+ unicode(abs(ans))
        except:
            OneVar.answer = u'Please enter valid input'
            OneVar.sub = u'Error'

class Answer1(Screen):
    def show(self):
        self.ids.sub.text = OneVar.sub
        self.ids.ans.text = OneVar.answer
    def clear(self):
        self.ids.sub.text = u''
        self.ids.ans.text = u''


class TwoVar1(Screen):
    dfda = u''
    dfdb = u''
    a = u''
    b = u''
    def clear(self):
        self.ids.dfda.text = u''
        self.ids.dfdb.text = u''
        self.ids.a.text = u''
        self.ids.b.text = u''
    def cont(self):
        TwoVar1.dfda = self.ids.dfda.text
        TwoVar1.dfdb = self.ids.dfdb.text
        TwoVar1.a = self.ids.a.text
        TwoVar1.b = self.ids.b.text
class TwoVar2(Screen):
    answer = u''
    sub = u''
    def clear(self):
        self.ids.Ea.text = u''
        self.ids.Eb.text = u''
        self.ids.ans.text = u''
    def calculate(self):
        try:
            dfda = TwoVar1.dfda
            dfdb = TwoVar1.dfdb
            a = eval(TwoVar1.a)
            b = eval(TwoVar1.b)
            Ea = eval(self.ids.Ea.text)
            Eb = eval(self.ids.Eb.text)
            ans = round(sqrt((eval(dfda)*Ea)**2+(eval(dfdb)*Eb)**2),4)
            dfda = df_subin(dfda, round(a, 2), u'a')
            dfda = df_subin(dfda, round(b, 2), u'b')
            dfdb = df_subin(dfdb, round(a, 2),u' a')
            dfdb = df_subin(dfdb, round(b, 2), u'b')
            TwoVar2.sub = u'sqrt(('+dfda+u')^2*('+unicode(round(Ea,2))+u')^2+('+dfdb+u')^2*('+unicode(round(Eb,2))+u')^2)'
            TwoVar2.answer = u'Error f = '+unicode(ans)
        except:
            TwoVar2.answer = u'Please enter valid input'
            TwoVar2.sub = u'Error'

class Answer2(Screen):
    def show(self):
        self.ids.sub.text = TwoVar2.sub
        self.ids.ans.text = TwoVar2.answer
    def clear(self):
        self.ids.sub.text = u''
        self.ids.ans.text = u''


class ThreeVar1(Screen):
    dfda = u''
    dfdb = u''
    dfdc = u''
    a = u''
    b = u''
    def clear(self):
        self.ids.dfda.text = u''
        self.ids.dfdb.text = u''
        self.ids.dfdc.text = u''
        self.ids.a.text = u''
        self.ids.b.text = u''
    def cont(self):
        ThreeVar1.dfda = self.ids.dfda.text
        ThreeVar1.dfdb = self.ids.dfdb.text
        ThreeVar1.dfdc = self.ids.dfdc.text
        ThreeVar1.a = self.ids.a.text
        ThreeVar1.b = self.ids.b.text
class ThreeVar2(Screen):
    answer = u''
    sub = u''
    def clear(self):
        self.ids.c.text = u''
        self.ids.Ea.text = u''
        self.ids.Eb.text = u''
        self.ids.Ec.text = u''
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
            dfda = df_subin(dfda, round(a, 2), u'a')
            dfda = df_subin(dfda, round(b, 2), u'b')
            dfda = df_subin(dfda, round(c, 2), u'c')
            dfdb = df_subin(dfdb, round(a, 2), u'a')
            dfdb = df_subin(dfdb, round(b, 2), u'b')
            dfdb = df_subin(dfdb, round(c, 2), u'c')
            dfdc = df_subin(dfdc, round(a, 2), u'a')
            dfdc = df_subin(dfdc, round(b, 2), u'b')
            dfdc = df_subin(dfdc, round(c, 2), u'c')
            ThreeVar2.sub = u'sqrt((' + dfda + u')^2*(' + unicode(round(Ea, 2)) + u')^2+(' + dfdb + u')^2*(' + unicode(
                round(Eb, 2)) + u')^2+('+dfdc+u')^2*('+unicode(round(Ec,2))+u')^2)'
            ThreeVar2.answer = u'Error f = ' + unicode(ans)
        except:
            ThreeVar2.answer = u'Please enter valid input'
            ThreeVar2.sub = u'Error'

class Answer3(Screen):
    def show(self):
        self.ids.sub.text = ThreeVar2.sub
        self.ids.ans.text = ThreeVar2.answer
    def clear(self):
        self.ids.sub.text = u''
        self.ids.ans.text = u''


class FourVar1(Screen):
    dfda = u''
    dfdb = u''
    dfdc = u''
    dfdd = u''
    a = u''
    def clear(self):
        self.ids.dfda.text = u''
        self.ids.dfdb.text = u''
        self.ids.dfdc.text = u''
        self.ids.dfdd.text = u''
        self.ids.a.text = u''
    def cont(self):
        FourVar1.dfda = self.ids.dfda.text
        FourVar1.dfdb = self.ids.dfdb.text
        FourVar1.dfdc = self.ids.dfdc.text
        FourVar1.dfdd = self.ids.dfdd.text
        FourVar1.a = self.ids.a.text
class FourVar2(Screen):
    b = u''
    c = u''
    d = u''
    Ea = u''
    def clear(self):
        self.ids.b.text = u''
        self.ids.c.text = u''
        self.ids.d.text = u''
        self.ids.Ea.text = u''
    def cont(self):
        FourVar2.b = self.ids.b.text
        FourVar2.c = self.ids.c.text
        FourVar2.d = self.ids.d.text
        FourVar2.Ea = self.ids.Ea.text
class FourVar3(Screen):
    answer = u''
    sub = u''
    def clear(self):
        self.ids.Eb.text = u''
        self.ids.Ec.text = u''
        self.ids.Ed.text = u''
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
            dfda = df_subin(dfda, round(a, 2), u'a')
            dfda = df_subin(dfda, round(b, 2), u'b')
            dfda = df_subin(dfda, round(c, 2), u'c')
            dfda = df_subin(dfda, round(d, 2), u'd')
            dfdb = df_subin(dfdb, round(a, 2), u'a')
            dfdb = df_subin(dfdb, round(b, 2), u'b')
            dfdb = df_subin(dfdb, round(c, 2), u'c')
            dfdb = df_subin(dfdb, round(d, 2), u'd')
            dfdc = df_subin(dfdc, round(a, 2), u'a')
            dfdc = df_subin(dfdc, round(b, 2), u'b')
            dfdc = df_subin(dfdc, round(c, 2), u'c')
            dfdc = df_subin(dfdc, round(d, 2), u'd')
            dfdd = df_subin(dfdd, round(a, 2), u'a')
            dfdd = df_subin(dfdd, round(b, 2), u'b')
            dfdd = df_subin(dfdd, round(c, 2), u'c')
            dfdd = df_subin(dfdd, round(d, 2), u'd')
            FourVar3.sub = u'sqrt((' + dfda + u')^2*(' + unicode(round(Ea, 2)) + u')^2+(' + dfdb + u')^2*(' + unicode(
                round(Eb, 2)) + u')^2+\n('+dfdc+u')^2*('+unicode(round(Ec,2))+u')^2+('+dfdd+u')^2*('+unicode(round(Ed,2)) + u')^2)'
            FourVar3.answer = u'Error f = ' + unicode(ans)
        except:
            FourVar3.answer = u'Please enter valid input'
            FourVar3.sub = u'Error'

class Answer4(Screen):
    def show(self):
        self.ids.sub.text = FourVar3.sub
        self.ids.ans.text = FourVar3.answer
    def clear(self):
        self.ids.sub.text = u''
        self.ids.ans.text = u''


class FiveVar1(Screen):
    dfda = u''
    dfdb = u''
    dfdc = u''
    dfdd = u''
    dfde = u''
    def clear(self):
        self.ids.dfda.text = u''
        self.ids.dfdb.text = u''
        self.ids.dfdc.text = u''
        self.ids.dfdd.text = u''
        self.ids.dfde.text = u''
    def cont(self):
        FiveVar1.dfda = self.ids.dfda.text
        FiveVar1.dfdb = self.ids.dfdb.text
        FiveVar1.dfdc = self.ids.dfdc.text
        FiveVar1.dfdd = self.ids.dfdd.text
        FiveVar1.dfde = self.ids.dfde.text
class FiveVar2(Screen):
    a = u''
    b = u''
    c = u''
    d = u''
    e = u''
    def clear(self):
        self.ids.a.text = u''
        self.ids.b.text = u''
        self.ids.c.text = u''
        self.ids.d.text = u''
        self.ids.e.text = u''
    def cont(self):
        FiveVar2.a = self.ids.a.text
        FiveVar2.b = self.ids.b.text
        FiveVar2.c = self.ids.c.text
        FiveVar2.d = self.ids.d.text
        FiveVar2.e = self.ids.e.text
class FiveVar3(Screen):
    answer = u''
    sub = u''
    def clear(self):
        self.ids.Ea.text = u''
        self.ids.Eb.text = u''
        self.ids.Ec.text = u''
        self.ids.Ed.text = u''
        self.ids.Ee.text = u''
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
            dfda = df_subin(dfda, round(a, 2), u'a')
            dfda = df_subin(dfda, round(b, 2), u'b')
            dfda = df_subin(dfda, round(c, 2), u'c')
            dfda = df_subin(dfda, round(d, 2), u'd')
            dfda = df_subin(dfda, round(e, 2), u'e')
            dfdb = df_subin(dfdb, round(a, 2), u'a')
            dfdb = df_subin(dfdb, round(b, 2), u'b')
            dfdb = df_subin(dfdb, round(c, 2), u'c')
            dfdb = df_subin(dfdb, round(d, 2), u'd')
            dfdb = df_subin(dfdb, round(e, 2), u'e')
            dfdc = df_subin(dfdc, round(a, 2), u'a')
            dfdc = df_subin(dfdc, round(b, 2), u'b')
            dfdc = df_subin(dfdc, round(c, 2), u'c')
            dfdc = df_subin(dfdc, round(d, 2), u'd')
            dfdc = df_subin(dfdc, round(e, 2), u'e')
            dfdd = df_subin(dfdd, round(a, 2), u'a')
            dfdd = df_subin(dfdd, round(b, 2), u'b')
            dfdd = df_subin(dfdd, round(c, 2), u'c')
            dfdd = df_subin(dfdd, round(d, 2), u'd')
            dfdd = df_subin(dfdd, round(e, 2), u'e')
            dfde = df_subin(dfde, round(a, 2), u'a')
            dfde = df_subin(dfde, round(b, 2), u'b')
            dfde = df_subin(dfde, round(c, 2), u'c')
            dfde = df_subin(dfde, round(d, 2), u'd')
            dfde = df_subin(dfde, round(e, 2), u'e')
            FiveVar3.sub = u'          sqrt((' + dfda + u')^2*(' + unicode(round(Ea, 2)) + u')^2+(' + dfdb + u')^2*(' + unicode(
                round(Eb, 2)) + u')^2+\n('+dfdc+u')^2*('+unicode(round(Ec,2))+u')^2+('+dfdd+u')^2*('+unicode(round(Ed,2)) + u')^2+('+dfde+u')^2*('+unicode(round(Ee,2)) + u')^2)'
            FiveVar3.answer = u'Error f = ' + unicode(ans)
        except:
            FiveVar3.answer = u'Please enter valid input'
            FiveVar3.sub = u'Error'

class Answer5(Screen):
    def show(self):
        self.ids.sub.text = FiveVar3.sub
        self.ids.ans.text = FiveVar3.answer
    def clear(self):
        self.ids.sub.text = u''
        self.ids.ans.text = u''


presentation = Builder.load_file(u"errorPropagation.kv")

class errorPropagationApp(App):
    def build(self):
        return presentation

if __name__==u'__main__':
    errorPropagationApp().run()
