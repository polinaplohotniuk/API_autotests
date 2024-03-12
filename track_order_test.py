import sender_stand_requests
def get_track_number_of_order():
    track_number = sender_stand_requests.post_new_order() #сохраняем ответ при создании нового заказа
    return track_number.json()["track"] #сохраняем полученный трек

def test_create_and_track_order():
    track_number = get_track_number_of_order()
    get_response = sender_stand_requests.get_order_info(track_number)  #сохраняем рузультат запроса на получение информации по треку
    assert get_response.status_code == 200  #проверяем,что код ответа 200