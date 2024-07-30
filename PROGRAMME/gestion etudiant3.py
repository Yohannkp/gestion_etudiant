from tkinter import*
import tkinter.font as font
from tkinter.messagebox import showerror,showinfo
import mysql.connector as mysql
from tkinter import ttk

db= mysql.connect(
    host= "localhost",
    user= "root",
    password= "",
    database="BULLETIN"
    )

#print(db)

cursor = db.cursor()
window=Tk()
window.title("BULLETIN D' EVALUATION")
window.geometry("1200x700")
window.config(background="#11719e")
window.iconbitmap("fond.ico")
#-------------------------------------------------------------------------
f = font.Font(family='Footlight MT Light', size=22)
label=Label(window, text="BULLETIN D' EVALUATION",bg="#11719e",fg="white")
label.place(x=540, y=0)
label["font"]=f
#-------------------------------------------------------------------------
f = font.Font(family='Footlight MT Light', size=19)
region=Entry(window,textvariable=StringVar(),width=20,bg="#11719e",fg="white")
region.place(x=297,y=20)
region2=Entry(window,textvariable=StringVar(),width=20,bg="#11719e",fg="white")
region2.place(x=297,y=40)
f = font.Font(family='Footlight MT Light', size=7)
label=Label(window, text="Region",bg="#11719e",fg="white")
label.place(x=297, y=10)
label["font"]=f
#-------------------------------------------------------------------------
nom_ecole=Entry(window,textvariable=StringVar(),width=35,bg="#11719e",fg="white")
nom_ecole.place(x=297,y=70)
#-------------------------------------------------------------------------
f = font.Font(family='Footlight MT Light', size=12)
label_nom=Label(window, text="Nom:",bg="#11719e",fg="white")
label_nom.place(x=330, y=100)
label_nom["font"]=f
nom=Entry(window,textvariable=StringVar(),width=20,bg="#11719e",fg="white")
nom.place(x=390,y=100)
#----------------------------------------------------------------------------
f = font.Font(family='Footlight MT Light', size=12)
label_prenom=Label(window, text="prenom:",bg="#11719e",fg="white")
label_prenom.place(x=570, y=100)
label_prenom["font"]=f
prenom=Entry(window,textvariable=StringVar(),width=24,bg="#11719e",fg="white")
prenom.place(x=635,y=100)
#--------------------------------------------------------------------------
f = font.Font(family='Footlight MT Light', size=12)
label_sexe=Label(window, text="Sexe:",bg="#11719e",fg="white")
label_sexe.place(x=792, y=100)
label_sexe["font"]=f
sexe=Entry(window,textvariable=StringVar(),width=20,bg="#11719e",fg="white")
sexe.place(x=860,y=100)
#-------------------------------------------------------------------
#------------------------------------------------------------------
f = font.Font(family='Footlight MT Light', size=12)
label_naissance=Label(window, text="Né(e)Le:",bg="#11719e",fg="white")
label_naissance.place(x=330, y=130)
label_naissance["font"]=f
naissance=Entry(window,textvariable=StringVar(),width=20,bg="#11719e",fg="white")
naissance.place(x=390,y=130)
#----------------------------------------------------------------------------
f = font.Font(family='Footlight MT Light', size=12)
label_lieu=Label(window, text="Lieu Naissance:",bg="#11719e",fg="white")
label_lieu.place(x=524, y=130)
label_lieu["font"]=f
lieu=Entry(window,textvariable=StringVar(),width=24,bg="#11719e",fg="white")
lieu.place(x=635,y=130)
#------------------------------------------------------------------
f = font.Font(family='Footlight MT Light', size=12)
label_numero=Label(window, text="N°Matri:",bg="#11719e",fg="white")
label_numero.place(x=792, y=130)
label_numero["font"]=f
numero=Entry(window,textvariable=StringVar(),width=20,bg="#11719e",fg="white")
numero.place(x=860,y=130)
#-------------------------------------------------------------------
#------------------------------------------------------------------
f = font.Font(family='Footlight MT Light', size=12)
label_sta=Label(window, text="Statut:",bg="#11719e",fg="white")
label_sta.place(x=792, y=160)
label_sta["font"]=f
sta=Entry(window,textvariable=StringVar(),width=20,bg="#11719e",fg="white")
sta.place(x=860,y=160)
#----------------------------------------------------------------------------
f = font.Font(family='Footlight MT Light', size=12)
label_class=Label(window, text="Classe:",bg="#11719e",fg="white")
label_class.place(x=581, y=160)
label_class["font"]=f
classe=Entry(window,textvariable=StringVar(),width=24,bg="#11719e",fg="white")
classe.place(x=635,y=160)
#------------------------------------------------------------------
f = font.Font(family='Footlight MT Light', size=12)
label_anne=Label(window, text="Année scolaire:",bg="#11719e",fg="white")
label_anne.place(x=287, y=160)
label_anne["font"]=f
anne=Entry(window,textvariable=StringVar(),width=20,bg="#11719e",fg="white")
anne.place(x=390,y=160)
#--------------------------------------------------------------------
#--------------------------------------------------------------------
f = font.Font(family='Footlight MT Light', size=12)
label_decou=Label(window, text="Decoupage Année:",bg="#11719e",fg="white")
label_decou.place(x=380, y=194)
label_decou["font"]=f
decou=Entry(window,textvariable=StringVar(),width=20,bg="#11719e",fg="white")
decou.place(x=513,y=194)
#-------------------------------------------------------------------------
f = font.Font(family='Footlight MT Light', size=12)
label_effectif=Label(window, text="Effectif:",bg="#11719e",fg="white")
label_effectif.place(x=700, y=194)
label_effectif["font"]=f
effectif=Entry(window,textvariable=StringVar(),width=20,bg="#11719e",fg="white")
effectif.place(x=760,y=194)
#----------------------------------------------------------------------------------------------------------------------
f = font.Font(family='Footlight MT Light', size=12)
labeltrait=Label(window, text="                                                                                                                                                                                                        ",bg="#11719e",fg="white")
labeltrait.place(x=290, y=230)
labeltrait["font"]=f
f.configure(underline=True)
#--------------------------------------------------------------------
f = font.Font(family='Footlight MT Light', size=12)
label_disci=Label(window, text="DISCIPLINES",bg="#11719e",fg="white")
label_disci.place(x=290, y=260)
label_disci["font"]=f
#--------------------------------------------------------------------
f = font.Font(family='Footlight MT Light', size=12)
label_moycls=Label(window, text="MOYENNE DE\nCLASSE",bg="#11719e",fg="white")
label_moycls.place(x=430, y=260)
label_moycls["font"]=f
#--------------------------------------------------------------------
f = font.Font(family='Footlight MT Light', size=12)
label_exam=Label(window, text="NOTE DE\nCOMPOSITION",bg="#11719e",fg="white")
label_exam.place(x=530, y=260)
label_exam["font"]=f
#---------------------------------------------------------------------
f = font.Font(family='Footlight MT Light', size=12)
label_moyge=Label(window, text="MOYENNE\nGENERALE",bg="#11719e",fg="white")
label_moyge.place(x=650, y=260)
label_moyge["font"]=f
#------------------------------------------------------------------------
f = font.Font(family='Footlight MT Light', size=12)
label_coeff=Label(window, text="COEFF",bg="#11719e",fg="white")
label_coeff.place(x=740, y=260)
label_coeff["font"]=f
#-------------------------------------------------------------------------
f = font.Font(family='Footlight MT Light', size=12)
label_rg=Label(window, text="RANG",bg="#11719e",fg="white")
label_rg.place(x=800, y=260)
label_rg["font"]=f
#---------------------------------------------------------------------------t
f = font.Font(family='Footlight MT Light', size=12)
label_prof=Label(window, text="PROFESSEURS",bg="#11719e",fg="white")
label_prof.place(x=850, y=260)
label_prof["font"]=f
#-----------------------------------------------------------------------------
f = font.Font(family='Footlight MT Light', size=12)
label_apre=Label(window, text="APPRECIATIONS",bg="#11719e",fg="white")
label_apre.place(x=980, y=260)
label_apre["font"]=f
#-----------------------------------------------------------------------------
f = font.Font(family='Footlight MT Light', size=12)
labeltrait2=Label(window, text="                                                                                                                                                                                                        ",bg="#11719e",fg="white")                                                                                                                                                                                                      
labeltrait2.place(x=290, y=300)
labeltrait2["font"]=f
f.configure(underline=True)
#---------------------------------------------------------------------------------
f = font.Font(family='Footlight MT Light', size=12)
labelmat2=Label(window, text="MATIERES SCIENTIFIQUES",bg="#11719e",fg="white")                                                                                                                                                                                                      
labelmat2.place(x=600, y=320)
labelmat2["font"]=f
f.configure(underline=True)
#---------------------------------------------------------------------------------
disci1=Entry(window,textvariable=StringVar(),width=23,bg="#11719e",fg="white")
disci1.place(x=290,y=360)
#---------------------------------------------------------------------------------
moycls1=Entry(window,textvariable=IntVar(),width=16,bg="#11719e",fg="white")
moycls1.place(x=432,y=360)
#---------------------------------------------------------------------------------
exam1=Entry(window,textvariable=IntVar(),width=17,bg="#11719e",fg="white")
exam1.place(x=532,y=360)
#---------------------------------------------------------------------------------
moygen1=Entry(window,textvariable=IntVar(),width=15,bg="#11719e",fg="white")
moygen1.place(x=638,y=360)
#---------------------------------------------------------------------------------
coeff1=Entry(window,textvariable=IntVar(),width=11,bg="#11719e",fg="white")
coeff1.place(x=732,y=360)
#---------------------------------------------------------------------------------
rang1=Entry(window,textvariable=StringVar(),width=8,bg="#11719e",fg="white")
rang1.place(x=802,y=360)
#---------------------------------------------------------------------------------
prof1=Entry(window,textvariable=StringVar(),width=17,bg="#11719e",fg="white")
prof1.place(x=854,y=360)
#---------------------------------------------------------------------------------
apre1=Entry(window,textvariable=StringVar(),width=21,bg="#11719e",fg="white")
apre1.place(x=960,y=360)
#-----------------------------------------------------------------------------------
#----------------------------------------------------------------------------------
#---------------------------------------------------------------------------------
disci2=Entry(window,textvariable=StringVar(),width=23,bg="#11719e",fg="white")
disci2.place(x=290,y=380)
#---------------------------------------------------------------------------------
moycls2=Entry(window,textvariable=IntVar(),width=16,bg="#11719e",fg="white")
moycls2.place(x=432,y=380)
#---------------------------------------------------------------------------------
exam2=Entry(window,textvariable=IntVar(),width=17,bg="#11719e",fg="white")
exam2.place(x=532,y=380)
#---------------------------------------------------------------------------------
moygen2=Entry(window,textvariable=IntVar(),width=15,bg="#11719e",fg="white")
moygen2.place(x=638,y=380)
#---------------------------------------------------------------------------------
coeff2=Entry(window,textvariable=IntVar(),width=11,bg="#11719e",fg="white")
coeff2.place(x=732,y=380)
#---------------------------------------------------------------------------------
rang2=Entry(window,textvariable=StringVar(),width=8,bg="#11719e",fg="white")
rang2.place(x=802,y=380)
#---------------------------------------------------------------------------------
prof2=Entry(window,textvariable=StringVar(),width=17,bg="#11719e",fg="white")
prof2.place(x=854,y=380)
#---------------------------------------------------------------------------------
apre2=Entry(window,textvariable=StringVar(),width=21,bg="#11719e",fg="white")
apre2.place(x=960,y=380)
#-----------------------------------------------------------------------------------
#----------------------------------------------------------------------------------
#---------------------------------------------------------------------------------
disci3=Entry(window,textvariable=StringVar(),width=23,bg="#11719e",fg="white")
disci3.place(x=290,y=400)
#---------------------------------------------------------------------------------
moycls3=Entry(window,textvariable=IntVar(),width=16,bg="#11719e",fg="white")
moycls3.place(x=432,y=400)
#---------------------------------------------------------------------------------
exam3=Entry(window,textvariable=IntVar(),width=17,bg="#11719e",fg="white")
exam3.place(x=532,y=400)
#---------------------------------------------------------------------------------
moygen3=Entry(window,textvariable=IntVar(),width=15,bg="#11719e",fg="white")
moygen3.place(x=638,y=400)
#---------------------------------------------------------------------------------
coeff3=Entry(window,textvariable=IntVar(),width=11,bg="#11719e",fg="white")
coeff3.place(x=732,y=400)
#---------------------------------------------------------------------------------
rang3=Entry(window,textvariable=StringVar(),width=8,bg="#11719e",fg="white")
rang3.place(x=802,y=400)
#---------------------------------------------------------------------------------
prof3=Entry(window,textvariable=StringVar(),width=17,bg="#11719e",fg="white")
prof3.place(x=854,y=400)
#---------------------------------------------------------------------------------
apre3=Entry(window,textvariable=StringVar(),width=21,bg="#11719e",fg="white")
apre3.place(x=960,y=400)
f = font.Font(family='Footlight MT Light', size=12)
labelmat3=Label(window, text="MATIERES LTTERAIRES",bg="#11719e",fg="white")                                                                                                                                                                                                      
labelmat3.place(x=614, y=420)
labelmat3["font"]=f
f.configure(underline=True)
#-----------------------------------------------------------------------------------
#----------------------------------------------------------------------------------
#---------------------------------------------------------------------------------
disci4=Entry(window,textvariable=StringVar(),width=23,bg="#11719e",fg="white")
disci4.place(x=290,y=460)
#---------------------------------------------------------------------------------
moycls4=Entry(window,textvariable=IntVar(),width=16,bg="#11719e",fg="white")
moycls4.place(x=432,y=460)
#---------------------------------------------------------------------------------
exam4=Entry(window,textvariable=IntVar(),width=17,bg="#11719e",fg="white")
exam4.place(x=532,y=460)
#---------------------------------------------------------------------------------
moygen4=Entry(window,textvariable=IntVar(),width=15,bg="#11719e",fg="white")
moygen4.place(x=638,y=460)
#---------------------------------------------------------------------------------
coeff4=Entry(window,textvariable=IntVar(),width=11,bg="#11719e",fg="white")
coeff4.place(x=732,y=460)
#---------------------------------------------------------------------------------
rang4=Entry(window,textvariable=StringVar(),width=8,bg="#11719e",fg="white")
rang4.place(x=802,y=460)
#---------------------------------------------------------------------------------
prof4=Entry(window,textvariable=StringVar(),width=17,bg="#11719e",fg="white")
prof4.place(x=854,y=460)
#---------------------------------------------------------------------------------
apre4=Entry(window,textvariable=StringVar(),width=21,bg="#11719e",fg="white")
apre4.place(x=960,y=460)
#-----------------------------------------------------------------------------------
#----------------------------------------------------------------------------------
#---------------------------------------------------------------------------------
disci5=Entry(window,textvariable=StringVar(),width=23,bg="#11719e",fg="white")
disci5.place(x=290,y=480)
#---------------------------------------------------------------------------------
moycls5=Entry(window,textvariable=IntVar(),width=16,bg="#11719e",fg="white")
moycls5.place(x=432,y=480)
#---------------------------------------------------------------------------------
exam5=Entry(window,textvariable=IntVar(),width=17,bg="#11719e",fg="white")
exam5.place(x=532,y=480)
#---------------------------------------------------------------------------------
moygen5=Entry(window,textvariable=IntVar(),width=15,bg="#11719e",fg="white")
moygen5.place(x=638,y=480)
#---------------------------------------------------------------------------------
coeff5=Entry(window,textvariable=IntVar(),width=11,bg="#11719e",fg="white")
coeff5.place(x=732,y=480)
#---------------------------------------------------------------------------------
rang5=Entry(window,textvariable=StringVar(),width=8,bg="#11719e",fg="white")
rang5.place(x=802,y=480)
#---------------------------------------------------------------------------------
prof5=Entry(window,textvariable=StringVar(),width=17,bg="#11719e",fg="white")
prof5.place(x=854,y=480)
#---------------------------------------------------------------------------------
apre5=Entry(window,textvariable=StringVar(),width=21,bg="#11719e",fg="white")
apre5.place(x=960,y=480)
#-----------------------------------------------------------------------------------
#----------------------------------------------------------------------------------
#---------------------------------------------------------------------------------
disci6=Entry(window,textvariable=StringVar(),width=23,bg="#11719e",fg="white")
disci6.place(x=290,y=500)
#---------------------------------------------------------------------------------
moycls6=Entry(window,textvariable=IntVar(),width=16,bg="#11719e",fg="white")
moycls6.place(x=432,y=500)
#---------------------------------------------------------------------------------
exam6=Entry(window,textvariable=IntVar(),width=17,bg="#11719e",fg="white")
exam6.place(x=532,y=500)
#---------------------------------------------------------------------------------
moygen6=Entry(window,textvariable=IntVar(),width=15,bg="#11719e",fg="white")
moygen6.place(x=638,y=500)
#---------------------------------------------------------------------------------
coeff6=Entry(window,textvariable=IntVar(),width=11,bg="#11719e",fg="white")
coeff6.place(x=732,y=500)
#---------------------------------------------------------------------------------
rang6=Entry(window,textvariable=StringVar(),width=8,bg="#11719e",fg="white")
rang6.place(x=802,y=500)
#---------------------------------------------------------------------------------
prof6=Entry(window,textvariable=StringVar(),width=17,bg="#11719e",fg="white")
prof6.place(x=854,y=500)
#---------------------------------------------------------------------------------
apre6=Entry(window,textvariable=StringVar(),width=21,bg="#11719e",fg="white")
apre6.place(x=960,y=500)
#-----------------------------------------------------------------------------------
#----------------------------------------------------------------------------------
#---------------------------------------------------------------------------------
disci7=Entry(window,textvariable=StringVar(),width=23,bg="#11719e",fg="white")
disci7.place(x=290,y=520)
#---------------------------------------------------------------------------------
moycls7=Entry(window,textvariable=IntVar(),width=16,bg="#11719e",fg="white")
moycls7.place(x=432,y=520)
#---------------------------------------------------------------------------------
exam7=Entry(window,textvariable=IntVar(),width=17,bg="#11719e",fg="white")
exam7.place(x=532,y=520)
#---------------------------------------------------------------------------------
moygen7=Entry(window,textvariable=IntVar(),width=15,bg="#11719e",fg="white")
moygen7.place(x=638,y=520)
#---------------------------------------------------------------------------------
coeff7=Entry(window,textvariable=IntVar(),width=11,bg="#11719e",fg="white")
coeff7.place(x=732,y=520)
#---------------------------------------------------------------------------------
rang7=Entry(window,textvariable=StringVar(),width=8,bg="#11719e",fg="white")
rang7.place(x=802,y=520)
#---------------------------------------------------------------------------------
prof7=Entry(window,textvariable=StringVar(),width=17,bg="#11719e",fg="white")
prof7.place(x=854,y=520)
#---------------------------------------------------------------------------------
apre7=Entry(window,textvariable=StringVar(),width=21,bg="#11719e",fg="white")
apre7.place(x=960,y=520)
f = font.Font(family='Footlight MT Light', size=12)
labelmat3=Label(window, text="MATIERES FACULTATIVES",bg="#11719e",fg="white")                                                                                                                                                                                                      
labelmat3.place(x=607, y=540)
labelmat3["font"]=f
f.configure(underline=True)
#-----------------------------------------------------------------------------------
#----------------------------------------------------------------------------------
#---------------------------------------------------------------------------------
disci8=Entry(window,textvariable=StringVar(),width=23,bg="#11719e",fg="white")
disci8.place(x=290,y=580)
#---------------------------------------------------------------------------------
moycls8=Entry(window,textvariable=IntVar(),width=16,bg="#11719e",fg="white")
moycls8.place(x=432,y=580)
#---------------------------------------------------------------------------------
exam8=Entry(window,textvariable=IntVar(),width=17,bg="#11719e",fg="white")
exam8.place(x=532,y=580)
#---------------------------------------------------------------------------------
moygen8=Entry(window,textvariable=IntVar(),width=15,bg="#11719e",fg="white")
moygen8.place(x=638,y=580)
#---------------------------------------------------------------------------------
coeff8=Entry(window,textvariable=IntVar(),width=11,bg="#11719e",fg="white")
coeff8.place(x=732,y=580)
#---------------------------------------------------------------------------------
rang8=Entry(window,textvariable=StringVar(),width=8,bg="#11719e",fg="white")
rang8.place(x=802,y=580)
#---------------------------------------------------------------------------------
prof8=Entry(window,textvariable=StringVar(),width=17,bg="#11719e",fg="white")
prof8.place(x=854,y=580)
#---------------------------------------------------------------------------------
apre8=Entry(window,textvariable=StringVar(),width=21,bg="#11719e",fg="white")
apre8.place(x=960,y=580)
#-----------------------------------------------------------------------------------
#----------------------------------------------------------------------------------
#---------------------------------------------------------------------------------
disci9=Entry(window,textvariable=StringVar(),width=23,bg="#11719e",fg="white")
disci9.place(x=290,y=600)
#---------------------------------------------------------------------------------
moycls9=Entry(window,textvariable=IntVar(),width=16,bg="#11719e",fg="white")
moycls9.place(x=432,y=600)
#---------------------------------------------------------------------------------
exam9=Entry(window,textvariable=IntVar(),width=17,bg="#11719e",fg="white")
exam9.place(x=532,y=600)
#---------------------------------------------------------------------------------
moygen9=Entry(window,textvariable=IntVar(),width=15,bg="#11719e",fg="white")
moygen9.place(x=638,y=600)
#---------------------------------------------------------------------------------
coeff9=Entry(window,textvariable=IntVar(),width=11,bg="#11719e",fg="white")
coeff9.place(x=732,y=600)
#---------------------------------------------------------------------------------
rang9=Entry(window,textvariable=StringVar(),width=8,bg="#11719e",fg="white")
rang9.place(x=802,y=600)
#---------------------------------------------------------------------------------
prof9=Entry(window,textvariable=StringVar(),width=17,bg="#11719e",fg="white")
prof9.place(x=854,y=600)
#--------------------------------------------------------------------------------
apre9=Entry(window,textvariable=StringVar(),width=21,bg="#11719e",fg="white")
apre9.place(x=960,y=600)
#-----------------------------------------------------------------------------------
#----------------------------------------------------------------------------------
#---------------------------------------------------------------------------------
disci10=Entry(window,textvariable=StringVar(),width=23,bg="#11719e",fg="white")
disci10.place(x=290,y=620)
#---------------------------------------------------------------------------------
moycls10=Entry(window,textvariable=IntVar(),width=16,bg="#11719e",fg="white")
moycls10.place(x=432,y=620)
#---------------------------------------------------------------------------------
exam10=Entry(window,textvariable=IntVar(),width=17,bg="#11719e",fg="white")
exam10.place(x=532,y=620)
#---------------------------------------------------------------------------------
moygen10=Entry(window,textvariable=IntVar(),width=15,bg="#11719e",fg="white")
moygen10.place(x=638,y=620)
#---------------------------------------------------------------------------------
coeff10=Entry(window,textvariable=IntVar(),width=11,bg="#11719e",fg="white")
coeff10.place(x=732,y=620)
#---------------------------------------------------------------------------------
rang10=Entry(window,textvariable=StringVar(),width=8,bg="#11719e",fg="white")
rang10.place(x=802,y=620)
#---------------------------------------------------------------------------------
prof10=Entry(window,textvariable=StringVar(),width=17,bg="#11719e",fg="white")
prof10.place(x=854,y=620)
#--------------------------------------------------------------------------------
apre10=Entry(window,textvariable=StringVar(),width=21,bg="#11719e",fg="white")
apre10.place(x=960,y=620)
#-----------------------------------------------------------------------------------
#----------------------------------------------------------------------------------
#---------------------------------------------------------------------------------
disci11=Entry(window,textvariable=StringVar(),width=23,bg="#11719e",fg="white")
disci11.place(x=290,y=640)
#---------------------------------------------------------------------------------
moycls11=Entry(window,textvariable=IntVar(),width=16,bg="#11719e",fg="white")
moycls11.place(x=432,y=640)
#---------------------------------------------------------------------------------
exam11=Entry(window,textvariable=IntVar(),width=17,bg="#11719e",fg="white")
exam11.place(x=532,y=640)
#---------------------------------------------------------------------------------
moygen11=Entry(window,textvariable=IntVar(),width=15,bg="#11719e",fg="white")
moygen11.place(x=638,y=640)
#---------------------------------------------------------------------------------
coeff11=Entry(window,textvariable=IntVar(),width=11,bg="#11719e",fg="white")
coeff11.place(x=732,y=640)
#---------------------------------------------------------------------------------
rang11=Entry(window,textvariable=StringVar(),width=8,bg="#11719e",fg="white")
rang11.place(x=802,y=640)
#---------------------------------------------------------------------------------
prof11=Entry(window,textvariable=StringVar(),width=17,bg="#11719e",fg="white")
prof11.place(x=854,y=640)
#--------------------------------------------------------------------------------
apre11=Entry(window,textvariable=StringVar(),width=21,bg="#11719e",fg="white")              
apre11.place(x=960,y=640)
#-------------------------------------------------------------------------------------------
f = font.Font(family='Footlight MT Light', size=12)
labeltot=Label(window, text="TOTAUX:",bg="#11719e",fg="white") 
labeltot.place(x=290,y=660)
labeltot["font"]=f
f.configure(underline=True)
#-------------------------------------------------------------------------------------------
coeff_final=Entry(window,textvariable=StringVar(),width=11,bg="#11719e",fg="white")
coeff_final.place(x=732,y=660)
#-------------------------------------------------------------------------------------
moygen_final=Entry(window,textvariable=StringVar(),width=15,bg="#11719e",fg="white")
moygen_final.place(x=638,y=660)
#----------------------------------------------------------------------------------------------------------------------------------------
f = font.Font(family='Footlight MT Light', size=12)
labelmoytot=Label(window, text="MOYENNE:",bg="#11719e",fg="white") 
labelmoytot.place(x=290,y=680)
labelmoytot["font"]=f
f.configure(underline=True)
moyenn_final=Entry(window,textvariable=StringVar(),width=21,bg="#11719e",fg="white")
moyenn_final.place(x=960,y=660)

f = font.Font(family='Footlight MT Light', size=12)
label_idel=Label(window, text="id eleve:",bg="#11719e",fg="white")
label_idel.place(x=70, y=250)
label_idel["font"]=f

f = font.Font(family='Footlight MT Light', size=12)
label_idmat=Label(window, text="id matiere:",bg="#11719e",fg="white")
label_idmat.place(x=70, y=302)
label_idmat["font"]=f
idselect=Entry(window,textvariable=IntVar(),width=17,bg="#11719e",fg="white")
idselect.place(x=150,y=250)
idselect2=Entry(window,textvariable=IntVar(),width=17,bg="#11719e",fg="white")
idselect2.place(x=150,y=302)

 
class Eleve:
    def __init__(self,nom,prenom,sexe,date_naiss,lieu,matricule,statut,classe,Annescol,decoup):
        self.nom=nom
        self.prenom=prenom
        self.sexe=sexe
        self.date_naiss=date_naiss
        self.lieu=lieu
        self.matricule=matricule
        self.statut=statut
        self.classe=classe
        self.Annescol=Annescol
        self.decoup=decoup
class Matiere:
    def __init__(self,nom_mat,moyclass,notecompo,moygen,coef,prof,apreci):
        self.nom_mat=nom_mat
        self.moyclass=moyclass
        self.notecompo=notecompo
        self.moygen=moygen
        self.coef=coef
        self.prof=prof
        self.apreci=apreci

        
def calculer_moy():
    moy1=int(float(moygen1.get()))*int(float(coeff1.get()))
    moy2=int(float(moygen2.get()))*int(float(coeff2.get()))
    moy3=int(float(moygen3.get()))*int(float(coeff3.get()))
    moy4=int(float(moygen4.get()))*int(float(coeff4.get()))
    moy5=int(float(moygen5.get()))*int(float(coeff5.get()))
    moy6=int(float(moygen6.get()))*int(float(coeff6.get()))
    moy7=int(float(moygen7.get()))*int(float(coeff7.get()))
    moy8=int(float(moygen8.get()))*int(float(coeff8.get()))
    moy9=int(float(moygen9.get()))*int(float(coeff9.get()))
    moy10=int(float(moygen10.get()))*int(float(coeff10.get()))
    moy11=int(float(moygen11.get()))*int(float(coeff11.get()))
    moygencoeff=moy1+moy2+moy3+moy4+moy5+moy6+moy7+moy8+moy9+moy10+moy11
    coefftot=int(coeff1.get())+int(coeff2.get())+int(coeff3.get())+int(coeff4.get())+int(coeff5.get())+int(coeff6.get())+int(coeff7.get())+int(coeff8.get())+int(coeff9.get())+int(coeff10.get())+int(coeff11.get())
    if moygencoeff==0 and coefftot==0:
        showerror(title="Validation error",message="Remplissez tous les champs")
    else:
        id_eleve=idselect.get()
        moygen_final.insert(INSERT,moygencoeff)
        coeff_final.insert(INSERT,coefftot)
        moyenne_general=moygencoeff/coefftot
        moyenn_final.insert(INSERT,moyenne_general)
        id_moy=0
        if moyenne_general<=7:
            id_moy=1
            insertion="INSERT INTO Moyengen(id_moyenne,moyennegenerale,id_eleve)VALUES(%s,%s,%s)"
            valeurs=(id_moy, moyenne_general,id_eleve)
            cursor.execute(insertion, valeurs)
            db.commit()
            showinfo(title="Validation Reussi",message="Moyenne CALCULE")
        elif moyenne_general >=7 and moyenne_general <10:
            id_moy=2
            insertion="INSERT INTO Moyengen(id_moyenne,moyennegenerale,id_eleve)VALUES(%s,%s,%s)"
            valeurs=(id_moy, moyenne_general,id_eleve)
            cursor.execute(insertion, valeurs)
            db.commit()
            showinfo(title="Validation Reussi",message="Moyenne CALCULE")
        elif moyenne_general >=10 and moyenne_general<11:
            id_moy=3
            insertion="INSERT INTO Moyengen(id_moyenne,moyennegenerale,id_eleve)VALUES(%s,%s,%s)"
            valeurs=(id_moy, moyenne_general,id_eleve)
            cursor.execute(insertion, valeurs)
            db.commit()
            showinfo(title="Validation Reussi",message="Moyenne CALCULE")
        elif moyenne_general>11 and moyenne_general<=13:
            id_moy=4
            insertion="INSERT INTO Moyengen(id_moyenne,moyennegenerale,id_eleve)VALUES(%s,%s,%s)"
            valeurs=(id_moy, moyenne_general,id_eleve)
            cursor.execute(insertion, valeurs)
            db.commit()
            showinfo(title="Validation Reussi",message="Moyenne CALCULE")
        elif moyenne_general>13 and moyenne_general<=15:
            id_moy=5
            insertion="INSERT INTO Moyengen(id_moyenne,moyennegenerale,id_eleve)VALUES(%s,%s,%s)"
            valeurs=(id_moy, moyenne_general,id_eleve)
            cursor.execute(insertion, valeurs)
            db.commit()
            showinfo(title="Validation Reussi",message="Moyenne CALCULE")
        elif moyenne_general>=16:
            id_moy=6
            insertion="INSERT INTO Moyengen(id_moyenne,moyennegenerale,id_eleve)VALUES(%s,%s,%s)"
            valeurs=(id_moy, moyenne_general,id_eleve)
            cursor.execute(insertion, valeurs)
            db.commit()
            showinfo(title="Validation Reussi",message="Moyenne CALCULE")
    
listenom=[]
listeprenom=[]
listesexe=[]
listenaiss=[]
listelieu=[]
listenum=[]
listesta=[]
listeclasse=[]
listeanne=[]
listedecou=[]
liste_elevetab=[]


    
def liste_eleve():
      
    fenetre_liste=Toplevel(window)
    fenetre_liste.title("Listes des eleves")
    fenetre_liste.geometry("1200x700")
    #fenetre_liste.iconbitmap("icone.ico")
    #fenetre_liste.iconbitmap("ico1.ico")
    fenetre_liste.config(background="#11719e")
    def afficher():
        db= mysql.connect(
            host= "localhost",
            user= "root",
            password= "",
            database="BULLETIN"
        )

        cursor = db.cursor()
        cursor.execute("SELECT id_eleve,nom,prenom,sexe,naissance,lieu,numero,statut,classe,anne,decou FROM Eleve")
        fenetre_liste.config(background="#11719e")
        label_liste_eleve=Label(fenetre_liste, text="Listes des Eleves Enregistrés",fg="white",bg="#11719e")
        f = font.Font(family='Footlight MT Light', size=22, weight="bold")
        label_liste_eleve["font"]=f
        label_liste_eleve.place(x=510,y=0)
        rows=cursor.fetchall()
        for i,(id_eleve,nom,prenom,sexe,naissance,lieu,numero,statut,classe,anne,decou) in enumerate(rows,start=1):
            listbox.insert("","end",values=(id_eleve,nom,prenom,sexe,naissance,lieu,numero,statut,classe,anne,decou))
            db.close()

    cols=("Id_eleve","Nom","Prenom","Sexe","Date Naissance","Lieu N","Matricule","Statut","Classe","Anne","Decoup")
    listbox = ttk.Treeview(fenetre_liste,columns=cols,show="headings",height=28)

    for col in cols:
        listbox.heading(col, text=col)
        listbox.grid(row=1,column=0,columnspan=3)
        listbox.heading(col, text=col)
        listbox.place(x=0,y=60)
                
    afficher()
            

def calculatrice():
    fenetre_calcul=Toplevel(window)
    fenetre_calcul.geometry("490x300")
    affich=Label(fenetre_calcul,text="CALCULATRICE",fg="white",bg="#11719e")
    affich.place(x=127,y=0)
    fenetre_calcul.resizable(width=FALSE,height=FALSE)
    fenetre_calcul.title("CALCULATRICE")
    fenetre_calcul.config(background="#11719e")
    nombre1=Entry(fenetre_calcul,textvariable=IntVar(),width=23,fg="white",bg="#11719e")
    nombre1.place(x=100,y=20)
    nombre2=Entry(fenetre_calcul,textvariable=IntVar(),width=23,fg="white",bg="#11719e")
    nombre2.place(x=100,y=40)
    def add():
        rep=int(nombre1.get())+int((nombre2.get()))
        resultat.insert(INSERT,rep)

    def sous():
        rep=(int(nombre1.get()))-(int((nombre2.get())))
        resultat.insert(INSERT,rep)
    def mul():
        rep=(int(nombre1.get()))*(int((nombre2.get())))
        resultat.insert(INSERT,rep)
    def div():
        rep=(int(nombre1.get()))/(int((nombre2.get())))
        resultat.insert(INSERT,rep)
    def delc():
        no1=nombre1.delete(0,END)
        no2=nombre2.delete(0,END)
        res=resultat.delete(0,END)
    buton1=Button(fenetre_calcul,text="+",fg="white",bg="#11719e",command=add)
    buton1.place(x=160,y=60)
    buton2=Button(fenetre_calcul,text="-",fg="white",bg="#11719e",command=sous)
    buton2.place(x=100,y=90)
    buton3=Button(fenetre_calcul,text="x",fg="white",bg="#11719e",command=mul)
    buton3.place(x=220,y=90)
    buton4=Button(fenetre_calcul,text="/",fg="white",bg="#11719e",command=div)
    buton4.place(x=160,y=130)
    buton_del=Button(fenetre_calcul,text="supprimer",fg="white",bg="#11719e",command=delc)
    buton_del.place(x=138,y=200)
    resultat_label=Label(fenetre_calcul,text="RESULTAT:",fg="white",bg="#11719e")
    resultat_label.place(x=20,y=160)
    resultat=Entry(fenetre_calcul,textvariable=StringVar(),width=23,fg="white",bg="#11719e")
    resultat.place(x=100,y=160)
def notegen():
    
    fenetre_liste=Toplevel(window)
    fenetre_liste.title("CALCUL MOYENNE GENERALE")
    fenetre_liste.geometry("490x300")
    #fenetre_liste.iconbitmap("icone.ico")
    #fenetre_liste.iconbitmap("ico1.ico")
    fenetre_liste.config(background="#11719e")
    fenetre_liste.resizable(width=FALSE,height=FALSE)
    moycls_label=Label(fenetre_liste,text="Moyenne classe",fg="white",bg="#11719e")
    moycls_label.place(x=30,y=60)
    moycls=Entry(fenetre_liste,textvariable=IntVar(),width=23,bg="#11719e",fg="white")
    moycls.place(x=140,y=80)

    compo_label=Label(fenetre_liste,text="Note compo:",fg="white",bg="#11719e")
    compo_label.place(x=30,y=80)
    compo=Entry(fenetre_liste,textvariable=IntVar(),width=23,bg="#11719e",fg="white")
    compo.place(x=140,y=60)
    

    
    coef_label=Label(fenetre_liste,text="Coefficient:",fg="white",bg="#11719e")
    coef_label.place(x=30,y=100)
    coef=Entry(fenetre_liste,textvariable=IntVar(),width=23,bg="#11719e",fg="white")
    coef.place(x=140,y=100)
    def calcul_note():
        moyclscl=int(float(moycls.get()))
        coefcl=int(float(coef.get()))
        compocl=int(float(compo.get()))        
        calcul=(moyclscl+compocl)/coefcl
        moyengentot.insert(INSERT,calcul)
        showinfo(title="Validation Reussi",message="Moyenne GENERALE CALCULE")
    def supprimer():
        moycls1=moycls.delete(0,END)
        compon1=compo.delete(0,END)
        coef1=coef.delete(0,END)
        moyengentot1=moyengentot.delete(0,END)
    boutton_calcul=Button(fenetre_liste, text="calculer la moyenne generale ", width=26, height=1,bg="#FF6800",fg="white",command=calcul_note)
    boutton_calcul.place(x=90,y=200)

    boutton_del=Button(fenetre_liste, text="supprimer", width=15, height=1,bg="#FF6800",fg="white",command=supprimer)
    boutton_del.place(x=300,y=200)
    
    moygen_label=Label(fenetre_liste,text="MOYENNE GENERALE:",fg="white",bg="#11719e")
    moygen_label.place(x=10,y=140)
    
    moyengentot=Entry(fenetre_liste,textvariable=IntVar(),width=23,bg="#11719e",fg="white")                                                                                                
    moyengentot.place(x=140,y=140)


    
def noteclass():
    
    fenetre_liste=Toplevel(window)
    fenetre_liste.title("calcul note")
    fenetre_liste.geometry("490x300")
    #fenetre_liste.iconbitmap("icone.ico")
    #fenetre_liste.iconbitmap("ico1.ico")
    fenetre_liste.config(background="#11719e")
    fenetre_liste.resizable(width=FALSE,height=FALSE)
    intero1_label=Label(fenetre_liste,text="Interrogation1:",fg="white",bg="#11719e")
    intero1_label.place(x=50,y=60)
    intero1=Entry(fenetre_liste,textvariable=IntVar(),width=23,bg="#11719e",fg="white")
    intero1.place(x=140,y=60)
    
    intero2_label=Label(fenetre_liste,text="Interrogation2:",fg="white",bg="#11719e")
    intero2_label.place(x=50,y=80)
    intero2=Entry(fenetre_liste,textvariable=IntVar(),width=23,bg="#11719e",fg="white")
    intero2.place(x=140,y=80)

    
    intero3_label=Label(fenetre_liste,text="Interrogation3:",fg="white",bg="#11719e")
    intero3_label.place(x=50,y=100)
    intero3=Entry(fenetre_liste,textvariable=IntVar(),width=23,bg="#11719e",fg="white")
    intero3.place(x=140,y=100)


    intero4_label=Label(fenetre_liste,text="Interrogation4:",fg="white",bg="#11719e")
    intero4_label.place(x=50,y=120)
    intero4=Entry(fenetre_liste,textvariable=IntVar(),width=23,bg="#11719e",fg="white")
    intero4.place(x=140,y=120)

    Note_devoir1_label=Label(fenetre_liste,text="Note devoir1:",fg="white",bg="#11719e")
    Note_devoir1_label.place(x=50,y=140)
    Note_devoir1=Entry(fenetre_liste,textvariable=IntVar(),width=23,bg="#11719e",fg="white")
    Note_devoir1.place(x=140,y=140)
    
    Note_devoir2_label=Label(fenetre_liste,text="Note devoir2:",fg="white",bg="#11719e")
    Note_devoir2_label.place(x=50,y=160)
    Note_devoir2=Entry(fenetre_liste,textvariable=IntVar(),width=23,bg="#11719e",fg="white")
    Note_devoir2.place(x=140,y=160)

    coef_label=Label(fenetre_liste,text="coefficient matiere:",fg="white",bg="#11719e")
    coef_label.place(x=30,y=180)
    coef=Entry(fenetre_liste,textvariable=IntVar(),width=23,bg="#11719e",fg="white")
    coef.place(x=140,y=180)
    resultatlabel=Label(fenetre_liste,text="Moyenne generale classe:",fg="white",bg="#11719e")
    resultatlabel.place(x=50,y=220)
    resultat=Entry(fenetre_liste,textvariable=IntVar(),width=23,bg="#11719e",fg="white")
    resultat.place(x=197,y=220)
    def calcul_note():
        moyen_intero=int(float(intero1.get()))+int(float(intero2.get()))+int(float(intero3.get()))+int(float(intero4.get()))
        moyendev=int(float(Note_devoir1.get()))+int(float(Note_devoir2.get()))
        moyen_gen_cls=(moyen_intero+moyendev)/int(float(coef.get()))
        resultat.insert(INSERT,moyen_gen_cls)
        showinfo(title="Validation Reussi",message="Moyenne CALCULE")
    def supprimer():
        interog1=intero1.delete(0,END)
        interog2=intero2.delete(0,END)
        interog3=intero3.delete(0,END)
        interog4=intero4.delete(0,END)
        Note_dev1=Note_devoir1.delete(0,END)
        Note_dev2=Note_devoir2.delete(0,END)
        coefmat=coef.delete(0,END)
        resultatgen=resultat.delete(0,END)
    boutton_calcul=Button(fenetre_liste, text="calculer la moyenne de classe ", width=26, height=1,bg="#FF6800",fg="white",command=calcul_note)
    boutton_calcul.place(x=155,y=240)

    boutton_del=Button(fenetre_liste, text="supprimer", width=15, height=1,bg="#FF6800",fg="white",command=supprimer)
    boutton_del.place(x=360,y=240)
        
def liste_prof_mat():
      
    fenetre_liste=Toplevel(window)
    fenetre_liste.title("Listes des profs et leurs matieres")
    fenetre_liste.geometry("490x300")
    fenetre_liste.resizable(width=FALSE,height=FALSE)
    def afficher():
        db= mysql.connect(
        host= "localhost",
        user= "root",
        password= "",
        database="BULLETIN"
        )

        cursor = db.cursor()
        cursor.execute("SELECT DISTINCT nom_mat,prof_mat FROM matiere")
        fenetre_liste.config(background="#11719e")
        label_liste_prof=Label(fenetre_liste, text="Listes des profs et leurs matieres",fg="white",bg="#11719e")
        f = font.Font(family='Footlight MT Light', size=12, weight="bold")
        label_liste_prof["font"]=f
        label_liste_prof.place(x=120,y=0)
        rows=cursor.fetchall()
        for i,(nom,moyennegenerale) in enumerate(rows,start=1):
            listbox.insert("","end",values=( nom,moyennegenerale))
            db.close()

    cols=("Nom Matiere","Proffesseur Enseignant")
    listbox = ttk.Treeview(fenetre_liste,columns=cols,show="headings")

    for col in cols:
        listbox.heading(col, text=col)
        listbox.grid(row=1,column=0,columnspan=3)
        listbox.heading(col, text=col)
        listbox.place(x=43,y=34)
            
    afficher()
            
def infos():
      
    fenetre_liste=Toplevel(window)
    fenetre_liste.title("Infos Eleve")
    fenetre_liste.geometry("1200x700")
    fenetre_liste.iconbitmap("etudiant.ico")
    fenetre_liste.config(background="#11719e")
    
    def afficher():
        db= mysql.connect(
        host= "localhost",
        user= "root",
        password= "",
        database="BULLETIN"
        )

        cursor = db.cursor()
        cursor.execute("SELECT nom,nom_mat,moyclass,notecompo,moygen,rang,appreciation FROM Matiere,Eleve Where Matiere.id_eleve=Eleve.id_eleve")
        fenetre_liste.config(background="#11719e")
        label_liste_mat=Label(fenetre_liste, text="Listes des Eleves Et Informations",fg="white",bg="#11719e")
        f = font.Font(family='Freestyle Script', size=24, weight="bold")
        label_liste_mat["font"]=f
        label_liste_mat.place(x=510,y=0)
        rows=cursor.fetchall()
        for i,(nom,nom_mat,moyclass,notecompo,moygen,rang,appreciation)in enumerate(rows,start=1):
            listbox.insert("","end",values=(nom,nom_mat,moyclass,notecompo,moygen,rang,appreciation))
            db.close()
    cols=("Nom eleve","Nom Matiere","Note de compo","Moyenne classe","Moyen General","Rang","Appreciation")
    listbox = ttk.Treeview(fenetre_liste,columns=cols,show="headings",height=30)

    for col in cols:
        listbox.heading(col, text=col)
        listbox.grid(row=1,column=0,columnspan=1)
        listbox.heading(col, text=col)
        listbox.place(x=0,y=42)
            
    afficher()

def mat1():
    nommat=disci1.get()
    moyclas=moycls1.get()
    note_exam=exam1.get()
    moygenera=moygen1.get()
    coefficient=coeff1.get()
    rang=rang1.get()                       
    proffesseur=prof1.get()
    apreciation=apre1.get()
    id_eleve=idselect.get()
    id_mat=idselect2.get()
    insertion="INSERT INTO Matiere(id_mat,nom_mat,moyclass,notecompo,moygen,coef,rang,prof_mat,appreciation,id_eleve)VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
    valeurs=(id_mat,nommat,moyclas,note_exam,moygenera,coefficient,rang,proffesseur,apreciation,id_eleve)
    cursor.execute(insertion, valeurs)
    showinfo(title="validation reusie",message="Matiere bien enregistré")
    db.commit()

def mat2():
    nommat=disci2.get()
    moyclas=moycls2.get()
    note_exam=exam2.get()
    moygenera=moygen2.get()
    coefficient=coeff2.get()
    rang=rang2.get()                       
    proffesseur=prof2.get()
    apreciation=apre2.get()
    id_eleve=idselect.get()
    id_mat=idselect2.get()
    insertion="INSERT INTO Matiere(id_mat,nom_mat,moyclass,notecompo,moygen,coef,rang,prof_mat,appreciation,id_eleve)VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
    valeurs=(id_mat,nommat,moyclas,note_exam,moygenera,coefficient,rang,proffesseur,apreciation,id_eleve)
    cursor.execute(insertion, valeurs)
    showinfo(title="validation reusie",message="Matiere bien enregistré")
    db.commit()
    
def mat3():
    nommat=disci3.get()
    moyclas=moycls3.get()
    note_exam=exam3.get()
    moygenera=moygen3.get()
    coefficient=coeff3.get()
    rang=rang3.get()                       
    proffesseur=prof3.get()
    apreciation=apre3.get()
    id_eleve=idselect.get()
    id_mat=idselect2.get()
    insertion="INSERT INTO Matiere(id_mat,nom_mat,moyclass,notecompo,moygen,coef,rang,prof_mat,appreciation,id_eleve)VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
    valeurs=(id_mat,nommat,moyclas,note_exam,moygenera,coefficient,rang,proffesseur,apreciation,id_eleve)
    cursor.execute(insertion, valeurs)
    showinfo(title="validation reusie",message="Matiere bien enregistré")
    db.commit()


def mat4():
    nommat=disci4.get()
    moyclas=moycls4.get()
    note_exam=exam4.get()
    moygenera=moygen4.get()
    coefficient=coeff4.get()
    rang=rang4.get()                       
    proffesseur=prof4.get()
    apreciation=apre4.get()
    id_eleve=idselect.get()
    id_mat=idselect2.get()
    insertion="INSERT INTO Matiere(id_mat,nom_mat,moyclass,notecompo,moygen,coef,rang,prof_mat,appreciation,id_eleve)VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
    valeurs=(id_mat,nommat,moyclas,note_exam,moygenera,coefficient,rang,proffesseur,apreciation,id_eleve)
    cursor.execute(insertion, valeurs)
    showinfo(title="validation reusie",message="Matiere bien enregistré")
    db.commit()

def mat5():
    nommat=disci5.get()
    moyclas=moycls5.get()
    note_exam=exam5.get()
    moygenera=moygen5.get()
    coefficient=coeff5.get()
    rang=rang5.get()                       
    proffesseur=prof5.get()
    apreciation=apre5.get()
    id_eleve=idselect.get()
    id_mat=idselect2.get()
    insertion="INSERT INTO Matiere(id_mat,nom_mat,moyclass,notecompo,moygen,coef,rang,prof_mat,appreciation,id_eleve)VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
    valeurs=(id_mat,nommat,moyclas,note_exam,moygenera,coefficient,rang,proffesseur,apreciation,id_eleve)
    cursor.execute(insertion, valeurs)
    showinfo(title="validation reusie",message="Matiere bien enregistré")
    db.commit()

def mat6():
    nommat=disci6.get()
    moyclas=moycls6.get()
    note_exam=exam6.get()
    moygenera=moygen6.get()
    coefficient=coeff6.get()
    rang=rang6.get()                       
    proffesseur=prof6.get()
    apreciation=apre6.get()
    id_eleve=idselect.get()
    id_mat=idselect2.get()
    insertion="INSERT INTO Matiere(id_mat,nom_mat,moyclass,notecompo,moygen,coef,rang,prof_mat,appreciation,id_eleve)VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
    valeurs=(id_mat,nommat,moyclas,note_exam,moygenera,coefficient,rang,proffesseur,apreciation,id_eleve)
    cursor.execute(insertion, valeurs)
    showinfo(title="validation reusie",message="Matiere bien enregistré")
    db.commit()

def mat7():
    nommat=disci7.get()
    moyclas=moycls7.get()
    note_exam=exam7.get()
    moygenera=moygen7.get()
    coefficient=coeff7.get()
    rang=rang7.get()                       
    proffesseur=prof7.get()
    apreciation=apre7.get()
    id_eleve=idselect.get()
    id_mat=idselect2.get()
    insertion="INSERT INTO Matiere(id_mat,nom_mat,moyclass,notecompo,moygen,coef,rang,prof_mat,appreciation,id_eleve)VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
    valeurs=(id_mat,nommat,moyclas,note_exam,moygenera,coefficient,rang,proffesseur,apreciation,id_eleve)
    cursor.execute(insertion, valeurs)
    showinfo(title="validation reusie",message="Matiere bien enregistré")
    db.commit()
def mat8():
    nommat=disci8.get()
    moyclas=moycls8.get()
    note_exam=exam8.get()
    moygenera=moygen8.get()
    coefficient=coeff8.get()
    rang=rang8.get()                       
    proffesseur=prof8.get()
    apreciation=apre8.get()
    id_eleve=idselect.get()
    id_mat=idselect2.get()
    insertion="INSERT INTO Matiere(id_mat,nom_mat,moyclass,notecompo,moygen,coef,rang,prof_mat,appreciation,id_eleve)VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
    valeurs=(id_mat,nommat,moyclas,note_exam,moygenera,coefficient,rang,proffesseur,apreciation,id_eleve)
    cursor.execute(insertion, valeurs)
    showinfo(title="validation reusie",message="Matiere bien enregistré")
    db.commit()

def mat9():
    nommat=disci9.get()
    moyclas=moycls9.get()
    note_exam=exam9.get()
    moygenera=moygen9.get()
    coefficient=coeff9.get()
    rang=rang9.get()                       
    proffesseur=prof9.get()
    apreciation=apre9.get()
    id_eleve=idselect.get()
    id_mat=idselect2.get()
    insertion="INSERT INTO Matiere(id_mat,nom_mat,moyclass,notecompo,moygen,coef,rang,prof_mat,appreciation,id_eleve)VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
    valeurs=(id_mat,nommat,moyclas,note_exam,moygenera,coefficient,rang,proffesseur,apreciation,id_eleve)
    cursor.execute(insertion, valeurs)
    showinfo(title="validation reusie",message="Matiere bien enregistré")
    db.commit()

def mat10():
    nommat=disci10.get()
    moyclas=moycls10.get()
    note_exam=exam10.get()
    moygenera=moygen10.get()
    coefficient=coeff10.get()
    rang=rang10.get()                       
    proffesseur=prof10.get()
    apreciation=apre10.get()
    id_eleve=idselect.get()
    id_mat=idselect2.get()
    insertion="INSERT INTO Matiere(id_mat,nom_mat,moyclass,notecompo,moygen,coef,rang,prof_mat,appreciation,id_eleve)VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
    valeurs=(id_mat,nommat,moyclas,note_exam,moygenera,coefficient,rang,proffesseur,apreciation,id_eleve)
    cursor.execute(insertion, valeurs)
    showinfo(title="validation reusie",message="Matiere bien enregistré")
    db.commit()

def mat11():
    nommat=disci11.get()
    moyclas=moycls11.get()
    note_exam=exam11.get()
    moygenera=moygen11.get()
    coefficient=coeff11.get()
    rang=rang11.get()                       
    proffesseur=prof11.get()
    apreciation=apre11.get()
    id_eleve=idselect.get()
    id_mat=idselect2.get()
    insertion="INSERT INTO Matiere(id_mat,nom_mat,moyclass,notecompo,moygen,coef,rang,prof_mat,appreciation,id_eleve)VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
    valeurs=(id_mat,nommat,moyclas,note_exam,moygenera,coefficient,rang,proffesseur,apreciation,id_eleve)
    cursor.execute(insertion, valeurs)
    showinfo(title="validation reusie",message="Matiere bien enregistré")
    db.commit()
    
def enregistrer():
    neweleve=Eleve(nom.get(),prenom.get(),sexe.get(),naissance.get(),lieu.get(),numero.get(),sta.get(),classe.get(),anne.get(),decou.get())
    listenom.append(nom.get())
    listeprenom.append(prenom.get())
    listesexe.append(sexe.get())
    listenaiss.append(naissance.get())
    listelieu.append(lieu.get())
    listenum.append(numero.get())
    listesta.append(sta.get())
    listeclasse.append(classe.get())
    listeanne.append(anne.get())
    listedecou.append(decou.get())
    liste_elevetab.append(neweleve)
    insertion="INSERT INTO ELEVE(nom,prenom,sexe,naissance,lieu,numero,statut,classe,anne,decou)VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
    valeurs=(nom.get(),prenom.get(),sexe.get(),naissance.get(),lieu.get(),numero.get(),sta.get(),classe.get(),anne.get(),decou.get())
    cursor.execute(insertion, valeurs)
    db.commit()
    showinfo(title="validation reusie",message="Eleve bien enregistré")

def supenre():
    nom1=nom.delete(0,END)
    prenom1=prenom.delete(0,END)
    sexe1=sexe.delete(0,END)
    naissance1=naissance.delete(0,END)
    lieu1=lieu.delete(0,END)
    num=numero.delete(0,END)
    sta1=sta.delete(0,END)
    classe1=classe.delete(0,END)
    anne1=anne.delete(0,END)
    decou1=decou.delete(0,END)
    effectif1=effectif.delete(0,END)
def id_mat():
    fenetre_liste=Toplevel(window)
    fenetre_liste.title("Matieres et Id Correspondants")
    fenetre_liste.geometry("280x300")
    #fenetre_liste.iconbitmap("icone.ico")
    #fenetre_liste.iconbitmap("ico1.ico")
    fenetre_liste.config(background="#11719e")
    fenetre_liste.resizable(width=FALSE,height=FALSE)
    facture =Text(fenetre_liste, height = 16,width = 28,fg="black",bg="white",bd=3)
    f = font.Font(family='Footlight MT Light', size=12)
    facture["font"]=f
    facture.insert(END,"      Matieres et Id correspondants")
    facture.insert(END,"\n")
    facture.insert(END,"\n")
    facture.insert(END,"\tMatiere 1: id=1")
    facture.insert(END,"\n")
    facture.insert(END,"\tMatiere 2: id=2")
    facture.insert(END,"\n")
    facture.insert(END,"\tMatiere 3: id=3")
    facture.insert(END,"\n")
    facture.insert(END,"\tMatiere 4: id=4")
    facture.insert(END,"\n")
    facture.insert(END,"\tMatiere 5: id=5")
    facture.insert(END,"\n")
    facture.insert(END,"\tMatiere 6: id=6")
    facture.insert(END,"\n")
    facture.insert(END,"\tMatiere 7: id=7")
    facture.insert(END,"\n")
    facture.insert(END,"\tMatiere 8: id=8")
    facture.insert(END,"\n")
    facture.insert(END,"\tMatiere 9: id=9")
    facture.insert(END,"\n")
    facture.insert(END,"\tMatiere 10: id=10")
    facture.insert(END,"\n")
    facture.insert(END,"\tMatiere 11: id=11")
    facture.place(x=10,y=0)
    
def classement():
      
    fenetre_liste=Toplevel(window)
    fenetre_liste.title("classement des eleves")
    fenetre_liste.geometry("490x300")
    #fenetre_liste.iconbitmap("icone.ico")
    #fenetre_liste.iconbitmap("ico1.ico")
    fenetre_liste.config(background="#11719e")
    fenetre_liste.resizable(width=FALSE,height=FALSE)
    

    
    def afficher():
        db= mysql.connect(
        host= "localhost",
        user= "root",
        password= "",
        database="BULLETIN"
        )

        cursor = db.cursor()

        cursor.execute("SELECT nom,moyennegenerale FROM moyengen,eleve WHERE moyengen.id_eleve=eleve.id_eleve ORDER BY moyennegenerale DESC")
        label_liste_eleve=Label(fenetre_liste, text="Classement De La Plus Grande Moyenne A la Plus Petite",fg="white",bg="#11719e")
        f = font.Font(family='Freestyle Script', size=20, weight="bold")
        label_liste_eleve["font"]=f
        label_liste_eleve.place(x=13,y=0)
        rows=cursor.fetchall()
        for i,(nom,moyennegenerale) in enumerate(rows,start=1):
            listbox.insert("","end",values=( nom,moyennegenerale))
            db.close()

    cols=("nom","moyenne generale")
    listbox = ttk.Treeview(fenetre_liste,columns=cols,show="headings")

    for col in cols:
        listbox.heading(col, text=col)
        listbox.grid(row=1,column=0,columnspan=3)
        listbox.heading(col, text=col)
        listbox.place(x=43,y=40)
        
    afficher()
        
    
bouttonenregis=Button(window, text="Enregistrer l Eleve", width=14, height=1,bg="#FF6800",fg="white",command=enregistrer)
bouttonenregis.place(x=150,y=160)

bouttonsupenre=Button(window, text="Effacer les valeurs", width=14, height=1,bg="#FF6800",fg="white",command=supenre)
bouttonsupenre.place(x=150,y=200) 

bouttonmoyenne=Button(window, text="Moyenne", width=13, height=1,bg="#FF6800",fg="white",command=calculer_moy)
bouttonmoyenne.place(x=1120,y=655) 
        
bouttonmat1=Button(window, text="valider matiere 1", width=13, height=1,bg="#FF6800",fg="white",command=mat1)
bouttonmat1.place(x=155,y=350)

bouttonmat2=Button(window, text="valider matiere 2", width=13, height=1,bg="#FF6800",fg="white",command=mat2)
bouttonmat2.place(x=155,y=375)

bouttonmat3=Button(window, text="valider matiere 3", width=13, height=1,bg="#FF6800",fg="white",command=mat3)
bouttonmat3.place(x=155,y=400)

bouttonmat4=Button(window, text="valider matiere 4", width=13, height=1,bg="#FF6800",fg="white",command=mat4)
bouttonmat4.place(x=155,y=450)

bouttonmat5=Button(window, text="valider matiere 5", width=13, height=1,bg="#FF6800",fg="white",command=mat5)
bouttonmat5.place(x=155,y=475)

bouttonmat6=Button(window, text="valider matiere 6", width=13, height=1,bg="#FF6800",fg="white",command=mat6)
bouttonmat6.place(x=155,y=500)

bouttonmat7=Button(window, text="valider matiere 7", width=13, height=1,bg="#FF6800",fg="white",command=mat7)
bouttonmat7.place(x=155,y=525)

bouttonmat8=Button(window, text="valider matiere 8", width=13, height=1,bg="#FF6800",fg="white",command=mat8)
bouttonmat8.place(x=155,y=575)

bouttonmat9=Button(window, text="valider matiere 9", width=13, height=1,bg="#FF6800",fg="white",command=mat9)
bouttonmat9.place(x=155,y=600)
menuprinci=Menu(window,tearoff=0)

bouttonmat10=Button(window, text="valider matiere 10", width=13, height=1,bg="#FF6800",fg="white",command=mat10)
bouttonmat10.place(x=155,y=625)

bouttonmat11=Button(window, text="valider matiere 11", width=13, height=1,bg="#FF6800",fg="white",command=mat11)
bouttonmat11.place(x=155,y=650)

menuprinci=Menu(window,tearoff=0)

menu_afficher=Menu(menuprinci,tearoff=0)
menuprinci.add_cascade(label="Afficher",menu=menu_afficher)
menu_afficher.add_command(label="Listes des Eleves Enregistrés",command=liste_eleve)
menu_afficher.add_command(label="Listes des Profs et Matieres Enregistrés",command=liste_prof_mat)
menu_afficher.add_command(label="Afficher l Id des Matieres",command=id_mat)

menu_noteclass=Menu(menuprinci,tearoff=0)
menuprinci.add_cascade(label="Calculer la note de classe",menu=menu_noteclass)
menu_noteclass.add_command(label="Effectuer Calcul",command=noteclass)

menu_moy=Menu(menuprinci,tearoff=0)
menuprinci.add_cascade(label="Calculer la Moyenne Generale",menu=menu_moy)
menu_moy.add_command(label="Effectuer Calcul",command=notegen)


menu_classmt=Menu(menuprinci,tearoff=0)
menuprinci.add_cascade(label="Classement des eleves",menu=menu_classmt)
menu_classmt.add_command(label="Voir le classement des Eleves Enregistrés",command=classement)

menu_calcu=Menu(menuprinci,tearoff=0)
menuprinci.add_cascade(label="Effectuer Operations",menu=menu_calcu)
menu_calcu.add_command(label="Calculatrice",command=calculatrice)

menu_infos=Menu(menuprinci,tearoff=0)
menuprinci.add_cascade(label="Informations",menu=menu_infos)
menu_infos.add_command(label="Informations des Eleves",command=infos)

menu_quitter=Menu(menuprinci,tearoff=0)
menuprinci.add_cascade(label="Sortir de L application",menu=menu_quitter)
menu_quitter.add_command(label="Quitter",command=window.quit)
window.config(menu=menuprinci)
window.mainloop()
