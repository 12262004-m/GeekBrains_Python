time = int(input("Введите время в секундах: "))
hours = time//3600
ms = time % 3600
minutes = ms//60
seconds = ms % 60
print(f"Время: {hours}:{minutes}:{seconds}")