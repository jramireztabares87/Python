import datetime

my_time = datetime.datetime.now()
print(my_time)

#----------------------------------------------------------------------------

my_day = datetime.date.today()
print(my_day)
print("Año ", my_day.year)
print("Mes ", my_day.month)
print("Día ", my_day.day)

#----------------------------------------------------------------------------
# Formato de fechas
# Year = %Y
# Month = %m
# Day = %d
# Hour = %H
# Minute = %M
# Second = %S

my_date_time = datetime.datetime.now()
print(my_date_time)

my_str = my_date_time.strftime("%d/%m/%Y")
print("Formato LATAN ", my_str)

my_str = my_date_time.strftime("%m/%d/%Y")
print("Formato USA ", my_str)

my_str = my_date_time.strftime("Estamos en el año  %Y")
print("Cualquier formato ", my_str)