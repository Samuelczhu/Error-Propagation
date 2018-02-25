from kivy.app import App
from kivy.uix.screenmanager import Screen,ScreenManager
from kivy.lang import Builder
import math


alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

mathFunction3 = ['sin','cos','tan','csc','sec','cot','log']
mathFunction6 = ['arcsin','arccos','arctan','math.e']

emptylist = [' ',' ',' ',' ',' ',' ',' ',' ',' ',' ']

def sin(x):
    return math.sin(x)
def cos(x):
    return math.cos(x)
def tan(x):
    return math.tan(x)
def csc(x):
    return 1/math.sin(x)
def sec(x):
    return 1/math.cos(x)
def cot(x):
    return 1/math.tan(x)
def arcsin(x):
    return math.asin(x)
def arccos(x):
    return math.acos(x)
def arctan(x):
    return math.atan(x)
def log10(x):
    return math.log10(x)
def ln(x):
    return math.log(x,math.e)
def log(x,b):
    return math.log(x,b)
def sqrt(x):
    return math.sqrt(x)

# important functions
def sub_in(string,length,var,stringValue):
    string = list(string)+emptylist
    i = 0
    while i<len(string):
        if ''.join(string[i:i + 3]) in mathFunction3:
            i += 3
        elif ''.join(string[i:i + 6]) in mathFunction6:
            i += 6
        elif ''.join(string[i:i + 5]) == 'log10':
            i += 5
        elif ''.join(string[i:i + 2]) == 'ln':
            i += 2
        elif ''.join(string[i:i + 4]) == 'sqrt':
            i += 4
        elif ''.join(string[i:i + 7]) == 'math.pi':
            i += 7
        elif ''.join(string[i:i + 3]) == 'abs':
            i += 3
        elif ''.join(string[i:i+2]) == '--':
            string[i] = '+'
            string[i+1] = ''
            i += 2
        elif ''.join(string[i:i+2]) == '+-':
            string[i] = '-'
            string[i+1] = ''
            i += 2
        elif ''.join(string[i:i+length]) == var:
            string[i] = stringValue
            for j in range(len(string[i+1:i+length])):
                string[i+1+j] = ''
            i += length
        i += 1
    string = ''.join(string).replace(' ','')
    return string


def evaluate(string):
    string = list(string)
    for i in range(len(string)):
        if string[i] == '^':
            string[i] = '**'
    string = ''.join(string).replace(' ','')
    return eval(string)


class ScreenManagement(ScreenManager):
    pass


class MainScreen(Screen):
    counted = []
    equation = ''

    def start(self):
        equation = self.ids.equation.text.replace(' ','')
        self.Equation = equation + '          '
        numVar = -1
        i = 0
        counted = []
        while i<len(self.Equation)-10:
            if self.Equation[i:i+3] in mathFunction3:
                i += 3
            elif self.Equation[i:i+6] in mathFunction6:
                i += 6
            elif self.Equation[i:i+5]=='log10':
                i += 5
            elif self.Equation[i:i+2]=='ln':
                i += 2
            elif self.Equation[i:i+4]=='sqrt':
                i += 4
            elif self.Equation[i:i+7]=='math.pi':
                i += 7
            elif self.Equation[i:i+3] == 'abs':
                i += 3
            elif (self.Equation[i] in alphabet) and (self.Equation[i] not in counted):
                counted += self.Equation[i]
                numVar += 1
            i += 1
        MainScreen.counted = counted
        MainScreen.equation =equation

        if '=' not in list(equation):
            self.parent.current = 'Error'
        elif numVar==1:
            self.parent.ids.one.ids.dfdaLabel.text = 'Derivative d'+counted[0]+'/d'+ counted[1] + ' = '
            self.parent.ids.one.ids.aLabel.text = counted[1] + ' = '
            self.parent.ids.one.ids.EaLabel.text = 'Error '+ counted[1] + ' = '
            self.parent.current = 'OneVar'
        elif numVar==2:
            self.parent.ids.two1.ids.dfdaLabel.text = 'Derivative d'+counted[0]+'/d'+ counted[1] + ' = '
            self.parent.ids.two1.ids.dfdbLabel.text = 'Derivative d'+counted[0]+'/d'+ counted[2] + ' = '
            self.parent.ids.two1.ids.aLabel.text = counted[1] + ' = '
            self.parent.ids.two1.ids.bLabel.text = counted[2] + ' = '
            self.parent.ids.two2.ids.EaLabel.text = 'Error '+ counted[1] + ' = '
            self.parent.ids.two2.ids.EbLabel.text = 'Error '+ counted[2] + ' = '
            self.parent.current = 'TwoVar1'
        elif numVar==3:
            self.parent.ids.three1.ids.dfdaLabel.text = 'Derivative d'+counted[0]+'/d'+counted[1]+ ' = '
            self.parent.ids.three1.ids.dfdbLabel.text = 'Derivative d'+counted[0]+'/d'+counted[2]+ ' = '
            self.parent.ids.three1.ids.dfdcLabel.text = 'Derivative d'+counted[0]+'/d'+counted[3]+ ' = '
            self.parent.ids.three1.ids.aLabel.text = counted[1] + ' = '
            self.parent.ids.three1.ids.bLabel.text = counted[2] + ' = '
            self.parent.ids.three2.ids.cLabel.text = counted[3] + ' = '
            self.parent.ids.three2.ids.EaLabel.text = 'Error '+ counted[1] + ' = '
            self.parent.ids.three2.ids.EbLabel.text = 'Error '+ counted[2] + ' = '
            self.parent.ids.three2.ids.EcLabel.text = 'Error '+ counted[3] + ' = '
            self.parent.current = 'ThreeVar1'
        elif numVar==4:
            self.parent.ids.four1.ids.dfdaLabel.text = 'Derivative d'+counted[0]+'/d'+counted[1]+ ' = '
            self.parent.ids.four1.ids.dfdbLabel.text = 'Derivative d'+counted[0]+'/d'+counted[2]+ ' = '
            self.parent.ids.four1.ids.dfdcLabel.text = 'Derivative d'+counted[0]+'/d'+counted[3]+ ' = '
            self.parent.ids.four1.ids.dfddLabel.text = 'Derivative d'+counted[0]+'/d'+counted[4]+ ' = '
            self.parent.ids.four1.ids.aLabel.text = counted[1] + ' = '
            self.parent.ids.four2.ids.bLabel.text = counted[2] + ' = '
            self.parent.ids.four2.ids.cLabel.text = counted[3] + ' = '
            self.parent.ids.four2.ids.dLabel.text = counted[4] + ' = '
            self.parent.ids.four2.ids.EaLabel.text = 'Error '+ counted[1] + ' = '
            self.parent.ids.four3.ids.EbLabel.text = 'Error '+ counted[2] + ' = '
            self.parent.ids.four3.ids.EcLabel.text = 'Error '+ counted[3] + ' = '
            self.parent.ids.four3.ids.EdLabel.text = 'Error ' + counted[4] + ' = '
            self.parent.current = 'FourVar1'
        elif numVar==5:
            self.parent.ids.five1.ids.dfdaLabel.text = 'Derivative d'+counted[0]+'/d'+counted[1]+ ' = '
            self.parent.ids.five1.ids.dfdbLabel.text = 'Derivative d'+counted[0]+'/d'+counted[2]+ ' = '
            self.parent.ids.five1.ids.dfdcLabel.text = 'Derivative d'+counted[0]+'/d'+counted[3]+ ' = '
            self.parent.ids.five1.ids.dfddLabel.text = 'Derivative d'+counted[0]+'/d'+counted[4]+ ' = '
            self.parent.ids.five1.ids.dfdeLabel.text = 'Derivative d' + counted[0] + '/d' + counted[5] + ' = '
            self.parent.ids.five2.ids.aLabel.text = counted[1] + ' = '
            self.parent.ids.five2.ids.bLabel.text = counted[2] + ' = '
            self.parent.ids.five2.ids.cLabel.text = counted[3] + ' = '
            self.parent.ids.five2.ids.dLabel.text = counted[4] + ' = '
            self.parent.ids.five2.ids.eLabel.text = counted[5] + ' = '
            self.parent.ids.five3.ids.EaLabel.text = 'Error '+ counted[1] + ' = '
            self.parent.ids.five3.ids.EbLabel.text = 'Error '+ counted[2] + ' = '
            self.parent.ids.five3.ids.EcLabel.text = 'Error '+ counted[3] + ' = '
            self.parent.ids.five3.ids.EdLabel.text = 'Error ' + counted[4] + ' = '
            self.parent.ids.five3.ids.EeLabel.text = 'Error ' + counted[5] + ' = '
            self.parent.current = 'FiveVar1'
        else:
            self.parent.current = 'Error'


class InfoScreen(Screen):
    pass


class ErrorScreen(Screen):
    pass


class OneVar(Screen):
    def clear(self):
        self.ids.dfda.text = ''
        self.ids.a.text = ''
        self.ids.Ea.text = ''

    def calculate(self):
        try:
            formula = 'sqrt(d'+MainScreen.counted[0]+'/d'+MainScreen.counted[1]+'^2*E'+MainScreen.counted[1]+'^2)'
            equation = MainScreen.equation
            dfda = self.ids.dfda.text
            a = self.ids.a.text
            Ea = self.ids.Ea.text
            dfda = sub_in(dfda,1,MainScreen.counted[1],str(a))
            subin = sub_in(formula,5,'d'+MainScreen.counted[0]+'/d'+MainScreen.counted[1],'('+str(dfda)+')')
            subin = sub_in(subin,2,'E'+MainScreen.counted[1],'('+str(Ea)+')')

            self.parent.ids.ans1.ids.formula.text = formula[5:-1]
            self.parent.ids.ans1.ids.sub.ids.myLabel.text = subin
            self.parent.ids.ans1.ids.ansfLabel.text = MainScreen.counted[0] + ' = '
            self.parent.ids.ans1.ids.ansf.text = str(evaluate(sub_in(equation[2:],1,MainScreen.counted[1],str(a))))
            self.parent.ids.ans1.ids.ansEfLabel.text = 'E'+MainScreen.counted[0] + ' = '
            self.parent.ids.ans1.ids.ansEf.text = str(evaluate(subin))
            self.parent.current = 'Answer1'
        except:
            self.parent.current = 'Error'
class Answer1(Screen):
    def clear(self):
        self.ids.sub.ids.myLabel.text = ''
        self.ids.ansf.text = ''
        self.ids.ansEf.text = ''


class TwoVar1(Screen):
    def clear(self):
        self.ids.dfda.text = ''
        self.ids.dfdb.text = ''
        self.ids.a.text = ''
        self.ids.b.text = ''
class TwoVar2(Screen):
    def clear(self):
        self.ids.Ea.text = ''
        self.ids.Eb.text = ''

    def calculate(self):
        try:
            formula = 'sqrt(d'+MainScreen.counted[0]+'/d'+MainScreen.counted[1]+'^2*E'+MainScreen.counted[1]+'^2+d'+MainScreen.counted[0]+'/d'+MainScreen.counted[2]+'^2*E'+MainScreen.counted[2]+'^2)'
            equation = MainScreen.equation
            dfda = self.parent.ids.two1.ids.dfda.text
            dfdb = self.parent.ids.two1.ids.dfdb.text
            a = self.parent.ids.two1.ids.a.text
            b = self.parent.ids.two1.ids.b.text
            Ea = self.ids.Ea.text
            Eb = self.ids.Eb.text
            dfda = sub_in(dfda,1,MainScreen.counted[1],str(a))
            dfda = sub_in(dfda,1,MainScreen.counted[2],str(b))
            dfdb = sub_in(dfdb,1,MainScreen.counted[1],str(a))
            dfdb = sub_in(dfdb,1,MainScreen.counted[2],str(b))
            subin = sub_in(formula,5,'d'+MainScreen.counted[0]+'/d'+MainScreen.counted[1],'('+str(dfda)+')')
            subin = sub_in(subin,5,'d'+MainScreen.counted[0]+'/d'+MainScreen.counted[2],'('+str(dfdb)+')')
            subin = sub_in(subin,2,'E'+MainScreen.counted[1],'('+str(Ea)+')')
            subin = sub_in(subin,2,'E'+MainScreen.counted[2],'('+str(Eb)+')')

            self.parent.ids.ans2.ids.formula.text = formula[5:-1]
            self.parent.ids.ans2.ids.sub.ids.myLabel.text = subin
            self.parent.ids.ans2.ids.ansfLabel.text = MainScreen.counted[0] + ' = '
            ansf = sub_in(equation[2:],1,MainScreen.counted[1],str(a))
            ansf = sub_in(ansf,1,MainScreen.counted[2],str(b))
            self.parent.ids.ans2.ids.ansf.text = str(evaluate(ansf))
            self.parent.ids.ans2.ids.ansEfLabel.text = 'E'+MainScreen.counted[0] + ' = '
            self.parent.ids.ans2.ids.ansEf.text = str(evaluate(subin))
            self.parent.current = 'Answer2'
        except:
            self.parent.current = 'Error'
class Answer2(Screen):
    def clear(self):
        self.ids.sub.ids.myLabel.text = ''
        self.ids.ansf.text = ''
        self.ids.ansEf.text = ''


class ThreeVar1(Screen):
    def clear(self):
        self.ids.dfda.text = ''
        self.ids.dfdb.text = ''
        self.ids.dfdc.text = ''
        self.ids.a.text = ''
        self.ids.b.text = ''
class ThreeVar2(Screen):
    def clear(self):
        self.ids.c.text = ''
        self.ids.Ea.text = ''
        self.ids.Eb.text = ''
        self.ids.Ec.text = ''
        
    def calculate(self):
        try:
            formula = 'sqrt(d'+MainScreen.counted[0]+'/d'+MainScreen.counted[1]+'^2*E'+MainScreen.counted[1]+'^2+d'+MainScreen.counted[0]+'/d'+MainScreen.counted[2]+'^2*E'+MainScreen.counted[2]+'^2+d'+MainScreen.counted[0]+'/d'+MainScreen.counted[3]+'^2*E'+MainScreen.counted[3]+'^2)'
            equation = MainScreen.equation
            dfda = self.parent.ids.three1.ids.dfda.text
            dfdb = self.parent.ids.three1.ids.dfdb.text
            dfdc = self.parent.ids.three1.ids.dfdc.text
            a = self.parent.ids.three1.ids.a.text
            b = self.parent.ids.three1.ids.b.text
            c = self.ids.c.text
            Ea = self.ids.Ea.text
            Eb = self.ids.Eb.text
            Ec = self.ids.Ec.text
            dfda = sub_in(dfda,1,MainScreen.counted[1],str(a))
            dfda = sub_in(dfda,1,MainScreen.counted[2],str(b))
            dfda = sub_in(dfda,1,MainScreen.counted[3],str(c))
            dfdb = sub_in(dfdb,1,MainScreen.counted[1],str(a))
            dfdb = sub_in(dfdb,1,MainScreen.counted[2],str(b))
            dfdb = sub_in(dfdb,1,MainScreen.counted[3],str(c))
            dfdc = sub_in(dfdc,1,MainScreen.counted[1],str(a))
            dfdc = sub_in(dfdc,1,MainScreen.counted[2],str(b))
            dfdc = sub_in(dfdc,1,MainScreen.counted[3],str(c))
            subin = sub_in(formula,5,'d'+MainScreen.counted[0]+'/d'+MainScreen.counted[1],'('+str(dfda)+')')
            subin = sub_in(subin,5,'d'+MainScreen.counted[0]+'/d'+MainScreen.counted[2],'('+str(dfdb)+')')
            subin = sub_in(subin,5,'d'+MainScreen.counted[0]+'/d'+MainScreen.counted[3],'('+str(dfdc)+')')
            subin = sub_in(subin,2,'E'+MainScreen.counted[1],'('+str(Ea)+')')
            subin = sub_in(subin,2,'E'+MainScreen.counted[2],'('+str(Eb)+')')
            subin = sub_in(subin,2,'E'+MainScreen.counted[3],'('+str(Ec)+')')

            self.parent.ids.ans3.ids.formula.text = formula[5:-1]
            self.parent.ids.ans3.ids.sub.ids.myLabel.text = subin
            self.parent.ids.ans3.ids.ansfLabel.text = MainScreen.counted[0] + ' = '
            ansf = sub_in(equation[2:],1,MainScreen.counted[1],str(a))
            ansf = sub_in(ansf,1,MainScreen.counted[2],str(b))
            ansf = sub_in(ansf,1,MainScreen.counted[3],str(c))
            self.parent.ids.ans3.ids.ansf.text = str(evaluate(ansf))
            self.parent.ids.ans3.ids.ansEfLabel.text = 'E'+MainScreen.counted[0] + ' = '
            self.parent.ids.ans3.ids.ansEf.text = str(evaluate(subin))
            self.parent.current = 'Answer3'
        except:
            self.parent.current = 'Error'
class Answer3(Screen):
    def clear(self):
        self.ids.sub.ids.myLabel.text = ''
        self.ids.ansf.text = ''
        self.ids.ansEf.text = ''


class FourVar1(Screen):
    def clear(self):
        self.ids.dfda.text = ''
        self.ids.dfdb.text = ''
        self.ids.dfdc.text = ''
        self.ids.dfdd.text = ''
        self.ids.a.text = ''
class FourVar2(Screen):
    def clear(self):
        self.ids.b.text = ''
        self.ids.c.text = ''
        self.ids.d.text = ''
        self.ids.Ea.text = ''
class FourVar3(Screen):
    def clear(self):
        self.ids.Eb.text = ''
        self.ids.Ec.text = ''
        self.ids.Ed.text = ''
    def calculate(self):
        try:
            formula = 'sqrt(d'+MainScreen.counted[0]+'/d'+MainScreen.counted[1]+'^2*E'+MainScreen.counted[1]+'^2+d'+MainScreen.counted[0]+'/d'+MainScreen.counted[2]+'^2*E'+MainScreen.counted[2]+'^2+d'+MainScreen.counted[0]+'/d'+MainScreen.counted[3]+'^2*E'+MainScreen.counted[3]+'^2+d'+MainScreen.counted[0]+'/d'+MainScreen.counted[4]+'^2*E'+MainScreen.counted[4]+'^2)'
            equation = MainScreen.equation
            dfda = self.parent.ids.four1.ids.dfda.text
            dfdb = self.parent.ids.four1.ids.dfdb.text
            dfdc = self.parent.ids.four1.ids.dfdc.text
            dfdd = self.parent.ids.four1.ids.dfdd.text
            a = self.parent.ids.four1.ids.a.text
            b = self.parent.ids.four2.ids.b.text
            c = self.parent.ids.four2.ids.c.text
            d = self.parent.ids.four2.ids.d.text
            Ea = self.parent.ids.four2.ids.Ea.text
            Eb = self.ids.Eb.text
            Ec = self.ids.Ec.text
            Ed = self.ids.Ed.text
            dfda = sub_in(dfda,1,MainScreen.counted[1],str(a))
            dfda = sub_in(dfda,1,MainScreen.counted[2],str(b))
            dfda = sub_in(dfda,1,MainScreen.counted[3],str(c))
            dfda = sub_in(dfda, 1, MainScreen.counted[4], str(d))
            dfdb = sub_in(dfdb,1,MainScreen.counted[1],str(a))
            dfdb = sub_in(dfdb,1,MainScreen.counted[2],str(b))
            dfdb = sub_in(dfdb,1,MainScreen.counted[3],str(c))
            dfdb = sub_in(dfdb, 1, MainScreen.counted[4], str(d))
            dfdc = sub_in(dfdc,1,MainScreen.counted[1],str(a))
            dfdc = sub_in(dfdc,1,MainScreen.counted[2],str(b))
            dfdc = sub_in(dfdc,1,MainScreen.counted[3],str(c))
            dfdc = sub_in(dfdc, 1, MainScreen.counted[4], str(d))
            dfdd = sub_in(dfdd,1,MainScreen.counted[1],str(a))
            dfdd = sub_in(dfdd,1,MainScreen.counted[2],str(b))
            dfdd = sub_in(dfdd,1,MainScreen.counted[3],str(c))
            dfdd = sub_in(dfdd, 1, MainScreen.counted[4], str(d))
            subin = sub_in(formula,5,'d'+MainScreen.counted[0]+'/d'+MainScreen.counted[1],'('+str(dfda)+')')
            subin = sub_in(subin,5,'d'+MainScreen.counted[0]+'/d'+MainScreen.counted[2],'('+str(dfdb)+')')
            subin = sub_in(subin,5,'d'+MainScreen.counted[0]+'/d'+MainScreen.counted[3],'('+str(dfdc)+')')
            subin = sub_in(subin, 5, 'd' + MainScreen.counted[0] + '/d' + MainScreen.counted[4], '(' + str(dfdd) + ')')
            subin = sub_in(subin,2,'E'+MainScreen.counted[1],'('+str(Ea)+')')
            subin = sub_in(subin,2,'E'+MainScreen.counted[2],'('+str(Eb)+')')
            subin = sub_in(subin,2,'E'+MainScreen.counted[3],'('+str(Ec)+')')
            subin = sub_in(subin, 2, 'E' + MainScreen.counted[4], '(' + str(Ed) + ')')

            self.parent.ids.ans4.ids.formula.text = formula[5:-1]
            self.parent.ids.ans4.ids.sub.ids.myLabel.text = subin
            self.parent.ids.ans4.ids.ansfLabel.text = MainScreen.counted[0] + ' = '
            ansf = sub_in(equation[2:],1,MainScreen.counted[1],str(a))
            ansf = sub_in(ansf,1,MainScreen.counted[2],str(b))
            ansf = sub_in(ansf,1,MainScreen.counted[3],str(c))
            ansf = sub_in(ansf, 1, MainScreen.counted[4], str(d))
            self.parent.ids.ans4.ids.ansf.text = str(evaluate(ansf))
            self.parent.ids.ans4.ids.ansEfLabel.text = 'E'+MainScreen.counted[0] + ' = '
            self.parent.ids.ans4.ids.ansEf.text = str(evaluate(subin))
            self.parent.current = 'Answer4'
        except:
            self.parent.current = 'Error'
class Answer4(Screen):
    def clear(self):
        self.ids.sub.ids.myLabel.text = ''
        self.ids.ansf.text = ''
        self.ids.ansEf.text = ''


class FiveVar1(Screen):
    def clear(self):
        self.ids.dfda.text = ''
        self.ids.dfdb.text = ''
        self.ids.dfdc.text = ''
        self.ids.dfdd.text = ''
        self.ids.dfde.text = ''
class FiveVar2(Screen):
    def clear(self):
        self.ids.a.text = ''
        self.ids.b.text = ''
        self.ids.c.text = ''
        self.ids.d.text = ''
        self.ids.e.text = ''
class FiveVar3(Screen):
    def clear(self):
        self.ids.Ea.text = ''
        self.ids.Eb.text = ''
        self.ids.Ec.text = ''
        self.ids.Ed.text = ''
        self.ids.Ee.text = ''
    def calculate(self):
        try:
            formula = 'sqrt(d'+MainScreen.counted[0]+'/d'+MainScreen.counted[1]+'^2*E'+MainScreen.counted[1]+'^2+d'+MainScreen.counted[0]+'/d'+MainScreen.counted[2]+'^2*E'+MainScreen.counted[2]+'^2+d'+MainScreen.counted[0]+'/d'+MainScreen.counted[3]+'^2*E'+MainScreen.counted[3]+'^2+d'+MainScreen.counted[0]+'/d'+MainScreen.counted[4]+'^2*E'+MainScreen.counted[4]+'^2+d'+MainScreen.counted[0]+'/d'+MainScreen.counted[5]+'^2*E'+MainScreen.counted[5]+'^2)'
            equation = MainScreen.equation
            dfda = self.parent.ids.five1.ids.dfda.text
            dfdb = self.parent.ids.five1.ids.dfdb.text
            dfdc = self.parent.ids.five1.ids.dfdc.text
            dfdd = self.parent.ids.five1.ids.dfdd.text
            dfde = self.parent.ids.five1.ids.dfde.text
            a = self.parent.ids.five2.ids.a.text
            b = self.parent.ids.five2.ids.b.text
            c = self.parent.ids.five2.ids.c.text
            d = self.parent.ids.five2.ids.d.text
            e = self.parent.ids.five2.ids.e.text
            Ea = self.ids.Ea.text
            Eb = self.ids.Eb.text
            Ec = self.ids.Ec.text
            Ed = self.ids.Ed.text
            Ee = self.ids.Ee.text
            dfda = sub_in(dfda,1,MainScreen.counted[1],str(a))
            dfda = sub_in(dfda,1,MainScreen.counted[2],str(b))
            dfda = sub_in(dfda,1,MainScreen.counted[3],str(c))
            dfda = sub_in(dfda, 1, MainScreen.counted[4], str(d))
            dfda = sub_in(dfda, 1, MainScreen.counted[5], str(e))
            dfdb = sub_in(dfdb,1,MainScreen.counted[1],str(a))
            dfdb = sub_in(dfdb,1,MainScreen.counted[2],str(b))
            dfdb = sub_in(dfdb,1,MainScreen.counted[3],str(c))
            dfdb = sub_in(dfdb, 1, MainScreen.counted[4], str(d))
            dfdb = sub_in(dfdb, 1, MainScreen.counted[5], str(e))
            dfdc = sub_in(dfdc,1,MainScreen.counted[1],str(a))
            dfdc = sub_in(dfdc,1,MainScreen.counted[2],str(b))
            dfdc = sub_in(dfdc,1,MainScreen.counted[3],str(c))
            dfdc = sub_in(dfdc, 1, MainScreen.counted[4], str(d))
            dfdc = sub_in(dfdc, 1, MainScreen.counted[5], str(e))
            dfdd = sub_in(dfdd,1,MainScreen.counted[1],str(a))
            dfdd = sub_in(dfdd,1,MainScreen.counted[2],str(b))
            dfdd = sub_in(dfdd,1,MainScreen.counted[3],str(c))
            dfdd = sub_in(dfdd, 1, MainScreen.counted[4], str(d))
            dfdd = sub_in(dfdd, 1, MainScreen.counted[5], str(e))
            dfde = sub_in(dfde,1,MainScreen.counted[1],str(a))
            dfde = sub_in(dfde,1,MainScreen.counted[2],str(b))
            dfde = sub_in(dfde,1,MainScreen.counted[3],str(c))
            dfde = sub_in(dfde, 1, MainScreen.counted[4], str(d))
            dfde = sub_in(dfde, 1, MainScreen.counted[5], str(e))
            subin = sub_in(formula,5,'d'+MainScreen.counted[0]+'/d'+MainScreen.counted[1],'('+str(dfda)+')')
            subin = sub_in(subin,5,'d'+MainScreen.counted[0]+'/d'+MainScreen.counted[2],'('+str(dfdb)+')')
            subin = sub_in(subin,5,'d'+MainScreen.counted[0]+'/d'+MainScreen.counted[3],'('+str(dfdc)+')')
            subin = sub_in(subin, 5, 'd' + MainScreen.counted[0] + '/d' + MainScreen.counted[4], '(' + str(dfdd) + ')')
            subin = sub_in(subin, 5, 'd' + MainScreen.counted[0] + '/d' + MainScreen.counted[5], '(' + str(dfde) + ')')
            subin = sub_in(subin,2,'E'+MainScreen.counted[1],'('+str(Ea)+')')
            subin = sub_in(subin,2,'E'+MainScreen.counted[2],'('+str(Eb)+')')
            subin = sub_in(subin,2,'E'+MainScreen.counted[3],'('+str(Ec)+')')
            subin = sub_in(subin, 2, 'E' + MainScreen.counted[4], '(' + str(Ed) + ')')
            subin = sub_in(subin, 2, 'E' + MainScreen.counted[5], '(' + str(Ee) + ')')

            self.parent.ids.ans5.ids.formula.text = formula[5:-1]
            self.parent.ids.ans5.ids.sub.ids.myLabel.text = subin
            self.parent.ids.ans5.ids.ansfLabel.text = MainScreen.counted[0] + ' = '
            ansf = sub_in(equation[2:],1,MainScreen.counted[1],str(a))
            ansf = sub_in(ansf,1,MainScreen.counted[2],str(b))
            ansf = sub_in(ansf,1,MainScreen.counted[3],str(c))
            ansf = sub_in(ansf, 1, MainScreen.counted[4], str(d))
            ansf = sub_in(ansf, 1, MainScreen.counted[5], str(e))
            self.parent.ids.ans5.ids.ansf.text = str(evaluate(ansf))
            self.parent.ids.ans5.ids.ansEfLabel.text = 'E'+MainScreen.counted[0] + ' = '
            self.parent.ids.ans5.ids.ansEf.text = str(evaluate(subin))
            self.parent.current = 'Answer5'
        except:
            self.parent.current = 'Error'
class Answer5(Screen):
    def clear(self):
        self.ids.sub.ids.myLabel.text = ''
        self.ids.ansf.text = ''
        self.ids.ansEf.text = ''


presentation = Builder.load_file('errorPropagation2.kv')


class errorPropagation2App(App):
    def build(self):
        return presentation


if __name__=='__main__':
    errorPropagation2App().run()
