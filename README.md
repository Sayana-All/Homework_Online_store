# Homework_Online_store
### Проект для домашних заданий по модулю ООП.

## Описание
Большая часть разработки использует ООП-подход для создания своих сервисов, а также работы с данными, которые представляют собой сущности или объекты со своими параметрами и методами. 
В рамках этих домашних заданий мы проработаем использование классов и объектов на основе популярной темы e-commerce.

E-commerce — электронная торговля, или электронная коммерция. На данном этапе работы мы не будем реализовывать систему платежей, однако подготовим всё для того, чтобы у нас появилось ядро для интернет-магазина. 
В дальнейшем для этого ядра возможно будет реализовать любой интерфейс — от сайта до телеграм-бота.

## Информация для пользователей
### В настоящее время реализовано несколько полезных функций для интернет-магазина:
1) В модуле **product** представлен класс `Product` с названием каждого продукта, его описанием, ценой и количеством, а помимо:
    + создан класс-метод, принимающий параметры товара в словаре и возвращающий объекты класса Product;
    + есть геттер для получения цены продукта, являющейся приватным атрибутом;
    + создан сеттер для изменения цены продукта. При этом, если новая цена ниже или равна 0, то выводится окно с предупреждением, а цена не меняется.
    Если новая цена ниже старой, то делается запрос пользователю для подтверждения изменения цены или отказе, сохраняя старую;
    + применен магический метод `__str__` для отображения класса Product для пользователей в виде строки;
    + применен магический метод `__add__` для сложения двух продуктов и получения их общей стоимости. При этом можно складывать продукты лишь одного и того же класса.
2) В модуле **category** представлен класс `Category` с названием и описанием категории, а также списком продуктов, соответствующим этой категории, а также:
    + есть два атрибута для подсчета общего количества продуктов и количества категорий. Оба заполняются автоматически при создании нового экземпляра класса;
    + создан геттер для получения списка продуктов категории, так как список продуктов является приватным атрибутом;
    + создан метод для добавления товаров в список продуктов категории, по одному за раз. При этом метод добавляет продукт в категорию таким образом, чтобы не было возможности добавить вместо продукта или его наследников любой другой объект;
    + представлен и переопределен геттер для выведения информации о списке продуктов категорий в виде спец-строки;
    + применен магический метод `__str__` для отображения класса Category для пользователей в виде строки.
3) В модуле **product_iterator** представлен вспомогательный класс `ProductIterator`, принимающий на вход объект класса категории и производящий итерацию по товарам, которые хранятся в данной категории.
4) В модуле **utils.py** реализована функция получения данных из JSON-файла, а также функция создания объектов классов из полученных данных.
5) В модуле **smartphone_prod.py** создан дочерний класс `Smartphone`(от род.класса Product), в котором есть все атрибуты родительского класса, а также:
    + добавлены новые атрибуты для инициализации (производительность, модель, объем встроенной памяти и цвет);
    + переопределен магический метод `__add__` для сложения двух продуктов и получения их общей стоимости. При этом можно складывать продукты лишь класса Смартфон.
6) В модуле **lawngrass_prod.py** создан дочерний класс `LawnGrass`(от род.класса Product), в котором есть все атрибуты родительского класса, а также:
    + добавлены новые атрибуты для инициализации (страна-производитель, срок прорастания и цвет);
    + переопределен магический метод `__add__` для сложения двух продуктов и получения их общей стоимости. При этом можно складывать продукты лишь класса Газонная трава.
7) В модуле **main** реализована проверка функциональности, весь код запускается без ошибок.

## Тестирование
В ходе тестирования кода был выполнен ряд проверок и отладки отдельных блоков:

**Модуль product**

Класс `Product`:
+ Проверена корректность инициализации объектов класса с помощью фикстур.
+ Тестирование на добавление нового продукта в список продуктов выбранной категории с помощью класс-метода `new_product()`.
+ Проверена работа сеттера `price` на изменение цены. Отработаны успешно случаи, когда новая цена ниже или равна 0 с выведением окна с предупреждением, а цена не меняется.
+ В сеттере price проверены ситуации, когда новая цена ниже старой с выводом информации пользователю и получения согласия на изменение цены.
+ Проверка на корректность отображения класса в виде строки для пользователя.
+ Тестирование на сложение двух продуктов и получение их общей стоимости.

**Модуль category**

Класс `Category`:
+ Проверена корректность инициализации объектов класса с помощью фикстур.
+ Проверено, что подсчет количества продуктов и количество категорий ведется верно и доступно для каждого объекта класса.
+ Тестирование геттера `products` на выведение строки списка продуктов класса.
+ Тестирование геттера `product_list` на получение списка продуктов и взаимодействия с ним.
+ Проверка метода `add_product` для добавления товаров в список продуктов категории.
+ Произведена обработка исключений в случаях, когда в список продуктов пытаются добавить не продукт из существующих классов или их наследников.
+ Тестирование на корректность отображения класса в виде строки для пользователя.

Класс `ProductIterator`:
+ Проверена корректность выполнения итерации по товарам в указанной категории товаров.
+ Проверено, что в начале работы итератора количество итераций равняется 0.
+ Произведена обработка исключения, когда итерация по товарам заканчивается и вызывается остановка.

**Модуль smartphone_prod**

Класс `Smartphone`:
+ Проверена корректность инициализации объектов класса с помощью фикстур.
+ Проведено тестирование на сложение двух продуктов данного класса и получение их общей стоимости.
+ Обработаны случаи вызова исключения, когда пытаются сложить продукты не одного класса.

**Модуль lawngrass_prod**

Класс `LawnGrass`:
+ Проверена корректность инициализации объектов класса с помощью фикстур.
+ Проведено тестирование на сложение двух продуктов данного класса и получение их общей стоимости.
+ Обработаны случаи вызова исключения, когда пытаются сложить продукты не одного класса.

### Общие аспекты тестирования
**Фикстуры.** 
Все фикстуры для тестов модулей проекта перенесены в единый модуль **conftest.py**

**Покрытие тестами.** 
Покрытие тестами составляет 99% кода

## Документация
Узнать более подробно о проекте и функционале можно по следующим ссылкам:
- [добавление двух классов и получение объектов для них из JSON-файла](Homework_14.1.md)
- [расширение функциональности классов Product и Category, настройки доступа](Homework_14.2.md)
- [использование магических методов и добавление класса ProductIterator](Homework_15.1.md)
- [дочерние классы Smartphone и LawnGrass](Homework_16.1.md)