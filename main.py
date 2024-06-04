import random
a = input("Name = ")
b = input("Your login = ")
c = input("Your password = ")
print("Вы вошли в аккаунт!", a)
print("Список команд - как дела , майонез , предсказание , погода , смешное видео , upgrade , продвинутый список команд")
print("Пишете всё с заглавной буквы!")

#Стартовое сообщение
def greet():
    messages = ['Привет! Я ваш виртуальный помощник.', 'Здравствуйте! Чем могу помочь?']
    print(random.choice(messages))

#Ответы на сообщения пользователя
def handle_user_input(user_input):
     if 'Привет' in user_input:
        greet()
     elif 'Как дела' in user_input:
        print('Всё отлично, спасибо! А как у вас дела?')
     elif 'Майонез' in user_input:
        print('Вы открыли секретную команду! Теперь вы вступили в тайное агенство Майонез!')
     elif 'Предсказание' in user_input:
        print('Ооо, я вижу вокруг вас светлую энергетику! Ваш день пройдёт замечательно!')
     elif 'Погода' in user_input:
        print('+12 , Облачно')
     elif 'Смешное видео' in user_input:
        print('https://youtu.be/irpBtTdJVps?si=g-groZSycJzw6reg') or print('https://youtu.be/KAZVQls4XRk?si=CNHTbuEzKxT72mvo')
     elif 'Картинки' in user_input:
      print("Это скоро появится в обновлении Beta3! А пока разраб съел майонез и улетел на Мальдивы.")
     elif 'Upgrade' in user_input:
      print("Loading...Upgrade file system...10%...20%...30%...40%...50%...60%...70%...80%...90%...100%. Complite!")
     elif 'Продвинутый список команд' in user_input:
      print("Список комманд: book , weather , youtube , vk , Сбер Маркет , Chat Gpt , telegram , Upgrade Beta3")
     elif 'book' in user_input:
      print("https://litnet.com/")
      print("https://litmarket.ru/")
      print("https://readli.net/zhanryi/")
      print("https://www.litres.ru/popular/")
      print("https://mybook.ru/catalog/books/free/")
      print("https://litlife.club/genres")
      print("https://litgorod.ru/")
      print("https://litmir.club/")
     elif 'weather' in user_input:
      print("https://www.gismeteo.ru/weather-tyumen-4501/")
     elif 'youtube' in user_input:
      print("https://www.youtube.com/")
     elif 'vk' in user_input:
      print("https://m.vk.com/")
     elif 'Сбер Маркет' in user_input:
      print("https://sbermarket.ru/")
     elif 'Chat Gpt' in user_input:
      print("https://chadgpt.ru/")
      print("https://trychatgpt.ru/")
     elif 'Telegram' in user_input:
      print("https://web.telegram.org/")
     elif 'upgrade- Beta3' in user_input:
      print("Loading...10%...20%...30%...40%...50%...60%...70%...80%...90%...100%...Complite!")
      print("Pleese write your E-Mail")
      Mail = input("E-Mail - ")
      print("Вы подтвердили акаунт!")
      print("Новый список комманд:")
      print("Браузер , как дела , майонез , предсказание , погода , смешное видео , продвинутый список команд")
     #Браузер Игорёк
     elif 'Браузер' in user_input:
      print("Приветствую в браузере Игорёк 0.1!")
      print("Куда держим курс?")
      print("-youtube , vk , weather , Сбер Маркет")
      print("Chat Gpt , book , newspaper , мемы , kodland , zolors_play , Map")
      print("Ok , Games , dns , ozon")
     elif 'Newspaper' in user_input:
      print("https://ria.ru/")
     elif 'Мемы' in user_input:
      print("https://ru.pinterest.com/alinkafr20/%D1%81%D0%BC%D0%B5%D1%88%D0%BD%D1%8B%D0%B5-%D0%BC%D0%B5%D0%BC%D1%8B/")
     elif 'Kodland' in user_input:
      print("https://www.kodland.org/ru")
     elif 'Zolors_play' in user_input:
      print("https://youtube.com/@zolors_play5484?si=bN04_bv7pZEL01sP")
     elif 'Map' in user_input:
      print("https://maps.google.com/")
     elif 'Ok' in user_input:
      print("https://ok.ru/")
     elif 'Games' in user_input:
      print("https://www.crazygames.com/")
      print("https://yandex.com/games/")
     elif 'Dns' in user_input:
      print("https://www.dns-shop.ru/")
     elif 'Ozon' in user_input:
      print("https://www.ozon.ru/")
     elif 'My account' in user_input:
      print("Простите, но вы ещё не создали акаунт в Игорёк браузер")
      print("Создадим?")
     elif 'Да' in user_input:
      print("Поздравляю! Вы создали акаунт! Ваш ник - user5465")


#Работа приложения
def main():
    greet()
    while True:
        user_input = input('Вы: ')
        if user_input.lower() == 'пока':
            print('До свидания!')
            break
        handle_user_input(user_input)

if __name__ == '__main__':
    main()