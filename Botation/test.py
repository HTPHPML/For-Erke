from pprint import pprint
from fpdf import FPDF
import datetime


class StringManager:
    def __init__(self):
        self.file = open("assets/dat.txt", "r", encoding='utf-8')
        self.data = []
        self.pdf = FPDF()
        self.now = datetime.datetime.now()

        self.month = {1: "Января", 2: "Февраля", 3: "Марта", 4: "Апреля", 5: "Мая", 6: "Июня",
                      7: "Июля", 8: "Августа", 9: "Сентября", 10: "Октября", 11: "Ноября", 12: "Декабря"}
        self.date = "Отчёт от " + str(self.now.day) + " " + self.month[self.now.month] + " " + str(
            self.now.year) + " года"

        self.dic = {"Lads": []}
        self.dat_time = None
        self.info = [["Нет ограничений на регистрацию", 0], ["Не найдено разрешение на работу в такси", 0],
                     ["Нет сведений о розыске", 0 ], []]

    def make_dic(self):
        owners = False
        for line in self.data:
            if not owners:
                self.dic[line[0]] = line[1:]
            else:
                self.dic["Lads"].append(line)
            if "Владельцев по ПТС" in line:
                owners = True

    def manage_data(self, data):
        for line in data:
            line = line.replace("\n", "")
            self.data.append(line.split(":"))
        self.dat_time = self.data.pop(-1)

    def write_pdf(self):
        pprint(self.dic)
        self.pdf.add_page()
        self.pdf.add_font('DejaVu', '', r'C:\Users\Tard\Desktop\Botation\assets\DejaVuSansCondensed.ttf')
        self.pdf.add_font('DejaVuBold', '', r'C:\Users\Tard\Desktop\Botation\assets\DejaVuSansCondensed-Bold.ttf')

        self.pdf.image("assets/logo.png", x=15, y=10, w=10, h=10)
        self.pdf.set_font("DejaVuBold", size=12)
        self.pdf.cell(50)
        self.pdf.cell(0, 5, txt="Отчёт куплен на сайте Sverka.com", align="R")
        self.pdf.ln(1)
        self.pdf.set_font("DejaVu", size=10)
        self.pdf.cell(0, 14,  txt="SverkaVIN - сервис по проверке автомобиля по VIN", align="R")

        self.pdf.ln(15)
        self.pdf.cell(3)
        self.pdf.set_font("DejaVu", size=9)
        self.pdf.cell(1, 0, txt=self.date, align="L")

        self.pdf.ln(10)
        self.pdf.set_font("DejaVuBold", size=24)
        self.pdf.cell(0, 0, txt=self.dic["Модель"][0] + ", " + self.dic["Год"][0], align="L")

        # Vin and type
        self.pdf.ln(20)
        self.pdf.cell(3)
        self.pdf.set_font("DejaVu", size=10)
        self.pdf.cell(40, 0, txt="VIN: ", align="L")
        self.pdf.set_font("DejaVuBold", size=10)
        self.pdf.cell(50, 0, txt=self.dic["VIN номер"][0], align="L")

        self.pdf.set_font("DejaVu", size=10)
        self.pdf.cell(40, 0, txt="Тип ТС: ", align="L")
        self.pdf.set_font("DejaVuBold", size=10)
        self.pdf.cell(0, 0, txt=self.dic["Тип ТС"][0], align="L")

        # gosnum and color
        self.pdf.ln(8)
        self.pdf.cell(3)
        self.pdf.set_font("DejaVu", size=10)
        self.pdf.cell(40, 0, txt="Госномер: ", align="L")
        self.pdf.set_font("DejaVuBold", size=10)
        self.pdf.cell(50, 0, txt=self.dic["Серия и номер ПТС"][0], align="L")

        self.pdf.set_font("DejaVu", size=10)
        self.pdf.cell(40, 0, txt="Цвет: ", align="L")
        self.pdf.set_font("DejaVuBold", size=10)
        self.pdf.cell(1, 0, txt=self.dic["Цвет"][0], align="L")

        # Номер кузова и объём двигателя
        self.pdf.ln(8)
        self.pdf.cell(3)
        self.pdf.set_font("DejaVu", size=10)
        self.pdf.cell(40, 0, txt="Номер кузова: ", align="L")
        self.pdf.set_font("DejaVuBold", size=10)
        self.pdf.cell(50, 0, txt=self.dic["Номер кузова"][0], align="L")

        self.pdf.set_font("DejaVu", size=10)
        self.pdf.cell(40, 0, txt="Объём двигателя: ", align="L")
        self.pdf.set_font("DejaVuBold", size=10)
        self.pdf.cell(1, 0, txt=self.dic["Объем двигателя"][0], align="L")

        # Номер двигателя и мощность
        self.pdf.ln(8)
        self.pdf.cell(3)
        self.pdf.set_font("DejaVu", size=10)
        self.pdf.cell(40, 0, txt="Номер двигателя: ", align="L")
        self.pdf.set_font("DejaVuBold", size=10)
        self.pdf.cell(50, 0, txt=self.dic["Номер двигателя"][0], align="L")

        self.pdf.set_font("DejaVu", size=10)
        self.pdf.cell(40, 0, txt="Мощность: ", align="L")
        self.pdf.set_font("DejaVuBold", size=10)
        self.pdf.cell(1, 0, txt=self.dic["Мощность двигателя"][0], align="L")

        # год выпуска
        self.pdf.ln(8)
        self.pdf.cell(3)
        self.pdf.set_font("DejaVu", size=10)
        self.pdf.cell(40, 0, txt="Год выпуска: ", align="L")
        self.pdf.set_font("DejaVuBold", size=10)
        self.pdf.cell(50, 0, txt=self.dic["Год"][0], align="L")

        self.pdf.set_font("DejaVu", size=10)
        self.pdf.ln(10)
        self.pdf.cell(3)
        self.pdf.cell(1, 0, txt="При осмотре автомобиля всегда сверяйте данные ПТС и VIN с указанными в отчёте. ", align="L")
        self.pdf.ln(5)
        self.pdf.cell(3)
        self.pdf.cell(1, 0, txt="Рекомендуем перед покупкой автомобиля обновить отчёт.", align="L")

        # Сводка по автомобилю
        self.pdf.ln(10)
        self.pdf.cell(3)
        self.pdf.set_font("DejaVuBold", size=12)
        self.pdf.cell(1, 0, txt="Сводка по автомобилю", align="L")

        # Ограничения регистрации и Разрешение такси
        self.pdf.image("assets/fine.png", x=15, y=120, w=8, h=8)
        self.pdf.ln(12)
        self.pdf.cell(16)
        self.pdf.set_font("Dejavu", size=10)
        self.pdf.cell(1, 0, txt=self.info[0][0], align="L")


        self.pdf.output("Test.pdf")

        
if __name__ == '__main__':
    sm = StringManager()
    sm.manage_data(sm.file)
    sm.make_dic()
    sm.write_pdf()
