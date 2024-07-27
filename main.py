#-- Analizador de sentimientos (COMPUTACIÓN EN LA NUBE I) --

from analizar_sentimientos_en import analizarSentimientosIngles
from analisar_sentimientos_es import analizarSentimientoEspanol
from conexion import conn

cursor = conn.cursor() #Cursor para ejecutar consultas
comentarios = [] #Almacenar comentarios

#Analiar en español
cursor.execute("SELECT COMENTARIO FROM Comentarios") #Ejecutar consulta con el cursor creado
for i in cursor.fetchall(): #Obtener los elementos de la consulat
    comentarios.append(i) #Agregar elementos a la lista
conn.close()
print()

#Analizar version español
analizarSentimientoEspanol(comentarios)

#Analizar version ingles
#analizarSentimientosIngles()

