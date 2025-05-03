## Aplicacion para convertir archivos DICOM o PDF a JPG

# [Descargar demo](https://download1349.mediafire.com/oqpj9lhkl1igUh15xxMhEWe-Ungk-eUz-Ckei489stRkqzhxgNvEAokZezFJkw8MZ8QeTCvKDdV5d_xw7V9VqeGte9SksolIcHcsrEU1bw_WG5GGx5wDBqV8ht0MYCQLTqbjdRcAhI6vu-1MMmgdYZgKrF1gLYGiMeev6AjsWfnV/afcjo52t0n0kh1f/ConvertJPG.rar)

# 🔍 ¿Que utilice?
  - [Flet](https://flet.dev/) Flet es un framework de python bastante nuevo, pero su potencia y velocidad para crear aplicaciones frontend y backend en un mismo lugar es espactacular, mayormente utilizo Flet para este tipo de proyecto.
    Pero asi como tiene ventajas, tambien tiene sus desventajas, asi que actualmente me encuentro estudiando y practicando en [Electron](https://www.electronjs.org/es/) un Framework para desarrollar aplicaciones de escritorio utilizando HTML, CSS, JavaScript.
  - [Pydicom](https://pydicom.github.io/pydicom/stable/) libreria para la manipulacion de archivos DICOM, ayundome a extraer su informacion la cual utilizaria para la creacion de la imagen
  - [Poppler](https://github.com/oschwartz10612/poppler-windows?tab=readme-ov-file) Poppler es una bibloteca de software que puede manipular archivos PDF y en conjunto con [pdf2image](https://pypi.org/project/pdf2image/) puedo hacer uso de las utilidades que ofrece      Poppler en Python
  - [Numpy](https://numpy.org/doc/) con numpy pude normalizar la cantidad pixeles de un archivo DICOM a la escala que una imagen JPG necesita
  - [Pillow](https://pillow.readthedocs.io/en/stable/) con pillow puede reconstruir con la escala correcta de pixeles y guardala en el directorio asignado

# 🤔 ¿Que aprendi?
  - Aprendi a manipular archivos DICOM y PDF, entendiendo a nivel basico los datos que los componen y como podemos utilizarlos para crear cosas, en este caso una imagen JPG. Aunque fue complejo entenderlo no me tomo mucho tiempo,
    gracias a las diferentes librerias que hacen el trabajo duro de por detras, pero que son importantes saber como utilizarlas y sacarle provecho.
    
# 🎯 Proximos objetivos 
  - Desarrollar una version mas pulida, mejorar la interfaz grafica y agregar nuevas funcionalidades
  - Desarrollar la misma aplicacion en Electron JS + React + TypeScript + Tailwind y utilizando scripts de Python para manejar la logica de la aplicacion
    




