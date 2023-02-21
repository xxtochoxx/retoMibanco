# retoMibanco

1.-Instale Jenkis local desde el siguiente comando ( previamente se debe tener instalado docker)
	
	1.1 comando usado docker pull jenkis/jenkis:alpine
	
	1.2 levantando imagen:
	
		1.2.1-docker run -d --name=jenkins -p 8080:8080 -p 50000:50000 -v jenkins_home:/var/jenkins_home jenkins/jenkins:alpine
		
	1.3 configurar ramas remotas desde localhost ( error )

2.-Clonar el api , con las credenciales publicas de Marvel cominc.

	2.1 git clone git@github.com:xxtochoxx/retoMibanco.git

3.-El pipe1.yml es el más básico a ejecutar solo carga el archivo api.

4.-El pipe2.yml es el que tiene mayores validaciones , ejecuta el setup.py para la contruncción y compilar.

	4.1 se ejecuta pytest tests para pruebas unitarias.
	4.2 se valida que exista el archivo  y que tenga algún peso.
	4.3 se Comprime en formato tar.gz
	4.4 se usa twine upload para la publicación.
	
	
5.-Ejemplo de como se visualiza el pipeline2

<img width="805" alt="Captura de Pantalla 2023-02-21 a la(s) 11 54 38" src="https://user-images.githubusercontent.com/7839541/220409970-cc38ade9-cd55-4689-a3e3-0c4304e7e42a.png">

6.-Ejemplo de como se visualiza el pipeline1

<img width="509" alt="Captura de Pantalla 2023-02-21 a la(s) 11 57 47" src="https://user-images.githubusercontent.com/7839541/220410550-245f8aca-b391-425c-b139-3b6ec0cfec90.png">

He tenido que levantar un jenkis local , localhost pero por reglas de github no logre a depurar el error de conexión desde mi localhost hacia github, posible error de firewall de mi laptop.

7.-Referencia para corregir el error presentado.

https://stackoverflow.com/questions/33766275/i-need-help-setting-up-a-github-webhook-with-a-localhost-jenkins



