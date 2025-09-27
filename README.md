## Задание 1
У пользователя 2 сегмента/перелета, судя по структуре и неймингу полей ответа `GetOrderList`, они определяются полем `<ns1:segments>` -> `<ns1:AirSegment>` -> `<ns1:segment_id>0</ns1:segment_id>` и `<ns1:segment_id>1</ns1:segment_id>`

В запросе `AddOrderService` передается поле `<ns0:segment_id>2</ns0:segment_id>`, ну соответственно услугу попытались применить к несуществующему перелету.

Из улучшений наверное важно добавить нормальный ответ, потому что сейчас получилось, что вернулся `OK` `(код 200)`, а по факту я бы вернул ошибку `(404 ну или хотя бы 400)`.

Еще наверное из такого разобраться как пользователь вообще смог отправить запрос со значением, которого для него не существует. Следовательно на клиенте не давать ему возможность указать какие-то "левые" данные, а только выбрать из предложенных вариантов, для которых фоново проставлен заранее `segment_id`, и потом просто в запросе отправлять что-то типо `selected.segment_id`

## Задание 2
### Задание по MongoDB
```
db.users.find({
  $or: [
    { "channels.phone.verified": true, "channels.email.verified": false },
    { "channels.phone.verified": false, "channels.email.verified": true}
  ]
}).limit(3)
```
[Тут](https://github.com/yarik1811/test-task/blob/main/generate_data.py) код (файл `generate_date.py`), для того, чтобы сгенерировать данные и потом проверить на реальной БД, а не просто образный запрос.

### Задание по PostgreSQL
#### Запрос 1
```sql
SELECT 
    a.id, a.created_at
    -- , SUM(ABS(tb.amount)) as total_debited
FROM account a
JOIN transaction t ON a.id = t.account
JOIN transaction_balance tb ON t.id = tb.transaction_id
WHERE tb.amount < 0
GROUP BY a.id
HAVING SUM(ABS(tb.amount)) > 500;
```

#### Запрос 2
```sql
SELECT t.id, t.account, t.created_at
FROM transaction t
JOIN account a ON t.account = a.id
JOIN transaction_balance tb ON t.id = tb.transaction_id
WHERE 
    a.created_at >= '2020-01-01'
    AND tb.amount > 0
ORDER BY t.created_at;
```

#### Запрос 3
```sql
SELECT DISTINCT a.id, a.created_at
FROM account a
LEFT JOIN transaction t ON a.id = t.account
    AND t.created_at >= '2020-01-01'
    AND t.created_at < '2021-01-01'
WHERE t.id IS NULL;
```


## Задание 3
Попыток платной регистрации: **95 (48.7% от общего числа)**  
Попыток бесплатной регистрации: **100  (51.3% от общего числа)**  
Общее число регистраций: **195**  
Регистраций завершившихся успешно: **159**   


Процент регистраций завершенных успешно относительно общего числа - **81.5%**

Если результативность каждого способа регистрации одинакова (81.5%), то:  
    - **78** пользователей зарегистрировались бесплатно  
    - **81** пользователь зарегистрировался платно
    
Если не одинакова (что более вероятно), то по этим данным нельзя сказать, нужно хранить сколько по какому способу зарегистрировались.

В любом случае высокий процент регистрации (по умному наверное конверсия), говорит о том, что процесс хорошо выстроен, пользователи особо не испытывали проблем

Чуть отходя от конкретного вопроса:
Пик регистраций ежедневно приходится на 9:00 - 10:00 (17 и 18 числа)

## Задание 4
Код [тут](https://github.com/yarik1811/test-task/blob/main/get_problem_data.py) (файл `get_problem_data.py`), ответы в файлаx [`only_owner.json`](https://github.com/yarik1811/test-task/blob/main/only_owner.json) и [`missing_users.json`](https://github.com/yarik1811/test-task/blob/main/missing_users.json)
