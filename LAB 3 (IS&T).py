import serial # Импортировать модуль serial
import time # Импортировать модуль времени
import serial.tools.list_ports # Импортировать инструменты для работы с серийными портами
speeds = ['1200','2400', '4800', '9600', '19200', '38400', '57600', '115200'] # Создать спи-сок доступных скоростей передачи данных
ports = [p.device for p in serial.tools.list_ports.comports()] # Получить список доступ-ных портов для подключения
port_name = ports[0] # Выбрать первый порт из списка
port_speed = int(speeds[-1]) # Установить скорость соединения с портом равной мак-симальной скорости
port_timeout = 10 #Установить таймаут соединения 10 секунд
ard = serial.Serial(port_name, port_speed, timeout = port_timeout) # Создать объект Seri-al для работы с Arduino через выбранный порт с выбранными параметрами
time.sleep(1) # Задержать выполнение программы на 1 секунду
ard.flushInput() # Очистить буфер входных данных
try: # Попытаться выполнить блок кода
 msg_bin = ard.read(ard.inWaiting()) # Прочитать данные из буфера ввода в виде байт и сконкатенировать их	
 msg_bin += ard.read(ard.inWaiting()) 
 msg_bin += ard.read(ard.inWaiting())
 msg_bin += ard.read(ard.inWaiting())
 msg_str_ = msg_bin.decode() # Декодировать полученные байты в строку
 print(len(msg_bin)) # Вывести длину полученной строки
except Exception as e:
 print('Error!') # Если возникло исключение, вывести 'Ошибка!'
ard.close() # Закрыть соединение с портом Arduino
time.sleep(1) # Задержать выполнение программы на 1 секунду
print(msg_str) # Вывести значение полученной строки на экран
