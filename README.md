## Aplicación para convertir archivos DICOM o PDF a JPG

# Demostracion


![Video](https://github.com/user-attachments/assets/5746780d-e628-406b-8079-e9051a247c87)


[Descargar demo](https://download1349.mediafire.com/oqpj9lhkl1igUh15xxMhEWe-Ungk-eUz-Ckei489stRkqzhxgNvEAokZezFJkw8MZ8QeTCvKDdV5d_xw7V9VqeGte9SksolIcHcsrEU1bw_WG5GGx5wDBqV8ht0MYCQLTqbjdRcAhI6vu-1MMmgdYZgKrF1gLYGiMeev6AjsWfnV/afcjo52t0n0kh1f/ConvertJPG.rar)

# 🔍 ¿Que utilice?
  - [Flet](https://flet.dev/) Flet es un framework de python bastante nuevo, pero su potencia y velocidad para crear aplicaciónes frontend y backend en un mismo lugar es espactacular, mayormente utilizo Flet para este tipo de proyectos.
    Pero asi como tiene ventajas, también tiene sus desventajas, asi que actualmente me encuentro estudiando y practicando en [Electron](https://www.electronjs.org/es/) un framework para desarrollar aplicaciónes de escritorio utilizando HTML, CSS, JavaScript.
  - [Pydicom](https://pydicom.github.io/pydicom/stable/) libreria para la manipulacion de archivos DICOM, ayundome a extraer su informacion la cual utilizaria para la creación de la imagen
  - [Poppler](https://github.com/oschwartz10612/poppler-windows?tab=readme-ov-file) Poppler es una bibloteca de software que puede manipular archivos PDF y en conjunto con [pdf2image](https://pypi.org/project/pdf2image/) puedo hacer uso de las utilidades que ofrece      Poppler en Python
  - [Numpy](https://numpy.org/doc/) con numpy pude normalizar la cantidad pixeles de un archivo DICOM a la escala que una imagen JPG necesita
  - [Pillow](https://pillow.readthedocs.io/en/stable/) con pillow pude reconstruir la imagen con la escala correcta de pixeles y guardala en el directorio asignado

# 🤔 ¿Que aprendí?
  - Aprendí a manipular archivos DICOM y PDF, entendiendo a nivel básico los datos que los componen y como podemos utilizarlos para crear cosas, en este caso una imagen JPG. Aunque fue complejo entenderlo no me tomo mucho tiempo,
    gracias a las diferentes librerias que hacen el trabajo duro por de detras, pero que son importantes saber como utilizarlas y sacarle provecho.
    
# 🎯 Proximos objetivos 
  - Desarrollar una versión mas pulida, mejorar la interfaz grafica y agregar nuevas funcionalidades
  - Desarrollar la misma aplicación en Electron JS + React + TypeScript + Tailwind y utilizando scripts de Python para manejar la lógica de la aplicación
    




