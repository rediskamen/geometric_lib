# Geometric Lib
___
## калькулятор
___
## Производит вычисления фигур:
- [x] [Круг](https://github.com/rediskamen/geometric_lib/blob/main/circle.py)
- [x] [Прямоугольник](https://github.com/rediskamen/geometric_lib/blob/main/rectangle.py)
- [x] [Квадрат](https://github.com/rediskamen/geometric_lib/blob/main/square.py)
- [x] [Треугольник](https://github.com/rediskamen/geometric_lib/blob/main/triangle.py)
### 1) Круг
- `def area(r)` получает *радиус* круга и возвращает его площадь, рассчитанную по формуле **S = πR<sup>2</
sup>**
```python
import math
area(r)
return(area)
```
>in >> `5` \
>out << `78,53982`
- `def perimeter(r)`получает *радиус* круга и возвращает его периметр, рассчитанный по формулеa **P = 2πR**
```python
import math
perimetr(r)
return(perimetr)
```
>in >> `5` \
>out << `31,41593`
### 2) Прямоугольник
- `def area(a, b)` получает *длину сторон* прямоугольника и возвращает его площадь, рассчитанную по
формуле **S = a * b**
```python
area(a, b)
return(area)
```
>in >> `3` >> `4` \
>out << `12`
- `def perimeter(a, b)` получает *длину сторон* прямоугольника и возвращает его периметр, рассчитанный по
формуле **P = 2 * (a + b)**
```python
perimeter(a, b)
return(perimeter)
```
>in >> `3` >> `4` \
>out << `14`
### 3) Квадрат
- `def area(a)` получает *длину стороны* квадрата и возвращает его площадь, рассчитанную по формуле **S =
a<sup>2</sup>**
```python
area(a)
return(area)
```
>in >> `5` \
>out << `25`
- `def perimeter(a)` получает *длину стороны* квадрата и возвращает его периметр, рассчитанный по формуле
**P = 4 * a**
```python
perimeter(a)
return(perimeter)
```
>in >> `5` \
>out << `20`
### 4) Треугольник
- `def area(a, h)` получает *длину основания треугольника* и *его высоту* и возвращает площадь, рассчитанную
по формуле **S = a * (h / 2)**
```python
area(a, h)
return(area)
```
>in >> `3` >> `6` \
>out << `9`
- `def perimeter(a, b, c)` получает *длину всех сторон треугольника* и возвращает его периметр, рассчитанный
по формуле **P = a + b + c**
```python
perimeter(a, b, c)
return(perimeter)
```
>in >> `3` >> `4` >> `5` \
>out << `12`
## История коммитов проекта:
`update README.md` *78766a2* \
`declaration of functions added and README.md` *d078c8d* \
`README.md modified` *58ee1bc* \
`mistake in rectangle.py fixed` *0e990bd* \
`mistake in rectangle.py fixed and new features triangle.py added` *24a9def* \
`new features rectangle.py added` *8ba8351*
