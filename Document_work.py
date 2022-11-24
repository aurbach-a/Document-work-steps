import sqlite3
from tkinter import *
from tkinter import messagebox
from datetime import date,datetime,timedelta 
import time
import numpy as np
import matplotlib.pyplot as plt

#Verbindungspfad zur Datenbankdatei'
db_pfad = 'Arbeitsschritte.db'

#Ausführen einer Aufgabe bei Auswahl des Buttons
def button_action0():
        # Create a GUI window Menüauswahl Kategorie hinzufügen
        def read_sub_kategorie():
	        #Kategorien einlesen und in die Listbox übergeben
                verbindung2 = sqlite3.connect(db_pfad)
                kategorie_zeiger = verbindung2.cursor()
                sql_anweisung = """SELECT Name FROM Kategorie;"""
                kategorie_zeiger = verbindung2.cursor()
                kategorie_zeiger.execute(sql_anweisung)
                my_kategorie=[]
                # my_kategorie.append("Kategorie")
                for i in kategorie_zeiger:
                        my_kategorie.append(i[0])        
                        #print(kategorie_zeiger(i))
                verbindung2.close()
                #print("Katagogien:",my_kategorie)
                #Listbox leeren und neu füllen
                listaction0.delete(0, END)
                listaction0.insert(0, *my_kategorie)
        
        def Kategorie_write():
                #wert aus Eingabefeld holen
                var_write_kategorie = Kategorie_txt.get()
                if var_write_kategorie > "":
                        kategorie_sql = "INSERT INTO 'Kategorie' ('Name') VALUES ('"
                        kategorie_sql = kategorie_sql + str(var_write_kategorie) +"');"
                        #ausführen der SQL-Anweisung 
                        #print("SQL_Kategorietext:", kategorie_sql)
                        verbindung2 = sqlite3.connect(db_pfad)
                        kategorie_zeiger = verbindung2.cursor()
                        kategorie_zeiger.execute(kategorie_sql)
                        verbindung2.commit()
                        verbindung2.close()
                        read_sub_kategorie()
                        read_main_kategorie()
                else:
                        messagebox.showinfo(message="keine Kategorie eingetragen", title = "Information")

        # #print("Hier können Kategorien hinzugefügt werden.")
        # Create a GUI window Menüauswahl Kategorie hinzufügen
        action0gui = Tk()
     
        # Set the background colour of GUI window
        #action0gui.config(background = "white")
 
        # set the name of tkinter GUI window
        action0gui.title("Kategorie hinzufügen")
 
        # Set the configuration of GUI window
        action0gui.geometry("350x250")
        #Kategorien eingabe
        Kategorie_lbl = Label(action0gui,  text="Neue Kategorie:")
        Kategorie_lbl.config(justify ="right", border = 5, background = "beige")
        #positon label
        Kategorie_lbl.grid(column = 1, row = 1)
        Kategorie_txt = Entry(action0gui, width=20)
        Kategorie_txt.grid(column =2, row =1) 
        Kategorie_btn = Button(action0gui, text = "Kategorie hinzufügen" , fg = "Black", command=Kategorie_write)
        #lage des Button
        Kategorie_btn.grid(column=2, row=2)
        # This is the section of code which creates a listbox
        listaction0=Listbox(action0gui, bg=fa_da, font=('arial', 10, 'normal'), width=20, height=10)
        #Lage der Listbox
        listaction0.grid(column = 1, row =3)
        # Create a Exit Button and attached to exit function
        Verlassen = Button(action0gui, text = "Menü Verlassen", fg = "Black",  border = 3, command = action0gui.destroy)
        Verlassen.grid(column = 2, row = 3)
        read_sub_kategorie()
#********************************************************************************************************
def button_action1():
        # Create a GUI window Menüauswahl Kategorie ändern
        def read_sub_kategorie():
	        #Kategorien einlesen und in die Listbox übergeben
                verbindung2 = sqlite3.connect(db_pfad)
                kategorie_zeiger = verbindung2.cursor()
                sql_anweisung = """SELECT Name FROM Kategorie;"""
                kategorie_zeiger = verbindung2.cursor()
                kategorie_zeiger.execute(sql_anweisung)
                my_kategorie=[]
                # my_kategorie.append("Kategorie")
                for i in kategorie_zeiger:
                        my_kategorie.append(i[0])        
                        #print(kategorie_zeiger(i))
                verbindung2.close()
                #print("Katagogien:",my_kategorie)
                #Listbox leeren und neu füllen
                ltb_Kategorie.delete(0, END)
                ltb_Kategorie.insert(0, *my_kategorie)
        
        def Kategorie_update():
                if (var_str_lbl_Kategorie.get()) == "Kategorie wählen":
                        messagebox.showinfo(message="keine zu ändernte Kategorie ausgewählt", title = "Information")
                else:
                        #wert aus Eingabefeld holen
                        if (enty_txt_Kategorie.get()) > "":
                                kategorie_sql = "UPDATE Kategorie SET Name = '" + str(enty_txt_Kategorie.get()) + "' WHERE Name = '"
                                kategorie_sql = kategorie_sql + (var_str_lbl_Kategorie.get()) +"';"
                                #ausführen der SQL-Anweisung 
                                #print("SQL_Kategorietext:", kategorie_sql)
                                verbindung2 = sqlite3.connect(db_pfad)
                                kategorie_zeiger = verbindung2.cursor()
                                kategorie_zeiger.execute(kategorie_sql)
                                verbindung2.commit()
                                verbindung2.close()
                                read_sub_kategorie()
                                read_main_kategorie()
                        else:
                                messagebox.showinfo(message="keine Kategorie eingetragen", title = "Information")
        #auswahl aus Listbaox übergeben
        def btn_listboxselect():
                ltb_select = ltb_Kategorie.curselection()
                item_ltb_select = ltb_select [0]
                nameAusgewaehlt = ltb_Kategorie.get(item_ltb_select)
                #textBegruessung = 'Hallo ' + nameAusgewaehlt +'!'
                (var_str_lbl_Kategorie.set(nameAusgewaehlt))
                #labelText.config(text=textBegruessung)

        # #print("Hier können Kategorien geaendert werden.")
        # Create a GUI window Menüauswahl Kategorie ändern
        action1gui = Tk()
     
        # Set the background colour of GUI window
        #action0gui.config(background = "white")
 
        # set the name of tkinter GUI window
        action1gui.title("Kategorie geaendert")
 
        # Set the configuration of GUI window
        action1gui.geometry("450x270")
        #Kategorien eingabe
        var_str_lbl_Kategorie = StringVar(action1gui)
        lbl_Kategorie_change = Label(action1gui,  text=" zu ändernte Kategorie:")
        lbl_Kategorie_select = Label(action1gui, textvariable=var_str_lbl_Kategorie)
        lbl_Kategorie_info= Label(action1gui,  text="wird zu")
        lbl_Kategorie_change.config(justify ="right", border = 5, background = "beige")
        #positon label
        lbl_Kategorie_change.grid(column = 1, row = 1)
        lbl_Kategorie_select.grid(column = 2, row = 1)
        lbl_Kategorie_info.grid(column = 3, row = 1)
        enty_txt_Kategorie = Entry(action1gui, width=20)
        enty_txt_Kategorie.grid(column =4, row =1)
        # declare Button
        Kategorieselect_btn = Button(action1gui, text = "Kategorie auswählen" , fg = "Black", command=btn_listboxselect)
        Kategorie_btn = Button(action1gui, text = "Kategorie aendern" , fg = "Black", command=Kategorie_update)
        # positon Button
        Kategorieselect_btn.grid(column=2, row=2)
        Kategorie_btn.grid(column=4, row=2)
        # This is the section of code which creates a listbox
        ltb_Kategorie=Listbox(action1gui, bg=fa_da, font=('arial', 10, 'normal'), width=20, height=10)
        
        # link a scrollbar to a list
        scrollbar = Scrollbar(action1gui)
        #position der srollbar neben die listbox (ltb_Kategorie) hoehe von Nord bis Sued und West angelehnt
        scrollbar.grid(column = 2, row =3, sticky=N+S+W)
        # Attaching Listbox to Scrollbar
        # Since we need to have a vertical 
        # scroll we use yscrollcommand
        ltb_Kategorie.config(yscrollcommand = scrollbar.set)
  
        # setting scrollbar command parameter 
        # to listbox.yview method its yview because
        # we need to have a vertical view
        scrollbar.config(command = ltb_Kategorie.yview, orient='vertical',)
        
        #Lage der Listbox
        ltb_Kategorie.grid(column = 1, row =3)
        # Create a Exit Button and attached to exit function
        Verlassen = Button(action1gui, text = "Menü Verlassen", fg = "Black",  border = 3, command = action1gui.destroy)
        Verlassen.grid(column = 1, row = 4)
        (var_str_lbl_Kategorie.set("Kategorie wählen"))
        read_sub_kategorie()
#********************************************************************************************************
def button_action2():
        # Create a GUI window Menüauswahl Kategorie entfernen
        def read_sub_kategorie():
	        #Kategorien einlesen in OptionMenue
                verbindung2 = sqlite3.connect(db_pfad)
                kategorie_zeiger = verbindung2.cursor()
                sql_anweisung = """SELECT * FROM Kategorie;"""
                kategorie_zeiger = verbindung2.cursor()
                kategorie_zeiger.execute(sql_anweisung)
                result_kategorie = kategorie_zeiger.fetchall()
                var_read_kategorie = []
                #print(result_kategorie)
                # var_del_kategorie.append("Kategorie") an OptionMenu
                for i in range(len(result_kategorie)):
                        var_read_kategorie.append(result_kategorie[i][1])
                #print(var_del_kategorie)
                verbindung2.close()
                var_del_kategorie.set(var_read_kategorie[0])
                txtd = OptionMenu(action2gui, var_del_kategorie, *var_read_kategorie)
                txtd.config(width=7, font=('Helvetica', 10))
                txtd.grid(column = 1, row =2)
                #print("Katagogien:",my_kategorie)

        
        def Kategorie_delete():
                if (var_del_kategorie.get()) == "Kategorie wählen":
                        messagebox.showinfo(message="keine zu entfernenten Kategorie gewählt", title = "Information")
                else:
                        verbindung2 = sqlite3.connect(db_pfad)
                        kategorie_zeiger = verbindung2.cursor()
                        kategorie_sql= "Select Count(*) from Arbeitsschritte Where KategorieID = (SELECT ID From Kategorie WHERE Name = '" + str(var_del_kategorie.get()) + "');"
                        kategorie_zeiger.execute(kategorie_sql)
                        result = kategorie_zeiger.fetchone();
                        #print("Ergebnis", result)
                        if result[0] > 0:
                                messagebox.showinfo(message="Kategorien sind noch mit " + str(result[0]) + " Datensätzen verknüpft", title = "Verknüpfungen noch vorhanden")
                        else:
                                kategorie_sql = "DELETE FROM Kategorie WHERE Name = '" + str(var_del_kategorie.get()) +"';"
                                #ausführen der SQL-Anweisung 
                                #print("SQL_Kategorietext:", kategorie_sql)
                                verbindung2 = sqlite3.connect(db_pfad)
                                kategorie_zeiger = verbindung2.cursor()
                                kategorie_zeiger.execute(kategorie_sql)
                                verbindung2.commit()
                                verbindung2.close()
                                read_sub_kategorie()
                                read_main_kategorie()
 
        # #print("Hier können Kategorien entfernt werden.")
        # Create a GUI window Menüauswahl Kategorie entfernen action2gui
        action2gui = Tk()
     
        # Set the background colour of GUI window
        #action0gui.config(background = "white")
 
        # set the name of tkinter GUI window
        action2gui.title("Kategorie geaendert")
 
        # Set the configuration of GUI window
        action2gui.geometry("450x270")
        #Kategorien eingabe
        #Kategorie
        #variable setzen
        var_del_kategorie = StringVar(action2gui)
        read_sub_kategorie()

        lbl_Kategorie_delete = Label(action2gui,  text=" zu ändernde Kategorie auswählen:")
        lbl_Kategorie_delete.config(justify ="right", border = 5, background = "beige")
        #positon label
        lbl_Kategorie_delete.grid(column = 1, row = 1)
        # declare Button
        btn_delete_kategorie = Button(action2gui, text = "Kategorie entfernen" , fg = "Black", command=Kategorie_delete)
        # positon Button
        btn_delete_kategorie.grid(column=3, row=2)
         
        # Create a Exit Button and attached to exit function
        Verlassen = Button(action2gui, text = "Menü Verlassen", fg = "Black",  border = 3, command = action2gui.destroy)
        Verlassen.grid(column = 1, row = 4)
        read_sub_kategorie()
#********************************************************************************************************
def button_action3():
        # Create a GUI window Menüauswahl Kategorie entfernen
        def read_sub_kategorie():
	        #Kategorien einlesen in OptionMenue
                verbindung2 = sqlite3.connect(db_pfad)
                kategorie_zeiger = verbindung2.cursor()
                sql_anweisung = """SELECT * FROM Kategorie;"""
                kategorie_zeiger = verbindung2.cursor()
                kategorie_zeiger.execute(sql_anweisung)
                result_kategorie = kategorie_zeiger.fetchall()
                var_read_kategorie = []
                #print(result_kategorie)
                # Kategorien vorbereiten um an OptionMenu zu übergeben
                for i in range(len(result_kategorie)):
                        var_read_kategorie.append(result_kategorie[i][1])
                #print(var_read_kategorie)
                verbindung2.close()
                
                var_link_kategorie1.set(var_read_kategorie[0])
                txt1 = OptionMenu(action3gui, var_link_kategorie1, *var_read_kategorie)
                txt1.config(width=8, font=('Helvetica', 10))
                txt1.grid(column = 1, row =2)
                #print("Katagogien:",my_kategorie)
                var_link_kategorie2.set(var_read_kategorie[0])
                txt2 = OptionMenu(action3gui, var_link_kategorie2, *var_read_kategorie)
                txt2.config(width=8, font=('Helvetica', 10))
                txt2.grid(column = 3, row =2)

        
        def Kategorie_linking():
                if ((var_link_kategorie1.get()) == "Kategorie wählen") or ((var_link_kategorie2.get()) == "Kategorien auswählen"):
                        messagebox.showinfo(message="beide Kategorie müssen gewählt sein", title = "Information")
                else:
                        verbindung2 = sqlite3.connect(db_pfad)
                        kategorie_zeiger = verbindung2.cursor()
                        kategorie_sql= "Select Count(*) from Arbeitsschritte Where KategorieID = (SELECT ID From Kategorie WHERE Name = '" + str(var_link_kategorie1.get()) + "');"
                        kategorie_zeiger.execute(kategorie_sql)
                        result = kategorie_zeiger.fetchone();
                        #print("Ergebnis", result)
                        if result[0] > 0:
                                messagebox.showinfo(message="Es werden " + str(result[0]) + " Datensätzen neu verknüpft", title = "Verknüpfungen")
                                kategorie_sql = "UPDATE Arbeitsschritte SET KategorieID = (SELECT ID From Kategorie WHERE Name = '" + str(var_link_kategorie2.get()) + "') WHERE KategorieID = "
                                kategorie_sql = kategorie_sql + "(SELECT ID From Kategorie WHERE Name = '" + str(var_link_kategorie1.get()) + "');"
                                #ausführen der SQL-Anweisung 
                                #print("SQL_Kategorietext:", kategorie_sql)
                                verbindung2 = sqlite3.connect(db_pfad)
                                kategorie_zeiger = verbindung2.cursor()
                                kategorie_zeiger.execute(kategorie_sql)
                                verbindung2.commit()
                                verbindung2.close()
                                read_sub_kategorie()
                                read_main_kategorie()
                                action3gui.destroy
                        else:
                                messagebox.showinfo(message="Es gibt keine Datensätze die neu verknüpft werden sollen", title = "Keine Verknüpfungen")
                                action3gui.destroy
 
        # #print("Hier können Kategorien geaendert werden.")
        # Create a GUI window Menüauswahl Kategorie entfernenaction3gui
        action3gui = Tk()
     
        # Set the background colour of GUI window
        #action0gui.config(background = "white")
 
        # set the name of tkinter GUI window
        action3gui.title("Kategorie geaendert")
 
        # Set the configuration of GUI window
        action3gui.geometry("460x200")
        #Kategorien eingabe
        #Kategorie
        #variable setzen
        var_link_kategorie1 = StringVar(action3gui)
        var_link_kategorie2 = StringVar(action3gui)
        read_sub_kategorie()

        lbl_Kategorie_link1 = Label(action3gui,  text=" zu ändernde Kategorien auswählen:")
        lbl_Kategorie_link1.config(justify ="right", border = 5, background = "beige")
        lbl_Kategorie_link2 = Label(action3gui,  text=" wird zu Kategorie:")
        lbl_Kategorie_link2.config(justify ="right", border = 5)
        #positon label
        lbl_Kategorie_link1.grid(column = 1, row = 1)
        lbl_Kategorie_link2.grid(column = 2, row = 2)
        # declare Button
        btn_link_kategorie = Button(action3gui, text = "Kategorie neu verlinken" , fg = "Black", command=Kategorie_linking)
        # positon Button
        btn_link_kategorie.grid(column = 1, row=3)
         
        # Create a Exit Button and attached to exit function
        Verlassen = Button(action3gui, text = "Menü Verlassen", fg = "Black",  border = 3, command = action3gui.destroy)
        Verlassen.grid(column = 1, row = 4)
        read_sub_kategorie()
#********************************************************************************************************
def button_action4():
        print("Hier können Einträge verändert werden.")
#********************************************************************************************************
def button_action5():
        # Create a GUI window Menüauswahl Auswertung
        def Kategorie_auswerten():
                verbindung = sqlite3.connect(db_pfad)
                zeiger = verbindung.cursor()
                sql_anweisung = "SELECT Name, SUM(Worktime) AS Minuten FROM Worktime_VIEW WHERE (Starttime > (CAST(strftime('%s', '"
                sql_anweisung = sql_anweisung + entry_txt_datestart.get() + " 00:00') as integer))) and (Finishtime < (CAST(strftime('%s', '"
                sql_anweisung = sql_anweisung + entry_txt_dateend.get() +" 23:59') as integer))) GROUP BY Name order by Minuten desc;"
                #print(sql_anweisung)
                zeiger.execute(sql_anweisung)
                #data =zeiger.fetchall()
                # Ausgabe des Ergebnisses
                data=[]
                data1=[]
                data2=[]
                data.append("Kategorie | Minuten")
                for i in zeiger:
                        data1.append(str(i[0])) 
                        data2.append((i[1])) 
                        data.append(str(i[0])+" | "+str(i[1]))        
                verbindung.close()
                #print("Data",data)
                #Listbox leeren und neu füllen
                lst_auswert_kategogie.delete(0, END)
                lst_auswert_kategogie.insert(0, *data) 
                #Datenübernahme
                x = np.array(data2)
                label = data1
                #Grafikausgabe
                plt.pie(x, labels=label)
                plt.show()

# Menueaufbau Kategorien auswerten.")
        # Create a GUI window Menüauswahl Kategorie auswerten action5gui
        action5gui = Tk()
     
        # Set the background colour of GUI window
        #action0gui.config(background = "white")
 
        # set the name of tkinter GUI window
        action5gui.title("Kategorie auswerten")
 
        # Set the configuration of GUI window
        action5gui.geometry("600x300")
        #Kategorien eingabe
        #Kategorie
        #variable setzen
        var_link_kategorie1 = StringVar(action5gui)
        var_link_kategorie2 = StringVar(action5gui)
        verbindung = sqlite3.connect(db_pfad)
        zeiger = verbindung.cursor()
        sql_anweisung = "SELECT Date(Beginn) FROM Worktime_VIEW order by Beginn ASC LIMIT 1;"
        zeiger.execute(sql_anweisung)
        data = zeiger.fetchall()
        var_link_kategorie1.set(data)
        sql_anweisung = "SELECT Date(Ende) FROM Worktime_VIEW order by Ende DESC LIMIT 1;"
        zeiger.execute(sql_anweisung)
        data =zeiger.fetchall()
        var_link_kategorie2.set(data)

        lbl_Kategorie_link1 = Label(action5gui,  text="Abfragezeitraum einstellen:")
        lbl_Kategorie_link1.config(justify ="right", border = 5, background = "beige")
        lbl_Kategorie_link2 = Label(action5gui,  text=" bis ")
        lbl_Kategorie_link2.config(justify ="right", border = 5)
        entry_txt_datestart = Entry(action5gui, width=16,textvariable=var_link_kategorie1)
        entry_txt_dateend = Entry(action5gui, width=16,textvariable=var_link_kategorie2)
        
        #positon Entry
        entry_txt_datestart.grid(column =1, row =2)
        entry_txt_dateend.grid(column =3, row =2)  
        #positon label
        lbl_Kategorie_link1.grid(column = 1, row = 1)
        lbl_Kategorie_link2.grid(column = 2, row = 2)
        # This is the section of code which creates a listbox
        lst_auswert_kategogie=Listbox(action5gui, bg=fa_da, font=('arial', 10, 'normal'), width=35, height=0)
        lst_auswert_kategogie.place(x=40, y=120)
        # declare Button
        btn_link_kategorie = Button(action5gui, text = "Kategoriezeiten auswerten" , fg = "Black", command=Kategorie_auswerten)
        # positon Button
        btn_link_kategorie.grid(column = 1, row=3)
         
        # Create a Exit Button and attached to exit function
        Verlassen = Button(action5gui, text = "Menü Verlassen", fg = "Black",  border = 3, command = action5gui.destroy)
        Verlassen.grid(column = 1, row = 8)
#********************************************************************************************************
        
#Textausgabe mit info Button
def action_get_info_dialog():
	m_text = "\
************************\n\
Arbeitsschritte dokumentieren\n\
Autor: Andreas Aurbach\n\
Date: 05.11.2022\n\
Version: 0.03\n\
************************"
	messagebox.showinfo(message=m_text, title = "Infos")

def datenlesen():
        verbindung = sqlite3.connect(db_pfad)
        zeiger = verbindung.cursor()
        sql_anweisung = """SELECT ARS.Beginn
        ,ARS.Ende
        ,ARS.Pause
        ,KA.Name
        ,ARS.Beschreibung
        FROM "Arbeitsschritte" AS ARS
        join Kategorie AS KA ON KA.ID = ARS.KategorieID
        --WHERE ARS.Beginn > '2022-09-14 06:30'
        order by ARS.Beginn DESC 
        LIMIT """ 
        sql_anweisung = sql_anweisung + str(li) + " OFFSET " + str(of) + ";"
        #print(sql_anweisung)
        zeiger.execute(sql_anweisung)
        #data =zeiger.fetchall()
        # Ausgabe des Ergebnisses
        data=[]
        data.append("Beginn_________| Ende__________ |Pause| Kategorie  | Tätigkeit")
        for i in zeiger:
                data.append(i[0]+" | "+i[1]+" | "+i[2]+" | "+i[3]+" | "+i[4])        
        verbindung.close()
        #print("Data",data)
        #Listbox leeren und neu füllen
        listone.delete(0, END)
        listone.insert(0, *data)

def vorblaettern():
        global li
        global of
        li = 20
        of = of + 20
        #print(li,of)
        datenlesen()

def anfang():
        global li
        global of
        li = 20
        of = 0
        datenlesen()
        #print(li,of)

#uebernahme der Werte aus den Auswahlfeldern
def clicked():
        Datenlst[0] = var_auswdate.get()+" "+var_bquarter.get()
        Datenlst[1] = var_auswdate.get()+" "+var_equarter.get()
        Datenlst[2] = var_pause.get()
        Datenlst[3] = var_kategorie.get()
        var_txte = txte.get()
        if var_txte > "":
                Datenlst[4] = var_txte
                #print(Datenlst[0])
                #print(Datenlst[1])
                #print(Datenlst[2])
                #print(Datenlst[3])
                #print(Datenlst[4])
                sql_anweisung = "SELECT ID FROM 'Arbeitsschritte' Where Beginn = '"
                sql_anweisung = sql_anweisung + str(Datenlst[0]) + "' and  Ende = '"
                sql_anweisung = sql_anweisung + str(Datenlst[1]) + "' and Pause = '"
                sql_anweisung = sql_anweisung + str(Datenlst[2]) + "';"
                #ausführen der SQL-Anweisung 
                #print("SQL-Abfrage", sql_anweisung)
                verbindung = sqlite3.connect(db_pfad)
                zeiger = verbindung.cursor()
                zeiger.execute(sql_anweisung)
                abfrageerg = len(zeiger.fetchall())
                verbindung.close()
                #print("Ergebnis abfrageergebnis", abfrageerg)
                if abfrageerg > 0:
                        messagebox.showinfo(message="Zeitbereich besteht schon", title = "Befehl")
                        #exit()
                else:
                        res = "INSERT INTO 'Arbeitsschritte' ('Beginn', 'Ende', 'Pause', 'KategorieID', 'Beschreibung') VALUES ('"
                        res = res + str(Datenlst[0]) + "','" 
                        res = res + str(Datenlst[1]) + "','"
                        res = res + str(Datenlst[2]) + "',(SELECT ID FROM  Kategorie  WHERE Name = '"
                        res = res + str(Datenlst[3]) + "'),'" 
                        res = res + str(Datenlst[4]) +"');"
                        #ausführen der SQL-Anweisung print(res)
                        verbindung = sqlite3.connect(db_pfad)
                        zeiger = verbindung.cursor()
                        zeiger.execute(res)
                        verbindung.commit()
                        verbindung.close()
                        #btn = Button.config(root, text = "erledigt" , fg = "green")
                        #messagebox.showinfo(message="Datensatz eingetragen", title = "Befehl")
                        datenlesen()
        else:
                messagebox.showinfo(message="Beschreibung eingeben", title = "Hinweis")

def read_main_kategorie():
        # im Rootfenster
        verbindung = sqlite3.connect(db_pfad)
        zeiger = verbindung.cursor()
        sql_anweisung = """SELECT * FROM Kategorie AS KA;"""
        zeiger = verbindung.cursor()
        zeiger.execute(sql_anweisung)
        inhalt = zeiger.fetchall()
        my_kategorie = []
        for i in range(len(inhalt)):
                my_kategorie.append(inhalt[i][1]) 
        #print(my_kategorie)
        verbindung.close()
        
        var_kategorie.set(my_kategorie[0])
        txtd = OptionMenu(root, var_kategorie, *my_kategorie)
        txtd.config(width=7, font=('Helvetica', 10))
        txtd.grid(column = 4, row =2) 
        
        


#Datenliste muss vorgefüllt sein um Änderungen darauf zuzulassen
Datenlst = [] #["2022-09-23 15:00", "2022-09-23 15:00", "Pause", "Kategorie", "Beschreibung"]
for i in range (5):
    var_test = i * 15
    Datenlst.append(var_test)
#print(Datenlst)

# *************** Mainmenu ****************** Mainmenu ************************************
root = Tk()
 
root.title("Arbeitsschritte dokumentieren")
root.geometry('1040x480')

# Menüleiste erstellen 
menuleiste = Menu(root)

# Menü Datei und Help erstellen
datei_menu = Menu(menuleiste, tearoff=0)
help_menu = Menu(menuleiste, tearoff=0)

# Beim Klick auf Datei oder auf Help sollen nun weitere Einträge erscheinen.
# Diese werden also zu "datei_menu" und "help_menu" hinzugefügt
datei_menu.add_command(label="Kategorie hinzufügen", command=button_action0)
datei_menu.add_command(label="Kategorie ändern", command=button_action1)
datei_menu.add_command(label="Kategorie entfernen", command=button_action2)
datei_menu.add_command(label="Kategorie umhängen", command=button_action3)
datei_menu.add_command(label="Eintrag ändern", command=button_action4)
datei_menu.add_command(label="Auswertung", command=button_action5)
datei_menu.add_separator() # Fügt eine Trennlinie hinzu
#in IDLE funktioniert  quit per Programm nicht
datei_menu.add_command(label="Exit", command=root.quit)

help_menu.add_command(label="Info!", command=action_get_info_dialog)

# Nun fügen wir die Menüs (Datei und Help) der Menüleiste als
# "Drop-Down-Menü" hinzu
menuleiste.add_cascade(label="Datei", menu=datei_menu)
menuleiste.add_cascade(label="Help", menu=help_menu)

# Die Menüleiste mit den Menüeinrägen noch dem Fenster übergeben und fertig.
root.config(menu=menuleiste)  

# Beschreibungs-Label
my_txtdatum = Label(root, text="Datum:")
my_txta = Label(root, text="Beginn:")
my_txtb = Label(root, text="Ende:")
my_txtc = Label(root, text="Pause:")
my_txtd = Label(root, text="Kategorie:")
my_txte = Label(root, text="Beschreibung:")

#Datum
# my_auswahldatum in Liste schreiben
my_auswdate = []
today = date.today()
#vorhergehende Tage in Liste schreiben
for i in range (12):
    my_auswdate.append(today + timedelta(days=-i))
#positon label
my_txtdatum.grid(column = 0, row = 1)
var_auswdate = StringVar(root)
var_auswdate.set(my_auswdate[0])
txtc = OptionMenu(root, var_auswdate, *my_auswdate)
txtc.config(width=8, font=('Helvetica', 10))
txtc.grid(column =0, row =2) 

#Beginn
# my_quarter in Liste schreiben
time = datetime.now()
aminute = time.minute
last_quarter_minute = 15*(time.minute//15)
#Minuten berechnen die von der aktuellen Zeit abgezogen werden
Abzugtime = aminute-last_quarter_minute
#aktuelle Zeit kuerzen
gekuerztquarter = time - timedelta(minutes= Abzugtime)
# Zeitraum festlegen der ausgewählt werden kann
format_data = "%H:%M"
rangebeginn = datetime.strptime("05:00", format_data)
rangeend = datetime.strptime("19:00", format_data)
#vorhergehende Quarterzeiten berechnen
my_quarter=[]
for i in range (96):
    Abzugminute = i * 15
    fquarter = (gekuerztquarter - timedelta(minutes= Abzugminute)).strftime("%H:%M")
    if (datetime.strptime(fquarter,format_data))>rangebeginn and (datetime.strptime(fquarter,format_data))<rangeend:
        my_quarter.append(fquarter)
    #print(my_quarter[i])
#positon label
my_txta.grid(column = 1, row = 1)

var_bquarter = StringVar(root)
var_bquarter.set(my_quarter[0])
txta = OptionMenu(root, var_bquarter, *my_quarter)
txta.config(width=4, font=('Helvetica', 10))
txta.grid(column =1, row =2) 

#Ende
#positon label
my_txtb.grid(column = 2, row = 1)

var_equarter = StringVar(root)
var_equarter.set(my_quarter[0])
txtb = OptionMenu(root, var_equarter, *my_quarter)
txtb.config(width=4, font=('Helvetica', 10))
txtb.grid(column =2, row =2) 

#Pause
my_pause = ['00:00', '00:15', '00:30', '00:45', '01:00']
#positon label
my_txtc.grid(column = 3, row = 1)
var_pause = StringVar(root)
var_pause.set(my_pause[0])
txtc = OptionMenu(root, var_pause, *my_pause)
txtc.config(width=4, font=('Helvetica', 10))
txtc.grid(column =3, row =2) 

#Kategorie
#positon label
var_kategorie = StringVar(root)
read_main_kategorie()

#Beschreibung
#positon label
my_txte.grid(column = 5, row = 1)
txte = Entry(root, width=100)
txte.grid(column =5, row =2) 

 
btn = Button(root, text = "Datensatz schreiben" , fg = "red", command=clicked)
#lage des Button
btn.grid(column=5, row=3)

#farbe_datenausgabe
fa_da = '#CDC0B0'

# This is the section of code which creates a button für vor und zurückblättern
btn_vor = Button(root, text='vorwärts', bg=fa_da, font=('arial', 10, 'normal'), command=vorblaettern).place(x=900, y=60)

btn_anfang = Button(root, text = 'zum Anfang', bg=fa_da, font=('arial', 10, 'normal'), command=anfang).place(x=800, y=60)

# This is the section of code which creates a listbox
listone=Listbox(root, bg=fa_da, font=('arial', 10, 'normal'), width=135, height=0)
listone.place(x=40, y=90)
#global li
#global of

li = 20
of = 0

datenlesen()

root.mainloop()
