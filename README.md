Шаг действий ддля работы с ботом ==
КАЧАЕМ ПИТОН 3.7 ОБЯЗАТЕЛЬНО ЧТОБЫ ОН БЫЛ 
1. Создаем venv  (python3.7 -m venv venv)

2. Активируем   ( . venv/scripts/activate) если не получается активировать -- гуглим ошибку 

3. затем мы устанвливаем все библиотеки которые сюда входят --> Они прописанны в requirements.txt 
    пишем pip install -r requirements.txt


4. Запускаем бота --  python bot.py 

по вопросам пишите справшивайте

оздание своей ветки, коммит изменений в удаленный репозиторий и создание запроса на слияние (pull request) — это стандартный процесс работы с системами контроля версий, такими как Git. Вот пошаговая инструкция:

1. Клонирование репозитория
Если вы еще не клонировали репозиторий, сделайте это:

bash
Копировать код
git clone <URL_репозитория>
cd <имя_репозитория>
2. Создание новой ветки
Создайте новую ветку для ваших изменений:

bash
Копировать код
git checkout -b <имя_ветки>
3. Внесение изменений
Внесите необходимые изменения в код. После этого добавьте измененные файлы в индекс:

bash
Копировать код
git add <имя_файла>  # Для добавления конкретного файла
git add .  # Для добавления всех измененных файлов
4. Коммит изменений
Сделайте коммит с описанием ваших изменений:

bash
Копировать код
git commit -m "Описание ваших изменений"
5. Отправка ветки в удаленный репозиторий
Отправьте вашу ветку в удаленный репозиторий:

bash
Копировать код
git push origin <имя_ветки>
6. Создание запроса на слияние
Теперь, когда ваша ветка отправлена в удаленный репозиторий, вам нужно создать запрос на слияние (pull request). Это можно сделать через интерфейс вашего репозитория на платформе, такой как GitHub, GitLab или Bitbucket:

Перейдите на страницу вашего репозитория.
Найдите кнопку "Pull Requests" или "Merge Requests".
Нажмите на "New Pull Request" или "New Merge Request".
Выберите вашу ветку и ветку, в которую вы хотите слить изменения (обычно это main или master).
Заполните заголовок и описание запроса на слияние.
Нажмите "Create Pull Request" или "Submit Merge Request".
7. Обсуждение и слияние
После создания запроса на слияние другие участники проекта могут просмотреть ваши изменения, оставить комментарии и, при необходимости, запросить доработки. Когда все будут довольны, запрос на слияние можно будет слить в основную ветку.

Заключение
Теперь вы знаете, как создать свою ветку, сделать коммит и создать запрос на слияние в удаленном репозитории. Удачи в разработке!




