# Task 19.7.2

В директории /tests располагается файл с тестами

В директории /tests/images лежат картинки для теста добавления питомца и теста добавления картинки

В корневой директории лежит файл settings.py - содержит информацию о валидном логине и пароле

В корневой директории лежит файл api.py, который является библиотекой к REST api сервису веб приложения Pet Friends

Библиотека api написана в классе, что соответствует принципам ООП и позволяет удобно пользоваться её методами. При инициализации библиотеки объявляется переменная base_url которая используется при формировании url для запроса.

Методы имеют подродное описание.

Тесты проверяют работу методов используя api библиотеку.

**Описание тестов в папке tests**
|#| name| description |
| --- | --- | --- |
|1|test_get_api_key_for_valid_user| | 
|2|test_get_all_pets_with_valid_key| |
|3|test_add_new_pet_with_valid_data| |
|4|test_successful_update_self_pet_info| |
|5|test_successful_delete_self_pet| |
|6|test_add_new_pet_without_photo_valid_data| |
|7|test_successful_add_pets_photo| |
|8|test_get_api_key_for_invalid_user| | 