# Homework_Online_store
### Проект для домашних заданий по модулю ООП.

## Описание
Продолжаем работу над магазином: в этой домашней работе оптимизируем работу с данными путем добавления магических методов.

## Инструкции
Обратите внимание:
- Новые проекты и репозитории не создаются.
- Задания выполняйте в репозиториях соответствующих проектов из предыдущего домашнего задания.

# Задачи:
1. Для класса **Product** добавить строковое отображение в следующем виде:
```Название продукта, 80 руб. Остаток: 15 шт.```

В предыдущей домашке вы делали геттер для класса Category для вывода списка товаров, теперь каждый продукт имеет реализованное строковое отображение. 
Вы можете вернуться к этому геттеру и оптимизировать его работу, просто преобразовав объект продукта в строку.

Для класса **Category** добавить строковое отображение в следующем виде:
```Название категории, количество продуктов: 200 шт.```

2. Для удобства работы с продуктами реализовать возможность их складывать. Логика сложения должна работать так, чтобы в итоге у вас получалась полная стоимость всех товаров на складе.
Например, для товара `a` с ценой `100` рублей и количеством на складе `10` и товара `b` с ценой `200` рублей и количеством на складе 2 результатом выполнения операции `a + b` должно стать значение, полученное из ```100 × 10 + 200 × 2 = 1400```.

3. Напишите тесты для новой функциональности. При этом убедитесь что тесты, которые были написаны ранее, выполняются без ошибок.

4. Проверьте, что весь имеющийся код в файле **main.py** запускается без ошибок.

#### * Дополнительное задание к проекту
Создайте новый вспомогательный класс, с помощью которого можно перебирать товары одной категории, например в цикле for. 
Для этого новый класс должен принимать на вход объект класса категории и производить итерацию по товарам, которые хранятся в данной категории.

То есть метод выполнения следующего шага итерации должен возвращать очередной товар категории.

`Дополнительное задание, помеченное звездочкой, желательно, но не обязательно выполнять.`