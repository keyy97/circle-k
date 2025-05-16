paso 1. crear la base de datos
paso 2.generar un entorno virtual (saltar si ya existe)
paso 3.habilitar el entorno virtual
paso 4. comandos para el entorno virtual
python -m venv venv 
pip list
git init
paso 5.
crear una carpeta gitignore
dentro del archivo incluir el nombre del entorno virtual (venv)
-iniciar 
.\venv\Scripts\activate 
-cerrar
deactivate 
paso 6.
GitHub
-Iniciar repositorio
git init
-Cargar mi rep local a mi GitHub
git remote add origin https://github.com/keyy97/circle-k.git
-Asegurarme que esta correcto
git remote -v
-Salida esperada
origin  https://github.com/tu-usuario/GUITOPICOS.git (fetch)
origin  https://github.com/tu-usuario/GUITOPICOS.git (push)
-Preparo el commit 
git add .
-Realizo un commit 
git commit -m "Primer commit"
-Subo
git branch -M main
git push -u origin main

