from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def main():
     dane = {'tytul':'Strona główna', 'tresc':'Strona Główna!'}
     return render_template('index.html', tytul=dane['tytul'], tresc=dane['tresc'])

	
@app.route("/about")
def about():
     dane = {'tytul':'O mnie', 'tresc':'Karol Janowicz - Student'}
     return render_template('omnie.html', tytul=dane['tytul'], tresc=dane['tresc'])

@app.route('/info')
def info():
    posty = [
        {
         'author': {'username': 'Karol'},
         'body': 'Post1'
        },
        {
         'author': {'username': 'Jan'}, 
         'body': 'Post2'
    }]
    dane = {'tytul':'Informacje', 'tresc':'Lorem ipsum dolor sit met.'}
    return render_template('info.html', tytul=dane['tytul'], tresc=dane['tresc'], posty=posty)
 
@app.route("/kontent")
def kontent():
     dane = {'tytul':'Kontent', 'tresc':'Content'}
     return render_template('kontent.html', tytul=dane['tytul'], tresc=dane['tresc'])
	
if __name__ == "__main__":
	app.run()
