import random
def questionSet(number, right, wrong):
    if number==1:
        answer=raw_input("first kinematics equation: ")
        if answer=="vf=vi+at":
            print "correct"
            right+=1
        else:
            print "wrong"
            print "vf=vi+at"
            wrong+=1
        return [right, wrong]
    elif number==2:
        answer=raw_input("1 Coulomb/1 Joule is called a ____? ")
        if answer=="volt":
            print "correct"
            right+=1
        else:
            print "wrong"
            print "volt"
            wrong+=1
        return [right, wrong]
    elif number==3:
        answer=raw_input("the charge of an electron is: ")
        if answer=="-1.6*10^-19 C":
            print "correct"
            right+=1
        else:
            print "wrong"
            print "-1.6*10^-19 C"
            wrong+=1
        return [right, wrong]
    elif number==4:
        answer=raw_input("second kinematics equation ")
        if answer=="x=vit+1/2mv^2":
            print "correct"
            right+=1
        else:
            print "x=vit+1/2mv^2"
            print "rate law"
            wrong+=1
        return [right, wrong]
    elif number==5:
        answer=raw_input("third kinematics equations ")
        if answer=="vf^2=vi^2+2ax":
            print "correct"
            right+=1
        else:
            print "wrong"
            print "second"
            wrong+=1
        return [right, wrong]
    elif number==6:
        answer=raw_input("What is the overall order of the following reaction: k[X]?")
        if answer=="first":
            print "correct"
            right+=1
        else:
            print "wrong"
            print "first"
            wrong+=1
        return [right, wrong]
    elif number==7:
        answer=raw_input("what order is the following integrated rate law: ln[A]=-kt+ln[A0] ")
        if answer=="first":
            print "correct"
            right+=1
        else:
            print "wrong"
            print "first"
            wrong+=1
        return [right, wrong]
    elif number==8:
        answer=raw_input("what order is the following integrated rate law: [A]^-1=kt+[A0]^-1 ")
        if answer=="second":
            print "correct"
            right+=1
        else:
            print "wrong"
            print "second"
            wrong+=1
        return [right, wrong]
    elif number==9:
        answer=raw_input("what order is the following integrated rate law: [A]=-kt+[A0] ")
        if answer=="zero":
            print "correct"
            right+=1
        else:
            print "wrong"
            print "zero"
            wrong+=1
        return [right, wrong]
    elif number==10:
        answer=raw_input("what order is the following half life eqaution: t1/2=[A0]/2k ")
        if answer=="zero":
            print "correct"
            right+=1
        else:
            print "wrong"
            print "zero"
            wrong+=1
        return [right, wrong]
    elif number==11:
        answer=raw_input("what order is the following half life equation: t1/2=1/(k[A0]) ")
        if answer=="second":
            print "correct"
            right+=1
        else:
            print "wrong"
            print "second"
            wrong+=1
        return [right, wrong]
    elif number==12:
        answer=raw_input("what order is the following half life equation: t1/2=ln(2)/k or t1/2=0.693/k ")
        if answer=="first":
            print "correct"
            right+=1
        else:
            print "wrong"
            print "first"
            wrong+=1
        return [right, wrong]
    elif number==13:
        answer=raw_input("True or False: The fastest step is the rate determining step? ")
        if answer=="false":
            print "correct"
            right+=1
        else:
            print "wrong"
            wrong+=1
        return [right, wrong]
    elif number==14:
        answer=raw_input("True or False: The slowest step is the rate determining step? ")
        if answer=="true":
            print "correct"
            right+=1
        else:
            print "wrong"
            wrong+=1
        return [right, wrong]
    elif number==15:
        answer=raw_input("True or False: The coefficients of the rate determining step are the coefficients of the rate law ")
        if answer=="false":
            print "correct"
            right+=1
        else:
            print "wrong"
            wrong+=1
        return [right, wrong]
    elif number==16:
        answer=raw_input("True or False: The coefficients of the rate determining step are the exponents of the rate law ")
        if answer=="true":
            print "correct"
            right+=1
        else:
            print "wrong"
            wrong+=1
        return [right, wrong]
    elif number==17:
        answer=raw_input("True or False: H2SO4 is a strong acid ")
        if answer=="true":
            print "correct"
            right+=1
        else:
            print "wrong"
            wrong+=1
        return [right, wrong]
    elif number==18:
        answer=raw_input("True or False: HSO4 is a strong acid ")
        if answer=="false":
            print "correct"
            right+=1
        else:
            print "wrong"
            wrong+=1
        return [right, wrong]
    elif number==19:
        answer=raw_input("True or False: HBr is a weak acid ")
        if answer=="false":
            print "correct"
            right+=1
        else:
            print "wrong"
            wrong+=1
        return [right, wrong]
    elif number==20:
        answer=raw_input("True or False: HCl is a strong acid ")
        if answer=="true":
            print "correct"
            right+=1
        else:
            print "wrong"
            wrong+=1
        return [right, wrong]
    elif number==21:
        answer=raw_input("True or False: If the AP gives you a Ka, the acid must be a strong acid ")
        if answer=="false":
            print "correct"
            right+=1
        else:
            print "wrong"
            wrong+=1
        return [right, wrong]
    elif number==22:
        answer=raw_input("True or False: Strong acids dissociate completely ")
        if answer=="true":
            print "correct"
            right+=1
        else:
            print "wrong"
            wrong+=1
        return [right, wrong]
    elif number==23:
        answer=raw_input("True or False: At 25 degrees Celsius 10^14/[H+]=[OH-]")
        if answer=="true":
            print "correct"
            right+=1
        else:
            print "wrong"
            wrong+=1
        return [right, wrong]
    elif number==24:
        answer=raw_input("True or False: ph=log[H+] ")
        if answer=="false":
            print "correct"
            right+=1
        else:
            print "wrong"
            wrong+=1
        return [right, wrong]
    elif number==25:
        answer=raw_input("True or False: At 25 degrees Celsius pH+pOH=14 ")
        if answer=="true":
            print "correct"
            right+=1
        else:
            print "wrong"
            wrong+=1
        return [right, wrong]
    elif number==26:
        answer=raw_input("True or False: The Arrhenius equation (ln(k)=-(Ea/R)(1/T)+ln(A)) becomes a linear equation y=mx+b ")
        if answer=="true":
            print "correct"
            right+=1
        else:
            print "wrong"
            wrong+=1
        return [right, wrong]
    elif number==27:
        answer=raw_input("True or False: For all polyprotic Acids except H2SO4, only the first dissociation makes an important contribution ")
        if answer=="true":
            print "correct"
            right+=1
        else:
            print "wrong"
            wrong+=1
        return [right, wrong]
    elif number==28:
        answer=raw_input("True or False: Amphoteric substances can be conjugate acids or bases ")
        if answer=="true":
            print "correct"
            right+=1
        else:
            print "wrong"
            wrong+=1
        return [right, wrong]
    elif number==29:
        answer=raw_input("True or False: Salts can't have an effect on the solution's pH ")
        if answer=="false":
            print "correct"
            right+=1
        else:
            print "wrong"
            wrong+=1
        return [right, wrong]
    elif number==30:
        answer=raw_input("True or False: A salt of ions that form strong acids and bases has a large effect on the solution pH ")
        if answer=="false":
            print "correct"
            right+=1
        else:
            print "wrong"
            wrong+=1
        return [right, wrong]
    elif number==31:
        answer=raw_input("True or False: An Arrhenius base is an H+ acceptor")
        if answer=="false":
            print "correct"
            right+=1
        else:
            print "wrong"
            wrong+=1
        return [right, wrong]
    elif number==32:
        answer=raw_input("True or False: A Bronstead-Lowry acid is an H+ donor")
        if answer=="true":
            print "correct"
            right+=1
        else:
            print "wrong"
            wrong+=1
        return [right, wrong]
    elif number==33:
        answer=raw_input("True or False: A Lewis acid is an electron pair donor")
        if answer=="false":
            print "correct"
            right+=1
        else:
            print "wrong"
            wrong+=1
        return [right, wrong]
    elif number==34:
        answer=raw_input("True or False: Entropy is a state function ")
        if answer=="true":
            print "correct"
            right+=1
        else:
            print "wrong"
            wrong+=1
        return [right, wrong]
    elif number==35:
        answer=raw_input("True or False: A spontaneous process always results in an increase in entropy in the universe ")
        if answer=="true":
            print "correct"
            right+=1
        else:
            print "wrong"
            wrong+=1
        return [right, wrong]
    elif number==36:
        answer=raw_input("True or False: Nature spotaneously moves towards the states that have the lowest probability of existence ")
        if answer=="false":
            print "correct"
            right+=1
        else:
            print "wrong"
            wrong+=1
        return [right, wrong]
    elif number==37:
        answer=raw_input("True or False: DeltaSUniverse=DeltaSSystem-DeltaSSurrounding")
        if answer=="false":
            print "correct"
            right+=1
        else:
            print "wrong"
            wrong+=1
        return [right, wrong]
    elif number==38:
        answer=raw_input("True or False: The sign of DeltaSSurroundings is dependant on heat flow ")
        if answer=="true":
            print "correct"
            right+=1
        else:
            print "wrong"
            wrong+=1
        return [right, wrong]
    elif number==39:
        answer=raw_input("True or False: The magnitude of DeltaSSurroundings depends on the surrounding temperature ")
        if answer=="true":
            print "correct"
            right+=1
        else:
            print "wrong"
            wrong+=1
        return [right, wrong]
    elif number==40:
        answer=raw_input("True or False: DeltaG=DeltaH+TDeltaS ")
        if answer=="false":
            print "correct"
            right+=1
        else:
            print "wrong"
            wrong+=1
        return [right, wrong]
    elif number==41:
        answer=raw_input("True or False: -DeltaG/T=DeltaSUniverse ")
        if answer=="true":
            print "correct"
            right+=1
        else:
            print "wrong"
            wrong+=1
        return [right, wrong]
    elif number==42:
        answer=raw_input("True or False: A process is spontaneous when Gibbs Free Energy stays constant ")
        if answer=="false":
            print "correct"
            right+=1
        else:
            print "wrong"
            wrong+=1
        return [right, wrong]
    elif number==43:
        answer=raw_input("True or False: T=DeltaH0/DeltaS0 ")
        if answer=="true":
            print "correct"
            right+=1
        else:
            print "wrong"
            wrong+=1
        return [right, wrong]
    elif number==44:
        answer=raw_input("True or False: DeltaSReaction=DeltaSProducts-DeltaSReactants ")
        if answer=="true":
            print "correct"
            right+=1
        else:
            print "wrong"
            wrong+=1
        return [right, wrong]
    elif number==45:
        answer=raw_input("True or False: G=G0-RTln(q) ")
        if answer=="false":
            print "correct"
            right+=1
        else:
            print "wrong"
            wrong+=1
        return [right, wrong]
    elif number==46:
        answer=raw_input("True or False: At equilibrium, DeltaG0=-RTlnK ")
        if answer=="true":
            print "correct"
            right+=1
        else:
            print "wrong"
            wrong+=1
        return [right, wrong]
    elif number==47:
        answer=raw_input("True or False: Alpha particle production is not a common method of decay in radioactive heavy nuclear elements" )
        if answer=="false":
            print "correct"
            right+=1
        else:
            print "wrong"
            wrong+=1
        return [right, wrong]
    elif number==48:
        answer=raw_input("True or False: An alpha particle is a helium nucleus ")
        if answer=="true":
            print "correct"
            right+=1
        else:
            print "wrong"
            wrong+=1
        return [right, wrong]
    elif number==49:
        answer=raw_input("True or False: Spontaneous fission is an uncommon decay process in which a nucleus splits into two smaller nuclei of similar size ")
        if answer=="true":
            print "correct"
            right+=1
        else:
            print "wrong"
            wrong+=1
        return [right, wrong]
    elif number==50:
        answer=raw_input("True or False: A beta particle is a helium nucleus ")
        if answer=="false":
            print "correct"
            right+=1
        else:
            print "wrong"
            wrong+=1
        return [right, wrong]
    elif number==51:
        answer=raw_input("True or False: Gamma ray production often accompanies other types of decay ")
        if answer=="true":
            print "correct"
            right+=1
        else:
            print "wrong"
            wrong+=1
        return [right, wrong]
    elif number==52:
        answer=raw_input("True or False: Positron production turns a proton into a neutron, raising the neutron/proton ratio toward the zone of stability ")
        if answer=="true":
            print "correct"
            right+=1
        else:
            print "wrong"
            wrong+=1
        return [right, wrong]
    elif number==53:
        answer=raw_input("True or False: Ecell=Ereduction-Eoxidation")
        if answer=="false":
            print "correct"
            right+=1
        else:
            print "wrong"
            wrong+=1
        return [right, wrong]
    elif number==54:
        answer=raw_input("True or False: Ecell is always positive ")
        if answer=="true":
            print "correct"
            right+=1
        else:
            print "wrong"
            wrong+=1
        return [right, wrong]
    elif number==55:
        answer=raw_input("True or False: Eoxidation=Ereduction ")
        if answer=="false":
            print "correct"
            right+=1
        else:
            print "wrong"
            wrong+=1
        return [right, wrong]
    elif number==56:
        answer=raw_input("True or False: Ecell=Ecathode-Eanode ")
        if answer=="true":
            print "correct"
            right+=1
        else:
            print "wrong"
            wrong+=1
        return [right, wrong]
    elif number==57:
        answer=raw_input("True or False: The following is correct line notation X(s)|X^n+(aq)|Y^m+(aq)|Y(s) (anode is made of X, and cathode is made of Y) ")
        if answer=="true":
            print "correct"
            right+=1
        else:
            print "wrong"
            wrong+=1
        return [right, wrong]
    elif number==58:
        answer=raw_input("True or False: work=qEcell ")
        if answer=="false":
            print "correct"
            right+=1
        else:
            print "wrong"
            wrong+=1
        return [right, wrong]
    elif number==59:
        answer=raw_input("True or False: q=moles e*Faraday's Constant ")
        if answer=="true":
            print "correct"
            right+=1
        else:
            print "wrong"
            wrong+=1
        return [right, wrong]
    elif number==60:
        answer=raw_input("True or False: DeltaG=-moles e*Faraday's Constant*E0 ")
        if answer=="true":
            print "correct"
            right+=1
        else:
            print "wrong"
            wrong+=1
        return [right, wrong]
    elif number==61:
        answer=raw_input("True or False: E=E0+(RT/(moles E*Faraday's Constant))*ln(q) ")
        if answer=="true":
            print "correct"
            right+=1
        else:
            print "wrong"
            wrong+=1
        return [right, wrong]
    elif number==62:
        answer=raw_input("True or False: At 25 degrees Celsius E=E0-(0.0591/moles e)log(q) ")
        if answer=="false":
            print "correct"
            right+=1
        else:
            print "wrong"
            wrong+=1
        return [right, wrong]
    elif number==63:
        answer=raw_input("True or False: Q=([X]^n)/([Y]^m) when the balanced reactions result in nX and mY ")
        if answer=="true":
            print "correct"
            right+=1
        else:
            print "wrong"
            wrong+=1
        return [right, wrong]
    elif number==64:
        answer=raw_input("True or False: At equilibrium, log(k)=(n*E0)/0.0591 ")
        if answer=="true":
            print "correct"
            right+=1
        else:
            print "wrong"
            wrong+=1
        return [right, wrong]
    elif number==65:
        answer=raw_input("True or False: Amps(coulombs per second)* seconds=Coulombs, which can be used to find the metal deposited during electroplating ")
        if answer=="true":
            print "correct"
            right+=1
        else:
            print "wrong"
            wrong+=1
        return [right, wrong]
    elif number==66:
        answer=raw_input("True or False: HF is a strong acid ")
        if answer=="false":
            print "correct"
            right+=1
        else:
            print "wrong"
            wrong+=1
        return [right, wrong]
    elif number==67:
        answer=raw_input("True or False: HF can be used to etch glass ")
        if answer=="true":
            print "correct"
            right+=1
        else:
            print "wrong"
            wrong+=1
        return [right, wrong]
        
right, wrong=0,0
answerCollector=[]
while True:
    question=random.randint(1,67)
    while question in answerCollector:
        question=random.randint(1,67)
    answerCollector.append(question)
    if len(answerCollector)==3:
        del answerCollector[0]
    answers=questionSet(question, right, wrong)
    right=answers[0]
    wrong=answers[1]
    print right
    print wrong
        
