# Para instalar flet: pip install flet



import flet as ft


class ButtonOperations(ft.ElevatedButton):
    def __init__(self, text, on_click):
        super().__init__()

        self.text = text
        self.data = text  # Store the button text as data
        
        self.width=58
        self.height=58
    
        self.style = ft.ButtonStyle(
            text_style=ft.TextStyle(
                color='#FFFFFF',
                weight=ft.FontWeight.W_300,
                size= 25,
            ),
            shape=ft.RoundedRectangleBorder(radius=16),
            bgcolor='#0A6FFF'
        )

        self.on_click = on_click

class ButtonNumbers(ft.ElevatedButton):
    def __init__(self, text, on_click):
        super().__init__()

        self.text = text
        self.data = text

        self.width=58
        self.height=58
        self.style = ft.ButtonStyle(
            text_style=ft.TextStyle(
                color='#FFFFFF',
                weight=ft.FontWeight.W_500,
                size= 28,
            ),
            shape=ft.RoundedRectangleBorder(radius=16),
            bgcolor='#171A4A',
        )

        self.on_click = on_click

        
class Calculadora(ft.Container):
    def __init__(self):
        super().__init__()
        
        self.reset()

        self.resultado = ft.Text(
            value='0',
            size=50,
            weight=ft.FontWeight.W_500,
        )

        self.expand = True
        self.content = ft.Column(
            spacing=0,
            controls=[
                #Container Ingreso de Datos
                ft.Container(
                    height= 230,
                    padding=20,
                    #bgcolor="#F5F5F5",
                    content=ft.Row(
                        alignment=ft.MainAxisAlignment.END,
                        vertical_alignment=ft.CrossAxisAlignment.END,
                        controls=[
                            self.resultado
                        ]
                    )
                ),
                
                # Container Botones
                ft.Container(
                    padding=10,
                    expand=True,
                    bgcolor="#000000",
                    
                    content=ft.Column(
                        alignment=ft.MainAxisAlignment.CENTER,
                        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                        controls=[
                            # Fila AC, ^, /, *
                            ft.Row(
                                alignment=ft.MainAxisAlignment.SPACE_EVENLY,
                                controls=[
                                    ButtonOperations('AC', on_click=self.button_clicked),
                                    ButtonOperations('%', on_click=self.button_clicked),
                                    ButtonOperations('^', on_click=self.button_clicked),
                                    ButtonOperations('/', on_click=self.button_clicked),
                                ]
                            ),
                            # Fila 7, 8, 9, -
                            ft.Row(
                                alignment=ft.MainAxisAlignment.SPACE_EVENLY,
                                controls=[
                                    ButtonNumbers('7', on_click=self.button_clicked),
                                    ButtonNumbers('8', on_click=self.button_clicked),
                                    ButtonNumbers('9', on_click=self.button_clicked),
                                    ButtonOperations('*', on_click=self.button_clicked),
                                ]
                            ),
                            # Fila 4, 5, 6, -
                            ft.Row(
                                alignment=ft.MainAxisAlignment.SPACE_EVENLY,
                                controls=[
                                    ButtonNumbers('4', on_click=self.button_clicked),
                                    ButtonNumbers('5', on_click=self.button_clicked),
                                    ButtonNumbers('6', on_click=self.button_clicked),
                                    ButtonOperations('-', on_click=self.button_clicked),
                                ]
                            ),
                            # Fila 1, 2, 3, +
                            ft.Row(
                                alignment=ft.MainAxisAlignment.SPACE_EVENLY,
                                controls=[
                                    ButtonNumbers('1', on_click=self.button_clicked),
                                    ButtonNumbers('2', on_click=self.button_clicked),
                                    ButtonNumbers('3', on_click=self.button_clicked),
                                    ButtonOperations('+', on_click=self.button_clicked),
                                ]
                            ),
                            # Fila 0, 00, ., =
                            ft.Row(
                                alignment=ft.MainAxisAlignment.SPACE_EVENLY,
                                controls=[
                                    ButtonNumbers('0', on_click=self.button_clicked),
                                    ButtonNumbers('00', on_click=self.button_clicked),
                                    ButtonOperations('.', on_click=self.button_clicked),
                                    ButtonOperations('=', on_click=self.button_clicked),
                                ]
                            )
                        ]
                    )
                )
            ]
        )
    
    # Funcion para Botones Clickeados
    def button_clicked(self, e):
        data = e.control.data
        #self.resultado.value = data
        

        # Ver si hay un error o si se borro el resultado
        if data == 'AC':
            self.resultado.value = '0'
            self.reset()
            
        
        elif data in ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0', '00', '.']:
            if self.resultado.value == '0' or self.nuevo_numero:
                self.resultado.value = data
                self.nuevo_numero = False
                
            else:
                self.resultado.value = self.resultado.value + data
                
            
        elif data in ['+', '-', '*', '/', '^', '%']:
            self.resultado.value = self.calcular(
                self.operador1, 
                float(self.resultado.value), 
                self.operacion
            )

            if self.resultado.value == 'ERROR':
                self.operador1 = 0
            else:
                self.operador1 = float(self.resultado.value)

            self.operacion = data
            self.nuevo_numero = True

        elif data == '=':
            self.resultado.value = self.calcular(
                self.operador1, 
                float(self.resultado.value), 
                self.operacion
            )
            self.reset()

        print(f"Botón presionado: {data}")
        
        self.update()

    def reset(self):
        self.operacion = '+'
        self.operador1 = 0
        self.nuevo_numero = True
    
    def tipoResultado(self, num):
        if num % 1 == 0:
            return int(num)
        else:
            return num

    def calcular(self, num1, num2, operacion):
        
        if operacion == '^':
            return self.tipoResultado(num1 ** num2)
        elif operacion == '%': # Módulo
            return self.tipoResultado(num1 % num2)
        elif operacion == '/':
            if num2 == 0:
                return 'ERROR'
            else:
                return self.tipoResultado(num1 / num2)
        elif operacion == '*':
            return self.tipoResultado(num1 * num2)
        elif operacion == '-':
            return self.tipoResultado(num1 - num2)
        elif operacion == '+':
            return self.tipoResultado(num1 + num2)


        

def main(page: ft.Page):
    page.title = "Calculator App"
    page.window.width = 340
    page.window.height = 640
    page.window.resizable = False
    page.padding = 0
    page.spacing = 0
    page.bgcolor = "#000000"
    page.add(Calculadora())


ft.app(target=main)