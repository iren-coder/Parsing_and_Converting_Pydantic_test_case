Тестовое задание Backend Developer


TODO: Сделать простой парсер и конвертер структур

Рекомендуемый стэк:

python3.6+

pydantic

pytest

Рекомендуемая методология: TDD

Результат выполнения в виде репозитория на github


Комментарий:<em> Если в инпуте инфы нет, значит нужно сделать это поле необязательным и дефолтное значение из output</em>

Входящие данные:
<pre>
{
 "description": "<ul><li>поддержка текущих проектов и сервисов компании,</li><li>разработка новых и доработка существующих функций по техническим заданиям,</li><li>активное взаимодействие с командой разработки,</li><li>освоение новых технологий и развитие профессиональных навыков под руководством опытного наставника.</li><li>Написание автотестов</li></ul>",
 "employment": "fullDay",
 "address": {
   "region": "Кировская",
   "city": "Киров",
   "street_type": "",
   "street": "",
   "house_type": "",
   "house": "",
   "value": "г Киров, ул Володарского, д 157",
   "lat": 58.593565,
   "lng": 49.672739
 },
 "name": "Junior Backend-developer",
 "salary": {
   "from": 30000,
   "to": 70000,
   "currency": "RUR",
   "gross": false
 },
 "contacts": {
   "fullName": "Журавлев Илья",
   "phone": "79536762399",
   "email": "ilya.zhuravlev@hrb.software"
 }
}

Результат:
{
 "address": "г Киров, ул Володарского, д 157",
 "allow_messages": true,
 "billing_type": "packageOrSingle",
 "business_area": 1,
 "contacts": {
   "email": "ilya.zhuravlev@hrb.software",
   "name": "Журавлев Илья",
   "phone": {
     "city": "953",
     "country": "7",
     "number": "676-23-99"
   }
 },
 "coordinates": {
   "latitude": 58.593565,
   "longitude": 49.672739
 },
 "description": "<ul><li>поддержка текущих проектов и сервисов компании,</li><li>разработка новых и доработка существующих функций по техническим заданиям,</li><li>активное взаимодействие с командой разработки,</li><li>освоение новых технологий и развитие профессиональных навыков под руководством опытного наставника.</li><li>Написание автотестов</li></ul>",
 "experience": {
   "id": "noMatter"
 },
 "html_tags": true,
 "image_url": "https://img.hhcdn.ru/employer-logo/3410666.jpeg",
 "name": "Junior Backend-developer",
 "salary": 70000,
 "salary_range": {
   "from": 30000,
   "to": 70000
 },
 "schedule": {
   "id": "fullDay"
 }
}
</pre>

<em>Что сделано:</em> При запуске main.py создаётся файл output.py с сконвертированными по примеру данными.
Использованный стек: Pydantic, Pytest

Чтобы запустить программу:
1. Создайте виртуальное окружение: 

       python -m venv env
       
2. Активируйте виртуальное окружение: 

       source env/bin/activate
       
3. Установите требуемые зависимости: 

       pip install -r requirements.txt

1. Запустите main.py: 

       python main.py
       
2. Для запуска тестов: 

       pytest tests.py

       либо

        pytest testing/

       


