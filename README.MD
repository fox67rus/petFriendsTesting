# Task 19.7.2

**Описание тестов в папке tests**
Позитивные тесты:
|#| Тест-кейс (имя метода) | Описание | Ссылка на метод|
| --- | --- | --- | --- |
|p1|test_get_api_key_for_valid_user| Получение api ключа для зарегистрированного пользователя| [link](https://github.com/fox67rus/petFriendsTesting/blob/cccc1b7428e5b5529f314afef52a65899803b295/tests/test_pet_friends.py#L8)|
|p2|test_get_all_pets_with_valid_key| Получение списка всех питомцев с валидным api ключом| [link](https://github.com/fox67rus/petFriendsTesting/blob/a43096b9de5b54e57fec0603be3242d5535adcf9/tests/test_pet_friends.py#L21)|
|p3|test_add_new_pet_with_valid_data| Добавление нового питомца с корректными данными| [link](https://github.com/fox67rus/petFriendsTesting/blob/a43096b9de5b54e57fec0603be3242d5535adcf9/tests/test_pet_friends.py#L34)|
|p4|test_successful_update_self_pet_info| Успешное обновление данных своего питомца| [link](https://github.com/fox67rus/petFriendsTesting/blob/a43096b9de5b54e57fec0603be3242d5535adcf9/tests/test_pet_friends.py#L53)|
|p5|test_successful_delete_self_pet| Успешное удаление питомца| [link](https://github.com/fox67rus/petFriendsTesting/blob/a43096b9de5b54e57fec0603be3242d5535adcf9/tests/test_pet_friends.py#L72)|
|p6|test_add_new_pet_without_photo_valid_data| Простое добавление питомца (без фото) с валидными данными| [link](https://github.com/fox67rus/petFriendsTesting/blob/776fbfea4e97df786945baa78dd31dff990aadff/tests/test_pet_friends.py#L97)|
|p7|test_successful_add_pets_correct_photo| Успешное добавление фото питомца с корректным файлом изображения (.jpg)| [link](https://github.com/fox67rus/petFriendsTesting/blob/776fbfea4e97df786945baa78dd31dff990aadff/tests/test_pet_friends.py#L113)|

Негативные тесты:
|#| Тест-кейс| Описание |
| --- | --- | --- |
|n1|test_get_api_key_for_invalid_user| Получение api ключа для не зарегистрированного пользователя|
|n2|test_get_all_pets_with_invalid_key| Запрос списка питомцев с невалидным api ключом возвращает код 403|
|n3|test_unsuccessful_update_another_user_pet_info| Отказ при обновлении данных чужого питомца|
|n4|test_unsuccessful_update_self_pet_info_with_empty_type| Обновление данных питомца: новая порода пустая строка|
|n5|test_unsuccessful_delete_another_user_pet| Отказ при удалении чужого питомца|
|n6|test_add_new_pet_without_photo_empty_name| Простое добавление питомца (без фото) с пустым именем|
|n7|test_add_new_pet_without_photo_long_animal_type| Простое добавление питомца (без фото): порода - текст 256 символов|
|n8|test_add_new_pet_without_photo_negative_age| Простое добавление питомца (без фото): отрицательный возраст|


В директории /tests располагается файл с тестами.

В директории /tests/images лежат картинки для теста добавления питомца и теста добавления картинки

В корневой директории лежит файл settings.py - содержит информацию о валидном логине и пароле

В корневой директории лежит файл api.py, который является библиотекой к REST api сервису веб приложения Pet Friends

Библиотека api написана в классе, что соответствует принципам ООП и позволяет удобно пользоваться её методами. При инициализации библиотеки объявляется переменная base_url которая используется при формировании url для запроса.

Методы имеют подробное описание.

Тесты проверяют работу методов используя api библиотеку.
