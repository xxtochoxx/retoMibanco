# retoMibanco

1.-Clonar el api , con las credenciales publicas de Marvel cominc.

Git clone git@github.com:xxtochoxx/retoMibanco.git

2.-El pipe1.yml es el más básico a ejecutar solo carga el archivo api.

3.-El pipe2.yml es el que tiene mayores validaciones , ejecuta el setup.py para la contruncción y compilar.

	3.1 se ejecuta pytest tests para pruebas unitarias.
	3.2 se valida que exista el archivo  y que tenga algún peso.
	3.3 se Comprime en formato tar.gz
	3.4 se usa twine upload para la publicación.