
from requests import get
s = input('Введите площадь = ')
length = input('Введите мин длину оси = ')
v_oblast= input('Введите выпуклую область  = ')
p= input('Введите периметр= ')
max_length= input('Введите макс длину оси= ')
excentricity = input('Введите эксцентриситет= ')
extent = input('extent= ')
print(get(f'http://localhost:5000/api?list1={s}&list2={length}&list3={v_oblast}&list4={p}&list5={max_length}&list6={excentricity}&list7={extent}').json())

