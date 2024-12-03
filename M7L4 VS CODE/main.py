#Kütüphaneler
from flask import Flask, render_template,request, redirect
#Veritabanı kütüphanesi
from flask_sqlalchemy import SQLAlchemy
#Speech.py'dan olluşturduğumuz fonksiyonu içeri aktardık.
from speech import speech_fnc


app = Flask(__name__)
#SQLite'a bağlantı
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///diary.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
#Veritabanı oluşturmak
db = SQLAlchemy(app)
#Tablo oluşturmak

#Görev #1. Veritabanı oluşturmak
class Card(db.Model):
    #Gerekli alanları oluşturmak
    #id
    id = db.Column(db.Integer, primary_key=True)
    #Başlık
    title = db.Column(db.String(100), nullable=False)
    #Açıklama
    subtitle = db.Column(db.String(300), nullable=False)
    #Yazı
    text = db.Column(db.Text, nullable=False)

    #Objeyi çıktı olarak vermek
    def __repr__(self):
        return f'<Card {self.id}>'


#Sayfayı çalıştırma
@app.route('/')
def index():
    #Veritabanındaki objeleri çıktı vermek
    #Görev #2. Veritabanındaki objelerin index.html içinde gözükmesini sağlamak
    cards = Card.query.order_by(Card.id).all()

    return render_template('index.html', cards=cards)

#Girdilerin olduğu sayfayı çalıştırma
@app.route('/card/<int:id>')
def card(id):
    #Görev #2. id'sini kullanarak doğru girdiyi göstermek
    card = Card.query.get(id)

    return render_template('card.html', card=card)

#Girdi oluşturma sayfasını çalıştırmak
@app.route('/create')
def create():
    return render_template('create_card.html')

#Girdinin formu 
@app.route('/form_create', methods=['GET','POST'])
def form_create():
    if request.method == 'POST':
        title =  request.form['title']
        subtitle =  request.form['subtitle']
        text =  request.form['text']

        #Veritabanına paslamak için bir obje oluşturmak

        #Görev #2. Veritabanında veri depolamak için bir yöntem
        card = Card(title=title, subtitle=subtitle, text=text)

        db.session.add(card)
        db.session.commit()
        return redirect('/')
    else:
        return render_template('create_card.html')

@app.route("/record_tr")
def record_fnc():
    try:
        text = speech_fnc("tr-TR")
    except:
        text = "Bir şeyler ters gitti, tekrar deneyin."

    return render_template('create_card.html', text=text)

@app.route("/record_en")
def record_fncn():
    try:
        text = speech_fnc("en-GB")
    except:
        text = "Something is wrong, try again."

    return render_template('create_card.html', text=text)

if __name__ == "__main__":
    app.run(debug=True)