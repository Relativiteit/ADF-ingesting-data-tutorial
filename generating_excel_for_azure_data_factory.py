from openpyxl import Workbook
from openpyxl.styles import Font
from openpyxl.chart import BarChart, Series, Reference

import random
import string


wb = Workbook()
ws = wb.active
header = ["Name", "Country", "Hobby", "Environment",
          "Age", "UserId", "Zipcode", "Mistakes"]
ws.append(header)
# generate random data
for data in range(999):
    data = [''.join(random.choices(string.ascii_lowercase,
                                   k=random.randint(1, 15))),  # name
            ''.join(random.choices(string.ascii_lowercase,
                    k=random.randint(1, 15))),  # country
            ''.join(random.choices(string.ascii_lowercase,
                    k=random.randint(1, 15))),  # hobby
            ''.join(random.choices(string.ascii_lowercase,
                    k=random.randint(1, 15))),  # environment
            random.randint(20, 80),  # age
            random.randint(10001, 10999),  # userId
            random.randint(3001, 3999),  # Zipcode
            random.randint(0, 5),  # Zipcode
            ]
    ws.append(data)

ft = Font(bold=True)
for cell in ws[1]:
    cell.font = ft
# Barchart look

chart = BarChart()
chart.type = "col"
chart.title = "Generated Data"
chart.y_axis.title = "Count"
chart.x_axis.title = "Categories"
chart.legend = None

# Add Reference
data = Reference(ws, min_col=8, min_row=2, max_row=11, max_col=8)
categories = Reference(ws, min_col=1, min_row=2, max_row=11, max_col=1)

chart.add_data(data)
chart.set_categories(categories)
ws.add_chart(chart, "I1")
wb.save("RandomData.xlsx")
