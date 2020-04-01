from flask import Flask, render_template, request
import sqlite3
cur = sqlite3.connect("dataflask.db")
c = cur.cursor()

app4 = Flask(__name__)
   
@app4.route('/') 
def menu():
    return render_template("page_menu.html")

@app4.route('/pages', methods=['GET','POST'])
def pages():     
    op_page = request.form["choice_page"]
    if op_page == '1' :
        return render_template('home4.html')
    else: 
        cur = sqlite3.connect('dataflask.db')
        c = cur.cursor()
        c.execute("select * from adherents")
        record= c.fetchall()
        cur.close()
        return render_template('page_consult.html')
 
@app4.route('/text_box',methods=['GET','POST'])
def text_box():
       
    texte_prenom = request.form['userprenom']
    texte_nom = request.form['usernom']
    texte_sexe = request.form["usersexe"]
    texte_pseudo = request.form['userpseudo']
    
    
    if texte_sexe == '2' :
        texte_sexe = 'M.'
    else: texte_sexe = 'Mme.'
        
    c.execute("create table if not exists adherents (prenom varchar, nom varchar, sexe varchar, pseudo varchar)")
    c.execute("select * from adherents")
    record= c.fetchall() 

    for i in record :
       if texte_pseudo in i:
          flash=("Pseudo  "+ texte_pseudo + " non valide!!!")
          return render_template("page3_4exo.html",message=flash)

    c.execute("insert into adherents  values (?,?,?,?)",(texte_prenom,texte_nom,texte_sexe,texte_pseudo))
    cur.commit()
    cur.close()
    texte=(texte_sexe+' '+texte_prenom+' '+texte_nom+' '+'votre nom dutilisateur est :  '+texte_pseudo)
    processed_text = texte
    return render_template("page2_4exo.html", message=processed_text) 


cur.close()   
if __name__ == '__main__':
    app4.run()