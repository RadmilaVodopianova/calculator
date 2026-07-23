# Користувач вводить з клавіатури якусь кількість метрів. Виведіть результат
# конвертування метрів у сантиметри, дециметри, міліметри, милі.

meters = int(input("Enter  meters-"))
cm =  meters*100
dec = meters*10
km = meters/1000
miles =meters/1609.34
print(f"\ncentimeters is {cm}\ndecimeters is {dec}\nkilometers is {km}\nmiles is {miles}")


