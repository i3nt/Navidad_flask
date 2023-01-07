from flask import Flask, render_template
import datetime
app = Flask(__name__)
@app.route('/')
def navidad():
    hoy = datetime.datetime.now()
    if hoy.month == 12 and hoy.day == 25:
        mensaje = "¡Feliz Navidad🎄!"
    else:
        mensaje = f"Hoy no es Navidad.⛄"
    return render_template('index.html', mensaje=mensaje)











# from flask import Flask, render_template
# import datetime
# #el render template rendereizara un html
# #creamos una variable flask donde instanceamos una app de flask

# app = Flask(__name__)
# @app.route('/')
# def navidad():
#     hoy = datetime.datetime.now()
#     # navidad = datetime.datetime(hoy.year, 12, 25)
#     # if navidad < hoy:
#     #     navidad = datetime.datetime(hoy.year + 1, 12, 25)
#     if hoy.month == 12 and hoy.day == 25:
#         mensaje = "¡Feliz Navidad🎄!"
#     else:
#         # Proxima_Navidad = navidad - hoy
#         mensaje = f"Hoy no es Navidad.⛄ Aun faltan {Proxima_Navidad.days} días."

#     return render_template('index.html', mensaje=mensaje)

