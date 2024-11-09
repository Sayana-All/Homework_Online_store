# Homework_Online_store
### Проект для домашних заданий по модулю ООП.

## Описание
Большая часть разработки использует ООП-подход для создания своих сервисов, а также работы с данными, которые представляют собой сущности или объекты со своими параметрами и методами. 
В рамках этих домашних заданий мы проработаем использование классов и объектов на основе популярной темы e-commerce.

E-commerce — электронная торговля, или электронная коммерция. На данном этапе работы мы не будем реализовывать систему платежей, однако подготовим всё для того, чтобы у нас появилось ядро для интернет-магазина. 
В дальнейшем для этого ядра возможно будет реализовать любой интерфейс — от сайта до телеграм-бота.

## Информация для пользователей
### В настоящее время реализовано несколько полезных функций для виджета:
+ в модуле **masks** реализована функция маскировки номера банковской карты и счета пользователя.
+ в модуле **widget** также доступна функция маски номера карты или счета, а также реализована функция форматирования даты и приведения её к виду `"ДД.ММ.ГГГГ"`.
+ в модуле **main** реализована головная функция, отвечающая за общую логику проекта, связывающая остальные функциональности между собой.

_Данные модули прошли проверку тестами на валидность и работоспособность!_


## Логирование
Добавлено сохранение логов в файл для модулей **masks**, **utils** и **read_files**.
Логи сохранены в директории _logs_ в корне проекта.

## Тестирование
В ходе тестирования кода был выполнен ряд проверок и отладки отдельных блоков:

**Модуль masks**  

Функция `get_mask_card_number`:
+ Правильность маскирования номера карты.
+ Параметризованные тесты для проверки работы функции на различных входных форматах номеров карт.
+ Обработка исключения _ValueError_ при случаях, когда номер карты введен некорректно или имеет неправильную длину, нулевое или строчное (буквенное) значение. 


### Общие аспекты тестирования
**Фикстуры.** 
Все фикстуры для тестов модулей проекта перенесены в единый модуль **conftest.py**

**Mock и patch**
Тестирование функции с обращением к API, а также чтение файлов в модуле **read_files** произведено с помощью декоратора patch.

**Покрытие тестами.** 
Все ветви кода и исключения, которые могут быть сгенерированы функциями, тестируются.
Покрытие тестами составляет 93% кода


## Документация
Узнать более подробно о проекте и реализованных функциях можно по следующим ссылкам:
- [функция маски](Homework_9.1.md)
- [виджет](Homework_9.2.md)
- [работа с банковскими операциями (сортировка по ключу и дате)](Homework_10.1.md)
- [генераторы](Homework_11.1.md)
- [тестировка функций](Homework_10.2.md)
- [декораторы](Homework_11.2.md)
- [импорт транзакций из json-файла и конвертация валютных сумм](Homework_12.1.md)
- [логи для masks и utils](Homework_12.2.md)
- [получение данных из csv-файла и excel-файла](Homework_13.1.md)
- [поиск по описанию и основная сборка проекта](Homework_13.2.md)

