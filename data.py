import pytest


class Urls:
    MAIN_PAGE = 'https://qa-scooter.praktikum-services.ru/'
    ORDER_PAGE = 'https://qa-scooter.praktikum-services.ru/order'
    YANDEX_PAGE = 'https://dzen.ru/?yredirect=true'


class Faq:
    """Вопросы и ответы блока Вопросы о важном"""
    pytestmark = pytest.mark.parametrize(
        'question_text, expected_response_text',
        [
            ('Сколько это стоит? И как оплатить?', 'Сутки — 400 рублей. Оплата курьеру — наличными или картой.'),
            ('Хочу сразу несколько самокатов! Так можно?',
             'Пока что у нас так: один заказ — один самокат. Если хотите покататься с друзьями, можете просто сделать несколько заказов — один за другим.'),
            ('Как рассчитывается время аренды?',
             'Допустим, вы оформляете заказ на 8 мая. Мы привозим самокат 8 мая в течение дня. Отсчёт времени аренды начинается с момента, когда вы оплатите заказ курьеру. Если мы привезли самокат 8 мая в 20:30, суточная аренда закончится 9 мая в 20:30.'),
            ('Можно ли заказать самокат прямо на сегодня?',
             'Только начиная с завтрашнего дня. Но скоро станем расторопнее.'),
            ('Можно ли продлить заказ или вернуть самокат раньше?',
             'Пока что нет! Но если что-то срочное — всегда можно позвонить в поддержку по красивому номеру 1010.'),
            ('Вы привозите зарядку вместе с самокатом?',
             'Самокат приезжает к вам с полной зарядкой. Этого хватает на восемь суток — даже если будете кататься без передышек и во сне. Зарядка не понадобится.'),
            ('Можно ли отменить заказ?',
             'Да, пока самокат не привезли. Штрафа не будет, объяснительной записки тоже не попросим. Все же свои.'),
            ('Я жизу за МКАДом, привезёте?', 'Да, обязательно. Всем самокатов! И Москве, и Московской области.')
        ]
    )


class RentalPeriod:
    """Срок аренды самоката"""
    rental_period_visible = ["сутки", "двое суток", "трое суток", "четверо суток",
                             "пятеро суток", "шестеро суток", "семеро суток"]


class ScooterColor:
    """Цвета самоката"""
    scooter_color = ["black", "grey"]


class MetroStation:
    """Все станции метро. Брать из ответа сервера. Ручка /api/v1/stations/search"""
    metro_station = [
        {
            "number": "1",
            "name": "Бульвар Рокоссовского",
            "color": "#D92B2C"
        },
        {
            "number": "2",
            "name": "Черкизовская",
            "color": "#D92B2C"
        },
        {
            "number": "3",
            "name": "Преображенская площадь",
            "color": "#D92B2C"
        },
        {
            "number": "4",
            "name": "Сокольники",
            "color": "#D92B2C"
        },
        {
            "number": "5",
            "name": "Красносельская",
            "color": "#D92B2C"
        },
        {
            "number": "6",
            "name": "Комсомольская",
            "color": "#D92B2C"
        },
        {
            "number": "7",
            "name": "Красные Ворота",
            "color": "#D92B2C"
        },
        {
            "number": "8",
            "name": "Чистые пруды",
            "color": "#D92B2C"
        },
        {
            "number": "9",
            "name": "Лубянка",
            "color": "#D92B2C"
        },
        {
            "number": "10",
            "name": "Охотный Ряд",
            "color": "#D92B2C"
        },
        {
            "number": "11",
            "name": "Библиотека имени Ленина",
            "color": "#D92B2C"
        },
        {
            "number": "12",
            "name": "Кропоткинская",
            "color": "#D92B2C"
        },
        {
            "number": "13",
            "name": "Парк культуры",
            "color": "#D92B2C"
        },
        {
            "number": "14",
            "name": "Фрунзенская",
            "color": "#D92B2C"
        },
        {
            "number": "15",
            "name": "Спортивная",
            "color": "#D92B2C"
        },
        {
            "number": "16",
            "name": "Воробьёвы горы",
            "color": "#D92B2C"
        },
        {
            "number": "17",
            "name": "Университет",
            "color": "#D92B2C"
        },
        {
            "number": "18",
            "name": "Проспект Вернадского",
            "color": "#D92B2C"
        },
        {
            "number": "19",
            "name": "Юго-Западная",
            "color": "#D92B2C"
        },
        {
            "number": "20",
            "name": "Тропарёво",
            "color": "#D92B2C"
        },
        {
            "number": "21",
            "name": "Румянцево",
            "color": "#D92B2C"
        },
        {
            "number": "22",
            "name": "Саларьево",
            "color": "#D92B2C"
        },
        {
            "number": "23",
            "name": "Речной вокзал",
            "color": "#4DBE52"
        },
        {
            "number": "24",
            "name": "Водный стадион",
            "color": "#4DBE52"
        },
        {
            "number": "25",
            "name": "Войковская",
            "color": "#4DBE52"
        },
        {
            "number": "26",
            "name": "Сокол",
            "color": "#4DBE52"
        },
        {
            "number": "27",
            "name": "Аэропорт",
            "color": "#4DBE52"
        },
        {
            "number": "28",
            "name": "Динамо",
            "color": "#4DBE52"
        },
        {
            "number": "29",
            "name": "Белорусская",
            "color": "#4DBE52"
        },
        {
            "number": "30",
            "name": "Маяковская",
            "color": "#4DBE52"
        },
        {
            "number": "31",
            "name": "Тверская",
            "color": "#4DBE52"
        },
        {
            "number": "32",
            "name": "Театральная",
            "color": "#4DBE52"
        },
        {
            "number": "33",
            "name": "Новокузнецкая",
            "color": "#4DBE52"
        },
        {
            "number": "34",
            "name": "Павелецкая",
            "color": "#4DBE52"
        },
        {
            "number": "35",
            "name": "Автозаводская",
            "color": "#4DBE52"
        },
        {
            "number": "36",
            "name": "Технопарк",
            "color": "#4DBE52"
        },
        {
            "number": "37",
            "name": "Коломенская",
            "color": "#4DBE52"
        },
        {
            "number": "38",
            "name": "Каширская",
            "color": "#4DBE52"
        },
        {
            "number": "39",
            "name": "Кантемировская",
            "color": "#4DBE52"
        },
        {
            "number": "40",
            "name": "Царицыно",
            "color": "#4DBE52"
        },
        {
            "number": "41",
            "name": "Орехово",
            "color": "#4DBE52"
        },
        {
            "number": "42",
            "name": "Домодедовская",
            "color": "#4DBE52"
        },
        {
            "number": "43",
            "name": "Красногвардейская",
            "color": "#4DBE52"
        },
        {
            "number": "44",
            "name": "Алма-Атинская",
            "color": "#4DBE52"
        },
        {
            "number": "45",
            "name": "Пятницкое шоссе",
            "color": "#2C75C4"
        },
        {
            "number": "46",
            "name": "Митино",
            "color": "#2C75C4"
        },
        {
            "number": "47",
            "name": "Волоколамская",
            "color": "#2C75C4"
        },
        {
            "number": "48",
            "name": "Мякинино",
            "color": "#2C75C4"
        },
        {
            "number": "49",
            "name": "Строгино",
            "color": "#2C75C4"
        },
        {
            "number": "50",
            "name": "Крылатское",
            "color": "#2C75C4"
        },
        {
            "number": "51",
            "name": "Молодёжная",
            "color": "#2C75C4"
        },
        {
            "number": "52",
            "name": "Кунцевская",
            "color": "#2C75C4"
        },
        {
            "number": "53",
            "name": "Славянский бульвар",
            "color": "#2C75C4"
        },
        {
            "number": "54",
            "name": "Парк Победы",
            "color": "#2C75C4"
        },
        {
            "number": "55",
            "name": "Киевская",
            "color": "#2C75C4"
        },
        {
            "number": "56",
            "name": "Смоленская",
            "color": "#2C75C4"
        },
        {
            "number": "57",
            "name": "Арбатская",
            "color": "#2C75C4"
        },
        {
            "number": "58",
            "name": "Площадь Революции",
            "color": "#2C75C4"
        },
        {
            "number": "59",
            "name": "Курская",
            "color": "#2C75C4"
        },
        {
            "number": "60",
            "name": "Бауманская",
            "color": "#2C75C4"
        },
        {
            "number": "61",
            "name": "Электрозаводская",
            "color": "#2C75C4"
        },
        {
            "number": "62",
            "name": "Семёновская",
            "color": "#2C75C4"
        },
        {
            "number": "63",
            "name": "Партизанская",
            "color": "#2C75C4"
        },
        {
            "number": "64",
            "name": "Измайловская",
            "color": "#2C75C4"
        },
        {
            "number": "65",
            "name": "Первомайская",
            "color": "#2C75C4"
        },
        {
            "number": "66",
            "name": "Щёлковская",
            "color": "#2C75C4"
        },
        {
            "number": "67",
            "name": "Кунцевская",
            "color": "#4DC6F4"
        },
        {
            "number": "68",
            "name": "Пионерская",
            "color": "#4DC6F4"
        },
        {
            "number": "69",
            "name": "Филёвский парк",
            "color": "#4DC6F4"
        },
        {
            "number": "70",
            "name": "Багратионовская",
            "color": "#4DC6F4"
        },
        {
            "number": "71",
            "name": "Фили",
            "color": "#4DC6F4"
        },
        {
            "number": "72",
            "name": "Кутузовская",
            "color": "#4DC6F4"
        },
        {
            "number": "73",
            "name": "Студенческая",
            "color": "#4DC6F4"
        },
        {
            "number": "74",
            "name": "Международная",
            "color": "#4DC6F4"
        },
        {
            "number": "75",
            "name": "Выставочная",
            "color": "#4DC6F4"
        },
        {
            "number": "76",
            "name": "Киевская",
            "color": "#4DC6F4"
        },
        {
            "number": "77",
            "name": "Смоленская",
            "color": "#4DC6F4"
        },
        {
            "number": "78",
            "name": "Арбатская",
            "color": "#4DC6F4"
        },
        {
            "number": "79",
            "name": "Александровский сад",
            "color": "#4DC6F4"
        },
        {
            "number": "92",
            "name": "Медведково",
            "color": "#F07025"
        },
        {
            "number": "93",
            "name": "Бабушкинская",
            "color": "#F07025"
        },
        {
            "number": "94",
            "name": "Свиблово",
            "color": "#F07025"
        },
        {
            "number": "95",
            "name": "Ботанический сад",
            "color": "#F07025"
        },
        {
            "number": "96",
            "name": "ВДНХ",
            "color": "#F07025"
        },
        {
            "number": "97",
            "name": "Алексеевская",
            "color": "#F07025"
        },
        {
            "number": "98",
            "name": "Рижская",
            "color": "#F07025"
        },
        {
            "number": "99",
            "name": "Проспект Мира",
            "color": "#F07025"
        },
        {
            "number": "100",
            "name": "Сухаревская",
            "color": "#F07025"
        },
        {
            "number": "101",
            "name": "Тургеневская",
            "color": "#F07025"
        },
        {
            "number": "102",
            "name": "Китай-город",
            "color": "#F07025"
        },
        {
            "number": "103",
            "name": "Третьяковская",
            "color": "#F07025"
        },
        {
            "number": "104",
            "name": "Октябрьская",
            "color": "#F07025"
        },
        {
            "number": "105",
            "name": "Шаболовская",
            "color": "#F07025"
        },
        {
            "number": "106",
            "name": "Ленинский проспект",
            "color": "#F07025"
        },
        {
            "number": "107",
            "name": "Академическая",
            "color": "#F07025"
        },
        {
            "number": "108",
            "name": "Профсоюзная",
            "color": "#F07025"
        },
        {
            "number": "109",
            "name": "Новые Черёмушки",
            "color": "#F07025"
        },
        {
            "number": "110",
            "name": "Калужская",
            "color": "#F07025"
        },
        {
            "number": "111",
            "name": "Беляево",
            "color": "#F07025"
        },
        {
            "number": "112",
            "name": "Коньково",
            "color": "#F07025"
        },
        {
            "number": "113",
            "name": "Тёплый Стан",
            "color": "#F07025"
        },
        {
            "number": "114",
            "name": "Ясенево",
            "color": "#F07025"
        },
        {
            "number": "115",
            "name": "Новоясеневская",
            "color": "#F07025"
        },
        {
            "number": "116",
            "name": "Планерная",
            "color": "#89339E"
        },
        {
            "number": "117",
            "name": "Сходненская",
            "color": "#89339E"
        },
        {
            "number": "118",
            "name": "Тушинская",
            "color": "#89339E"
        },
        {
            "number": "119",
            "name": "Спартак",
            "color": "#89339E"
        },
        {
            "number": "120",
            "name": "Щукинская",
            "color": "#89339E"
        },
        {
            "number": "121",
            "name": "Октябрьское поле",
            "color": "#89339E"
        },
        {
            "number": "122",
            "name": "Полежаевская",
            "color": "#89339E"
        },
        {
            "number": "123",
            "name": "Беговая",
            "color": "#89339E"
        },
        {
            "number": "124",
            "name": "Улица 1905 года",
            "color": "#89339E"
        },
        {
            "number": "125",
            "name": "Баррикадная",
            "color": "#89339E"
        },
        {
            "number": "126",
            "name": "Пушкинская",
            "color": "#89339E"
        },
        {
            "number": "127",
            "name": "Кузнецкий Мост",
            "color": "#89339E"
        },
        {
            "number": "128",
            "name": "Китай-город",
            "color": "#89339E"
        },
        {
            "number": "129",
            "name": "Таганская",
            "color": "#89339E"
        },
        {
            "number": "130",
            "name": "Пролетарская",
            "color": "#89339E"
        },
        {
            "number": "131",
            "name": "Волгоградский проспект",
            "color": "#89339E"
        },
        {
            "number": "132",
            "name": "Текстильщики",
            "color": "#89339E"
        },
        {
            "number": "133",
            "name": "Кузьминки",
            "color": "#89339E"
        },
        {
            "number": "134",
            "name": "Рязанский проспект",
            "color": "#89339E"
        },
        {
            "number": "135",
            "name": "Выхино",
            "color": "#89339E"
        },
        {
            "number": "136",
            "name": "Лермонтовский проспект",
            "color": "#89339E"
        },
        {
            "number": "137",
            "name": "Жулебино",
            "color": "#89339E"
        },
        {
            "number": "138",
            "name": "Котельники",
            "color": "#89339E"
        },
        {
            "number": "139",
            "name": "Раменки",
            "color": "#FBC81E"
        },
        {
            "number": "140",
            "name": "Ломоносовский проспект",
            "color": "#FBC81E"
        },
        {
            "number": "141",
            "name": "Минская",
            "color": "#FBC81E"
        },
        {
            "number": "142",
            "name": "Парк Победы",
            "color": "#FBC81E"
        },
        {
            "number": "143",
            "name": "Деловой центр",
            "color": "#FBC81E"
        },
        {
            "number": "144",
            "name": "Третьяковская",
            "color": "#FBC81E"
        },
        {
            "number": "145",
            "name": "Марксистская",
            "color": "#FBC81E"
        },
        {
            "number": "146",
            "name": "Площадь Ильича",
            "color": "#FBC81E"
        },
        {
            "number": "147",
            "name": "Авиамоторная",
            "color": "#FBC81E"
        },
        {
            "number": "148",
            "name": "Шоссе Энтузиастов",
            "color": "#FBC81E"
        },
        {
            "number": "149",
            "name": "Перово",
            "color": "#FBC81E"
        },
        {
            "number": "150",
            "name": "Новогиреево",
            "color": "#FBC81E"
        },
        {
            "number": "151",
            "name": "Новокосино",
            "color": "#FBC81E"
        },
        {
            "number": "152",
            "name": "Алтуфьево",
            "color": "#9F9F9F"
        },
        {
            "number": "153",
            "name": "Бибирево",
            "color": "#9F9F9F"
        },
        {
            "number": "154",
            "name": "Отрадное",
            "color": "#9F9F9F"
        },
        {
            "number": "155",
            "name": "Владыкино",
            "color": "#9F9F9F"
        },
        {
            "number": "156",
            "name": "Петровско-Разумовская",
            "color": "#9F9F9F"
        },
        {
            "number": "157",
            "name": "Тимирязевская",
            "color": "#9F9F9F"
        },
        {
            "number": "158",
            "name": "Дмитровская",
            "color": "#9F9F9F"
        },
        {
            "number": "159",
            "name": "Савёловская",
            "color": "#9F9F9F"
        },
        {
            "number": "160",
            "name": "Менделеевская",
            "color": "#9F9F9F"
        },
        {
            "number": "161",
            "name": "Цветной бульвар",
            "color": "#9F9F9F"
        },
        {
            "number": "162",
            "name": "Чеховская",
            "color": "#9F9F9F"
        },
        {
            "number": "163",
            "name": "Боровицкая",
            "color": "#9F9F9F"
        },
        {
            "number": "164",
            "name": "Полянка",
            "color": "#9F9F9F"
        },
        {
            "number": "165",
            "name": "Серпуховская",
            "color": "#9F9F9F"
        },
        {
            "number": "166",
            "name": "Тульская",
            "color": "#9F9F9F"
        },
        {
            "number": "167",
            "name": "Нагатинская",
            "color": "#9F9F9F"
        },
        {
            "number": "168",
            "name": "Нагорная",
            "color": "#9F9F9F"
        },
        {
            "number": "169",
            "name": "Нахимовский проспект",
            "color": "#9F9F9F"
        },
        {
            "number": "170",
            "name": "Севастопольская",
            "color": "#9F9F9F"
        },
        {
            "number": "171",
            "name": "Чертановская",
            "color": "#9F9F9F"
        },
        {
            "number": "172",
            "name": "Южная",
            "color": "#9F9F9F"
        },
        {
            "number": "173",
            "name": "Пражская",
            "color": "#9F9F9F"
        },
        {
            "number": "174",
            "name": "Улица Академика Янгеля",
            "color": "#9F9F9F"
        },
        {
            "number": "175",
            "name": "Аннино",
            "color": "#9F9F9F"
        },
        {
            "number": "176",
            "name": "Бульвар Дмитрия Донского",
            "color": "#9F9F9F"
        },
        {
            "number": "177",
            "name": "Петровско-Разумовская",
            "color": "#A8D92D"
        },
        {
            "number": "178",
            "name": "Фонвизинская",
            "color": "#A8D92D"
        },
        {
            "number": "179",
            "name": "Бутырская",
            "color": "#A8D92D"
        },
        {
            "number": "180",
            "name": "Марьина роща",
            "color": "#A8D92D"
        },
        {
            "number": "181",
            "name": "Достоевская",
            "color": "#A8D92D"
        },
        {
            "number": "182",
            "name": "Трубная",
            "color": "#A8D92D"
        },
        {
            "number": "183",
            "name": "Сретенский бульвар",
            "color": "#A8D92D"
        },
        {
            "number": "184",
            "name": "Чкаловская",
            "color": "#A8D92D"
        },
        {
            "number": "185",
            "name": "Римская",
            "color": "#A8D92D"
        },
        {
            "number": "186",
            "name": "Крестьянская застава",
            "color": "#A8D92D"
        },
        {
            "number": "187",
            "name": "Дубровка",
            "color": "#A8D92D"
        },
        {
            "number": "188",
            "name": "Кожуховская",
            "color": "#A8D92D"
        },
        {
            "number": "189",
            "name": "Печатники",
            "color": "#A8D92D"
        },
        {
            "number": "190",
            "name": "Волжская",
            "color": "#A8D92D"
        },
        {
            "number": "191",
            "name": "Люблино",
            "color": "#A8D92D"
        },
        {
            "number": "192",
            "name": "Братиславская",
            "color": "#A8D92D"
        },
        {
            "number": "193",
            "name": "Марьино",
            "color": "#A8D92D"
        },
        {
            "number": "194",
            "name": "Борисово",
            "color": "#A8D92D"
        },
        {
            "number": "195",
            "name": "Шипиловская",
            "color": "#A8D92D"
        },
        {
            "number": "196",
            "name": "Зябликово",
            "color": "#A8D92D"
        },
        {
            "number": "197",
            "name": "Каширская",
            "color": "#80D4C9"
        },
        {
            "number": "198",
            "name": "Варшавская",
            "color": "#80D4C9"
        },
        {
            "number": "199",
            "name": "Каховская",
            "color": "#80D4C9"
        },
        {
            "number": "200",
            "name": "Битцевский парк",
            "color": "#B0BFE7"
        },
        {
            "number": "201",
            "name": "Лесопарковая",
            "color": "#B0BFE7"
        },
        {
            "number": "202",
            "name": "Улица Старокачаловская",
            "color": "#B0BFE7"
        },
        {
            "number": "203",
            "name": "Улица Скобелевская",
            "color": "#B0BFE7"
        },
        {
            "number": "204",
            "name": "Бульвар Адмирала Ушакова",
            "color": "#B0BFE7"
        },
        {
            "number": "205",
            "name": "Улица Горчакова",
            "color": "#B0BFE7"
        },
        {
            "number": "206",
            "name": "Бунинская аллея",
            "color": "#B0BFE7"
        },
        {
            "number": "207",
            "name": "Окружная",
            "color": "#efadb5"
        },
        {
            "number": "208",
            "name": "Владыкино",
            "color": "#efadb5"
        },
        {
            "number": "209",
            "name": "Ботанический сад",
            "color": "#efadb5"
        },
        {
            "number": "210",
            "name": "Ростокино",
            "color": "#efadb5"
        },
        {
            "number": "211",
            "name": "Белокаменная",
            "color": "#efadb5"
        },
        {
            "number": "212",
            "name": "Бульвар Рокоссовского",
            "color": "#efadb5"
        },
        {
            "number": "213",
            "name": "Локомотив",
            "color": "#efadb5"
        },
        {
            "number": "214",
            "name": "Измайлово",
            "color": "#efadb5"
        },
        {
            "number": "215",
            "name": "Соколиная Гора",
            "color": "#efadb5"
        },
        {
            "number": "216",
            "name": "Шоссе Энтузиастов",
            "color": "#efadb5"
        },
        {
            "number": "217",
            "name": "Андроновка",
            "color": "#efadb5"
        },
        {
            "number": "218",
            "name": "Нижегородская",
            "color": "#efadb5"
        },
        {
            "number": "219",
            "name": "Новохохловская",
            "color": "#efadb5"
        },
        {
            "number": "220",
            "name": "Угрешская",
            "color": "#efadb5"
        },
        {
            "number": "221",
            "name": "Дубровка",
            "color": "#efadb5"
        },
        {
            "number": "222",
            "name": "Автозаводская",
            "color": "#efadb5"
        },
        {
            "number": "223",
            "name": "ЗИЛ",
            "color": "#efadb5"
        },
        {
            "number": "224",
            "name": "Верхние Котлы",
            "color": "#efadb5"
        },
        {
            "number": "225",
            "name": "Крымская",
            "color": "#efadb5"
        },
        {
            "number": "226",
            "name": "Площадь Гагарина",
            "color": "#efadb5"
        },
        {
            "number": "227",
            "name": "Лужники",
            "color": "#efadb5"
        },
        {
            "number": "228",
            "name": "Кутузовская",
            "color": "#efadb5"
        },
        {
            "number": "229",
            "name": "Деловой центр",
            "color": "#efadb5"
        },
        {
            "number": "230",
            "name": "Шелепиха",
            "color": "#efadb5"
        },
        {
            "number": "231",
            "name": "Хорошёво",
            "color": "#efadb5"
        },
        {
            "number": "232",
            "name": "Зорге",
            "color": "#efadb5"
        },
        {
            "number": "233",
            "name": "Панфиловская",
            "color": "#efadb5"
        },
        {
            "number": "234",
            "name": "Стрешнево",
            "color": "#efadb5"
        },
        {
            "number": "235",
            "name": "Балтийская",
            "color": "#efadb5"
        },
        {
            "number": "236",
            "name": "Коптево",
            "color": "#efadb5"
        },
        {
            "number": "237",
            "name": "Лихоборы",
            "color": "#efadb5"
        }
    ]

