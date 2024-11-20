# Homework_Online_store
### Проект для домашних заданий по модулю ООП.

## Описание
Продолжаем работу над магазином: В домашнем задании этого урока вы создадите родительские классы и выделите классы-наследники, чтобы исключить повторение функциональности и оптимизировать код.

## Инструкции
Обратите внимание:
- Новые проекты и репозитории не создаются.
- Задания выполняйте в репозиториях соответствующих проектов из предыдущего домашнего задания.

# Задачи:
1. Для магазина необходимо выделить две категории товаров и создать под них классы:
    - ``«Смартфон» (Smartphone)``
    Помимо имеющихся свойств, необходимо добавить следующие:
        + производительность (efficiency),
        + модель (model),
        + объем встроенной памяти (memory),
        + цвет (color).
      
    - `«Трава газонная» (LawnGrass)`
    Помимо имеющихся свойств, необходимо добавить следующие:
        + страна-производитель (country),
        + срок прорастания (germination_period),
        + цвет (color).
      
Эти оба класса должны быть классами-наследниками от исходного класса `Product`.

2. Доработайте функциональность сложения таким образом, чтобы можно было складывать товары только из одинаковых классов продуктов.
То есть новая функциональность не должна давать возможность сложить смартфон и траву газонную, вместо этого должна быть выдана ошибка _TypeError_.

3. Ранее мы реализовали отдельный метод, с помощью которого можно добавлять объекты продуктов в категории. 
Теперь защитим метод так, чтобы, кроме смартфонов, травы газонной или других продуктов, в список нельзя было добавлять ничего другого.
Доработайте метод, который добавляет продукт в категорию, таким образом, чтобы не было возможности добавить вместо продукта или его наследников любой другой объект.

4. Напишите тесты для новой функциональности. При этом убедитесь что тесты, которые были написаны ранее, выполняются без ошибок.

5. Проверьте, что весь имеющийся код в файле **main.py** запускается без ошибок.