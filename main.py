from flask import Flask, render_template, request, jsonify, make_response

server = Flask(__name__, template_folder="./webapp/templates", static_folder="./webapp/static")

@server.route('/', methods=["GET", "POST"])
def home():
    if(request.method == "GET"):
        return render_template("index.html")#Template principal
    if(request.method == "POST"):
        message = request.form["message"]#Guarda el mensaje en la variable message
        print("Message:", message)#Imprime
        return make_response(jsonify({"message": "success"}))#Retorna un "success"

if __name__ == '__main__':
   server.run(debug = True, port=8000)