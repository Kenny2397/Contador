from flask import Flask, render_template,request,session,redirect
app=Flask(__name__)
app.secret_key ="Chicken_little"

#inicio
@app.route('/')
def inicio():
    session['contador'] += 1
    return render_template('main.html')

#enlace redirect/se inicia session
@app.route('/reset', methods=['post'])
def reset():
    # session['+2']=request.form('aumenta2')
    session['contador'] = 0
    # print(session['submit'])  #imprime :Iniciar session
    if 'contador' in session:
        print('la llave existe!')
    else:
        print("la llave 'contador' NO existe")
    return redirect('/')


@app.route('/aumenta2', methods=['post'])
def aumenta2():
    session['contador'] += 1
    return redirect('/')

@app.route('/destroy_session')
def destroy():
    session.clear()
    if 'contador' in session:
        print('la llave existe!')
    else:
        print("la llave 'contador' NO existe")
    return render_template('main.html')

# #ruta raiz 
# @app.route('/main')
# def main():
#     session['contador'] += 1
#     if 'contador' in session:
#         print('la llave existe!')
#     else:
#         print("la llave 'contador' NO existe")
#     return render_template('main.html')


# @app.route('/leave', methods=['post'])
# def leav():
#     session.clear()
#     session.pop('contador')
#     session['contador']=1
#     if 'contador' in session:
#         print('la llave existe!')
#     else:
#         print("la llave 'contador' NO existe")
#     return render_template('/main.html')


if __name__ =='__main__':
    app.run(debug=True)

