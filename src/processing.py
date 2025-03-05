def filter_by_state(id_list: list, state: str = "EXECUTED") -> list:
    """Функция сортировки по ключу состояния id клиента"""
    executed_list = []
    for id_number in id_list:
        if id_number["state"] == "EXECUTED":
            executed_list.append(id_number)

    return executed_list


print(
    filter_by_state(
        [
            {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
            {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
            {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
            {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
        ]
    )
)


def sort_by_date(id_list: list, reverse: bool = True) -> list:
    """Функция сортировки по дате"""
    date_sorted_list = sorted(id_list, key=lambda x: x["date"], reverse=True)

    return date_sorted_list


print(
    sort_by_date(
        [
            {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
            {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
            {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
            {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
        ]
    )
)
