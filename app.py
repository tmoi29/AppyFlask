#Tiffany Moi
#SoftDev1 pd7
#HW04--Fill Up Yer Flask
#2017-09-25

from flask import Flask

app = Flask(__name__)


@app.route('/')
def home():
    ret = "<h1>Hey there!</h1>"
    ret += "I bet you have some homework<br>"
    ret += "Check ya classes:<br>"
    ret += '<ol><li><a href="/espanol">Spanish</a></li>'
    ret += '<li><a href="/economia">Econ</a></li>'
    ret += '<li><a href="/gobierno">Gov</a></li></ol>'
    return ret

@app.route('/espanol')
def espana():
    ret = "<h1>Ver Mas Peliculas!</h1>"
    return ret

@app.route('/economia')
def econ():
    ret = 'Ven <a href="http://keepcalmpaddleon.weebly.com/hes21x---basic-economic-principles.html">aqui</a>!'
    return ret

@app.route('/gobierno')
def gov():
    ret = 'Ven <a href="http://polazzo.com/17-18APUSGOVhw.htm">aqui</a>!'
    return ret
    
if __name__ == '__main__':
    app.debug = True
    app.run()
