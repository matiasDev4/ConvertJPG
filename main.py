import flet as ft
from utils.convert_image import convert_dicom_to_image, convert_pdf_to_image, convert_word_to_image 
from utils.progress_bar import progress_bar_
import time
def main(page: ft.Page):
    page.window.width = 400
    page.window.height = 400
    page.window.resizable = False
    page.window.alignment = ft.alignment.center
    page.title = 'Convertidor'
    page.bgcolor = '#2b2b2b'
    

    message = ft.Text(color=ft.Colors.WHITE)

    snack_bar = ft.SnackBar(
        content=message
    )
    
    def progres_sucess():
        view_file_names.value = 'Archivos listos!'
        message.value = 'Imagenes creadas en /documentos/IMAGENES DICOM'
        snack_bar.bgcolor = ft.Colors.GREEN_500
        page.open(snack_bar)
        page.update()
        
    
    def custom_error(error:str , filename:str = None):
        progress_bar.value = 0
        message.value = f'{error} {'' if filename == None else filename}'
        snack_bar.bgcolor = ft.Colors.RED_500
        page.open(snack_bar)
        page.update()
        

    
    def pick_files(e: ft.FilePickerResultEvent):
        files_size = []
        for file in e.files:
            extension = file.name.split('.')[1]
            files_size.append(file.size)
            try:
                match extension.lower():
                    case 'pdf':
                        try:
                            size = files_size
                            view_file_names.value = 'Subiendo...'
                            pdf = convert_pdf_to_image(file.path, file.name.split('.')[0])
                            for x in size:
                                pdf
                                progress_bar.value = progress_bar_(x, len(size))
                            if progress_bar.value >= 1:
                                progres_sucess()
                                
                        except Exception as e:
                            custom_error('Ocurrio un error al convertir el archivo', file.name)
                    case 'docx':
                        try:
                            view_file_names.value = 'Subiendo...'
                            size = files_size
                            word = convert_word_to_image(file.path, file.name)
                            for x in size:
                                word
                                progress_bar.value += progress_bar_(x, len(size))
                                progress_bar.update()
                            if progress_bar.value >= 1:
                                progres_sucess()
                        except Exception as e:
                            custom_error('Ocurrio un error al convertir el archivo', file.name)
                    case 'dcm':
                        try:
                            view_file_names.value = 'Subiendo...'
                            dicom = convert_dicom_to_image(file.path)  
                            size = files_size
                            for x in size:
                                dicom
                                progress_bar.value = progress_bar_(x, len(size))
                            if progress_bar.value >= 1:
                                progres_sucess()
                        except Exception as e:
                            custom_error('Ocurrio un error al convertir el archivo', file.name)
                    case _:
                        custom_error('El archivo no se reconoce, verifique el tipo de extension')
            except Exception as e:
                custom_error('Error inesperado', file.name)
            page.update()

            
    progress_bar = ft.ProgressBar(width=400, color=ft.Colors.AMBER, bgcolor=ft.Colors.BLACK, value=0)

    def open_directory(e):
        files.pick_files(allow_multiple=True)
        progress_bar.value = 0
        view_file_names.value = 'Esperando archivos...'
        view_file_names.update()
        page.update()

    files = ft.FilePicker(on_result=pick_files)
    button_input_files = ft.Button(
        text='Subir archivo',
        color=ft.Colors.WHITE,
        bgcolor=ft.Colors.BLACK,
        on_click=open_directory
    )
    view_file_names = ft.Text(value='Esperando archivos...', color=ft.Colors.WHITE)

    container = ft.Container(
        ft.Column(
        controls=[button_input_files, view_file_names, progress_bar]
    ),
    alignment=ft.alignment.center,
    margin=ft.margin.only(0,10,0,0)
    )

    page.add(container)
    page.add(files)
    page.update()
    






if __name__ == '__main__':
    ft.app(target=main, name='Converts files to JPG', assets_dir='assets')