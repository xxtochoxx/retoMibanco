from flask import Flask, jsonify, request
from flask_mysqldb import MySQL

app = Flask(__name__)
app.config['MYSQL_HOST'] = 'TU_HOST'
app.config['MYSQL_USER'] = 'TU_USUARIO'
app.config['MYSQL_PASSWORD'] = 'TU_CONTRASEÑA'
app.config['MYSQL_DB'] = 'TU_BASE_DE_DATOS'
mysql = MySQL(app)

@app.route('/customer', methods=['POST'])
def registrar_cliente():
    name_bank = request.json['name_bank']
    name_type_account = request.json['name_type_account']
    customer_account = request.json['customer_account']
    nro_account = request.json['nro_account']

    cur = mysql.connection.cursor()
    cur.execute('INSERT INTO customer_list_bank (tipo_banco, tipo_cuenta, nombre_cliente, numero_cuenta) VALUES (%s, %s, %s, %s)', (tipo_banco, tipo_cuenta, nombre_cliente, numero_cuenta))
    mysql.connection.commit()
    cur.close()

    return jsonify({'message': 'Cliente registrado exitosamente'})

if __name__ == '__main__':
    app.run()
