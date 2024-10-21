# GRUPO N° 19

<div id="top"></div>

<div align="center">
<h3 align="center">Evidencia 2: Sistema de Gestión de Empleados para Recursos Humanos</h3>
 <p align="center">
    Proyecto: DATA  HUMAN´S
    <br />
    VER ÍNDICE MÁS ABAJO
    <br />
    <br />
  </p>
</div>

<!-- INDICE -->
<details>
  <summary>Tabla de contenidos</summary>
  <ul>
    <li>
      <a href="#integrantes">Integrantes</a>
    </li>
    <li><a href="#introduccion-a-la-programación">Introducción a la programación</a>
     <ul>
        <li><a href="#presentación">Presentación del proyecto</a></li>
        <li><a href="#descripción">Descripción inicial</a></li>
        <li><a href="#pseudocodigo">Pseudocódigo</a></li>
        <li><a href="#descripcion-archivos">Descripción de carpetas y archivos</a>
     <ul>
        <li><a href="#db">db</a></li>
        <li><a href="#aplicacion">aplicacion</a></li>
      </ul>
    </li>
      </ul>
    </li>
    <li><a href="#etica">Etica y Deontología Profesional</a></li>
        <li><a href="#bbdd">Base de datos</a></li>
        <li>
      <a href="#tutorial">Pasos para utilizar la aplicación</a>
    </li>
     <li><a href="#video">Link al Video</a>
          <li><a href="#PDF">Link al PDF</a>
  </ul>
</details>

<br />
<br />

<!-- INTEGRANTES -->

# Integrantes

Joaquin Dorgnach - 45.704.025 - dorgnachj@gmail.com - https://github.com/dorgnachj</br>
Lucas Ryser - 44.346.194 - lucasryser4k@gmail.com - https://github.com/lucasryser6</br>
Emanuel Guaráz - 38.276.061- guarazjemanuel@gmail.com https://github.com/JEmanuelG</br>
Nicolás Allende Olmedo - 35.871.057 - nicoallende92@gmail.com - https://github.com/AllendeNicolas</br>
Rocío Girardini - 41.280.222 - rogirardini@gmail.com - https://github.com/rociogirardini</br>

<hr />

<h3 align="center" id="introduccion-a-la-programación">Introducción a la programación</h3>

<h4 id='presentación'><strong>PRESENTACIÓN</strong></h4>

<p>DATA HUMAN'S es una empresa dedicada al desarrollo y mantenimiento de Software y Bases de Datos, orientada a la organización y asistencia de los departamentos de Recursos Humanos (RRHH), de las empresas en general.</p>

<p>Brindamos un sistema de Bases de Datos y Gestión de empleados, el cual cuenta con un sistema de selección de personal, mediante filtros de búsqueda entre los posibles candidatos, para los puestos vacantes de las empresas, ajustandose a las necesidades y requisitos a cumplir para el ingreso a planta.</p>

<p>De ampliarse el proyecto, nos gustaría que contase también con un análisis de producción de cada empleado, considerando las tareas que debe realizar, analizando su eficacia, y eficiencia laboral. También un análisis del ambiente laboral, teniendo en cuenta las relaciones interpersonales de los empleados dentro de la planta, y considerando la salud mental (aptos psicológicos) de los integrantes de la empresa.</p>

<p>Entre otras funciones, podríamos encontrar, conteos de empleados en planta, alta y baja de los mismos, filtros por departamentos, asignaciones de indumentaria laboral, pagos de sueldos, aportes y seguridad social, verificación de asistencia laboral, etc.</p>

<p>La descripción anterior es a lo que nos gustaría llegar como proyecto final, pero para esta instancia nos hemos enfocado únicamente en la carga de vacantes y búsqueda de postulantes.</p>

<h4 id='descripción'><strong>DESCRIPCIÓN INICIAL DEL PROYECTO</strong></h4>

En esta parte inicial del proyecto, proponemos realizar un sistema de selección de personal básico, donde la empresa que utiliza la aplicación podría ingresar los datos de una vacante, así como modificarla o eliminarla. Además, también podría ver los candidatos disponibles para el puesto, o filtrar por algún requisito en específico y ver solo ciertos candidatos.


<hr />

<h3 align="center" id='descripcion-archivos'>DESCRIPCIÓN DE LOS ARCHIVOS</h3>

<h4 id="db"> 📂 Carpeta <code>db</code></h4>

<p>Contiene los archivos:</p>

📂 Carpeta notacion-crows foot-mwb-sql
 - DER-MYSQL.mwb y DER-MYSQL.mwb.bak

 <p>Ambos archivos contienen el Modelo Crow Foot en sus respectivos formatos</p>

📂 Carpeta datahumans_db

- datahumans_db.sql
<p>Archivo con la base de datos completa de la aplicación. Este archivo será el que utilizaremos para la ejecución de la aplicación (más adelante se encuentran los pasos a seguir).</p>

- datahumans_estructura.sql
<p>Contiene únicamente la estructura del esquema, sin datos.</p>

- datahumans_consultas.sql
<p>En este archivo se encuentran diferentes consultas para hacer sobre la base de datos.</p>

🖼️ Imagen diagrama_entidad_relacion.jpg

<p> El modelo Entidad-Relación entregado en la segunda evidencia</p>

🖼️ Imagen diagrama_crow_foot.jpeg

<p> El modelo Crow Foot entregado en la tercer evidencia</p>

<hr />

<h4 id="aplicacion"> 📂 Carpeta <code>aplicacion</code></h4>

<p>Contiene los archivos:</p>

#### `index.py`

<p>Este archivo contiene el punto de entrada de la aplicación y la función principal `seleccion_personal()`, que maneja el menú y las opciones del usuario.</p>

<h4> <strong> 📂 Carpeta <code>candidatos</code> </strong> </h4>

<p>Contiene los archivos:</p>

#### `candidatos.py`

<p>Este módulo contiene una función llamada `ver_candidatos()`, la cual permite ver una lista detallada de todos los candidatos existentes en la base de datos.</p>

#### `filtros.py`

<p>Acá se encuentra la función `filtrar_por_requisitos()` donde el usuario puede ingresar ciertas características del candidato, como lugar de residencia, experiencia o educación y la función devuelve solo aquellos candidatos que coincidan con los filtros de búsqueda.</p>

<h4> <strong> 📂 Carpeta <code>vacante</code> </strong> </h4>

<p>Contiene los archivos del CRUD de una vacante:</p>

#### `create.py`

<p>Contiene la función `cargar_vacante()` donde se le solicitan al usuario todos los datos relacionados a la vacante, tales como título del puesto, descripción, condiciones de contratación, entre otros.</p>

#### `read.py`

<p>En este archivo se encuentra la función `ver_vacantes()`, que devuelve un listado de todas las vacantes disponibles.</p>

#### `update.py`

<p>Contiene la función `modificar_vacante()` donde el usuario, mediante el previo ingreso del ID de la vacante que desea modificar, puede modificar cualquiera de sus datos.</p>

#### `delete.py`

<p>Acá se encuentra la función `eliminar_vacante()` donde el usuario debe ingresar el ID de la vacante que desea eliminar para que esta sea quitada de la base de datos.</p>

<hr />

<h3 align="center" id="etica">Etica y Deontología Profesional</h3>
<p align="center"><a href="https://github.com/rociogirardini/ispc-tpi-2024/wiki"><strong>Ver Wiki »</strong></a></p>

<hr />

<h3 align="center" id="bbdd">Base de datos I</h3>
<p align="center"><a href="https://github.com/rociogirardini/ispc-tpi-2024/blob/main/db/diagrama_entidad_relacion.jpg"><strong>Ver Diagrama Entidad - Relación »</strong></a></p>
<p align="center"><a href="https://github.com/rociogirardini/ispc-tpi-2024/blob/main/db/diagrama_crow_foot.jpeg"><strong>Ver Diagrama Crows Foot »</strong></a></p>

<hr />

<h3 align="center" id="tutorial">Pasos para utilizar la aplicación</h3>

<h4>1. Descarga de archivos necesarios</h4>

<ul>
<li> Al inicio de este repositorio, hacer clic en el botón verde "Code" y seleccionar la opción Download ZIP</li>
<li> Buscar el archivo en tu computadora y descomprimirlo</li>
<li> Tener a mano solo los archivos:
<ul>
<li> Carpeta "aplicación"</li>
<li> Archivo "datahumans_db.sql" que se encuentra en la carpeta db > datahumans_db > datahumans_db.sql</li>
</ul>
</li>
</ul>

<h4>2. Preparación de entornos</h4>

<ul>
<li> Abrir mySQL Workbench y abrí tu instancia local (o creá una nueva, si no la tuvieras). Buscar la tab "Server" en la tab superior y hacer clic en "Data Import". </li>
<li>Seleccionar la opción "Import from Self-Contained File" y buscar en tus documentos el archivo descargado  <code>datahumans_db.sql</code></li>
<li>En la opción "Default Target Schema" hacer clic en "New" y escribir "data_human´s"</li>
<li>En el menú desplegable que aparece al final de la pantalla, asegurarse de tener seleccionada la opción "Dump Structure and Data"</li>
<li>Una vez hecha la importación, si aún no aparece en el menú "Schemas" de la izquierda, hacer clic en el ícono de Refrescar (se encuentra al lado de la palabra SCHEMA)</li>
<li>Abrir la carpeta <code>aplicacion</code> en Visual Studio Code</li>
</ul>

<h4>3. Ejecución</h4>

<ul>
<li>En Visual Studio Code, buscar la tab "Terminal" en la tab superior y hacer clic en "New Terminal"</li>
<li>Una vez dentro de la carpeta aplicacion, ejecutar en la terminal "pip install dependencias.txt" o, si no anduviera, ejecutar directamente "pip install mysql-connector-python"</li>
<li>En el VSC, ejecutar Crtl + Shift + F y escribir "mysql.connector.connect"</li>
<li>En todos los archivos donde se use "mysql.connector.connect", cambiar el campo "password" por tu contraseña de mySQL</li>
<li>Además, agregar el campo "port" como <code>port='3306'</code></li>
<li>Ejecutar el comando "python index.py"</li>
<li>¡Listo! Ahora queda seguir los pasos del menú en la terminal</li>
</ul>

<hr />

<h3 align="center" id="pdf">Presentación en PDF</h3>
<p align="center"><a href="https://github.com/rociogirardini/ispc-tpi-2024/blob/main/db/Base%20de%20datos%20del%20proyecto%2C%20sus%20diagramas%20y%20SQL.pdf"><strong>Ver Presentación en PDF »</strong></a></p>

<hr />

<h3 align="center" id="video">Video explicativo</h3>
<p align="center"><a href="https://drive.google.com/file/d/1DCGndz2koydTXqcuZBsKS5mhX70BrX-T/view"><strong>Link al video »</strong></a></p>
