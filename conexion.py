"""
-Credenciales-
IP: 137.184.153.254
USER: grp1
DB=personas_cen
PASS=1234
"""

import mysql.connector #Conector para MySQL

conn = mysql.connector.connect( #Establece una conexion con la BBDD y devuelve un objeto de tipo conexion en caso de ser exitosa
    host = '137.184.153.254',
    database = 'personas_cen',
    user = 'grp1',
    password = '1234'
)