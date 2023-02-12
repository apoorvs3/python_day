# This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the
# program requirements.
from flight_search import FlightSearch
from flight_data import FlightData

if __name__ == '__main__':
    # fs = FlightSearch(location='DEL')
    fs = {
        "search_id": "9bc245cb-e6c0-0a9a-97a0-327cb36b19a3",
        "currency": "EUR",
        "fx_rate": 1,
        "data": [
            {
                "id": "071109fd4bc900003d139c6f_0",
                "flyFrom": "DEL",
                "flyTo": "AGR",
                "cityFrom": "New Delhi",
                "cityCodeFrom": "DEL",
                "cityTo": "Agra",
                "cityCodeTo": "AGR",
                "countryFrom": {
                    "code": "IN",
                    "name": "India"
                },
                "countryTo": {
                    "code": "IN",
                    "name": "India"
                },
                "nightsInDest": "None",
                "quality": 44.999955,
                "distance": 178.27,
                "duration": {
                    "departure": 2700,
                    "return": 0,
                    "total": 2700
                },
                "price": 27,
                "conversion": {
                    "EUR": 27
                },
                "bags_price": {
                    "1": 0
                },
                "baglimit": {
                    "hand_height": 35,
                    "hand_length": 55,
                    "hand_weight": 7,
                    "hand_width": 25,
                    "hold_dimensions_sum": 158,
                    "hold_height": 52,
                    "hold_length": 78,
                    "hold_weight": 15,
                    "hold_width": 28
                },
                "availability": {
                    "seats": 2
                },
                "airlines": [
                    "G8"
                ],
                "route": [
                    {
                        "id": "071109fd4bc900003d139c6f_0",
                        "combination_id": "071109fd4bc900003d139c6f",
                        "flyFrom": "DEL",
                        "flyTo": "AGR",
                        "cityFrom": "New Delhi",
                        "cityCodeFrom": "DEL",
                        "cityTo": "Agra",
                        "cityCodeTo": "AGR",
                        "airline": "G8",
                        "flight_no": 1014,
                        "operating_carrier": "",
                        "operating_flight_no": "",
                        "fare_basis": "NO9RBINE",
                        "fare_category": "M",
                        "fare_classes": "N",
                        "fare_family": "",
                        "return": 0,
                        "bags_recheck_required": False,
                        "vi_connection": False,
                        "guarantee": False,
                        "equipment": "None",
                        "vehicle_type": "aircraft",
                        "local_arrival": "2023-02-13T10:30:00.000Z",
                        "utc_arrival": "2023-02-13T05:00:00.000Z",
                        "local_departure": "2023-02-13T09:45:00.000Z",
                        "utc_departure": "2023-02-13T04:15:00.000Z"
                    }
                ],
                "booking_token": "E_c-rglOCRt1pesO8E3stJTNvwqz_FDJoYwRHRk36svI8lIkNiIVxuflb0PdmMfahFJ8spjSKpYuXnjdwzgu8nGibaUkOdYBTG4cKAa0amkQ0jcc_fJcV5SlBfwpJpJ8vFv7LM8uwbTcH6xv5rz1F111Mh9g3h-JfgzNQL3OYKQhvEqWRuoT8YRbhisMS-FmcLH-D6QlWE2aGyzcgOLDkREh9TwRCTJfxkc5n2F57xVinjthSt2pY-r8Fg9Ed5TtX5EbmceJRVdLS_tByZU8uFWDiX9Ldfkj6BhZkIW2qGEokk1zLHwFkpxsE4bDWjeVJYAzVCwEuuaaKBqOZmHQvwzfRF3XzvRt9z59gPk3PGJKqzyD4qzyO19LbUXLzo9NlHDkeJDQPYvWmE0MGoefgTV_wE1j1QyyiHm_3Yo4QXXIk-LJKIF52_U-w_nnkASe4oJnBYI7fqgocedLHvh4wO-VTXftxp3JpquhHUq2uh8i6bDomGRCqMWiDPgP60e3gZSQ4WD_lNHvEAHrCsOHkpZVA2dhF97I1brHMvq6uYn124EendPifzkuqnWYDJZAV",
                "deep_link": "https://www.kiwi.com/deep?affilid=apoorvflightsearch&currency=EUR&flightsId=071109fd4bc900003d139c6f_0&from=DEL&lang=en&passengers=1&to=AGR&booking_token=EPoCXmJWnJs-8hOKETAK6xnfNeVN_sWZ8m14ixe9rkQyoCZB7nEmx_jRkVxsCGmKFDPLWYgdmrmDml4Jg2zJZzknqFRHCJ0a05a-F878MPvU5nFwkPT2OhgbT8WEq_1-ldx-9zVRE9E5Ce1Chhz10reADyl0_WJSLCCRyB3ZxzRfC8vuJhoVL-6t2YkbOX3gHwP7FjI6vxAJ8owzJ8UmypsUbcJvXXNY9wd4YO7eMqtRh6CugFuVTjrz7NC71teOy86qnxKLl_zUH4msaKPMi2mbq16kJsALs6RW41JCEEAL0oYxia5Wkqx4sP2Xm0CYD8HV-YlC-hlbCX_XRH7BA2YUz6FX3eft5MfJFxOUqsTWHMdL_49DcCJVBtv8W8e57w58aICFSXzlaYLTdTWCQmT6Hr0T6PPyD_LB04LzAd4A=",
                "facilitated_booking_available": True,
                "pnr_count": 1,
                "has_airport_change": False,
                "technical_stops": 0,
                "throw_away_ticketing": False,
                "hidden_city_ticketing": False,
                "virtual_interlining": False,
                "local_arrival": "2023-02-13T10:30:00.000Z",
                "utc_arrival": "2023-02-13T05:00:00.000Z",
                "local_departure": "2023-02-13T09:45:00.000Z",
                "utc_departure": "2023-02-13T04:15:00.000Z"
            },
            {
                "id": "071104c24bc900006a3344cd_0",
                "flyFrom": "DEL",
                "flyTo": "LKO",
                "cityFrom": "New Delhi",
                "cityCodeFrom": "DEL",
                "cityTo": "Lucknow",
                "cityCodeTo": "LKO",
                "countryFrom": {
                    "code": "IN",
                    "name": "India"
                },
                "countryTo": {
                    "code": "IN",
                    "name": "India"
                },
                "nightsInDest": "None",
                "quality": 50.666615,
                "distance": 423.95,
                "duration": {
                    "departure": 3900,
                    "return": 0,
                    "total": 3900
                },
                "price": 30,
                "conversion": {
                    "EUR": 30
                },
                "bags_price": {
                    "1": 0
                },
                "baglimit": {
                    "hand_height": 38,
                    "hand_length": 57,
                    "hand_weight": 7,
                    "hand_width": 20,
                    "hold_dimensions_sum": 158,
                    "hold_height": 52,
                    "hold_length": 78,
                    "hold_weight": 15,
                    "hold_width": 28
                },
                "availability": {
                    "seats": 2
                },
                "airlines": [
                    "6E"
                ],
                "route": [
                    {
                        "id": "071104c24bc900006a3344cd_0",
                        "combination_id": "071104c24bc900006a3344cd",
                        "flyFrom": "DEL",
                        "flyTo": "LKO",
                        "cityFrom": "New Delhi",
                        "cityCodeFrom": "DEL",
                        "cityTo": "Lucknow",
                        "cityCodeTo": "LKO",
                        "airline": "6E",
                        "flight_no": 2025,
                        "operating_carrier": "6E",
                        "operating_flight_no": "2025",
                        "fare_basis": "R0IP",
                        "fare_category": "M",
                        "fare_classes": "X",
                        "fare_family": "",
                        "return": 0,
                        "bags_recheck_required": False,
                        "vi_connection": False,
                        "guarantee": False,
                        "equipment": "None",
                        "vehicle_type": "aircraft",
                        "local_arrival": "2023-02-13T07:15:00.000Z",
                        "utc_arrival": "2023-02-13T01:45:00.000Z",
                        "local_departure": "2023-02-13T06:10:00.000Z",
                        "utc_departure": "2023-02-13T00:40:00.000Z"
                    }
                ],
                "booking_token": "ECS1g8Ki3RXC5uYcfxnirqq42WbWZjzNsm6PachjrwF32RBEsqIdhl4CKs11UiZTD6c7KsLcyWZIuBSa0eh7ZohwRfN1EpYqxL-bVqp2YtTMjKYRi6KytyE4ghfYDgWmdSDbKAvk8LRbUtPnjPN5t3zuMekrWw5TnFrxk6g2VKufzekGwdSbUJuvK-aYwDnGZiIbEewTmsk3IBf8ysUmPpnDIcM3kWYgx41GOZskA8ZAhPinU525a_4tUx66lAuW-rEhYy4wOL24-2U43Yobo-4bazoWr4fOIyIPYQug5xjmPb90LJDk67zsBEGD2gK0dq3EOaTWk5S6qnROMHvg3pN2QMgOKB_p8jrKQR5Exo1KR-pYJi_R4EB0oc7bzCd8OWXpiscSBDSnskVQIsI-FcFFnbPmwuyzctaXWgec7nd5c3uxAr5UkWQ2NT-vwc2tvJoBWBn_UDdQCh8OFWr5Ev87tXBcSHp219sSVI80b0rncf0DSup3-bTZV6mdMj-sCPT-GkEXtyvTq28O6ZrP1lS5T8FoEc7Rz4adC1dY2vGI=",
                "deep_link": "https://www.kiwi.com/deep?affilid=apoorvflightsearch&currency=EUR&flightsId=071104c24bc900006a3344cd_0&from=DEL&lang=en&passengers=1&to=LKO&booking_token=ES0vUZvm585Bh07wWQ7YSkrBgwR4EU0hlyPWtVVnFCkhkxVKbHuWJ8JD5YuxiBO8Potyx61ou_q6yOz4Jd6BB1jnD_ImpgdXzVeHWil0xON3kFb_zWzYIbY0o-lhyl4JVQRHOsQ37166GSZkTU-f7fX_puZ_0rei97YX8zNwCFkS2-1uIvo9GcRRt7O5XgCh4cbMTF8E6jDFGConePgxzrpUz0fKTBLrdp3aFjVCTlzbpRKx1WW81KC0R-2jQ9h2326YAoQSsYatDAn25xTv7_yqfSf3l7L3mYRzq317kH-Dd7pdaMvTa_Y2huW32GoPES6Cz5vJsKnG-icJXhTPF_YjlT80xApOnMg1lGjABG5qoj30iWOtpjf0OxjJol2AxwVg9w2WIvonHTrb3zV1ZazhHyPok8K6f4h7U_paBtuA=",
                "facilitated_booking_available": True,
                "pnr_count": 1,
                "has_airport_change": False,
                "technical_stops": 0,
                "throw_away_ticketing": False,
                "hidden_city_ticketing": False,
                "virtual_interlining": False,
                "local_arrival": "2023-02-13T07:15:00.000Z",
                "utc_arrival": "2023-02-13T01:45:00.000Z",
                "local_departure": "2023-02-13T06:10:00.000Z",
                "utc_departure": "2023-02-13T00:40:00.000Z"
            },
            {
                "id": "071104c24bc8000000748581_0",
                "flyFrom": "DEL",
                "flyTo": "LKO",
                "cityFrom": "New Delhi",
                "cityCodeFrom": "DEL",
                "cityTo": "Lucknow",
                "cityCodeTo": "LKO",
                "countryFrom": {
                    "code": "IN",
                    "name": "India"
                },
                "countryTo": {
                    "code": "IN",
                    "name": "India"
                },
                "nightsInDest": "None",
                "quality": 50.666615,
                "distance": 423.95,
                "duration": {
                    "departure": 3900,
                    "return": 0,
                    "total": 3900
                },
                "price": 30,
                "conversion": {
                    "EUR": 30
                },
                "bags_price": {
                    "1": 0
                },
                "baglimit": {
                    "hand_height": 38,
                    "hand_length": 57,
                    "hand_weight": 7,
                    "hand_width": 20,
                    "hold_dimensions_sum": 158,
                    "hold_height": 52,
                    "hold_length": 78,
                    "hold_weight": 15,
                    "hold_width": 28
                },
                "availability": {
                    "seats": 2
                },
                "airlines": [
                    "6E"
                ],
                "route": [
                    {
                        "id": "071104c24bc8000000748581_0",
                        "combination_id": "071104c24bc8000000748581",
                        "flyFrom": "DEL",
                        "flyTo": "LKO",
                        "cityFrom": "New Delhi",
                        "cityCodeFrom": "DEL",
                        "cityTo": "Lucknow",
                        "cityCodeTo": "LKO",
                        "airline": "6E",
                        "flight_no": 2025,
                        "operating_carrier": "6E",
                        "operating_flight_no": "2025",
                        "fare_basis": "R0IP",
                        "fare_category": "M",
                        "fare_classes": "X",
                        "fare_family": "",
                        "return": 0,
                        "bags_recheck_required": False,
                        "vi_connection": False,
                        "guarantee": False,
                        "equipment": "None",
                        "vehicle_type": "aircraft",
                        "local_arrival": "2023-02-12T07:15:00.000Z",
                        "utc_arrival": "2023-02-12T01:45:00.000Z",
                        "local_departure": "2023-02-12T06:10:00.000Z",
                        "utc_departure": "2023-02-12T00:40:00.000Z"
                    }
                ],
                "booking_token": "EbdRPPz1--buEUJSq20Eox56KifnVK50TWzASIKQkH4QNfx5jANQAidIlGEFfv3N3xlSC33y8jXJXGSvYCQ0kZ-cfj5wjLwi7MboBKe16Jrp0qwoisYpt2W5nfProU7qDdBZciLLz-157GKZsuY4G0xF-mWzFm5bqOJdPmXk1KvPZUmDPO2urMu-Hz5MGAWWz4tzn6-m359M5yM4Fd4frPx_kHgAHcSF7L4MYO4N-TlI-EhbIknrwpj38mVCIzvr2JgTx7oF05dxT5FAP7e53a4K1LN3ziE5eV_C1fRFx600EOLlpk3fb66j0MfPOXZcSVvwP0wzX8jXG5bEuOrayBO3W3mWHQd-yt4lGqmhKYPijf39g4EIFpugdpPuc-uUAWAh3lG2bBx4bW87Fh7stucqs2N-gv0S9QYFJnRlU2aoEqYYT027hOFOSvk5fQmcsSJ5sZlYnt-b8Mkkn5riGwJnETGd43ocDMDuhnMdeYuZDgoXott1FhOhWrbqMi2LeXYh9CuJ68XQ6kl1-SgwE1YFD5G99I6XY3hlPln1By38=",
                "deep_link": "https://www.kiwi.com/deep?affilid=apoorvflightsearch&currency=EUR&flightsId=071104c24bc8000000748581_0&from=DEL&lang=en&passengers=1&to=LKO&booking_token=EH5HPj2O98tO49fSVdL4LmMUbxb6JPbMyIGr9qcDJ4pE559RdD47NvpiEYd0cd8PifI0epccQtIFTiDvap8EDAMe0O75UNGrPwvRLXLE4iikiLf3kPd04Wi8Ljsr29Veg4jUfSezTz7hNJ-e3HpnXvrn8dgW5hi9UAcx_4fH8admlFE4yjrdSkoiBAhgLnHb2LAWvZbP2a9o3BkkUbXW4gL4vAyeJ5NFI9QjTN6Zeuw3Jc8aNFBf4TI9yNS_6d-JYfTmNUS_VQjypi0vB5PyIDA4JoP2OcPRNSvuaYIqh62A-ICAZ3hbUAkZyCm4w80It8MMgyHAvKt0Kd7g6Abz8TC_2m92mbT6HUmeiCzjJlnPWMoBh4aMzm6G6XyULCuv_xqJgWfZl0ULw04LdzPoB968TBADjvAfvPh39snyvcf4=",
                "facilitated_booking_available": True,
                "pnr_count": 1,
                "has_airport_change": False,
                "technical_stops": 0,
                "throw_away_ticketing": False,
                "hidden_city_ticketing": False,
                "virtual_interlining": False,
                "local_arrival": "2023-02-12T07:15:00.000Z",
                "utc_arrival": "2023-02-12T01:45:00.000Z",
                "local_departure": "2023-02-12T06:10:00.000Z",
                "utc_departure": "2023-02-12T00:40:00.000Z"
            },
            {
                "id": "071104c24bc90000219bc27d_0",
                "flyFrom": "DEL",
                "flyTo": "LKO",
                "cityFrom": "New Delhi",
                "cityCodeFrom": "DEL",
                "cityTo": "Lucknow",
                "cityCodeTo": "LKO",
                "countryFrom": {
                    "code": "IN",
                    "name": "India"
                },
                "countryTo": {
                    "code": "IN",
                    "name": "India"
                },
                "nightsInDest": "None",
                "quality": 50.666615,
                "distance": 423.95,
                "duration": {
                    "departure": 3900,
                    "return": 0,
                    "total": 3900
                },
                "price": 30,
                "conversion": {
                    "EUR": 30
                },
                "bags_price": {
                    "1": 0
                },
                "baglimit": {
                    "hand_height": 38,
                    "hand_length": 57,
                    "hand_weight": 7,
                    "hand_width": 20,
                    "hold_dimensions_sum": 158,
                    "hold_height": 52,
                    "hold_length": 78,
                    "hold_weight": 15,
                    "hold_width": 28
                },
                "availability": {
                    "seats": 2
                },
                "airlines": [
                    "6E"
                ],
                "route": [
                    {
                        "id": "071104c24bc90000219bc27d_0",
                        "combination_id": "071104c24bc90000219bc27d",
                        "flyFrom": "DEL",
                        "flyTo": "LKO",
                        "cityFrom": "New Delhi",
                        "cityCodeFrom": "DEL",
                        "cityTo": "Lucknow",
                        "cityCodeTo": "LKO",
                        "airline": "6E",
                        "flight_no": 2251,
                        "operating_carrier": "6E",
                        "operating_flight_no": "2251",
                        "fare_basis": "R0IP",
                        "fare_category": "M",
                        "fare_classes": "X",
                        "fare_family": "",
                        "return": 0,
                        "bags_recheck_required": False,
                        "vi_connection": False,
                        "guarantee": False,
                        "equipment": "None",
                        "vehicle_type": "aircraft",
                        "local_arrival": "2023-02-13T20:15:00.000Z",
                        "utc_arrival": "2023-02-13T14:45:00.000Z",
                        "local_departure": "2023-02-13T19:10:00.000Z",
                        "utc_departure": "2023-02-13T13:40:00.000Z"
                    }
                ],
                "booking_token": "EIXscwQ9ZRw1y_12wqN2MW_HPV0w2qr_08TJvlRdqi3I2NScQ6ZRvH_drgICLxsnsaHZnrynON42yw0PAFyOFt3JnWgjyNOEa_NsjW-5cx1pKdKOqFiJJQqzcSSrnxm4-igee2kQWbjYDT7u5yXLckyMflFyufKIM-azo4ZTYez4ONFGyTfY1kFfu5l8-OTxXe3QsPscZqjvKUOxA2z0ET2FlDekGZ9BdvxMmSB4NpVJfHbGlW-S3fhixMkHQh3vnjTYmLgF8U-hbrOWLmu9VZMxyGFQG5tJMMMg1wS8EZWTiNW6jc14ij1YiiHtz4AKDEMcoxLAnew3gfxHkFQlypmO7iuFuRFjq5SRFOVlGb_UF6yF2MmKbbL8kknl0auoIJIvV2EBNlxPay0sGzOfC8yPls0545hu670QTV8pNUhtSF8hPXirxHYfNVRVvtPSnxDpTZOYGFZxYE8EstkAz45AUkfrpMh1pGA9LjtqFWaK3bUDc9WxMUxzDwKnIwWqKZZJFXm96k-supOYthsUqxtBVHcMfs_V6VnXK1B6LfGE=",
                "deep_link": "https://www.kiwi.com/deep?affilid=apoorvflightsearch&currency=EUR&flightsId=071104c24bc90000219bc27d_0&from=DEL&lang=en&passengers=1&to=LKO&booking_token=E3j2c6Fcqidiwj3mkShp3DGL0a0BMUDiEH1QDAJMDP8TBj29EXLnWWpvfroXJTvlXGuN_fYR0WXqV4Pek47jX1nN39hGuNQZ6n7Xdpa3RoK9iHxIhlWcUpy-OplhLndOyVXSP1d10PEprzXxF2LohpBGx6A-Au7AXODpVhWlR_WVWNszw4JS-3izvt8kf3iwTNJO-MBo4IAUi2Lmnmany1rlNQPP3tn0kuSq8mnBTbFV5BQfgEt9gkMs1oSllZz1Rg8xRbwo7x4sirqswjiKjwSNaJB52Sf6LTFQ0XYLqwiRrTSVGAr_s8fWR5ylxLBRK09ryOSXIlhsrJXP7oFibRkKoVre2DukxEykGNbRLZzRwkJ2GpE74-n3Zg0y3jQoMDH7Q8-ZUhVA9om3fCq8z9sFA-IKMvr3kgoWI6KD8QAQ=",
                "facilitated_booking_available": True,
                "pnr_count": 1,
                "has_airport_change": False,
                "technical_stops": 0,
                "throw_away_ticketing": False,
                "hidden_city_ticketing": False,
                "virtual_interlining": False,
                "local_arrival": "2023-02-13T20:15:00.000Z",
                "utc_arrival": "2023-02-13T14:45:00.000Z",
                "local_departure": "2023-02-13T19:10:00.000Z",
                "utc_departure": "2023-02-13T13:40:00.000Z"
            },
            {
                "id": "071104c24bc90000d5cede69_0",
                "flyFrom": "DEL",
                "flyTo": "LKO",
                "cityFrom": "New Delhi",
                "cityCodeFrom": "DEL",
                "cityTo": "Lucknow",
                "cityCodeTo": "LKO",
                "countryFrom": {
                    "code": "IN",
                    "name": "India"
                },
                "countryTo": {
                    "code": "IN",
                    "name": "India"
                },
                "nightsInDest": "None",
                "quality": 51.33328,
                "distance": 423.95,
                "duration": {
                    "departure": 4200,
                    "return": 0,
                    "total": 4200
                },
                "price": 30,
                "conversion": {
                    "EUR": 30
                },
                "bags_price": {
                    "1": 0
                },
                "baglimit": {
                    "hand_height": 38,
                    "hand_length": 57,
                    "hand_weight": 7,
                    "hand_width": 20,
                    "hold_dimensions_sum": 158,
                    "hold_height": 52,
                    "hold_length": 78,
                    "hold_weight": 15,
                    "hold_width": 28
                },
                "availability": {
                    "seats": 2
                },
                "airlines": [
                    "6E"
                ],
                "route": [
                    {
                        "id": "071104c24bc90000d5cede69_0",
                        "combination_id": "071104c24bc90000d5cede69",
                        "flyFrom": "DEL",
                        "flyTo": "LKO",
                        "cityFrom": "New Delhi",
                        "cityCodeFrom": "DEL",
                        "cityTo": "Lucknow",
                        "cityCodeTo": "LKO",
                        "airline": "6E",
                        "flight_no": 789,
                        "operating_carrier": "6E",
                        "operating_flight_no": "789",
                        "fare_basis": "R0IP",
                        "fare_category": "M",
                        "fare_classes": "X",
                        "fare_family": "",
                        "return": 0,
                        "bags_recheck_required": False,
                        "vi_connection": False,
                        "guarantee": False,
                        "equipment": "None",
                        "vehicle_type": "aircraft",
                        "local_arrival": "2023-02-13T22:40:00.000Z",
                        "utc_arrival": "2023-02-13T17:10:00.000Z",
                        "local_departure": "2023-02-13T21:30:00.000Z",
                        "utc_departure": "2023-02-13T16:00:00.000Z"
                    }
                ],
                "booking_token": "Ey6ANwt4T0OJJ_PYEpRXGUxWmDt0tUXelRIRKkbmTASnKDYkIpyghr9yTYC6RpnXOnkXOvoUIT7B9anJsYbUzNTqJWzP_X77t2KsBzcWMel6kjyEBQjh30H21M3LQgwfjl7veP6TxCtduioSfN_xlfv3QVcryfpiOy1PJhPoC3kwdqQjWCorGZLjgyqR5YJ2B0SP1ewCsb07TCICI2_K9pJHKZikHOea6f0VmHwRSAKHpbhyiIQunpQsNXI_DnViJ5ZE09Pm4M-aMs0wyamZzE61TiDFa0trIqCNlrLNeofoymG4QbX7XSzAa6xLvIMws9TvXGv566iJUaygvBmCwOka3dcRgz4fSkJ0oleyu-MzKeXwKE6Nxa09T8YxYdVpJxazLuWjOnxFaqbPeo03NrAZxpO5CDTttq-QQGiBEj6L_2yB65vCHWif4UK57XBauDv3F2TFYqiMfxD9R1o_l7RUx_U60JYabphsn2sjuy5s7gNBROUxr_zZtLWxoNF65CPEEQ6w8JV-kHI-vk7TkQXOIHeD0IflyUy6221ADKLA=",
                "deep_link": "https://www.kiwi.com/deep?affilid=apoorvflightsearch&currency=EUR&flightsId=071104c24bc90000d5cede69_0&from=DEL&lang=en&passengers=1&to=LKO&booking_token=ENyZJssNyd_ubfTN5P7yU6_UJuQwuaL6kyBfUuu_UKGFUg8c9xyeGIff8GNa2Xg7h2uzbRvCZuxDrvcrsoPbIOiBWQMpBB24lF46Othg6o6T-i-2Zs8dewu3gscYe656G1if9djJAaiFEbEBcP209IvhL_Ek9DJDH_70Sy9zWpTeBYMwsVxHmkp-dh1iZoA8kkoxfrdhPaxAKM-TQz96Poz-YrBi6kOvUhZwdHceI2rFgxPYBThtrIL433NwB78OnOvw8btuQbHjVoSCtwRDO4mnRV8T4u52fxRnQqBq4jUARSrua2pFZeolvURvjBUqchZb1T07WsMPsSkL3mmoPevY0n4ldYZ9OC-QkVG9J68JMkPWmFXiL5ChlniHYmEKL18pLtqXWTPoBvd9wiGKP4SltAnjRrAGM5hBGmKygmm8=",
                "facilitated_booking_available": True,
                "pnr_count": 1,
                "has_airport_change": False,
                "technical_stops": 0,
                "throw_away_ticketing": False,
                "hidden_city_ticketing": False,
                "virtual_interlining": False,
                "local_arrival": "2023-02-13T22:40:00.000Z",
                "utc_arrival": "2023-02-13T17:10:00.000Z",
                "local_departure": "2023-02-13T21:30:00.000Z",
                "utc_departure": "2023-02-13T16:00:00.000Z"
            },
            {
                "id": "071104c24bc900004aeee57c_0",
                "flyFrom": "DEL",
                "flyTo": "LKO",
                "cityFrom": "New Delhi",
                "cityCodeFrom": "DEL",
                "cityTo": "Lucknow",
                "cityCodeTo": "LKO",
                "countryFrom": {
                    "code": "IN",
                    "name": "India"
                },
                "countryTo": {
                    "code": "IN",
                    "name": "India"
                },
                "nightsInDest": "None",
                "quality": 51.33328,
                "distance": 423.95,
                "duration": {
                    "departure": 4200,
                    "return": 0,
                    "total": 4200
                },
                "price": 30,
                "conversion": {
                    "EUR": 30
                },
                "bags_price": {
                    "1": 0
                },
                "baglimit": {
                    "hand_height": 38,
                    "hand_length": 57,
                    "hand_weight": 7,
                    "hand_width": 20,
                    "hold_dimensions_sum": 158,
                    "hold_height": 52,
                    "hold_length": 78,
                    "hold_weight": 15,
                    "hold_width": 28
                },
                "availability": {
                    "seats": 2
                },
                "airlines": [
                    "6E"
                ],
                "route": [
                    {
                        "id": "071104c24bc900004aeee57c_0",
                        "combination_id": "071104c24bc900004aeee57c",
                        "flyFrom": "DEL",
                        "flyTo": "LKO",
                        "cityFrom": "New Delhi",
                        "cityCodeFrom": "DEL",
                        "cityTo": "Lucknow",
                        "cityCodeTo": "LKO",
                        "airline": "6E",
                        "flight_no": 2319,
                        "operating_carrier": "6E",
                        "operating_flight_no": "2319",
                        "fare_basis": "R0IP",
                        "fare_category": "M",
                        "fare_classes": "X",
                        "fare_family": "",
                        "return": 0,
                        "bags_recheck_required": False,
                        "vi_connection": False,
                        "guarantee": False,
                        "equipment": "None",
                        "vehicle_type": "aircraft",
                        "local_arrival": "2023-02-13T17:25:00.000Z",
                        "utc_arrival": "2023-02-13T11:55:00.000Z",
                        "local_departure": "2023-02-13T16:15:00.000Z",
                        "utc_departure": "2023-02-13T10:45:00.000Z"
                    }
                ],
                "booking_token": "E83TL3H4QqVNoPoSN110Uu7Mu5f1fIizfN4vy8U753ELCptjiZcsYMXTCquYVGI1nIehKDWOOTS1tD7stTeOBSakVhM0F5Re1lLIgH7adrtevDz_KueP4gSz2e3LW6nju6MJId9OfQh_PCCW1DbuZkaKRi4hagcPccuk4nKWtSp5HVxHOpiahyLB5sxCH3kGHfHO3CfERTZhK1PVsVUTp71C0Ac6jPLLqQz23GILjNZ65oXHLQSu5wBP9wV38dq_RbPdfRhgiRX8Ycdd2FRaCvEH5gz8V23EMduxAl2ixCA1zHbXZiTeWeyYUwW6OFfWpapbTrRB_hSPdtgkjbtouNjKu9JgZGpW1r6pHGswCWJNV3MXyug_hwPIO4DS3Fckq2oa6ct93IxQO9Jbjl416UmcIMpTVPLTm-02XOQ2QAhNEdRsjE9tkEuJps30NxMFLx1Eg_ShTIcRg-aHQyKpBaaf8z9AP6f8CfeQkuqKt-tqLqUXULS-m5XYzgJ_q16a_tPjMCFX1KVNcSvmVOt7R3wgklqXAY2wBcWAyABelLOg=",
                "deep_link": "https://www.kiwi.com/deep?affilid=apoorvflightsearch&currency=EUR&flightsId=071104c24bc900004aeee57c_0&from=DEL&lang=en&passengers=1&to=LKO&booking_token=EshEsLScmuK9ffYLld_wyit_LaJ2IkedfFID4TWTsxFhoUnlYXHBtXpcdnjhnL8q7FpU13SZ1OIX0bEEC7Jcv-vQSSC_vAWRU-h-H0z46XY_DTvijerle3mfPE_OtOdcsvNriFNnGscnhDjLDNrjOc6mS9Kje0tArZAoXA5eNDB2rIA-5o48YTx9VDEHMEXDcmuLixyL8R5IvO5F7wqx4HEwTXGDEMHKu9vbgqsQA5RfKoUrgflAYpjQ3TyFxN5OEj_tv6Oscshjeltae6R03ov_UfeZDC4iP9su4rOTYnzzLOOvu1Q1RVti4CSgTn1OnjI1ApawHPvG24Z6w7EylK3-x523jIaDvJjZyYe84oJ-19Bv6jtCJdL7SjQPRGyaOy8BMJSCBLXRWYya4YVHrf85Qco5c2SyzDnHXJ5bDnfM=",
                "facilitated_booking_available": True,
                "pnr_count": 1,
                "has_airport_change": False,
                "technical_stops": 0,
                "throw_away_ticketing": False,
                "hidden_city_ticketing": False,
                "virtual_interlining": False,
                "local_arrival": "2023-02-13T17:25:00.000Z",
                "utc_arrival": "2023-02-13T11:55:00.000Z",
                "local_departure": "2023-02-13T16:15:00.000Z",
                "utc_departure": "2023-02-13T10:45:00.000Z"
            },
            {
                "id": "071104c24bc90000762a2711_0",
                "flyFrom": "DEL",
                "flyTo": "LKO",
                "cityFrom": "New Delhi",
                "cityCodeFrom": "DEL",
                "cityTo": "Lucknow",
                "cityCodeTo": "LKO",
                "countryFrom": {
                    "code": "IN",
                    "name": "India"
                },
                "countryTo": {
                    "code": "IN",
                    "name": "India"
                },
                "nightsInDest": "None",
                "quality": 52.33328,
                "distance": 423.95,
                "duration": {
                    "departure": 4200,
                    "return": 0,
                    "total": 4200
                },
                "price": 31,
                "conversion": {
                    "EUR": 31
                },
                "bags_price": {
                    "1": 0
                },
                "baglimit": {
                    "hand_height": 36,
                    "hand_length": 56,
                    "hand_weight": 7,
                    "hand_width": 23,
                    "hold_dimensions_sum": 158,
                    "hold_height": 50,
                    "hold_length": 70,
                    "hold_weight": 15,
                    "hold_width": 38
                },
                "availability": {
                    "seats": "None"
                },
                "airlines": [
                    "I5"
                ],
                "route": [
                    {
                        "id": "071104c24bc90000762a2711_0",
                        "combination_id": "071104c24bc90000762a2711",
                        "flyFrom": "DEL",
                        "flyTo": "LKO",
                        "cityFrom": "New Delhi",
                        "cityCodeFrom": "DEL",
                        "cityTo": "Lucknow",
                        "cityCodeTo": "LKO",
                        "airline": "I5",
                        "flight_no": 784,
                        "operating_carrier": "",
                        "operating_flight_no": "",
                        "fare_basis": "KNRA000",
                        "fare_category": "M",
                        "fare_classes": "K",
                        "fare_family": "",
                        "return": 0,
                        "bags_recheck_required": False,
                        "vi_connection": False,
                        "guarantee": False,
                        "equipment": "None",
                        "vehicle_type": "aircraft",
                        "local_arrival": "2023-02-13T17:40:00.000Z",
                        "utc_arrival": "2023-02-13T12:10:00.000Z",
                        "local_departure": "2023-02-13T16:30:00.000Z",
                        "utc_departure": "2023-02-13T11:00:00.000Z"
                    }
                ],
                "booking_token": "EJlcmU4DRnrO-Enz5ZGErpK6H5S3NBeq01u_Y1RiK6uOWX5v_EmqW2wMKiSjbYzi3QexpVZ6w65n3ZFbbNXDHbOn3E0KERZ4qRIdv_LLhtI-s4CVaXspP5BLP0YnMSQg8y4KiQp60qqw-WJNOi1naX1Z_WENgCipALQL-QqYiydZpJeS3TtqhFFJpXkwzA8xJNVw99M-MoeC93i8wpX4BKKwF-edTvDIvOraXZNK-T1SyPJwNY2Ve-HkgWFJoGv8zkIsZtEzTgLUeMF6kVbB-g7sJ15blKi5OIXzGYvC42L9ADClbhsP3cjwdCJdn7-aooZCqVQOECbcUPy1twA-IWUi0R2-Shx1NiLvjlsiPAmVR-hrbRSJCDXGRq8_WegdI6n_8LybvfblvAKZTTvhy9edK87NCzZebDnJF5QiJRl-ncBlmfULlNAS6QxMafWc5Xhsq4c8DRe0RnZFh1gJV-Rh0LoNXATuP21dmQfX3QLvdhMj0Qkx6zC_K7AuMZFX_DnnsV-uk8UOhIGW9glSXJprgTJo5a5lws9IjZ1AwvYDbQ-giY1U6jVIibjPnaYY2",
                "deep_link": "https://www.kiwi.com/deep?affilid=apoorvflightsearch&currency=EUR&flightsId=071104c24bc90000762a2711_0&from=DEL&lang=en&passengers=1&to=LKO&booking_token=EsIBD-ubWjJE0TAT9mXFOrsOGEOdUWm2ZpJN8CRu9BQcJgc6zu77z8STCHO_Esc45BcHGmOBKrbhxDyO-Rk9XgJRC9TIJ0jMcHQIgu3uLPVcea38obKbo4zJty0IsFHvA1SzqsqfKdlf4ojOcEMwRC6QR7dMi5eAqEfWiX6Ju1D6jWyTkBJCN0j6RfL4vSmsclobL3N3H1nfNwk7-KgSPk8wAI-N2AHhAZ7e6ZbztQDxAH9CpJ01x4ttIf_IhSV2bACGnYvMf4DbaTc-aaX1PuDarRAavhg_1dk-do1GRIqfzHi-lX_ieTBB34sJueEHZFSDcOtqvBjqO5utN7tYsKeoKKLaeUavQ1NdCheCapWbME4EAi2kJieLh77erUZWORcJ7TKCayPTtRSpqLk8tyLp3LxZjWlQWkC8z9sHwbCQ=",
                "facilitated_booking_available": True,
                "pnr_count": 1,
                "has_airport_change": False,
                "technical_stops": 0,
                "throw_away_ticketing": False,
                "hidden_city_ticketing": False,
                "virtual_interlining": False,
                "local_arrival": "2023-02-13T17:40:00.000Z",
                "utc_arrival": "2023-02-13T12:10:00.000Z",
                "local_departure": "2023-02-13T16:30:00.000Z",
                "utc_departure": "2023-02-13T11:00:00.000Z"
            },
            {
                "id": "071104c24bc90000d0adf058_0",
                "flyFrom": "DEL",
                "flyTo": "LKO",
                "cityFrom": "New Delhi",
                "cityCodeFrom": "DEL",
                "cityTo": "Lucknow",
                "cityCodeTo": "LKO",
                "countryFrom": {
                    "code": "IN",
                    "name": "India"
                },
                "countryTo": {
                    "code": "IN",
                    "name": "India"
                },
                "nightsInDest": "None",
                "quality": 52.999945,
                "distance": 423.95,
                "duration": {
                    "departure": 4500,
                    "return": 0,
                    "total": 4500
                },
                "price": 31,
                "conversion": {
                    "EUR": 31
                },
                "bags_price": {
                    "1": 0
                },
                "baglimit": {
                    "hand_height": 36,
                    "hand_length": 56,
                    "hand_weight": 7,
                    "hand_width": 23,
                    "hold_dimensions_sum": 158,
                    "hold_height": 50,
                    "hold_length": 70,
                    "hold_weight": 15,
                    "hold_width": 38
                },
                "availability": {
                    "seats": "None"
                },
                "airlines": [
                    "I5"
                ],
                "route": [
                    {
                        "id": "071104c24bc90000d0adf058_0",
                        "combination_id": "071104c24bc90000d0adf058",
                        "flyFrom": "DEL",
                        "flyTo": "LKO",
                        "cityFrom": "New Delhi",
                        "cityCodeFrom": "DEL",
                        "cityTo": "Lucknow",
                        "cityCodeTo": "LKO",
                        "airline": "I5",
                        "flight_no": 548,
                        "operating_carrier": "I5",
                        "operating_flight_no": "548",
                        "fare_basis": "KNRA000",
                        "fare_category": "M",
                        "fare_classes": "K",
                        "fare_family": "",
                        "return": 0,
                        "bags_recheck_required": False,
                        "vi_connection": False,
                        "guarantee": False,
                        "equipment": "None",
                        "vehicle_type": "aircraft",
                        "local_arrival": "2023-02-13T08:25:00.000Z",
                        "utc_arrival": "2023-02-13T02:55:00.000Z",
                        "local_departure": "2023-02-13T07:10:00.000Z",
                        "utc_departure": "2023-02-13T01:40:00.000Z"
                    }
                ],
                "booking_token": "E6TaMuWl9030XTUFEDsrD1xpPqA7OfofINLNMskJ6wLfOgq9EIHOnqcnYpycm_l7mogfuBYHtVhiGs7lJEsE7zO9Os7d84KS3XcY0njGsHrzfpnokPyBdt8Qi8U21xSFYrWvVbjDvZBz9F3jdHLMojJeioMbiXIoxQ8qluIowAU30OpjqKUOz1TDkICoa8_CBThnUeaBbZHZaJ4hhQdvBHV56BNynDYAP_LZTD805Eh2RmE9wanb-H2pxxhq4xjqnyOAQhG1fM3IPfUfxv809PZzqJT4N-f7EoTN0cuUyY8xEyYGgPU1pDuQT0Ke-RZlDe-EKpX6Cd7pVHfahgGweBAxP84L7PXLTNvQIB3O5ggHHxxTJpNgE4vlgpC9z9rKc8rMHazaIopqLwWGiYqcGkZ8hk4vpJh-wiBRG3kruqIJraLZXJ-DLZjOWVCaaDtyToWRx_alZNQiNAuA1ReGs1SrzbLfMPSRks7ub-s3FyizTI-WjmljA3FF2zSf-io7TUOZCOiHtyvur9NKQgV5gtz_Ui5ASgXRYGgLzlMIE-eaBnG6XC9RMk-lzz4dUa-tS",
                "deep_link": "https://www.kiwi.com/deep?affilid=apoorvflightsearch&currency=EUR&flightsId=071104c24bc90000d0adf058_0&from=DEL&lang=en&passengers=1&to=LKO&booking_token=ElMlYgo7gMGHwyQsGzeVG7p1ezpWSsegdJf8oTREBt8x0EoLkhS6y7ZWEzgEjwnDcmdffPeb2q_KpVFAAk9qhDa_lQhiV2GWjywxk6YGUFHeMpW0A7ACBZbioiqhVF1UvH4dHMHhldF4Oc0dwk8zImo8VIabdg-GDC-JUEG-folsLmb4ktLbucYvKbmzpEbH-8g5ZV7IDy-6zy9nbyThHrPaMFp7INLdCHhcL2wuHTxiiCu8QGGo4e7NxzoxE_6IctGeecCWAqX7qr9gIZjn5Ie28zerx5bGE4uOdx07Sbv4l1xAKW4EWdAnnxStAwKusuIORuUWhmNb5nYXxsn82i9s1wETmzL_saRMq_Y6APspYBSl0A854bx15PaDEwPQ6AylTRw-mhGfpXqNg_ql-VrvQxl9BE3daxfjPeS3CYp_AMp0C8hUGLe6m9j7bTGjM",
                "facilitated_booking_available": True,
                "pnr_count": 1,
                "has_airport_change": False,
                "technical_stops": 0,
                "throw_away_ticketing": False,
                "hidden_city_ticketing": False,
                "virtual_interlining": False,
                "local_arrival": "2023-02-13T08:25:00.000Z",
                "utc_arrival": "2023-02-13T02:55:00.000Z",
                "local_departure": "2023-02-13T07:10:00.000Z",
                "utc_departure": "2023-02-13T01:40:00.000Z"
            },
            {
                "id": "071104c24bc7000037e21f9b_0",
                "flyFrom": "DEL",
                "flyTo": "LKO",
                "cityFrom": "New Delhi",
                "cityCodeFrom": "DEL",
                "cityTo": "Lucknow",
                "cityCodeTo": "LKO",
                "countryFrom": {
                    "code": "IN",
                    "name": "India"
                },
                "countryTo": {
                    "code": "IN",
                    "name": "India"
                },
                "nightsInDest": "None",
                "quality": 53.33328,
                "distance": 423.95,
                "duration": {
                    "departure": 4200,
                    "return": 0,
                    "total": 4200
                },
                "price": 32,
                "conversion": {
                    "EUR": 32
                },
                "bags_price": {
                    "1": 0
                },
                "baglimit": {
                    "hand_height": 38,
                    "hand_length": 57,
                    "hand_weight": 7,
                    "hand_width": 20,
                    "hold_dimensions_sum": 158,
                    "hold_height": 52,
                    "hold_length": 78,
                    "hold_weight": 15,
                    "hold_width": 28
                },
                "availability": {
                    "seats": 2
                },
                "airlines": [
                    "6E"
                ],
                "route": [
                    {
                        "id": "071104c24bc7000037e21f9b_0",
                        "combination_id": "071104c24bc7000037e21f9b",
                        "flyFrom": "DEL",
                        "flyTo": "LKO",
                        "cityFrom": "New Delhi",
                        "cityCodeFrom": "DEL",
                        "cityTo": "Lucknow",
                        "cityCodeTo": "LKO",
                        "airline": "6E",
                        "flight_no": 2376,
                        "operating_carrier": "6E",
                        "operating_flight_no": "2376",
                        "fare_basis": "R0IP",
                        "fare_category": "M",
                        "fare_classes": "X",
                        "fare_family": "",
                        "return": 0,
                        "bags_recheck_required": False,
                        "vi_connection": False,
                        "guarantee": False,
                        "equipment": "None",
                        "vehicle_type": "aircraft",
                        "local_arrival": "2023-02-11T19:00:00.000Z",
                        "utc_arrival": "2023-02-11T13:30:00.000Z",
                        "local_departure": "2023-02-11T17:50:00.000Z",
                        "utc_departure": "2023-02-11T12:20:00.000Z"
                    }
                ],
                "booking_token": "Ewu4Xk6XFM02Ke_rLoafH7199xUBKPhr_wliDtnXE_s1tucUbq10mn1dPFGrZ91Jpgt0STBUqobY4_PPFeesnyTtf63ico2O7rDnrn9c6VlDF4Sj35-kzEd7EaVxNVyavJBPyVrXYiupYO5W8NUMwFGYRkuGYxVCcy_dPYHKG0sOsV5HhsTjbMbZSd7y5XVJsaS89SDCu1BC2swvZvBMN96ivG-xKgWcoft9JYrI2yKQT9IPskt3DqUUfwIPwBZydNwc3AmU87eb9UKDX8w0SwNEiXqDDh0XUKJzj3NK8geOrPu9sSxxp7B8AfSS_l6i2s-BH0vOCsuL8Nh7_f0WDZodPBlscExXtgXI5G8Sk7oj54VGohi8pqS19mdHQAleZQJ4jucJj4TShIZn8LkXVDeY7yzYof4-CdUzCTosUoySpameHrRVy99BQ_38l0hDeW5p1ERAnidNxUm8j15h5y8FXP0KkB6sdM4az0DUAhr5_egDtXGmMH8lK7YY5SrFPcoOwoWVCP1TE3LUAJxx8SDnaUsntNqbMW-nZ0ypxm1c=",
                "deep_link": "https://www.kiwi.com/deep?affilid=apoorvflightsearch&currency=EUR&flightsId=071104c24bc7000037e21f9b_0&from=DEL&lang=en&passengers=1&to=LKO&booking_token=ELuMR5BUz6U2USGo6-51lIFYjWdn8bfJe9ZBs5Fal0_yaJo2v3PNoGqGjfxnL21hlsMQIUaIkx-v9XnJt21O3Ze7dBxvhQiTlCM3mhRC2MDd60yMvog3wG87tCMgU_CtuvT2C3RpkEkHOSVxvz7E_z-GOez9JKaSblLZjEAXgfPcibf9wcRMq7-k1R_NK_liv4mzUUczNUhLZKWRe_zO7mWw-owYDjciPRpEnUfZD188JX-wLYHiB1aD0cUhZeAw7DJctiW-omndaMfMB3uVbk6igEUIAKLwCbgX94mBTzZ6VPGy44crpfAkO6X7p9SwnMj1eJnfsTsXvuFsd2bA4A-h2NYVWuXrgbDd47utyOP_VXBQG5XaySGbYp8WOvIz37CzX9lZ0-dCHzrCe9cJYmXJiP6Uvbp3tIj2JPfD-cUU=",
                "facilitated_booking_available": True,
                "pnr_count": 1,
                "has_airport_change": False,
                "technical_stops": 0,
                "throw_away_ticketing": False,
                "hidden_city_ticketing": False,
                "virtual_interlining": False,
                "local_arrival": "2023-02-11T19:00:00.000Z",
                "utc_arrival": "2023-02-11T13:30:00.000Z",
                "local_departure": "2023-02-11T17:50:00.000Z",
                "utc_departure": "2023-02-11T12:20:00.000Z"
            },
            {
                "id": "071104c24bc900008c0b5f6b_0",
                "flyFrom": "DEL",
                "flyTo": "LKO",
                "cityFrom": "New Delhi",
                "cityCodeFrom": "DEL",
                "cityTo": "Lucknow",
                "cityCodeTo": "LKO",
                "countryFrom": {
                    "code": "IN",
                    "name": "India"
                },
                "countryTo": {
                    "code": "IN",
                    "name": "India"
                },
                "nightsInDest": "None",
                "quality": 53.33328,
                "distance": 423.95,
                "duration": {
                    "departure": 4200,
                    "return": 0,
                    "total": 4200
                },
                "price": 32,
                "conversion": {
                    "EUR": 32
                },
                "bags_price": {
                    "1": 0
                },
                "baglimit": {
                    "hand_height": 38,
                    "hand_length": 57,
                    "hand_weight": 7,
                    "hand_width": 20,
                    "hold_dimensions_sum": 158,
                    "hold_height": 52,
                    "hold_length": 78,
                    "hold_weight": 15,
                    "hold_width": 28
                },
                "availability": {
                    "seats": 2
                },
                "airlines": [
                    "6E"
                ],
                "route": [
                    {
                        "id": "071104c24bc900008c0b5f6b_0",
                        "combination_id": "071104c24bc900008c0b5f6b",
                        "flyFrom": "DEL",
                        "flyTo": "LKO",
                        "cityFrom": "New Delhi",
                        "cityCodeFrom": "DEL",
                        "cityTo": "Lucknow",
                        "cityCodeTo": "LKO",
                        "airline": "6E",
                        "flight_no": 2376,
                        "operating_carrier": "6E",
                        "operating_flight_no": "2376",
                        "fare_basis": "R0IP",
                        "fare_category": "M",
                        "fare_classes": "X",
                        "fare_family": "",
                        "return": 0,
                        "bags_recheck_required": False,
                        "vi_connection": False,
                        "guarantee": False,
                        "equipment": "None",
                        "vehicle_type": "aircraft",
                        "local_arrival": "2023-02-13T19:00:00.000Z",
                        "utc_arrival": "2023-02-13T13:30:00.000Z",
                        "local_departure": "2023-02-13T17:50:00.000Z",
                        "utc_departure": "2023-02-13T12:20:00.000Z"
                    }
                ],
                "booking_token": "EP7mdD76iyIZfG4YwXDYM97yS71aD4UgUJRwypfCEXtSyRmiVFnaMxLmEE9eCXRRFEW3a4f74QO0Qs1emtM-7EP_cx2c0MDmgAuzdEJRBuUH7W9T-r368kWaO_IhitCB4jybIh0Ria1_rL6gfOoWWzX9RDEy_yEmxE4_8ni3iveuWV_gdKXpCI8uYqKDiz_0Trz7cbvb7KSvhDS3b4pWHMQ7O3E1-82UhKlctc2g-lcY_j6PcZ12icOLTn262GhNOQ6OmSYWuVkS8lnb9FPAG9_T8M4q9TiewvH0JnJiodpQ-iyncy3_NJc0jtb61_lDbZO-mUMaP2P69G8lWIGflrOcraHJshRCfn_bGm1oXm74NYpW_pwVkbSwgslMCghhpoBRy_SbVOzLjBD5zmcK3L_crTlu6YQmWnaMwpJOsUmxpx2u7Sjg8Aj9xlqibpSnVIi9ml5LDyALdZvXYEvWFHC1PMPUDm6yFbjqtT794xd89ckzIuwg6T3GbTmVqd_sevMUqeuVzWEXpuuIfbnqQ63PClFPV0SiG7yNQyvrap0yc08woLlIn96M8IThrk_XM",
                "deep_link": "https://www.kiwi.com/deep?affilid=apoorvflightsearch&currency=EUR&flightsId=071104c24bc900008c0b5f6b_0&from=DEL&lang=en&passengers=1&to=LKO&booking_token=Eroba9d17koc_nSOIhbUGSbivN7aXjgyLUfewG1abf91FA0ya1hvq3dpPpkYwSetCAJ4FdPRvIachx5qsLzMoQHi2Cn7l9d0dcwiYxEgtMrMxzrV08zjBKmwJEQzQES_kgYOO_kpQoTv9BOmoJgf2P8B9s4QE-TbGclpqCFtpGTpBci8qnLjP0GAxavAuJxKJchp1ZsSSrttmDX6BqZdEVMmOruWxn6KhvZVPai5GXZqJOTYZeV5fNUPTk86R0ybSY7tGfjuQl04f5cwcPlIY-DNS7hraXD34v-hx4gJWU1wr-7Uc7OIOx0E8cF5rep5WD6eZsar1ECGX06wY56xFdXcXjfWBUg9L26DJxse-Lg-rqlqsvONGfjZmWeTMc3F1A-ooxql_mpN6lHfsgn1mVfP504jhVMeenKbeH7s4pWk=",
                "facilitated_booking_available": True,
                "pnr_count": 1,
                "has_airport_change": False,
                "technical_stops": 0,
                "throw_away_ticketing": False,
                "hidden_city_ticketing": False,
                "virtual_interlining": False,
                "local_arrival": "2023-02-13T19:00:00.000Z",
                "utc_arrival": "2023-02-13T13:30:00.000Z",
                "local_departure": "2023-02-13T17:50:00.000Z",
                "utc_departure": "2023-02-13T12:20:00.000Z"
            },
            {
                "id": "071104c24bc80000e64c9e27_0",
                "flyFrom": "DEL",
                "flyTo": "LKO",
                "cityFrom": "New Delhi",
                "cityCodeFrom": "DEL",
                "cityTo": "Lucknow",
                "cityCodeTo": "LKO",
                "countryFrom": {
                    "code": "IN",
                    "name": "India"
                },
                "countryTo": {
                    "code": "IN",
                    "name": "India"
                },
                "nightsInDest": "None",
                "quality": 53.33328,
                "distance": 423.95,
                "duration": {
                    "departure": 4200,
                    "return": 0,
                    "total": 4200
                },
                "price": 32,
                "conversion": {
                    "EUR": 32
                },
                "bags_price": {
                    "1": 0
                },
                "baglimit": {
                    "hand_height": 38,
                    "hand_length": 57,
                    "hand_weight": 7,
                    "hand_width": 20,
                    "hold_dimensions_sum": 158,
                    "hold_height": 52,
                    "hold_length": 78,
                    "hold_weight": 15,
                    "hold_width": 28
                },
                "availability": {
                    "seats": 2
                },
                "airlines": [
                    "6E"
                ],
                "route": [
                    {
                        "id": "071104c24bc80000e64c9e27_0",
                        "combination_id": "071104c24bc80000e64c9e27",
                        "flyFrom": "DEL",
                        "flyTo": "LKO",
                        "cityFrom": "New Delhi",
                        "cityCodeFrom": "DEL",
                        "cityTo": "Lucknow",
                        "cityCodeTo": "LKO",
                        "airline": "6E",
                        "flight_no": 2376,
                        "operating_carrier": "6E",
                        "operating_flight_no": "2376",
                        "fare_basis": "R0IP",
                        "fare_category": "M",
                        "fare_classes": "X",
                        "fare_family": "",
                        "return": 0,
                        "bags_recheck_required": False,
                        "vi_connection": False,
                        "guarantee": False,
                        "equipment": "None",
                        "vehicle_type": "aircraft",
                        "local_arrival": "2023-02-12T19:00:00.000Z",
                        "utc_arrival": "2023-02-12T13:30:00.000Z",
                        "local_departure": "2023-02-12T17:50:00.000Z",
                        "utc_departure": "2023-02-12T12:20:00.000Z"
                    }
                ],
                "booking_token": "EGVTDbvcUmNEaW963tDgfYKu6P3QD3at4DUCB6fZ9hiDSTkHmQeVGuGszTosazxS9JzZiWk9y07XRUJENlg9EvRDMJVZLea-ls2EDj88FTl9zL3mqpYfRNhb6UYTGS20c4Wa4w3cmlRv67edEsjZWgiq42NT1Qg24_XT0YiFjsaUx493zS0uKR7frl3ca5arXCe1NoZAautR7QsnEKwuWEOu9jjt5MYAyGxjjRLL8-m1-YW1dkKr_Wwe_OiBe7Bdpp-RBkJQ_4RJLQ_NbhsNEcKgLP71aopz34W9sfcJeWZ1o5Z-MLr_oAYdhLzMLFaI9WbKG725YOVJKWfs1rD7ur9cSi-aAXDG5dDXBWH_89bH9736pe3CK_8JrS776APuIIhNLt3r_MfdhdqwB4OfzvMiqIshLLm5lZHL8ehpOvGabktm7TGOHViLpBo0GVfSopB9YQyoLJDBnKt2bILMywgDZVfEE90TC8_W74SmothfEdDWWp-7JdPuk3IV6oGow1QV9zoVHZawv9y_GiwQJiqbyPQqzkdZRkPC2Ae_Gp88xnfdzD5R6bCm_jnYwsvtE",
                "deep_link": "https://www.kiwi.com/deep?affilid=apoorvflightsearch&currency=EUR&flightsId=071104c24bc80000e64c9e27_0&from=DEL&lang=en&passengers=1&to=LKO&booking_token=EORyeD7NG3uVwHtdDV3pP7EA7HZ5e3twAjUl5DHybVIBmPocDVvlvNHfB3InKnVeyLZ0Kd_T_ESFHjLNhzGWdSUo-mRW97NC3wILYruNjc9emnf4ez3PxLo5DS233JjfEs3XeXWeR_uA1lmHfeqnUptffMdU7n7DYjc7MWdZEgbkvzbgJRyn8A6lTAN-WkOGJ-reIGDrIf3-bi-gNpGzg0rMiDcRfjpoyfJp7wzv3ur7HoaocFRt4kuuF5BOBqdI40oyUjD0ANnbaw-b1GhRxI06WpvUPfGJNlPZN2s0A-pn_RsHx9W4Ws-7WdoOiFLZY5W17QOYpDtvalP48wjaBKh1VXEu0lyZtZcUldR8aVf1khvuojk5XJx4hrGesVZxi8WxKR52qReoSloZhSA_kzryOnyOW4IxozdP6iqCehTg=",
                "facilitated_booking_available": True,
                "pnr_count": 1,
                "has_airport_change": False,
                "technical_stops": 0,
                "throw_away_ticketing": False,
                "hidden_city_ticketing": False,
                "virtual_interlining": False,
                "local_arrival": "2023-02-12T19:00:00.000Z",
                "utc_arrival": "2023-02-12T13:30:00.000Z",
                "local_departure": "2023-02-12T17:50:00.000Z",
                "utc_departure": "2023-02-12T12:20:00.000Z"
            },
            {
                "id": "071104c24bc8000081cb9900_0",
                "flyFrom": "DEL",
                "flyTo": "LKO",
                "cityFrom": "New Delhi",
                "cityCodeFrom": "DEL",
                "cityTo": "Lucknow",
                "cityCodeTo": "LKO",
                "countryFrom": {
                    "code": "IN",
                    "name": "India"
                },
                "countryTo": {
                    "code": "IN",
                    "name": "India"
                },
                "nightsInDest": "None",
                "quality": 55.33328,
                "distance": 423.95,
                "duration": {
                    "departure": 4200,
                    "return": 0,
                    "total": 4200
                },
                "price": 34,
                "conversion": {
                    "EUR": 34
                },
                "bags_price": {
                    "1": 0
                },
                "baglimit": {
                    "hand_height": 36,
                    "hand_length": 56,
                    "hand_weight": 7,
                    "hand_width": 23,
                    "hold_dimensions_sum": 158,
                    "hold_height": 50,
                    "hold_length": 70,
                    "hold_weight": 15,
                    "hold_width": 38
                },
                "availability": {
                    "seats": "None"
                },
                "airlines": [
                    "I5"
                ],
                "route": [
                    {
                        "id": "071104c24bc8000081cb9900_0",
                        "combination_id": "071104c24bc8000081cb9900",
                        "flyFrom": "DEL",
                        "flyTo": "LKO",
                        "cityFrom": "New Delhi",
                        "cityCodeFrom": "DEL",
                        "cityTo": "Lucknow",
                        "cityCodeTo": "LKO",
                        "airline": "I5",
                        "flight_no": 784,
                        "operating_carrier": "",
                        "operating_flight_no": "",
                        "fare_basis": "ENRA000",
                        "fare_category": "M",
                        "fare_classes": "E",
                        "fare_family": "",
                        "return": 0,
                        "bags_recheck_required": False,
                        "vi_connection": False,
                        "guarantee": False,
                        "equipment": "None",
                        "vehicle_type": "aircraft",
                        "local_arrival": "2023-02-12T17:40:00.000Z",
                        "utc_arrival": "2023-02-12T12:10:00.000Z",
                        "local_departure": "2023-02-12T16:30:00.000Z",
                        "utc_departure": "2023-02-12T11:00:00.000Z"
                    }
                ],
                "booking_token": "EuR5KG1cxXEuBrmHtgTFu1qYTf5_Z3CZtXaBiSgSc3HOMaVUI2oyf3zdeEPlL0dAsnRXkhYupLD1WFX7iTv0yY3_8XfY4-M8ZDCDXgrtRo7ze0VljQEX0fJ1enO-ml26CyKtbilP4vq5HZPqew9EKB5NRfvEwP010woOGiXIPWhc8m4dHgn9KK_Gd78eSCNF2mGf2y1lUeBPyjQXPQOWNYRSYuudTf5nGs4Lqnb-bRotrQDCeKq7IWgpibgCuLZDjBWo61YqkDoQkH3DcehEKWCbdpmpPEF16onQ_vA54z49rzlxv_K-6ITgOfvinvNy3Xxch8D-STEVY3Xibf2WrQlESOkfH1_8-3m_yyesNrnMZEX6CoWHegPGWTyXQZHgh6d0G71vM5lq0WNTyPGCtTsZBS41D75pdeKVlvf4Mm9wmwetQV9aL0poyNEIFd9MsKTOkMEVANz8y-cVwPCgclEHRnn9FQj2nsxzQC6Nc_eF5TlEywzVWoD0u_tfUFQu1m4zmO-_axe5HcIvDwFxA_aXghHOiVuKciqpF2IUdYEVwq5Kih2y3G8EEoM_WkLZ4",
                "deep_link": "https://www.kiwi.com/deep?affilid=apoorvflightsearch&currency=EUR&flightsId=071104c24bc8000081cb9900_0&from=DEL&lang=en&passengers=1&to=LKO&booking_token=EixlkA0lRoavMLmQLme3EXrizdW5OZYr8iato6LWDn_dzEG8tWZkbUz9KJ6Av7bIOJez_F5pojKFMR5h1HLay7CHRuIPwE6MgyzCrfR_TyULpA1Wk4uCMUJAvTTHAqkgdheMTx5DxHxxcdrl5TD_nC7jDP3eQL1ozMvlqHQT-CV4gHmcnHXFd8fQKEB0wkIIFDBX85SbZB93FHzy_DOoSBLn67OyI0z53xtjt4byhsYOKK5kcv8Q3z0cmYPtei8T1hUaE88lOQ0bq6jwknZUSAieEJn05_4yYit-aXQo_HNHkh5tNLZZ4EevFL4E8zxNjJuqHAH-ZMzs_S9SOGUDTDFQmxijaA0LMsU1Mg1RHUU3jF4RFTycmBmSiWLjUuf6RD8btnafeMZb3IQa28n5AM-tQuUgUkEre6g-ZDseCOFE=",
                "facilitated_booking_available": True,
                "pnr_count": 1,
                "has_airport_change": False,
                "technical_stops": 0,
                "throw_away_ticketing": False,
                "hidden_city_ticketing": False,
                "virtual_interlining": False,
                "local_arrival": "2023-02-12T17:40:00.000Z",
                "utc_arrival": "2023-02-12T12:10:00.000Z",
                "local_departure": "2023-02-12T16:30:00.000Z",
                "utc_departure": "2023-02-12T11:00:00.000Z"
            },
            {
                "id": "071104c24bc90000ad98588b_0",
                "flyFrom": "DEL",
                "flyTo": "LKO",
                "cityFrom": "New Delhi",
                "cityCodeFrom": "DEL",
                "cityTo": "Lucknow",
                "cityCodeTo": "LKO",
                "countryFrom": {
                    "code": "IN",
                    "name": "India"
                },
                "countryTo": {
                    "code": "IN",
                    "name": "India"
                },
                "nightsInDest": "None",
                "quality": 55.33328,
                "distance": 423.95,
                "duration": {
                    "departure": 4200,
                    "return": 0,
                    "total": 4200
                },
                "price": 34,
                "conversion": {
                    "EUR": 34
                },
                "bags_price": {
                    "1": 0
                },
                "baglimit": {
                    "hand_height": 36,
                    "hand_length": 56,
                    "hand_weight": 7,
                    "hand_width": 23,
                    "hold_dimensions_sum": 158,
                    "hold_height": 50,
                    "hold_length": 70,
                    "hold_weight": 15,
                    "hold_width": 38
                },
                "availability": {
                    "seats": "None"
                },
                "airlines": [
                    "I5"
                ],
                "route": [
                    {
                        "id": "071104c24bc90000ad98588b_0",
                        "combination_id": "071104c24bc90000ad98588b",
                        "flyFrom": "DEL",
                        "flyTo": "LKO",
                        "cityFrom": "New Delhi",
                        "cityCodeFrom": "DEL",
                        "cityTo": "Lucknow",
                        "cityCodeTo": "LKO",
                        "airline": "I5",
                        "flight_no": 745,
                        "operating_carrier": "I5",
                        "operating_flight_no": "745",
                        "fare_basis": "ENRA000",
                        "fare_category": "M",
                        "fare_classes": "E",
                        "fare_family": "",
                        "return": 0,
                        "bags_recheck_required": False,
                        "vi_connection": False,
                        "guarantee": False,
                        "equipment": "None",
                        "vehicle_type": "aircraft",
                        "local_arrival": "2023-02-13T14:25:00.000Z",
                        "utc_arrival": "2023-02-13T08:55:00.000Z",
                        "local_departure": "2023-02-13T13:15:00.000Z",
                        "utc_departure": "2023-02-13T07:45:00.000Z"
                    }
                ],
                "booking_token": "Eu_LhuF16N3fSGCjHlyNkux_NTS8MqqkQfGC_EmZmHAYSmKZNaARDGV9pkB8JgWIhKjunYOVecWpCqAfRV8epNYhElTULruoyaCGtkouV9dTIImbRnkF3IskOcOKkHr4PFQHAPfn35tnO94E6yL4jPuNZSZ6OKsJK9aCFPE2nCNVaTewzQ-IGW2EVgeiZWx-ItkfLTRHXDYLDbnpXeKnZQHHLpq3JbCc7Lq0ZJG0VoyA2L2zSqkCL1p7GK8fmcPEYhHZJIDCZU7J0DTk1W8tZRmry01F5G7-QxIp3xw4PkE2bVSECmvCRlALRLilLRag8p3vv_6-ChfqEDQpTS5w__KoHlipV-Kbjja5n195u3GvouqDnNBh-P8OkT5CDTFBzbFaKe5l48iftaAqSE5gGUPggEfXE7AMRfqGxPqQHLKefQjN9n_eWUotN51PCIsTRV4nrZfmfMpy3dX_zakkDC-rNXvtHaNfuRMI7T23O4QQzlRdPAfAJDhMH9wPXYJ_ClAcVaHvTncfQv44HyY1qh2ZeOS7ag7Kv9E-3ofNICvKrx-SIZgpaRTdHFTjk3n0L",
                "deep_link": "https://www.kiwi.com/deep?affilid=apoorvflightsearch&currency=EUR&flightsId=071104c24bc90000ad98588b_0&from=DEL&lang=en&passengers=1&to=LKO&booking_token=EgsoYHlO8BGcTTY5EdrqEquZzz0iG3QcZ1iRppLhk2vQHw3X_fcSG7Me2DMKhKkrSglMy7-VLd-n04evGZsDOHgurSNEj9EvdqJyn3_n6_fRXcc-jhbIHdrzPWDlEZRR7dT0Hfxy69VghO6FH9V_jgeNwLKe9ykeOj15-2aaDfQgIX-Im_yjT3W8rtKBgzG-GVYNR4idOUq8lD44Wfp95kxpeO06oW-_hapT2yfVrSxYXY7KXS_gzZEsdqZ36ldUdIPrDkGUQ7EQMuFslMfWJ5q07Rdeq45tccQtUNXy3uI_IYz48fZYjoxoUICI7Ix6OiVnT7FynSN-GTGdh_Qj0eK4SecSAt_UNoiu1t5CQ0bdw2LMllPth7wvnFGMLgjkMZWjkTKEMFFf9ayUeQIPAIM3A09D8jxrtgo0UNuunCBQ=",
                "facilitated_booking_available": True,
                "pnr_count": 1,
                "has_airport_change": False,
                "technical_stops": 0,
                "throw_away_ticketing": False,
                "hidden_city_ticketing": False,
                "virtual_interlining": False,
                "local_arrival": "2023-02-13T14:25:00.000Z",
                "utc_arrival": "2023-02-13T08:55:00.000Z",
                "local_departure": "2023-02-13T13:15:00.000Z",
                "utc_departure": "2023-02-13T07:45:00.000Z"
            },
            {
                "id": "071104c24bc80000274c4e49_0",
                "flyFrom": "DEL",
                "flyTo": "LKO",
                "cityFrom": "New Delhi",
                "cityCodeFrom": "DEL",
                "cityTo": "Lucknow",
                "cityCodeTo": "LKO",
                "countryFrom": {
                    "code": "IN",
                    "name": "India"
                },
                "countryTo": {
                    "code": "IN",
                    "name": "India"
                },
                "nightsInDest": "None",
                "quality": 55.999945,
                "distance": 423.95,
                "duration": {
                    "departure": 4500,
                    "return": 0,
                    "total": 4500
                },
                "price": 34,
                "conversion": {
                    "EUR": 34
                },
                "bags_price": {
                    "1": 0
                },
                "baglimit": {
                    "hand_height": 36,
                    "hand_length": 56,
                    "hand_weight": 7,
                    "hand_width": 23,
                    "hold_dimensions_sum": 158,
                    "hold_height": 50,
                    "hold_length": 70,
                    "hold_weight": 15,
                    "hold_width": 38
                },
                "availability": {
                    "seats": "None"
                },
                "airlines": [
                    "I5"
                ],
                "route": [
                    {
                        "id": "071104c24bc80000274c4e49_0",
                        "combination_id": "071104c24bc80000274c4e49",
                        "flyFrom": "DEL",
                        "flyTo": "LKO",
                        "cityFrom": "New Delhi",
                        "cityCodeFrom": "DEL",
                        "cityTo": "Lucknow",
                        "cityCodeTo": "LKO",
                        "airline": "I5",
                        "flight_no": 548,
                        "operating_carrier": "",
                        "operating_flight_no": "",
                        "fare_basis": "ENRA000",
                        "fare_category": "M",
                        "fare_classes": "E",
                        "fare_family": "",
                        "return": 0,
                        "bags_recheck_required": False,
                        "vi_connection": False,
                        "guarantee": False,
                        "equipment": "None",
                        "vehicle_type": "aircraft",
                        "local_arrival": "2023-02-12T08:25:00.000Z",
                        "utc_arrival": "2023-02-12T02:55:00.000Z",
                        "local_departure": "2023-02-12T07:10:00.000Z",
                        "utc_departure": "2023-02-12T01:40:00.000Z"
                    }
                ],
                "booking_token": "ECfZ84Lkt7G6BRqJjgmkkC_19vBumSdHWXkEA9iqtNIr2HIm5afT8j24wj5VCGugBwwoC1b4pRbH-C8mlVatHwH6LlaV4MelKEX6FVCM33l6YQL4wZbB597js2guj4FmQvqBOpADKkSNSqvjD1QOKjs2UVepUmQP0kz1VJFKd1rpVhv4-U5VWkat1svxOXrR3_6F0A_M-J48av398xBCVWFIh5KHERCtuC8xqrCAiRTIddbI9ygzdi4SW5q94FgcKEpRSg7aQI3nw7xt_xQBNV5WBdO74Z-vOlmLh1tnjZt-2ajWsrAGJgziC7vwFu1DrTXTRduwXrVHCfpnCsR4I-4w1JPgyvsv0afLU5WVcPF87bRQoBBeVRkR1xOJm9MFc7lpnLpWaIEq7O5cwW8IHEo4bRP9_eURwdxp46Kjbg3EilppDUJIMMFVbnNI-3-FG_BLc266Nvwr3HotvuAtw3qmnqMNNbmS4x0ChYzIl1JNO3rXv-KAfOkcRvel84OFk1HQnU5CNXxF59y8kf9Z6ym1A3rxEfkF5GPFnQbdCFxU=",
                "deep_link": "https://www.kiwi.com/deep?affilid=apoorvflightsearch&currency=EUR&flightsId=071104c24bc80000274c4e49_0&from=DEL&lang=en&passengers=1&to=LKO&booking_token=Ejv_FoHOgyfUffe3vRXjqIsYYOku4HOCvbDB1FOZIHXhdfYrKUMWkvxLWQYElvI-P_zjWA4p8AWGDHL3EQRbnByKSASjXs8mvRL6ExWoZmA6s8fTdISs4v1IkGe60aZ9_KU-eXFp-PoCYxGwHnOSU16FDVihW1kSuQG4VJb5gB2l3J6Wg2KInuFXF2uKtwTb_v2DhrLJJA4yhCvq2t1zqEd_j8JMjZ9JkTiE8xpK9zTB0ogbl0UCiMt1VCkuDy1d3a2b68EZd449In_o2uSS274khJFLzMYc4RdxMJc69et8pe92_hcThlbHMa1ojj_qSfZvZyQaE_nHWwi-S0rdqN5rh6-RpPS_ui7JLAiDDbXK1EqND7ifIe0_VBYi_XAdeU_PMxnxYZS2-lVR7oYXDFg==",
                "facilitated_booking_available": True,
                "pnr_count": 1,
                "has_airport_change": False,
                "technical_stops": 0,
                "throw_away_ticketing": False,
                "hidden_city_ticketing": False,
                "virtual_interlining": False,
                "local_arrival": "2023-02-12T08:25:00.000Z",
                "utc_arrival": "2023-02-12T02:55:00.000Z",
                "local_departure": "2023-02-12T07:10:00.000Z",
                "utc_departure": "2023-02-12T01:40:00.000Z"
            },
            {
                "id": "071104c24bc8000020a92430_0",
                "flyFrom": "DEL",
                "flyTo": "LKO",
                "cityFrom": "New Delhi",
                "cityCodeFrom": "DEL",
                "cityTo": "Lucknow",
                "cityCodeTo": "LKO",
                "countryFrom": {
                    "code": "IN",
                    "name": "India"
                },
                "countryTo": {
                    "code": "IN",
                    "name": "India"
                },
                "nightsInDest": "None",
                "quality": 56.33328,
                "distance": 423.95,
                "duration": {
                    "departure": 4200,
                    "return": 0,
                    "total": 4200
                },
                "price": 35,
                "conversion": {
                    "EUR": 35
                },
                "bags_price": {
                    "1": 0
                },
                "baglimit": {
                    "hand_height": 38,
                    "hand_length": 57,
                    "hand_weight": 7,
                    "hand_width": 20,
                    "hold_dimensions_sum": 158,
                    "hold_height": 52,
                    "hold_length": 78,
                    "hold_weight": 15,
                    "hold_width": 28
                },
                "availability": {
                    "seats": 2
                },
                "airlines": [
                    "6E"
                ],
                "route": [
                    {
                        "id": "071104c24bc8000020a92430_0",
                        "combination_id": "071104c24bc8000020a92430",
                        "flyFrom": "DEL",
                        "flyTo": "LKO",
                        "cityFrom": "New Delhi",
                        "cityCodeFrom": "DEL",
                        "cityTo": "Lucknow",
                        "cityCodeTo": "LKO",
                        "airline": "6E",
                        "flight_no": 2319,
                        "operating_carrier": "6E",
                        "operating_flight_no": "2319",
                        "fare_basis": "P0IP",
                        "fare_category": "M",
                        "fare_classes": "X",
                        "fare_family": "",
                        "return": 0,
                        "bags_recheck_required": False,
                        "vi_connection": False,
                        "guarantee": False,
                        "equipment": "None",
                        "vehicle_type": "aircraft",
                        "local_arrival": "2023-02-12T17:25:00.000Z",
                        "utc_arrival": "2023-02-12T11:55:00.000Z",
                        "local_departure": "2023-02-12T16:15:00.000Z",
                        "utc_departure": "2023-02-12T10:45:00.000Z"
                    }
                ],
                "booking_token": "E9MjRIX59vP2V2a2VczwBx5x9LGHNb9E8ZIGGHYhv6rO8aTYCS1KjXYZjJC_FFvrwKLKB2u7EmJ61qRbweS7FfTcRfjA9NRWCLF2IozqhsaCH2BSQ7zpOf_EUSHJh5YCSTUFKm-XttBL_NtwuZP_x96NlOTrp7iHP52rafxKHb2Tq3g763QFw-4mETBA-59KCUi2d-YZgctR-JnMxG1U_wKaDfvh3KASYOoSWaBcDeSElLHdbhrx0g6PwsUj_TeYvJ_a3rTQFeMctKGVeuOirPIo3n_4sIilFhkVV2V8v0qH-mMPQifZH2AzWf9T631OWYixo4m9UHw3zM18QVGLuRn7ykp7ISa2n0arktJvvglP13RiVOPrG-yyKJCRxVkNvp6BEUpGOiTpc2YfMY9TOMJq3BzdEJLCeKwfLNc2IQRJPOIZTLF11dbtQ-U-5FA4aVGhzOsWNLB770vLnusFGcpNLbVJl0RdlWI1XYv072T1ZoYOK_3zhfIeIRf05FKM8l2S0xWRTnoiCwtwGZf9RGrsUuFBthfcL2sQcpSOtbKY=",
                "deep_link": "https://www.kiwi.com/deep?affilid=apoorvflightsearch&currency=EUR&flightsId=071104c24bc8000020a92430_0&from=DEL&lang=en&passengers=1&to=LKO&booking_token=EdCYs-KHM-lgCCOPjTRrl7MQKQc-SyZ_OMsbfJzqbo_kQtYidamPG_NeJJW1LU-jGwAEVcAHDNNOwOklb5DYsClZttBK64NHS-AW0Kn9N1H89i6v_l9S5fw-cah4ElA92qnRjVWZK7Jv2Mz9gF4iY6-4_zPwQihHLOkU2w3nmDS-6dcQnaq2pnhxlnW7xpON-ASrpOThrIfWnMZlU1HOWUB4DSvtef0pjTaoQWGQ9ZyE9rkVVjuQOUyWfym8iZFWiia0t0-8vqzXl8EHNOaZfqAs7JxxvfCPnrx97XqVvCYFT9AL_xRniYTZpvqK6l1OIzShGLGgNQjopkfxp24JAcJJBldLEg6-TAmhlw7q34ZhKUkgK2y_9rb0deVn0zYZdgF3qVyHlybApc0XpW0ljBM2HarXlYDJInwNusnuhAO0=",
                "facilitated_booking_available": True,
                "pnr_count": 1,
                "has_airport_change": False,
                "technical_stops": 0,
                "throw_away_ticketing": False,
                "hidden_city_ticketing": False,
                "virtual_interlining": False,
                "local_arrival": "2023-02-12T17:25:00.000Z",
                "utc_arrival": "2023-02-12T11:55:00.000Z",
                "local_departure": "2023-02-12T16:15:00.000Z",
                "utc_departure": "2023-02-12T10:45:00.000Z"
            },
            {
                "id": "071104c24bc900007fd9e9e1_0",
                "flyFrom": "DEL",
                "flyTo": "LKO",
                "cityFrom": "New Delhi",
                "cityCodeFrom": "DEL",
                "cityTo": "Lucknow",
                "cityCodeTo": "LKO",
                "countryFrom": {
                    "code": "IN",
                    "name": "India"
                },
                "countryTo": {
                    "code": "IN",
                    "name": "India"
                },
                "nightsInDest": "None",
                "quality": 56.666615,
                "distance": 423.95,
                "duration": {
                    "departure": 3900,
                    "return": 0,
                    "total": 3900
                },
                "price": 36,
                "conversion": {
                    "EUR": 36
                },
                "bags_price": {
                    "1": 0
                },
                "baglimit": {
                    "hand_height": 35,
                    "hand_length": 55,
                    "hand_weight": 8,
                    "hand_width": 25,
                    "hold_dimensions_sum": 158,
                    "hold_height": 52,
                    "hold_length": 78,
                    "hold_weight": 25,
                    "hold_width": 28,
                    "personal_item_height": 20,
                    "personal_item_length": 40,
                    "personal_item_weight": 5,
                    "personal_item_width": 10
                },
                "availability": {
                    "seats": "None"
                },
                "airlines": [
                    "AI"
                ],
                "route": [
                    {
                        "id": "071104c24bc900007fd9e9e1_0",
                        "combination_id": "071104c24bc900007fd9e9e1",
                        "flyFrom": "DEL",
                        "flyTo": "LKO",
                        "cityFrom": "New Delhi",
                        "cityCodeFrom": "DEL",
                        "cityTo": "Lucknow",
                        "cityCodeTo": "LKO",
                        "airline": "AI",
                        "flight_no": 811,
                        "operating_carrier": "AI",
                        "operating_flight_no": "811",
                        "fare_basis": "TIP",
                        "fare_category": "M",
                        "fare_classes": "T",
                        "fare_family": "",
                        "return": 0,
                        "bags_recheck_required": False,
                        "vi_connection": False,
                        "guarantee": False,
                        "equipment": "None",
                        "vehicle_type": "aircraft",
                        "local_arrival": "2023-02-13T19:45:00.000Z",
                        "utc_arrival": "2023-02-13T14:15:00.000Z",
                        "local_departure": "2023-02-13T18:40:00.000Z",
                        "utc_departure": "2023-02-13T13:10:00.000Z"
                    }
                ],
                "booking_token": "E8y0-sy3pslNTNNkx9VuJRiOQkbH8JdnbazcVXkVP0H2vZBw_c3-gXElU-HSQc20gIpeMso5gL6el3yp31XDLxFHKLHyQt1OjJETxu-7zEDugAAAY-M3YsmZX2ELSU4ohqqaEW5jOkhCPZkAUAqOkwWxLFGPa2n6PFOHFZ4w6McLbxdl6jrT35LyW36wO7nuQ6Nq2eLyaLf1vYdAtm9D-mqfrgaTeBDRG2xuqNdOanoD9xR3V0aPIj_lcLvqwZ0TyzkDqrD1KC1F_elDLp5y-AiOGOiz4I7Xbq3Fg9pC1scd0xsiEwds-DgKQ3s-IvCbpMAsg6QkaPlXmX5KdUxv_WjmnRogVmkx6s8Tdx77CcGGvtG1a30mNw66BvMDddjs_maB07ZJkz3wlHdVIJPtgF8uYUuxGZ7d4JHzTcrhvLCC_3TN94Il3ZPVKR88GNHZT_4eLvCRxOoYCGao6R8eWBty-g7iscKA6r-Uz0XZ5uDeYdtFbNvqKbTORDw00jyaR2Ygsi4ge9p5tju_tET8pJigl7Ap4KICavYAYEukY2AM4M0vpRLf-b2s7xrg1GCJKwO-yJTTjMXijApQIof20Y9Zj6Qd6ZuFei1z2b-QjFJY=",
                "deep_link": "https://www.kiwi.com/deep?affilid=apoorvflightsearch&currency=EUR&flightsId=071104c24bc900007fd9e9e1_0&from=DEL&lang=en&passengers=1&to=LKO&booking_token=EzuvIwSuTkU-iw9nPvtbJsOkCnFVBamKPqTJQkyNx2pP8J0Cl-K6ZayrHdZm8H9472sjqI6hc7EYx7SfYlDHwZR0oROk9LjJ_BifTgOYq_H9TJ6TrJw2XgVzGtdbms4zBlpdoh0QzQ369cnpeoQYwY6DUeGBUcjiPZ850YpGnIVQhPJPw7ciK8UPBpyktfp_cvK7Jw29aIsa0Yiu62JfAyIqmUgH9wNKJdFX2xat4yRxpPh1qqRl8bbIEEgbEj0UvaPGJjAcolzVwceU8Z453gSOi5ECrL4ZS9vNEtsGJBN6PJB3ru0Oq6N9HbwKgUCSEh_Q8LoWzaEXMI9yATwibP-pH24NOR1_TJA3zWn98JEA0wq170HsSnO-7bImkVO1iBY1XYqwzTM6WbahuVKb8X3ta65ChsB1B8-6eB-ojMLmtwr0QdLKTh3YWu6HDBNxsAxYK8-9v-tbJ6i2kjE_YJHAAeoGYH26kXIxUHzO3jDA=",
                "facilitated_booking_available": True,
                "pnr_count": 1,
                "has_airport_change": False,
                "technical_stops": 0,
                "throw_away_ticketing": False,
                "hidden_city_ticketing": False,
                "virtual_interlining": False,
                "local_arrival": "2023-02-13T19:45:00.000Z",
                "utc_arrival": "2023-02-13T14:15:00.000Z",
                "local_departure": "2023-02-13T18:40:00.000Z",
                "utc_departure": "2023-02-13T13:10:00.000Z"
            },
            {
                "id": "071104c24bc800005a79e69a_0",
                "flyFrom": "DEL",
                "flyTo": "LKO",
                "cityFrom": "New Delhi",
                "cityCodeFrom": "DEL",
                "cityTo": "Lucknow",
                "cityCodeTo": "LKO",
                "countryFrom": {
                    "code": "IN",
                    "name": "India"
                },
                "countryTo": {
                    "code": "IN",
                    "name": "India"
                },
                "nightsInDest": "None",
                "quality": 58.33328,
                "distance": 423.95,
                "duration": {
                    "departure": 4200,
                    "return": 0,
                    "total": 4200
                },
                "price": 37,
                "conversion": {
                    "EUR": 37
                },
                "bags_price": {
                    "1": 0
                },
                "baglimit": {
                    "hand_height": 36,
                    "hand_length": 56,
                    "hand_weight": 7,
                    "hand_width": 23,
                    "hold_dimensions_sum": 158,
                    "hold_height": 50,
                    "hold_length": 70,
                    "hold_weight": 15,
                    "hold_width": 38
                },
                "availability": {
                    "seats": "None"
                },
                "airlines": [
                    "I5"
                ],
                "route": [
                    {
                        "id": "071104c24bc800005a79e69a_0",
                        "combination_id": "071104c24bc800005a79e69a",
                        "flyFrom": "DEL",
                        "flyTo": "LKO",
                        "cityFrom": "New Delhi",
                        "cityCodeFrom": "DEL",
                        "cityTo": "Lucknow",
                        "cityCodeTo": "LKO",
                        "airline": "I5",
                        "flight_no": 745,
                        "operating_carrier": "I5",
                        "operating_flight_no": "745",
                        "fare_basis": "ONRA000",
                        "fare_category": "M",
                        "fare_classes": "O",
                        "fare_family": "",
                        "return": 0,
                        "bags_recheck_required": False,
                        "vi_connection": False,
                        "guarantee": False,
                        "equipment": "None",
                        "vehicle_type": "aircraft",
                        "local_arrival": "2023-02-12T14:25:00.000Z",
                        "utc_arrival": "2023-02-12T08:55:00.000Z",
                        "local_departure": "2023-02-12T13:15:00.000Z",
                        "utc_departure": "2023-02-12T07:45:00.000Z"
                    }
                ],
                "booking_token": "EmO_v9M78-c_Zqjh_GsZBrQVXSN6ioqEqtD3M-1W-TcfhuMNDAuRD8AaukAUY_PrpgHWqAkHB_tNymnWbYh24UfzoCIz5ZnpH1fdRfPpt2Z0BlCI2rnCIb-z8hbMrge0D22YB5eAoplMaml57berPLSq8hIvTmwCX8GQ0W4Lt6oKyguJvLyAw-Va2VNegrj75YJoHe_R0k6-hqp0A4Fb1picAPsOQ79oY0Q3uRByd8MI101mRXBP4VPpMMrgbOAphtuuvru7XwBLbBSkHhC1mC0NUyRBmd1-io5k15hTcEnni7SvREu17M9fkN6tv07b8WQHaXvjqx_z4z625X55DjIOsfXVQXg_tvl5gNdXrjLSn2-RCSfvLbrO2Da1YDSOJ6uyFV17XQZ8Br-Ho2s3g_rbHyJ3-iCoDNXfcsKn1nXfppQy66i820Xh8ZnyrCWNrah37r1MTz4Cz8eiSvNYfNEiFZV4qgBKTax2LcMPeiOrQB9rtf-natfGzigr1bUIR1AADa_q4EgpjkCa2-knsfAEOJR0AhFsptQJOybJ22Opr6tehoDJncKnwUoLrpyTD",
                "deep_link": "https://www.kiwi.com/deep?affilid=apoorvflightsearch&currency=EUR&flightsId=071104c24bc800005a79e69a_0&from=DEL&lang=en&passengers=1&to=LKO&booking_token=EYPhyqEqV-5D8ph3AnTYyzGSwPo161uTZ4cMzTe0783cuaHN2NGUeqM5gZwg1a38AYlLTg3_eSj1BSRHNBCZWu658wFKxEfzokUdcPgJGdq5-hezpQumF2gtLfEXBAA5B7NXtZnKJu2H2RhSuvSZeuuq6Yisf698PrQ1uOqhSYf-H9RIVwxEx8OEG0UEj0E2Lku1aLQKlLhKyjgmjU1glmirI_c83cfkb4DQTqS72z5oC0q5_xj3bLffNKe-_hATIPkBrEKeTyqiMRpe4ZCeaA2QaxYOtpyqtsxJ0Kylzi2Nm630H62tKD9CJuPS82VzpmGmPaLVTVQ0WIbb7ldX8pt3F1rErtxUvPVaxMIJskDS5eLP4qrXNew2yJNSDy2OziHSPkC40xSX_c_lwu4LLiy6MIosgB7UbwEC5ED4GZ2A=",
                "facilitated_booking_available": True,
                "pnr_count": 1,
                "has_airport_change": False,
                "technical_stops": 0,
                "throw_away_ticketing": False,
                "hidden_city_ticketing": False,
                "virtual_interlining": False,
                "local_arrival": "2023-02-12T14:25:00.000Z",
                "utc_arrival": "2023-02-12T08:55:00.000Z",
                "local_departure": "2023-02-12T13:15:00.000Z",
                "utc_departure": "2023-02-12T07:45:00.000Z"
            },
            {
                "id": "071104c24bc900000d3ced8a_0",
                "flyFrom": "DEL",
                "flyTo": "LKO",
                "cityFrom": "New Delhi",
                "cityCodeFrom": "DEL",
                "cityTo": "Lucknow",
                "cityCodeTo": "LKO",
                "countryFrom": {
                    "code": "IN",
                    "name": "India"
                },
                "countryTo": {
                    "code": "IN",
                    "name": "India"
                },
                "nightsInDest": "None",
                "quality": 60.33328,
                "distance": 423.95,
                "duration": {
                    "departure": 4200,
                    "return": 0,
                    "total": 4200
                },
                "price": 39,
                "conversion": {
                    "EUR": 39
                },
                "bags_price": {
                    "1": 0
                },
                "baglimit": {
                    "hand_height": 38,
                    "hand_length": 57,
                    "hand_weight": 7,
                    "hand_width": 20,
                    "hold_dimensions_sum": 158,
                    "hold_height": 52,
                    "hold_length": 78,
                    "hold_weight": 15,
                    "hold_width": 28
                },
                "availability": {
                    "seats": 2
                },
                "airlines": [
                    "6E"
                ],
                "route": [
                    {
                        "id": "071104c24bc900000d3ced8a_0",
                        "combination_id": "071104c24bc900000d3ced8a",
                        "flyFrom": "DEL",
                        "flyTo": "LKO",
                        "cityFrom": "New Delhi",
                        "cityCodeFrom": "DEL",
                        "cityTo": "Lucknow",
                        "cityCodeTo": "LKO",
                        "airline": "6E",
                        "flight_no": 2282,
                        "operating_carrier": "6E",
                        "operating_flight_no": "2282",
                        "fare_basis": "R0IP",
                        "fare_category": "M",
                        "fare_classes": "X",
                        "fare_family": "",
                        "return": 0,
                        "bags_recheck_required": False,
                        "vi_connection": False,
                        "guarantee": False,
                        "equipment": "None",
                        "vehicle_type": "aircraft",
                        "local_arrival": "2023-02-13T13:40:00.000Z",
                        "utc_arrival": "2023-02-13T08:10:00.000Z",
                        "local_departure": "2023-02-13T12:30:00.000Z",
                        "utc_departure": "2023-02-13T07:00:00.000Z"
                    }
                ],
                "booking_token": "EC3wqLTBj6GB3vL6YsQhXWm3XUn9KYkb4LYGAkbWdwtCOCqdIqKC0K2Vw_EriUaMuuBKmvy2c9hrt4LSXZAO7XKSzxTxnLQ5S00hqZfj0nkaFHYcAXPxx5aPV8UVIXJy4Ih8LR8J_XE43k49P1f_gmNh1Y_efWOC8XjPUaOaQBzCjG9uZkDWAvgv-zYl1XcXC9aNTNzmzxVSvoMEFTI5DSRxPZOfezESu25AzHH9s61MlIgbxRno8-oGD0AIWkZZOIrcoL70o1vwbmTpADBFrqiDEp7gVp-zLZOJ3GWI0Dyp42l-d3-XZ82EexvqvyY8h9YlRgpwdHZ5KbmLP-JV2USBVwZifwNEo99ZE2o0_RNel7IzkKMplvN1winEywQsQDCB5Yx_7rCB3XVvd3KQDg7-WOVlK2UBGlhgRv48b-hIggrlJze9hyfORGMke8KKIteOOrotbyEhWoBssVH2bfUrQAGNQlP5X0BSE67C8O5VPzRN328WUomWIr3orHLl0y2son3p3Bxt5_gYIm5qX51zrFSsqjUfkaK6nggPjG9Y=",
                "deep_link": "https://www.kiwi.com/deep?affilid=apoorvflightsearch&currency=EUR&flightsId=071104c24bc900000d3ced8a_0&from=DEL&lang=en&passengers=1&to=LKO&booking_token=EJYmL-u58IHzAmEQQtD_2QwY_Sje6gmpO9DOe_7w8esijMGJM8g_2X2yGWDlyBNFLC7gejgS9Avi-cYW6wJtyH-q2tsv1UdWgUP7JGj9_VO4bfgKv06yv8IHXc3_ZYrfvFs-chVW-mBu_-QHYYSYlLsU485h3LLWXuf9GT-LCKy5d-RjYG0fr5GqHuuIHcbX3nGhvbtMeIEDlrfjMFu1XhWgRkBwgZcJVk82mOPc7CjcGIxYpb2Ah0JQk7kGNulxvuLSBp8ElcX7ydPc1-WF169TND7MrZhdaeT2-gdoitqm-aO3hUhmrIGZPr3vipl_6HtpDHimxiUWJ9mvLb6fFnAhtTovlusqgQ2eGDK6xNgWyrbQ_lBGZ-XOcxk1aJkExYnzmwnKqLEjPtFo3JNAhGHnSmZgsbzasslnhTpuy46I=",
                "facilitated_booking_available": True,
                "pnr_count": 1,
                "has_airport_change": False,
                "technical_stops": 0,
                "throw_away_ticketing": False,
                "hidden_city_ticketing": False,
                "virtual_interlining": False,
                "local_arrival": "2023-02-13T13:40:00.000Z",
                "utc_arrival": "2023-02-13T08:10:00.000Z",
                "local_departure": "2023-02-13T12:30:00.000Z",
                "utc_departure": "2023-02-13T07:00:00.000Z"
            },
            {
                "id": "071104c24bc80000dd8eec18_0",
                "flyFrom": "DEL",
                "flyTo": "LKO",
                "cityFrom": "New Delhi",
                "cityCodeFrom": "DEL",
                "cityTo": "Lucknow",
                "cityCodeTo": "LKO",
                "countryFrom": {
                    "code": "IN",
                    "name": "India"
                },
                "countryTo": {
                    "code": "IN",
                    "name": "India"
                },
                "nightsInDest": "None",
                "quality": 60.999945,
                "distance": 423.95,
                "duration": {
                    "departure": 4500,
                    "return": 0,
                    "total": 4500
                },
                "price": 39,
                "conversion": {
                    "EUR": 39
                },
                "bags_price": {
                    "1": 0
                },
                "baglimit": {
                    "hand_height": 38,
                    "hand_length": 57,
                    "hand_weight": 7,
                    "hand_width": 20,
                    "hold_dimensions_sum": 158,
                    "hold_height": 52,
                    "hold_length": 78,
                    "hold_weight": 15,
                    "hold_width": 28
                },
                "availability": {
                    "seats": 1
                },
                "airlines": [
                    "6E"
                ],
                "route": [
                    {
                        "id": "071104c24bc80000dd8eec18_0",
                        "combination_id": "071104c24bc80000dd8eec18",
                        "flyFrom": "DEL",
                        "flyTo": "LKO",
                        "cityFrom": "New Delhi",
                        "cityCodeFrom": "DEL",
                        "cityTo": "Lucknow",
                        "cityCodeTo": "LKO",
                        "airline": "6E",
                        "flight_no": 2107,
                        "operating_carrier": "6E",
                        "operating_flight_no": "2107",
                        "fare_basis": "",
                        "fare_category": "M",
                        "fare_classes": "R",
                        "fare_family": "",
                        "return": 0,
                        "bags_recheck_required": False,
                        "vi_connection": False,
                        "guarantee": False,
                        "equipment": "None",
                        "vehicle_type": "aircraft",
                        "local_arrival": "2023-02-12T09:45:00.000Z",
                        "utc_arrival": "2023-02-12T04:15:00.000Z",
                        "local_departure": "2023-02-12T08:30:00.000Z",
                        "utc_departure": "2023-02-12T03:00:00.000Z"
                    }
                ],
                "booking_token": "EFcUpAlPFy1eKkuSv_LtHOs6Jd4XlmD4ObUB1cW5ck11LBmoh9_T0i2MQ_DpuBoUSquedNy_fh5LCN0ZBrU0NYrCF5WswCfTRPxQx2puCkigRj5qC3THC2fxN1nhi4D-w9S-9rby_o58Ha85RP7hKs2rjSeUsa87HbBvmWhdZGKjPHgd-oj18q6n1inV-O1LxjVL9LUDp3YjweIph2-TBG7FkA11T-l1f2HzOwaeXhzlHpt0yiJ1kSyP64vvORv3L_Awi-KC0-uAWStoLKBlLL9WLlElIDcX80ZrY8bSkH96kgz3N8gungc_5r2SIEaPwQehp4uyImo2VJ8FPlRCAdKsHMCgV2dkW15tL-JA95js923zz8wYcStGXkzhs5xyg3XNFhUpt-tEzyxqJqJxxsvlS0ZZfeIOzgQv2MnNATBOKP4bvy_oEyHhGHzotS9y-eQIrRUPAJonbxuqB_NkBAbOplEdoUjDw3KNeXxVNur1dJt1x9GReEr3_2P6czOcmb2Or0JIYmdCw3Z-JvOX1-30GWBayNfn8p5TDd9HHzTU=",
                "deep_link": "https://www.kiwi.com/deep?affilid=apoorvflightsearch&currency=EUR&flightsId=071104c24bc80000dd8eec18_0&from=DEL&lang=en&passengers=1&to=LKO&booking_token=EVVrZ7d8qOt3jOdfoiN1O_4gSDURKExcW_OrrDVnsB_Vv20JPW20U-ax-LcMc4EwofHCW0RGNhqy86dY3I-TG51A8a0csAlaCdrEwCFnOh_uxiEoVpYFtYfN4a7A2a98bdgPKNTLDTxImyACQGTvljL6sudqt8E4IhrvPpys5_7UtxBrQCAmfoQS12YaLV96L8O3V1FaC-DQ3pY3Q3mAa9DtjYHbi2WKczYytxxrFgyvm6d_3NrlaM8rxZECtVRJJm1jDWO7goJPByv0YaQnZAX6JH86I0B7S5mVCDBN1RuIq-_HQuCnBuB2YfXO-PwrDjnJM2uyeEXpROIA2irnFqu56gX0nHXuUelL6jSqnvfontlMHUzYmMuAqUiAmBiq0KLajut7qvazNgmiKcYXJAg==",
                "facilitated_booking_available": True,
                "pnr_count": 1,
                "has_airport_change": False,
                "technical_stops": 0,
                "throw_away_ticketing": False,
                "hidden_city_ticketing": False,
                "virtual_interlining": False,
                "local_arrival": "2023-02-12T09:45:00.000Z",
                "utc_arrival": "2023-02-12T04:15:00.000Z",
                "local_departure": "2023-02-12T08:30:00.000Z",
                "utc_departure": "2023-02-12T03:00:00.000Z"
            },
            {
                "id": "071104c24bc70000942dd4a4_0",
                "flyFrom": "DEL",
                "flyTo": "LKO",
                "cityFrom": "New Delhi",
                "cityCodeFrom": "DEL",
                "cityTo": "Lucknow",
                "cityCodeTo": "LKO",
                "countryFrom": {
                    "code": "IN",
                    "name": "India"
                },
                "countryTo": {
                    "code": "IN",
                    "name": "India"
                },
                "nightsInDest": "None",
                "quality": 61.33328,
                "distance": 423.95,
                "duration": {
                    "departure": 4200,
                    "return": 0,
                    "total": 4200
                },
                "price": 40,
                "conversion": {
                    "EUR": 40
                },
                "bags_price": {
                    "1": 0
                },
                "baglimit": {
                    "hand_height": 36,
                    "hand_length": 56,
                    "hand_weight": 7,
                    "hand_width": 23,
                    "hold_dimensions_sum": 158,
                    "hold_height": 50,
                    "hold_length": 70,
                    "hold_weight": 15,
                    "hold_width": 38
                },
                "availability": {
                    "seats": 6
                },
                "airlines": [
                    "I5"
                ],
                "route": [
                    {
                        "id": "071104c24bc70000942dd4a4_0",
                        "combination_id": "071104c24bc70000942dd4a4",
                        "flyFrom": "DEL",
                        "flyTo": "LKO",
                        "cityFrom": "New Delhi",
                        "cityCodeFrom": "DEL",
                        "cityTo": "Lucknow",
                        "cityCodeTo": "LKO",
                        "airline": "I5",
                        "flight_no": 784,
                        "operating_carrier": "",
                        "operating_flight_no": "",
                        "fare_basis": "ZNRA000",
                        "fare_category": "M",
                        "fare_classes": "Z",
                        "fare_family": "",
                        "return": 0,
                        "bags_recheck_required": False,
                        "vi_connection": False,
                        "guarantee": False,
                        "equipment": "None",
                        "vehicle_type": "aircraft",
                        "local_arrival": "2023-02-11T17:40:00.000Z",
                        "utc_arrival": "2023-02-11T12:10:00.000Z",
                        "local_departure": "2023-02-11T16:30:00.000Z",
                        "utc_departure": "2023-02-11T11:00:00.000Z"
                    }
                ],
                "booking_token": "E7Zcco-mmtrTVAN3dAxkmBYJXw_J2ugjWnu3KxDh4OnmMcOQs3ma7i1DlLMv3w4T7_570wPIvzSrYARXKYqV47sTl4J0WM8XJrhzEompWFHn_WaGILYmwwbIgMHK3Q75Zd91-ajYHkydB2vMAiK8__wlQBYIQviUhao0JgSazPba3Y-F97jf2hxUfR6v0kXgXhJVh5Kh4NdAG-4rMAJJAkydsJsYl1LdG_1U1f0Jwl1ZgJEsfar1MNqFNVGFDi0jawyopl0EGYuinQ27Cy-VBRh07m9NjNKeWZAvJHCiL6Xo2B2eUZw40_qHtIwzj9wkgR6BzQCynrEQhkTLeof9phXzSXTeZjBUFIy3WWANP_MW7WXgUNBDOV4sEGeMxQ6QTR1SLbJo2HTC4VWwl_9Nfsv1MwhkFnx9aJ7XHuMqa0iYQI4F7WOXfAtYTXWjamZ_ZyrKfq8bwRXyio4HzpRRtVmNi_enNJ8XJUOf2IKI5MDhcyBFmbXf3lWVwE6TpX3AzeA_Lfk-98ICFdSYK-7b8ZlD1c_sWTE3lPd9hCnCZ7n2asiIfPlu2mO2wz9n5v1Jl0O3j_xqwv8n5WXY4Fx1Jx_6qWm0C8Y6FUQFi8lajq3c=",
                "deep_link": "https://www.kiwi.com/deep?affilid=apoorvflightsearch&currency=EUR&flightsId=071104c24bc70000942dd4a4_0&from=DEL&lang=en&passengers=1&to=LKO&booking_token=EMi0xgVFnt8B3jb4mag6KYvIXWuqzEEVMTMysIVEFIEqzNC0CMGf-fX-0bR5XyVd7q2ay_cqsHaKmDmhAJhfurAGoT6pktBh-y8KeVw4Jgoir0FVnOeV2phXkfPNJFT7bAIX7XcDO1_oOTNjr8ZzhCiaMerW93OvY3YrxCG9ANph2Bgk2lwLeZA_83OjDh2iNXvBoY1-o7CrRovuQqfZiVV7VbVdIeFSbvH3xpsfsu9zz0wIy9XAcHwEl-koJFzHXkzPzPSBTg6iRlKZfNZ_-amGkf43-cvtlbZt7hIIfqgMm1pyN-anITl3O-kj0XjB6-CmkrfnO3ttRgUzaMXBmQIhv8clSRFCDr0_WBAn7mFm0uSiaBZG5GT0QElSA13ASQZvmvuZZVTSRcMZDI0kt9X4tpOykO79_usTFqFZCRmH_SH-FYhsYQXci5otALH9wUQzRDs0SX8jtg6z5BcMVug==",
                "facilitated_booking_available": True,
                "pnr_count": 1,
                "has_airport_change": False,
                "technical_stops": 0,
                "throw_away_ticketing": False,
                "hidden_city_ticketing": False,
                "virtual_interlining": False,
                "local_arrival": "2023-02-11T17:40:00.000Z",
                "utc_arrival": "2023-02-11T12:10:00.000Z",
                "local_departure": "2023-02-11T16:30:00.000Z",
                "utc_departure": "2023-02-11T11:00:00.000Z"
            },
            {
                "id": "071104c24bc800004bdc0331_0",
                "flyFrom": "DEL",
                "flyTo": "LKO",
                "cityFrom": "New Delhi",
                "cityCodeFrom": "DEL",
                "cityTo": "Lucknow",
                "cityCodeTo": "LKO",
                "countryFrom": {
                    "code": "IN",
                    "name": "India"
                },
                "countryTo": {
                    "code": "IN",
                    "name": "India"
                },
                "nightsInDest": "None",
                "quality": 62.666615,
                "distance": 423.95,
                "duration": {
                    "departure": 3900,
                    "return": 0,
                    "total": 3900
                },
                "price": 42,
                "conversion": {
                    "EUR": 42
                },
                "bags_price": {
                    "1": 0
                },
                "baglimit": {
                    "hand_height": 38,
                    "hand_length": 57,
                    "hand_weight": 7,
                    "hand_width": 20,
                    "hold_dimensions_sum": 158,
                    "hold_height": 52,
                    "hold_length": 78,
                    "hold_weight": 15,
                    "hold_width": 28
                },
                "availability": {
                    "seats": 2
                },
                "airlines": [
                    "6E"
                ],
                "route": [
                    {
                        "id": "071104c24bc800004bdc0331_0",
                        "combination_id": "071104c24bc800004bdc0331",
                        "flyFrom": "DEL",
                        "flyTo": "LKO",
                        "cityFrom": "New Delhi",
                        "cityCodeFrom": "DEL",
                        "cityTo": "Lucknow",
                        "cityCodeTo": "LKO",
                        "airline": "6E",
                        "flight_no": 2251,
                        "operating_carrier": "6E",
                        "operating_flight_no": "2251",
                        "fare_basis": "J0IP",
                        "fare_category": "M",
                        "fare_classes": "X",
                        "fare_family": "",
                        "return": 0,
                        "bags_recheck_required": False,
                        "vi_connection": False,
                        "guarantee": False,
                        "equipment": "None",
                        "vehicle_type": "aircraft",
                        "local_arrival": "2023-02-12T20:15:00.000Z",
                        "utc_arrival": "2023-02-12T14:45:00.000Z",
                        "local_departure": "2023-02-12T19:10:00.000Z",
                        "utc_departure": "2023-02-12T13:40:00.000Z"
                    }
                ],
                "booking_token": "ERCUMgolAsr7MizYNW0vtVe5V8cAr9vuUSYgXG_eZiAvjTrNMDWQHnFIGG8CZ5sQrZ2T74i-6yUIlxAAoMA6Xt1zmpUNCLpngO780mex0tkBQvNeCRLj7JCo4cnEVODJ9JafzwWGE94ZHsIho1RxMp5brqN373Om7LlRj444GMvAO3JQ8-pillMsbUV9F35Udhcn3IZurDi2S9uvwNhP6VFPB746iQxd-xCG9su6592Hxgp5hgRFohaNnjFRPR7o1IrS9kihn2VwWfk1coqNyDEQX7wH6_T55E9Rf6HqKnjA0ueyyxhadIVsH8SRo72hREmloVXRv7hK8vAlMIktpZsQtYKS0RqlfyUtJ50jgdbZr3x2PQl3yejbYxX7iA8hlORgM-KOCRNmf9X2A_rP42SotMiuVOM9doHqJrhGLGKm9ceamZlV74sIElBsS3ywHtEaB1Z5NJIKs6wtOt3PAAqiLkkhKaUgMQUgpsmZKADz__pX1Oj6BtTKCVXirw9Ivlz6ExPYJeYprXBf_ygXj01fOODKE18pzP_Oto3y4j5k=",
                "deep_link": "https://www.kiwi.com/deep?affilid=apoorvflightsearch&currency=EUR&flightsId=071104c24bc800004bdc0331_0&from=DEL&lang=en&passengers=1&to=LKO&booking_token=Emu1mTS1R5gNr4xvgLAh4dzTZTVuOpah4wkQqavdXcPphxk9h1QjMURshEi0DMorFAbg0m8Nfz-xHRtvkGudT2mIjZilNDd34KoyoOZsgBK8US0dOnxYPGgrN7lnHCkptMViVTjVRPW4y-mnvuFtdjtT00p-S2ha7ehE2ndYfu3EwLzKi60j-mrguPDzyNCBjGtN1ca1jp_tjRFXmWXpVr-sjptv411z2bSv50X_NNld02TLFoMFUvVbvwhTOOxNG8VInE-UlcDL0ddOJXpnnh9tDLTi1P4jm_zMgvwPrXc_R5WOtypl0HUU6r2oQ3-6I59Jj2ON7tj-FaoYil_8XB7ZTnIMvkoPv5Wakg2m8N2wYWYXFnxW3UlhZsO7c_EwP1zM-dEC2o-qP0aKHINu-wB9W4lW7C1WI66g0O9XdJrs=",
                "facilitated_booking_available": True,
                "pnr_count": 1,
                "has_airport_change": False,
                "technical_stops": 0,
                "throw_away_ticketing": False,
                "hidden_city_ticketing": False,
                "virtual_interlining": False,
                "local_arrival": "2023-02-12T20:15:00.000Z",
                "utc_arrival": "2023-02-12T14:45:00.000Z",
                "local_departure": "2023-02-12T19:10:00.000Z",
                "utc_departure": "2023-02-12T13:40:00.000Z"
            },
            {
                "id": "071100174bc900007af02c16_0",
                "flyFrom": "DEL",
                "flyTo": "IXB",
                "cityFrom": "New Delhi",
                "cityCodeFrom": "DEL",
                "cityTo": "Bagdogra",
                "cityCodeTo": "IXB",
                "countryFrom": {
                    "code": "IN",
                    "name": "India"
                },
                "countryTo": {
                    "code": "IN",
                    "name": "India"
                },
                "nightsInDest": "None",
                "quality": 71.333265,
                "distance": 1126.41,
                "duration": {
                    "departure": 6900,
                    "return": 0,
                    "total": 6900
                },
                "price": 44,
                "conversion": {
                    "EUR": 44
                },
                "bags_price": {
                    "1": 0
                },
                "baglimit": {
                    "hand_height": 35,
                    "hand_length": 55,
                    "hand_weight": 7,
                    "hand_width": 25,
                    "hold_dimensions_sum": 158,
                    "hold_height": 52,
                    "hold_length": 78,
                    "hold_weight": 15,
                    "hold_width": 28
                },
                "availability": {
                    "seats": 2
                },
                "airlines": [
                    "G8"
                ],
                "route": [
                    {
                        "id": "071100174bc900007af02c16_0",
                        "combination_id": "071100174bc900007af02c16",
                        "flyFrom": "DEL",
                        "flyTo": "IXB",
                        "cityFrom": "New Delhi",
                        "cityCodeFrom": "DEL",
                        "cityTo": "Bagdogra",
                        "cityCodeTo": "IXB",
                        "airline": "G8",
                        "flight_no": 263,
                        "operating_carrier": "",
                        "operating_flight_no": "",
                        "fare_basis": "MO9RBSNE",
                        "fare_category": "M",
                        "fare_classes": "M",
                        "fare_family": "",
                        "return": 0,
                        "bags_recheck_required": False,
                        "vi_connection": False,
                        "guarantee": False,
                        "equipment": "None",
                        "vehicle_type": "aircraft",
                        "local_arrival": "2023-02-13T08:20:00.000Z",
                        "utc_arrival": "2023-02-13T02:50:00.000Z",
                        "local_departure": "2023-02-13T06:25:00.000Z",
                        "utc_departure": "2023-02-13T00:55:00.000Z"
                    }
                ],
                "booking_token": "EKXOM-Wu_mTC740lTjb0tlms-lvAQ-v5jn4nisI7FUpOsLVkBCWcRqYPUJ2MSKn20Dh8A6C5hRr0ss1wdDiBpZq-mhvLb4CZiUPWm3bjpKCS31Ad8wo5YQi8jp4wvovERHqfjVm9_Y60r4fkT54edxyLfdd9X3YgBVyJCHdxD4VEn2eokCbkA6AqayoC76sOtc-0Zo2WZWCdNHr71YD1tNOuPdeRfIoHzRw3wIb4bJppYE_gspZlKLHf8sBs77MWgcBcKyTVujpNV_pHnIs9HEZ9bWEysS1ZmYhPjQ1GP855bsMvsMiW5DrjmpjbRIkKrD9CRZXiQKRLHBkC00i4bpEmf8_yBrv-EN3V1Eg7AsXei2bmdWNJ6EdVaY5cCqWsx24CIBmY5S13ehqgVATKQNHenFAkSCM-rhGDTcCG9aMtmwz1HsvFyLUuNc-NvnNUyy9E78f7ylrHGjL1WhEKtk4C391BF0E5bRbpS6RI7doDjO9j0SR18-buoGVITYU2xr5CEwdaqIAx6DMY6N0enWSclVj9MA44yV2ajnIx5yfCmBpMEyif4b54g-XJ0V_N2",
                "deep_link": "https://www.kiwi.com/deep?affilid=apoorvflightsearch&currency=EUR&flightsId=071100174bc900007af02c16_0&from=DEL&lang=en&passengers=1&to=IXB&booking_token=EdgxYorOc9uzvY2y_CXsIoxYFMAj9jc1KCWiKFzLwlWSyfnFhboz0B6i5dIuVbsijJ2p1q_AgrmPelvskj9PHLlSCGazYljfT61cAoX_y_usn6AyWI1xp1yokjBioZzD4fyzbvf5GSh9EPFPmYun0Nqa24wVdjVLSuHJWdKixNNw1H8su1i65-E1UKO6SCAtwxEk391pR8mxymD9SIfeDHYfmltt9X9OW8g0Ci_qYm5Ilcak30oatB3R6sdZDTxMA530rkllAXbgm57-V8nd8tWrbQuCTeog17P9tWvfnTd3B7N0cGglLtf8wzS47wIT6yt3DynY0Cmg85rRgXS6gLiPUUa7LMrB6P0JkNmVV1rUtT--AMyXgT775qXPYx-7eryy8YBtKJKiKVsb1XndlytYBJKHOA0GpDv6hzTQPaSJSL36SY7cTa4Zwhi6ROlQz",
                "facilitated_booking_available": True,
                "pnr_count": 1,
                "has_airport_change": False,
                "technical_stops": 0,
                "throw_away_ticketing": False,
                "hidden_city_ticketing": False,
                "virtual_interlining": False,
                "local_arrival": "2023-02-13T08:20:00.000Z",
                "utc_arrival": "2023-02-13T02:50:00.000Z",
                "local_departure": "2023-02-13T06:25:00.000Z",
                "utc_departure": "2023-02-13T00:55:00.000Z"
            },
            {
                "id": "071104c24bc80000677b2cc6_0",
                "flyFrom": "DEL",
                "flyTo": "LKO",
                "cityFrom": "New Delhi",
                "cityCodeFrom": "DEL",
                "cityTo": "Lucknow",
                "cityCodeTo": "LKO",
                "countryFrom": {
                    "code": "IN",
                    "name": "India"
                },
                "countryTo": {
                    "code": "IN",
                    "name": "India"
                },
                "nightsInDest": "None",
                "quality": 66.33328,
                "distance": 423.95,
                "duration": {
                    "departure": 4200,
                    "return": 0,
                    "total": 4200
                },
                "price": 45,
                "conversion": {
                    "EUR": 45
                },
                "bags_price": {
                    "1": 0
                },
                "baglimit": {
                    "hand_height": 38,
                    "hand_length": 57,
                    "hand_weight": 7,
                    "hand_width": 20,
                    "hold_dimensions_sum": 158,
                    "hold_height": 52,
                    "hold_length": 78,
                    "hold_weight": 15,
                    "hold_width": 28
                },
                "availability": {
                    "seats": 2
                },
                "airlines": [
                    "6E"
                ],
                "route": [
                    {
                        "id": "071104c24bc80000677b2cc6_0",
                        "combination_id": "071104c24bc80000677b2cc6",
                        "flyFrom": "DEL",
                        "flyTo": "LKO",
                        "cityFrom": "New Delhi",
                        "cityCodeFrom": "DEL",
                        "cityTo": "Lucknow",
                        "cityCodeTo": "LKO",
                        "airline": "6E",
                        "flight_no": 2282,
                        "operating_carrier": "6E",
                        "operating_flight_no": "2282",
                        "fare_basis": "P0IP",
                        "fare_category": "M",
                        "fare_classes": "X",
                        "fare_family": "",
                        "return": 0,
                        "bags_recheck_required": False,
                        "vi_connection": False,
                        "guarantee": False,
                        "equipment": "None",
                        "vehicle_type": "aircraft",
                        "local_arrival": "2023-02-12T13:40:00.000Z",
                        "utc_arrival": "2023-02-12T08:10:00.000Z",
                        "local_departure": "2023-02-12T12:30:00.000Z",
                        "utc_departure": "2023-02-12T07:00:00.000Z"
                    }
                ],
                "booking_token": "ENzV_afVC2KCcUzc--hcmNAN7wn7cjQi5G4OKtaRUtVHfK-5da1gVzmtAJM-4n8MqOoNsuh9a2NhXDp-AdCqRgihcexkx9a3glvj18YotairQVfhzRE7GzXtW0VRXd4Gx6kRASblfV7EDxm5Ct-4O0vkvTD3MHi6ei3TU-8MZc_VaYW0p5bmqWtWW0WVFXz2v89ISUiTsEnkCNhO9aOnJ_KS-Ks0X5VVGxvS9D2pbwGc6ycX4AyZ8r_AeBMZrsss2GxE4z8rsly59Cs__X1MGH3Np--o9ZhCc9UkgaWsA7ZgMVeL4REB37SjI34w1IaiI_ddbQL63ZVSFHoV8rRcWYz9uJM0Gf9r_Zs0SmyvQ55eCfgoM9NeSLTJ_ZauwCqBgDRhbabGY7b8sSI-jayLZmTjhdghCqvE78TncAkexZpKkrDEl2FZ-u6023P0TXNTrfUoMuZ2nK-ac_0WgNt0nZkwUdiZ-Ipl9ddJL7L7IoPUfTGLzBmvwnxK9MPk4M1WeyBvyfMODHcncNviciPDDotYMsVoPFkeHD43IVRaptp4=",
                "deep_link": "https://www.kiwi.com/deep?affilid=apoorvflightsearch&currency=EUR&flightsId=071104c24bc80000677b2cc6_0&from=DEL&lang=en&passengers=1&to=LKO&booking_token=Eq-pBicD0KKUUbIe0dxOxDRG-NIJ-pUcxJpWyJNSM0v5OwPJiYzVrJ94iyPeuoszsbN3peOZrBHa2OzFRJXo9k4vnbKIhMQxU-JPf2aiWVLZH7vpxeJi4z3buEY7GMHRX_U1VhCuH1B4EhEX-Waz2u0LI7EEG0S-a8-sz74RTgTMPPmTbT6o5SUTv9RhuuNEzrlXzA7hN5Wd6iGVGpkrBtXmtfH-2i7iZUBM62pnrw5_PZwceeMJaJtFd84t_J_tHy9TO74SnNIWtvNlPq_UZHiZPINDpKCjiSrC2yL-ObzPWXZtw9vcR2wYgr15p0I-o8NHxouWkW8gNwMmOmh8M07dh3lbLDy9d9Ho4R5kWH-EqPXwk9oQeXI2axGCMsg1H3CHvT5HhCIgA94l3PCLCIg==",
                "facilitated_booking_available": True,
                "pnr_count": 1,
                "has_airport_change": False,
                "technical_stops": 0,
                "throw_away_ticketing": False,
                "hidden_city_ticketing": False,
                "virtual_interlining": False,
                "local_arrival": "2023-02-12T13:40:00.000Z",
                "utc_arrival": "2023-02-12T08:10:00.000Z",
                "local_departure": "2023-02-12T12:30:00.000Z",
                "utc_departure": "2023-02-12T07:00:00.000Z"
            },
            {
                "id": "0711019d4bc800005bf2a631_0",
                "flyFrom": "DEL",
                "flyTo": "JLR",
                "cityFrom": "New Delhi",
                "cityCodeFrom": "DEL",
                "cityTo": "Jabalpur",
                "cityCodeTo": "JLR",
                "countryFrom": {
                    "code": "IN",
                    "name": "India"
                },
                "countryTo": {
                    "code": "IN",
                    "name": "India"
                },
                "nightsInDest": "None",
                "quality": 69.666605,
                "distance": 668.53,
                "duration": {
                    "departure": 5700,
                    "return": 0,
                    "total": 5700
                },
                "price": 45,
                "conversion": {
                    "EUR": 45
                },
                "bags_price": {
                    "1": 0
                },
                "baglimit": {
                    "hand_height": 36,
                    "hand_length": 54,
                    "hand_weight": 7,
                    "hand_width": 18,
                    "hold_dimensions_sum": 158,
                    "hold_height": 52,
                    "hold_length": 78,
                    "hold_weight": 15,
                    "hold_width": 28
                },
                "availability": {
                    "seats": 2
                },
                "airlines": [
                    "SG"
                ],
                "route": [
                    {
                        "id": "0711019d4bc800005bf2a631_0",
                        "combination_id": "0711019d4bc800005bf2a631",
                        "flyFrom": "DEL",
                        "flyTo": "JLR",
                        "cityFrom": "New Delhi",
                        "cityCodeFrom": "DEL",
                        "cityTo": "Jabalpur",
                        "cityCodeTo": "JLR",
                        "airline": "SG",
                        "flight_no": 954,
                        "operating_carrier": "SG",
                        "operating_flight_no": "954",
                        "fare_basis": "USWB",
                        "fare_category": "M",
                        "fare_classes": "U",
                        "fare_family": "",
                        "return": 0,
                        "bags_recheck_required": False,
                        "vi_connection": False,
                        "guarantee": False,
                        "equipment": "None",
                        "vehicle_type": "aircraft",
                        "local_arrival": "2023-02-12T09:10:00.000Z",
                        "utc_arrival": "2023-02-12T03:40:00.000Z",
                        "local_departure": "2023-02-12T07:35:00.000Z",
                        "utc_departure": "2023-02-12T02:05:00.000Z"
                    }
                ],
                "booking_token": "E_37prngEVtvokCK1jWGsb5YLN-gM7oIfQ9gi490laywrxkg5smaaIrGPesESJkr7AVzh7hjejY4f8_jczUJhBzY1QgZGbH1wJhKqUlFvw0jGza6JUzG_EufQPpZZdTa-iNxy0J2ZbqWKIR7nP8Pz3BAoCJTWAcTo1TYBRULacSKoyUPEHLifC3UEOWO05cuJWkUsEffKBCou9ZRtIuye2cWfAbOOM43IDHJFH2Z72B5VTA5YLffazimVqYGd8ba3Ptp8Y7Nqr6K7jWCJj55EzziiZTvSKYf7g3zCMzTZK-fb_Xtq809WqgynjS_Y-UBOCJH-J3Qty6vzha_rZ0U6lj-IlBxJl9oww8ZfCQDMrB-eTaCsDY54KA4AH50DWUvhE-TLHfDlSTK3p3XtZ0XvKviv-b4V9pEV7UuKSLL0sb5eG_emf9wivO_3gECuHsd-wyIKa_jbrye84GJG-a2KfBH4l_dK4e41Drs15aVIuAk4rn0aju5zZmUeaOff2asD8VIKb8ui4RRXB76eCHUyelhcRIZs0BFT4_vP4ZE_fnv1E2GZ1mYtWAvMS-bLbwH3",
                "deep_link": "https://www.kiwi.com/deep?affilid=apoorvflightsearch&currency=EUR&flightsId=0711019d4bc800005bf2a631_0&from=DEL&lang=en&passengers=1&to=JLR&booking_token=EifTNz0iSK4vBjIFuIjLo6XIs2NgBegvh_Om2X6XMd-Shb1zDm6SrKQAuFge_ORicQf4FtiLr01-JnTpyS4guoEdFfE5pQMrQbIRlcdPWCkgaK2mcV5VJvBhxiiT1J2yMZncGBGkVsuQ4gFnpnY_kkDCJUJlyLVqAGTn6i4M9sZkxUXmQfKbTrnWrtGTfSesmMQ3lsKA7EXIt7pqDuvv3NKzHGNw2rw1MxJGNa1hmJq9wIyloFxqAuX8wgbk1uD74wUxt38A0U2Vd7Cf86OzOW1SaGKnTmJ2-spW8tFfN_e6TGzyUPiiTFNUZNdWIay1y8Jgxv0mZqqxCZXf45ghJU3w24Ws9ulFb2VhUq0DRBCP0xO_vvW5kRkR04QvUcFgcplzlq1c0mUkSECOPSJZP005HEh-Ppk_57seTRToR9Zg=",
                "facilitated_booking_available": True,
                "pnr_count": 1,
                "has_airport_change": False,
                "technical_stops": 0,
                "throw_away_ticketing": False,
                "hidden_city_ticketing": False,
                "virtual_interlining": False,
                "local_arrival": "2023-02-12T09:10:00.000Z",
                "utc_arrival": "2023-02-12T03:40:00.000Z",
                "local_departure": "2023-02-12T07:35:00.000Z",
                "utc_departure": "2023-02-12T02:05:00.000Z"
            },
            {
                "id": "0711019d4bc90000ac131820_0",
                "flyFrom": "DEL",
                "flyTo": "JLR",
                "cityFrom": "New Delhi",
                "cityCodeFrom": "DEL",
                "cityTo": "Jabalpur",
                "cityCodeTo": "JLR",
                "countryFrom": {
                    "code": "IN",
                    "name": "India"
                },
                "countryTo": {
                    "code": "IN",
                    "name": "India"
                },
                "nightsInDest": "None",
                "quality": 69.666605,
                "distance": 668.53,
                "duration": {
                    "departure": 5700,
                    "return": 0,
                    "total": 5700
                },
                "price": 45,
                "conversion": {
                    "EUR": 45
                },
                "bags_price": {
                    "1": 0
                },
                "baglimit": {
                    "hand_height": 36,
                    "hand_length": 54,
                    "hand_weight": 7,
                    "hand_width": 18,
                    "hold_dimensions_sum": 158,
                    "hold_height": 52,
                    "hold_length": 78,
                    "hold_weight": 15,
                    "hold_width": 28
                },
                "availability": {
                    "seats": 2
                },
                "airlines": [
                    "SG"
                ],
                "route": [
                    {
                        "id": "0711019d4bc90000ac131820_0",
                        "combination_id": "0711019d4bc90000ac131820",
                        "flyFrom": "DEL",
                        "flyTo": "JLR",
                        "cityFrom": "New Delhi",
                        "cityCodeFrom": "DEL",
                        "cityTo": "Jabalpur",
                        "cityCodeTo": "JLR",
                        "airline": "SG",
                        "flight_no": 954,
                        "operating_carrier": "SG",
                        "operating_flight_no": "954",
                        "fare_basis": "USWB",
                        "fare_category": "M",
                        "fare_classes": "U",
                        "fare_family": "",
                        "return": 0,
                        "bags_recheck_required": False,
                        "vi_connection": False,
                        "guarantee": False,
                        "equipment": "None",
                        "vehicle_type": "aircraft",
                        "local_arrival": "2023-02-13T09:10:00.000Z",
                        "utc_arrival": "2023-02-13T03:40:00.000Z",
                        "local_departure": "2023-02-13T07:35:00.000Z",
                        "utc_departure": "2023-02-13T02:05:00.000Z"
                    }
                ],
                "booking_token": "EkNjbAE9FvGas87PHm34w290yjmQyWwBLGWpu5dB9yWBW4__gMr6JAEBkh3eIS9NNgsgUMSMUX9q_hZEbV_JqJJVIZn1813E9wpUUq-Xx7LHClX3dpNdItWwdMFhfjv_mnUrgDHndPu8Xtf8zdzu-a5r3F8FjfqahhltE16dWycnPtp_2ECV5HZh_cOVeGGEkAQSmimTBPCIYwZFS9emBkMT67kV4A9ElHmGcNAsGFMzGmgdjZd2QIIHdos0zrc4HRjUuUtZck6-F6-AzUV-SZQxmyWEIWlTmjAfqGqXyc8-OUMPPkzp_qt-ah4mpcYCpYxp9ypbF5-FdJy-BXd_tl_a0vfXEzE1J5Xvlt0U8E8bx7vTOf8utvHD0ekdOW9lIjh7jU-ise_ePzJWVisLB3CqNDgT_RoPpl4KnzMHNsBq84K5lONkIksMct3Q3bRVv5iyqdtekrQQXEPrqAeYOj4uCL8sTvRKi3ZAFwppV3EBfjcfj7mcbcwrDmY7Al9WvjGIlfUzJxSz0_CdIEkrq0I73-ognpA9pPEc3wFdw_aqVH7Qqaxt-nI5ASTU-h2H4",
                "deep_link": "https://www.kiwi.com/deep?affilid=apoorvflightsearch&currency=EUR&flightsId=0711019d4bc90000ac131820_0&from=DEL&lang=en&passengers=1&to=JLR&booking_token=E_7XTneTxbIToFDDfrNs9C9xLp4XOCD9hJnx6DDxTbUFN7hzKABoPTMMjZ4u28KxsKRMsh9uz5_IKRiPejb-nxh2B3xB6bH_12eVO8i4ZBu7BHvR4Ia0P3RXBjZo3en2j9nWMPQEZfmFq038ruIg3st094qu2r35udyILEafzVbV6zOp3mjLZgPJSyvX_1HvvrvBZ1LbVBTWQDXLG15pkA7Pbqu_HRXF4yMeHVb8GodHporXHI2w1FzFI6YNwcpSGRonW_73Q_eYnGquc33QN9rKCbve_oXJtMGtsHdaPovnjlnPQgVLcGFBZo0Sqg4tq8NxE-uV_mcp1IsHXrpXtFgJEJ7RdHql6vaStN9YxcYjEX1COP6G6w5WAl4Z2cU7AKinXCyg32QwnJxjNxvv4y9OIWfezKhKQicjQA_B0h1s=",
                "facilitated_booking_available": True,
                "pnr_count": 1,
                "has_airport_change": False,
                "technical_stops": 0,
                "throw_away_ticketing": False,
                "hidden_city_ticketing": False,
                "virtual_interlining": False,
                "local_arrival": "2023-02-13T09:10:00.000Z",
                "utc_arrival": "2023-02-13T03:40:00.000Z",
                "local_departure": "2023-02-13T07:35:00.000Z",
                "utc_departure": "2023-02-13T02:05:00.000Z"
            },
            {
                "id": "0711019d4bc700004e14eb95_0",
                "flyFrom": "DEL",
                "flyTo": "JLR",
                "cityFrom": "New Delhi",
                "cityCodeFrom": "DEL",
                "cityTo": "Jabalpur",
                "cityCodeTo": "JLR",
                "countryFrom": {
                    "code": "IN",
                    "name": "India"
                },
                "countryTo": {
                    "code": "IN",
                    "name": "India"
                },
                "nightsInDest": "None",
                "quality": 69.666605,
                "distance": 668.53,
                "duration": {
                    "departure": 5700,
                    "return": 0,
                    "total": 5700
                },
                "price": 45,
                "conversion": {
                    "EUR": 45
                },
                "bags_price": {
                    "1": 0
                },
                "baglimit": {
                    "hand_height": 36,
                    "hand_length": 54,
                    "hand_weight": 7,
                    "hand_width": 18,
                    "hold_dimensions_sum": 158,
                    "hold_height": 52,
                    "hold_length": 78,
                    "hold_weight": 15,
                    "hold_width": 28
                },
                "availability": {
                    "seats": 2
                },
                "airlines": [
                    "SG"
                ],
                "route": [
                    {
                        "id": "0711019d4bc700004e14eb95_0",
                        "combination_id": "0711019d4bc700004e14eb95",
                        "flyFrom": "DEL",
                        "flyTo": "JLR",
                        "cityFrom": "New Delhi",
                        "cityCodeFrom": "DEL",
                        "cityTo": "Jabalpur",
                        "cityCodeTo": "JLR",
                        "airline": "SG",
                        "flight_no": 954,
                        "operating_carrier": "SG",
                        "operating_flight_no": "954",
                        "fare_basis": "USWB",
                        "fare_category": "M",
                        "fare_classes": "U",
                        "fare_family": "",
                        "return": 0,
                        "bags_recheck_required": False,
                        "vi_connection": False,
                        "guarantee": False,
                        "equipment": "None",
                        "vehicle_type": "aircraft",
                        "local_arrival": "2023-02-11T09:10:00.000Z",
                        "utc_arrival": "2023-02-11T03:40:00.000Z",
                        "local_departure": "2023-02-11T07:35:00.000Z",
                        "utc_departure": "2023-02-11T02:05:00.000Z"
                    }
                ],
                "booking_token": "EiNLHMOaz4bZIwMQ7Y3sKvrTVWSa4ESY6MMaFnuPWirzPol8pJbP7aPn7TF6zTbMSysp3flaXEGoVrYsOoidR_4DrKRtmy5MjgJGRjwZKCcHH75pUZ7xyETGMC69OHqu-n6FHsxAs_WUloSD8bmOQxa5JRflizrM3ESPFge70cv8jvv5H9ArvJQmggt0pGCrrFz7cc6zQhcE36MVBw0sKA4Vsfw8diVja48zJ-m_FlkCDv5dgmGRpxGZaPY5UqoQ8pwTOXEUq0smT19U-3c1tm8gTOi2c_by4z2pDWzvUu35luj69uyh6tgZ41C8O5aCn45oQeM4TurK6erVPHkJSA_1mrJC0XpmqW75XNr-YyWfF5-fcfgnJq0ITrOz-X5Z0KhemmdCMmqOvkZ2DfzLkccrLE6vyHZMxBtDY19y1CoTF2rmcUCGV8qkwszUQ-trCGLjy4feY7t4rHnzI4l-BpLlQQtXIFJPKM-QvujCuXYo9HrT1dSX5Ec3SWTQo5s3uRzWBdUI2MNYO9xv48nTCKeqEz7WztSMQf_YfSliiLI8=",
                "deep_link": "https://www.kiwi.com/deep?affilid=apoorvflightsearch&currency=EUR&flightsId=0711019d4bc700004e14eb95_0&from=DEL&lang=en&passengers=1&to=JLR&booking_token=Es-PYooUpjCdS6xrCmFrRzuaeAewKMCLlPiwBy_rb_Zod9os7TF2lAMiDvn0S0WIykKQ0XR5mlRVM7TDRarHdhhpxvxkebnhfnMNaPK_K0zINidK8aokUq2mYdQbW_PzkuPvuKUbY3Htzg28-P14k9YXWe0PsiHbCBBjxri94mZReclxiCJdBs0xOkpZ9BfNJ_7IIebEPs1PwITIqRdeUF0OeQJkXSJfHZiRVyZX1Fwn4kl0eje388Wg3PvK_j2QyQBXpdUi6irXGEdq97s2vl5m1abU_fJbAPp00B2o6pjRqQEx_JBBwNhjMw8bRWolfUz-r8Sn202ywsZlJOqdZ86XLGz9IMQVFQayPExj9zkJc8wxeTScfmS4e1tixbiZS7d2mg_3aBaEqqHMfq9UneQG-7ceJzCal4zCn0MF1qng=",
                "facilitated_booking_available": True,
                "pnr_count": 1,
                "has_airport_change": False,
                "technical_stops": 0,
                "throw_away_ticketing": False,
                "hidden_city_ticketing": False,
                "virtual_interlining": False,
                "local_arrival": "2023-02-11T09:10:00.000Z",
                "utc_arrival": "2023-02-11T03:40:00.000Z",
                "local_departure": "2023-02-11T07:35:00.000Z",
                "utc_departure": "2023-02-11T02:05:00.000Z"
            },
            {
                "id": "071104914bc7000035e593f2_0",
                "flyFrom": "DEL",
                "flyTo": "BOM",
                "cityFrom": "New Delhi",
                "cityCodeFrom": "DEL",
                "cityTo": "Mumbai",
                "cityCodeTo": "BOM",
                "countryFrom": {
                    "code": "IN",
                    "name": "India"
                },
                "countryTo": {
                    "code": "IN",
                    "name": "India"
                },
                "nightsInDest": "None",
                "quality": 75.33326,
                "distance": 1139.47,
                "duration": {
                    "departure": 7800,
                    "return": 0,
                    "total": 7800
                },
                "price": 46,
                "conversion": {
                    "EUR": 46
                },
                "bags_price": {
                    "1": 0
                },
                "baglimit": {
                    "hand_height": 35,
                    "hand_length": 55,
                    "hand_weight": 7,
                    "hand_width": 25,
                    "hold_dimensions_sum": 158,
                    "hold_height": 52,
                    "hold_length": 78,
                    "hold_weight": 15,
                    "hold_width": 28
                },
                "availability": {
                    "seats": 1
                },
                "airlines": [
                    "G8"
                ],
                "route": [
                    {
                        "id": "071104914bc7000035e593f2_0",
                        "combination_id": "071104914bc7000035e593f2",
                        "flyFrom": "DEL",
                        "flyTo": "BOM",
                        "cityFrom": "New Delhi",
                        "cityCodeFrom": "DEL",
                        "cityTo": "Mumbai",
                        "cityCodeTo": "BOM",
                        "airline": "G8",
                        "flight_no": 530,
                        "operating_carrier": "G8",
                        "operating_flight_no": "530",
                        "fare_basis": "",
                        "fare_category": "M",
                        "fare_classes": "",
                        "fare_family": "",
                        "return": 0,
                        "bags_recheck_required": False,
                        "vi_connection": False,
                        "guarantee": False,
                        "equipment": "None",
                        "vehicle_type": "aircraft",
                        "local_arrival": "2023-02-11T08:10:00.000Z",
                        "utc_arrival": "2023-02-11T02:40:00.000Z",
                        "local_departure": "2023-02-11T06:00:00.000Z",
                        "utc_departure": "2023-02-11T00:30:00.000Z"
                    }
                ],
                "booking_token": "EZslfjl7eviLYkQiwnBVsXhihfL0X2zfs-OZVua7KQDDKrfWDv_IeCb4LFeJyPnlT2Gonb-YnhNwMG_S1PEpH6PhmE4rspLKaRR7KZsifGOrxpzU85P6SNn6QmTmgCWoRlT8gRbgqlqbSnjDUDTimyrxvjGcw6ilTI9uVvV7--79cKcIHD14zTYU_WtzY0JjgOr3T2aXOY2_DI5Gsl0PLJiwpBtrnmh9jaawsAct2-uzpxH-OzzfJWI8AWRJrzalJP0txk51EkdM8mPlmcQgGjgEGs477ZG94AVh4xXGRDCu-_4cp5n9fpjnF7_2rE6dCe3UXkBntmUyec3FxjS7jQhZUnT_CygA_kF5mELFZ0XlQHHVGkJtAbXD5WuS8hyfs_kkRme0iNOxwqtkaJbU0-Omp1enkWXhpGIAH3GQyH8QplWLS-O8tLfJCAd9c5tat79AbQ72j2bDZTZ4Yzssf8hh4mnHTrWVgJzozt9rjpob3Zgz2B9zO8n9cJuGcS6HjExg4QEdzayifaJqrNVfRhPANtgM_FpZREqdIEPBL5zBR6Ymz_jN2AMfWdqR--Vhv",
                "deep_link": "https://www.kiwi.com/deep?affilid=apoorvflightsearch&currency=EUR&flightsId=071104914bc7000035e593f2_0&from=DEL&lang=en&passengers=1&to=BOM&booking_token=Ej2XlL3WYA38P1Nir4h4TWhJ9hUqrzkGECsea8CfWdGQdTuHFakyA6pegU9OoexmcXHhBIldzdYO7tUQubKz2NR9WKghqz2sf0krsGRiBksXVDCsbfuJqmj1ZwmDaQfjfnd5SdwGVBzkGUc9Rx7AccVbhWzc9fskIgXELRx4QquVz9y3ZB-65imzgrIUmrFTr7NkNT1lI9O3V5Fr0fxBWIJWtz0reBYSACbkuXafa6kifU3t4rkwx4bHbe5AzDJmEl_I4BJ_NFdTcCYBL6oQ14d-quZKYmJ13_xUgMPZxdmZA9L87RapGHxZGFPQdW6z2QnA2rMnbSrg9Emo8SeqWxSQLnLZYPxfSZVjyUEuyG-JlaZRjL5m7LoeReOqJ_30eVwTSs0pBSgub9Okp4R_8u5PK0PvTV0_SuPZhcaB1u6w=",
                "facilitated_booking_available": True,
                "pnr_count": 1,
                "has_airport_change": False,
                "technical_stops": 0,
                "throw_away_ticketing": False,
                "hidden_city_ticketing": False,
                "virtual_interlining": False,
                "local_arrival": "2023-02-11T08:10:00.000Z",
                "utc_arrival": "2023-02-11T02:40:00.000Z",
                "local_departure": "2023-02-11T06:00:00.000Z",
                "utc_departure": "2023-02-11T00:30:00.000Z"
            },
            {
                "id": "071104914bc60000ffae3b01_0",
                "flyFrom": "DEL",
                "flyTo": "BOM",
                "cityFrom": "New Delhi",
                "cityCodeFrom": "DEL",
                "cityTo": "Mumbai",
                "cityCodeTo": "BOM",
                "countryFrom": {
                    "code": "IN",
                    "name": "India"
                },
                "countryTo": {
                    "code": "IN",
                    "name": "India"
                },
                "nightsInDest": "None",
                "quality": 76.33326,
                "distance": 1139.47,
                "duration": {
                    "departure": 7800,
                    "return": 0,
                    "total": 7800
                },
                "price": 47,
                "conversion": {
                    "EUR": 47
                },
                "bags_price": {
                    "1": 0
                },
                "baglimit": {
                    "hand_height": 35,
                    "hand_length": 55,
                    "hand_weight": 7,
                    "hand_width": 25,
                    "hold_dimensions_sum": 158,
                    "hold_height": 52,
                    "hold_length": 78,
                    "hold_weight": 15,
                    "hold_width": 28
                },
                "availability": {
                    "seats": 1
                },
                "airlines": [
                    "G8"
                ],
                "route": [
                    {
                        "id": "071104914bc60000ffae3b01_0",
                        "combination_id": "071104914bc60000ffae3b01",
                        "flyFrom": "DEL",
                        "flyTo": "BOM",
                        "cityFrom": "New Delhi",
                        "cityCodeFrom": "DEL",
                        "cityTo": "Mumbai",
                        "cityCodeTo": "BOM",
                        "airline": "G8",
                        "flight_no": 530,
                        "operating_carrier": "G8",
                        "operating_flight_no": "530",
                        "fare_basis": "",
                        "fare_category": "M",
                        "fare_classes": "Y",
                        "fare_family": "",
                        "return": 0,
                        "bags_recheck_required": False,
                        "vi_connection": False,
                        "guarantee": False,
                        "equipment": "None",
                        "vehicle_type": "aircraft",
                        "local_arrival": "2023-02-10T08:10:00.000Z",
                        "utc_arrival": "2023-02-10T02:40:00.000Z",
                        "local_departure": "2023-02-10T06:00:00.000Z",
                        "utc_departure": "2023-02-10T00:30:00.000Z"
                    }
                ],
                "booking_token": "EApEZqEkJMqkRjadw82HKU5wCLQObEr9nUBQ8-3-AdLxMOBuy0a9BEqJtKd8ELIcap0cNzQffpfMI1NUR6b-28ZS95-U4rrtBVtSsio7cFg7E_jl4un_lNz07CmVLKGCk93hBrcPu8KxRTgCquPMAxXphHb9oFKcTMoNlYh_H2K1wbLPnFkCpQKRfVNHWcTN8gBaGTcgY8CuVfXx6ngxKZ5C43hNEX9QIsgP33f49HMRtC-SEgYdr8pwvgHYttvrDBfZJL0dCwEJ86gCYkVD49FTHAn96uzf-KVy6aRz9jqzOC9DkY9y4J9c6rht-wd24wNOMxmiN_Zrr59vJmDkIOdrVlUN_-MPPwLY_jXoWL4vIM2hnd3NvDXz0HfF_aF5BktTEj9ov84Va0P2CYjOrq28YOiqCqbfDuC4ZdCFF4VIx1KkOucHmCC7fSZeoxX6GquIZFJ1h7gZFzlG0e75ea5Prw_Ij72cNhYHbd4_vif8R2m1JMkjSZkcI9L7k07iJZtJvCxEkXw4D7MVhtXhLraf-cc8H7VVg8arj43V5cyMAjBfa20pSPrvDxFZlnBNWgQxAlIpwDWuHUGuESM9s5qNmMhVlSG06NAw2rARaRg0=",
                "deep_link": "https://www.kiwi.com/deep?affilid=apoorvflightsearch&currency=EUR&flightsId=071104914bc60000ffae3b01_0&from=DEL&lang=en&passengers=1&to=BOM&booking_token=EafR6B3Kqcty8usfY30wz33gLnQCjT6rkyh_ym3EnI5sNlm9Cvsw1v_UKNFoqN2JwiHNLHNsK2EqVJTXfDcldHYkWxunjUl6yYQQGe-hqn72d4s0AYeQjm7vgTfbwjFup5VWN8Vj3pm3GGQ87f2B32wYAGJAZ2S-KOsE1TB2SGzeQ6YY9ZTLBWIcAzLHUEhyPH3AGmuXCzHVtKrQjN-dPHIuqwG-y8rrot4pPkSiCalBlQpTsDUNMiqyhr2bfTmTIFV3xJuMXqww56pg6rhNa9iGEIGuLqaUYWpqnMOMyhKTlAuvvmx5esfDQ9KCEldcPbw58C6VLAK644dZGIOIyI-aDaCHmXcx9mHjGiiS2UDfVflVMZwJ2ZdprKHEpYkJM-4BgIms3WvOcr7lQTXGFaTPW9UDOvfpmT7xmYxXZczZDdsMI0S4NqBEH7r5pZjqgRlrS3SHN4OjpcsVkj4619s5wYnAuIYB3yK_EXZuJu68=",
                "facilitated_booking_available": True,
                "pnr_count": 1,
                "has_airport_change": False,
                "technical_stops": 0,
                "throw_away_ticketing": False,
                "hidden_city_ticketing": False,
                "virtual_interlining": False,
                "local_arrival": "2023-02-10T08:10:00.000Z",
                "utc_arrival": "2023-02-10T02:40:00.000Z",
                "local_departure": "2023-02-10T06:00:00.000Z",
                "utc_departure": "2023-02-10T00:30:00.000Z"
            },
            {
                "id": "071104914bc800002003de56_0",
                "flyFrom": "DEL",
                "flyTo": "BOM",
                "cityFrom": "New Delhi",
                "cityCodeFrom": "DEL",
                "cityTo": "Mumbai",
                "cityCodeTo": "BOM",
                "countryFrom": {
                    "code": "IN",
                    "name": "India"
                },
                "countryTo": {
                    "code": "IN",
                    "name": "India"
                },
                "nightsInDest": "None",
                "quality": 76.33326,
                "distance": 1139.47,
                "duration": {
                    "departure": 7800,
                    "return": 0,
                    "total": 7800
                },
                "price": 47,
                "conversion": {
                    "EUR": 47
                },
                "bags_price": {
                    "1": 0
                },
                "baglimit": {
                    "hand_height": 35,
                    "hand_length": 55,
                    "hand_weight": 7,
                    "hand_width": 25,
                    "hold_dimensions_sum": 158,
                    "hold_height": 52,
                    "hold_length": 78,
                    "hold_weight": 15,
                    "hold_width": 28
                },
                "availability": {
                    "seats": 2
                },
                "airlines": [
                    "G8"
                ],
                "route": [
                    {
                        "id": "071104914bc800002003de56_0",
                        "combination_id": "071104914bc800002003de56",
                        "flyFrom": "DEL",
                        "flyTo": "BOM",
                        "cityFrom": "New Delhi",
                        "cityCodeFrom": "DEL",
                        "cityTo": "Mumbai",
                        "cityCodeTo": "BOM",
                        "airline": "G8",
                        "flight_no": 530,
                        "operating_carrier": "G8",
                        "operating_flight_no": "530",
                        "fare_basis": "",
                        "fare_category": "M",
                        "fare_classes": "Y",
                        "fare_family": "",
                        "return": 0,
                        "bags_recheck_required": False,
                        "vi_connection": False,
                        "guarantee": False,
                        "equipment": "None",
                        "vehicle_type": "aircraft",
                        "local_arrival": "2023-02-12T08:10:00.000Z",
                        "utc_arrival": "2023-02-12T02:40:00.000Z",
                        "local_departure": "2023-02-12T06:00:00.000Z",
                        "utc_departure": "2023-02-12T00:30:00.000Z"
                    }
                ],
                "booking_token": "E-amIez1q1yMAjsDotDNEDzHIVrVUAPejMlcZgxcGUhLtig1HWlgOpyCr-jLfKfHKVWKoLShIk8waBg94shp3zqErsYE5mENN89NPx6HNsFUZt5E0ogT-Jf-6owKUtPyuvFTyj0EA4oc6Jp20k9hhMzl_ZuKZGRw9NhMAW3gj7Sq7L8SEzLDNlocJ6F6RFmbtfUti8LaJP5S7k13xfHhO6smc5dkPpto47w2pTspVQXkY26THytlzjByLNNsOfd3Ju4mv3wG3HXlmdHHvZhBEc64rq_egRkN4N7AoOrX8TbrdXhSEp_UdLPrzTSMlm5Xw8IDa5ALx2kbdaNOaPj3NO9SIqiePYabHV6TVsYq_gT-6cLMQbdiefZHpo6Lc7PwWa-6gKqonI7dPhZfVKojNmUynoN9GmhqHDwrR7WVDWXUldvZiYtZxrAALq2dQvbyTowOIzvNrAZ3OrJaMmsjhjsLu1TY_Dm70BLhJpP1L9VFg2lLXgelYwGtdKU4lIdrWM-QIbEWIvuOxfLCElHQK8AaIdtqtdwbrjivNrWjK5BYmSRA4swLJb3JX2lP4NS8mJXUKVujNlEvpBKmKbJZzucz7HTaGIbmszRkikTiCRKE=",
                "deep_link": "https://www.kiwi.com/deep?affilid=apoorvflightsearch&currency=EUR&flightsId=071104914bc800002003de56_0&from=DEL&lang=en&passengers=1&to=BOM&booking_token=EWzj2-JaG3Ijv91zjZ8dQd-9hs8o_0_5ZJvnPnu3gUrFFYP68JtPyuOoi1gBnMINrvXvYvm03AZai2R0mWUvi-JPkADeMitkQmVrqAtb1H1lB-raeRrQ_OB02ywJa15O2Lm6jNGhd9z6O4P0Yoz-yPvzi6ow_94s-Qg3wjb_vO73pCDpsw4bCnMDfVvqicklxJI_0qrFjDupIvX155MCqpSePf6DwsdtZDiLOJorIw-Z55uiIWyXbg8qH8We9TDlieXhXbtTizFAPk-4zskWCasek2NWosQ7UKkfxDIbUs32u89G9B6TEZRDN_aWMcmK3KWVfJAdO-jgXFetCqzX1lZZG_KPu39vsMqYxaXPHMLvL11oVyj2MtehExQHyKfoSo3LCYzWFGgjFsFgsI9GSktgi3wvThUrGTGpywdiRWYwPb6ad1p6zrOyiU8u-LPy7Vu1bCPFKuDNp_3dBjVwlLLsGKriB0Ibt7AvE4GQ03JM=",
                "facilitated_booking_available": True,
                "pnr_count": 1,
                "has_airport_change": False,
                "technical_stops": 0,
                "throw_away_ticketing": False,
                "hidden_city_ticketing": False,
                "virtual_interlining": False,
                "local_arrival": "2023-02-12T08:10:00.000Z",
                "utc_arrival": "2023-02-12T02:40:00.000Z",
                "local_departure": "2023-02-12T06:00:00.000Z",
                "utc_departure": "2023-02-12T00:30:00.000Z"
            },
            {
                "id": "071104c24bc9000076c31085_0",
                "flyFrom": "DEL",
                "flyTo": "LKO",
                "cityFrom": "New Delhi",
                "cityCodeFrom": "DEL",
                "cityTo": "Lucknow",
                "cityCodeTo": "LKO",
                "countryFrom": {
                    "code": "IN",
                    "name": "India"
                },
                "countryTo": {
                    "code": "IN",
                    "name": "India"
                },
                "nightsInDest": "None",
                "quality": 69.33328,
                "distance": 423.95,
                "duration": {
                    "departure": 4200,
                    "return": 0,
                    "total": 4200
                },
                "price": 48,
                "conversion": {
                    "EUR": 48
                },
                "bags_price": {
                    "1": 0
                },
                "baglimit": {
                    "hand_height": 35,
                    "hand_length": 55,
                    "hand_weight": 8,
                    "hand_width": 25,
                    "hold_dimensions_sum": 158,
                    "hold_height": 52,
                    "hold_length": 78,
                    "hold_weight": 25,
                    "hold_width": 28,
                    "personal_item_height": 20,
                    "personal_item_length": 40,
                    "personal_item_weight": 5,
                    "personal_item_width": 10
                },
                "availability": {
                    "seats": 6
                },
                "airlines": [
                    "AI"
                ],
                "route": [
                    {
                        "id": "071104c24bc9000076c31085_0",
                        "combination_id": "071104c24bc9000076c31085",
                        "flyFrom": "DEL",
                        "flyTo": "LKO",
                        "cityFrom": "New Delhi",
                        "cityCodeFrom": "DEL",
                        "cityTo": "Lucknow",
                        "cityCodeTo": "LKO",
                        "airline": "AI",
                        "flight_no": 411,
                        "operating_carrier": "AI",
                        "operating_flight_no": "411",
                        "fare_basis": "UIP",
                        "fare_category": "M",
                        "fare_classes": "U",
                        "fare_family": "",
                        "return": 0,
                        "bags_recheck_required": False,
                        "vi_connection": False,
                        "guarantee": False,
                        "equipment": "None",
                        "vehicle_type": "aircraft",
                        "local_arrival": "2023-02-13T08:15:00.000Z",
                        "utc_arrival": "2023-02-13T02:45:00.000Z",
                        "local_departure": "2023-02-13T07:05:00.000Z",
                        "utc_departure": "2023-02-13T01:35:00.000Z"
                    }
                ],
                "booking_token": "ExCxtG49jy_KIguxBV-Wb_YRsiUFDDuRokz4fvvf_HgzCCRpUS3k0wUuBYsQ_spDekY4o5cR3TfUz6s4NW9oesRnTw0jnbi2ZTD4F-EgL2SamAgiLUlkZ6FUkmRfo_1ZJIc7eAT0XYs6S2OX6exIpuTc9ZGoteTdmg_rqA_OJNfKQRNJ7i3fWHwOD4fBqrksVJcY2SSgsmBbnzNDmcCB8LxetFaQ8-M58-2SYBgOAhAsIiXPCne8m_WhUMoayApnfRxptX6pPpQaInZFXmnkVcKNJGvtzyshY2Z1RFnczy6Ll8qLZKSvmbnl2O1trXycAdJz5BL3E6e6ghfLIEJ5KUaW8ThD-Oj7CPi7n8Kbaw1gt0oMg_tyxkHnQ2KkXPrD7wBLSUXWzwwSeMvPWqbvn0sQE2IAehelZIeKAEsWgz9bSlDTmjWPRGtuBmQMcacHpCft21sziALqCGwC9IWflQu5zfKMFPk1-GxozK7gJ93DHxaYO9ZpaU2j_RHBsO_Y2qdVaghh66g-c_Xu4oUtMIo3uFON-RBFt07NMnvzqvW_3fg9nXWbnL9ORy73vKgceEGy7_TZ33v6S8Oy3KFQk4A==",
                "deep_link": "https://www.kiwi.com/deep?affilid=apoorvflightsearch&currency=EUR&flightsId=071104c24bc9000076c31085_0&from=DEL&lang=en&passengers=1&to=LKO&booking_token=EmlWTuk6S-MDG8eyzCTFuvq6wxK3AWC2vGLnrVi48lwiGWX_zIDVW3KSbAP5NZHX1j_rViBc56Z6tp86N1x4LKFHxmhOhoiATDvN2Y2lSgVM2gdhhFnZ8RENd4qCEf46_GcNeaPjEINPwxSnCK95q1NPmncIBG9IgXVa8SAo-2e4LzO38p_B49ZcJnDaCwUtbHYULmR1KAfXWe-_nLlxTCxBvQdeCt7pUS-PRDUbTA_3KLfrVhKI4rlAnNichzunLwR8MHD13CxAyBO97fPCpVW4efTZtVdsUp6zUbEXKR19dH8td_nhOHtRtEZtwTKt-9Qn3NDmI5P4n7gNn4jyAVWyLdHHHASymplf1rgX49vpFuc7BLNZiDXIQXhfjEYR4JygZ_S0-Mfu1aFFU2wPC24dKmDfbhAKi-PMFjsRkyRAfzkdqWEFBleb5wDVWc1nuCBu8lAyBu8aIneGd6NWOCQ==",
                "facilitated_booking_available": True,
                "pnr_count": 1,
                "has_airport_change": False,
                "technical_stops": 0,
                "throw_away_ticketing": False,
                "hidden_city_ticketing": False,
                "virtual_interlining": False,
                "local_arrival": "2023-02-13T08:15:00.000Z",
                "utc_arrival": "2023-02-13T02:45:00.000Z",
                "local_departure": "2023-02-13T07:05:00.000Z",
                "utc_departure": "2023-02-13T01:35:00.000Z"
            },
            {
                "id": "07111b744bc8000075a1ab8c_0",
                "flyFrom": "DEL",
                "flyTo": "BHO",
                "cityFrom": "New Delhi",
                "cityCodeFrom": "DEL",
                "cityTo": "Bhopal",
                "cityCodeTo": "BHO",
                "countryFrom": {
                    "code": "IN",
                    "name": "India"
                },
                "countryTo": {
                    "code": "IN",
                    "name": "India"
                },
                "nightsInDest": "None",
                "quality": 71.99994,
                "distance": 588.1,
                "duration": {
                    "departure": 5400,
                    "return": 0,
                    "total": 5400
                },
                "price": 48,
                "conversion": {
                    "EUR": 48
                },
                "bags_price": {
                    "1": 0
                },
                "baglimit": {
                    "hand_height": 38,
                    "hand_length": 57,
                    "hand_weight": 7,
                    "hand_width": 20,
                    "hold_dimensions_sum": 158,
                    "hold_height": 52,
                    "hold_length": 78,
                    "hold_weight": 15,
                    "hold_width": 28
                },
                "availability": {
                    "seats": 2
                },
                "airlines": [
                    "6E"
                ],
                "route": [
                    {
                        "id": "07111b744bc8000075a1ab8c_0",
                        "combination_id": "07111b744bc8000075a1ab8c",
                        "flyFrom": "DEL",
                        "flyTo": "BHO",
                        "cityFrom": "New Delhi",
                        "cityCodeFrom": "DEL",
                        "cityTo": "Bhopal",
                        "cityCodeTo": "BHO",
                        "airline": "6E",
                        "flight_no": 6022,
                        "operating_carrier": "6E",
                        "operating_flight_no": "6022",
                        "fare_basis": "SRIP",
                        "fare_category": "M",
                        "fare_classes": "X",
                        "fare_family": "",
                        "return": 0,
                        "bags_recheck_required": False,
                        "vi_connection": False,
                        "guarantee": False,
                        "equipment": "None",
                        "vehicle_type": "aircraft",
                        "local_arrival": "2023-02-12T08:20:00.000Z",
                        "utc_arrival": "2023-02-12T02:50:00.000Z",
                        "local_departure": "2023-02-12T06:50:00.000Z",
                        "utc_departure": "2023-02-12T01:20:00.000Z"
                    }
                ],
                "booking_token": "EQfL9l9EgqLUsVxMEJcB3LoVKa5crS60eejd_lPLFxNS3LZJRRfdjNW7T9DGf4UFcZFtN9FTPm5UgNTRixyyM5RUY7BDmEIlJAZBxvdT1hLJDPTsuvi7Vo9ozrk-FiaiyQP3yixvByuvhTXw5y6pAaqD1mya5zzVG8BGhtc9O2L4oGHb8HSQlnrbcRXD0vCDxVvlOfTqhssSFn7LwpQ3cuUQOSkTxS6UXqP9zSFt6pHSmah9GbwE7u97IJ7GDgIsTpJlJoF8WcEv67W19UIVjoeGOZXJI2oz_aKrD_e79LiYVpxp9cev0cvJBT1FBuQH9gg9KoLOPoNBNyQdF82xshtOhToK6fVmpPVcydT3g03mCjIndUBt6Grj5b794vVNVsUVsX4XR2_2075qGcmYGSJnzgZrAY-OOwXi1Lkq01O0b8g3Szrwz2Ita5vha2vrs8Q9dNuwedYWAyZPsJzMF3cv_xSg7tMaClgo2D3ler7xcg7zXdYgd1ud8CYltcKtqHcXt7ZSiYao3Qk5oyPN3QzgNpSMvhvO6pLZ0WjN2bHJJh3nkWQ5cxwRtRraIhSog",
                "deep_link": "https://www.kiwi.com/deep?affilid=apoorvflightsearch&currency=EUR&flightsId=07111b744bc8000075a1ab8c_0&from=DEL&lang=en&passengers=1&to=BHO&booking_token=EgwJs2-S3kPbD3_ksVx4tv8QyPShVqCqf_DqpafpBSlHaG8k1-Tyy13HdmbvTc5oqJu2mQNImpxCaU2nOH1PlaE1ub65jfNyMvI3zU8QwybEFA4pyBtRzF3P_u_IyAvgGsen8IQxdXYS-Pns2dfQ3PatrgxcdO8Qqf0gvgOQ3bWhBCS6VPt59E9djN7ffYY9sAovXJe04Qqv8XZeW4ct_c1Gyd2kFY_VbUZ-bLz-et-t1iVN6Tz18D4joosks1oqtY3UjD2RyXFiL3dVxkrdFg2-_zrJanMR37JpAQGdk3IRrAAqapAPIACDlCa7rNvyAg5Jh0WK9L6s7S_fN3ByVBp1YXbV0--2d8_UTqh8PiKOp5ctN2u53LKVxl6eEhaN_f6HBSFP8SsFIAWDceftjkYB0RcDUxd4RBR7fnAjME_Y=",
                "facilitated_booking_available": True,
                "pnr_count": 1,
                "has_airport_change": False,
                "technical_stops": 0,
                "throw_away_ticketing": False,
                "hidden_city_ticketing": False,
                "virtual_interlining": False,
                "local_arrival": "2023-02-12T08:20:00.000Z",
                "utc_arrival": "2023-02-12T02:50:00.000Z",
                "local_departure": "2023-02-12T06:50:00.000Z",
                "utc_departure": "2023-02-12T01:20:00.000Z"
            },
            {
                "id": "07111c024bc90000a58bc5ca_0",
                "flyFrom": "DEL",
                "flyTo": "VNS",
                "cityFrom": "New Delhi",
                "cityCodeFrom": "DEL",
                "cityTo": "Varanasi",
                "cityCodeTo": "VNS",
                "countryFrom": {
                    "code": "IN",
                    "name": "India"
                },
                "countryTo": {
                    "code": "IN",
                    "name": "India"
                },
                "nightsInDest": "None",
                "quality": 73.333275,
                "distance": 667.75,
                "duration": {
                    "departure": 5100,
                    "return": 0,
                    "total": 5100
                },
                "price": 50,
                "conversion": {
                    "EUR": 50
                },
                "bags_price": {
                    "1": 0
                },
                "baglimit": {
                    "hand_height": 36,
                    "hand_length": 54,
                    "hand_weight": 7,
                    "hand_width": 18,
                    "hold_dimensions_sum": 158,
                    "hold_height": 52,
                    "hold_length": 78,
                    "hold_weight": 15,
                    "hold_width": 28
                },
                "availability": {
                    "seats": 1
                },
                "airlines": [
                    "SG"
                ],
                "route": [
                    {
                        "id": "07111c024bc90000a58bc5ca_0",
                        "combination_id": "07111c024bc90000a58bc5ca",
                        "flyFrom": "DEL",
                        "flyTo": "VNS",
                        "cityFrom": "New Delhi",
                        "cityCodeFrom": "DEL",
                        "cityTo": "Varanasi",
                        "cityCodeTo": "VNS",
                        "airline": "SG",
                        "flight_no": 958,
                        "operating_carrier": "SG",
                        "operating_flight_no": "958",
                        "fare_basis": "VSWB",
                        "fare_category": "M",
                        "fare_classes": "V",
                        "fare_family": "",
                        "return": 0,
                        "bags_recheck_required": False,
                        "vi_connection": False,
                        "guarantee": False,
                        "equipment": "None",
                        "vehicle_type": "aircraft",
                        "local_arrival": "2023-02-13T20:55:00.000Z",
                        "utc_arrival": "2023-02-13T15:25:00.000Z",
                        "local_departure": "2023-02-13T19:30:00.000Z",
                        "utc_departure": "2023-02-13T14:00:00.000Z"
                    }
                ],
                "booking_token": "EJDAFsQHrGmqtUmu4_sdUX19W9pFzh5jc8Huig__UqTCvzr2eyD5jKdmdH7EgW1b_UIi6L6z-VXi_o2D9GAUu5mrA0eRmA1JFvx_SpwxEe8ZAkMR57-OPKbJuLwUZlcFtl5Dno-Z1OPpcsVGB59h-UK3RR7pkvzQPQpHflXWICE89DbVO9tlh5tFCYCMcwonP81mnuBEmOfi-tF5YjbJkvEG08bpfbhKV7yb08WZDcNa21oS115GfJjPG1KgVTBXdguN4hYPe2xGYd0cMDzilLaQfxrT1OAjmr5syFYBuWT36T9dtK2zh1UnBiKgC3zD0kwASwxU7m4ZNy4XY0nh04QwYKn8xfD7535joFuovAbZ7A0qU2Z9wknRkSoxt_3FwXE24Qs4eF9j0WTNjZfC0n22hkPIBm-qAI2Ka0jqBWKmf9g-E5kDzeJNOyFhkpx6RVG3nQ51n2ev7jp4ElWJbADi3hNX4h4s1_QiBi6KvE2__GQeyq8tPRkk-oBBECQ6qORwnL1F8ezoCQrhVvO-UR8R5tGxibAZE0G10ZGxvTD9vfnQB7DyI7gzSeF-87Go5",
                "deep_link": "https://www.kiwi.com/deep?affilid=apoorvflightsearch&currency=EUR&flightsId=07111c024bc90000a58bc5ca_0&from=DEL&lang=en&passengers=1&to=VNS&booking_token=ErIeUCxxOYGU1PmB4z8sQCMG1hE_B0M5DKl_kFvjvdpbzpIk7NHujy-ENehB8vwASJtfuaxfcMGkWR9ccFrrzN0Aw-W7Pb_ErmhQdhLjjs0IS3q-7GPBGb7P01mjQhDfu5IL7pgU7FVEDICtLJReOqR18plVqqNUHCPyIT96nMj7pFSbM4DA5t3xhcUxGDpD_i0PWvtYmqsYxYlNX-KYOHaSO7D2_aS46w1Nw7uf9NrtWUo0zBpbPHH4WgjQpGikiW4yEUj17yRPXaSjcIVDDs61vk6Brk8QctnrCbD_DKem-0kLiVC1M5bz-ap8PIpOJ2Of7-XEQ_JluAZi1gw-nxPke0-fwzLtlkR0C_cymCgmckNPQIsQwHvJuBgvmqVO9FwtIDQXlh8hkp-dXKHfCCwvh80pQWF3O_6TK69p47Jg=",
                "facilitated_booking_available": True,
                "pnr_count": 1,
                "has_airport_change": False,
                "technical_stops": 0,
                "throw_away_ticketing": False,
                "hidden_city_ticketing": False,
                "virtual_interlining": False,
                "local_arrival": "2023-02-13T20:55:00.000Z",
                "utc_arrival": "2023-02-13T15:25:00.000Z",
                "local_departure": "2023-02-13T19:30:00.000Z",
                "utc_departure": "2023-02-13T14:00:00.000Z"
            },
            {
                "id": "071104834bc7000050b3c4e1_0",
                "flyFrom": "DEL",
                "flyTo": "NAG",
                "cityFrom": "New Delhi",
                "cityCodeFrom": "DEL",
                "cityTo": "Nagpur",
                "cityCodeTo": "NAG",
                "countryFrom": {
                    "code": "IN",
                    "name": "India"
                },
                "countryTo": {
                    "code": "IN",
                    "name": "India"
                },
                "nightsInDest": "None",
                "quality": 73.99994,
                "distance": 854.82,
                "duration": {
                    "departure": 5400,
                    "return": 0,
                    "total": 5400
                },
                "price": 50,
                "conversion": {
                    "EUR": 50
                },
                "bags_price": {
                    "1": 0
                },
                "baglimit": {
                    "hand_height": 35,
                    "hand_length": 55,
                    "hand_weight": 7,
                    "hand_width": 25,
                    "hold_dimensions_sum": 158,
                    "hold_height": 52,
                    "hold_length": 78,
                    "hold_weight": 15,
                    "hold_width": 28
                },
                "availability": {
                    "seats": 2
                },
                "airlines": [
                    "G8"
                ],
                "route": [
                    {
                        "id": "071104834bc7000050b3c4e1_0",
                        "combination_id": "071104834bc7000050b3c4e1",
                        "flyFrom": "DEL",
                        "flyTo": "NAG",
                        "cityFrom": "New Delhi",
                        "cityCodeFrom": "DEL",
                        "cityTo": "Nagpur",
                        "cityCodeTo": "NAG",
                        "airline": "G8",
                        "flight_no": 2519,
                        "operating_carrier": "",
                        "operating_flight_no": "",
                        "fare_basis": "NO9RBSNE",
                        "fare_category": "M",
                        "fare_classes": "N",
                        "fare_family": "",
                        "return": 0,
                        "bags_recheck_required": False,
                        "vi_connection": False,
                        "guarantee": False,
                        "equipment": "None",
                        "vehicle_type": "aircraft",
                        "local_arrival": "2023-02-11T22:20:00.000Z",
                        "utc_arrival": "2023-02-11T16:50:00.000Z",
                        "local_departure": "2023-02-11T20:50:00.000Z",
                        "utc_departure": "2023-02-11T15:20:00.000Z"
                    }
                ],
                "booking_token": "EwD8HpNU3YyO2BmfWwEpNtD7iwZwNjYnF21yT1rbYO-gmDQ8P5ku-HV4JFRf_k3dUFOnsf-j1TFHxKxEO82YDG2111p3hzYxxxL5vrx6qwbPxLKnqXJz92NiSJga2_vWVwAMEsRVcRQwQ3yIAkeqxSBd5iJrsli1zIOjcQhRvRtUxs78pDW9MIWDLvKw9CmLCS6gPepfhAx5pZPnS3FqV2uqc6G_-x5oPJo_UQVUUgluaZAf49ua-WcHEK1ISnRCKGYM__cf9lwyYsTohQY-tvE8J5Llv2ZwYOzxuIqlHkm1DHZNBcOMI73Rb-7BPHLPO-dFswghp9eleWQ5dg1hb01mbh_41Gg2Xq1afuDaahzrf9HCdLZVpu1l8psXlJDiE6XttZiJZgb-Vknxi7eLBUfz5voGAT1OaOCBP0Fxu9lwTxQhcQ8FJKLJYDFpiqnMNg8I3GEGnZ1jNTLFSKVsMMlTi6Y0ZO5td-wQk-ELyjZMfTvgbA-GnHYK7NCNtmliqXKLUNMHuVt_oARJkatZTaeUkbx68MvqG3utmU81S6J-GhXkG3L8m0oNehc0mmq4l",
                "deep_link": "https://www.kiwi.com/deep?affilid=apoorvflightsearch&currency=EUR&flightsId=071104834bc7000050b3c4e1_0&from=DEL&lang=en&passengers=1&to=NAG&booking_token=EJvNAuwtxdzZWrsPt67CArdXLm44-v3uiKYWQmRqZqxTQ_2HxGDRKJixGC0_MTExPaYduuxah_6-GYikqbkZfHaM9Uq1aVRVbT5DFnbuz7iTw6gTax-PUSwoYRxz1EzygoHSUIFmEuE4oAmgvxrMr2GYhrXsTIYP_GM1BujJ12lQf_687n3-nZv-ILuBE8hhqJUWZt0wk7bBHAEBBLVUvUTIdAQDB506RJVtbHFJL4h0Fk7-VMpwL_A5Pxh22J2d_TAv6G_ejm7lFV61ZvmqNqgUSfaHGV_8mCOBtHZlc_o88IkkytU7yHZ4YPEnoMvMKdWOghY_YRiT35qGkkFUhhazro-J_jFOtZ1NmG5BfjrS39IGwf2YhD9bopdAQQc_Nd2C9ukcJNwYCUCwYWSDW2tHWfoTE-s3khYu3R9y4-iM=",
                "facilitated_booking_available": True,
                "pnr_count": 1,
                "has_airport_change": False,
                "technical_stops": 0,
                "throw_away_ticketing": False,
                "hidden_city_ticketing": False,
                "virtual_interlining": False,
                "local_arrival": "2023-02-11T22:20:00.000Z",
                "utc_arrival": "2023-02-11T16:50:00.000Z",
                "local_departure": "2023-02-11T20:50:00.000Z",
                "utc_departure": "2023-02-11T15:20:00.000Z"
            },
            {
                "id": "071104834bc90000eb5a8411_0",
                "flyFrom": "DEL",
                "flyTo": "NAG",
                "cityFrom": "New Delhi",
                "cityCodeFrom": "DEL",
                "cityTo": "Nagpur",
                "cityCodeTo": "NAG",
                "countryFrom": {
                    "code": "IN",
                    "name": "India"
                },
                "countryTo": {
                    "code": "IN",
                    "name": "India"
                },
                "nightsInDest": "None",
                "quality": 73.99994,
                "distance": 854.82,
                "duration": {
                    "departure": 5400,
                    "return": 0,
                    "total": 5400
                },
                "price": 50,
                "conversion": {
                    "EUR": 50
                },
                "bags_price": {
                    "1": 0
                },
                "baglimit": {
                    "hand_height": 35,
                    "hand_length": 55,
                    "hand_weight": 7,
                    "hand_width": 25,
                    "hold_dimensions_sum": 158,
                    "hold_height": 52,
                    "hold_length": 78,
                    "hold_weight": 15,
                    "hold_width": 28
                },
                "availability": {
                    "seats": 2
                },
                "airlines": [
                    "G8"
                ],
                "route": [
                    {
                        "id": "071104834bc90000eb5a8411_0",
                        "combination_id": "071104834bc90000eb5a8411",
                        "flyFrom": "DEL",
                        "flyTo": "NAG",
                        "cityFrom": "New Delhi",
                        "cityCodeFrom": "DEL",
                        "cityTo": "Nagpur",
                        "cityCodeTo": "NAG",
                        "airline": "G8",
                        "flight_no": 2519,
                        "operating_carrier": "",
                        "operating_flight_no": "",
                        "fare_basis": "NO9RBSNE",
                        "fare_category": "M",
                        "fare_classes": "N",
                        "fare_family": "",
                        "return": 0,
                        "bags_recheck_required": False,
                        "vi_connection": False,
                        "guarantee": False,
                        "equipment": "None",
                        "vehicle_type": "aircraft",
                        "local_arrival": "2023-02-13T22:20:00.000Z",
                        "utc_arrival": "2023-02-13T16:50:00.000Z",
                        "local_departure": "2023-02-13T20:50:00.000Z",
                        "utc_departure": "2023-02-13T15:20:00.000Z"
                    }
                ],
                "booking_token": "EuIVzBBVRutCyEzQ9zIaf2B2NbfdYpgmuYgQpT5BbFNpf2lc_X9pLg2MMHyT1AhA4jvLhhOshiicCoC8MaKnMRhLDKBRNaz2fFIOxUcE08KC0fWq6F5nFGmsiuZjZWXFP3mSBY_h2Yqp2BoIHthnYHoG6JUEkOktX1SbJpRr94b5OFYMKS5bVDbkfrXgE121of3nb2smGnnLS7TiBDlLNaBLM2tIw27hDaDNGkhq277LczabhHtjZDVReMEyiecCRRTTRVNKMuKImVQtJuGOtSk6rsVQP0FeLxVGBPZkba-wqgTeAEJqCdkXtPTDNEgTw_SeFh8Asw5sENT_fCoUwxbLfLUfZUMI0l_WDe3JMCscsgYUJW6f5upENGPN9Aiy5stnLojDO8bSmXcQhOYPI-EJKEN5I967g7GezOn4WI538t5wzFVeXxzyMEdx00Sq-yUpW3lh-WVHcKU5okYi0eVS_yOo8gE_fGD3KiVJUUVc56hHzKMPFcZ6Z9pZMcb_AkI0-pBbDoitI51uHQHpb-uW5cykXvhLTp5LL3Jsj4mEqrSdj7uO93UZz10qiOkRh",
                "deep_link": "https://www.kiwi.com/deep?affilid=apoorvflightsearch&currency=EUR&flightsId=071104834bc90000eb5a8411_0&from=DEL&lang=en&passengers=1&to=NAG&booking_token=EdrSrfsPpqLr9_DwYZqiCe0dyXSMV__HIIPZTSArci43y58yskRUXAIdxO3F--z1ZXeMQJU2X-s9MtrqEirNbEOm9Xr8gZWSLqokzOE1jG2blLh2IB-hHRiaehh4tuD6dmlMiWoheXSd58e4xG7iguxe0uGoSCG025NXdrBQGAspG9vrGv9fGTdAgd-GmG95hOd0U4g_MA_wYqLXuGTsryIuE15qe5NLhY_WMW-2VH5xFIJM-6I1DAGwcvkQ7Egzb9g945C-OKskdErWDqjelqk18iX923_rWpFMbd2_0gPMyYUtaEg9TI7nExbU4xS5qB8ypz7jfLnO4yoATADC6acrD4FJ4YQ_BVjnwbV5MBQ-o_JKePd1JgXkdUJb9672TAd5WAAcKfd6ONhV6bBi5tHGMu2AW0t9QPYTg3ew3V3d7sIy3MSy5ZIBst4lxgf3Y",
                "facilitated_booking_available": True,
                "pnr_count": 1,
                "has_airport_change": False,
                "technical_stops": 0,
                "throw_away_ticketing": False,
                "hidden_city_ticketing": False,
                "virtual_interlining": False,
                "local_arrival": "2023-02-13T22:20:00.000Z",
                "utc_arrival": "2023-02-13T16:50:00.000Z",
                "local_departure": "2023-02-13T20:50:00.000Z",
                "utc_departure": "2023-02-13T15:20:00.000Z"
            },
            {
                "id": "071104914bc7000071f1d951_0",
                "flyFrom": "DEL",
                "flyTo": "BOM",
                "cityFrom": "New Delhi",
                "cityCodeFrom": "DEL",
                "cityTo": "Mumbai",
                "cityCodeTo": "BOM",
                "countryFrom": {
                    "code": "IN",
                    "name": "India"
                },
                "countryTo": {
                    "code": "IN",
                    "name": "India"
                },
                "nightsInDest": "None",
                "quality": 78.666595,
                "distance": 1139.47,
                "duration": {
                    "departure": 7500,
                    "return": 0,
                    "total": 7500
                },
                "price": 50,
                "conversion": {
                    "EUR": 50
                },
                "bags_price": {
                    "1": 0
                },
                "baglimit": {
                    "hand_height": 36,
                    "hand_length": 54,
                    "hand_weight": 7,
                    "hand_width": 18,
                    "hold_dimensions_sum": 158,
                    "hold_height": 52,
                    "hold_length": 78,
                    "hold_weight": 15,
                    "hold_width": 28
                },
                "availability": {
                    "seats": 2
                },
                "airlines": [
                    "SG"
                ],
                "route": [
                    {
                        "id": "071104914bc7000071f1d951_0",
                        "combination_id": "071104914bc7000071f1d951",
                        "flyFrom": "DEL",
                        "flyTo": "BOM",
                        "cityFrom": "New Delhi",
                        "cityCodeFrom": "DEL",
                        "cityTo": "Mumbai",
                        "cityCodeTo": "BOM",
                        "airline": "SG",
                        "flight_no": 8169,
                        "operating_carrier": "SG",
                        "operating_flight_no": "8169",
                        "fare_basis": "PSAV",
                        "fare_category": "M",
                        "fare_classes": "P",
                        "fare_family": "",
                        "return": 0,
                        "bags_recheck_required": False,
                        "vi_connection": False,
                        "guarantee": False,
                        "equipment": "None",
                        "vehicle_type": "aircraft",
                        "local_arrival": "2023-02-11T22:05:00.000Z",
                        "utc_arrival": "2023-02-11T16:35:00.000Z",
                        "local_departure": "2023-02-11T20:00:00.000Z",
                        "utc_departure": "2023-02-11T14:30:00.000Z"
                    }
                ],
                "booking_token": "EvYSAmseUwvMF7E_18-Kt9TbJWcq_H6k2Xvx17JxfaNmTS68on6VDVrjqf3x0nyye5ZIiwMTD_D5oLCgzowlTSODjKTku5esZ_1umGIXESlJXCXIoDvlJxOZNR3QkUNec9hQvnVazONvRSDtojGnY0S6QOFr8ficd8ibCHwcPQS24pD0_taC9kzzUU_Seab8gQHOtOVUOsYznb6djtrmL-B0Fk1iVnPgpbKzAkj5gnhSQNi42fDyp0C-tOYfW7crWMds_JgbC1KEUt3PjrmkpwerlR_nIKl8obqleemSgq4aekpkW20BTYVBjA5afyzqup8eXIbX4N3u25XO7-4ufJ2FNFIG-iaZ5tbbZJ5oa1GewyNe4fMQOvIIeX-od3CCwxTXO9b9KY7S1pxHwv5UQQzt2B-oSAUfLCVwdA8-N_hfgjFRvBKEt1IeJ9on7K2W-Ymgxpc7YmOal0gyvHhnhVORHmfkcEke9ODWTcS9psrp9qwRaPYTdoPRw_kjq5ZikOQjhbxiMkg88HoWRhDj-QQi7ABp5B2rWB8mPIO2xmSA=",
                "deep_link": "https://www.kiwi.com/deep?affilid=apoorvflightsearch&currency=EUR&flightsId=071104914bc7000071f1d951_0&from=DEL&lang=en&passengers=1&to=BOM&booking_token=EQzjprbO1K0rQ7-c-TVq6WRGL_FcJ9gg1vf8KhWWGXlg5GV5jNtSl7aTgV4LqzKfdR0A625Ka7_07LgE2V0vShJzf9nRFImORcYSM4g9ioMPJiRuCb4J5tiLO_3Z1ylCZrcnt2kTB9eFbwEji-D-SNf39zQQhdvsI4zaXkGg4gfpQJ36_9z7vAtK1CH4_PZJE4GsdRD0pFCd64KMLyq1ZsXRQ1kOTNVSma2Mqvysnqo3YK7NnauXPv5bwYCZHAztvjXLYfsW8rwSyn9zJHa8PMUZUpn3WeRFaQAN2EsUV2gB7K2YLoNDdPPiyhefPnPU7uzYPvmCXalQ7-ft5F_4XBl-1axnWJPmQN5FE_1FKK5hfm4KTmd8sBH3a_rQQM2vKsK48oPomVf2A9116TiTUHq307bKhoeFHPj2gvornSGs=",
                "facilitated_booking_available": True,
                "pnr_count": 1,
                "has_airport_change": False,
                "technical_stops": 0,
                "throw_away_ticketing": False,
                "hidden_city_ticketing": False,
                "virtual_interlining": False,
                "local_arrival": "2023-02-11T22:05:00.000Z",
                "utc_arrival": "2023-02-11T16:35:00.000Z",
                "local_departure": "2023-02-11T20:00:00.000Z",
                "utc_departure": "2023-02-11T14:30:00.000Z"
            },
            {
                "id": "071104914bc90000ca1899a1_0",
                "flyFrom": "DEL",
                "flyTo": "BOM",
                "cityFrom": "New Delhi",
                "cityCodeFrom": "DEL",
                "cityTo": "Mumbai",
                "cityCodeTo": "BOM",
                "countryFrom": {
                    "code": "IN",
                    "name": "India"
                },
                "countryTo": {
                    "code": "IN",
                    "name": "India"
                },
                "nightsInDest": "None",
                "quality": 78.666595,
                "distance": 1139.47,
                "duration": {
                    "departure": 7500,
                    "return": 0,
                    "total": 7500
                },
                "price": 50,
                "conversion": {
                    "EUR": 50
                },
                "bags_price": {
                    "1": 0
                },
                "baglimit": {
                    "hand_height": 36,
                    "hand_length": 54,
                    "hand_weight": 7,
                    "hand_width": 18,
                    "hold_dimensions_sum": 158,
                    "hold_height": 52,
                    "hold_length": 78,
                    "hold_weight": 15,
                    "hold_width": 28
                },
                "availability": {
                    "seats": 2
                },
                "airlines": [
                    "SG"
                ],
                "route": [
                    {
                        "id": "071104914bc90000ca1899a1_0",
                        "combination_id": "071104914bc90000ca1899a1",
                        "flyFrom": "DEL",
                        "flyTo": "BOM",
                        "cityFrom": "New Delhi",
                        "cityCodeFrom": "DEL",
                        "cityTo": "Mumbai",
                        "cityCodeTo": "BOM",
                        "airline": "SG",
                        "flight_no": 8169,
                        "operating_carrier": "SG",
                        "operating_flight_no": "8169",
                        "fare_basis": "PSAV",
                        "fare_category": "M",
                        "fare_classes": "P",
                        "fare_family": "",
                        "return": 0,
                        "bags_recheck_required": False,
                        "vi_connection": False,
                        "guarantee": False,
                        "equipment": "None",
                        "vehicle_type": "aircraft",
                        "local_arrival": "2023-02-13T22:05:00.000Z",
                        "utc_arrival": "2023-02-13T16:35:00.000Z",
                        "local_departure": "2023-02-13T20:00:00.000Z",
                        "utc_departure": "2023-02-13T14:30:00.000Z"
                    }
                ],
                "booking_token": "E2otHrQwEUE4vJzVQ5rmprypc1-TEqtBWQjmRbY3nEBlDCdbDGzmFnQVQ2yCejq6AKZWT8KVeOwbZcw5I4KSNg7Mg8KZAge_z9pZ28aY2GfA-shytqg1RdlAAWSjQAg_DASZ1SlpjALI3fZgGO5lxd5tn6jUA4YSC4HPi8mw4GRiCYV4WrJcq_MA_lv5BSCl_i3L9R-RDhnsNcy00QW-eNBCwYQRfMLlvNi7RctH9y3dHo-E2ry5x_i2XWJGvjczAi5xGwcRjZh-avUrdapdavcbgZlEj-JKBZx0afEmIcJ9hv0giCmOx5tPxnqhPdtKymAzD8jGaYGZRRIEgKgl5-fCpJySyL3lAsJQ-6_ElbLGyXIXBQb1OxCDvsZCywQvshHC87XlgC1pStZqKm-a5WqgxZc1Je8NxjZs0Z6KFrY24JJnGyLQQ-9mER2rdR4uL0LMdbosQ0c6bN25RhFj7uieg25LdDBdOyeAcIm32gQSA9mffUst2R39xt2ZRTGRpBzfGHjD9oQPvaDrCAq4dhF_3vHvdwYsj0spNtznrLWciUwW7eTnICl-HnZ0vw4Ha",
                "deep_link": "https://www.kiwi.com/deep?affilid=apoorvflightsearch&currency=EUR&flightsId=071104914bc90000ca1899a1_0&from=DEL&lang=en&passengers=1&to=BOM&booking_token=EV5LkVstZ2bEbkahRplKaga9ZY7Oqh3DE5vZYa0OHa2Vt1Ge_Q1jmEliZ6lA7k9VLxHcsptzrt7hB3BrGjDD6mChgjzrJsdDOWcCQ6yb-QXVenI4z6aLkciSSrl7KfAdELA8K-zV75k0526Xwh0ox8iZKUoKA0To3E2TAKu8jcvBTPCNjGNmEJzLHSCMtMYsS7zi3f8ZTIN60iOHw_ibq8aC7PB3psKBGTdxFijGFmqFkpIhjlaiMjnGbdpWwa-M_1UcKrd42QWgvCPGm-y2TqlempgWTMwSdAOhgtwh0_8feOWJQJt9yYvxjgIR0E9oaw-nKpmDFFAV9WTcb88z_nGtdDE_EF4Ud8hYPVQ2dmYzUgL8VZrOToXlEjB6zSJs6AzGHqkvBHk9plRpX0hXL_RzUK_urwtdKtAHlCizPAv8=",
                "facilitated_booking_available": True,
                "pnr_count": 1,
                "has_airport_change": False,
                "technical_stops": 0,
                "throw_away_ticketing": False,
                "hidden_city_ticketing": False,
                "virtual_interlining": False,
                "local_arrival": "2023-02-13T22:05:00.000Z",
                "utc_arrival": "2023-02-13T16:35:00.000Z",
                "local_departure": "2023-02-13T20:00:00.000Z",
                "utc_departure": "2023-02-13T14:30:00.000Z"
            },
            {
                "id": "071104c24bc9000074c405f3_0",
                "flyFrom": "DEL",
                "flyTo": "LKO",
                "cityFrom": "New Delhi",
                "cityCodeFrom": "DEL",
                "cityTo": "Lucknow",
                "cityCodeTo": "LKO",
                "countryFrom": {
                    "code": "IN",
                    "name": "India"
                },
                "countryTo": {
                    "code": "IN",
                    "name": "India"
                },
                "nightsInDest": "None",
                "quality": 74.99994,
                "distance": 423.95,
                "duration": {
                    "departure": 5400,
                    "return": 0,
                    "total": 5400
                },
                "price": 51,
                "conversion": {
                    "EUR": 51
                },
                "bags_price": {
                    "1": 0
                },
                "baglimit": {
                    "hand_height": 38,
                    "hand_length": 57,
                    "hand_weight": 7,
                    "hand_width": 20,
                    "hold_dimensions_sum": 158,
                    "hold_height": 52,
                    "hold_length": 78,
                    "hold_weight": 15,
                    "hold_width": 28
                },
                "availability": {
                    "seats": 1
                },
                "airlines": [
                    "6E"
                ],
                "route": [
                    {
                        "id": "071104c24bc9000074c405f3_0",
                        "combination_id": "071104c24bc9000074c405f3",
                        "flyFrom": "DEL",
                        "flyTo": "LKO",
                        "cityFrom": "New Delhi",
                        "cityCodeFrom": "DEL",
                        "cityTo": "Lucknow",
                        "cityCodeTo": "LKO",
                        "airline": "6E",
                        "flight_no": 7148,
                        "operating_carrier": "6E",
                        "operating_flight_no": "7148",
                        "fare_basis": "O0IP",
                        "fare_category": "M",
                        "fare_classes": "X",
                        "fare_family": "",
                        "return": 0,
                        "bags_recheck_required": False,
                        "vi_connection": False,
                        "guarantee": False,
                        "equipment": "None",
                        "vehicle_type": "aircraft",
                        "local_arrival": "2023-02-13T16:25:00.000Z",
                        "utc_arrival": "2023-02-13T10:55:00.000Z",
                        "local_departure": "2023-02-13T14:55:00.000Z",
                        "utc_departure": "2023-02-13T09:25:00.000Z"
                    }
                ],
                "booking_token": "EZmdJxGon9Nf6FSGuKjpTNVyDGgooSxYr4n0QGB2EUCZXwLwa17Hdtya45ja6O28rMNB376fly_IhosC5vwcdXgOF0pH1xXBo1YRfjwa5rmGiYEzn-9rcRuaAwNvF-Uen9Kry4Mab0H6VRhfbbp-37Rh7tNiPLC8jzyLxj5sdDchEMNzelTKcZRJM0TDl539mVd_hajreuO-C0nJJ8v7liZPfZjtOBkJyFZjdvkk_SFTtYcU7s-OjCtiYo1VquiJuV8b1wWTlXmb80h7gzxZqPGAUUjZ5ICWiHOePaSoVhHXWB8i_d_YEdHHMNaVZ81pgsLahdGMHHEIqXQTd3mAdY2hkWwF96jpwcxYpLq9T47XyGP9zZI89x_8dVr4y5gwAr78E-mLTY7RmjF5PaDCXWiQi1V3FtzKGSDUF_qZCpb3QJynD3iABoLPehAzJ91ReIVpZNPMe9F93TpGpkTh8wTlCBtr76B91mghaRYeslo2mluYsrc3eFAO4bSWtP-Ic2vgy3rnQ9Enh22se7hIjycmWinI0-uS5opySTslYeIM=",
                "deep_link": "https://www.kiwi.com/deep?affilid=apoorvflightsearch&currency=EUR&flightsId=071104c24bc9000074c405f3_0&from=DEL&lang=en&passengers=1&to=LKO&booking_token=ExcjoIwH5VaPnUopcB8Hp8VH0IOr-wlv3fVk16ZMhIrPcDVd4dczBhPGBELL_HWeQNVKxaqVUG4Ju09HCwzSde3w7nrDuTvtNYfr4H60IHqCS-Mvh3T49yqS_SzlQvZgkEmy77XkjIwFlc6Vh5EZmUVu6j12clKVbkoAICFljyAqOdSJGaJS5mGjqPfUeY64lCxtt3xdvhTGltNA46MU3C6plcDwwR7GBB4bGkZdPcZgvPgfRByahvEWIyby0XEM6LYIRepwFeSIxF3WJWH37ipEXD4bP3ZwYXlZ_lwdcX20DEPBg1oUlQRrk9XKLqh5tHsES-uqILNdqi5LGi4mXpVsTeSq7396TqxFCREQOTVI0kZGTHWGvnjIzhJvUNrUQcZMwRUYgXf-BMKLU4xEeFA==",
                "facilitated_booking_available": True,
                "pnr_count": 1,
                "has_airport_change": False,
                "technical_stops": 0,
                "throw_away_ticketing": False,
                "hidden_city_ticketing": False,
                "virtual_interlining": False,
                "local_arrival": "2023-02-13T16:25:00.000Z",
                "utc_arrival": "2023-02-13T10:55:00.000Z",
                "local_departure": "2023-02-13T14:55:00.000Z",
                "utc_departure": "2023-02-13T09:25:00.000Z"
            },
            {
                "id": "071154a84bc700006157a4bb_0",
                "flyFrom": "DEL",
                "flyTo": "KBK",
                "cityFrom": "New Delhi",
                "cityCodeFrom": "DEL",
                "cityTo": "Kushinagar",
                "cityCodeTo": "",
                "countryFrom": {
                    "code": "IN",
                    "name": "India"
                },
                "countryTo": {
                    "code": "IN",
                    "name": "India"
                },
                "nightsInDest": "None",
                "quality": 75.666605,
                "distance": 699.93,
                "duration": {
                    "departure": 5700,
                    "return": 0,
                    "total": 5700
                },
                "price": 51,
                "conversion": {
                    "EUR": 51
                },
                "bags_price": {
                    "1": 0
                },
                "baglimit": {
                    "hand_height": 36,
                    "hand_length": 54,
                    "hand_weight": 7,
                    "hand_width": 18,
                    "hold_dimensions_sum": 158,
                    "hold_height": 52,
                    "hold_length": 78,
                    "hold_weight": 15,
                    "hold_width": 28
                },
                "availability": {
                    "seats": 1
                },
                "airlines": [
                    "SG"
                ],
                "route": [
                    {
                        "id": "071154a84bc700006157a4bb_0",
                        "combination_id": "071154a84bc700006157a4bb",
                        "flyFrom": "DEL",
                        "flyTo": "KBK",
                        "cityFrom": "New Delhi",
                        "cityCodeFrom": "DEL",
                        "cityTo": "Kushinagar",
                        "cityCodeTo": "None",
                        "airline": "SG",
                        "flight_no": 2987,
                        "operating_carrier": "SG",
                        "operating_flight_no": "2987",
                        "fare_basis": "USAV",
                        "fare_category": "M",
                        "fare_classes": "U",
                        "fare_family": "",
                        "return": 0,
                        "bags_recheck_required": False,
                        "vi_connection": False,
                        "guarantee": False,
                        "equipment": "None",
                        "vehicle_type": "aircraft",
                        "local_arrival": "2023-02-11T13:35:00.000Z",
                        "utc_arrival": "2023-02-11T08:05:00.000Z",
                        "local_departure": "2023-02-11T12:00:00.000Z",
                        "utc_departure": "2023-02-11T06:30:00.000Z"
                    }
                ],
                "booking_token": "EXHwwerXVYCSVmve-cYPbH4lys9vO41vnt5kaHb3sTcGHnOdJEJIhZFwS5qf4x0bjbixeFquV-VlF1uZUi76dwnyCzQTe-B9jHTETZ06Np7njT0zEvQi8tZ-4fxO26qxRZEZJ3Whlxb_YBViHOfCDnsP7nnw945ZyMuDlptZA-_hgcff5E5VjTzcDuGcZv78DbsWf559GYbEa1xaVAD1ykgVCx-8QXZy17aOCrvHbgTrl1IjuCNTnlDABAlWkiDDBQRadHdSG42VY4IAkU7nuRl6voIRpW1JVUcJsNI3vwPHMpqDSqHS4NiHV6LyHI220pf1GVYJRTi0rnzHvPDlLmkoRlNt4NmTQoxIdPOHBwIq5lFRiEKpgzKcz3VGgz35zOO_M94U40440pJAcMe9iRj54Rf_KKGgz-bAb0qnMuRhwNru6EmfgxabtA-O5x1FYAc8ZxsBk01zOZoaVYdI-ez88fGZWPvEY1Pce8Gj8ZPXDWdqBBwU5yv-zq0coVRdZuP6wuJ2YNlQq8EtKIXbSU911Y-T9IBD6HZzfTDXDnto=",
                "deep_link": "https://www.kiwi.com/deep?affilid=apoorvflightsearch&currency=EUR&flightsId=071154a84bc700006157a4bb_0&from=DEL&lang=en&passengers=1&to=KBK&booking_token=EK0ogKnnofhvTesEf2Ju7EWe2ZWAMbns4rewwe6eN9pogPFhTbPt3uuG4dcIa4pFeNBgCzkIjr_9jLF7nBQsT6w27H1jl9gYbkJ2GHxhuxAGdI_xFbp9zIwQpU9R5vhrgJu-MrStI9hUoFnNmq_WwR0sHdqtMNrGjYwEtxrSOSMK9mvnbs9tHNmvnjS-ZPqJ3HcvaDgZqMq0BREtRYMlcTGubmUyqp4tebw61COHtW52aNevqI3_kZ4NkO1eW8NCrBeqYkqBNRnhSXbQk2bKJeso6Zxm8yZX1O2zV80r1YNX7vY5bU0sV0sVZnPc2l3NlYekNkGNRItaBTUKVH3AADNwab42Vif5r1kYOb3mpuasZfXrh6v8JXb6vJUFTv8gmDW5PN_MmDeTlU1D6lyZ2tFpWCQC8K4ynYjyS6rnJK4E=",
                "facilitated_booking_available": True,
                "pnr_count": 1,
                "has_airport_change": False,
                "technical_stops": 0,
                "throw_away_ticketing": False,
                "hidden_city_ticketing": False,
                "virtual_interlining": False,
                "local_arrival": "2023-02-11T13:35:00.000Z",
                "utc_arrival": "2023-02-11T08:05:00.000Z",
                "local_departure": "2023-02-11T12:00:00.000Z",
                "utc_departure": "2023-02-11T06:30:00.000Z"
            },
            {
                "id": "071104914bc90000754d2f07_0",
                "flyFrom": "DEL",
                "flyTo": "BOM",
                "cityFrom": "New Delhi",
                "cityCodeFrom": "DEL",
                "cityTo": "Mumbai",
                "cityCodeTo": "BOM",
                "countryFrom": {
                    "code": "IN",
                    "name": "India"
                },
                "countryTo": {
                    "code": "IN",
                    "name": "India"
                },
                "nightsInDest": "None",
                "quality": 79.666595,
                "distance": 1139.47,
                "duration": {
                    "departure": 7500,
                    "return": 0,
                    "total": 7500
                },
                "price": 51,
                "conversion": {
                    "EUR": 51
                },
                "bags_price": {
                    "1": 0
                },
                "baglimit": {
                    "hand_height": 35,
                    "hand_length": 55,
                    "hand_weight": 7,
                    "hand_width": 25,
                    "hold_dimensions_sum": 158,
                    "hold_height": 52,
                    "hold_length": 78,
                    "hold_weight": 15,
                    "hold_width": 28
                },
                "availability": {
                    "seats": 2
                },
                "airlines": [
                    "G8"
                ],
                "route": [
                    {
                        "id": "071104914bc90000754d2f07_0",
                        "combination_id": "071104914bc90000754d2f07",
                        "flyFrom": "DEL",
                        "flyTo": "BOM",
                        "cityFrom": "New Delhi",
                        "cityCodeFrom": "DEL",
                        "cityTo": "Mumbai",
                        "cityCodeTo": "BOM",
                        "airline": "G8",
                        "flight_no": 346,
                        "operating_carrier": "G8",
                        "operating_flight_no": "346",
                        "fare_basis": "MO9RBINE",
                        "fare_category": "M",
                        "fare_classes": "M",
                        "fare_family": "",
                        "return": 0,
                        "bags_recheck_required": False,
                        "vi_connection": False,
                        "guarantee": False,
                        "equipment": "None",
                        "vehicle_type": "aircraft",
                        "local_arrival": "2023-02-13T22:05:00.000Z",
                        "utc_arrival": "2023-02-13T16:35:00.000Z",
                        "local_departure": "2023-02-13T20:00:00.000Z",
                        "utc_departure": "2023-02-13T14:30:00.000Z"
                    }
                ],
                "booking_token": "EEzipuaEeXsgelDIhCQ3LEEtuSeVAs5Q5QsHxdctSg18n4ocNnGT9Z_k5yW-4mI-WqIhcmCLqbEt4opkpGQ7PVBCBpn51fhTU-s3TPmqb_m-MsveK0KlPykcYkkbqy_-u0_1WL5wRK-eDRM42Gd6Hcos9-J2CF0aCDVzTqsBewtV-FdD0Bx5H5sLITC4XX2HB6h0v_K5hGRS9NaI57Px6iC2-DIqnlg5RaY3LGaDZjQQcRVOMrwlqQi7MfWzemm94w6jcttt-7twlOC1F-_ScOtNYO6XzLLLXQufnork1LcFgNUto4a0j1r3TfJPFEc3Pp2S7bYm0S05yqS6BkLVhXqnsjCROhV2dtXX4Z5Vz64kh1gHXr075eSKHj-8Ww6iToIPn-kr-wZ1irDONvMQccapB9ZJywtN7Adh9-HDKQqHSfsKNmkzEeBHX6G4gyoKjokXH2nlTg_ac1bL_gd4eBF-cAAzGJ7Nr43279XWyALUpZ69ZXAZQfdWWCrM-MmW8VO6nd4WHuLxz41dYK-ACTgr2Hu8-cSJ0TZP9lEVxyCjesIH61t7BThc7az-_w8gn",
                "deep_link": "https://www.kiwi.com/deep?affilid=apoorvflightsearch&currency=EUR&flightsId=071104914bc90000754d2f07_0&from=DEL&lang=en&passengers=1&to=BOM&booking_token=E8hVJtC3pv0z7hKooJUIqj4ygeiugY3ljnUBfcy2Grve5iAWN9QHe5EWi3Pq5L7VxL9ysI5iMDuH7Q-F1zxhPLxALx07guY39aOu6m2mws6G8GVMTZiKORmNpUhOfGj_J2_QjKigx_NJmUfcO9-GjAPdOoq7foFAlQefwSk1x2iGPIk5C04Ubn4-ZaBOMANREtVCTyPkFdI8QhPE4PzKORa02LaOSvad55I_zthXn9OMQFw2ntX2iZ1KlFEQeuYjQrsCd7EpYu924W4L08SuuvNcf1jQcSG97O_UfLbhYO6x659pnzxfq8c6_-py4PA6tS8m1wvhWc5yzydlHtr0lDzgWyzOveNzLDSQanzcuOPRKTmrBcZTSJrXNx5ET4iVVCngrc9_6EMENfLd2Cm9oM7Pa6KmAwOVVpXNS3rXjlWHLOuu7wQMIioUNt6-ZShP7",
                "facilitated_booking_available": True,
                "pnr_count": 1,
                "has_airport_change": False,
                "technical_stops": 0,
                "throw_away_ticketing": False,
                "hidden_city_ticketing": False,
                "virtual_interlining": False,
                "local_arrival": "2023-02-13T22:05:00.000Z",
                "utc_arrival": "2023-02-13T16:35:00.000Z",
                "local_departure": "2023-02-13T20:00:00.000Z",
                "utc_departure": "2023-02-13T14:30:00.000Z"
            },
            {
                "id": "071100174bc9000048061495_0",
                "flyFrom": "DEL",
                "flyTo": "IXB",
                "cityFrom": "New Delhi",
                "cityCodeFrom": "DEL",
                "cityTo": "Bagdogra",
                "cityCodeTo": "IXB",
                "countryFrom": {
                    "code": "IN",
                    "name": "India"
                },
                "countryTo": {
                    "code": "IN",
                    "name": "India"
                },
                "nightsInDest": "None",
                "quality": 80.33326,
                "distance": 1126.41,
                "duration": {
                    "departure": 7800,
                    "return": 0,
                    "total": 7800
                },
                "price": 51,
                "conversion": {
                    "EUR": 51
                },
                "bags_price": {
                    "1": 0
                },
                "baglimit": {
                    "hand_height": 36,
                    "hand_length": 54,
                    "hand_weight": 7,
                    "hand_width": 18,
                    "hold_dimensions_sum": 158,
                    "hold_height": 52,
                    "hold_length": 78,
                    "hold_weight": 15,
                    "hold_width": 28
                },
                "availability": {
                    "seats": 1
                },
                "airlines": [
                    "SG"
                ],
                "route": [
                    {
                        "id": "071100174bc9000048061495_0",
                        "combination_id": "071100174bc9000048061495",
                        "flyFrom": "DEL",
                        "flyTo": "IXB",
                        "cityFrom": "New Delhi",
                        "cityCodeFrom": "DEL",
                        "cityTo": "Bagdogra",
                        "cityCodeTo": "IXB",
                        "airline": "SG",
                        "flight_no": 187,
                        "operating_carrier": "SG",
                        "operating_flight_no": "187",
                        "fare_basis": "VSWB",
                        "fare_category": "M",
                        "fare_classes": "V",
                        "fare_family": "",
                        "return": 0,
                        "bags_recheck_required": False,
                        "vi_connection": False,
                        "guarantee": False,
                        "equipment": "None",
                        "vehicle_type": "aircraft",
                        "local_arrival": "2023-02-13T15:10:00.000Z",
                        "utc_arrival": "2023-02-13T09:40:00.000Z",
                        "local_departure": "2023-02-13T13:00:00.000Z",
                        "utc_departure": "2023-02-13T07:30:00.000Z"
                    }
                ],
                "booking_token": "EcHy3ETUm6-GQknvIr42CVBOd3mfIvtQst3MWWzEAurYqBr0mTBCtN2Cvgbu0DYqa-EGKkE8N_9Tv_OL42kOFX3k68lvMbvZ-UA9ts7ebSDZ0hMWUU6L2jgwtGSrH7IatIA1VppOs4irmZnlnlSx1f_IvjaBSGYNCWmiAOK8J8pEvJUU9ir_8VA2w_3raE9DyhKmJ1FWDJnWsDNqE0n1FJRq8fEErnlREVR6Of5YphDOui5bSmTP7YK15oTcGSqyAM73XEODy4DDTHQtkRVIJZvpXBxd8nZRzHjeKAqJcb3YgCWt9cX5bG54EUsCwemG2zJjHOGAI9_Na8oJrbTtc5XSQux7HdfP7VEuBK9guC9kBPevAqr8G_GOz0GSmZiIX-5BxjPSnv-_Ek0WlCw7KhbgMcWfhIDanHMXg4hX6e2Sg2O6b6GLoYvlm5U7g3NFeCudu2OaToyFxFyZ0VA9aZB_9sO5TEnNs_5yhL7nUT3YkZ389_BI4M5ntPhJEP_z7fNzk0jb_yCeIlFrZAqY9QfL9-rq0hxXd5EWez7OUQg8=",
                "deep_link": "https://www.kiwi.com/deep?affilid=apoorvflightsearch&currency=EUR&flightsId=071100174bc9000048061495_0&from=DEL&lang=en&passengers=1&to=IXB&booking_token=EXbAp45w28755PUHIzQVMJPM_8uOJ1zMu4RtQkX1QFnozYIzL8QgD9ILVwkcXH8SwOHceVS51TSJ5lLaMNyjjwN2kbWvmi5A1HIZCGFtZ1KUsK_g98oFwAkfcMJU0gGTFeCFO45DELozp5HSS9o1G3A8WTH_gxg1qaUgQ5eYUmryFDc-cJtWUTjMCzhOGHklQ09Gw4AKM0T3uglv60XydHIhSOQWM6gGjwHp4c03zhXbkWJDrLE9XnB2wglWKQWBjKPqilu5yqlp-510048S2Pes5ZJCt2wkxlAiAcSaUt6wlZL1s-erPJ3YdQOOjCG1lJv_Ns3erQeOIb2GYFea5OuYkKUfOWrqvSSgbdq-SpAuX657MqzKd4YJHgE2WxMswaAe1vwO4fbVgAC_xTxYIVEE2FzJ4xB3uBXYdsHYB7RI=",
                "facilitated_booking_available": True,
                "pnr_count": 1,
                "has_airport_change": False,
                "technical_stops": 0,
                "throw_away_ticketing": False,
                "hidden_city_ticketing": False,
                "virtual_interlining": False,
                "local_arrival": "2023-02-13T15:10:00.000Z",
                "utc_arrival": "2023-02-13T09:40:00.000Z",
                "local_departure": "2023-02-13T13:00:00.000Z",
                "utc_departure": "2023-02-13T07:30:00.000Z"
            },
            {
                "id": "071104914bc60000fc4e83aa_0",
                "flyFrom": "DEL",
                "flyTo": "BOM",
                "cityFrom": "New Delhi",
                "cityCodeFrom": "DEL",
                "cityTo": "Mumbai",
                "cityCodeTo": "BOM",
                "countryFrom": {
                    "code": "IN",
                    "name": "India"
                },
                "countryTo": {
                    "code": "IN",
                    "name": "India"
                },
                "nightsInDest": "None",
                "quality": 80.33326,
                "distance": 1139.47,
                "duration": {
                    "departure": 7800,
                    "return": 0,
                    "total": 7800
                },
                "price": 51,
                "conversion": {
                    "EUR": 51
                },
                "bags_price": {
                    "1": 0
                },
                "baglimit": {
                    "hand_height": 35,
                    "hand_length": 55,
                    "hand_weight": 7,
                    "hand_width": 25,
                    "hold_dimensions_sum": 158,
                    "hold_height": 52,
                    "hold_length": 78,
                    "hold_weight": 15,
                    "hold_width": 28
                },
                "availability": {
                    "seats": 4
                },
                "airlines": [
                    "G8"
                ],
                "route": [
                    {
                        "id": "071104914bc60000fc4e83aa_0",
                        "combination_id": "071104914bc60000fc4e83aa",
                        "flyFrom": "DEL",
                        "flyTo": "BOM",
                        "cityFrom": "New Delhi",
                        "cityCodeFrom": "DEL",
                        "cityTo": "Mumbai",
                        "cityCodeTo": "BOM",
                        "airline": "G8",
                        "flight_no": 334,
                        "operating_carrier": "G8",
                        "operating_flight_no": "334",
                        "fare_basis": "MO9RBINE",
                        "fare_category": "M",
                        "fare_classes": "M",
                        "fare_family": "",
                        "return": 0,
                        "bags_recheck_required": False,
                        "vi_connection": False,
                        "guarantee": False,
                        "equipment": "None",
                        "vehicle_type": "aircraft",
                        "local_arrival": "2023-02-10T09:30:00.000Z",
                        "utc_arrival": "2023-02-10T04:00:00.000Z",
                        "local_departure": "2023-02-10T07:20:00.000Z",
                        "utc_departure": "2023-02-10T01:50:00.000Z"
                    }
                ],
                "booking_token": "ETfQX5Z4FkDlIEDWDxkp7aInu5bR1LMsU3o0HJE3bdoX1awAluQZcX_JhXhpYBueVHFF8YIhBNMnNIyMor1noh3hnSbo9jkJ5i6aFasNmGITmRWdlYBsPUh7UyElg-5sdJ09zDP1o6JyBHcLHnbjKJl4en66pusmdbjiYdh-DZp6EOenJoEHCOCDdZXo-8vnx_9iU_MXmSk-eVhHw0-FoyeQv9S6ZvgTVdb3KfJ1p9Szyn36-4JFCDD5RMmfE1bpKde6PutbkurUzAZuuMcSrCpJxLCw4T3HUW2RDKCLmT27PqeFyP4ZSOSiC4R1hg8ik3SBUWUi7yXIG1j4tkRI_7kv02y5CaA8YhwHR-xT8d5VzD0emkbkKzavNCSaHnA0t81eNCgb5PFPVcGIlx94HR3NAdzAysuOL5NwT8_FbTptvhBbOICPgoefUfFXAM8rfVYZN8hNQo1o5uL00S0h3gDjHPRz5NdHt2CCATmcWW9OC5M13ySrcMHloCBFj7tLTdqBaT1l7T42HYtlwTUylJRdBmlufNdKR7fZr-lqLBxm5DJiXeGYTAiiv7bN6QnKN",
                "deep_link": "https://www.kiwi.com/deep?affilid=apoorvflightsearch&currency=EUR&flightsId=071104914bc60000fc4e83aa_0&from=DEL&lang=en&passengers=1&to=BOM&booking_token=Emc05u8dWR8lOtvmSifOfTK-jf0hAlQ7xD2pGKn6uIELntcdBZwOgXmH7qe0KxYgLlwLAggLE3VVBrCUXW2FtGzRUEEtDYvmjHnDKMe0FnQmJc8987lcbdi5KJ4HBrHEKIDV7zDl0FPzj3qVcmwhkVdYhH0n0Lt94B2LVwo95bvTE2O6O0pWC_6eJeZ_eVNoC35VjUCx7ofeum05gYdaAY9B4Db2n25-ec_cjYjHFuPw8UH5q5xbH7ps6fbpNjRJRPH9BLtWFlEVN2NuyMM56i4dCmJOfqtDoX9qiIAU-qcRIyMIc3hqQxbwjzLD0YlSBEZaWMPNcuYhguXDt969CC8i7LmLz1XRaRESAn8a13H3rM1aJEOAS6eslPFWKunQM7CvIiFQXuxulVSyfFcX31pncMq8lh_Pt6JhI7YLz9Ps=",
                "facilitated_booking_available": True,
                "pnr_count": 1,
                "has_airport_change": False,
                "technical_stops": 0,
                "throw_away_ticketing": False,
                "hidden_city_ticketing": False,
                "virtual_interlining": False,
                "local_arrival": "2023-02-10T09:30:00.000Z",
                "utc_arrival": "2023-02-10T04:00:00.000Z",
                "local_departure": "2023-02-10T07:20:00.000Z",
                "utc_departure": "2023-02-10T01:50:00.000Z"
            },
            {
                "id": "071104914bc7000036052b59_0",
                "flyFrom": "DEL",
                "flyTo": "BOM",
                "cityFrom": "New Delhi",
                "cityCodeFrom": "DEL",
                "cityTo": "Mumbai",
                "cityCodeTo": "BOM",
                "countryFrom": {
                    "code": "IN",
                    "name": "India"
                },
                "countryTo": {
                    "code": "IN",
                    "name": "India"
                },
                "nightsInDest": "None",
                "quality": 80.33326,
                "distance": 1139.47,
                "duration": {
                    "departure": 7800,
                    "return": 0,
                    "total": 7800
                },
                "price": 51,
                "conversion": {
                    "EUR": 51
                },
                "bags_price": {
                    "1": 0
                },
                "baglimit": {
                    "hand_height": 35,
                    "hand_length": 55,
                    "hand_weight": 7,
                    "hand_width": 25,
                    "hold_dimensions_sum": 158,
                    "hold_height": 52,
                    "hold_length": 78,
                    "hold_weight": 15,
                    "hold_width": 28
                },
                "availability": {
                    "seats": 1
                },
                "airlines": [
                    "G8"
                ],
                "route": [
                    {
                        "id": "071104914bc7000036052b59_0",
                        "combination_id": "071104914bc7000036052b59",
                        "flyFrom": "DEL",
                        "flyTo": "BOM",
                        "cityFrom": "New Delhi",
                        "cityCodeFrom": "DEL",
                        "cityTo": "Mumbai",
                        "cityCodeTo": "BOM",
                        "airline": "G8",
                        "flight_no": 334,
                        "operating_carrier": "G8",
                        "operating_flight_no": "334",
                        "fare_basis": "MO9RBINE",
                        "fare_category": "M",
                        "fare_classes": "M",
                        "fare_family": "",
                        "return": 0,
                        "bags_recheck_required": False,
                        "vi_connection": False,
                        "guarantee": False,
                        "equipment": "None",
                        "vehicle_type": "aircraft",
                        "local_arrival": "2023-02-11T09:30:00.000Z",
                        "utc_arrival": "2023-02-11T04:00:00.000Z",
                        "local_departure": "2023-02-11T07:20:00.000Z",
                        "utc_departure": "2023-02-11T01:50:00.000Z"
                    }
                ],
                "booking_token": "EHmgd93QAbWQhIutm5Ak2MW89K8f4ok_ikdO8PJHDECFqysjIQ65E69iTpWr68UaKtBLlM4tYQEEH6UYqvZpOe_RlzbCGCQ-mAZtZZW2yZyfH8nIdRjUJFRYBOcwiHabTKKUTJ0aon5D1MuygWPjmqmqKm-LdHJCSeHkzUqQ5Y7dFbEHqDW6x58OAY0IvV-hnfpvT98cA-j5xUib4eGcI2NnhL91uTj7v-Q1PntmwQOcUAq52FBlcpaM6Lzagd1oqTPnKnYWq6RlxKv5o0QrJOFjslf_I27ZkDO0ye2kQZpzDxqBuo2HD40TCB4rP56gK3AsVTjDSX-Ez4Ulp-uRlPkGwh9FZs8BdldOM8LLoRQ3pTR4HDQohlnK1Tiq62meG_QVbfm5SLoxg5uJkdf_u9jliLyuSDm2FX05h_UMcskOpGVpSp0XWrRveQV15FEFwh3ZygE7ag-OdmzNEtSDQ_NFFPCFrE6SzWebk2pw37NxMP4HEVdZK8f4AXUbmBFPvtl5S9K26RrG_oUf2qFuVMzr-75xpJ1Ow1aaTcCkRhPfVFT2aIaUT6ZWImuUG1Ahx_V3XVKOftpOaeiElWpTPCDlD7ON4KBWNSuAkAWYUyoQ=",
                "deep_link": "https://www.kiwi.com/deep?affilid=apoorvflightsearch&currency=EUR&flightsId=071104914bc7000036052b59_0&from=DEL&lang=en&passengers=1&to=BOM&booking_token=E-dtCo9ykHEIBdDZHMxCt6cVpc-agFdKerS-Izwz2BSq-e6qsjB-5gS7wXzySV7dunajdu09I0m9U2M2HVoa55hFhR_3WQnKiC6HZPi4Ha5Oav18KeY3Ja2XkseHcZFnGxOvLKFznlhYHbPG56IloSC5o3iuRMoWgl97IcVGSsN1JkkEnVoAC-qamFiJc-QIMSY28FWI22xrJOsQhIbnec43L_FA84UBPSKbU980zgF8MzFmzAUe1CQErmiElIpKz7O4VcCSbRB6jcSjdE1MMM6uP3BqbhcpQtPn4Ku9AqSkSCllsxF4f3_rryHYQ3dURiKlI_cUHJKsYs3ECu_NX5Q9SYkLONmg2kzPbk1aRCMhEtzEqEz2hF-Dc0XFHOuhfHJJt9CiYGTvHiaDJwkKEOP52ekUbdUNWTxrWmNfkamAihf7cjfjzgoAaG1jF1vGFvhf5pA-G4pFfUisSrJjJOw==",
                "facilitated_booking_available": True,
                "pnr_count": 1,
                "has_airport_change": False,
                "technical_stops": 0,
                "throw_away_ticketing": False,
                "hidden_city_ticketing": False,
                "virtual_interlining": False,
                "local_arrival": "2023-02-11T09:30:00.000Z",
                "utc_arrival": "2023-02-11T04:00:00.000Z",
                "local_departure": "2023-02-11T07:20:00.000Z",
                "utc_departure": "2023-02-11T01:50:00.000Z"
            },
            {
                "id": "071104914bc700004900dd1f_0",
                "flyFrom": "DEL",
                "flyTo": "BOM",
                "cityFrom": "New Delhi",
                "cityCodeFrom": "DEL",
                "cityTo": "Mumbai",
                "cityCodeTo": "BOM",
                "countryFrom": {
                    "code": "IN",
                    "name": "India"
                },
                "countryTo": {
                    "code": "IN",
                    "name": "India"
                },
                "nightsInDest": "None",
                "quality": 80.33326,
                "distance": 1139.47,
                "duration": {
                    "departure": 7800,
                    "return": 0,
                    "total": 7800
                },
                "price": 51,
                "conversion": {
                    "EUR": 51
                },
                "bags_price": {
                    "1": 0
                },
                "baglimit": {
                    "hand_height": 35,
                    "hand_length": 55,
                    "hand_weight": 7,
                    "hand_width": 25,
                    "hold_dimensions_sum": 158,
                    "hold_height": 52,
                    "hold_length": 78,
                    "hold_weight": 15,
                    "hold_width": 28
                },
                "availability": {
                    "seats": 2
                },
                "airlines": [
                    "G8"
                ],
                "route": [
                    {
                        "id": "071104914bc700004900dd1f_0",
                        "combination_id": "071104914bc700004900dd1f",
                        "flyFrom": "DEL",
                        "flyTo": "BOM",
                        "cityFrom": "New Delhi",
                        "cityCodeFrom": "DEL",
                        "cityTo": "Mumbai",
                        "cityCodeTo": "BOM",
                        "airline": "G8",
                        "flight_no": 2501,
                        "operating_carrier": "G8",
                        "operating_flight_no": "2501",
                        "fare_basis": "MO9RBINE",
                        "fare_category": "M",
                        "fare_classes": "M",
                        "fare_family": "",
                        "return": 0,
                        "bags_recheck_required": False,
                        "vi_connection": False,
                        "guarantee": False,
                        "equipment": "None",
                        "vehicle_type": "aircraft",
                        "local_arrival": "2023-02-11T04:50:00.000Z",
                        "utc_arrival": "2023-02-10T23:20:00.000Z",
                        "local_departure": "2023-02-11T02:40:00.000Z",
                        "utc_departure": "2023-02-10T21:10:00.000Z"
                    }
                ],
                "booking_token": "EzpOyE0S3W-_k5-KJEwrP3ZvaejYhSgrwxfHY7TL2Q0t-y0iKnI29KXDJqeZzIIfMSChS1s7nHlK_1F5U1xgh8Ak4rz8VzsDBrK1_YQLJhXxgPYNpF9l-NfWs7cdBQQkWwif22C9EXZulk2JNCZV89Z4bltXGuiYhYAXDR1CrfVELAX8gtpGq9ABN3GS7mE6TZW04L1eLbCUEptHjGWBdAwvzqQ83xXg0qxhxusxxDmGWC381CJqAMQv0nt9BakhlcvhxQJNqQQvLk8s5FYvrmtLRiFNy8MdZRyanUevlMmYdSXIt1NSD2dv_QB3B2bJ36OcnbwEwkKeEKP8JJ01y2nofO1UrHN3UFSA4rOv_R18s46fkuzEwT-jcOGSxIqQEVQgDb7VtvIS6nPnsjS6Lwk2RgYmYJIMsUrSoh7rxVwEc36UIYUr6N3bxwZ0BhJzPQZYIksBEjGu19p_sNrLKUPPPq0YJ6obYx21ME7ugQLDENycv6AWUF1aGrCpBEKbTUGhjiy4maP2LCaoDB_qdiDwrmn-oIX1tj5pr1iZzTeYByiS3tho9-4GKaAEWLulq",
                "deep_link": "https://www.kiwi.com/deep?affilid=apoorvflightsearch&currency=EUR&flightsId=071104914bc700004900dd1f_0&from=DEL&lang=en&passengers=1&to=BOM&booking_token=EhdZkyqh1aLeWPCmb0ajzIJPffyxWpprgCZv2lrBlFvMlWHk7vcmtYhaUXG64VsydfP6hyfqEHw2gQEZ_24r4BPCZC_SEaFMAD7Sc_WrhwTN1KOlshFl9gnDwFYmAWnrH9k_V2jBlqOXSKzNYhiriXX-ERAVPUP4Iy8O2yd6I-iamUzSUpXaLPYYtY_UMeLrnLw5lgip7TYz2NSBPScVqIN46tdpy1-2jiVBY5aWWJg8dvbaiXnUT_xNddz-CJoEPz32p3sEtUG7xdKT0idE1ucMio05rCYbma9DeO9F-D4VIcqv6PjXdLKuJN10KL9AaifzZnKXFz1QgeLDPz1uTATMO-r0I4Os_TJnD-J4yNyHO1nJgomfK11IK5-sVwX1I8onA9kAxrO-xgIHVo2hJKmQK6n1T4wywRAFAS_o_Gfk=",
                "facilitated_booking_available": True,
                "pnr_count": 1,
                "has_airport_change": False,
                "technical_stops": 0,
                "throw_away_ticketing": False,
                "hidden_city_ticketing": False,
                "virtual_interlining": False,
                "local_arrival": "2023-02-11T04:50:00.000Z",
                "utc_arrival": "2023-02-10T23:20:00.000Z",
                "local_departure": "2023-02-11T02:40:00.000Z",
                "utc_departure": "2023-02-10T21:10:00.000Z"
            },
            {
                "id": "071104914bc8000098ae5ca3_0",
                "flyFrom": "DEL",
                "flyTo": "BOM",
                "cityFrom": "New Delhi",
                "cityCodeFrom": "DEL",
                "cityTo": "Mumbai",
                "cityCodeTo": "BOM",
                "countryFrom": {
                    "code": "IN",
                    "name": "India"
                },
                "countryTo": {
                    "code": "IN",
                    "name": "India"
                },
                "nightsInDest": "None",
                "quality": 80.33326,
                "distance": 1139.47,
                "duration": {
                    "departure": 7800,
                    "return": 0,
                    "total": 7800
                },
                "price": 51,
                "conversion": {
                    "EUR": 51
                },
                "bags_price": {
                    "1": 0
                },
                "baglimit": {
                    "hand_height": 35,
                    "hand_length": 55,
                    "hand_weight": 7,
                    "hand_width": 25,
                    "hold_dimensions_sum": 158,
                    "hold_height": 52,
                    "hold_length": 78,
                    "hold_weight": 15,
                    "hold_width": 28
                },
                "availability": {
                    "seats": 2
                },
                "airlines": [
                    "G8"
                ],
                "route": [
                    {
                        "id": "071104914bc8000098ae5ca3_0",
                        "combination_id": "071104914bc8000098ae5ca3",
                        "flyFrom": "DEL",
                        "flyTo": "BOM",
                        "cityFrom": "New Delhi",
                        "cityCodeFrom": "DEL",
                        "cityTo": "Mumbai",
                        "cityCodeTo": "BOM",
                        "airline": "G8",
                        "flight_no": 2501,
                        "operating_carrier": "G8",
                        "operating_flight_no": "2501",
                        "fare_basis": "MO9RBINE",
                        "fare_category": "M",
                        "fare_classes": "M",
                        "fare_family": "",
                        "return": 0,
                        "bags_recheck_required": False,
                        "vi_connection": False,
                        "guarantee": False,
                        "equipment": "None",
                        "vehicle_type": "aircraft",
                        "local_arrival": "2023-02-12T04:50:00.000Z",
                        "utc_arrival": "2023-02-11T23:20:00.000Z",
                        "local_departure": "2023-02-12T02:40:00.000Z",
                        "utc_departure": "2023-02-11T21:10:00.000Z"
                    }
                ],
                "booking_token": "E-nciw1xdnpWAcqFEyHq2AwV5AHAbRmAHFeQrSxpRr7E-AJtOHs8pMEBc-UMJPopBQZlrmCvfPOJrOY0UMap4ZP-EQkogQjIjh7UhAug4djlADvy8_suQB4eimhUgL_u7vD9RW5QnLYtq1FJbLKhs50QA_B7lvISjFLOYabpo7qN-yIyzM1msp9lSyHbNF81bAmyum8OXrJBvr6F1F0ICrHPzH2ARInBXMyEVVKBbsZX0gSshb87fyyRvve6-H5sCeFFj806evK1KyTYINd4hq97ozJznfsP8Mn9G5IjAVUWNW85rnM7fZ55tWX0ht8uM1gTSoIdez4H4TxDGpETh2ucYmF9TwkmeiuKSGskXnfG065pZWk2oVbLyIEsbugHKW4gchlay3xyC9t3-dhf56LRh1eXVMDtebjp5ENGzIPwY2xMwwDNOO9Q5WxfYP2uItNbX_WwwupMKx3Uaahs3KDXKa5BFiCqut7kdrQKGZxqhNfc4mQYRCL8QvUt1fVZjs_WnCmp9xI0n6bZpyYj5aofl8ZZ4-IaCokwalDDQUwiDRUzgaxMAe4Vum6-KBkSM",
                "deep_link": "https://www.kiwi.com/deep?affilid=apoorvflightsearch&currency=EUR&flightsId=071104914bc8000098ae5ca3_0&from=DEL&lang=en&passengers=1&to=BOM&booking_token=EJCWar6gwXzj_SngONPDwYZzU130zsqpi_S_6Wh7Jr3usTqnKDWxrhJnMqTCXgwUQBHL8lRHqu5lMVfKGOAO9fbR2iHe6oG_CJHz0WWMpfX7ZQy3wQKtmcHSwGdsf6SoktUb7IlwdBS3IaP4TIyh407XD726vJo6xCfNHzw1x7rU9f9psYwnf_5PP8b7l3cl3HkuEV2mYrG5-4qplOenstPdkH1LPT2sKR0P2WY3w1eDkyNYhSwhbYZlfqEc3SfNvdM5ITSnX71eN_ITZHwvekGyi6C6pDk8exR2FFZKfvFlfvDt9ppDA6BIod-zgkHM171djCCw8C4IGMZ3jheBunfta5uDI9cBndfRch7YW1mLU2pcfrA0WcuMbik66C_h--7T_jof0IWcDqF8ys_l_yCK_W8dfbfYFwPuZjx2jI0ykoFEOfYF0MPO0g6sflkfM",
                "facilitated_booking_available": True,
                "pnr_count": 1,
                "has_airport_change": False,
                "technical_stops": 0,
                "throw_away_ticketing": False,
                "hidden_city_ticketing": False,
                "virtual_interlining": False,
                "local_arrival": "2023-02-12T04:50:00.000Z",
                "utc_arrival": "2023-02-11T23:20:00.000Z",
                "local_departure": "2023-02-12T02:40:00.000Z",
                "utc_departure": "2023-02-11T21:10:00.000Z"
            },
            {
                "id": "071104914bc90000537d7c0e_0",
                "flyFrom": "DEL",
                "flyTo": "BOM",
                "cityFrom": "New Delhi",
                "cityCodeFrom": "DEL",
                "cityTo": "Mumbai",
                "cityCodeTo": "BOM",
                "countryFrom": {
                    "code": "IN",
                    "name": "India"
                },
                "countryTo": {
                    "code": "IN",
                    "name": "India"
                },
                "nightsInDest": "None",
                "quality": 80.33326,
                "distance": 1139.47,
                "duration": {
                    "departure": 7800,
                    "return": 0,
                    "total": 7800
                },
                "price": 51,
                "conversion": {
                    "EUR": 51
                },
                "bags_price": {
                    "1": 0
                },
                "baglimit": {
                    "hand_height": 35,
                    "hand_length": 55,
                    "hand_weight": 7,
                    "hand_width": 25,
                    "hold_dimensions_sum": 158,
                    "hold_height": 52,
                    "hold_length": 78,
                    "hold_weight": 15,
                    "hold_width": 28
                },
                "availability": {
                    "seats": 2
                },
                "airlines": [
                    "G8"
                ],
                "route": [
                    {
                        "id": "071104914bc90000537d7c0e_0",
                        "combination_id": "071104914bc90000537d7c0e",
                        "flyFrom": "DEL",
                        "flyTo": "BOM",
                        "cityFrom": "New Delhi",
                        "cityCodeFrom": "DEL",
                        "cityTo": "Mumbai",
                        "cityCodeTo": "BOM",
                        "airline": "G8",
                        "flight_no": 323,
                        "operating_carrier": "G8",
                        "operating_flight_no": "323",
                        "fare_basis": "MO9RBINE",
                        "fare_category": "M",
                        "fare_classes": "M",
                        "fare_family": "",
                        "return": 0,
                        "bags_recheck_required": False,
                        "vi_connection": False,
                        "guarantee": False,
                        "equipment": "None",
                        "vehicle_type": "aircraft",
                        "local_arrival": "2023-02-13T20:10:00.000Z",
                        "utc_arrival": "2023-02-13T14:40:00.000Z",
                        "local_departure": "2023-02-13T18:00:00.000Z",
                        "utc_departure": "2023-02-13T12:30:00.000Z"
                    }
                ],
                "booking_token": "EG3MwoY4CJkL-ed7pD8EvWnIPtT3wQhgcjIcQd5yo1tbC6s2Dy1VHLLrr53zwKETo9ICoOjubtPz72cL0nDZ5dzVq_idhaXDWvru0yU2FVH3OPAkRt9Vuzamb6ru2WlJ66dpx8hc-nukLu1FMtUHlvdNFGp_YP-ktw5reobs-tTb7jWxi4wTpygF28Y6Cdvd5HOAIE1_F4W7uEw8g5u0n8ApLLwTVzYs3vv8uGtbXEyHDXKCG1UntO9uvWQtUjEI0RkMFCihpiEPbTmwyGmpqEQ_O48gsaE0olliTfYed5nGSqRILbRdNEL56q-oMY9O9buPgPj6eqf5yp5cN1FqHHoqe4MQLn9L62SRgXRMM-lmOVZtkW2-elK9GCa1sd5-7XJuEnV105mt_m8TDiMLknDnylj_e-Qt4ke3_tiuogfkPKBROVxI3AxNfoKx8JCA1ylVcSVse6EdiFDmNIDBg20hbE_uKIcGD1cVfoGler2isGTDCMrThzciFpggmcQVWCQDIH1gGIlJv4GAquX02ZSyFRnDSscA_FQY0IVRLuVLFvqbSmJ3XqLAsoNeHasd0",
                "deep_link": "https://www.kiwi.com/deep?affilid=apoorvflightsearch&currency=EUR&flightsId=071104914bc90000537d7c0e_0&from=DEL&lang=en&passengers=1&to=BOM&booking_token=EaGlXG3pxkphamAkaz5tmtTK_MjRF-I6QahhcRMHpOiaNNlhCQjgd3xW9MarlWcPqnR3KUz_Cdam6QV2YqP_wxKeAPuJfWIJpJxomRN_zdB7gZHivPWOz9wx2vJF2R7Xs7DRiyNbJyGKWCij5w3XoxNDFlG7OdN89OgiwjGhgjrVdMBv-n0mxuWa-Eo_VzpTh70g39M0zXK8k_9T1Gaj8r86-0NjOot9f3A4N_H-hJqbSigTLn8YUG0Jb3HS7xbrtnFFzLtkF4XVlIWnNYuU4uDiVS_A7wGmNbKepAFsEZGxqgx5cgiuOm26UuBoJFvMrQRDqce1I-LJUMzV-igoZ8U9_KN0-7NoqB9wYroRxXoEpJ-MW46fsg2oRvAWHIwIBUSfpBJhklCaPpPZGNO_AJDmHkEwn4EL5GQ0rLsJrAgS3U9uDfJFwJnlgyRIYLdkc",
                "facilitated_booking_available": True,
                "pnr_count": 1,
                "has_airport_change": False,
                "technical_stops": 0,
                "throw_away_ticketing": False,
                "hidden_city_ticketing": False,
                "virtual_interlining": False,
                "local_arrival": "2023-02-13T20:10:00.000Z",
                "utc_arrival": "2023-02-13T14:40:00.000Z",
                "local_departure": "2023-02-13T18:00:00.000Z",
                "utc_departure": "2023-02-13T12:30:00.000Z"
            },
            {
                "id": "071104914bc9000082587f6a_0",
                "flyFrom": "DEL",
                "flyTo": "BOM",
                "cityFrom": "New Delhi",
                "cityCodeFrom": "DEL",
                "cityTo": "Mumbai",
                "cityCodeTo": "BOM",
                "countryFrom": {
                    "code": "IN",
                    "name": "India"
                },
                "countryTo": {
                    "code": "IN",
                    "name": "India"
                },
                "nightsInDest": "None",
                "quality": 80.33326,
                "distance": 1139.47,
                "duration": {
                    "departure": 7800,
                    "return": 0,
                    "total": 7800
                },
                "price": 51,
                "conversion": {
                    "EUR": 51
                },
                "bags_price": {
                    "1": 0
                },
                "baglimit": {
                    "hand_height": 35,
                    "hand_length": 55,
                    "hand_weight": 7,
                    "hand_width": 25,
                    "hold_dimensions_sum": 158,
                    "hold_height": 52,
                    "hold_length": 78,
                    "hold_weight": 15,
                    "hold_width": 28
                },
                "availability": {
                    "seats": 2
                },
                "airlines": [
                    "G8"
                ],
                "route": [
                    {
                        "id": "071104914bc9000082587f6a_0",
                        "combination_id": "071104914bc9000082587f6a",
                        "flyFrom": "DEL",
                        "flyTo": "BOM",
                        "cityFrom": "New Delhi",
                        "cityCodeFrom": "DEL",
                        "cityTo": "Mumbai",
                        "cityCodeTo": "BOM",
                        "airline": "G8",
                        "flight_no": 354,
                        "operating_carrier": "G8",
                        "operating_flight_no": "354",
                        "fare_basis": "MO9RBINE",
                        "fare_category": "M",
                        "fare_classes": "M",
                        "fare_family": "",
                        "return": 0,
                        "bags_recheck_required": False,
                        "vi_connection": False,
                        "guarantee": False,
                        "equipment": "None",
                        "vehicle_type": "aircraft",
                        "local_arrival": "2023-02-14T00:40:00.000Z",
                        "utc_arrival": "2023-02-13T19:10:00.000Z",
                        "local_departure": "2023-02-13T22:30:00.000Z",
                        "utc_departure": "2023-02-13T17:00:00.000Z"
                    }
                ],
                "booking_token": "EYQTOhocBtQvKD6EAunGIzCo0jCrNgKBUHw9ivCCzkM9UPz4q7lTb_0EhedFCZcMuh1LFxgpz-JyTGq7Wjwsc9oZQMqsL5ep-U39O4_-srPmjQL0aJbBHH5-LHNU3l7T9003DWgWq1nYMr8jhOKwJFMiuHd5IaSg_w9BxWpQ5ZfW4KVEAwiWxfK2XphIGT4xAoF7F9mPOD6nVHy3DaT6agYPU8wafCRfWMmmidInLWxbWV9BN3e4b5NN_JoLEwDiKGN6LXP1qlxZrGQSNwmhmwagpCu4mqV6pARqHfzu0XhdBj8P1_rQ71GypczcCkEYQBhHTQlrJqUEsPlT-3vaPFekGjkO1Op5M5BZb7rqkkQi2oG_YMxYHbwGk19ziPyTc4dk1jidaaAY3JghQBGW4eKNJs16VGENbFyikkf3Y0O_eJH-MRQ_QzQETnsz9LMZHJi535ZsMqVpaO42u6W2_JSObjvIsVdF6NBtZXhT9CBRAKtYulgcI_aigKh7Q1zfgRvDB26c9swLkKbgWhEw2yd38M2fQDzPKTI04r6-sgRrvbAcf2xeVR8dtJFdQA1U4",
                "deep_link": "https://www.kiwi.com/deep?affilid=apoorvflightsearch&currency=EUR&flightsId=071104914bc9000082587f6a_0&from=DEL&lang=en&passengers=1&to=BOM&booking_token=E3WAP1JI9QNHxNc1FzmZGpsqKljn6-WyAJ53LZzqmGjHir0lJe2exyJuVZz2hUgjHxE8P5P4HyF92ck_HJK5ibY-6MKapZPD9XN1U1w7REgeuxjQXJR54sE3buLCL63H7viRowNbx4qOh-foIODkh4YFngiJleSS9johJUCoj4J29GRwe5O_muEeFYzihUnNmIISUC8WgKqnAyaR85lIKw3OeyDTWSz2Al0cKuF1VlzrGPTE3G-PisYx6Ok31ME7za4YWrxPTKmWgWvspIcg3qv3aY_5udbbr1orEpE6RK_UduzmLKG6Pi_GBMtAEsPfHVR1OS_6XUxaEzjVFfWpqCoxBc2xSr0YuZIosZjSnzweA2lUjtrH78VMaoX76FQWPGxFlOqnSzkiTk3NytX-TJhuhqvWq7-6t-CwDhGJyfL0=",
                "facilitated_booking_available": True,
                "pnr_count": 1,
                "has_airport_change": False,
                "technical_stops": 0,
                "throw_away_ticketing": False,
                "hidden_city_ticketing": False,
                "virtual_interlining": False,
                "local_arrival": "2023-02-14T00:40:00.000Z",
                "utc_arrival": "2023-02-13T19:10:00.000Z",
                "local_departure": "2023-02-13T22:30:00.000Z",
                "utc_departure": "2023-02-13T17:00:00.000Z"
            },
            {
                "id": "071104914bc9000023f6f2c1_0",
                "flyFrom": "DEL",
                "flyTo": "BOM",
                "cityFrom": "New Delhi",
                "cityCodeFrom": "DEL",
                "cityTo": "Mumbai",
                "cityCodeTo": "BOM",
                "countryFrom": {
                    "code": "IN",
                    "name": "India"
                },
                "countryTo": {
                    "code": "IN",
                    "name": "India"
                },
                "nightsInDest": "None",
                "quality": 80.33326,
                "distance": 1139.47,
                "duration": {
                    "departure": 7800,
                    "return": 0,
                    "total": 7800
                },
                "price": 51,
                "conversion": {
                    "EUR": 51
                },
                "bags_price": {
                    "1": 0
                },
                "baglimit": {
                    "hand_height": 38,
                    "hand_length": 57,
                    "hand_weight": 7,
                    "hand_width": 20,
                    "hold_dimensions_sum": 158,
                    "hold_height": 52,
                    "hold_length": 78,
                    "hold_weight": 15,
                    "hold_width": 28
                },
                "availability": {
                    "seats": 2
                },
                "airlines": [
                    "6E"
                ],
                "route": [
                    {
                        "id": "071104914bc9000023f6f2c1_0",
                        "combination_id": "071104914bc9000023f6f2c1",
                        "flyFrom": "DEL",
                        "flyTo": "BOM",
                        "cityFrom": "New Delhi",
                        "cityCodeFrom": "DEL",
                        "cityTo": "Mumbai",
                        "cityCodeTo": "BOM",
                        "airline": "6E",
                        "flight_no": 2017,
                        "operating_carrier": "6E",
                        "operating_flight_no": "2017",
                        "fare_basis": "",
                        "fare_category": "M",
                        "fare_classes": "R",
                        "fare_family": "",
                        "return": 0,
                        "bags_recheck_required": False,
                        "vi_connection": False,
                        "guarantee": False,
                        "equipment": "None",
                        "vehicle_type": "aircraft",
                        "local_arrival": "2023-02-13T21:30:00.000Z",
                        "utc_arrival": "2023-02-13T16:00:00.000Z",
                        "local_departure": "2023-02-13T19:20:00.000Z",
                        "utc_departure": "2023-02-13T13:50:00.000Z"
                    }
                ],
                "booking_token": "Evc-DA4YhfDxkNMD4hky6IFwbITPYxaRNWhiMUIgSXxZ30BHUYE4U_9CaWegS-ziY9HZz66KvyA7RfO7BngwEW_CcUyXURyH0_13T-quR5EaFYTAkUvm31qLRfRYvdzj7uFhZOc9XfThrqmdFC33MGPsek3onx7oe1-Ar23ioBd_-DShD1JWv87DC93FwfLPtVpmVCU98uaiDq7jZYzdDSlGQ3g0Z7owJDeKbpskTQBrF907_lXqT__w0rMSqlPOPZqz6Dcu5WAjSLQExLWxVu3QHoEFWaygrORImX5PQsN0-yf9idiPOb4YXlx4gt2kKw0gFvKNUd5v041DqFdfayNBGdUXDGtF0PiJvwX_McVEwoW-1Ylr-cxtRs4J2uIi7bGkFD-1trWN3qKV-N2kkrzjILX8ddX8qXwXsfN-ebDhQ1MepVVuPHdGiSoUoOJJLockD08cNOuwoAVGJ1wrHPrvYB_ws-l84Ce0TMTzkadbeCNmMoSP3b0hQBabPhoOWbYf4Of3WywAIam0U0r1zZl2sR1hsjFelCWrlBMpUWjY=",
                "deep_link": "https://www.kiwi.com/deep?affilid=apoorvflightsearch&currency=EUR&flightsId=071104914bc9000023f6f2c1_0&from=DEL&lang=en&passengers=1&to=BOM&booking_token=ECj-s4f0eBlPjsqZFpMb13KR421Uh7G1xuvBQMVpXXLOzwKTXiGM_9pmfz8lTHV8EPbNj_9u7AOjO-3qL7n0_phkliMGbI_YAwVgLJlwSVuGJ5Kzm8X5jVMkd6lweIEy14qzgXpcbM8PdEf6hlh6WA5t4tSGKYLRPDu6DEs9FoJLsXGjeTUIDnjtPkz72Aq0LJL5FiybA_4I13IVxQP3Ofig-6w2NAo75pJD8PjZ1LisLL7yDBo7fSnzjmedwEIyLp0ldMv43TCN0UG-xzNuOxD3R2fruOwxaNCmcN8YKH17ie5VdIxn-hHtj9hwepQM1uasGNr_DssSg_C6V3iAZf-ItDftMqnNDydDXge_Tkw21OcCZ7PNRiUoClCNx1Y_1a_f8VlnVwR5BNMGsOK_epLK_nSGTTfB9LI2YvttFY2s=",
                "facilitated_booking_available": True,
                "pnr_count": 1,
                "has_airport_change": False,
                "technical_stops": 0,
                "throw_away_ticketing": False,
                "hidden_city_ticketing": False,
                "virtual_interlining": False,
                "local_arrival": "2023-02-13T21:30:00.000Z",
                "utc_arrival": "2023-02-13T16:00:00.000Z",
                "local_departure": "2023-02-13T19:20:00.000Z",
                "utc_departure": "2023-02-13T13:50:00.000Z"
            },
            {
                "id": "071104914bc900002cd869b0_0",
                "flyFrom": "DEL",
                "flyTo": "BOM",
                "cityFrom": "New Delhi",
                "cityCodeFrom": "DEL",
                "cityTo": "Mumbai",
                "cityCodeTo": "BOM",
                "countryFrom": {
                    "code": "IN",
                    "name": "India"
                },
                "countryTo": {
                    "code": "IN",
                    "name": "India"
                },
                "nightsInDest": "None",
                "quality": 80.999925,
                "distance": 1139.47,
                "duration": {
                    "departure": 8100,
                    "return": 0,
                    "total": 8100
                },
                "price": 51,
                "conversion": {
                    "EUR": 51
                },
                "bags_price": {
                    "1": 0
                },
                "baglimit": {
                    "hand_height": 38,
                    "hand_length": 57,
                    "hand_weight": 7,
                    "hand_width": 20,
                    "hold_dimensions_sum": 158,
                    "hold_height": 52,
                    "hold_length": 78,
                    "hold_weight": 15,
                    "hold_width": 28
                },
                "availability": {
                    "seats": 2
                },
                "airlines": [
                    "6E"
                ],
                "route": [
                    {
                        "id": "071104914bc900002cd869b0_0",
                        "combination_id": "071104914bc900002cd869b0",
                        "flyFrom": "DEL",
                        "flyTo": "BOM",
                        "cityFrom": "New Delhi",
                        "cityCodeFrom": "DEL",
                        "cityTo": "Mumbai",
                        "cityCodeTo": "BOM",
                        "airline": "6E",
                        "flight_no": 5318,
                        "operating_carrier": "6E",
                        "operating_flight_no": "5318",
                        "fare_basis": "",
                        "fare_category": "M",
                        "fare_classes": "R",
                        "fare_family": "",
                        "return": 0,
                        "bags_recheck_required": False,
                        "vi_connection": False,
                        "guarantee": False,
                        "equipment": "None",
                        "vehicle_type": "aircraft",
                        "local_arrival": "2023-02-13T18:40:00.000Z",
                        "utc_arrival": "2023-02-13T13:10:00.000Z",
                        "local_departure": "2023-02-13T16:25:00.000Z",
                        "utc_departure": "2023-02-13T10:55:00.000Z"
                    }
                ],
                "booking_token": "EeuC7DVqRMuxZ7Uu_4Ko9gEdvA0wiCefRyAbWWHNnOVlbS4awO4HrWR6oAxMzIuKl5y5ctSaKFfV04GZ72fKu5d6nc2BECt5lNpNBuq0eTdqbDjnftDP7N_p5h5d4-ielIqA7Mxu04BLQuGwyEI3onn6iN-Pez3w0aDbS2bB5S277qqrDEtzo334U30E_ZvQVc39nXKlbeavJc703AX0HTQ9foDw8SNj4JsQ9tTlcYY8iSdCDADFQlWyfhgujnGQcGPXMgMhA3vlTRc0Hke0Ej2mYScC8XZjcjxZL3J3reU2eAWnXty4DW-mSxwBtQKH8I-1cjDcm4_aBdiBX60UIVTRCuWltSfza3qs-jlwETYwO_DQD0aERE-TDU9SoI1uVvH4blM10igqDhYDkmO9ryKQUbbknQj6DUpfD-65tyVBEera5APjIVqoliP8w2G7IsBFW-wWzPjQBWyoHCQlTfGL-ICJtDc7763URZs3Mf_qTkvtfQ2-I1cA_mALt4aRFYIzFEA6eSrPreatrWTB_svPr27q_T4D_alcrAa7c5bE=",
                "deep_link": "https://www.kiwi.com/deep?affilid=apoorvflightsearch&currency=EUR&flightsId=071104914bc900002cd869b0_0&from=DEL&lang=en&passengers=1&to=BOM&booking_token=EeCCZmx5lJIhnSTAMB3pE7g2UvdIcfbVAkRin74VT6ONXxYVi3cx6kucKDTy_Ih8UTm9wFjZfyXiUTv4hjm7oJSFehlchW12WBo68Lwyvq7OHtjqUS2eOkfeeRZR6sKzMteAXavOxjgrJIjzG0KaKt1S2mYLr9GiiNCZH7hvoUEZO-gx1cfIOn0y4gLXvxajvRstvjCSVoDQTKRGB0ZxoyZHRVIgaK1VABZ9K7_ruIDhSqfFh7blG7ic5tbzq2FBpZnlHkvVPyyhSdB0QPL4OpKTcBy47nM0KrztLlGqLPFZlFZx8RUml1icMFqs03W7mYkJ7nCEHcawbShgGK4XAF4WPeZBv-xhNa19fRZ2LUkFE8SDw8GBQ5lSrZA-tYv7sdgusC8r0rjO6RVxSki1vyg==",
                "facilitated_booking_available": True,
                "pnr_count": 1,
                "has_airport_change": False,
                "technical_stops": 0,
                "throw_away_ticketing": False,
                "hidden_city_ticketing": False,
                "virtual_interlining": False,
                "local_arrival": "2023-02-13T18:40:00.000Z",
                "utc_arrival": "2023-02-13T13:10:00.000Z",
                "local_departure": "2023-02-13T16:25:00.000Z",
                "utc_departure": "2023-02-13T10:55:00.000Z"
            },
            {
                "id": "071104914bc800003bf9159e_0",
                "flyFrom": "DEL",
                "flyTo": "BOM",
                "cityFrom": "New Delhi",
                "cityCodeFrom": "DEL",
                "cityTo": "Mumbai",
                "cityCodeTo": "BOM",
                "countryFrom": {
                    "code": "IN",
                    "name": "India"
                },
                "countryTo": {
                    "code": "IN",
                    "name": "India"
                },
                "nightsInDest": "None",
                "quality": 80.999925,
                "distance": 1139.47,
                "duration": {
                    "departure": 8100,
                    "return": 0,
                    "total": 8100
                },
                "price": 51,
                "conversion": {
                    "EUR": 51
                },
                "bags_price": {
                    "1": 0
                },
                "baglimit": {
                    "hand_height": 38,
                    "hand_length": 57,
                    "hand_weight": 7,
                    "hand_width": 20,
                    "hold_dimensions_sum": 158,
                    "hold_height": 52,
                    "hold_length": 78,
                    "hold_weight": 15,
                    "hold_width": 28
                },
                "availability": {
                    "seats": 2
                },
                "airlines": [
                    "6E"
                ],
                "route": [
                    {
                        "id": "071104914bc800003bf9159e_0",
                        "combination_id": "071104914bc800003bf9159e",
                        "flyFrom": "DEL",
                        "flyTo": "BOM",
                        "cityFrom": "New Delhi",
                        "cityCodeFrom": "DEL",
                        "cityTo": "Mumbai",
                        "cityCodeTo": "BOM",
                        "airline": "6E",
                        "flight_no": 2716,
                        "operating_carrier": "6E",
                        "operating_flight_no": "2716",
                        "fare_basis": "",
                        "fare_category": "M",
                        "fare_classes": "X",
                        "fare_family": "",
                        "return": 0,
                        "bags_recheck_required": False,
                        "vi_connection": False,
                        "guarantee": False,
                        "equipment": "None",
                        "vehicle_type": "aircraft",
                        "local_arrival": "2023-02-12T04:15:00.000Z",
                        "utc_arrival": "2023-02-11T22:45:00.000Z",
                        "local_departure": "2023-02-12T02:00:00.000Z",
                        "utc_departure": "2023-02-11T20:30:00.000Z"
                    }
                ],
                "booking_token": "EwOASFz0KTGnzssmWW32REr7PwO3ip9jwZEI7X8Sy9HdQGTxRNW3UcSXgOkeR3iwVNEZUbSm-jJqyMGBeqJtuPgjgqgxjV_6u5lHkO6G4L1OczrPT1wTpS6ibcpqfp3KVUIETYtwQ0eUXwqxkCUhEfdfyOwLyMbYldc6toYOtDIp4-16SoeVOQUUdtEm2-HiOO5F9ifN6VzpRtHBkTT1lYw1TLoRkiXyIWzh6O4oqzxnit6o1cWqi6RGwIbJID5LaeYoMckQR4k-Qv-99TFSTCNiWcPduopJtNlnnXUU7iMXXfP0SKnk0XLnWhvkY2pgEacns52NXK4QsKy6sBictrzKzCvj9YJX28wbioRyHXq07Sx7a4_wUbdprOnOvThLAkv-N3wOdTpthai9RQQpPcO4x0byOeeOMM4T9mtmROWydeCOK9ui6ROvJOwypmGIu800GsjhPjpvQ_T9BxKABurth1BcJv1l-PduRGpAxSxafZ14W4wcy9qcQljQWMMo25CCGtCH0V957M4fK5s21rKy5w27hQJ8Whwch5FqdN1qXDiUPATyxkBAhksMNuM5z",
                "deep_link": "https://www.kiwi.com/deep?affilid=apoorvflightsearch&currency=EUR&flightsId=071104914bc800003bf9159e_0&from=DEL&lang=en&passengers=1&to=BOM&booking_token=ETYnI5ehZUchWAX1th9OHOpbwuS-HvVki_-jQEfdhGiMy-e-7_04Xhmnti0QaUjG2HYbaXqFIZci2iu8GBFheclWr9q1SA09HK60WPIAX3L5f0bkA7tCnurneTTtcMM6usA1pHvNvHdIQ-ymJaJUG19kylScrmflhGitKjZlkEtuzfr_wwEUmdG-JYLm4MZNvP6Cbcl9DKI4nEgVX7D_S2xS-5axjmt7opYB-P4hmx5Gv7ADimaV7NZNa7bK2JL-r2AQOmI-lQFeVG3YNtGGqLyGCenEWUrLihzAgd_zroCtgTmT9LF77ZF_Mx6r8zhKI8qfRit8YunGJAh58NbFoF_8yMHjEE7de3Q04Fv_41EOnft-6w-F0-aVJ2mUxcjgZB5jWwisWpGtr2qNx9fqkA3ovlK9xvKSUbg8WhuIkfUA=",
                "facilitated_booking_available": True,
                "pnr_count": 1,
                "has_airport_change": False,
                "technical_stops": 0,
                "throw_away_ticketing": False,
                "hidden_city_ticketing": False,
                "virtual_interlining": False,
                "local_arrival": "2023-02-12T04:15:00.000Z",
                "utc_arrival": "2023-02-11T22:45:00.000Z",
                "local_departure": "2023-02-12T02:00:00.000Z",
                "utc_departure": "2023-02-11T20:30:00.000Z"
            },
            {
                "id": "071104914bc90000bb3dc94c_0",
                "flyFrom": "DEL",
                "flyTo": "BOM",
                "cityFrom": "New Delhi",
                "cityCodeFrom": "DEL",
                "cityTo": "Mumbai",
                "cityCodeTo": "BOM",
                "countryFrom": {
                    "code": "IN",
                    "name": "India"
                },
                "countryTo": {
                    "code": "IN",
                    "name": "India"
                },
                "nightsInDest": "None",
                "quality": 80.999925,
                "distance": 1139.47,
                "duration": {
                    "departure": 8100,
                    "return": 0,
                    "total": 8100
                },
                "price": 51,
                "conversion": {
                    "EUR": 51
                },
                "bags_price": {
                    "1": 0
                },
                "baglimit": {
                    "hand_height": 38,
                    "hand_length": 57,
                    "hand_weight": 7,
                    "hand_width": 20,
                    "hold_dimensions_sum": 158,
                    "hold_height": 52,
                    "hold_length": 78,
                    "hold_weight": 15,
                    "hold_width": 28
                },
                "availability": {
                    "seats": 2
                },
                "airlines": [
                    "6E"
                ],
                "route": [
                    {
                        "id": "071104914bc90000bb3dc94c_0",
                        "combination_id": "071104914bc90000bb3dc94c",
                        "flyFrom": "DEL",
                        "flyTo": "BOM",
                        "cityFrom": "New Delhi",
                        "cityCodeFrom": "DEL",
                        "cityTo": "Mumbai",
                        "cityCodeTo": "BOM",
                        "airline": "6E",
                        "flight_no": 2114,
                        "operating_carrier": "6E",
                        "operating_flight_no": "2114",
                        "fare_basis": "",
                        "fare_category": "M",
                        "fare_classes": "R",
                        "fare_family": "",
                        "return": 0,
                        "bags_recheck_required": False,
                        "vi_connection": False,
                        "guarantee": False,
                        "equipment": "None",
                        "vehicle_type": "aircraft",
                        "local_arrival": "2023-02-14T00:00:00.000Z",
                        "utc_arrival": "2023-02-13T18:30:00.000Z",
                        "local_departure": "2023-02-13T21:45:00.000Z",
                        "utc_departure": "2023-02-13T16:15:00.000Z"
                    }
                ],
                "booking_token": "Ejc4TJi0PWPRVyXzxh1avXyhlQ2KDMfYPlRkWYIDj6OJycg_sNQ6p5rmW02101HX2G_e-CmKfs3MOPwVJZ_PqVgHUymGohI-ynwFpK-S0qR65pM0cFTPM6JErnYBo6aUC9Mpru3tw5vUAZM-lqIFOt89YZ1rFdrHqPDanhzEXHdqyO1vKKi4a2o0Rl3NtBjmuPQnZlOdXlMhHtsHPndzXkxspyBbnn4wn4kdcEtdcSPO7UfBfO01N2nMXPK4Rni0UjRs2RIswQSkca_Vz7zYdkBe1BUkHSOsibqB9GgW-Dp7723e8GKD39XZGxYPB4IyrTFnMzF4vo4QxU6BU_jwxKqi6tqXjsqC5UyJtiw6WuEbXqTghaWGZnV5FmoH8hO4heDqTgahcRzcymsRnoEjl1TEtsYYh1xJrHD0Yr7FT03lJ0X6ExWUoeQLU04JZGAx6cjwQj7ZiHF756evZ8UtE2JrOCjoamL_f0AA2ozKLMTPcZ5_l2baFZCEWJpha0LydSwjcqXaqJDMDrB6nEJaA0UYnL5y_XdKcnKNbcKaVNVs=",
                "deep_link": "https://www.kiwi.com/deep?affilid=apoorvflightsearch&currency=EUR&flightsId=071104914bc90000bb3dc94c_0&from=DEL&lang=en&passengers=1&to=BOM&booking_token=EJ_0-6AXPeTHMOUE_NziJm2wSwQ9AYWQRgBeRB9hCJkIzW48JaE0gY82h8Il6fNTtNu73ZA4l5y4MUn6xiXAtNvPmnBKm6-PgjxlJP2W2ewEAYpTiUytAqvmpntpNwZ2jrppAEyzlTBSyUPL59W7nsMwBDmmzK281DqChZT1YdzlxkPgMHkV5f-rT1kvaGlH65T_qnp2NQubB3PzKZJDPzxCqRq2QEY1x36shCUrlQ5pp6aIhfRqLJbqzqlI5WBU7lgl_ZwYOMEXXt8-uHgKR1r-29Dhcw1Raywaiv9YEoeMl3mlXWDWcyzyRUWi_lo4bD4YzN4atfKUK-9mK4Tx6IcXj4DIhWCyZgS6hpwHPAenCWLPxYuwbT0s5QLe4OMAjLt6AC_pCCx_Zzfi31R-aZg==",
                "facilitated_booking_available": True,
                "pnr_count": 1,
                "has_airport_change": False,
                "technical_stops": 0,
                "throw_away_ticketing": False,
                "hidden_city_ticketing": False,
                "virtual_interlining": False,
                "local_arrival": "2023-02-14T00:00:00.000Z",
                "utc_arrival": "2023-02-13T18:30:00.000Z",
                "local_departure": "2023-02-13T21:45:00.000Z",
                "utc_departure": "2023-02-13T16:15:00.000Z"
            },
            {
                "id": "071104914bc900000b58d839_0",
                "flyFrom": "DEL",
                "flyTo": "BOM",
                "cityFrom": "New Delhi",
                "cityCodeFrom": "DEL",
                "cityTo": "Mumbai",
                "cityCodeTo": "BOM",
                "countryFrom": {
                    "code": "IN",
                    "name": "India"
                },
                "countryTo": {
                    "code": "IN",
                    "name": "India"
                },
                "nightsInDest": "None",
                "quality": 80.999925,
                "distance": 1139.47,
                "duration": {
                    "departure": 8100,
                    "return": 0,
                    "total": 8100
                },
                "price": 51,
                "conversion": {
                    "EUR": 51
                },
                "bags_price": {
                    "1": 0
                },
                "baglimit": {
                    "hand_height": 38,
                    "hand_length": 57,
                    "hand_weight": 7,
                    "hand_width": 20,
                    "hold_dimensions_sum": 158,
                    "hold_height": 52,
                    "hold_length": 78,
                    "hold_weight": 15,
                    "hold_width": 28
                },
                "availability": {
                    "seats": 2
                },
                "airlines": [
                    "6E"
                ],
                "route": [
                    {
                        "id": "071104914bc900000b58d839_0",
                        "combination_id": "071104914bc900000b58d839",
                        "flyFrom": "DEL",
                        "flyTo": "BOM",
                        "cityFrom": "New Delhi",
                        "cityCodeFrom": "DEL",
                        "cityTo": "Mumbai",
                        "cityCodeTo": "BOM",
                        "airline": "6E",
                        "flight_no": 864,
                        "operating_carrier": "6E",
                        "operating_flight_no": "864",
                        "fare_basis": "",
                        "fare_category": "M",
                        "fare_classes": "R",
                        "fare_family": "",
                        "return": 0,
                        "bags_recheck_required": False,
                        "vi_connection": False,
                        "guarantee": False,
                        "equipment": "None",
                        "vehicle_type": "aircraft",
                        "local_arrival": "2023-02-13T19:40:00.000Z",
                        "utc_arrival": "2023-02-13T14:10:00.000Z",
                        "local_departure": "2023-02-13T17:25:00.000Z",
                        "utc_departure": "2023-02-13T11:55:00.000Z"
                    }
                ],
                "booking_token": "ExS--Drukn597-hf3TyGOxFnob2aYx95Asow3wE-_Ygc5Gdlwa1iUAw5u-jGTkeu29EDVOKrik-HBzlwdhdTbknvNt-b79v_QwayWm6TEVp2nTslW3b4aknUqD44qBwGaankqk54ihQHdRzc5jbooDFI-JzaKkvR3DZtC4O3bhk-IEI-_01OgreX3JX4zusU780vQYDrpkkA2DMr7BC7lPgL1RIufRff2irUrYHGhWQLqadK3_M_vYJ3MCycea3kwo1Xox3uiay7S5gj2S0h_fFikxsvudGHQjZJAJpU33S_dV1ToC-p8N83h608AFLwaqVLpYgNOIgoZggYVTV5g2RSfIjt89JTY9E64UWbM2cIct3zkTEl-eGGKv8OFscy7SSbpOjQLa20JQpaCgPkT3iRhEVgxLmaVreJ86rSTSIkG8rSRLcsS_ZPUmupbfyo1WX3n2n_j74MFFHv4v5t_DKLLbU5-nZUGGWm_JaYFVvZO3_EKRNyp1mXN1XPuW1JSqlvHduYrEu4hz2igMkolA3kIMzhnOj7oyeJAjxFUvvk=",
                "deep_link": "https://www.kiwi.com/deep?affilid=apoorvflightsearch&currency=EUR&flightsId=071104914bc900000b58d839_0&from=DEL&lang=en&passengers=1&to=BOM&booking_token=EqQBUYtxsorVZ5vE65rrpRFHnYVp0lLFeUYvTjlNsSD3vfKOEMQrRQrJ8oT-b4LfRp_FnDvf27s_1r_aiq-DsxOOG6VStVSLX2n7QyL4koDVj3MABOVgfCQrViL6Tr9HuYUCNQTwD4V13HiO1O33sp4f9NtVdbvg6RyaqKso9htvYyfcl0Mell9kV6Lb4k5RFh3Oq72BOA_rUcoO6hsCj8kpcSLTk3as582hLh0eNUMZKYP1p5X_ix7Yj5Rda_YmONMRE_MhHp5rD1UyWBdpBdF4a9V_X8MMjVlZK30Dk_SxfnAL0XCDKX_2kNBlXJgtRpQIWHEE5RYmr38d9G4u-QscfDiMMNZ8_B-0pQmLKHaikO9FkWmi78mXb25orn-zYMV-s7s9fSOg0YGtCWSwuag==",
                "facilitated_booking_available": True,
                "pnr_count": 1,
                "has_airport_change": False,
                "technical_stops": 0,
                "throw_away_ticketing": False,
                "hidden_city_ticketing": False,
                "virtual_interlining": False,
                "local_arrival": "2023-02-13T19:40:00.000Z",
                "utc_arrival": "2023-02-13T14:10:00.000Z",
                "local_departure": "2023-02-13T17:25:00.000Z",
                "utc_departure": "2023-02-13T11:55:00.000Z"
            },
            {
                "id": "071104914bc90000d36f1cf5_0",
                "flyFrom": "DEL",
                "flyTo": "BOM",
                "cityFrom": "New Delhi",
                "cityCodeFrom": "DEL",
                "cityTo": "Mumbai",
                "cityCodeTo": "BOM",
                "countryFrom": {
                    "code": "IN",
                    "name": "India"
                },
                "countryTo": {
                    "code": "IN",
                    "name": "India"
                },
                "nightsInDest": "None",
                "quality": 80.999925,
                "distance": 1139.47,
                "duration": {
                    "departure": 8100,
                    "return": 0,
                    "total": 8100
                },
                "price": 51,
                "conversion": {
                    "EUR": 51
                },
                "bags_price": {
                    "1": 0
                },
                "baglimit": {
                    "hand_height": 35,
                    "hand_length": 55,
                    "hand_weight": 7,
                    "hand_width": 25,
                    "hold_dimensions_sum": 158,
                    "hold_height": 52,
                    "hold_length": 78,
                    "hold_weight": 15,
                    "hold_width": 28
                },
                "availability": {
                    "seats": 2
                },
                "airlines": [
                    "G8"
                ],
                "route": [
                    {
                        "id": "071104914bc90000d36f1cf5_0",
                        "combination_id": "071104914bc90000d36f1cf5",
                        "flyFrom": "DEL",
                        "flyTo": "BOM",
                        "cityFrom": "New Delhi",
                        "cityCodeFrom": "DEL",
                        "cityTo": "Mumbai",
                        "cityCodeTo": "BOM",
                        "airline": "G8",
                        "flight_no": 330,
                        "operating_carrier": "G8",
                        "operating_flight_no": "330",
                        "fare_basis": "MO9RBINE",
                        "fare_category": "M",
                        "fare_classes": "M",
                        "fare_family": "",
                        "return": 0,
                        "bags_recheck_required": False,
                        "vi_connection": False,
                        "guarantee": False,
                        "equipment": "None",
                        "vehicle_type": "aircraft",
                        "local_arrival": "2023-02-13T23:15:00.000Z",
                        "utc_arrival": "2023-02-13T17:45:00.000Z",
                        "local_departure": "2023-02-13T21:00:00.000Z",
                        "utc_departure": "2023-02-13T15:30:00.000Z"
                    }
                ],
                "booking_token": "Ee7eFQEqUxncY3zOvL5LZzlhNgYT1uC5g4URl9QLejGhXIRkv-5_UTfzevlDuaQuohWjpo4T-AjdNzGCOG7KElE2TTqZ_tqCNHEuAaZWbk0B0othsegsxgReBH9VDICZ1dtvhdV_4Z8cwtWa8OZevtj7k1koes-AODX6LMnl8hoeOW3ON0-CIvbRrpFl7ngY-dH9CsfR2SANqJHTb4LDwyRLiUCTMNKAvnN9lyooQA9pjD9gl1-7BZC3PHEZMqkvu_rAQ-S14-PoXAc2MChZnBKg_m8evuyPQlZsMVv4pH38Yru8mdvSbYWih9p45YvXeNUBpArI0IQJs5KVRpz90_KHVx-Szmqwi_akXA4m05Si7pBfdWDZPLfEprhd5eOQyFHHWzDilwkEkPn7fceKnZXkpiKhW7_-70fGbbFAIDUbnMTvbAsr9cdFm5c2XP4T8IHyAfLDSn9aNg9TBHqlA-7PFrwOrGhLMqaNxi7YDeSxKgC9P1Hp3VaA86RPtKbzW4wikIJY2irpWp7VNlsYxjbMgECVVoI-n3rdUZAp2WaSQH-Pre_LDkk1HaNCm8o6K",
                "deep_link": "https://www.kiwi.com/deep?affilid=apoorvflightsearch&currency=EUR&flightsId=071104914bc90000d36f1cf5_0&from=DEL&lang=en&passengers=1&to=BOM&booking_token=Er1MiWT7TPTZHk35g86OFiRFjCXevfpYkE5VOcG77ro84RD3qNhzDki7iPti5fRYMAKpdyj0ONfXwJm8koFT-BwGiIeGuxr-Qpwe-713wBdTJ-bLmYR6IBV2VYEiEPnulz3qI1lO3LkGqhlGfnQtKJPKg2H9XsmeT_AKe2mbsvB7qc5-_i8NVSJ5bp9pL2B-5w6QFKt0kochiJzFY_ee3XD2M1oBkpPzUewhb7CvAKgIKogVdwn_GsTBlzhy2cfTzPrF_jIDjPmz1o755wy0Q9BJV-UZxZDptP_N2YOs4l2vyGqlTcuSu_OHoXMHJiqR6UOzL13EhBURXh0oS5GJVOrz3-SLXt44y_9hQn5gW5KSMV0uYYLV23Xl9vMWYhgeb7cVd2BPkM-4zDGNHMfwMLzaSfFw77F5hp1R3qGQ9P8s=",
                "facilitated_booking_available": True,
                "pnr_count": 1,
                "has_airport_change": False,
                "technical_stops": 0,
                "throw_away_ticketing": False,
                "hidden_city_ticketing": False,
                "virtual_interlining": False,
                "local_arrival": "2023-02-13T23:15:00.000Z",
                "utc_arrival": "2023-02-13T17:45:00.000Z",
                "local_departure": "2023-02-13T21:00:00.000Z",
                "utc_departure": "2023-02-13T15:30:00.000Z"
            },
            {
                "id": "071104914bc9000080bde7e5_0",
                "flyFrom": "DEL",
                "flyTo": "BOM",
                "cityFrom": "New Delhi",
                "cityCodeFrom": "DEL",
                "cityTo": "Mumbai",
                "cityCodeTo": "BOM",
                "countryFrom": {
                    "code": "IN",
                    "name": "India"
                },
                "countryTo": {
                    "code": "IN",
                    "name": "India"
                },
                "nightsInDest": "None",
                "quality": 81.66659,
                "distance": 1139.47,
                "duration": {
                    "departure": 8400,
                    "return": 0,
                    "total": 8400
                },
                "price": 51,
                "conversion": {
                    "EUR": 51
                },
                "bags_price": {
                    "1": 0
                },
                "baglimit": {
                    "hand_height": 38,
                    "hand_length": 57,
                    "hand_weight": 7,
                    "hand_width": 20,
                    "hold_dimensions_sum": 158,
                    "hold_height": 52,
                    "hold_length": 78,
                    "hold_weight": 15,
                    "hold_width": 28
                },
                "availability": {
                    "seats": 2
                },
                "airlines": [
                    "6E"
                ],
                "route": [
                    {
                        "id": "071104914bc9000080bde7e5_0",
                        "combination_id": "071104914bc9000080bde7e5",
                        "flyFrom": "DEL",
                        "flyTo": "BOM",
                        "cityFrom": "New Delhi",
                        "cityCodeFrom": "DEL",
                        "cityTo": "Mumbai",
                        "cityCodeTo": "BOM",
                        "airline": "6E",
                        "flight_no": 2138,
                        "operating_carrier": "6E",
                        "operating_flight_no": "2138",
                        "fare_basis": "",
                        "fare_category": "M",
                        "fare_classes": "R",
                        "fare_family": "",
                        "return": 0,
                        "bags_recheck_required": False,
                        "vi_connection": False,
                        "guarantee": False,
                        "equipment": "None",
                        "vehicle_type": "aircraft",
                        "local_arrival": "2023-02-13T14:20:00.000Z",
                        "utc_arrival": "2023-02-13T08:50:00.000Z",
                        "local_departure": "2023-02-13T12:00:00.000Z",
                        "utc_departure": "2023-02-13T06:30:00.000Z"
                    }
                ],
                "booking_token": "E2EWV_KgLkV_h11FNPmv4OXcPZCHr6xJnKrv9N4lfG9TEzbJwwbkGfmZP8r_6x7VkVTqx_ntQUSQVtwrdE97ue7U74zsyTv0AEmdn_PMV9g7_an78uoCkwF9ij-eCoLktkvC3srs8FREIDoTpiyTg7vRZza-jOgdqwEy_G670av10grBC8hZ_ei0SEFvKZSOUaLZqdVngiCVN5Q-LWlF1jYlLYYSLZOpeXfIbNiWq_GVEB_beKM8WtMh8gjwX33OBoIvIdOZUxnKeiNmC5CEw-E4pdAQTDwAAt5bJM3IztDXrv4quQ6fasslgc0YC2VJXUh4cEs_7bD1niJtOGmDgwoXhylGkVKvQadGUL8VCt6jJcbHuyzmxxuUd-GOJ2LWgI7DN9iK0o0mk4DM0DORExaqnW7Nt7N6m_OxRRRqibEnWL5xhNUiOmoYb5iS9dJHR-SF7JIw2LMUBvFKvuz_6iFJLv-JF_rkL1D2tJ7UDU4mw8ioB0R0lt_-4zWXqa2RAXaVwOD86Aos9F0MumqfX5OiLvRcOrPFaFloTleI8oTk=",
                "deep_link": "https://www.kiwi.com/deep?affilid=apoorvflightsearch&currency=EUR&flightsId=071104914bc9000080bde7e5_0&from=DEL&lang=en&passengers=1&to=BOM&booking_token=EOlYiXR1bHwsZERiM98ekYQ4CLDpePV0hoEd3E6sQdv7vdcEUvFYv5JP3halBF89zmZ2S_ZL9htuIUsNd4GHb2AwACR3BBL4asWdThso71OtokgbPNeP229lQ-BTvuCIMX9bqoQfqUsLfGeYi99e__djVR4ohl1hO6uCQMxY_PELNqyej6OJpuVb8p8FhoqoLfoLZNfppMjv1vTPObcMSZO5CMx6TAvsGMim6UZ3RxkXUwebWbN9YFNImlJ1lUrKJkKbdft1ztIYHwcI8RZIGXivVy3fzVDm-6Rm0dt6rNqWy-QUruCK14SJVkgqJ8j2V3D3A8ZfMr6zJ4CRfeJK6jtSJunYG-khVCR2DOOBs3Y-H1IUwzWX9kOAQfdydrONfvp0EfQ0tFdmCgst84Exp8A==",
                "facilitated_booking_available": True,
                "pnr_count": 1,
                "has_airport_change": False,
                "technical_stops": 0,
                "throw_away_ticketing": False,
                "hidden_city_ticketing": False,
                "virtual_interlining": False,
                "local_arrival": "2023-02-13T14:20:00.000Z",
                "utc_arrival": "2023-02-13T08:50:00.000Z",
                "local_departure": "2023-02-13T12:00:00.000Z",
                "utc_departure": "2023-02-13T06:30:00.000Z"
            },
            {
                "id": "071104914bc800003819ad35_0",
                "flyFrom": "DEL",
                "flyTo": "BOM",
                "cityFrom": "New Delhi",
                "cityCodeFrom": "DEL",
                "cityTo": "Mumbai",
                "cityCodeTo": "BOM",
                "countryFrom": {
                    "code": "IN",
                    "name": "India"
                },
                "countryTo": {
                    "code": "IN",
                    "name": "India"
                },
                "nightsInDest": "None",
                "quality": 82.99992,
                "distance": 1139.47,
                "duration": {
                    "departure": 9000,
                    "return": 0,
                    "total": 9000
                },
                "price": 51,
                "conversion": {
                    "EUR": 51
                },
                "bags_price": {
                    "1": 0
                },
                "baglimit": {
                    "hand_height": 38,
                    "hand_length": 57,
                    "hand_weight": 7,
                    "hand_width": 20,
                    "hold_dimensions_sum": 158,
                    "hold_height": 52,
                    "hold_length": 78,
                    "hold_weight": 15,
                    "hold_width": 28
                },
                "availability": {
                    "seats": 2
                },
                "airlines": [
                    "6E"
                ],
                "route": [
                    {
                        "id": "071104914bc800003819ad35_0",
                        "combination_id": "071104914bc800003819ad35",
                        "flyFrom": "DEL",
                        "flyTo": "BOM",
                        "cityFrom": "New Delhi",
                        "cityCodeFrom": "DEL",
                        "cityTo": "Mumbai",
                        "cityCodeTo": "BOM",
                        "airline": "6E",
                        "flight_no": 2112,
                        "operating_carrier": "6E",
                        "operating_flight_no": "2112",
                        "fare_basis": "",
                        "fare_category": "M",
                        "fare_classes": "X",
                        "fare_family": "",
                        "return": 0,
                        "bags_recheck_required": False,
                        "vi_connection": False,
                        "guarantee": False,
                        "equipment": "None",
                        "vehicle_type": "aircraft",
                        "local_arrival": "2023-02-12T07:15:00.000Z",
                        "utc_arrival": "2023-02-12T01:45:00.000Z",
                        "local_departure": "2023-02-12T04:45:00.000Z",
                        "utc_departure": "2023-02-11T23:15:00.000Z"
                    }
                ],
                "booking_token": "Epl4FgPNEdseHwPqg7A4xlim1wjHWRZOVgpN9C0vLaB0x0SLZx7k7713psD3HM2M3K_2v1f5VJcmS6IQBAvUff6Io2GCI7IblKQSLPbfmCZJ_UvkA8dPxuN4mbc9UT1VFYY65keN0vBuvcePpnU3zhh9TiOeiBesx_djrNxi3NrZ8zrRYCRhdmGSq4DdVwkCPb8rNQzxbf8DB5sl6KF8v_8piBVVMUM6HIRrRik4umW7wI0swZmSUdSWr8D_BOJrYVpurwkjvVDB1Nsp36MppS8GsAKNHOGUac9NS2l4_mbLSwEYgQ3i8cOuUpFr1xCJ7MDX4olmQA6kVEUt1eHqPHbrtEQc0UH3oDScK7vbiya_IFFw1wXL8NJk-XGxBxS9sVFB_uGmQSi1mjLGdZivWA-U3Yc4eknwjrIZH_RVlbVi9JCwgOKtgqhvcgQ2cRGOfo2R1hcq1mIRVQgwX1zSZpJm62HlmDFb07_La5UmuDZk3XonpdxFl-Bz6brKnmPo-HCYYwIEuFpmmoE_UX382Z1iNLVRXw7fUU-gT2NPJhPo=",
                "deep_link": "https://www.kiwi.com/deep?affilid=apoorvflightsearch&currency=EUR&flightsId=071104914bc800003819ad35_0&from=DEL&lang=en&passengers=1&to=BOM&booking_token=E2Me3q5Q0Hl0QDYPRNNlB3U4wFcoqV2oJ_1PCGn2V2nnspWeIebqufLsjtEjOBrCRN6BFDdGmSIiQpIgge7NkRt_7DdAwYPoLobemIbVRZaMiK6a5dNgPP0kxSBSO3Vvf8JQhCVbo2sJcRbP3ojbXhLBkRJcTRaKXh2shI8Vf6lm1UoQk6zAXGS4XGV5pUCPR3sejo8rfF_j3ugokQH4uCzr4_hE-dUJ9LPvIXTfvKIWjNTpV2jXg995_pxVIOh6pHX68Qq7kjMGvJzG7rxeO0a5jeSRqoYsPxR0nYyjd6GAMf7wTVlekhRaqh7IAsr6wn2uR3qUeCiS9onF6CJOEJLQGCoSPGhTr7ue_IzFByXibEDYrfDEL4mZGKqYjdZwJ8afqpB7PZyruP85MCruvhdJpLYJkdLPnyje5ZK4lwdE=",
                "facilitated_booking_available": True,
                "pnr_count": 1,
                "has_airport_change": False,
                "technical_stops": 0,
                "throw_away_ticketing": False,
                "hidden_city_ticketing": False,
                "virtual_interlining": False,
                "local_arrival": "2023-02-12T07:15:00.000Z",
                "utc_arrival": "2023-02-12T01:45:00.000Z",
                "local_departure": "2023-02-12T04:45:00.000Z",
                "utc_departure": "2023-02-11T23:15:00.000Z"
            },
            {
                "id": "071104914bc70000e9b72c89_0",
                "flyFrom": "DEL",
                "flyTo": "BOM",
                "cityFrom": "New Delhi",
                "cityCodeFrom": "DEL",
                "cityTo": "Mumbai",
                "cityCodeTo": "BOM",
                "countryFrom": {
                    "code": "IN",
                    "name": "India"
                },
                "countryTo": {
                    "code": "IN",
                    "name": "India"
                },
                "nightsInDest": "None",
                "quality": 82.99992,
                "distance": 1139.47,
                "duration": {
                    "departure": 9000,
                    "return": 0,
                    "total": 9000
                },
                "price": 51,
                "conversion": {
                    "EUR": 51
                },
                "bags_price": {
                    "1": 0
                },
                "baglimit": {
                    "hand_height": 38,
                    "hand_length": 57,
                    "hand_weight": 7,
                    "hand_width": 20,
                    "hold_dimensions_sum": 158,
                    "hold_height": 52,
                    "hold_length": 78,
                    "hold_weight": 15,
                    "hold_width": 28
                },
                "availability": {
                    "seats": 2
                },
                "airlines": [
                    "6E"
                ],
                "route": [
                    {
                        "id": "071104914bc70000e9b72c89_0",
                        "combination_id": "071104914bc70000e9b72c89",
                        "flyFrom": "DEL",
                        "flyTo": "BOM",
                        "cityFrom": "New Delhi",
                        "cityCodeFrom": "DEL",
                        "cityTo": "Mumbai",
                        "cityCodeTo": "BOM",
                        "airline": "6E",
                        "flight_no": 2112,
                        "operating_carrier": "6E",
                        "operating_flight_no": "2112",
                        "fare_basis": "",
                        "fare_category": "M",
                        "fare_classes": "R",
                        "fare_family": "",
                        "return": 0,
                        "bags_recheck_required": False,
                        "vi_connection": False,
                        "guarantee": False,
                        "equipment": "None",
                        "vehicle_type": "aircraft",
                        "local_arrival": "2023-02-11T07:15:00.000Z",
                        "utc_arrival": "2023-02-11T01:45:00.000Z",
                        "local_departure": "2023-02-11T04:45:00.000Z",
                        "utc_departure": "2023-02-10T23:15:00.000Z"
                    }
                ],
                "booking_token": "EZ5JLeef8wmvd1wP5w5xBsZ3DQsRMPTOeE64f3KcVtPrA_FhCNWT7KecP9wKYFgGMhDnLovtoCQJcphHjUVM33qdnjuAcjPdxwlTO6RtkZn_lGqkuicHnR5t_z5TQ9o0vAcxFJT7_ZT85IsFOi9OiPfluLvW5ItWigb6rDJSz4ycNw5iJLozSATcV-U6YDC8Mxs_JZHcLQfWlOzLkv-ZPSqdD8ezdMZ6CfKPVWts2yVWpHytelJ2AGzyCSX3CtrOFpisDsPsDrfYreQDwzJW8E0_VEHrygfi3p8Ovo3QbyRmJtUB10L3I4gkkGfkf3DrRaMuJFQIqryyCoA309L7o0lLb9laiGhP9qj_vUvU7YzXE7EEM3b3uqD4MJvSFXShmEB3Q9T2PRILb_GiGrNOl9HZjv-Wil8-CHBfhGqg-4Yzezrbk9Bd36h8_-fu48pOd788qnZngh6fKb3fuv8URY3oJvxtuNlzkDXcqlxBS60geoTqlpnRy02VwUrKAIN1g-SKeH5n7qg3MwR6s3hZGBtMD4_K5BSkfuEpz-YAOaw0=",
                "deep_link": "https://www.kiwi.com/deep?affilid=apoorvflightsearch&currency=EUR&flightsId=071104914bc70000e9b72c89_0&from=DEL&lang=en&passengers=1&to=BOM&booking_token=E0HEICNOe02ccFTtu-y4swl4w14wm8szt9uxJBMBTQ5hj4tmifLSySco8ZP6jHgOKKACYEBmDBc1aYQU1j1eBRY1tHE8H8qoxWzIo73swL8FqaR9tOeXOSW7Qqd2hMcZd3DKLsim8hHdA8n6AvbiKSqvczE5NqZX2eeEcwJ_bcNAlsEs_1EfMoPyi2If2Zr_kEjG4V8qlwg0xAsOUYwOXCwc4aylXpioLqZ2Kst9DYi_2vUdVpAxOckf6VqEY_pFle2kviLtQGy-jNeFgPN1vthUmDKt3Jrbe5U8HKTU6qgU7xlzh5UYAxuJZtSSuaFEYM0XQsnVaUz0n4lwxGnmn8EXbZa6w4ji5wT_hFgAp47AJRdtB06Uc-Yac-pZHbin3Tf5lXV4NckmfTsvgjJt9DV8vkHJKyZPydmMj5xrp7C8=",
                "facilitated_booking_available": True,
                "pnr_count": 1,
                "has_airport_change": False,
                "technical_stops": 0,
                "throw_away_ticketing": False,
                "hidden_city_ticketing": False,
                "virtual_interlining": False,
                "local_arrival": "2023-02-11T07:15:00.000Z",
                "utc_arrival": "2023-02-11T01:45:00.000Z",
                "local_departure": "2023-02-11T04:45:00.000Z",
                "utc_departure": "2023-02-10T23:15:00.000Z"
            },
            {
                "id": "07111c024bc80000526a7bdb_0",
                "flyFrom": "DEL",
                "flyTo": "VNS",
                "cityFrom": "New Delhi",
                "cityCodeFrom": "DEL",
                "cityTo": "Varanasi",
                "cityCodeTo": "VNS",
                "countryFrom": {
                    "code": "IN",
                    "name": "India"
                },
                "countryTo": {
                    "code": "IN",
                    "name": "India"
                },
                "nightsInDest": "None",
                "quality": 75.333275,
                "distance": 667.75,
                "duration": {
                    "departure": 5100,
                    "return": 0,
                    "total": 5100
                },
                "price": 52,
                "conversion": {
                    "EUR": 52
                },
                "bags_price": {
                    "1": 0
                },
                "baglimit": {
                    "hand_height": 36,
                    "hand_length": 54,
                    "hand_weight": 7,
                    "hand_width": 18,
                    "hold_dimensions_sum": 158,
                    "hold_height": 52,
                    "hold_length": 78,
                    "hold_weight": 15,
                    "hold_width": 28
                },
                "availability": {
                    "seats": 2
                },
                "airlines": [
                    "SG"
                ],
                "route": [
                    {
                        "id": "07111c024bc80000526a7bdb_0",
                        "combination_id": "07111c024bc80000526a7bdb",
                        "flyFrom": "DEL",
                        "flyTo": "VNS",
                        "cityFrom": "New Delhi",
                        "cityCodeFrom": "DEL",
                        "cityTo": "Varanasi",
                        "cityCodeTo": "VNS",
                        "airline": "SG",
                        "flight_no": 958,
                        "operating_carrier": "SG",
                        "operating_flight_no": "958",
                        "fare_basis": "ASWB",
                        "fare_category": "M",
                        "fare_classes": "A",
                        "fare_family": "",
                        "return": 0,
                        "bags_recheck_required": False,
                        "vi_connection": False,
                        "guarantee": False,
                        "equipment": "None",
                        "vehicle_type": "aircraft",
                        "local_arrival": "2023-02-12T20:55:00.000Z",
                        "utc_arrival": "2023-02-12T15:25:00.000Z",
                        "local_departure": "2023-02-12T19:30:00.000Z",
                        "utc_departure": "2023-02-12T14:00:00.000Z"
                    }
                ],
                "booking_token": "E72QqJdSSQjiroXekyuv6Vhv4aV4h694n6cLe2X7lELF1-ESfIve60bfihNXYN6IzRUkbOH4KUBM66EDIDvO1b64PoBWBt3QXXyCa_0dpA1mH6t9OsmMJcFbRcVXhPrj59pOLL3tFPlUVW002rn2cfKdBqoJoMomGGoKzTeEfo-a7ELuRP2kdBlafPWHA1ObisfTyIb40PmV9LK5DJ7MpAEg8dBCtEVBC9hmOtwVCKCrsoWSi5TYDGwup7mgscX2PPG2YHXamooXWq0gcobNNJ9GHCaejvva6eDh2uWV6mzY_E6oV4ZzS23Drw_JnlU3nugenCuMo93DmB4SFdMSGozWYyzR7pHaaF4a8YNfdQjSFeNAlL-75ZhcLFJDNZzPEGiC3pMQjXdGPBSgFFun2CCMSz23T1JMtc7myUnQiE5JNSZzcLoaUeBwWrDyPdvIaqZeVHQVdCellyEeVTqin9YmfucvEcI9SH6o62Yar7zcgRn9bHvYDIuJNB2fuYmmgRMUYkJ7oV7sMK2qiDcSVn2OmXdFDQIFQ-9cPyS3sPvg=",
                "deep_link": "https://www.kiwi.com/deep?affilid=apoorvflightsearch&currency=EUR&flightsId=07111c024bc80000526a7bdb_0&from=DEL&lang=en&passengers=1&to=VNS&booking_token=EHZmWfNwh-lONeXmBkwFY_XOkza4MuIw-2R_9eSixQUYuBdLHEZOByGEcxjM8tW_k-CVg3SPgRUGg44A3Iy0OBtj6nOncThamFNOZjTHqX1zaJxDA7ltUy-T0NCZHidIMfKNUaWPzgLfDBEh_9E_vWHyuXCIg9p1LXum5Yn-9fwSj7KqQVrW-AHcHm3Aq6AL89G_GxjAUjvHLREbYlHweh79shgs57o_AZcSPX8jYN4hM3PNnzGWXqdSncLLlaekE_JpHP3J8hytMMCuT7ykPXbkzN_Rb3bkWaElXAQN8Udti19gAmzbh-e7fsgaErPUnUdBarUUFvPyfgjcLmQwE98pOjl7idXarIKabavUV_uWHKQCsI5OfbLgfzXxVs3ufy271Ve1xIFxWC6omdw8lX2-Sd90nys3pdXzjfGDT-J4=",
                "facilitated_booking_available": True,
                "pnr_count": 1,
                "has_airport_change": False,
                "technical_stops": 0,
                "throw_away_ticketing": False,
                "hidden_city_ticketing": False,
                "virtual_interlining": False,
                "local_arrival": "2023-02-12T20:55:00.000Z",
                "utc_arrival": "2023-02-12T15:25:00.000Z",
                "local_departure": "2023-02-12T19:30:00.000Z",
                "utc_departure": "2023-02-12T14:00:00.000Z"
            },
            {
                "id": "07111b744bc800008de51e38_0",
                "flyFrom": "DEL",
                "flyTo": "BHO",
                "cityFrom": "New Delhi",
                "cityCodeFrom": "DEL",
                "cityTo": "Bhopal",
                "cityCodeTo": "BHO",
                "countryFrom": {
                    "code": "IN",
                    "name": "India"
                },
                "countryTo": {
                    "code": "IN",
                    "name": "India"
                },
                "nightsInDest": "None",
                "quality": 75.99994,
                "distance": 588.1,
                "duration": {
                    "departure": 5400,
                    "return": 0,
                    "total": 5400
                },
                "price": 52,
                "conversion": {
                    "EUR": 52
                },
                "bags_price": {
                    "1": 0
                },
                "baglimit": {
                    "hand_height": 35,
                    "hand_length": 55,
                    "hand_weight": 8,
                    "hand_width": 25,
                    "hold_dimensions_sum": 158,
                    "hold_height": 52,
                    "hold_length": 78,
                    "hold_weight": 25,
                    "hold_width": 28,
                    "personal_item_height": 20,
                    "personal_item_length": 40,
                    "personal_item_weight": 5,
                    "personal_item_width": 10
                },
                "availability": {
                    "seats": "None"
                },
                "airlines": [
                    "AI"
                ],
                "route": [
                    {
                        "id": "07111b744bc800008de51e38_0",
                        "combination_id": "07111b744bc800008de51e38",
                        "flyFrom": "DEL",
                        "flyTo": "BHO",
                        "cityFrom": "New Delhi",
                        "cityCodeFrom": "DEL",
                        "cityTo": "Bhopal",
                        "cityCodeTo": "BHO",
                        "airline": "AI",
                        "flight_no": 435,
                        "operating_carrier": "AI",
                        "operating_flight_no": "435",
                        "fare_basis": "TIP",
                        "fare_category": "M",
                        "fare_classes": "T",
                        "fare_family": "",
                        "return": 0,
                        "bags_recheck_required": False,
                        "vi_connection": False,
                        "guarantee": False,
                        "equipment": "None",
                        "vehicle_type": "aircraft",
                        "local_arrival": "2023-02-12T07:25:00.000Z",
                        "utc_arrival": "2023-02-12T01:55:00.000Z",
                        "local_departure": "2023-02-12T05:55:00.000Z",
                        "utc_departure": "2023-02-12T00:25:00.000Z"
                    }
                ],
                "booking_token": "EQq0Kw4v2HpDrJhkzu3U3UPYOQ8c1QOz8NJEIZPlXqfEbGHioK0QoypYdkjrq1AlAuKLFj426Z6jEMAZnn1BP9YRMpcP44A9r6KWQc4bAlwXNPZ2VeL-lVYjbrvAJXQ1Xj-jQpggdkv2TKSjNRA30iBCdGY0EZfs_H7IfF8HsG7-hBQvi6-7wVt60Hl2uGsDCBQakrHeBieLCR6nAFGFKQ-OALkqn1nuFz9IvjdhjvB53t_Wk13krNoLBachTfKfqWmp8111MfYyhA-dZrSyxp-qe0pv6U94dlZ-jzC0gd2R3tA2jSKcnqIFwh1F9nYpv2kaRHjz2LuBNfe-XCUOMXeHPuciGaS1dh8reGl2BYcex9kWRLt_Lq9SviPhFTFydovg7NPz0VhH8v6v3CVsMWgxyEIXXax4fifEXBp59DIaCAsaLSdwBYeZp9urQcUBeHWir3_VBhjl31VifmJRRZTxYkRKWy9CxQl_JuY4KRx7v3anSiCrEzKKCKOu9TmE_dwbKsH3L73Xm2FZQfB6tjkNvnw85brSnJAwE5irQm9MWZukos3Q3ys9rwoTLKXEaosn8pWinOWHzXATSmH7gRhaU3y9UnIgsJOoght9Q6jI=",
                "deep_link": "https://www.kiwi.com/deep?affilid=apoorvflightsearch&currency=EUR&flightsId=07111b744bc800008de51e38_0&from=DEL&lang=en&passengers=1&to=BHO&booking_token=E4rcxqWVQtoy29Piv93bxXUPdt9cm2PiiaNzdEUzobiZtmsyPPNPQP41LQXosv9eNupBl12My0GIb56_3mbl0lC_50QBcCLPIFXWpc0TrvZt686bNanjDcBERcAHX6gMbCOoBXjPR_YS1Y4WzxEzbUPdnBBbTg56-xOF1VKaytm8ICBDbQZUeYZcMJQzdqBsUyn8sENT_kdmqFIbfOfkc0ROCRCAL2FnU4u2DN9zi6ivo85K8j1L9GmiQVPOpEqrPvkRCKbr8uh9ybpKmQah-8Cq5FUlGSwntocfSeekXke88GfcJKoa7Ej5z9e2VyXvniMKQfT5k3X2boCFS5tkIXOEGoY4Ys7lMEN0LAWFWILu7wPNsYGJKWpGARvO_mm-9_1pBqLk_34EqLvEUpaPHF0_VsGyzhWQ5ezygnj4rbdbKsW7NT1T6Z8LqNvHZT1Kap9WYV9naaDxpVPpNDmbhkA==",
                "facilitated_booking_available": True,
                "pnr_count": 1,
                "has_airport_change": False,
                "technical_stops": 0,
                "throw_away_ticketing": False,
                "hidden_city_ticketing": False,
                "virtual_interlining": False,
                "local_arrival": "2023-02-12T07:25:00.000Z",
                "utc_arrival": "2023-02-12T01:55:00.000Z",
                "local_departure": "2023-02-12T05:55:00.000Z",
                "utc_departure": "2023-02-12T00:25:00.000Z"
            },
            {
                "id": "071154a84bc90000dabee44b_0",
                "flyFrom": "DEL",
                "flyTo": "KBK",
                "cityFrom": "New Delhi",
                "cityCodeFrom": "DEL",
                "cityTo": "Kushinagar",
                "cityCodeTo": "",
                "countryFrom": {
                    "code": "IN",
                    "name": "India"
                },
                "countryTo": {
                    "code": "IN",
                    "name": "India"
                },
                "nightsInDest": "None",
                "quality": 76.666605,
                "distance": 699.93,
                "duration": {
                    "departure": 5700,
                    "return": 0,
                    "total": 5700
                },
                "price": 52,
                "conversion": {
                    "EUR": 52
                },
                "bags_price": {
                    "1": 0
                },
                "baglimit": {
                    "hand_height": 36,
                    "hand_length": 54,
                    "hand_weight": 7,
                    "hand_width": 18,
                    "hold_dimensions_sum": 158,
                    "hold_height": 52,
                    "hold_length": 78,
                    "hold_weight": 15,
                    "hold_width": 28
                },
                "availability": {
                    "seats": 1
                },
                "airlines": [
                    "SG"
                ],
                "route": [
                    {
                        "id": "071154a84bc90000dabee44b_0",
                        "combination_id": "071154a84bc90000dabee44b",
                        "flyFrom": "DEL",
                        "flyTo": "KBK",
                        "cityFrom": "New Delhi",
                        "cityCodeFrom": "DEL",
                        "cityTo": "Kushinagar",
                        "cityCodeTo": "None",
                        "airline": "SG",
                        "flight_no": 2987,
                        "operating_carrier": "SG",
                        "operating_flight_no": "2987",
                        "fare_basis": "USAV",
                        "fare_category": "M",
                        "fare_classes": "U",
                        "fare_family": "",
                        "return": 0,
                        "bags_recheck_required": False,
                        "vi_connection": False,
                        "guarantee": False,
                        "equipment": "None",
                        "vehicle_type": "aircraft",
                        "local_arrival": "2023-02-13T12:35:00.000Z",
                        "utc_arrival": "2023-02-13T07:05:00.000Z",
                        "local_departure": "2023-02-13T11:00:00.000Z",
                        "utc_departure": "2023-02-13T05:30:00.000Z"
                    }
                ],
                "booking_token": "EOwpm54KR7uPkJ5iuLAyiysbcHrLnEoFOYcpaf-nI2prPNwmRRqOqlsaNNzzc0UMBuEF_wigOQGjpSUewGeoVKMfa2sPbKkHuXi2vvprcPz3o2J9ljfGYtWf-giBH6ciZtTZM5LrjXAorxEwgbUzbxZTgO5Xcnn0BURsE3QpQQZQYZChQIT7yXJi_F0-ZaoUWyvPmuUxna34cvpN3d81zLwcjkN-X4eY_JGpzG6nLX1vgykwwjACRtzKID2VBnsW5YexajOXZXAKEHy7KhU7EwUIvQ3-zBfozqUDUNPA4AdD7rDbmG8vgg8yEIlLf3kGXy-HvUWrcNixhzcrjhzk-7C09DcxHseoJgNJktzxnOufLT2aneij55m0T75prZaTBqOrZvhaT8O0Bz822h4PEygFxeJBQn5F0G8MJAgCNOLrCh4aRQEpJQAoQXObRfHkdz7Lc3RKHxLptnaKY8Q0KwdZYTltijMwjomTOizx7qW9wJWMr81Huhh5vOJLboszhigYzw6upMhW4A9JENVP3I8UNrYM25BH6kkUXSuUoTiYS7c98gtzCgVuSdDk31-Qf",
                "deep_link": "https://www.kiwi.com/deep?affilid=apoorvflightsearch&currency=EUR&flightsId=071154a84bc90000dabee44b_0&from=DEL&lang=en&passengers=1&to=KBK&booking_token=EupfAdXeucbIYC5L3CUKqt0iDcC1DXxWUegnRsZOxehTDYT44tW8ox8bI_oZIQzmyPytyr4MRtgCvdSXtjrKK_AmhOsRHXK3MsXCfHMbOHv0lZ0jog_hM6vUhrDLuAe34DGqr6RPilXAz11wJELfgUEMJ883tFR6zYrSGkVxOhLvqYNm8Xv9MCsIcDW_2kHguyYy522-mfPZc8k8PP8RVEpRvqaZaRspUQOz8xftX4Njaunq4ySYm9JAOCKiwN9t8YCpz-wes99kSzmgJfdkij0-3I3XUSQlUvWHtaVUFFYQx0amlI03QbpXm4ZStNRb28dRl6i-DHmwQkvnZZQ8ktDVpGia6XcYsCA2x0GalPBu3KaJFOlCI_8j5Cj2z7N98jmUIMuCLrKPiy8ZcYynpFkMql5adAaln7y9DqIVONHE=",
                "facilitated_booking_available": True,
                "pnr_count": 1,
                "has_airport_change": False,
                "technical_stops": 0,
                "throw_away_ticketing": False,
                "hidden_city_ticketing": False,
                "virtual_interlining": False,
                "local_arrival": "2023-02-13T12:35:00.000Z",
                "utc_arrival": "2023-02-13T07:05:00.000Z",
                "local_departure": "2023-02-13T11:00:00.000Z",
                "utc_departure": "2023-02-13T05:30:00.000Z"
            },
            {
                "id": "071104c24bc700009dde1a54_0",
                "flyFrom": "DEL",
                "flyTo": "LKO",
                "cityFrom": "New Delhi",
                "cityCodeFrom": "DEL",
                "cityTo": "Lucknow",
                "cityCodeTo": "LKO",
                "countryFrom": {
                    "code": "IN",
                    "name": "India"
                },
                "countryTo": {
                    "code": "IN",
                    "name": "India"
                },
                "nightsInDest": "None",
                "quality": 73.666615,
                "distance": 423.95,
                "duration": {
                    "departure": 3900,
                    "return": 0,
                    "total": 3900
                },
                "price": 53,
                "conversion": {
                    "EUR": 53
                },
                "bags_price": {
                    "1": 0
                },
                "baglimit": {
                    "hand_height": 35,
                    "hand_length": 55,
                    "hand_weight": 8,
                    "hand_width": 25,
                    "hold_dimensions_sum": 158,
                    "hold_height": 52,
                    "hold_length": 78,
                    "hold_weight": 25,
                    "hold_width": 28,
                    "personal_item_height": 20,
                    "personal_item_length": 40,
                    "personal_item_weight": 5,
                    "personal_item_width": 10
                },
                "availability": {
                    "seats": 1
                },
                "airlines": [
                    "AI"
                ],
                "route": [
                    {
                        "id": "071104c24bc700009dde1a54_0",
                        "combination_id": "071104c24bc700009dde1a54",
                        "flyFrom": "DEL",
                        "flyTo": "LKO",
                        "cityFrom": "New Delhi",
                        "cityCodeFrom": "DEL",
                        "cityTo": "Lucknow",
                        "cityCodeTo": "LKO",
                        "airline": "AI",
                        "flight_no": 811,
                        "operating_carrier": "AI",
                        "operating_flight_no": "811",
                        "fare_basis": "LIP",
                        "fare_category": "M",
                        "fare_classes": "L",
                        "fare_family": "",
                        "return": 0,
                        "bags_recheck_required": False,
                        "vi_connection": False,
                        "guarantee": False,
                        "equipment": "None",
                        "vehicle_type": "aircraft",
                        "local_arrival": "2023-02-11T19:45:00.000Z",
                        "utc_arrival": "2023-02-11T14:15:00.000Z",
                        "local_departure": "2023-02-11T18:40:00.000Z",
                        "utc_departure": "2023-02-11T13:10:00.000Z"
                    }
                ],
                "booking_token": "EQuEjBgEaOTz8HH_mP2ljzXwDL92eBfo3kwy0rWdmrSUHc3slOwu0ENDV3sIWMQ4etA0g3DLPxdbyUQvrmMFdoLkoAzZ0zQZYdb31YnHoKAk-kE2B-J_sSzOa2VVUvTuOOmMir239bTQ3Ds4wqOM8niaVeBxhvIEDRDPhmuaJcYOicTeuHZfUDYB5Amb4gJvtVEmX-fFdD8VIU_ntAA4dkvBDRa9No9-3D4fCoKMjftwRwNUanjU-h07A2iZD-FtFkON24Zu-_rBuddPlNOgBzMtYyngAWgTWDleMVLW4ibb8rTSITRfA_16rYovX6M-PtJcIG4iSpbhI-tammaUm4RjdtrL-lOJe-8iyuk5HxRW49ej3cgGoM9jgPjMzY47uDY5EFShjnNTh3jUcwS6VKW8m3fCf9mfkJH0oRu4cAYZ-cDjVYuINSBlAJ2LB5XcwsyP_T2pOnpAQXArFeSJO_gXkRx9QzeYbOiN8DX8v49WukRVPI-rqhMNdD6OfVozznMctxlKML9NtspTtDOZYQhd1KxUw29EeN6F9qMBo175ICJG0ES9KS4b-CfRMOJ6DXwe9j18nEiS-tsJzyy3aEyszOU5lPriR5EwWxWZUPD4=",
                "deep_link": "https://www.kiwi.com/deep?affilid=apoorvflightsearch&currency=EUR&flightsId=071104c24bc700009dde1a54_0&from=DEL&lang=en&passengers=1&to=LKO&booking_token=ETAQg2bDuZfglIXB08Iyjk6LDk7cHZsJqHDdYa3ca4NsNxqlGlWg1vJybiH4ip-AVNA9vrdRacUuCvEfpVsoi5RndEGcQb2ETDKVEB4ZI0uFMtq4PFwVrmPLX5dKMyFCa-ED25IQUAaWeOGWPkItiVYq3fWhg_S7Et6AIzf26DOnH3aiWoryi3VAfYEnIFILcyvOAGlEdfSf-2eEuLfArZcyZnyx_Bw2Wn8ouK8HMkR1QUE8SU8ATLQX-PPgCluci33RtjOaYqFWsdiYE05RdP2ufnE0DpC--XIhlpavIaQ_aRXA4pIZCo4YQSvpn9A_KgRi4sZuU9maXqS3vsyYsQZmzMGoQdQUR_XEqsrq1axBjjMqf_3FngGWbj7xSxv-HRqQmrZZqrqHUF-trxsNL9qRDJWw1uYO7XkKrf0gGdqX1857aMwyyCC_KAqcZ0BmvIykiKh3LDI0j37xvrNE87w==",
                "facilitated_booking_available": True,
                "pnr_count": 1,
                "has_airport_change": False,
                "technical_stops": 0,
                "throw_away_ticketing": False,
                "hidden_city_ticketing": False,
                "virtual_interlining": False,
                "local_arrival": "2023-02-11T19:45:00.000Z",
                "utc_arrival": "2023-02-11T14:15:00.000Z",
                "local_departure": "2023-02-11T18:40:00.000Z",
                "utc_departure": "2023-02-11T13:10:00.000Z"
            },
            {
                "id": "071104c24bc90000b7c92d54_0",
                "flyFrom": "DEL",
                "flyTo": "LKO",
                "cityFrom": "New Delhi",
                "cityCodeFrom": "DEL",
                "cityTo": "Lucknow",
                "cityCodeTo": "LKO",
                "countryFrom": {
                    "code": "IN",
                    "name": "India"
                },
                "countryTo": {
                    "code": "IN",
                    "name": "India"
                },
                "nightsInDest": "None",
                "quality": 74.999945,
                "distance": 423.95,
                "duration": {
                    "departure": 4500,
                    "return": 0,
                    "total": 4500
                },
                "price": 53,
                "conversion": {
                    "EUR": 53
                },
                "bags_price": {
                    "1": 0
                },
                "baglimit": {
                    "hand_height": 38,
                    "hand_length": 57,
                    "hand_weight": 7,
                    "hand_width": 20,
                    "hold_dimensions_sum": 158,
                    "hold_height": 52,
                    "hold_length": 78,
                    "hold_weight": 15,
                    "hold_width": 28
                },
                "availability": {
                    "seats": 2
                },
                "airlines": [
                    "6E"
                ],
                "route": [
                    {
                        "id": "071104c24bc90000b7c92d54_0",
                        "combination_id": "071104c24bc90000b7c92d54",
                        "flyFrom": "DEL",
                        "flyTo": "LKO",
                        "cityFrom": "New Delhi",
                        "cityCodeFrom": "DEL",
                        "cityTo": "Lucknow",
                        "cityCodeTo": "LKO",
                        "airline": "6E",
                        "flight_no": 2107,
                        "operating_carrier": "6E",
                        "operating_flight_no": "2107",
                        "fare_basis": "",
                        "fare_category": "M",
                        "fare_classes": "J",
                        "fare_family": "",
                        "return": 0,
                        "bags_recheck_required": False,
                        "vi_connection": False,
                        "guarantee": False,
                        "equipment": "None",
                        "vehicle_type": "aircraft",
                        "local_arrival": "2023-02-13T09:45:00.000Z",
                        "utc_arrival": "2023-02-13T04:15:00.000Z",
                        "local_departure": "2023-02-13T08:30:00.000Z",
                        "utc_departure": "2023-02-13T03:00:00.000Z"
                    }
                ],
                "booking_token": "EPL-8A58FMzUs_OZjy-xnd2AmWgWEBFzsc628y5vCDa0NxwopeW5X2vyuhXdd36vwxvMj7PUNHSWDoLqeJSYZXC_jjllRcZhfWDT_8xnp63BWyBQcZTxMZJTx8tTXi7oUCJB6rypkENFjb5D6OHRRs7YeL0caH90vRK9eZ-cZlLc18PGwyHpnQs-pfjqLzqyL8xKw-tPE6XFf9NOe2QU7IkRg5SepSIMvcmQOAFfoA-PSleNTKeIAoPw_cb-vMFyviKUTAUMqMNJfFGi1Fkjv7R1KvyxbtUciVD5gZFMRKgKTK-aMD5DQSJ1JDx4v3mSuXyL-K5w4cOQvzDNCruDW4T-p4mdOmz3mqgzSzb_yuvJfstZzl8D1W3TKKA1rlfdmRXMyjAvVpQNuMfeDrHOuLhtQ0T7u_3Pt-vaYe530TR_r04mloeu9iAi80ccC7HqIw-Jv-T42aIHqucF_FyiQ6IKfw0yitxD6osXFoLoPilbGs1HUVea8nuLODKdRJTs4mg1vLWJv7Sezo4Utv0w-b2d-dIae3IeZF_2YC2HCYyc=",
                "deep_link": "https://www.kiwi.com/deep?affilid=apoorvflightsearch&currency=EUR&flightsId=071104c24bc90000b7c92d54_0&from=DEL&lang=en&passengers=1&to=LKO&booking_token=E4PwupMcom3ZbS8Y2_j9IcxLD_Njv7E6n6z5oVsq88FEkvS9a3wA7E1a-i70oA9Va8vaUnKwY8vdpjcU52kwrT_jY2B5ECfO5HVXWKjFqbOWdjeJ6CrS5c5YwKKWTM-VtyNSh5cIpU5ybPDlWy2pWVoOUvabqQBSBLtLf4u2kuqbmPs_oVgmRRY-1wAWoFJ_YGEqwfX8rPrm8AHhCZwhHlBM2WcfbUqWtHad2vEatf1xKfsWq375oKr_PR_Cu-HQ_sJTzGLn3GveXbjV8YlY80lKzBXeIStD72h15qp7w8SAu8jzkv1gcpbVg-PhzvMi11VTctjtdmR18hso92xShj2NpAsq_SmS1Z269xZXBPdF8NqS9POsvHjWGk1dRLJAOVn1cAbU3BuE_alPMey1CBzssCCV5HOjdplWRgCLxllA=",
                "facilitated_booking_available": True,
                "pnr_count": 1,
                "has_airport_change": False,
                "technical_stops": 0,
                "throw_away_ticketing": False,
                "hidden_city_ticketing": False,
                "virtual_interlining": False,
                "local_arrival": "2023-02-13T09:45:00.000Z",
                "utc_arrival": "2023-02-13T04:15:00.000Z",
                "local_departure": "2023-02-13T08:30:00.000Z",
                "utc_departure": "2023-02-13T03:00:00.000Z"
            },
            {
                "id": "07111b744bc900001fe66ac0_0",
                "flyFrom": "DEL",
                "flyTo": "BHO",
                "cityFrom": "New Delhi",
                "cityCodeFrom": "DEL",
                "cityTo": "Bhopal",
                "cityCodeTo": "BHO",
                "countryFrom": {
                    "code": "IN",
                    "name": "India"
                },
                "countryTo": {
                    "code": "IN",
                    "name": "India"
                },
                "nightsInDest": "None",
                "quality": 76.99994,
                "distance": 588.1,
                "duration": {
                    "departure": 5400,
                    "return": 0,
                    "total": 5400
                },
                "price": 53,
                "conversion": {
                    "EUR": 53
                },
                "bags_price": {
                    "1": 0
                },
                "baglimit": {
                    "hand_height": 38,
                    "hand_length": 57,
                    "hand_weight": 7,
                    "hand_width": 20,
                    "hold_dimensions_sum": 158,
                    "hold_height": 52,
                    "hold_length": 78,
                    "hold_weight": 15,
                    "hold_width": 28
                },
                "availability": {
                    "seats": 2
                },
                "airlines": [
                    "6E"
                ],
                "route": [
                    {
                        "id": "07111b744bc900001fe66ac0_0",
                        "combination_id": "07111b744bc900001fe66ac0",
                        "flyFrom": "DEL",
                        "flyTo": "BHO",
                        "cityFrom": "New Delhi",
                        "cityCodeFrom": "DEL",
                        "cityTo": "Bhopal",
                        "cityCodeTo": "BHO",
                        "airline": "6E",
                        "flight_no": 6022,
                        "operating_carrier": "6E",
                        "operating_flight_no": "6022",
                        "fare_basis": "R0IP",
                        "fare_category": "M",
                        "fare_classes": "X",
                        "fare_family": "",
                        "return": 0,
                        "bags_recheck_required": False,
                        "vi_connection": False,
                        "guarantee": False,
                        "equipment": "None",
                        "vehicle_type": "aircraft",
                        "local_arrival": "2023-02-13T08:20:00.000Z",
                        "utc_arrival": "2023-02-13T02:50:00.000Z",
                        "local_departure": "2023-02-13T06:50:00.000Z",
                        "utc_departure": "2023-02-13T01:20:00.000Z"
                    }
                ],
                "booking_token": "EeC5ZdmFaj7US8kFz9czSMkCqZms7VbBEs2bqDxgJ931xZYCUy96qtd4Q4YPEgJXQjsxEVj96NeOijrhJXCrKi_6n9PscLSteXAYi__i9ffxiCf4VGwze7NsQCReJDBlJwXycyRIIiYYV2N0mzNWNCJZl4-AIyYanj_53N2EqgEl4tWB6_J6s-fd0sF1-e9zpccdr0y_Z9oVQ1DdbgpzbOOM-z-GWkqWkk1TpMhE847A2kg9FdETqpsSYZTvy3cr6lhJ9gq0okPCBau-_klONITQ9vUIDE6a2PDGwew4mpngtaXd3aOdI6itEqbQGGKfr8N2woYlSqPmkNrfqFd9FG0ctJ1vRcQ5wHtgzn9W0K3GqV7YTxnNMJTlxnpsH2pwW1662_fPY1aY7nLRlPREN-3tLsf4-dDWDqvsw_GSC83Qi21MnfKuOGxBCBoNgBOPmYbAqPK9pEjNCNVfC8eNE3I1t6Wmvb_g9N3_LMlIe0Y9rtdxy6YTW8MGRSy4BvkDL1xE8HPFyNGJHe5Kq9rmyfLC5VEcNoHKa3doxHe_O0xI=",
                "deep_link": "https://www.kiwi.com/deep?affilid=apoorvflightsearch&currency=EUR&flightsId=07111b744bc900001fe66ac0_0&from=DEL&lang=en&passengers=1&to=BHO&booking_token=EEqiM-dZm97I05ZY6KuUUfkiqIIMO0RLHzvxsTWheykxK4AAsJzJ_nkXVoIqz9ce40mbW34N4ed5_VPsDIXqZXt6zUyqdIaQr110qKK7gDVNEZcAi2qHaYzNZ2t6OJK3apP-wLQxwdmuzRGpLzmeHj4B_eF5RqAZAnKnl5QsNuSHMAtfqXG-YFlSv0KD6IYyhrklB6Qxdg6gAdo_aFB1Q8Kgdc_UsuwThY4_QjGbLNCwQPLRim_rj0ThwSQDU6mm8ckugN9xjy-zu5pQBo_-D0XOG_0lC_GV7tjXrWh8FaEEJf3SJtw1taproN6xzd_A22u3nsTU5NNKo1x91TrmVDE8eFATok_EPJTkS-NyQ9Qjbotrk9RQ0XTX2uVtirZhiOOl7Dx25gthVpx74pbyAfo4WuqCHaMQZ42EX_V1vD7w=",
                "facilitated_booking_available": True,
                "pnr_count": 1,
                "has_airport_change": False,
                "technical_stops": 0,
                "throw_away_ticketing": False,
                "hidden_city_ticketing": False,
                "virtual_interlining": False,
                "local_arrival": "2023-02-13T08:20:00.000Z",
                "utc_arrival": "2023-02-13T02:50:00.000Z",
                "local_departure": "2023-02-13T06:50:00.000Z",
                "utc_departure": "2023-02-13T01:20:00.000Z"
            },
            {
                "id": "07111b744bc900007a04a029_0",
                "flyFrom": "DEL",
                "flyTo": "BHO",
                "cityFrom": "New Delhi",
                "cityCodeFrom": "DEL",
                "cityTo": "Bhopal",
                "cityCodeTo": "BHO",
                "countryFrom": {
                    "code": "IN",
                    "name": "India"
                },
                "countryTo": {
                    "code": "IN",
                    "name": "India"
                },
                "nightsInDest": "None",
                "quality": 76.99994,
                "distance": 588.1,
                "duration": {
                    "departure": 5400,
                    "return": 0,
                    "total": 5400
                },
                "price": 53,
                "conversion": {
                    "EUR": 53
                },
                "bags_price": {
                    "1": 0
                },
                "baglimit": {
                    "hand_height": 35,
                    "hand_length": 55,
                    "hand_weight": 8,
                    "hand_width": 25,
                    "hold_dimensions_sum": 158,
                    "hold_height": 52,
                    "hold_length": 78,
                    "hold_weight": 25,
                    "hold_width": 28,
                    "personal_item_height": 20,
                    "personal_item_length": 40,
                    "personal_item_weight": 5,
                    "personal_item_width": 10
                },
                "availability": {
                    "seats": 5
                },
                "airlines": [
                    "AI"
                ],
                "route": [
                    {
                        "id": "07111b744bc900007a04a029_0",
                        "combination_id": "07111b744bc900007a04a029",
                        "flyFrom": "DEL",
                        "flyTo": "BHO",
                        "cityFrom": "New Delhi",
                        "cityCodeFrom": "DEL",
                        "cityTo": "Bhopal",
                        "cityCodeTo": "BHO",
                        "airline": "AI",
                        "flight_no": 435,
                        "operating_carrier": "AI",
                        "operating_flight_no": "435",
                        "fare_basis": "TIP",
                        "fare_category": "M",
                        "fare_classes": "T",
                        "fare_family": "",
                        "return": 0,
                        "bags_recheck_required": False,
                        "vi_connection": False,
                        "guarantee": False,
                        "equipment": "None",
                        "vehicle_type": "aircraft",
                        "local_arrival": "2023-02-13T07:25:00.000Z",
                        "utc_arrival": "2023-02-13T01:55:00.000Z",
                        "local_departure": "2023-02-13T05:55:00.000Z",
                        "utc_departure": "2023-02-13T00:25:00.000Z"
                    }
                ],
                "booking_token": "ETPgtx86X0utg7sW0baa8B4bfyGOTganQh_1UCI7DPacjuOhLN41XFE-Q9m6Smu__CsN4hgEuN1keHCFkRuSywEYULWXrEtMRTzoelWYVvMQPE7rYUIdCjZoHuvMHkkkFFlKHbzZz0g6Jp-byzkNH-pWGjWilMzBzlweDUoPYBnQttTqY-Lim-3ZO99W4KDNSvVJMC9QjIV86b3bSAIUN8c5uLiO1-rBCiYGITnlsXMNlrXhA-AfC20LnxGR3s010Z62NnWVAnFVutLRMBKM7Jb23uTzNnC5RkLCFnGRG40nHLX-54q90z9mW4z359_ujRwdVgOTasXgzIPOpZjOr5qkOUqh_PIF-BlmHw_nvm_SwJppJOO73ZbTEBgrhNbL21G8KurW5tyUccyjmlxhQfgolkJElHXbtpiC3QJvhryiWRuR8l-9eJvYVMeU9fRgKDrEEUz427RBhmKKpriu5oYcP6k0Cs2z4CmvUcl9lsHhyrDJF7pu10ier09jZwdZeJqUxkBBzocykEIsiMq0gHbPAbzBoLfm0LjE4DMjFMwhEi99vdKjbFUaobrvfQ8zVUBTxrbwJUwI1U9xi3fpNAWO4U3iNIlW2IUBQtRms3e0EbInaOxRX1hHKNvHNXE5r",
                "deep_link": "https://www.kiwi.com/deep?affilid=apoorvflightsearch&currency=EUR&flightsId=07111b744bc900007a04a029_0&from=DEL&lang=en&passengers=1&to=BHO&booking_token=E04wT2ePkri7lAC45RIiIL0wdCOKMvJyfrh-b2vMYFdHvxMe-AOrCQNX8fiyLv3uSa6-c7ZABgI90o6hQ9-SDI9Bay_vqr-ZndvMDeYSPIe_sGSXwLz8F__UDLfjNshMJlQyOqCMKhIyoT2rmrWVTgvOKyBmJYMConKsXWC8lU1CsGTFLdbHF_ygZIhLkF95DRL3zOJAp-vcc3VvScMck2mRmxQM9q3klGUTHzaJjjgxYboX-bp3_Wz4f6AhrqVwKZFa1UtU71HdUjXcHznVdWo3TZ12QShUAGj9xbSgLo3Kk2HvKn3KDxGNm0XRuPQOoefaJfaRJLFd5HxX5bzdOJ_mHksRiQYgv5RKO6ETAhAhxpwT4inqTbOT0JVEDMUQ0BGwg-dJJMVWw7WA4no9ZHuCpA6psmi7h0LxqAvmr1HVe6wLODZyfQUzJpmCraUSLFIW_C0wisbU-DmFdyrWSlKkhvP9w5xx_SD7K7-nMcAO970O3lrtn9w8aRq_djUIP",
                "facilitated_booking_available": True,
                "pnr_count": 1,
                "has_airport_change": False,
                "technical_stops": 0,
                "throw_away_ticketing": False,
                "hidden_city_ticketing": False,
                "virtual_interlining": False,
                "local_arrival": "2023-02-13T07:25:00.000Z",
                "utc_arrival": "2023-02-13T01:55:00.000Z",
                "local_departure": "2023-02-13T05:55:00.000Z",
                "utc_departure": "2023-02-13T00:25:00.000Z"
            },
            {
                "id": "071125764bc70000d7101b7f_0",
                "flyFrom": "DEL",
                "flyTo": "HJR",
                "cityFrom": "New Delhi",
                "cityCodeFrom": "DEL",
                "cityTo": "Khajuraho Group of Monuments",
                "cityCodeTo": "HJR",
                "countryFrom": {
                    "code": "IN",
                    "name": "India"
                },
                "countryTo": {
                    "code": "IN",
                    "name": "India"
                },
                "nightsInDest": "None",
                "quality": 78.333275,
                "distance": 502.53,
                "duration": {
                    "departure": 5100,
                    "return": 0,
                    "total": 5100
                },
                "price": 55,
                "conversion": {
                    "EUR": 55
                },
                "bags_price": {
                    "1": 0
                },
                "baglimit": {
                    "hand_height": 36,
                    "hand_length": 54,
                    "hand_weight": 7,
                    "hand_width": 18,
                    "hold_dimensions_sum": 158,
                    "hold_height": 52,
                    "hold_length": 78,
                    "hold_weight": 15,
                    "hold_width": 28
                },
                "availability": {
                    "seats": 2
                },
                "airlines": [
                    "SG"
                ],
                "route": [
                    {
                        "id": "071125764bc70000d7101b7f_0",
                        "combination_id": "071125764bc70000d7101b7f",
                        "flyFrom": "DEL",
                        "flyTo": "HJR",
                        "cityFrom": "New Delhi",
                        "cityCodeFrom": "DEL",
                        "cityTo": "Khajuraho Group of Monuments",
                        "cityCodeTo": "HJR",
                        "airline": "SG",
                        "flight_no": 2931,
                        "operating_carrier": "SG",
                        "operating_flight_no": "2931",
                        "fare_basis": "CSAV",
                        "fare_category": "M",
                        "fare_classes": "C",
                        "fare_family": "",
                        "return": 0,
                        "bags_recheck_required": False,
                        "vi_connection": False,
                        "guarantee": False,
                        "equipment": "None",
                        "vehicle_type": "aircraft",
                        "local_arrival": "2023-02-11T17:20:00.000Z",
                        "utc_arrival": "2023-02-11T11:50:00.000Z",
                        "local_departure": "2023-02-11T15:55:00.000Z",
                        "utc_departure": "2023-02-11T10:25:00.000Z"
                    }
                ],
                "booking_token": "ELFb3oZ-hDASRD5i5pDZ4Gi3qiWjJdBMIrhax-AFFEVaVv0hUGS0UBs4DR0ijgxdLu2dOmY-3aN8imsOuqPTvVM3BZYwS-AHoIjw5ScqoibR9zKJXUu7LyUBnyifyt1XZu3V8IaAu_A9d71QrGYiJ8NyXW0QPtPJ8mZvCpljNwO8BTC1Qco5d1wC7CCnVe1ooGBPcAnrsHaFOq-49vUn4VmWL0fiPnNl4aOnmYghucL9MyUB3PFIZTzZy9IIV8g7Rl9d8g_9HqQw4T_zqA73h-QDv1fkjbZawhABMmekwXffd9rie_CevV-V2L9C5BE3i0gcFjCcXx-0xho5w_lBRVKYXiQaQp6Kz7B1BrsThaPH0y7_F5bMxx3z-sVHlvvw9BUdE1QKQhv8ykhI7C33Q1D3LdvyY6XXPOqb79oatwVUQIKIqj5-xBWc-TsUpzcMjpWk3Mg26w05-hEPc60SdNE3qnRYom1kMnDhXAk_-zdQY_gzeBN_WN9-_rykxB0BST4FuF53A5h6P2JM_usSyGjdkde8x4ELaVHm0a0aJ_w_k1WudjnZof3h2kDwFUk3B",
                "deep_link": "https://www.kiwi.com/deep?affilid=apoorvflightsearch&currency=EUR&flightsId=071125764bc70000d7101b7f_0&from=DEL&lang=en&passengers=1&to=HJR&booking_token=EgX6AqCsu-bjc4pvTheswX-J7e1PuHznVVVIjIk0T15bns3ImQ50WbkrTpkz78H1Mil6xDB12OTG5_txfM3wrWm8YT8ap10XMrLDIpcq9zcf9RqRkx_vdWSmwMhTNwBLTKSag9Kb2aJ1sv-qMmZ-dCwtiXCPQwO_ujzWRf0T0i2_qZRvoWIFcwiy29E9eZf08oFMgB6cXXkMgxX_08RtczQXf63FLGu2wnweJ92-uqBmDFFsc3AmySifinG_r0KDznz-eMo6t98ya09Cey-Rr_KEPF0nRfe56PcQk3RWhvnQqzKd5PjtTCWIvBhWyTRd2VaZOr-WKQeAOmZ9g2FCxHuyYKyv09rZareaCI1q1nGieLds14Cb2ZU86ovXoIYscaDhy4mZJdgxcNfcWX6A_MYabA023fL__cHLxuzcm-OQ=",
                "facilitated_booking_available": True,
                "pnr_count": 1,
                "has_airport_change": False,
                "technical_stops": 0,
                "throw_away_ticketing": False,
                "hidden_city_ticketing": False,
                "virtual_interlining": False,
                "local_arrival": "2023-02-11T17:20:00.000Z",
                "utc_arrival": "2023-02-11T11:50:00.000Z",
                "local_departure": "2023-02-11T15:55:00.000Z",
                "utc_departure": "2023-02-11T10:25:00.000Z"
            },
            {
                "id": "0711019d4bc8000073bf7448_0",
                "flyFrom": "DEL",
                "flyTo": "JLR",
                "cityFrom": "New Delhi",
                "cityCodeFrom": "DEL",
                "cityTo": "Jabalpur",
                "cityCodeTo": "JLR",
                "countryFrom": {
                    "code": "IN",
                    "name": "India"
                },
                "countryTo": {
                    "code": "IN",
                    "name": "India"
                },
                "nightsInDest": "None",
                "quality": 78.99994,
                "distance": 668.53,
                "duration": {
                    "departure": 5400,
                    "return": 0,
                    "total": 5400
                },
                "price": 55,
                "conversion": {
                    "EUR": 55
                },
                "bags_price": {
                    "1": 0
                },
                "baglimit": {
                    "hand_height": 38,
                    "hand_length": 57,
                    "hand_weight": 7,
                    "hand_width": 20,
                    "hold_dimensions_sum": 158,
                    "hold_height": 52,
                    "hold_length": 78,
                    "hold_weight": 15,
                    "hold_width": 28
                },
                "availability": {
                    "seats": 2
                },
                "airlines": [
                    "6E"
                ],
                "route": [
                    {
                        "id": "0711019d4bc8000073bf7448_0",
                        "combination_id": "0711019d4bc8000073bf7448",
                        "flyFrom": "DEL",
                        "flyTo": "JLR",
                        "cityFrom": "New Delhi",
                        "cityCodeFrom": "DEL",
                        "cityTo": "Jabalpur",
                        "cityCodeTo": "JLR",
                        "airline": "6E",
                        "flight_no": 6788,
                        "operating_carrier": "",
                        "operating_flight_no": "",
                        "fare_basis": "O0IP",
                        "fare_category": "M",
                        "fare_classes": "X",
                        "fare_family": "",
                        "return": 0,
                        "bags_recheck_required": False,
                        "vi_connection": False,
                        "guarantee": False,
                        "equipment": "None",
                        "vehicle_type": "aircraft",
                        "local_arrival": "2023-02-12T15:15:00.000Z",
                        "utc_arrival": "2023-02-12T09:45:00.000Z",
                        "local_departure": "2023-02-12T13:45:00.000Z",
                        "utc_departure": "2023-02-12T08:15:00.000Z"
                    }
                ],
                "booking_token": "EaxU2i33EbujxsnuCK_BjLhJ3SAEcj2O00Pu08pT2sVBtrBMZLKeaI1dp9DOBfUKZY4e3-ZwmZ3mI6ySas4pELU2Yg1mRBCMLhgDZtM6Hy88ZNKjZQY3OIbEQJyk0CUzoXXcWWPDUwxXBS2HjCMOlypZX-2Vdj6egcAt_YrBZbCTlkTDtqjCPgWYulv-R6HeaLwJXGE9bhvwPZd02ab9p-amP3za1905wDsnLRXY393NZozwu-PXW_gP6-5hc20b24c83o_jIy_0MQcdeV6-VPXKwdZzttsnI2aYrJF9xEhKmwZnbnEgOxasxtFIwDgVu8ZKd0vVGAandPa8v8hG7kJrE2Xdrdx0daQsTu3FMB1WJpN10-rsilqvusa2B-MwAcIfNyg37y1QYcO6pdjFSktQRXvF6tk1yGYrdaCdkraqTEw5Rcel6OvDB2VcYzWRXK949EwKa9Yc3FkbdMRvtDh942_LnYAoejM7WnPO1S10E5fkNL_ymT-Aw0VyEgR5wM9WuGop2FF-bpUhKyM1U5T30KHpVBmB7wlaMlgzroMU=",
                "deep_link": "https://www.kiwi.com/deep?affilid=apoorvflightsearch&currency=EUR&flightsId=0711019d4bc8000073bf7448_0&from=DEL&lang=en&passengers=1&to=JLR&booking_token=ETghfzrDkRjm9Dgvhb62SH8czIZi5STlqTG2KZM28UEhlSEjIVp_Ut9t2kq5ljBOG9014uHNf8XqR8SUdYf0qteZd-rOVgniZa9rajnQE9Jd3H7-Avcw33RnEs-Jlz6X33F6qMe_qXLjDSiMx9ynWWUry2yM0k9CFcuyYGWTGgqFz2gMrWx3OePpjPQgBanIZET0wzqAzueAJBLefP6eULBXH9oVFyd5OR3Mj-xMTytrMF3O01pHmYcZ3Ff44efvm0gxb-CqJtS-SAnQqPDYip6lKIEnasQqQaA027umu_LDKQk3PJZFdFYMQM-kDsvZiOu5IjHW_GTB_Ic2MQaooATqilABQkHM8s159GYZHvvV3LBlONYKMlYmo9MMMEkY_kHWIUr-K13zBsDSl1rWzgTI0_A1xnBPrPSk-NyB-kUE=",
                "facilitated_booking_available": True,
                "pnr_count": 1,
                "has_airport_change": False,
                "technical_stops": 0,
                "throw_away_ticketing": False,
                "hidden_city_ticketing": False,
                "virtual_interlining": False,
                "local_arrival": "2023-02-12T15:15:00.000Z",
                "utc_arrival": "2023-02-12T09:45:00.000Z",
                "local_departure": "2023-02-12T13:45:00.000Z",
                "utc_departure": "2023-02-12T08:15:00.000Z"
            },
            {
                "id": "07111b744bc70000a40f2a30_0",
                "flyFrom": "DEL",
                "flyTo": "BHO",
                "cityFrom": "New Delhi",
                "cityCodeFrom": "DEL",
                "cityTo": "Bhopal",
                "cityCodeTo": "BHO",
                "countryFrom": {
                    "code": "IN",
                    "name": "India"
                },
                "countryTo": {
                    "code": "IN",
                    "name": "India"
                },
                "nightsInDest": "None",
                "quality": 78.99994,
                "distance": 588.1,
                "duration": {
                    "departure": 5400,
                    "return": 0,
                    "total": 5400
                },
                "price": 55,
                "conversion": {
                    "EUR": 55
                },
                "bags_price": {
                    "1": 0
                },
                "baglimit": {
                    "hand_height": 38,
                    "hand_length": 57,
                    "hand_weight": 7,
                    "hand_width": 20,
                    "hold_dimensions_sum": 158,
                    "hold_height": 52,
                    "hold_length": 78,
                    "hold_weight": 15,
                    "hold_width": 28
                },
                "availability": {
                    "seats": "None"
                },
                "airlines": [
                    "6E"
                ],
                "route": [
                    {
                        "id": "07111b744bc70000a40f2a30_0",
                        "combination_id": "07111b744bc70000a40f2a30",
                        "flyFrom": "DEL",
                        "flyTo": "BHO",
                        "cityFrom": "New Delhi",
                        "cityCodeFrom": "DEL",
                        "cityTo": "Bhopal",
                        "cityCodeTo": "BHO",
                        "airline": "6E",
                        "flight_no": 6022,
                        "operating_carrier": "6E",
                        "operating_flight_no": "6022",
                        "fare_basis": "R0IP",
                        "fare_category": "M",
                        "fare_classes": "R",
                        "fare_family": "",
                        "return": 0,
                        "bags_recheck_required": False,
                        "vi_connection": False,
                        "guarantee": False,
                        "equipment": "None",
                        "vehicle_type": "aircraft",
                        "local_arrival": "2023-02-11T08:20:00.000Z",
                        "utc_arrival": "2023-02-11T02:50:00.000Z",
                        "local_departure": "2023-02-11T06:50:00.000Z",
                        "utc_departure": "2023-02-11T01:20:00.000Z"
                    }
                ],
                "booking_token": "E4B3I5vOZ0RTUsrbaroIS2UFj3iPDIKAC3NXGq_l7yg4S3PcMorPoSbF7OYbD9PU3UmJ25Ws-g2ASGbosQCdnx7imVIYNbl6vEg2TrRkGtxsJ1x1nKrzd1lh0DN5pzGP7kMcKUU3I2cwfCu1atjB0hL0SHE3f4-I9b4AxVOiKq45MJfXkVILyJyL7TG8wl9ticHzY7pgUqnDjgg9RsEf6Devz8wRU8gu8O5WHjyjs-NQBjFXSPUssMgeDHiBekzcWlYTjVTupmozrrvxZ3gfYit2aRJNcJ-HwYkPNsNDVz22z2_lCP5jWceQGrvjC2JPtFXb2yh1ggKbM0g0SuZtcNo7g8nszIN7uvlclbQphOUHMVOaMNlVbH-8WceMzCAEalIhMsSQDRAv6Nb8S94D7zO7POed9y-vS2sprprqAGRS77qAReWMYuPXAdDG9HmcW0VhJYniX0zbM3X0HiKdgMH5RgpwdJh11hB0uWaMVkwfLa1PLXG4IvTpgZVFoApBBYExs9P9_tRmtw_teYtou24wX0wVXzLQDu6YzsnqXA4NLTpOCIBu4wchgEDMm3bqs",
                "deep_link": "https://www.kiwi.com/deep?affilid=apoorvflightsearch&currency=EUR&flightsId=07111b744bc70000a40f2a30_0&from=DEL&lang=en&passengers=1&to=BHO&booking_token=E-ol1BzRvdAuw63vDQO1le8RQknbE6QXiSxN7G9oSRQZvjNjOGfkU-tRN_XvnxsjCuvclm8n9GvoKS-Lvw6dRVXYNSJWawi459JMFmqFVsXhjUcjKD2PiO_oop1J675HcHv_dR5_SkuFM-YLV9sU-0HqNAEGuMvnRdNpK37606W-L5RdZct3mJSA0VQ_CDDLCQf7z_DKl5GLw14q3kBcggHlfh4ibvORpJ2U8WjK0g7GaGQmdQn3meBs5B43A4k8wsf26LcrXo9DG1pohYKjm3uuMIo4Cu6BcXV9rEophPBbrK_A-Rq1si76gZCrWxIwOCzwNwC2m6gOeIuge74yW_T61Vt2EsJhbugl1xtkVqSz_BPxlKP3gEe7uH302tcyscd11PZzHh7n2DzVlzg8fdQe23XpDKihNNQcMdWYBtyA=",
                "facilitated_booking_available": True,
                "pnr_count": 1,
                "has_airport_change": False,
                "technical_stops": 0,
                "throw_away_ticketing": False,
                "hidden_city_ticketing": False,
                "virtual_interlining": False,
                "local_arrival": "2023-02-11T08:20:00.000Z",
                "utc_arrival": "2023-02-11T02:50:00.000Z",
                "local_departure": "2023-02-11T06:50:00.000Z",
                "utc_departure": "2023-02-11T01:20:00.000Z"
            },
            {
                "id": "07111b744bc70000ae16fb4a_0",
                "flyFrom": "DEL",
                "flyTo": "BHO",
                "cityFrom": "New Delhi",
                "cityCodeFrom": "DEL",
                "cityTo": "Bhopal",
                "cityCodeTo": "BHO",
                "countryFrom": {
                    "code": "IN",
                    "name": "India"
                },
                "countryTo": {
                    "code": "IN",
                    "name": "India"
                },
                "nightsInDest": "None",
                "quality": 80.33327,
                "distance": 588.1,
                "duration": {
                    "departure": 6000,
                    "return": 0,
                    "total": 6000
                },
                "price": 55,
                "conversion": {
                    "EUR": 55
                },
                "bags_price": {
                    "1": 0
                },
                "baglimit": {
                    "hand_height": 38,
                    "hand_length": 57,
                    "hand_weight": 7,
                    "hand_width": 20,
                    "hold_dimensions_sum": 158,
                    "hold_height": 52,
                    "hold_length": 78,
                    "hold_weight": 15,
                    "hold_width": 28
                },
                "availability": {
                    "seats": "None"
                },
                "airlines": [
                    "6E"
                ],
                "route": [
                    {
                        "id": "07111b744bc70000ae16fb4a_0",
                        "combination_id": "07111b744bc70000ae16fb4a",
                        "flyFrom": "DEL",
                        "flyTo": "BHO",
                        "cityFrom": "New Delhi",
                        "cityCodeFrom": "DEL",
                        "cityTo": "Bhopal",
                        "cityCodeTo": "BHO",
                        "airline": "6E",
                        "flight_no": 2168,
                        "operating_carrier": "6E",
                        "operating_flight_no": "2168",
                        "fare_basis": "R0IP",
                        "fare_category": "M",
                        "fare_classes": "R",
                        "fare_family": "",
                        "return": 0,
                        "bags_recheck_required": False,
                        "vi_connection": False,
                        "guarantee": False,
                        "equipment": "None",
                        "vehicle_type": "aircraft",
                        "local_arrival": "2023-02-11T21:10:00.000Z",
                        "utc_arrival": "2023-02-11T15:40:00.000Z",
                        "local_departure": "2023-02-11T19:30:00.000Z",
                        "utc_departure": "2023-02-11T14:00:00.000Z"
                    }
                ],
                "booking_token": "E3rgFT6kQjrmgbsU3W6PI81RyJIxdbtgYq69FQ3vZQzvFmb16iI5IFf-Casr66yK5ODaDiDR26ldxbBlJTb1toZ-_ynmSH_SbRzD8mdwgAY1ypryhWtxOsHb3S-AuuRHQyxWNypjUICDc2bNtAfbGZG0ryAl2Jm1RfE6B4F9wbiPnPKDsbPu5iMWCdVtiGXgi7WFDmibNLGOyM7MjmuLVeSFRZCA4PFSQ2KRY51YFtPM6nsJXMV2LyQVCBmGy6_vxa28MPmphN19XL2xlPvfeo9FpOfXr-UqCHC1pTqJbvW3S_gFmabTkYBM7-AOW-x0CiDaY3FrRa1hpP2VdJpXabnGPYD_wpD4HgbFCLIhBUrfnOtHMZlY61-rhrc9eGLPdrDgA3TUdVZxt2q67TxvcZusbIKXVy0YinCRx-Vw5l4c2Zyk7YAYdKeGOVpKp2ANJ1y28NoydvTdukGRz4qMh_Fwp04uLojsjQcBmVgglVnyMtTyELuJ3aaFhpqjQKHWgwXowuCmrj968M6N1yj4Pko5jmuD8QBg2M176kK6wBLSKdZkXtkI9NHyRp9lDd5tgILp8QmzQ9oPQ1Cto5lHMMcIKg8C5PqwCrRQdri1xlC8=",
                "deep_link": "https://www.kiwi.com/deep?affilid=apoorvflightsearch&currency=EUR&flightsId=07111b744bc70000ae16fb4a_0&from=DEL&lang=en&passengers=1&to=BHO&booking_token=EKMMaCOrLsWAOgzbcMtILLCb3NucvXPH35vLabwmmbaRWItDes_by0zJD51c0hrc1ERChDiTrmFOT9tBp4lYjyivHkp_MF8X9jHrVCNWSwsSt-KagpeAeNoBa9dTuMntiuWPiuwgKpZBWtYon0ld3rx3CmWOwrwTVkl2ZZXLUQREzKGcEYDaa-KfzwjCqo-OyrkQkUki1H67cMjLfOZ5fduN731ve25ro24THHHZBKP0DOptuFRVoY3ok1regyq7FjJHzL56fIeTv9JYuWchMpqOtZE9s0c_EGjy6XC2ylZHlo16q5YCQGGcqraqZyrUoypaZ0MiqiK7KB1mtnNFQPUwIrMOCHhn0Ts9tcBIc4RQ2-BLQSFsdhilwVqgR6t47ULstjSLN8Vw0IWOX1EmPziFHCVatd5eE90FOgZqk5_6vPT2sQltBdTSj4Ocje8SlHdZwVI_kXOqyunMPa2Dpdw==",
                "facilitated_booking_available": True,
                "pnr_count": 1,
                "has_airport_change": False,
                "technical_stops": 0,
                "throw_away_ticketing": False,
                "hidden_city_ticketing": False,
                "virtual_interlining": False,
                "local_arrival": "2023-02-11T21:10:00.000Z",
                "utc_arrival": "2023-02-11T15:40:00.000Z",
                "local_departure": "2023-02-11T19:30:00.000Z",
                "utc_departure": "2023-02-11T14:00:00.000Z"
            },
            {
                "id": "071107194bc90000b1136b70_0",
                "flyFrom": "DEL",
                "flyTo": "DED",
                "cityFrom": "New Delhi",
                "cityCodeFrom": "DEL",
                "cityTo": "Dehradun",
                "cityCodeTo": "DED",
                "countryFrom": {
                    "code": "IN",
                    "name": "India"
                },
                "countryTo": {
                    "code": "IN",
                    "name": "India"
                },
                "nightsInDest": "None",
                "quality": 74.66662,
                "distance": 208.74,
                "duration": {
                    "departure": 3000,
                    "return": 0,
                    "total": 3000
                },
                "price": 56,
                "conversion": {
                    "EUR": 56
                },
                "bags_price": {
                    "1": 0
                },
                "baglimit": {
                    "hand_height": 38,
                    "hand_length": 57,
                    "hand_weight": 7,
                    "hand_width": 20,
                    "hold_dimensions_sum": 158,
                    "hold_height": 52,
                    "hold_length": 78,
                    "hold_weight": 15,
                    "hold_width": 28
                },
                "availability": {
                    "seats": 2
                },
                "airlines": [
                    "6E"
                ],
                "route": [
                    {
                        "id": "071107194bc90000b1136b70_0",
                        "combination_id": "071107194bc90000b1136b70",
                        "flyFrom": "DEL",
                        "flyTo": "DED",
                        "cityFrom": "New Delhi",
                        "cityCodeFrom": "DEL",
                        "cityTo": "Dehradun",
                        "cityCodeTo": "DED",
                        "airline": "6E",
                        "flight_no": 2071,
                        "operating_carrier": "6E",
                        "operating_flight_no": "2071",
                        "fare_basis": "",
                        "fare_category": "M",
                        "fare_classes": "Q",
                        "fare_family": "",
                        "return": 0,
                        "bags_recheck_required": False,
                        "vi_connection": False,
                        "guarantee": False,
                        "equipment": "None",
                        "vehicle_type": "aircraft",
                        "local_arrival": "2023-02-13T17:45:00.000Z",
                        "utc_arrival": "2023-02-13T12:15:00.000Z",
                        "local_departure": "2023-02-13T16:55:00.000Z",
                        "utc_departure": "2023-02-13T11:25:00.000Z"
                    }
                ],
                "booking_token": "EW8IY-i9OrVTcctdmOrXzqv6nnk07Wl-B1rGwx15Ox_mQHpVF1qY4FPAdm5HTDM2Pq4w2wS5Sre0u9KiIydBvhgVuaoP26Y0A3sbm8OLZAQ8_Lu5vr2_hqu4U66Xsrw5EviRCN_G4OAZrZlG6uvRpqo3d8Go1idu1H5x4WFhp1nLNsdPmmc3JY9JLRZSvuuv6zzcbyWdXd5v_iHQWPnnhdXihEwQUA4CDhipa2_EKz7JdjXy6bmB2NNrUUTGKhqdceG9og92BaNdTx05BIZqRrYBLf3BK9moViC2rnrvtF5UIorBvp6DZmZfmcVtFxfrhZvNDeYlBeqEhM6u38vKBgqJbp7SEEY4i7Un2L8wTZSC2rbXer3OaZkIwvhsqnSo2u5ZMBIeu0u8vnQSYXjPYJJZp1QcgUfAkv5yMwS0FvFdn4zREhk15-H99N_EZeWd69rBoif5eMxlH6MqEXA9oNkD5P50lEnbW_SWiYg81yucZb9PGWP1h9RdB0Ope705oCQq_UF0n22ixM9vZnfiBMvOXKPJZYsk-pS10lZVNJrpVNaC6xYLywAH-DlUZ7v0Q",
                "deep_link": "https://www.kiwi.com/deep?affilid=apoorvflightsearch&currency=EUR&flightsId=071107194bc90000b1136b70_0&from=DEL&lang=en&passengers=1&to=DED&booking_token=Ei_78GGcSdqrk10Li0zPChpDPMpZVpbhBk-vSXRN8DKUIMvrPPYzq04Zl3udBD-WS1Ilt6RiG2m6ymfIIRONkQNWOrwjU_9jFx-xjoX0DChpJ-GjCy3vH9RHsgpdQhGUO9XweUpFm15AMNXo26OLshQREalPq-ovXFnMZZ4LUfOGv3A9BKFGwuxS4ZGhCn1badJ-_i6PfFQyJEeJ_kDINUU7sMUK8W4T4O_kC67KvXlGMV2Qi49a8TUxarRhpBiWXu7OBxYJINg0qqHBMSXXhAJJFxVdkf92v7uVmOIOBjwPK0-KG3NBVfiBd0Bj9vg-G_QRMoCQaBuV4_SK290eyQSKIWvf1vEW2D4I2uuPNcThqKw124xtyyeJX7nlMf2VRQd9TXXmc74MJHXYe1onkJaH0HkITQjTdi4JB6_wNTpY=",
                "facilitated_booking_available": True,
                "pnr_count": 1,
                "has_airport_change": False,
                "technical_stops": 0,
                "throw_away_ticketing": False,
                "hidden_city_ticketing": False,
                "virtual_interlining": False,
                "local_arrival": "2023-02-13T17:45:00.000Z",
                "utc_arrival": "2023-02-13T12:15:00.000Z",
                "local_departure": "2023-02-13T16:55:00.000Z",
                "utc_departure": "2023-02-13T11:25:00.000Z"
            },
            {
                "id": "071107194bc90000cfd7322f_0",
                "flyFrom": "DEL",
                "flyTo": "DED",
                "cityFrom": "New Delhi",
                "cityCodeFrom": "DEL",
                "cityTo": "Dehradun",
                "cityCodeTo": "DED",
                "countryFrom": {
                    "code": "IN",
                    "name": "India"
                },
                "countryTo": {
                    "code": "IN",
                    "name": "India"
                },
                "nightsInDest": "None",
                "quality": 75.333285,
                "distance": 208.74,
                "duration": {
                    "departure": 3300,
                    "return": 0,
                    "total": 3300
                },
                "price": 56,
                "conversion": {
                    "EUR": 56
                },
                "bags_price": {
                    "1": 0
                },
                "baglimit": {
                    "hand_height": 38,
                    "hand_length": 57,
                    "hand_weight": 7,
                    "hand_width": 20,
                    "hold_dimensions_sum": 158,
                    "hold_height": 52,
                    "hold_length": 78,
                    "hold_weight": 15,
                    "hold_width": 28
                },
                "availability": {
                    "seats": 2
                },
                "airlines": [
                    "6E"
                ],
                "route": [
                    {
                        "id": "071107194bc90000cfd7322f_0",
                        "combination_id": "071107194bc90000cfd7322f",
                        "flyFrom": "DEL",
                        "flyTo": "DED",
                        "cityFrom": "New Delhi",
                        "cityCodeFrom": "DEL",
                        "cityTo": "Dehradun",
                        "cityCodeTo": "DED",
                        "airline": "6E",
                        "flight_no": 5026,
                        "operating_carrier": "6E",
                        "operating_flight_no": "5026",
                        "fare_basis": "",
                        "fare_category": "M",
                        "fare_classes": "Q",
                        "fare_family": "",
                        "return": 0,
                        "bags_recheck_required": False,
                        "vi_connection": False,
                        "guarantee": False,
                        "equipment": "None",
                        "vehicle_type": "aircraft",
                        "local_arrival": "2023-02-13T09:15:00.000Z",
                        "utc_arrival": "2023-02-13T03:45:00.000Z",
                        "local_departure": "2023-02-13T08:20:00.000Z",
                        "utc_departure": "2023-02-13T02:50:00.000Z"
                    }
                ],
                "booking_token": "E9MgBzwZr0Z1P4C8UcnQgBXLE8_bYrWV36PM95oG7ifz6zJXSqWZJikz64zzV9rghBRIo96z0_3qRy0vZ7m7GDxkb-WmLWv3qhb9kbSty56cRnsFXrT-AQZGbmG0dDSCs6xBCVgGnOWjN9tQ1jFhVYDIzkVmB7MiraIMU48sn4AMtj1GJADEMAhV46FSG3x9qWdfq9hZVtIXpWlaQD6jg6DonnLh_Mt75Bwqf2AdXtZNfJIVdmoOMQZb2Lk7bZoB1AlBYB2vdXcZk1iueNbyFnSQc_HhUd55QhWzrOC48WADguBAClqXP1XDX-a2nayIM6fsGxRFsyFUURPmFAz7r32RzCJGea9ZhTVxBG8jr8w4u1ngNN5mTpOx1ODNxLSwfUXaWk-Lotfu3FCuIN9aokf-Pmj_7AjmOSNkpKdbzNAJzpj-vPdXvd4tI1Yxt_9eqKTfLxyHB2FSYi7L1V5dhjoPX0zJW25QiCnl50IBbLVI9KEnp62ci3mlDg53sj90Mw21AV65wMmZyBp7KyEB0kghdRWGCdoR2qHZtGqqLoLFrKfbRxH4oWzApjHFSXY1E",
                "deep_link": "https://www.kiwi.com/deep?affilid=apoorvflightsearch&currency=EUR&flightsId=071107194bc90000cfd7322f_0&from=DEL&lang=en&passengers=1&to=DED&booking_token=EE3EqI2B6LclPFEQl6z-4CaWH3QQ-5j370NOjLrEIdDOOmSL2vEGI_XpBVUArUWJnbJJHNPyzmG3b0NlEkZMffHyocyrgzNktCVmMJDnMo4WiGuV4zO9RuVL-jKhPNnpHP2NKZAiw77EDt0GacIk5xKzrqNFLnpDHmrSCcw4dAfWxcSutEtwtuQVk9L1Jlfvb4ZtS9cEzyhkvz1vMlNzml0CyhuiopeFyolcS10DWQ6EJyZmso8jxirUa0SgdZm0Oli7ZbjFhTFTcWihKE7vkP90kj93vn2hDZFg-uiHi1DPhp-J0dY20D4alCbMOo64WcAY3pbYEMpwgIL4mhS9OX9c9DUCaQn-OumJ_3WXAhgCFpplmQpnjO0egJUBFSe3JjEI46zGDPU5cx5iYnRG8RlNu7SiElXzMchUfpqlXio4=",
                "facilitated_booking_available": True,
                "pnr_count": 1,
                "has_airport_change": False,
                "technical_stops": 0,
                "throw_away_ticketing": False,
                "hidden_city_ticketing": False,
                "virtual_interlining": False,
                "local_arrival": "2023-02-13T09:15:00.000Z",
                "utc_arrival": "2023-02-13T03:45:00.000Z",
                "local_departure": "2023-02-13T08:20:00.000Z",
                "utc_departure": "2023-02-13T02:50:00.000Z"
            },
            {
                "id": "071113884bc90000898c5e1a_0",
                "flyFrom": "DEL",
                "flyTo": "IDR",
                "cityFrom": "New Delhi",
                "cityCodeFrom": "DEL",
                "cityTo": "Indore",
                "cityCodeTo": "IDR",
                "countryFrom": {
                    "code": "IN",
                    "name": "India"
                },
                "countryTo": {
                    "code": "IN",
                    "name": "India"
                },
                "nightsInDest": "None",
                "quality": 78.66661,
                "distance": 663.59,
                "duration": {
                    "departure": 4800,
                    "return": 0,
                    "total": 4800
                },
                "price": 56,
                "conversion": {
                    "EUR": 56
                },
                "bags_price": {
                    "1": 0
                },
                "baglimit": {
                    "hand_height": 38,
                    "hand_length": 57,
                    "hand_weight": 7,
                    "hand_width": 20,
                    "hold_dimensions_sum": 158,
                    "hold_height": 52,
                    "hold_length": 78,
                    "hold_weight": 15,
                    "hold_width": 28
                },
                "availability": {
                    "seats": 3
                },
                "airlines": [
                    "6E"
                ],
                "route": [
                    {
                        "id": "071113884bc90000898c5e1a_0",
                        "combination_id": "071113884bc90000898c5e1a",
                        "flyFrom": "DEL",
                        "flyTo": "IDR",
                        "cityFrom": "New Delhi",
                        "cityCodeFrom": "DEL",
                        "cityTo": "Indore",
                        "cityCodeTo": "IDR",
                        "airline": "6E",
                        "flight_no": 6103,
                        "operating_carrier": "6E",
                        "operating_flight_no": "6103",
                        "fare_basis": "Q0IP",
                        "fare_category": "M",
                        "fare_classes": "Q",
                        "fare_family": "",
                        "return": 0,
                        "bags_recheck_required": False,
                        "vi_connection": False,
                        "guarantee": False,
                        "equipment": "None",
                        "vehicle_type": "aircraft",
                        "local_arrival": "2023-02-13T22:20:00.000Z",
                        "utc_arrival": "2023-02-13T16:50:00.000Z",
                        "local_departure": "2023-02-13T21:00:00.000Z",
                        "utc_departure": "2023-02-13T15:30:00.000Z"
                    }
                ],
                "booking_token": "E1ryNa_T5A8IjcllgAVcXXxNznFkR8kHJy5lI0afV9aY9C_MF69g8iFQbDEnmhqKbGKJd0KCQU-IOEw6l2pnJdbOUk0fiHprNot3XNrvZ9fTa0PvlgyInfVthBAfsz5QSzGzl4yVJlZS5pC8JtxeE5lT_fYgqaSOfB-PI4F3jfUkRDSJ_KaIDbK3oLAIpEB9qgii3G3fBLVrW1tEDhgPbvDAFm4TyrVozA5ggh5JFHhqC2x4fgrN5DrtmViT7zRgnByorKoHpk62EeDkcbPI3N2cDm-lz9F7fP1P3z-URHuDObzZqNWOSJsaItPXAX89nJxgPFIM4xbzTusZ1zZI84m1WixrZOPwbeF_sSqg_-eOAbP8SzVfuob6ZvSLA4P4NZ_W4CM3VdZQeFCWvrvtYEaV55rbXxMC5U1D7otvHLFJTad4wPzSA4DntzkfZIxBrRQC9YJaMwwI8OF13ZoazBlSGLweeM53ptloSbzQSF3OCBrJLiHqsrW7WWi2d-XDc8JOeDaU7awL4CngM3JX3J3bU0sJGU016ZyV7iW0IASpn5GCoBrFN8UjwRRXUWyFxn8J7zGlIEsNXhUVteAtixhEDIXM10D5P98Km693H_b4=",
                "deep_link": "https://www.kiwi.com/deep?affilid=apoorvflightsearch&currency=EUR&flightsId=071113884bc90000898c5e1a_0&from=DEL&lang=en&passengers=1&to=IDR&booking_token=E2Ct4cyibjR6vzT1nhhUq3W11v7Or6PEPpnApJ0V7GPlEuPHL9QzEwdJ7t9swuqINlkxv5ZkSkt9imaijf18Y2p8sxg2rgoy2pDD6pV1mkWpITGkhsyqSlpnKkclrIJZgl89ur6q2I40iGL-J9LxduH1nTdCZmDNpbHqjPy6HR-QDrA-v1MmdprmAt2C7jEpqpaRT-8VIyvqRqbuodRtDQb7yPSb05b0dlFXy58QjeEu18F-HlGcv4hjouCA8MqC2Oq3AckeQeXa4Ezi7ks3Tgkx6rW23jFbUH24DL189CFHeNUTK6KqRrUq5cAq_GB-8ZhrzL-ZggM5Dfpm2AE5sfGTNWdaDIVC7qzcv7Yo2mJ0hCahQclllfQyu_RsWQwMIOKZTDoNMLc-uq-C4oSPYIJisNXldJumCZxIiebW39j7uvxe70qT1RsjI0DikDuc5lcRF33lxt5m3CVWTJz_jBg==",
                "facilitated_booking_available": True,
                "pnr_count": 1,
                "has_airport_change": False,
                "technical_stops": 0,
                "throw_away_ticketing": False,
                "hidden_city_ticketing": False,
                "virtual_interlining": False,
                "local_arrival": "2023-02-13T22:20:00.000Z",
                "utc_arrival": "2023-02-13T16:50:00.000Z",
                "local_departure": "2023-02-13T21:00:00.000Z",
                "utc_departure": "2023-02-13T15:30:00.000Z"
            },
            {
                "id": "07111c024bc80000ca8c7693_0",
                "flyFrom": "DEL",
                "flyTo": "VNS",
                "cityFrom": "New Delhi",
                "cityCodeFrom": "DEL",
                "cityTo": "Varanasi",
                "cityCodeTo": "VNS",
                "countryFrom": {
                    "code": "IN",
                    "name": "India"
                },
                "countryTo": {
                    "code": "IN",
                    "name": "India"
                },
                "nightsInDest": "None",
                "quality": 79.99994,
                "distance": 667.75,
                "duration": {
                    "departure": 5400,
                    "return": 0,
                    "total": 5400
                },
                "price": 56,
                "conversion": {
                    "EUR": 56
                },
                "bags_price": {
                    "1": 0
                },
                "baglimit": {
                    "hand_height": 38,
                    "hand_length": 57,
                    "hand_weight": 7,
                    "hand_width": 20,
                    "hold_dimensions_sum": 158,
                    "hold_height": 52,
                    "hold_length": 78,
                    "hold_weight": 15,
                    "hold_width": 28
                },
                "availability": {
                    "seats": 2
                },
                "airlines": [
                    "6E"
                ],
                "route": [
                    {
                        "id": "07111c024bc80000ca8c7693_0",
                        "combination_id": "07111c024bc80000ca8c7693",
                        "flyFrom": "DEL",
                        "flyTo": "VNS",
                        "cityFrom": "New Delhi",
                        "cityCodeFrom": "DEL",
                        "cityTo": "Varanasi",
                        "cityCodeTo": "VNS",
                        "airline": "6E",
                        "flight_no": 2414,
                        "operating_carrier": "",
                        "operating_flight_no": "",
                        "fare_basis": "",
                        "fare_category": "M",
                        "fare_classes": "Q",
                        "fare_family": "",
                        "return": 0,
                        "bags_recheck_required": False,
                        "vi_connection": False,
                        "guarantee": False,
                        "equipment": "None",
                        "vehicle_type": "aircraft",
                        "local_arrival": "2023-02-12T19:55:00.000Z",
                        "utc_arrival": "2023-02-12T14:25:00.000Z",
                        "local_departure": "2023-02-12T18:25:00.000Z",
                        "utc_departure": "2023-02-12T12:55:00.000Z"
                    }
                ],
                "booking_token": "E3ALOLqBZArw0IlFLNFAbG2SZ9ZhJMMR0AMXgKkN3zNi__SevyheBzMnHiSPdb7vO3BOehZiQH16BbuAAQhL6naTDX0HxYKcCa8cglRI1RCaVGjqy_odWzYmiOIggCy5P4m1Y39YJjohDcU5zh0fgfE4Xe1eFCVzdrd8H7L9M0Sf1JKn3gE84rrUBZ7eGR9HNbRnHrbuxZAufwNi9Q-QMQacRvyr8tzbKIWIuTOnBPpIHFmieHH8X2LFYAGE5f5hrm8kRqGGCuAYbN6ZNn8_N1G41v5x6irp4UFi1-Wl6B53dbQ3PL8XpVJ7-MDIQCLQR7oHliLZQh6u6s_S39HQ7W3lbaDflvPcsEDxUhkDWNHf6aCSIoew8SPsBx9FLRNuz4Tp9eDcyep20o-JK6YpCj5qDc77AwmhEoAoLIibMcs9_HOtITf-RbgAjGEt4f2sVodOOo1XIPHt4d5EFvvrtXZ7iDLHLPpu37SqIApvFyN28G0S9YNpo-UV8PjzR1NN08RRGeRdxW0nNVH_LfwfS1dqYOGIL3wO64CspyiCreqE=",
                "deep_link": "https://www.kiwi.com/deep?affilid=apoorvflightsearch&currency=EUR&flightsId=07111c024bc80000ca8c7693_0&from=DEL&lang=en&passengers=1&to=VNS&booking_token=EGbDJwaI-VmiizUhc7HTZx5acXqL_mpNXkgpkgnr9SuTEItMdmAdxoYZ380C6Z4FO_RdpsBBZbtU5_JURdcd-SVsckcTdcl0KPjvofCP6NzdfqPj-BZIy8nMMJ7vwhOxTUC5AVKZdV3wesE6yhw8uf-C-WLmJpeAfaUY4Ky5JwdLftywuYf9Ra0SSmiQE3KsnFgoHBvOgBAL_ahPDWAr767DHg7GfpFNuct1wLYjPeehb9RjWa_Ry0eDxUOtTXeRe8zA2DNQzXisXGUd9agWV1HBa3zNPl7zTrPm0WvlV3Bw8Em4W8_BJJSmoxdQc1g6CUlTne_Ldet0lFVZMpst22dVoJAkWkiJHvTwcCaQHrcd8hGma8jT1YM4Z7NGs93iqgVG4Jo6lXGUPfp3PziA5CuCCH1JvH0Fc9HTXPy8a9qA=",
                "facilitated_booking_available": True,
                "pnr_count": 1,
                "has_airport_change": False,
                "technical_stops": 0,
                "throw_away_ticketing": False,
                "hidden_city_ticketing": False,
                "virtual_interlining": False,
                "local_arrival": "2023-02-12T19:55:00.000Z",
                "utc_arrival": "2023-02-12T14:25:00.000Z",
                "local_departure": "2023-02-12T18:25:00.000Z",
                "utc_departure": "2023-02-12T12:55:00.000Z"
            },
            {
                "id": "071107194bc90000a949e4ee_0",
                "flyFrom": "DEL",
                "flyTo": "DED",
                "cityFrom": "New Delhi",
                "cityCodeFrom": "DEL",
                "cityTo": "Dehradun",
                "cityCodeTo": "DED",
                "countryFrom": {
                    "code": "IN",
                    "name": "India"
                },
                "countryTo": {
                    "code": "IN",
                    "name": "India"
                },
                "nightsInDest": "None",
                "quality": 75.66662,
                "distance": 208.74,
                "duration": {
                    "departure": 3000,
                    "return": 0,
                    "total": 3000
                },
                "price": 57,
                "conversion": {
                    "EUR": 57
                },
                "bags_price": {
                    "1": 0
                },
                "baglimit": {
                    "hand_height": 38,
                    "hand_length": 57,
                    "hand_weight": 7,
                    "hand_width": 20,
                    "hold_dimensions_sum": 158,
                    "hold_height": 52,
                    "hold_length": 78,
                    "hold_weight": 15,
                    "hold_width": 28
                },
                "availability": {
                    "seats": 2
                },
                "airlines": [
                    "6E"
                ],
                "route": [
                    {
                        "id": "071107194bc90000a949e4ee_0",
                        "combination_id": "071107194bc90000a949e4ee",
                        "flyFrom": "DEL",
                        "flyTo": "DED",
                        "cityFrom": "New Delhi",
                        "cityCodeFrom": "DEL",
                        "cityTo": "Dehradun",
                        "cityCodeTo": "DED",
                        "airline": "6E",
                        "flight_no": 2582,
                        "operating_carrier": "6E",
                        "operating_flight_no": "2582",
                        "fare_basis": "",
                        "fare_category": "M",
                        "fare_classes": "Q",
                        "fare_family": "",
                        "return": 0,
                        "bags_recheck_required": False,
                        "vi_connection": False,
                        "guarantee": False,
                        "equipment": "None",
                        "vehicle_type": "aircraft",
                        "local_arrival": "2023-02-13T19:05:00.000Z",
                        "utc_arrival": "2023-02-13T13:35:00.000Z",
                        "local_departure": "2023-02-13T18:15:00.000Z",
                        "utc_departure": "2023-02-13T12:45:00.000Z"
                    }
                ],
                "booking_token": "Eb9tjHkaPykKHotwqH-75mJkAvmVeWwPE99jkBknHMXii5JXK8q04h2Nwqa8kzJmoBxYP2p8tQIpFXs9QE3iBAWOKLUdPnmaqQ0qDJ-DKI5KYxbQ5uI7naJFutLJFs5YMWTE1jzupsel4pEnElIerr6P_Z_KM33dp7UOZ5Jm5q55OBsjVL4OCX9oijNr-HLPhGroWTl_CnPjMz50qvAciFopnkl3XfkdKixYIirBkOtMM7fH7y7SgwCqba6lUGkh9m4MzU1PinEGnVu9ELEvoTu-6Ne_mqmAIGFiEoaAckvYx-vZmr7CxD18qv-DIvCLLpS_CwHrLnTSUsZZbJOpY5Fzm6JdcYPRd4F-PGjZpAb8o4fXMb6zk34iuGKESHAxsrtUDQLbY8289L2A41_I-aas56CaaQUlcUyfsunTklrTLidAvajukvi35HxGZsaYrx1c--6wmTSI8wBD1kG0PahXRifrAviP7fXbON-im7MO6hxcvPD4i6LgYF19XQodx1lsA9vHXku7yQn1YNASLkUghwKbO4zh1dAvKo2G1KR1fmmQvxTAq2oR9XyZViiyT",
                "deep_link": "https://www.kiwi.com/deep?affilid=apoorvflightsearch&currency=EUR&flightsId=071107194bc90000a949e4ee_0&from=DEL&lang=en&passengers=1&to=DED&booking_token=EqcETx_icUpks-pUMCWlmx5BkSPsbRB4fIXcDTkE_w46TCLh9_6gW5uYqbVRbTCqPMdJsuiFcX2eFwwM0fHJwc_d1tgKNeTqi16MQY-w8jbG0usSU-Mkbjs1Hj5-CqaHhgSyi1fXM3VLAzHvJG92phLf5Dinx66OhDGhsmm0Uyx5dysWaEJXXcfYBY5sM5ENspNOCqYZbizQI_5M91k9kobBXArjm-790vfugZzQjoKEVnduMeHJZegLNLbP4tX_oncRfSxil-kukwo5fhaq6y3wuPQGVfJm44AHHwvH73U6rqYc2tEpU7azOU53UjVNRpYnpc71Q7AMVdCY6gkmuhcU5cgqnmMYb3Km0Cub7GpuEHN11Uw_7lIi2r1zENt8zKaURjNE0_K_hpvjR1_WNjdh8MgcgSclG04ENynZIm02ikkhiAjwfZY_HhizhmDB9",
                "facilitated_booking_available": True,
                "pnr_count": 1,
                "has_airport_change": False,
                "technical_stops": 0,
                "throw_away_ticketing": False,
                "hidden_city_ticketing": False,
                "virtual_interlining": False,
                "local_arrival": "2023-02-13T19:05:00.000Z",
                "utc_arrival": "2023-02-13T13:35:00.000Z",
                "local_departure": "2023-02-13T18:15:00.000Z",
                "utc_departure": "2023-02-13T12:45:00.000Z"
            },
            {
                "id": "071104c24bc600005e667c57_0",
                "flyFrom": "DEL",
                "flyTo": "LKO",
                "cityFrom": "New Delhi",
                "cityCodeFrom": "DEL",
                "cityTo": "Lucknow",
                "cityCodeTo": "LKO",
                "countryFrom": {
                    "code": "IN",
                    "name": "India"
                },
                "countryTo": {
                    "code": "IN",
                    "name": "India"
                },
                "nightsInDest": "None",
                "quality": 78.33328,
                "distance": 423.95,
                "duration": {
                    "departure": 4200,
                    "return": 0,
                    "total": 4200
                },
                "price": 57,
                "conversion": {
                    "EUR": 57
                },
                "bags_price": {
                    "1": 0
                },
                "baglimit": {
                    "hand_height": 36,
                    "hand_length": 56,
                    "hand_weight": 7,
                    "hand_width": 23,
                    "hold_dimensions_sum": 158,
                    "hold_height": 50,
                    "hold_length": 70,
                    "hold_weight": 15,
                    "hold_width": 38
                },
                "availability": {
                    "seats": 1
                },
                "airlines": [
                    "I5"
                ],
                "route": [
                    {
                        "id": "071104c24bc600005e667c57_0",
                        "combination_id": "071104c24bc600005e667c57",
                        "flyFrom": "DEL",
                        "flyTo": "LKO",
                        "cityFrom": "New Delhi",
                        "cityCodeFrom": "DEL",
                        "cityTo": "Lucknow",
                        "cityCodeTo": "LKO",
                        "airline": "I5",
                        "flight_no": 784,
                        "operating_carrier": "",
                        "operating_flight_no": "",
                        "fare_basis": "PNRA000",
                        "fare_category": "M",
                        "fare_classes": "P",
                        "fare_family": "",
                        "return": 0,
                        "bags_recheck_required": False,
                        "vi_connection": False,
                        "guarantee": False,
                        "equipment": "None",
                        "vehicle_type": "aircraft",
                        "local_arrival": "2023-02-10T17:40:00.000Z",
                        "utc_arrival": "2023-02-10T12:10:00.000Z",
                        "local_departure": "2023-02-10T16:30:00.000Z",
                        "utc_departure": "2023-02-10T11:00:00.000Z"
                    }
                ],
                "booking_token": "EfLYdx-hMJ2Fv8Xs85Gnkj0lcL-uDTtmdD3NUp3tt69bGjkezgjaXsyDBZeG5yncJCevk3zX7GUSCttOpsKkRaydTahLppG-XH8ZkCK6u2rFf4Oxzc90TO9lRpkqhCqjReuOateEgdYWLIdkwVCGQlSRcC_EIkdUq94M-hgvHbkwI7ySbF8RlDyPFFXv5e2-O12m2pGy5BxgtFW6THtnVjqJG2HdSZs6d4IkBJnei4e1J9BWQksN1c-niHr3pcEjt_ZSrhCHLXeQIDvpnRqW0EJ0stFQWOQkUl7NwgszM59nGGX61HGnP8pe3BfHc7E8oNK0lO4RzVSt8rux1LBl_CBIKhSMPrHsy9PQBOzREnSXPubDKFoTF9HbbSlcS0ukC4DXTt7Ak-g5qIWrsp2Ezyz6NyerKwFEC4xsBJKmKyMjq-D5xgmdUN6v-2SlBytmrGJWQm1rG6YIJ4NJgrHxIssDyYWCC_FMTEq1vb3IyQ2LWgcO7mqYOD8F6Z7G3-9t9c3Dj7ohYwMPuWbyVMGYunxQjq52_gsKeBsMTz6J6xuIhaCtrUY7g9nXGS3AEjzHHgooP-KFjqBQmpoEYseGxTLW7HnlAutt3SrE0fX51zFs=",
                "deep_link": "https://www.kiwi.com/deep?affilid=apoorvflightsearch&currency=EUR&flightsId=071104c24bc600005e667c57_0&from=DEL&lang=en&passengers=1&to=LKO&booking_token=Ev-Qds0VzCa_CyRRCaqzZeJbwhy9Zq4Dx2F12aztXyfOSJtMrekvTVAihRleDFKJSknGwxfkqgURSVLMh0sNnb4sx9al7TIeJyhtVze0CMsWxEDu8vQjbWd46Ga8lBx0Q9Jh5KUVyIRf5ua41pu9bTPEmFutnixVR0rV2Rdd_nIqhU0HufL7mke8FTeoMEm3vVVWrl8HcKyZhrAQHfKS5fculWM9EHl4iLyIXZ4bVN-FgycKpWFKFUFYi9-R0DG6BgccuqsmxVwuF2VuCXfitaP98oc2cJxKdHO7rg3mCbFbfT4ad37tcS_E2tniq-clZbO-1zgvjoRfJpirBqIcmJBO1I7xrIikhI0IaoXuTPSkMeinP1R5Vb21UNTvpdcYbp5tuy_SGFuhpsZgZfUmqJtLdearOFRLDh_wM_dLYwOegzTPzEqeXvD9WcMoiG38slhmZYPVs26qV-p27m1C2Qw==",
                "facilitated_booking_available": True,
                "pnr_count": 1,
                "has_airport_change": False,
                "technical_stops": 0,
                "throw_away_ticketing": False,
                "hidden_city_ticketing": False,
                "virtual_interlining": False,
                "local_arrival": "2023-02-10T17:40:00.000Z",
                "utc_arrival": "2023-02-10T12:10:00.000Z",
                "local_departure": "2023-02-10T16:30:00.000Z",
                "utc_departure": "2023-02-10T11:00:00.000Z"
            },
            {
                "id": "071113884bc90000ac569ddc_0",
                "flyFrom": "DEL",
                "flyTo": "IDR",
                "cityFrom": "New Delhi",
                "cityCodeFrom": "DEL",
                "cityTo": "Indore",
                "cityCodeTo": "IDR",
                "countryFrom": {
                    "code": "IN",
                    "name": "India"
                },
                "countryTo": {
                    "code": "IN",
                    "name": "India"
                },
                "nightsInDest": "None",
                "quality": 81.666605,
                "distance": 663.59,
                "duration": {
                    "departure": 5700,
                    "return": 0,
                    "total": 5700
                },
                "price": 57,
                "conversion": {
                    "EUR": 57
                },
                "bags_price": {
                    "1": 0
                },
                "baglimit": {
                    "hand_height": 38,
                    "hand_length": 57,
                    "hand_weight": 7,
                    "hand_width": 20,
                    "hold_dimensions_sum": 158,
                    "hold_height": 52,
                    "hold_length": 78,
                    "hold_weight": 15,
                    "hold_width": 28
                },
                "availability": {
                    "seats": 2
                },
                "airlines": [
                    "6E"
                ],
                "route": [
                    {
                        "id": "071113884bc90000ac569ddc_0",
                        "combination_id": "071113884bc90000ac569ddc",
                        "flyFrom": "DEL",
                        "flyTo": "IDR",
                        "cityFrom": "New Delhi",
                        "cityCodeFrom": "DEL",
                        "cityTo": "Indore",
                        "cityCodeTo": "IDR",
                        "airline": "6E",
                        "flight_no": 902,
                        "operating_carrier": "6E",
                        "operating_flight_no": "902",
                        "fare_basis": "",
                        "fare_category": "M",
                        "fare_classes": "L",
                        "fare_family": "",
                        "return": 0,
                        "bags_recheck_required": False,
                        "vi_connection": False,
                        "guarantee": False,
                        "equipment": "None",
                        "vehicle_type": "aircraft",
                        "local_arrival": "2023-02-13T18:20:00.000Z",
                        "utc_arrival": "2023-02-13T12:50:00.000Z",
                        "local_departure": "2023-02-13T16:45:00.000Z",
                        "utc_departure": "2023-02-13T11:15:00.000Z"
                    }
                ],
                "booking_token": "ERGLkuCv7EtYHTRm0mIpwXD5guyhPPhBghdYKemscmmYNTcXadEX42751ZYAvUBpGF2BiX86TAxslndSEruQMTSZqhCiDxrpt2j64ZGrPPa3MGQV26z8mprP4mV5udPrFTdtQ0nABQbzG_PMwCmoyLXSehGnvWOxoQ2DDS3jxSTCn3tZTRthL815OQqNcO2K1244omXUX3H8HC_WRfu8dUSbyItGFT5d9EGzxQxsmXsUkUTbw3H814Qgj65-1jJi-6olB5jQvf3yBaqMAtxwgMyZhC11ZLvpDRnT5Ny3FGQCKKETUGbRFgesrcLHAhwVk38udVr9qx-LwaueHUR903KWE-qAJoQ2B7NW-IgXtd9AcQYAU3KDbs__utdYD1df_tHPq4LyzfSkN4j8Bm4_qjgGP7AQVSdJCCRmA7jeNfYKVHB7p6p6A7txG1Bu1gWH_0N44SXxmta1lWQjiam1SJsi3KhxZRpf40mzNkMpCaucHZ2x6TBOaoX7jb3Un6Z0le0GmO3mRNjO8NoBNAkypW3-a_Icf6Fe_bEPXm8z545svDs9OCcg9D_d6xrZTXMoJ",
                "deep_link": "https://www.kiwi.com/deep?affilid=apoorvflightsearch&currency=EUR&flightsId=071113884bc90000ac569ddc_0&from=DEL&lang=en&passengers=1&to=IDR&booking_token=EUUddKLfb9QIhwCQaQPvv-0jH5Ils7Ii7GV7H3kEzuv7_T9fuJC4NnoZB8kkNJ1580qkIFIvV8wv2G7HOJx45TX7Ms0_TKju3V5BuqIk_Rrnhx8s-4sduprfhjzHJofH-ydQp_z9PocTxw-E8BoeUE5F1PqhWA3Vgj_6xMvq9T2yK1VvGbVzJW7s3CCIf0NNLJLXUBzoApFxTnFLwpwI99zxi1DTh0nJVrtujI_npa5uOP4CMsZN-qnoCGtHG29qeXv5JCVkno4jMEvAZ-aRTjQnEWo5dtMUUCL0aPMzB7DSWmIIf_RtmVqgoBKvNKl3Zn76S1RB50vy_c_d5MLq6vx_1Z438hwgQyXd8TT9Br06_SPsoxzITWnFSUA-pL-dfPRyEQ4BLuXxH84xGlPmaRVIJAYSAQrEZD5vuX9i7PeA=",
                "facilitated_booking_available": True,
                "pnr_count": 1,
                "has_airport_change": False,
                "technical_stops": 0,
                "throw_away_ticketing": False,
                "hidden_city_ticketing": False,
                "virtual_interlining": False,
                "local_arrival": "2023-02-13T18:20:00.000Z",
                "utc_arrival": "2023-02-13T12:50:00.000Z",
                "local_departure": "2023-02-13T16:45:00.000Z",
                "utc_departure": "2023-02-13T11:15:00.000Z"
            },
            {
                "id": "071107194bc7000012a0a41e_0",
                "flyFrom": "DEL",
                "flyTo": "DED",
                "cityFrom": "New Delhi",
                "cityCodeFrom": "DEL",
                "cityTo": "Dehradun",
                "cityCodeTo": "DED",
                "countryFrom": {
                    "code": "IN",
                    "name": "India"
                },
                "countryTo": {
                    "code": "IN",
                    "name": "India"
                },
                "nightsInDest": "None",
                "quality": 76.66662,
                "distance": 208.74,
                "duration": {
                    "departure": 3000,
                    "return": 0,
                    "total": 3000
                },
                "price": 58,
                "conversion": {
                    "EUR": 58
                },
                "bags_price": {
                    "1": 0
                },
                "baglimit": {
                    "hand_height": 38,
                    "hand_length": 57,
                    "hand_weight": 7,
                    "hand_width": 20,
                    "hold_dimensions_sum": 158,
                    "hold_height": 52,
                    "hold_length": 78,
                    "hold_weight": 15,
                    "hold_width": 28
                },
                "availability": {
                    "seats": 2
                },
                "airlines": [
                    "6E"
                ],
                "route": [
                    {
                        "id": "071107194bc7000012a0a41e_0",
                        "combination_id": "071107194bc7000012a0a41e",
                        "flyFrom": "DEL",
                        "flyTo": "DED",
                        "cityFrom": "New Delhi",
                        "cityCodeFrom": "DEL",
                        "cityTo": "Dehradun",
                        "cityCodeTo": "DED",
                        "airline": "6E",
                        "flight_no": 2582,
                        "operating_carrier": "6E",
                        "operating_flight_no": "2582",
                        "fare_basis": "Q0IP",
                        "fare_category": "M",
                        "fare_classes": "X",
                        "fare_family": "",
                        "return": 0,
                        "bags_recheck_required": False,
                        "vi_connection": False,
                        "guarantee": False,
                        "equipment": "None",
                        "vehicle_type": "aircraft",
                        "local_arrival": "2023-02-11T19:05:00.000Z",
                        "utc_arrival": "2023-02-11T13:35:00.000Z",
                        "local_departure": "2023-02-11T18:15:00.000Z",
                        "utc_departure": "2023-02-11T12:45:00.000Z"
                    }
                ],
                "booking_token": "EkjACKD6TBcZJ24Iq4t-uAcT4u4O5g70fbiyTjJIp8RboHktcNOUGSvnh9u8CDCswnc0M575G7DjF4fSbFZvzB8370ynnYpXnc6wLU6XE9kEU38BK8mp9LivDf6mTz3NMQwO4sn5IdV6SlkBT6fr9ccIsfueaSpoDT8iDd2AQnWfrXBlj1TG_mRK07dmGWR1XxKCLOtSWzKR2TkbSB6mYRNXgZwG6A1X5imLU7Z1KhwtC3JQWJu95YtAQS6iw4otlE0nqa_yJ6vCH8Mcf-8XFP-zulfS6JAVuXq-Qkj_THQL3g39zXKdjbAYLbLdUelrvIG8muclUPNJ_BaaWH9Zo1CE5mv1TXmRrzjzoDiqpX24QL7_MNWKzl1oc-LRCmirwAJMVMrhZ3qeNkbj1wkoa_bRCR8b5D8QGCbxHDHMqPL5fqrvRZpl44t11-EqxETn9zBaoQDLw6ggTDCsb1o9PeGZEUqMsxLGnCT2U53R5oYlTbEUFORjEv0yZIel8-nuehg2OxU0ygN8b4geyMcUwvwSTLDpgzsSEeEE4_ql9hXI=",
                "deep_link": "https://www.kiwi.com/deep?affilid=apoorvflightsearch&currency=EUR&flightsId=071107194bc7000012a0a41e_0&from=DEL&lang=en&passengers=1&to=DED&booking_token=EYUYxEjMfL7XH4e5rAYAA4ZybXRN5qq_oAz6d2avrlAfoJmzzhXiD9wf-c7KQSDp1WoXl1KDCbNGJH5-A7OkXqnJxNEWeiypSoIf3DBZwdI_kvSXnjmCQZi15yCTiCAim_38JGqZT2s3wGBwRkIK7Bh9UP0ZSeOh9MciwqULOqTCRpuKDRHnPCNv9ytsRpagNsHVyN-nz-xo81wF-Qmnr3mK5FEXRG3v2c2bqSYZEsS6syWd0NKzqQHzPO5qKq7KkhQiX48nFMkTSEoor-ttK1rfc_TP3hEKn4B3WpAO53ECF1K8UVsQdfhQ5NDJNG03Po9BjQ_Lkw72adHIH8zUdlChrGSvluI-WpOGL6AY9rDitZ5HnLE7Ews8-XRe5xUoEFz1oxR33d0ZoM1zt4wucWqDqSvcm6EhL3FYpqwPz50U=",
                "facilitated_booking_available": True,
                "pnr_count": 1,
                "has_airport_change": False,
                "technical_stops": 0,
                "throw_away_ticketing": False,
                "hidden_city_ticketing": False,
                "virtual_interlining": False,
                "local_arrival": "2023-02-11T19:05:00.000Z",
                "utc_arrival": "2023-02-11T13:35:00.000Z",
                "local_departure": "2023-02-11T18:15:00.000Z",
                "utc_departure": "2023-02-11T12:45:00.000Z"
            },
            {
                "id": "071107194bc80000a590f363_0",
                "flyFrom": "DEL",
                "flyTo": "DED",
                "cityFrom": "New Delhi",
                "cityCodeFrom": "DEL",
                "cityTo": "Dehradun",
                "cityCodeTo": "DED",
                "countryFrom": {
                    "code": "IN",
                    "name": "India"
                },
                "countryTo": {
                    "code": "IN",
                    "name": "India"
                },
                "nightsInDest": "None",
                "quality": 77.333285,
                "distance": 208.74,
                "duration": {
                    "departure": 3300,
                    "return": 0,
                    "total": 3300
                },
                "price": 58,
                "conversion": {
                    "EUR": 58
                },
                "bags_price": {
                    "1": 0
                },
                "baglimit": {
                    "hand_height": 38,
                    "hand_length": 57,
                    "hand_weight": 7,
                    "hand_width": 20,
                    "hold_dimensions_sum": 158,
                    "hold_height": 52,
                    "hold_length": 78,
                    "hold_weight": 15,
                    "hold_width": 28
                },
                "availability": {
                    "seats": 2
                },
                "airlines": [
                    "6E"
                ],
                "route": [
                    {
                        "id": "071107194bc80000a590f363_0",
                        "combination_id": "071107194bc80000a590f363",
                        "flyFrom": "DEL",
                        "flyTo": "DED",
                        "cityFrom": "New Delhi",
                        "cityCodeFrom": "DEL",
                        "cityTo": "Dehradun",
                        "cityCodeTo": "DED",
                        "airline": "6E",
                        "flight_no": 5026,
                        "operating_carrier": "6E",
                        "operating_flight_no": "5026",
                        "fare_basis": "Q0IP",
                        "fare_category": "M",
                        "fare_classes": "X",
                        "fare_family": "",
                        "return": 0,
                        "bags_recheck_required": False,
                        "vi_connection": False,
                        "guarantee": False,
                        "equipment": "None",
                        "vehicle_type": "aircraft",
                        "local_arrival": "2023-02-12T09:15:00.000Z",
                        "utc_arrival": "2023-02-12T03:45:00.000Z",
                        "local_departure": "2023-02-12T08:20:00.000Z",
                        "utc_departure": "2023-02-12T02:50:00.000Z"
                    }
                ],
                "booking_token": "E6Q_n42wSKnHntSKknyK2GCcTXarp3sKF64bmatCHubwhr0_iVP5wlKNLz5SWqQfcRZmbXmRJyMJOtzSdPiVgqVqPNQ0rl1V8FVMwbF8Sj8yt4QExVFJ83PCWBCPHNrrcFqAnwW64eaUC7wTz0OH7fIcLQySgI3elGEtYWPbXB2S9eZPm1ECazAQD4wiukJry0fLNUPdyup64iQ1a3B2eTmf_nDYr1HYRzyHa5jDsloYDg0VbHBVCMzWco6lU93W4mW36NAR7-WeRqPSosBbiRblYUXGCoQEPRGgpVEExQwAj8R6_8sMApnIO06Ap3kOOACX1eaCCJygxi89j2xLvYzfwdKB24Lp54lTlFgqXwoky5CcJ3s3BYQ3xmIPBQnx0j3lNIVKXo5DLvlTy0BDKMprrUDw_2Sdc2r1EDvvOmEv9YHgEuD5wx_DWpLWCOeS2NV9CjeG5PY5tRufKdSmH7djLO1L002NkIasuRkjSlfYoxbs18vVAdT3vrc_77pCKAaLLP7EktawA5rlOzqBPs2BzA2Dly4FX1Fx6SBpWsuE=",
                "deep_link": "https://www.kiwi.com/deep?affilid=apoorvflightsearch&currency=EUR&flightsId=071107194bc80000a590f363_0&from=DEL&lang=en&passengers=1&to=DED&booking_token=E8uppvJNXpy6C4X-HILXoPdr5ZLfOjvyUGT6hChWKBuC5-hFgp2Drhn08tgmn_QxWJWDGyHC3cEvpNTvfUSYOqizc7YlpYHTmJvtpx4sSU9vADBf-fLdnJPoukCVXvSEFv0kEXY7UYFXHYwHq_YSGVr8Wo54F9sDusayvfWnWwPw6YvmD6MFiojMZb9PRTeEP2VEOrbGjm1corb1Im9_TTLODn1hAEYvBfVPklIA-ovwDTXkV56fynXU7k1EfdgO-NXA5eamAzAInRcyjkcx8am8AFhC4r86Z9vzwUB8K7QrMT7pYmSF_QqhKJ4rIGO4T_npoBRO9EsxrteKRU-DW5F0POOU8eLRpPbyvRaPQknFoo-2TwrBG-c6IgEQiskj0O4H83q8_WsMU4i-UE3S0EBWSPP4mDm8n1myA39YYfpw=",
                "facilitated_booking_available": True,
                "pnr_count": 1,
                "has_airport_change": False,
                "technical_stops": 0,
                "throw_away_ticketing": False,
                "hidden_city_ticketing": False,
                "virtual_interlining": False,
                "local_arrival": "2023-02-12T09:15:00.000Z",
                "utc_arrival": "2023-02-12T03:45:00.000Z",
                "local_departure": "2023-02-12T08:20:00.000Z",
                "utc_departure": "2023-02-12T02:50:00.000Z"
            },
            {
                "id": "07111b744bc600005248fb6f_0",
                "flyFrom": "DEL",
                "flyTo": "BHO",
                "cityFrom": "New Delhi",
                "cityCodeFrom": "DEL",
                "cityTo": "Bhopal",
                "cityCodeTo": "BHO",
                "countryFrom": {
                    "code": "IN",
                    "name": "India"
                },
                "countryTo": {
                    "code": "IN",
                    "name": "India"
                },
                "nightsInDest": "None",
                "quality": 81.99994,
                "distance": 588.1,
                "duration": {
                    "departure": 5400,
                    "return": 0,
                    "total": 5400
                },
                "price": 58,
                "conversion": {
                    "EUR": 58
                },
                "bags_price": {
                    "1": 0
                },
                "baglimit": {
                    "hand_height": 35,
                    "hand_length": 55,
                    "hand_weight": 8,
                    "hand_width": 25,
                    "hold_dimensions_sum": 158,
                    "hold_height": 52,
                    "hold_length": 78,
                    "hold_weight": 25,
                    "hold_width": 28,
                    "personal_item_height": 20,
                    "personal_item_length": 40,
                    "personal_item_weight": 5,
                    "personal_item_width": 10
                },
                "availability": {
                    "seats": 6
                },
                "airlines": [
                    "AI"
                ],
                "route": [
                    {
                        "id": "07111b744bc600005248fb6f_0",
                        "combination_id": "07111b744bc600005248fb6f",
                        "flyFrom": "DEL",
                        "flyTo": "BHO",
                        "cityFrom": "New Delhi",
                        "cityCodeFrom": "DEL",
                        "cityTo": "Bhopal",
                        "cityCodeTo": "BHO",
                        "airline": "AI",
                        "flight_no": 435,
                        "operating_carrier": "AI",
                        "operating_flight_no": "435",
                        "fare_basis": "UIP",
                        "fare_category": "M",
                        "fare_classes": "U",
                        "fare_family": "",
                        "return": 0,
                        "bags_recheck_required": False,
                        "vi_connection": False,
                        "guarantee": False,
                        "equipment": "None",
                        "vehicle_type": "aircraft",
                        "local_arrival": "2023-02-10T07:25:00.000Z",
                        "utc_arrival": "2023-02-10T01:55:00.000Z",
                        "local_departure": "2023-02-10T05:55:00.000Z",
                        "utc_departure": "2023-02-10T00:25:00.000Z"
                    }
                ],
                "booking_token": "EUQFrE7oGNpD1dkS8MAObxpu_3kaIbNGp5S5U2gSd8ptGXVNag4vuHS9fn3JXIb8MpiG4IqRgjQ_lTzQdTCwx2m2R1l5pNzvwDvehEC1UbmjuW6zoKx-VvzJNXFASnizdQ8qs_6fNUg3ANR6vThyJbYcVYd48a7zBbEYPsyURY3cfooqvOH7k1pMQ5sL1YgIwQAUfWh9Omd0eGxrKsAwsnaJwwEMwPSAl6zSY5oOdDnSnvtQ9YGaa3MqeRYBnDGVV8Zy9_NzUg3xNHUdJlxnjdLsv0m37g7PRs1P8aelidkbRLYIwB2jawYPYlgwC2ndN7zZ3uTTG4vWNH-dBgZNwlnn8cNB0Knfed_1-gMiAfcoZ66H3UUWBnOKqU5xBj4_hL-cKnaMx7gVW_Bybkte4xAyuV2gA67or-wKI7wJIVRI6XQYqrNm67NT_gJ3bGy9rJqlAP_uRSufVh_E0LwcU5h4CNdfFM29lOmpAyRBX3MX0AyFDIIsz0jFzNK_G-jqTN8tIo2KALGJw-XJhnBdWgk4SSbShA93ttMPfexjoN-STJzfB8sIX2eVGHx3SAT9Rw_akb-6EViQxEllhXTCCaZqG_vV_YzCrJXLo4GfXk_w=",
                "deep_link": "https://www.kiwi.com/deep?affilid=apoorvflightsearch&currency=EUR&flightsId=07111b744bc600005248fb6f_0&from=DEL&lang=en&passengers=1&to=BHO&booking_token=ESHTYnzAs_7A9B737krosQ2B88nGY4jbdFEtA6B8Cn9dL8mkKgeBBhCm3jFlrXZZV0kCpOPyZKswb2nQfx4P2CJnUbXeImfOLnDmSTLuASnPdlrCwS4_q47_viR3LKcCnMcgmu-HQnfWs4iMf_LUh7zcpspNRDsrt6Y6aICjQ0BRAolWSyZEcSnfYthQM974o0E0dg2BpBdvwLTSkSdqLf2VzQmwPhKota-4lSQlZlEvEWV6JDLYMTLnQlSXTggYIA2DDXXsBaHEt2LZ2OBQOXMuHoRVA256SYmdNfsfSbUaAakv3gT1jdEbHYXsK8eX34qjZlmYefqPRL4ai-JhrhYaCp-71w6_l3Y3R2eOA7IdZB3YBShliVUiKf8X_buUFJEjAWGR2QidpHx8G7EGgfLiWZ6kGW7ekHai4JqcLdI_dnPC7xmKzFLcwdlFq5_jOD_Xw1-aRYlXqYGMdlSmdG-4qTR8tT6RUo7UJv7-JFpI=",
                "facilitated_booking_available": True,
                "pnr_count": 1,
                "has_airport_change": False,
                "technical_stops": 0,
                "throw_away_ticketing": False,
                "hidden_city_ticketing": False,
                "virtual_interlining": False,
                "local_arrival": "2023-02-10T07:25:00.000Z",
                "utc_arrival": "2023-02-10T01:55:00.000Z",
                "local_departure": "2023-02-10T05:55:00.000Z",
                "utc_departure": "2023-02-10T00:25:00.000Z"
            },
            {
                "id": "0711019d4bc9000019f8b504_0",
                "flyFrom": "DEL",
                "flyTo": "JLR",
                "cityFrom": "New Delhi",
                "cityCodeFrom": "DEL",
                "cityTo": "Jabalpur",
                "cityCodeTo": "JLR",
                "countryFrom": {
                    "code": "IN",
                    "name": "India"
                },
                "countryTo": {
                    "code": "IN",
                    "name": "India"
                },
                "nightsInDest": "None",
                "quality": 81.99994,
                "distance": 668.53,
                "duration": {
                    "departure": 5400,
                    "return": 0,
                    "total": 5400
                },
                "price": 58,
                "conversion": {
                    "EUR": 58
                },
                "bags_price": {
                    "1": 0
                },
                "baglimit": {
                    "hand_height": 38,
                    "hand_length": 57,
                    "hand_weight": 7,
                    "hand_width": 20,
                    "hold_dimensions_sum": 158,
                    "hold_height": 52,
                    "hold_length": 78,
                    "hold_weight": 15,
                    "hold_width": 28
                },
                "availability": {
                    "seats": 2
                },
                "airlines": [
                    "6E"
                ],
                "route": [
                    {
                        "id": "0711019d4bc9000019f8b504_0",
                        "combination_id": "0711019d4bc9000019f8b504",
                        "flyFrom": "DEL",
                        "flyTo": "JLR",
                        "cityFrom": "New Delhi",
                        "cityCodeFrom": "DEL",
                        "cityTo": "Jabalpur",
                        "cityCodeTo": "JLR",
                        "airline": "6E",
                        "flight_no": 6788,
                        "operating_carrier": "",
                        "operating_flight_no": "",
                        "fare_basis": "N0IP",
                        "fare_category": "M",
                        "fare_classes": "X",
                        "fare_family": "",
                        "return": 0,
                        "bags_recheck_required": False,
                        "vi_connection": False,
                        "guarantee": False,
                        "equipment": "None",
                        "vehicle_type": "aircraft",
                        "local_arrival": "2023-02-13T15:15:00.000Z",
                        "utc_arrival": "2023-02-13T09:45:00.000Z",
                        "local_departure": "2023-02-13T13:45:00.000Z",
                        "utc_departure": "2023-02-13T08:15:00.000Z"
                    }
                ],
                "booking_token": "EyH7CxwEfFthgDTdoxAHK-0UsV-8U0JuyjbD3UJgYBImz2WyYlWzMd1iEXSwZYkk7WfoFKsvRmTaK_GsmXHtPCqZx9ygQ5HWaioysHr4jYedTazVj0hopaEEEcaeKH7JcneXoIJJF4Ais8SRzCrI98RffrwEA40ZhTEzhgUe6mZMmzXiMd5QSt1qPWWbTz2VHcLA7XgcmxDKjtNTdfkORyFMbDRIIeojmYzMYSXqVo5-rE4XS1F1xqQSiEJOJfARhyEKgSQXuMHT2NrYTfxQ5LxO2pAKSWDyYSEsvZ812CsgPJ2oqDB6ln6flC0kLCj8o9ltppwzYzr3aD1mTGOljAVsXxMCw1yozKf6EeaYNZKT8pA4HTwhfUX0V8OfZ_6rg-9TGMDvq2yOUd-CjDODUogQEL3vMlv-8XtEmh2GqbcneULCNQyv5AvCT5Pvh_8YjJFpId5VGxEBQfrTwX0Ih3KDjWAHE4B161azVTuTY4I0L6MZdVYi-W9LIJRkyPzh0MXoet2eCMcEnm2ZBkDphsBPzV04PnPjK2TcLe6TJKiEqek24uEJ8NQ9yqOszYNpM",
                "deep_link": "https://www.kiwi.com/deep?affilid=apoorvflightsearch&currency=EUR&flightsId=0711019d4bc9000019f8b504_0&from=DEL&lang=en&passengers=1&to=JLR&booking_token=EU59GScUPMpXrwhdaqCKOnGMI9NYh2qGD5w_7funNo7UoEjCJ15q9fo0aF8S7NawOiiJxr0YP9v73IbE7LJYWlfXqmhLknez-dmjhZ4vhi8hJW8O80MabqFZRmActE10-MxNaWj7VIYjslZYj7e8CCaaIqrXyMxqpfklqBtYQ5okAacPFRmhsAF7PUEWevl7kOwrlLV8xS192lYOiInyHhyms90JNf3hsANdywQrXrIjWoh5YFQgM9nJ9ZVZMgaOrNwqwWEUHKOBgKXS9Rct90oZmmLdhfaedqP7rH0EuEo2vN-WGQVvDdfZGjgIomd9pggDY39cv3s53aDPEV1kgTkPt0AYtpK9QoX7e3dAgI0m89PeLDucBk1FLKtAm7APsdaa_3OA2iAd-kKd8hdofZBpm7dsc9wtMGbhwgZQR-bE=",
                "facilitated_booking_available": True,
                "pnr_count": 1,
                "has_airport_change": False,
                "technical_stops": 0,
                "throw_away_ticketing": False,
                "hidden_city_ticketing": False,
                "virtual_interlining": False,
                "local_arrival": "2023-02-13T15:15:00.000Z",
                "utc_arrival": "2023-02-13T09:45:00.000Z",
                "local_departure": "2023-02-13T13:45:00.000Z",
                "utc_departure": "2023-02-13T08:15:00.000Z"
            },
            {
                "id": "0711019d4bc70000a211f5f4_0",
                "flyFrom": "DEL",
                "flyTo": "JLR",
                "cityFrom": "New Delhi",
                "cityCodeFrom": "DEL",
                "cityTo": "Jabalpur",
                "cityCodeTo": "JLR",
                "countryFrom": {
                    "code": "IN",
                    "name": "India"
                },
                "countryTo": {
                    "code": "IN",
                    "name": "India"
                },
                "nightsInDest": "None",
                "quality": 81.99994,
                "distance": 668.53,
                "duration": {
                    "departure": 5400,
                    "return": 0,
                    "total": 5400
                },
                "price": 58,
                "conversion": {
                    "EUR": 58
                },
                "bags_price": {
                    "1": 0
                },
                "baglimit": {
                    "hand_height": 38,
                    "hand_length": 57,
                    "hand_weight": 7,
                    "hand_width": 20,
                    "hold_dimensions_sum": 158,
                    "hold_height": 52,
                    "hold_length": 78,
                    "hold_weight": 15,
                    "hold_width": 28
                },
                "availability": {
                    "seats": 3
                },
                "airlines": [
                    "6E"
                ],
                "route": [
                    {
                        "id": "0711019d4bc70000a211f5f4_0",
                        "combination_id": "0711019d4bc70000a211f5f4",
                        "flyFrom": "DEL",
                        "flyTo": "JLR",
                        "cityFrom": "New Delhi",
                        "cityCodeFrom": "DEL",
                        "cityTo": "Jabalpur",
                        "cityCodeTo": "JLR",
                        "airline": "6E",
                        "flight_no": 6788,
                        "operating_carrier": "",
                        "operating_flight_no": "",
                        "fare_basis": "O0IP",
                        "fare_category": "M",
                        "fare_classes": "O",
                        "fare_family": "",
                        "return": 0,
                        "bags_recheck_required": False,
                        "vi_connection": False,
                        "guarantee": False,
                        "equipment": "None",
                        "vehicle_type": "aircraft",
                        "local_arrival": "2023-02-11T15:15:00.000Z",
                        "utc_arrival": "2023-02-11T09:45:00.000Z",
                        "local_departure": "2023-02-11T13:45:00.000Z",
                        "utc_departure": "2023-02-11T08:15:00.000Z"
                    }
                ],
                "booking_token": "EnyHhIa1ICgbjvAqPNgfWttE5IfRkA1qMoeok68xh_s1vc37XyQffvLnWOULU8dg7V60ZMYojbK-8J_AnOB3sedjAK2hoEXXujEHmiARkKPXhpC0RmK0DmpTbogh5JK6EvkX9jTvqpvfqGOeoRfHjw-15aThmmkn710ZbxcGJUafpTczNjbAW8QvbiUDK_4fS5HlTyOUUKG0zmUW31VL3OzX3qH8HpNitXTqRgndjC8JC_z0u70sOU2W3hP4ENfXdOE5dyYt2qPQWVrhMnPSDXTTNb5ESx4YhlwjksnGnwPEQ4_5I4N-21b5s_ggi4OJ8Pl-6I0NIgB7rkTqOXwwpuBGf-G33Oylx6P2kndVFIklKZXCcdD-LtN5jKPKSUvpuDCw6aMY8UCCKGy4WAtsQ2eKDWzVq68RCZt7bm7-L3Yc3PELPhzZ6VgWfT6hgsxDoFSkzaqbh6kJXUhzA5Nj83clEofreni75YS9cWuUQFtpPVuRiR1m_JabqIiDSwKC-s-Lbrl4msAxvDtntuWFts9j30KvbI3lompgrRPmKkLlZczs81iOHVQFQZSlK3WdsV5uoZoPH2PX1f4kHe8OyWLntgF35Tpr3wLf5yQf72y8=",
                "deep_link": "https://www.kiwi.com/deep?affilid=apoorvflightsearch&currency=EUR&flightsId=0711019d4bc70000a211f5f4_0&from=DEL&lang=en&passengers=1&to=JLR&booking_token=EoGeXBG88NODJxo-5-r_Xst-wXlJIb50lVFWXkX2rrUR8hRbeQlxlV2dL9IwLQtFyrwQutn6G6Y2fCdR9m1dhHZS-FcrJwEHfcjNAV6aR46awS0ay3J32H2epoow9yqSJV0o6K7szESU1apM1zde2YHALBr4Epa-Lts8VOapgnGeJKmt5x0uUY2aE43NN5OPy98odZlKmLBMkHOu09M7OXJB_ij-UTNmJEe9R96VStCnJSVlrSaVNK7LL5BJYeux-zXPHqo2nAk7Vdr-qJrVbS-naCfiJ4eD54YZ6QhTvvEfTVXz58AxntI4tLHtOlKGlXEY_esVB6RkOm_tX28nOckqOvyVlQupFYjwxiJyEiMtqkPz-n4MnFnNarvdrboRzBEA0-ZXqZJ_MAXy2sWUDShxqvBbBwkzw8oxGxhkHn0CQ9fyV0OLvZr3XkajNsKidlXA-8NISLdwVAI4XR4hLug==",
                "facilitated_booking_available": True,
                "pnr_count": 1,
                "has_airport_change": False,
                "technical_stops": 0,
                "throw_away_ticketing": False,
                "hidden_city_ticketing": False,
                "virtual_interlining": False,
                "local_arrival": "2023-02-11T15:15:00.000Z",
                "utc_arrival": "2023-02-11T09:45:00.000Z",
                "local_departure": "2023-02-11T13:45:00.000Z",
                "utc_departure": "2023-02-11T08:15:00.000Z"
            },
            {
                "id": "071117634bc900001a5cb5de_0",
                "flyFrom": "DEL",
                "flyTo": "DHM",
                "cityFrom": "New Delhi",
                "cityCodeFrom": "DEL",
                "cityTo": "Dharamshala",
                "cityCodeTo": "DHM",
                "countryFrom": {
                    "code": "IN",
                    "name": "India"
                },
                "countryTo": {
                    "code": "IN",
                    "name": "India"
                },
                "nightsInDest": "None",
                "quality": 81.99994,
                "distance": 408.7,
                "duration": {
                    "departure": 5400,
                    "return": 0,
                    "total": 5400
                },
                "price": 58,
                "conversion": {
                    "EUR": 58
                },
                "bags_price": {
                    "1": 0
                },
                "baglimit": {
                    "hand_height": 36,
                    "hand_length": 54,
                    "hand_weight": 7,
                    "hand_width": 18,
                    "hold_dimensions_sum": 158,
                    "hold_height": 52,
                    "hold_length": 78,
                    "hold_weight": 15,
                    "hold_width": 28
                },
                "availability": {
                    "seats": 2
                },
                "airlines": [
                    "SG"
                ],
                "route": [
                    {
                        "id": "071117634bc900001a5cb5de_0",
                        "combination_id": "071117634bc900001a5cb5de",
                        "flyFrom": "DEL",
                        "flyTo": "DHM",
                        "cityFrom": "New Delhi",
                        "cityCodeFrom": "DEL",
                        "cityTo": "Dharamshala",
                        "cityCodeTo": "DHM",
                        "airline": "SG",
                        "flight_no": 3235,
                        "operating_carrier": "SG",
                        "operating_flight_no": "3235",
                        "fare_basis": "USAV",
                        "fare_category": "M",
                        "fare_classes": "U",
                        "fare_family": "",
                        "return": 0,
                        "bags_recheck_required": False,
                        "vi_connection": False,
                        "guarantee": False,
                        "equipment": "None",
                        "vehicle_type": "aircraft",
                        "local_arrival": "2023-02-13T12:30:00.000Z",
                        "utc_arrival": "2023-02-13T07:00:00.000Z",
                        "local_departure": "2023-02-13T11:00:00.000Z",
                        "utc_departure": "2023-02-13T05:30:00.000Z"
                    }
                ],
                "booking_token": "E4g9k2EY30FNKDjYhm-34kvXfOkeTfEeVNz9zJIj1IHs6ZlMcrKOFO3iijMgQCwW8X4VrsbjLt3HygihCfVxPZMUOinezQubtiqor8ysK8K62RY26HeNwhCn7HGB54AeKUWj1ef3gf_xEAoG5CTvKf2QQjyDZkfc3-oXKpkc-F9Kp_kBk1E-vioZGmZ1LV2h63yF_b_koD-aIrceZOafqK-kSoaS6g5YJ6Afktkvq7ymHzBy_WfD1TucpNs-cqn4p2Dg0FeLMhzla-gB-q9aTLm6mlSbY10_PWRjCAkvD3JLd4bVXSgkKPB68sfB1750t_-UvEPidwkWznohDDbFf1D82iv027M4mgE4FvuwqC-kJ2ca181TwZQaBBzVQY6nqEqCXfvEWyGBCd4HJlOPxtPX14G2xFsDfgkzZtqcHZV4U1WM7YOPuePKfHPo4gfX7uw1fWZM4D_At-WugkOmKBZBYDlV91f4nscc8mASTsPeuO9wUwESXozV9ZExKHUZMop3Sq-mNkTSqHjkEHXQRqRa5F7SCDBzaLbteiHOQGPA=",
                "deep_link": "https://www.kiwi.com/deep?affilid=apoorvflightsearch&currency=EUR&flightsId=071117634bc900001a5cb5de_0&from=DEL&lang=en&passengers=1&to=DHM&booking_token=EzlTZupJ6NBNt8eFwO76Pcv52EQgmx_ZvI7ioIszTQ5EzrIR1itxUN9qD68PlJ7CHh9V_TYlLes0Iks8a58GaEiKYkn_Tl64EnSZ5gjPAETJ0hGRz1bC0VxZltxGanvPg-rXOCYU_tsibOxM3ohDQLJ-87S7vwEe6vCS4zwLPXFLdVSvpahB5UM9HNqfOmXEOnFPFndTls-n3q4WYv_PS1Hi5BBfSORyDl6pHuhZkJjucobxw0it8lEaaHPcL5twEI4LwXrglcYQJi_pxkqJIBTKrtvhSyKGkdH5g2zbqbhxmK0V6ltjNVD09QwrfgcB0sF4-C0xqJLyWi-_HXMO67u75_iOm24Dx_4SowetQsCDn0k0P1pn20Ueula28Gh2fJ6ClfYuB_RryIk7frNwvhzWYlNe75JemempHnKa5rLU=",
                "facilitated_booking_available": True,
                "pnr_count": 1,
                "has_airport_change": False,
                "technical_stops": 0,
                "throw_away_ticketing": False,
                "hidden_city_ticketing": False,
                "virtual_interlining": False,
                "local_arrival": "2023-02-13T12:30:00.000Z",
                "utc_arrival": "2023-02-13T07:00:00.000Z",
                "local_departure": "2023-02-13T11:00:00.000Z",
                "utc_departure": "2023-02-13T05:30:00.000Z"
            },
            {
                "id": "071117634bc90000ec632e4b_0",
                "flyFrom": "DEL",
                "flyTo": "DHM",
                "cityFrom": "New Delhi",
                "cityCodeFrom": "DEL",
                "cityTo": "Dharamshala",
                "cityCodeTo": "DHM",
                "countryFrom": {
                    "code": "IN",
                    "name": "India"
                },
                "countryTo": {
                    "code": "IN",
                    "name": "India"
                },
                "nightsInDest": "None",
                "quality": 83.999935,
                "distance": 408.7,
                "duration": {
                    "departure": 6300,
                    "return": 0,
                    "total": 6300
                },
                "price": 58,
                "conversion": {
                    "EUR": 58
                },
                "bags_price": {
                    "1": 0
                },
                "baglimit": {
                    "hand_height": 36,
                    "hand_length": 54,
                    "hand_weight": 7,
                    "hand_width": 18,
                    "hold_dimensions_sum": 158,
                    "hold_height": 52,
                    "hold_length": 78,
                    "hold_weight": 15,
                    "hold_width": 28
                },
                "availability": {
                    "seats": 2
                },
                "airlines": [
                    "SG"
                ],
                "route": [
                    {
                        "id": "071117634bc90000ec632e4b_0",
                        "combination_id": "071117634bc90000ec632e4b",
                        "flyFrom": "DEL",
                        "flyTo": "DHM",
                        "cityFrom": "New Delhi",
                        "cityCodeFrom": "DEL",
                        "cityTo": "Dharamshala",
                        "cityCodeTo": "DHM",
                        "airline": "SG",
                        "flight_no": 2345,
                        "operating_carrier": "SG",
                        "operating_flight_no": "2345",
                        "fare_basis": "USAV",
                        "fare_category": "M",
                        "fare_classes": "U",
                        "fare_family": "",
                        "return": 0,
                        "bags_recheck_required": False,
                        "vi_connection": False,
                        "guarantee": False,
                        "equipment": "None",
                        "vehicle_type": "aircraft",
                        "local_arrival": "2023-02-13T08:40:00.000Z",
                        "utc_arrival": "2023-02-13T03:10:00.000Z",
                        "local_departure": "2023-02-13T06:55:00.000Z",
                        "utc_departure": "2023-02-13T01:25:00.000Z"
                    }
                ],
                "booking_token": "EeshnL6qNesrhfEHT-Y9sj082JOxKOD8014YDEw4eKTYiWepN66uTfL8HgU2hJ2JfllurgjP19gggRScggUN7i7NFJ5FYVbGcaPRB-nI_2NGI0KgYbl0WPke2mnxngf6d3y1Rl3QdHz0RuLSEuURN-uv9RPfwOSL-9qMAtu98_d8mHbVWoby_-baajhvIJJRzA6Reu-m44nZPJcC9pKdCt33wFQGhy2ens7TOGYdT_jycITO4UAGYYAIf9QeY_TZSVh9HgufQUByVHfRxGdg9i_iZS3YyRGvZyTSScX1VDnHHEdTlZEcHcNdWJd2eJ6xXetZ0k3LjnwkDqWQDMOgFRwHgaUrvPqlsNPSv-VNqcehgwv-D_dzCLCEpjiJQRuAvkyBOWtfO38HXV4J-Cpx3ez8RH9zESGA79xApvM42opJokB94YxCFwc7qaHiGRTxVJp0mitlweArZYPizeSQ4fF53YgbFsvl6HUGq55iNhCXRYryrop9GMZb52LCapf_tT1XxCz0U2oUnYMZ8EHyfuKVPae-u_Uow9SwU0Pw1JHg=",
                "deep_link": "https://www.kiwi.com/deep?affilid=apoorvflightsearch&currency=EUR&flightsId=071117634bc90000ec632e4b_0&from=DEL&lang=en&passengers=1&to=DHM&booking_token=ElwxqdFH2I7j8lEpAs1XbVAQln9kuyLQC9SFkdMVKiQjPXKuLOcDPg-VRBrW4RbUFSAomvFNGeId-nESXil53banowZKrC1FgTngp5Om18kzAeoRqd11PZlTyN-JDc6-Z4oS_69xm2lITfbgHSkjFwlJPFXzjzE34DB-jWEuTL3tjaoDoEZHNuznRVWr1FRuhDW9jVeNEzA__fxOcx1KJ23YLAnuyf1z7eoccH-l5jxnxsUSp8xAUyeFyCmKGcgo4CnaNmcTYLHrTc8k8egNtlHS9Lkif9neJToB46Nxkw81C3Mvv-juFQajX2-Lgj_cmEhFq_08Ae8lqwbX2zVNudonz7hAimK40YWv0WEUbhl-0LJsBeEmMTNQ4BOBfp0pNXgWTzl4ZhfzJvPAlkHWYkyqisRMgkO4VhmRuV7DYzQw=",
                "facilitated_booking_available": True,
                "pnr_count": 1,
                "has_airport_change": False,
                "technical_stops": 0,
                "throw_away_ticketing": False,
                "hidden_city_ticketing": False,
                "virtual_interlining": False,
                "local_arrival": "2023-02-13T08:40:00.000Z",
                "utc_arrival": "2023-02-13T03:10:00.000Z",
                "local_departure": "2023-02-13T06:55:00.000Z",
                "utc_departure": "2023-02-13T01:25:00.000Z"
            },
            {
                "id": "071107194bc700000afa2b80_0",
                "flyFrom": "DEL",
                "flyTo": "DED",
                "cityFrom": "New Delhi",
                "cityCodeFrom": "DEL",
                "cityTo": "Dehradun",
                "cityCodeTo": "DED",
                "countryFrom": {
                    "code": "IN",
                    "name": "India"
                },
                "countryTo": {
                    "code": "IN",
                    "name": "India"
                },
                "nightsInDest": "None",
                "quality": 77.66662,
                "distance": 208.74,
                "duration": {
                    "departure": 3000,
                    "return": 0,
                    "total": 3000
                },
                "price": 59,
                "conversion": {
                    "EUR": 59
                },
                "bags_price": {
                    "1": 0
                },
                "baglimit": {
                    "hand_height": 38,
                    "hand_length": 57,
                    "hand_weight": 7,
                    "hand_width": 20,
                    "hold_dimensions_sum": 158,
                    "hold_height": 52,
                    "hold_length": 78,
                    "hold_weight": 15,
                    "hold_width": 28
                },
                "availability": {
                    "seats": 2
                },
                "airlines": [
                    "6E"
                ],
                "route": [
                    {
                        "id": "071107194bc700000afa2b80_0",
                        "combination_id": "071107194bc700000afa2b80",
                        "flyFrom": "DEL",
                        "flyTo": "DED",
                        "cityFrom": "New Delhi",
                        "cityCodeFrom": "DEL",
                        "cityTo": "Dehradun",
                        "cityCodeTo": "DED",
                        "airline": "6E",
                        "flight_no": 2071,
                        "operating_carrier": "6E",
                        "operating_flight_no": "2071",
                        "fare_basis": "P0IP",
                        "fare_category": "M",
                        "fare_classes": "X",
                        "fare_family": "",
                        "return": 0,
                        "bags_recheck_required": False,
                        "vi_connection": False,
                        "guarantee": False,
                        "equipment": "None",
                        "vehicle_type": "aircraft",
                        "local_arrival": "2023-02-11T17:45:00.000Z",
                        "utc_arrival": "2023-02-11T12:15:00.000Z",
                        "local_departure": "2023-02-11T16:55:00.000Z",
                        "utc_departure": "2023-02-11T11:25:00.000Z"
                    }
                ],
                "booking_token": "E5nIlHOouTJS4sAa3T8frXV5aiS12-kvuDMAFj9s-HSiiFN5rWUIPEhEYxQ8ZMEZJyCyQxRhh3yjBR4ByPXKcQt0veVRmaoKVrtj7dmb9YmPjAj6upr0FH_XqEmkuBbqA8Zj4WalEXuO1LNoJkVuirpyQ559r8pVxuVXe6AnNJ_5rCkf5E6OOf0MV7gLM2LlbLvuWaXMWQVK_aOucKbhOQ531ogGJXaw2MFdewTzYy7HvUToREiArBfzddZsd2LgSaGxitVQKW0bRGZ4hCry8seAyJJLerRQkn0_T6jy-_I_cePBfevWYXnA9OQF73EvCtL7Z2l3VA1FuG6ZqcaxSnemWfVry8wDdk9EGJWprVbsR7CjKu7JWRPGiXAzVhsgxU2TbFpFncirSJTvi1g8Yorwjpu_MOInAjeFowh39NGpV6WO4ztu-E9On_R0UMmEUisFxFKt7U1NPwPCaTA-Am1c8EFg64oXH2tK7LbSwrh0nBJBMls_ZL0UjAZ5y69IAZQVqPt0686r2LuE4rYZtc6ayvemPmCCn7mEiAfBUjF4ooLwMnfWcQKOtaMaZwaD6",
                "deep_link": "https://www.kiwi.com/deep?affilid=apoorvflightsearch&currency=EUR&flightsId=071107194bc700000afa2b80_0&from=DEL&lang=en&passengers=1&to=DED&booking_token=E0cP7WKCdsWbfNosI5K6J_fY3YRWf1UxTvmHsSZNPZmlXkMZ9i0LID8_RtMW0EJ7ECXezfPCqEkUPPZ9wPLUhE4-BsGp7lVS7Y31W1EsdGEMlqQdHdgalUeuqTUKbYwGV5qg94_Et4CYAPt1Zb6hEei5upeFAho-6hbQ0uMBnHNxYoORAThA04IQdne5VQ0SWFaFSTUy39Fk7exRvF4aMB7VYFscfOclPfZrL_tYIPwyrZJR9gqtCMqbM5RooAean6toLSHMMddyaX7D1Q4nOWRnwCbm-RjQCUtVzcTL27q1Yr--J7y8AYiUgYbsuzWxV4uGHvtKbszNeIp6OQBcABxtYF2RbWLKbYPEJ_WchYj1YKhYJeHeioiprOxRtO6e6jYWwEDtw14HrKcNiBmWYznHV5M-WZXFkHJoWVGyuonw=",
                "facilitated_booking_available": True,
                "pnr_count": 1,
                "has_airport_change": False,
                "technical_stops": 0,
                "throw_away_ticketing": False,
                "hidden_city_ticketing": False,
                "virtual_interlining": False,
                "local_arrival": "2023-02-11T17:45:00.000Z",
                "utc_arrival": "2023-02-11T12:15:00.000Z",
                "local_departure": "2023-02-11T16:55:00.000Z",
                "utc_departure": "2023-02-11T11:25:00.000Z"
            },
            {
                "id": "071107194bc90000eeb99738_0",
                "flyFrom": "DEL",
                "flyTo": "DED",
                "cityFrom": "New Delhi",
                "cityCodeFrom": "DEL",
                "cityTo": "Dehradun",
                "cityCodeTo": "DED",
                "countryFrom": {
                    "code": "IN",
                    "name": "India"
                },
                "countryTo": {
                    "code": "IN",
                    "name": "India"
                },
                "nightsInDest": "None",
                "quality": 77.66662,
                "distance": 208.74,
                "duration": {
                    "departure": 3000,
                    "return": 0,
                    "total": 3000
                },
                "price": 59,
                "conversion": {
                    "EUR": 59
                },
                "bags_price": {
                    "1": 0
                },
                "baglimit": {
                    "hand_height": 40,
                    "hand_length": 55,
                    "hand_weight": 7,
                    "hand_width": 20,
                    "hold_dimensions_sum": 158,
                    "hold_height": 52,
                    "hold_length": 78,
                    "hold_weight": 15,
                    "hold_width": 28,
                    "personal_item_height": 30,
                    "personal_item_length": 40,
                    "personal_item_weight": 3,
                    "personal_item_width": 15
                },
                "availability": {
                    "seats": "None"
                },
                "airlines": [
                    "UK"
                ],
                "route": [
                    {
                        "id": "071107194bc90000eeb99738_0",
                        "combination_id": "071107194bc90000eeb99738",
                        "flyFrom": "DEL",
                        "flyTo": "DED",
                        "cityFrom": "New Delhi",
                        "cityCodeFrom": "DEL",
                        "cityTo": "Dehradun",
                        "cityCodeTo": "DED",
                        "airline": "UK",
                        "flight_no": 617,
                        "operating_carrier": "UK",
                        "operating_flight_no": "617",
                        "fare_basis": "W0DNINYS",
                        "fare_category": "M",
                        "fare_classes": "W",
                        "fare_family": "",
                        "return": 0,
                        "bags_recheck_required": False,
                        "vi_connection": False,
                        "guarantee": False,
                        "equipment": "None",
                        "vehicle_type": "aircraft",
                        "local_arrival": "2023-02-13T14:50:00.000Z",
                        "utc_arrival": "2023-02-13T09:20:00.000Z",
                        "local_departure": "2023-02-13T14:00:00.000Z",
                        "utc_departure": "2023-02-13T08:30:00.000Z"
                    }
                ],
                "booking_token": "E9fcQwNRJQdG0l08bAUCWP2m6sdSuQzfHzVEYRXwb2encCVCm1ymZAFpLVi-3_nGSf433SZuMSjs-0Ni6Bw19NMZ84vzvWZqbljnmol_CQ_UsYajmPsGLLFZctfftx4wcH6I2W6ZeeH7mq59pSwr9T3G2MANtCj01DYtNwRdBSM2D5DhRYb7i-78krcln1zW18zuQjiWeLZQio6CHggwt1BBlPPUo4Sz-wV9erFQIYLm5Ebj3o0sUN3HO2Lf-AEOndSnE0lZwBUBm67657IlDa6w5PlQ6tcxdwu6qbgBzHc8Qus0ws8URpi4YZ8sCvbqzpxDsq5___HHh6xjLMASKz7EYtjoZkv129nas9PrNzDlvk4Tu5ybxUitjeArz9uXQc12Uy8S0xYcactu26InMWBVRhiY-N1oMOWsq8rHkyg3itnAZD1UETXycwUttwSRsYIaZ_WCm-fYpzYs_vJCdVOOsFDI9ZhwI9YhvUL27HD5SjzdOJ36DscoGwSOg0UApVH2C2dHD6Oq2uU_28K5G-EYqTuz5-02xaYFjKRCqUd0BPueqOXxTJUrI7OTczfMa6aVLw0LKAbCsWcoA7cteRBFXByizoyHnBi4tVPU7A5r_TbWtwyq20tjsueQwQBqD",
                "deep_link": "https://www.kiwi.com/deep?affilid=apoorvflightsearch&currency=EUR&flightsId=071107194bc90000eeb99738_0&from=DEL&lang=en&passengers=1&to=DED&booking_token=Ey6BIbvFhZpuF2RS5YdX386HDemHG-SKQVYrbb7aGPW7V5OvZzmVIr48UULSMWwwl5Hea62QBmjFFbeIvvvH8kGZ6gTuCtrVLZbuhixyPpe7UZmfkq5dEUYGxA6kXxxE3Mbx-UPF5iSaCOTBflJssH95Pggb7_LUBAFzyDdl6afTe0RU-tVnGO0M1wqN00xNfBVV4O3OJdeRckn0zI_RmM30p-v6aqf2CnIpg1_pNNlF-qM1Dl1lc00t4XsRaNO6TMI4WyoTRLWqqLG-Cb0LlXESIrL9_s_XAY6Gr4Wmb6qrEa3KnwWnUOaL_ZXVW6bRaT9bDzHeK_0FqFpvUH7R88wW1LbQj4ULnKC1YjaKv4Pb7wpuJEe-3Is-b9XKmcsTeOHBwXJTmK88xnW03ykwrx_W-4k4w3xeGTsBIz_XvMBo5T9OSMFCZa-wzTaT89MpqjcwWIeWP5vnKj6x7PPMUwqX8XVzqQ9wx1LXHpEE8SK1cPnndkleTU7muvbapeMpe",
                "facilitated_booking_available": True,
                "pnr_count": 1,
                "has_airport_change": False,
                "technical_stops": 0,
                "throw_away_ticketing": False,
                "hidden_city_ticketing": False,
                "virtual_interlining": False,
                "local_arrival": "2023-02-13T14:50:00.000Z",
                "utc_arrival": "2023-02-13T09:20:00.000Z",
                "local_departure": "2023-02-13T14:00:00.000Z",
                "utc_departure": "2023-02-13T08:30:00.000Z"
            },
            {
                "id": "071107194bc6000050409ad1_0",
                "flyFrom": "DEL",
                "flyTo": "DED",
                "cityFrom": "New Delhi",
                "cityCodeFrom": "DEL",
                "cityTo": "Dehradun",
                "cityCodeTo": "DED",
                "countryFrom": {
                    "code": "IN",
                    "name": "India"
                },
                "countryTo": {
                    "code": "IN",
                    "name": "India"
                },
                "nightsInDest": "None",
                "quality": 78.333285,
                "distance": 208.74,
                "duration": {
                    "departure": 3300,
                    "return": 0,
                    "total": 3300
                },
                "price": 59,
                "conversion": {
                    "EUR": 59
                },
                "bags_price": {
                    "1": 0
                },
                "baglimit": {
                    "hand_height": 38,
                    "hand_length": 57,
                    "hand_weight": 7,
                    "hand_width": 20,
                    "hold_dimensions_sum": 158,
                    "hold_height": 52,
                    "hold_length": 78,
                    "hold_weight": 15,
                    "hold_width": 28
                },
                "availability": {
                    "seats": 2
                },
                "airlines": [
                    "6E"
                ],
                "route": [
                    {
                        "id": "071107194bc6000050409ad1_0",
                        "combination_id": "071107194bc6000050409ad1",
                        "flyFrom": "DEL",
                        "flyTo": "DED",
                        "cityFrom": "New Delhi",
                        "cityCodeFrom": "DEL",
                        "cityTo": "Dehradun",
                        "cityCodeTo": "DED",
                        "airline": "6E",
                        "flight_no": 5026,
                        "operating_carrier": "6E",
                        "operating_flight_no": "5026",
                        "fare_basis": "P0IP",
                        "fare_category": "M",
                        "fare_classes": "X",
                        "fare_family": "",
                        "return": 0,
                        "bags_recheck_required": False,
                        "vi_connection": False,
                        "guarantee": False,
                        "equipment": "None",
                        "vehicle_type": "aircraft",
                        "local_arrival": "2023-02-10T09:15:00.000Z",
                        "utc_arrival": "2023-02-10T03:45:00.000Z",
                        "local_departure": "2023-02-10T08:20:00.000Z",
                        "utc_departure": "2023-02-10T02:50:00.000Z"
                    }
                ],
                "booking_token": "Ex-CbzjGu3w28vkvgN8xL9712huHoVjjC5bENVgeNDbzRjpqV9MXk_NL9T2tThogTDXWB6L6iC0h1MK0YNsjtbVkkpkH4ixS-bIPOb5x5L5IM0-rW8515DNdjUDGtz5245drLvm5f1WqM5D00jA06m90BTfQfT89DHJ9Dz5WxbFZE-EjT70A2OzGDd1zo7EkX7T9m4y-ZId5HsZcJI2KZL1dgvs6qik1ZIOjoq8le1rqIqcxotWcG2exrub10Myfp4sdWyHyZmEIifBNm2CZrxrM9KvfvN9WJsjTzIDzhKFcNZE4gTCaxOhjdBCCFCWnZHLjFRtWOOZTqAjp90axXE_nYztYxsPVKIXwDLGldEVAd_IN7n9-5DrgTYijHfdDajp9ZKAQXuJ7mMB9ExUzjCpeM23GBqd4CHgtl8GgWAE90xPs2H6_gDpsb22-btrCI9iog_Ipk284IUqXsHXBw4o1gNQZ6jyGCUhKKaL5qGVRiNwm4WWDjGM7wfI63bXjReFYxKp9Syi2wwyxGFI_8F1E6UMT1fvLfkm2s9-ihKFBmbCWWkBQcewLhnlqegdbI",
                "deep_link": "https://www.kiwi.com/deep?affilid=apoorvflightsearch&currency=EUR&flightsId=071107194bc6000050409ad1_0&from=DEL&lang=en&passengers=1&to=DED&booking_token=EHn3kNvkTTKSXcTn9RAsQPDwU8ntjuP0KORwItCuPeV1PJZD0mHvioHAtkqR4klcokLGy_FXB7ksvQDtxh1pFfaqF_rgyxX4N1FhlK42Y9z54BhOdniB8X7NdPOZ2U33cq1w7jaJumiqb5d_8EYBaOPL9Ozz6dMNvxTQI51Y_jgumsxnhzpuKv2UbDpS4W_Jl_4m6HF2Cjxmu9UX8U1BjaLxgctY8E259PWjsyAP1ytPjBSUMQQOrSmBP5WKFtv4DaAbAu-W_ZAi8RCHvGuG6TS62y3hw_S4C55ATajl659TBvOTTv3t7or2gPzWASgmbe0Wa7laedjAtBA__ffqoxZT3Qokl5yZU2LkjjNfDYolObQto-6pnVtvXziiboCbJK-aHFSgRXJrq9I-Zk77oUnzX-Wuu6lciZjU-oSaahbA=",
                "facilitated_booking_available": True,
                "pnr_count": 1,
                "has_airport_change": False,
                "technical_stops": 0,
                "throw_away_ticketing": False,
                "hidden_city_ticketing": False,
                "virtual_interlining": False,
                "local_arrival": "2023-02-10T09:15:00.000Z",
                "utc_arrival": "2023-02-10T03:45:00.000Z",
                "local_departure": "2023-02-10T08:20:00.000Z",
                "utc_departure": "2023-02-10T02:50:00.000Z"
            },
            {
                "id": "071107194bc90000a4d730cc_0",
                "flyFrom": "DEL",
                "flyTo": "DED",
                "cityFrom": "New Delhi",
                "cityCodeFrom": "DEL",
                "cityTo": "Dehradun",
                "cityCodeTo": "DED",
                "countryFrom": {
                    "code": "IN",
                    "name": "India"
                },
                "countryTo": {
                    "code": "IN",
                    "name": "India"
                },
                "nightsInDest": "None",
                "quality": 79.666615,
                "distance": 208.74,
                "duration": {
                    "departure": 3900,
                    "return": 0,
                    "total": 3900
                },
                "price": 59,
                "conversion": {
                    "EUR": 59
                },
                "bags_price": {
                    "1": 0
                },
                "baglimit": {
                    "hand_height": 38,
                    "hand_length": 57,
                    "hand_weight": 7,
                    "hand_width": 20,
                    "hold_dimensions_sum": 158,
                    "hold_height": 52,
                    "hold_length": 78,
                    "hold_weight": 15,
                    "hold_width": 28
                },
                "availability": {
                    "seats": 2
                },
                "airlines": [
                    "6E"
                ],
                "route": [
                    {
                        "id": "071107194bc90000a4d730cc_0",
                        "combination_id": "071107194bc90000a4d730cc",
                        "flyFrom": "DEL",
                        "flyTo": "DED",
                        "cityFrom": "New Delhi",
                        "cityCodeFrom": "DEL",
                        "cityTo": "Dehradun",
                        "cityCodeTo": "DED",
                        "airline": "6E",
                        "flight_no": 2134,
                        "operating_carrier": "6E",
                        "operating_flight_no": "2134",
                        "fare_basis": "",
                        "fare_category": "M",
                        "fare_classes": "L",
                        "fare_family": "",
                        "return": 0,
                        "bags_recheck_required": False,
                        "vi_connection": False,
                        "guarantee": False,
                        "equipment": "None",
                        "vehicle_type": "aircraft",
                        "local_arrival": "2023-02-13T15:00:00.000Z",
                        "utc_arrival": "2023-02-13T09:30:00.000Z",
                        "local_departure": "2023-02-13T13:55:00.000Z",
                        "utc_departure": "2023-02-13T08:25:00.000Z"
                    }
                ],
                "booking_token": "E6AhndvmO1NtGpXjDZsvLLx_YHvES3NscWFYlHFB3dk6fWpIPgsLXKw4OMlrNjgkexeCey79J31PqzL403oH5PJzD9Dm35fnU8KbhsArzozarERaseszR76dMNwuznX114bO0bLw3eriZgoYtTO3zDABJHGJPbuVawX6bys4svJPl5t4zwW-FgKdVJTUis2V84PBKBM8ZhitpPGdk3WERdnsQiTdNP2xC-Teqgd8oSpYyuZYNN0asELK-0g801RWW2ij49rn5LqGsl8MP0CjZ10zS1XZiownbgfdqhDYoHIRVv91gq3mDy21ZgMaMoljTh1EvahBjnQyrR1sWg_G4gwPOkCfljRDS04XrG3GBOY0qbhmAyBT9xpNuGGnHDgzhXZNICoTbiGsXB3rzSfPqjphO4AtMRh3hIaLqX2CyVEQDZw7of63nY-8rnLkWbxaHSqFvmPPiu2xA2dqeoweCVHPilhN3da7JM5AFwSMXtMKBis1JO_VIBwNvR3whwy-rA7qv6-M8pzf2HxmvKugV7Uqp_PKPtC0gmopTn4QnyKA=",
                "deep_link": "https://www.kiwi.com/deep?affilid=apoorvflightsearch&currency=EUR&flightsId=071107194bc90000a4d730cc_0&from=DEL&lang=en&passengers=1&to=DED&booking_token=EyKJebeFAP38XLRMlKBWtj-_jNzduRxz_ieQ_jlvfN7JK9LgTRdV0MChZwypl2uDEU47oAeqKHpSqUYVgXE4me2k4flo3ocFnDVi6hhDO881_yUpvcz3LnDIS_HHsaBZ45bsyvAVraimpbpn3RCuAC-4PTSwdxkSQDhq54CWVEPFqztYtYUinnK4lmGAFcDMtIYF6ZnysQdXI0w6jrwaXRlFA0GpyU-GOUMp1A6hIx9WfxDhPhBqqHEeqxD26xzn8FjBaNs7FJ_dW3tUnDv6adeMC8_09T1NaUrpgLX_xugx577YwCFwRbI5e0PrmDAB-QZcv0SukWWtS4oZIjads94_wxBKieYOdtktL0ncxCT6OJf7y5QMdWrE3kRG83g1va_nev6t_pma2kkhCi5jYdA==",
                "facilitated_booking_available": True,
                "pnr_count": 1,
                "has_airport_change": False,
                "technical_stops": 0,
                "throw_away_ticketing": False,
                "hidden_city_ticketing": False,
                "virtual_interlining": False,
                "local_arrival": "2023-02-13T15:00:00.000Z",
                "utc_arrival": "2023-02-13T09:30:00.000Z",
                "local_departure": "2023-02-13T13:55:00.000Z",
                "utc_departure": "2023-02-13T08:25:00.000Z"
            },
            {
                "id": "071104c24bc90000db97d9a9_0",
                "flyFrom": "DEL",
                "flyTo": "LKO",
                "cityFrom": "New Delhi",
                "cityCodeFrom": "DEL",
                "cityTo": "Lucknow",
                "cityCodeTo": "LKO",
                "countryFrom": {
                    "code": "IN",
                    "name": "India"
                },
                "countryTo": {
                    "code": "IN",
                    "name": "India"
                },
                "nightsInDest": "None",
                "quality": 80.999945,
                "distance": 423.95,
                "duration": {
                    "departure": 4500,
                    "return": 0,
                    "total": 4500
                },
                "price": 59,
                "conversion": {
                    "EUR": 59
                },
                "bags_price": {
                    "1": 0
                },
                "baglimit": {
                    "hand_height": 40,
                    "hand_length": 55,
                    "hand_weight": 7,
                    "hand_width": 20,
                    "hold_dimensions_sum": 158,
                    "hold_height": 52,
                    "hold_length": 78,
                    "hold_weight": 15,
                    "hold_width": 28,
                    "personal_item_height": 30,
                    "personal_item_length": 40,
                    "personal_item_weight": 3,
                    "personal_item_width": 15
                },
                "availability": {
                    "seats": 3
                },
                "airlines": [
                    "UK"
                ],
                "route": [
                    {
                        "id": "071104c24bc90000db97d9a9_0",
                        "combination_id": "071104c24bc90000db97d9a9",
                        "flyFrom": "DEL",
                        "flyTo": "LKO",
                        "cityFrom": "New Delhi",
                        "cityCodeFrom": "DEL",
                        "cityTo": "Lucknow",
                        "cityCodeTo": "LKO",
                        "airline": "UK",
                        "flight_no": 641,
                        "operating_carrier": "UK",
                        "operating_flight_no": "641",
                        "fare_basis": "Q0DNINYS",
                        "fare_category": "M",
                        "fare_classes": "Q",
                        "fare_family": "",
                        "return": 0,
                        "bags_recheck_required": False,
                        "vi_connection": False,
                        "guarantee": False,
                        "equipment": "None",
                        "vehicle_type": "aircraft",
                        "local_arrival": "2023-02-13T14:50:00.000Z",
                        "utc_arrival": "2023-02-13T09:20:00.000Z",
                        "local_departure": "2023-02-13T13:35:00.000Z",
                        "utc_departure": "2023-02-13T08:05:00.000Z"
                    }
                ],
                "booking_token": "EfzcssxYBrf8FfuTesMNxCrUHze1XFnlbPSm7lVVhkYGOLDptW8PVTod6J6Tu1rrFiJh5OWuEG8HhhPhbk0o-4TRMH2k-H_0MZFvvskeLBvLD3o5E8PMYxWVrFyDY7j0ahbZnXS9tCoZKbeRsd330CJIFX3YEr7hHbZhkeFUBhvTOTu3LxQeqQJDYn6p0xqoAKybK7_Z1QdZ5eWtjK71ruphdqVJDUWg3k70mioUnXi_-gJK_Hw86JtZMEwulxTEL4aKA5Th6iXBMSvpv1LZ6DwcuqaH05PyOfF8bW6fIJp6F6XLcOs5uZNNGPPjMjaaqnSFinBFoqQ7rCz4EwvUp4WSdBvc4bft7Rap4uxaq_EREYnZW9b1MJjsL3bWham33jDVjqxzXdcHU7-oOEtZeFRWOYy3r8pu80v47J9kXspAIxMar25v-f_vyhR2qATBNY1V06CFpFTFONTYXgx9T5UfLsDgenj6nknQdf0vcANe9f011oXb3RAmil3sZdTSme5V7mp6WCfPDv2jupl_6F_ITrEBjyee-atiNRBRQNwn7Bu7XhrrHr4kluAeIKyWYz0FOIsltd-7OtF8JpEy7q1NgJDV2fQavYI7ztPx7ZgNjTNftLn0vz0Kmlw8MwsjK",
                "deep_link": "https://www.kiwi.com/deep?affilid=apoorvflightsearch&currency=EUR&flightsId=071104c24bc90000db97d9a9_0&from=DEL&lang=en&passengers=1&to=LKO&booking_token=EHNV7SIUEg8i2NFAW1H7OuuFeIQ1wNrERF_okbikWJw-ufjLXgSgIw_zEB2hQK0Mj3W_4mlAs-H3vEcUa7hodVGDpJdJ1QRz4_A3w-N0WCEwuhHOTyw77ghnYdmJ4aTK9I3Mx4lQdqFcYPdcsQ3hxRs4hKX5Uj-LtfjEc39q2BY-z3YNFtKczsV81cKPIy8q9n_kZqXoIbCZV657ZiulKFYb9iySUw5djtZmjKLu74BklQ-ae5k5YRLZiLllGFMscKkQPHye1-PxIuEZ4xieNH_U50V36kbYFLz1WiEqFr4EOVvHk3ELf4xWB4mBio1q_zabZewKBsEclR31K7wqoYR5Lh__lrp62UySJjjCn3DOwUyliX9-ByjUnySQRJoWbdxcBH739JLPN564byvcehax7v3ek114XknlPGXimcgb0YS8BeR3uhjgcruSqQ4GO7JDK5xd786LBLwsJrgSNxjw28YHsjNXWpdPs5BS6YWBoNkC4WGqBw1k5EVlWwDDi",
                "facilitated_booking_available": True,
                "pnr_count": 1,
                "has_airport_change": False,
                "technical_stops": 0,
                "throw_away_ticketing": False,
                "hidden_city_ticketing": False,
                "virtual_interlining": False,
                "local_arrival": "2023-02-13T14:50:00.000Z",
                "utc_arrival": "2023-02-13T09:20:00.000Z",
                "local_departure": "2023-02-13T13:35:00.000Z",
                "utc_departure": "2023-02-13T08:05:00.000Z"
            },
            {
                "id": "071113884bc8000024ae13e0_0",
                "flyFrom": "DEL",
                "flyTo": "IDR",
                "cityFrom": "New Delhi",
                "cityCodeFrom": "DEL",
                "cityTo": "Indore",
                "cityCodeTo": "IDR",
                "countryFrom": {
                    "code": "IN",
                    "name": "India"
                },
                "countryTo": {
                    "code": "IN",
                    "name": "India"
                },
                "nightsInDest": "None",
                "quality": 82.333275,
                "distance": 663.59,
                "duration": {
                    "departure": 5100,
                    "return": 0,
                    "total": 5100
                },
                "price": 59,
                "conversion": {
                    "EUR": 59
                },
                "bags_price": {
                    "1": 0
                },
                "baglimit": {
                    "hand_height": 38,
                    "hand_length": 57,
                    "hand_weight": 7,
                    "hand_width": 20,
                    "hold_dimensions_sum": 158,
                    "hold_height": 52,
                    "hold_length": 78,
                    "hold_weight": 15,
                    "hold_width": 28
                },
                "availability": {
                    "seats": 2
                },
                "airlines": [
                    "6E"
                ],
                "route": [
                    {
                        "id": "071113884bc8000024ae13e0_0",
                        "combination_id": "071113884bc8000024ae13e0",
                        "flyFrom": "DEL",
                        "flyTo": "IDR",
                        "cityFrom": "New Delhi",
                        "cityCodeFrom": "DEL",
                        "cityTo": "Indore",
                        "cityCodeTo": "IDR",
                        "airline": "6E",
                        "flight_no": 6231,
                        "operating_carrier": "6E",
                        "operating_flight_no": "6231",
                        "fare_basis": "L0IP",
                        "fare_category": "M",
                        "fare_classes": "X",
                        "fare_family": "",
                        "return": 0,
                        "bags_recheck_required": False,
                        "vi_connection": False,
                        "guarantee": False,
                        "equipment": "None",
                        "vehicle_type": "aircraft",
                        "local_arrival": "2023-02-12T06:40:00.000Z",
                        "utc_arrival": "2023-02-12T01:10:00.000Z",
                        "local_departure": "2023-02-12T05:15:00.000Z",
                        "utc_departure": "2023-02-11T23:45:00.000Z"
                    }
                ],
                "booking_token": "EmAjWgKjPQGh-87nu3UMlhG7iJldSiI8q4iic6LJtW0wOuh-LhPK2mrXKoSBPwT2OlnFEbz59lr2No1pmqTwhF7kW6mrT1odM7O3xBkiwuhFdfPCuZWnl3AOvBcz9jWmlSImszTa0GmvG-W44Y4T6eY_p3ot11qsEQuGL8L0v-A5tCk-IztDGwVRfwOUIZ-dD6X-06GOhdy8LdGy8H615dBqRLCcLWob-2QTX0M1AE85iEF_WAf5_dTf4SQyoaEnVxuMofH_qMgCPdf74gglevo6BnWqUNSFhr_vHiBYQA508KpilSGm7v-v099WR-xzUWfCHFHtUZtqBxEPLE95IoIKKqAfb0Mj-ZaIGpIOk9u3nhQsNIa34Chqv2SOSnlo1ojz-TLL12klW0v0VxrPVG_rWeLr-ebArJBAVwQ86lVq5kP3dt4_3OO-h7vrMqit6t9tS9JeA5WqqXlg6hxrxjOHIoR1tSsc_fSjpXoy9bd3U2R5cuZ8gmUVmPqEEsilBJlnuLVqKGa8ylRXbUr4yrsouCnZkpG3A8YvdP6wUMuWEO6_kdtY851A9fZRSY3W7",
                "deep_link": "https://www.kiwi.com/deep?affilid=apoorvflightsearch&currency=EUR&flightsId=071113884bc8000024ae13e0_0&from=DEL&lang=en&passengers=1&to=IDR&booking_token=E0NlAEML3GpQ9Ifc85zZvV1A_Rh3Ay6Kbk8kVuzgo0cD4a0yf-9nXI3V8aEq6-F5AZuiuwBg41vO02a73wDUAeLFPVBQ84ZKHm04t9n14Fsj-DMh5c3K-PB2OmrIxoaNDy1mHHm1yjvzPCnwDWhJo-cUH_qnqUCUPFsFLnVUSYn8__2737fqvz1pADYCvW_cUmZmkcA51h8nOQCUz_Zat3ApaWBrZry4oPIsgFzWBRghXSqT29AOCDCM3G93SCpfy0wBxitHpiBBTrNjv2jr4NPdiBAMiYul84A1eHNGIWweDIM2i6nEvIUUPW8JRHgZiZ8PCTx46I8HNTGzBhp53_tGSzplMeVTFdVi51RF8PAWOL69tRNLMyqNAO5H_afcyRQ5SiGMYsGFEHLg147xhZ729Ctf5bpr2DaSbHS_exGg=",
                "facilitated_booking_available": True,
                "pnr_count": 1,
                "has_airport_change": False,
                "technical_stops": 0,
                "throw_away_ticketing": False,
                "hidden_city_ticketing": False,
                "virtual_interlining": False,
                "local_arrival": "2023-02-12T06:40:00.000Z",
                "utc_arrival": "2023-02-12T01:10:00.000Z",
                "local_departure": "2023-02-12T05:15:00.000Z",
                "utc_departure": "2023-02-11T23:45:00.000Z"
            },
            {
                "id": "071113884bc900004ee9d2ac_0",
                "flyFrom": "DEL",
                "flyTo": "IDR",
                "cityFrom": "New Delhi",
                "cityCodeFrom": "DEL",
                "cityTo": "Indore",
                "cityCodeTo": "IDR",
                "countryFrom": {
                    "code": "IN",
                    "name": "India"
                },
                "countryTo": {
                    "code": "IN",
                    "name": "India"
                },
                "nightsInDest": "None",
                "quality": 82.333275,
                "distance": 663.59,
                "duration": {
                    "departure": 5100,
                    "return": 0,
                    "total": 5100
                },
                "price": 59,
                "conversion": {
                    "EUR": 59
                },
                "bags_price": {
                    "1": 0
                },
                "baglimit": {
                    "hand_height": 38,
                    "hand_length": 57,
                    "hand_weight": 7,
                    "hand_width": 20,
                    "hold_dimensions_sum": 158,
                    "hold_height": 52,
                    "hold_length": 78,
                    "hold_weight": 15,
                    "hold_width": 28
                },
                "availability": {
                    "seats": 2
                },
                "airlines": [
                    "6E"
                ],
                "route": [
                    {
                        "id": "071113884bc900004ee9d2ac_0",
                        "combination_id": "071113884bc900004ee9d2ac",
                        "flyFrom": "DEL",
                        "flyTo": "IDR",
                        "cityFrom": "New Delhi",
                        "cityCodeFrom": "DEL",
                        "cityTo": "Indore",
                        "cityCodeTo": "IDR",
                        "airline": "6E",
                        "flight_no": 6231,
                        "operating_carrier": "6E",
                        "operating_flight_no": "6231",
                        "fare_basis": "",
                        "fare_category": "M",
                        "fare_classes": "L",
                        "fare_family": "",
                        "return": 0,
                        "bags_recheck_required": False,
                        "vi_connection": False,
                        "guarantee": False,
                        "equipment": "None",
                        "vehicle_type": "aircraft",
                        "local_arrival": "2023-02-13T06:40:00.000Z",
                        "utc_arrival": "2023-02-13T01:10:00.000Z",
                        "local_departure": "2023-02-13T05:15:00.000Z",
                        "utc_departure": "2023-02-12T23:45:00.000Z"
                    }
                ],
                "booking_token": "E659JBB52gycbyUFfsBPHWzcOpvbFeJ6Wbm5yPe1jjvov9In9BL5uWgLIpGwM90W5Jo040_zZsqPp6QS_Gg5NzRgmCdiQ5tquvsdDZX2nDGhb54eWbkd35bFPPUFZSP_tEgmUy_C0l8--_d3vo0vTrlxVklzyWCZhlTTLMWY5dZ4jBAJ4ijmck4SztkJMDjsC5nagUA376PfPbllM_fIT3WEj8-2LCROEdroKYCW5WmdustQthNQ9an_snJz0PBfB0nEADYQS_hPfUmQiYJdTtGfPx7hedy3gUx-wFlAS6NwW47yvtmHf3Ik1HGf09VlzTYXcqa9ISznQlax-HtTPAVrFh0RzA6YDpa60AsfNrwV8zvoUGiYPVW5U7h1qvcJh60ir8Dnv9H5NU6JOjG-zrI0_jZ8Npqk3iNSMVO9Cshz8w-N6lVoj-kLqrKLVaV3BgS9SxA12BFylX23RHfvdzkAWWqeb9GN34kLIW5EgJi5lUP8BJaPP0KXk9oj3WafV5W1j30_q20BRpDtZpD-qi8AHPuA-Z-oc9ogEQnrQlQk=",
                "deep_link": "https://www.kiwi.com/deep?affilid=apoorvflightsearch&currency=EUR&flightsId=071113884bc900004ee9d2ac_0&from=DEL&lang=en&passengers=1&to=IDR&booking_token=EuOkDW8CY_VHh7nzR5I8_OPBMudGBODLEUIUsJelyWGF2oRpFr3CflwLtf5lORAMOr-1bJHNByot4J75vOQHTBMpPhMZIPiZT7-CD5QgSCvtpWBd4je0S1kRRjhJV0XgFzKVy4TRzzku1281HjJJASyJV85_D3WpOJ2I2hEN3ZlbbyqyhJkJMYyJF57vnoGPtWC2htqz-mKGdOckJVXTxD2WkWlJ67b4Iv0zEHNMvIQCOYZ76lLomNGOFay8-g6XX1iIAAywYs5DsrcgpbYzIvUtBr2eFXF2i1RAC1phl4brMEqPNlVu-A50UxT4uP7aWdeJUgpFdwaeTo4hLLAGP5rqC61p8aIzcC5S_L1Sp8RaDh9HZ-sA6Qq_fHSVOCdr3voc6c-NQrla5mDQNO6CKzzgknsTDe3VFDDNAUUf2H2Q=",
                "facilitated_booking_available": True,
                "pnr_count": 1,
                "has_airport_change": False,
                "technical_stops": 0,
                "throw_away_ticketing": False,
                "hidden_city_ticketing": False,
                "virtual_interlining": False,
                "local_arrival": "2023-02-13T06:40:00.000Z",
                "utc_arrival": "2023-02-13T01:10:00.000Z",
                "local_departure": "2023-02-13T05:15:00.000Z",
                "utc_departure": "2023-02-12T23:45:00.000Z"
            },
            {
                "id": "071113884bc60000d17e7a52_0",
                "flyFrom": "DEL",
                "flyTo": "IDR",
                "cityFrom": "New Delhi",
                "cityCodeFrom": "DEL",
                "cityTo": "Indore",
                "cityCodeTo": "IDR",
                "countryFrom": {
                    "code": "IN",
                    "name": "India"
                },
                "countryTo": {
                    "code": "IN",
                    "name": "India"
                },
                "nightsInDest": "None",
                "quality": 82.333275,
                "distance": 663.59,
                "duration": {
                    "departure": 5100,
                    "return": 0,
                    "total": 5100
                },
                "price": 59,
                "conversion": {
                    "EUR": 59
                },
                "bags_price": {
                    "1": 0
                },
                "baglimit": {
                    "hand_height": 38,
                    "hand_length": 57,
                    "hand_weight": 7,
                    "hand_width": 20,
                    "hold_dimensions_sum": 158,
                    "hold_height": 52,
                    "hold_length": 78,
                    "hold_weight": 15,
                    "hold_width": 28
                },
                "availability": {
                    "seats": 4
                },
                "airlines": [
                    "6E"
                ],
                "route": [
                    {
                        "id": "071113884bc60000d17e7a52_0",
                        "combination_id": "071113884bc60000d17e7a52",
                        "flyFrom": "DEL",
                        "flyTo": "IDR",
                        "cityFrom": "New Delhi",
                        "cityCodeFrom": "DEL",
                        "cityTo": "Indore",
                        "cityCodeTo": "IDR",
                        "airline": "6E",
                        "flight_no": 6231,
                        "operating_carrier": "6E",
                        "operating_flight_no": "6231",
                        "fare_basis": "L0IP",
                        "fare_category": "M",
                        "fare_classes": "X",
                        "fare_family": "",
                        "return": 0,
                        "bags_recheck_required": False,
                        "vi_connection": False,
                        "guarantee": False,
                        "equipment": "None",
                        "vehicle_type": "aircraft",
                        "local_arrival": "2023-02-10T06:40:00.000Z",
                        "utc_arrival": "2023-02-10T01:10:00.000Z",
                        "local_departure": "2023-02-10T05:15:00.000Z",
                        "utc_departure": "2023-02-09T23:45:00.000Z"
                    }
                ],
                "booking_token": "El8RpUJKxXtf44h4atrZiMz3_IzBQDzz2UCa7BhbFOj82ElUButkR47-a0HjdaimKyKyUt9U28HStDiiZmjntPYPVCNEx-0misGvoMygKZcF3vKUkv9nXn3_WNfPbQMbT0Cbd7avctom5FxbGBPHMJJ-kKiZ41YN_9Qo11sVaymgv8LN05ZoIEC8j6_W1pNY2QKSXwOTT5IVc2MviCEMOVh8ToDtQUYNiR2XOX7ue3KmYeK7dNosZk1mt0PHqFjP_t8LauzWbPg0qevD1cDswm-1m7rB5yjPVDz7F_98SH2qLg4XCZU9U2eRyxhnrxH_7rPHbI9X1QtwVO7EkBWsS_J2Y29fD_FQ6uZTTvwAd5Vg7o4jn6k4-3KMOb-rGe7fGZ6iXspZng3WUuLkZKY73vTWQSLUH7q2MmvemMtZxYM9Offcmu0tfpGN9vkhgOXvIQaPnuw-wOhTGXmglxmWofiiQkG-avYQXmI8a9y6P7Ca35jG9QRymjlAwKiuCWhcpYvnE5bCh3JzSIfTXlR_nRWI7UThpeCxsmM1vsDndgpay_aMDUXGzBsn1wi4c7qec",
                "deep_link": "https://www.kiwi.com/deep?affilid=apoorvflightsearch&currency=EUR&flightsId=071113884bc60000d17e7a52_0&from=DEL&lang=en&passengers=1&to=IDR&booking_token=E8zP2FWWOJf1Dv20vhQcGoOybkTnNrAuunJu1B4dCo10WsYvDTDkkYIBXwGFvo5raiiXhyueIBmXlCbx7HhbJtHGRtrk5tO6YqDs1xFV6TN0DSezD49hXl8X0hwITkzql4LEQBi47yEak9Ig2c89qeIgf9GkX1f86IOu5RYaTYNw3q0YaXbc04jYY6B_3xTSvnCi_mnTzaApym1mHXbjVGlqdXAaUggf6g0Gdk4fjW6Q56811c0LX9YOh6TbYBej4FtZuip0z69gtCLmANcrSPn1jlE1g30Bfewlk7Z2ZF1hyMTeSKZ2RllOZSbKXUgDlYGxFL4srMtClq6Rr-q8uBTS-dIvhPeUnG4Ps607N_gWIYUrP0RWOmmpXgFoPgTWs9kprWOVSaeMW-_ucy2ekC7XsmYiRtQHyYZjbmSgfxaM=",
                "facilitated_booking_available": True,
                "pnr_count": 1,
                "has_airport_change": False,
                "technical_stops": 0,
                "throw_away_ticketing": False,
                "hidden_city_ticketing": False,
                "virtual_interlining": False,
                "local_arrival": "2023-02-10T06:40:00.000Z",
                "utc_arrival": "2023-02-10T01:10:00.000Z",
                "local_departure": "2023-02-10T05:15:00.000Z",
                "utc_departure": "2023-02-09T23:45:00.000Z"
            },
            {
                "id": "07111b744bc600008071c23e_0",
                "flyFrom": "DEL",
                "flyTo": "BHO",
                "cityFrom": "New Delhi",
                "cityCodeFrom": "DEL",
                "cityTo": "Bhopal",
                "cityCodeTo": "BHO",
                "countryFrom": {
                    "code": "IN",
                    "name": "India"
                },
                "countryTo": {
                    "code": "IN",
                    "name": "India"
                },
                "nightsInDest": "None",
                "quality": 82.99994,
                "distance": 588.1,
                "duration": {
                    "departure": 5400,
                    "return": 0,
                    "total": 5400
                },
                "price": 59,
                "conversion": {
                    "EUR": 59
                },
                "bags_price": {
                    "1": 0
                },
                "baglimit": {
                    "hand_height": 38,
                    "hand_length": 57,
                    "hand_weight": 7,
                    "hand_width": 20,
                    "hold_dimensions_sum": 158,
                    "hold_height": 52,
                    "hold_length": 78,
                    "hold_weight": 15,
                    "hold_width": 28
                },
                "availability": {
                    "seats": 4
                },
                "airlines": [
                    "6E"
                ],
                "route": [
                    {
                        "id": "07111b744bc600008071c23e_0",
                        "combination_id": "07111b744bc600008071c23e",
                        "flyFrom": "DEL",
                        "flyTo": "BHO",
                        "cityFrom": "New Delhi",
                        "cityCodeFrom": "DEL",
                        "cityTo": "Bhopal",
                        "cityCodeTo": "BHO",
                        "airline": "6E",
                        "flight_no": 6022,
                        "operating_carrier": "6E",
                        "operating_flight_no": "6022",
                        "fare_basis": "Q0IP",
                        "fare_category": "M",
                        "fare_classes": "Q",
                        "fare_family": "",
                        "return": 0,
                        "bags_recheck_required": False,
                        "vi_connection": False,
                        "guarantee": False,
                        "equipment": "None",
                        "vehicle_type": "aircraft",
                        "local_arrival": "2023-02-10T08:20:00.000Z",
                        "utc_arrival": "2023-02-10T02:50:00.000Z",
                        "local_departure": "2023-02-10T06:50:00.000Z",
                        "utc_departure": "2023-02-10T01:20:00.000Z"
                    }
                ],
                "booking_token": "Ee3wq1XwZ7BFA2GLaLinKWvtEiVmhwQkvZw2wNmeNyjGseostXnhBHOD4tzBMZ8Xaivb1m67OtsqbvEzELA8KDxhhptsdfId_JmZLrUXTgiJIaNvgZbnlQP1OjP5wwdUIhgouH6JMvF8BcqF294vJRmvG3yZdq7QcEuLnsttcnVhTTpsUPLSvY4KkPi1KAd37-OX_3cJXgzyZA7h-IHyx7YsefzjMO8Utkx3gEfCIi4dcndcYpV2R_P7HQm4FvRlY2kNpyIWAuBxnG4k7eWxeMFJAPYXtdMr3VXfB9RvB_fN6pKU2hsyllwRuixJSutphBnm-O-dg9lewz511wuhWy_NKMmPef7PCANOi6B8Llt6RoDcyCsz_u9rGExFkn3ZNoaP2444z__ZX0Oif418Q5H_2CiT_TnZCNOGr8B9BTgluWr2bIV_QOq2T1IqbMNP-Hj2lcZOhlNLIqiPoo0A_2YQBSytj8-XJzqUWAJN9xjriHJL_I5yHSAkeSHbi38H6Fw3fY27LM7EvzTDN7Eso8t3enB19elmTxBnC_Ov3BvlCvJRpd8yqgn8YMtw49crYYOqVyLGARGy1CVhmgar9iCohf7dnmDZkdS46qmQVa7U=",
                "deep_link": "https://www.kiwi.com/deep?affilid=apoorvflightsearch&currency=EUR&flightsId=07111b744bc600008071c23e_0&from=DEL&lang=en&passengers=1&to=BHO&booking_token=ENjtQ1yVaNDEIktfrAo2YkD4AwY991iShjGSx_5mr4-yRzbRkcRS17zftdvYqoT-Cwrz661ls-QcomGDCnhuuE-mrpgGbk0q3uua-N5WKNPnk9QUoDA-dE1pfvFlIr-RN9oGtyC6MVJwGyUSb-qNsh5SlUebT9C8e1MXZ1FwxxYPDXiKyINU4u7Lx60O_JTe2KlPsuIMM1jcI7qSzxb8JqP2DT_nBBysIvgugEX7NnRIRDqTjWtzlT_-A3xy63Aga3125APf-7SLCOyUgHVh4lY4xrptGA5JVa63ADCYZFBq1dYFzKSNjhIYWTnLZ5Gipj5sCm4s0fort2Hq5awiHPOIZ5vJBncYH8uWY1zODpNTbc9su5MA-wLIV8Qj8gAdV65LAsQO3y6AKrh0gH9_b7HlDVADWS_fBHG0KORrQ9NxKoxuPypbWPYzHi-ocqeMAR2eX8Z-enf0-5zGUEG-5sg==",
                "facilitated_booking_available": True,
                "pnr_count": 1,
                "has_airport_change": False,
                "technical_stops": 0,
                "throw_away_ticketing": False,
                "hidden_city_ticketing": False,
                "virtual_interlining": False,
                "local_arrival": "2023-02-10T08:20:00.000Z",
                "utc_arrival": "2023-02-10T02:50:00.000Z",
                "local_departure": "2023-02-10T06:50:00.000Z",
                "utc_departure": "2023-02-10T01:20:00.000Z"
            },
            {
                "id": "071107194bc80000c30e25a2_0",
                "flyFrom": "DEL",
                "flyTo": "DED",
                "cityFrom": "New Delhi",
                "cityCodeFrom": "DEL",
                "cityTo": "Dehradun",
                "cityCodeTo": "DED",
                "countryFrom": {
                    "code": "IN",
                    "name": "India"
                },
                "countryTo": {
                    "code": "IN",
                    "name": "India"
                },
                "nightsInDest": "None",
                "quality": 78.66662,
                "distance": 208.74,
                "duration": {
                    "departure": 3000,
                    "return": 0,
                    "total": 3000
                },
                "price": 60,
                "conversion": {
                    "EUR": 60
                },
                "bags_price": {
                    "1": 0
                },
                "baglimit": {
                    "hand_height": 38,
                    "hand_length": 57,
                    "hand_weight": 7,
                    "hand_width": 20,
                    "hold_dimensions_sum": 158,
                    "hold_height": 52,
                    "hold_length": 78,
                    "hold_weight": 15,
                    "hold_width": 28
                },
                "availability": {
                    "seats": 2
                },
                "airlines": [
                    "6E"
                ],
                "route": [
                    {
                        "id": "071107194bc80000c30e25a2_0",
                        "combination_id": "071107194bc80000c30e25a2",
                        "flyFrom": "DEL",
                        "flyTo": "DED",
                        "cityFrom": "New Delhi",
                        "cityCodeFrom": "DEL",
                        "cityTo": "Dehradun",
                        "cityCodeTo": "DED",
                        "airline": "6E",
                        "flight_no": 2582,
                        "operating_carrier": "6E",
                        "operating_flight_no": "2582",
                        "fare_basis": "L0IP",
                        "fare_category": "M",
                        "fare_classes": "X",
                        "fare_family": "",
                        "return": 0,
                        "bags_recheck_required": False,
                        "vi_connection": False,
                        "guarantee": False,
                        "equipment": "None",
                        "vehicle_type": "aircraft",
                        "local_arrival": "2023-02-12T19:05:00.000Z",
                        "utc_arrival": "2023-02-12T13:35:00.000Z",
                        "local_departure": "2023-02-12T18:15:00.000Z",
                        "utc_departure": "2023-02-12T12:45:00.000Z"
                    }
                ],
                "booking_token": "EbgnuBdv58xf-uTvOA-lcs6eM5m8P4daQfTjc8wppHqBXNJhsg14-hkd76E52JOY0pOFtnfCqp9eLDe2rhGU4ci4C70LfpIcb53WUlMYq4KccjjunW97_SXEYTg08Uoml0qyqEuwTFdLVUUWEI_u62cxIQMXnVx3dWQnE3gaT5c3wgAARCsRZC8YAq1xgz7G2pRMr0zGWdlajo4mY3ZUab_8J9lkY8QjREBx6VcfeWTOY4kj0b5p839q_PKQziHHSHZcHZiQuWZ6FZxWi6OmJLvTfBlIblXZLQc71T5ZUTy8n20LlEgAKcfhlhN0C5U-zzfMwL5rSjJbV3ydaoSjYiBD2WSgvDrdRLZ_-5XxeSRNZN1rcXr-SMIrphHamJoyhydPzFlwtX_B86tbffhjmsPXtb0BOs2oBdiCHe3jwMu6NaF7gZla0WQ4YZl__E7eFXB5Xws6PIzIMqKSlZ5kiYNO_6muar0ypcfW13EAhJuMHi2TqOjZaryZNSQuL3gTP9odNVhs7lVf9rMIFtLyJ75bNkcdXi64knf98A8LQk0hWeojAgLSWwMscE7s-C4LL",
                "deep_link": "https://www.kiwi.com/deep?affilid=apoorvflightsearch&currency=EUR&flightsId=071107194bc80000c30e25a2_0&from=DEL&lang=en&passengers=1&to=DED&booking_token=EZN9EwMPn5Odr3zZPc2t84y1mukZKjcmILyaVOvRcX3fZT3G5g_HOZkziuy_VEjQZMXL_0kTn-HJAxtAKp3Gae7XOw5TFVRdP8RxYQqrpO_0rorPhVXGfr3Qhw3GHK1BXo-t7hJGkxh_A-DmprNGFXv9PeJKbZNK4qepF29h9t9kjhzUc89OxXE3jp1tSuD2Zih9gFRlg5qKPoJ1ubwz6p7G7Onx_xdLHzk9_UwUHUC5W40wZclfyPoMpeElQqFy1BC7PXwP7eWQn1ENFTgkQrlyLhPzjK8ehY6FpPoVfp_-tWl9awsyw3IXk3XsBHGK2BCdIILMFwCSpd4xLtDHBrtLy-pod4CuXjw7yGUY7qSWFuXXm-oJMFf9r8b1-_3Nuj6_uJZmA7hOXXT60rwhOeQqiVRCEhRj9Gu9GbuW0kR3dTox3VJXldLJDxrc2vm-S",
                "facilitated_booking_available": True,
                "pnr_count": 1,
                "has_airport_change": False,
                "technical_stops": 0,
                "throw_away_ticketing": False,
                "hidden_city_ticketing": False,
                "virtual_interlining": False,
                "local_arrival": "2023-02-12T19:05:00.000Z",
                "utc_arrival": "2023-02-12T13:35:00.000Z",
                "local_departure": "2023-02-12T18:15:00.000Z",
                "utc_departure": "2023-02-12T12:45:00.000Z"
            },
            {
                "id": "071107194bc70000743e72df_0",
                "flyFrom": "DEL",
                "flyTo": "DED",
                "cityFrom": "New Delhi",
                "cityCodeFrom": "DEL",
                "cityTo": "Dehradun",
                "cityCodeTo": "DED",
                "countryFrom": {
                    "code": "IN",
                    "name": "India"
                },
                "countryTo": {
                    "code": "IN",
                    "name": "India"
                },
                "nightsInDest": "None",
                "quality": 79.333285,
                "distance": 208.74,
                "duration": {
                    "departure": 3300,
                    "return": 0,
                    "total": 3300
                },
                "price": 60,
                "conversion": {
                    "EUR": 60
                },
                "bags_price": {
                    "1": 0
                },
                "baglimit": {
                    "hand_height": 38,
                    "hand_length": 57,
                    "hand_weight": 7,
                    "hand_width": 20,
                    "hold_dimensions_sum": 158,
                    "hold_height": 52,
                    "hold_length": 78,
                    "hold_weight": 15,
                    "hold_width": 28
                },
                "availability": {
                    "seats": 2
                },
                "airlines": [
                    "6E"
                ],
                "route": [
                    {
                        "id": "071107194bc70000743e72df_0",
                        "combination_id": "071107194bc70000743e72df",
                        "flyFrom": "DEL",
                        "flyTo": "DED",
                        "cityFrom": "New Delhi",
                        "cityCodeFrom": "DEL",
                        "cityTo": "Dehradun",
                        "cityCodeTo": "DED",
                        "airline": "6E",
                        "flight_no": 5026,
                        "operating_carrier": "6E",
                        "operating_flight_no": "5026",
                        "fare_basis": "L0IP",
                        "fare_category": "M",
                        "fare_classes": "X",
                        "fare_family": "",
                        "return": 0,
                        "bags_recheck_required": False,
                        "vi_connection": False,
                        "guarantee": False,
                        "equipment": "None",
                        "vehicle_type": "aircraft",
                        "local_arrival": "2023-02-11T09:15:00.000Z",
                        "utc_arrival": "2023-02-11T03:45:00.000Z",
                        "local_departure": "2023-02-11T08:20:00.000Z",
                        "utc_departure": "2023-02-11T02:50:00.000Z"
                    }
                ],
                "booking_token": "E30068Dx6BUi-xaQ_ZS4gTeEo44c7gaYYttETB1voDuPBfImLN9StURE5Swy57I4GKIjBSwDQzYqVgicHxjenmbcrdNMxtG1O9aM4pq_GUEntOshD97dzK2CTgrQ1ZeMX1K--AQzz34cZJxvgYohc3wsLUUhnvk2qfgQxo9LakfFSnwnJmMxwGoFbnMSRnpddV01_Dx2tF7QGA8ABcp1uq1uu5psaQ-zqi3G2xKRLtH6fEPqbGdOkZMvEX6HlzDn8dr6eXvgXKwUkh6DCQ1ziTsIkViJEXP9HqAmFpaIdr8UewzzSKg0vAB66doiqmI4JVdW0fHrSrxyeJIirpw903WXDxvtruwBq_bCItlJfC610TbxEDk1FV9UFBDeBPzxodihm9AKcDeNfAjDX9BMVUmxFutQP9ZYwbjLco5eX82q6KRxMyYOqN_T9KJQA6gYX32ctA-ryc2aX6Iozni7Lxse-U0XUtYSBS_HVRjo_-xUF9KXAiPURSaMTwWLrtF6r8_7s7Kve15Lw_z_lrZ3dJKVxF69FNiWJxT77_gq5jLiATzxBvnVdH3GdeqqNcMpI",
                "deep_link": "https://www.kiwi.com/deep?affilid=apoorvflightsearch&currency=EUR&flightsId=071107194bc70000743e72df_0&from=DEL&lang=en&passengers=1&to=DED&booking_token=ExRdk21znQobhIQ3SDg_Bhv6QBf8DFaL_uQ3o8qgfUrv8keIVaoD8D8bGka7nWr77fTvuR0PZT4rTtOS0o_iLTaMYARNI8sNsetPyAnTf4MJOmZJqKXYEEpcmIxlXSkow5x2VuvzcauwXxfrHUGUnWiyrXn2nOGclqi22XSOj0WM1AWbjgZUgrbAXdD06GDOtzxlVlnU_dqNHoEsa3ItH4V70D6NJvaAT9qzcf2AX7kiWKcb0dtX1cvjCbMCANsZBPZXOpg2r0J2ZBBxIcsLQk5RQEhwZJDb2dSDUr3cIEuLKz1j_cuHGrRr3mx7mpIfayonltDla-unHF5Qt-leFc_p1U2dyZIeX0tDWjRxSzoBt-GVNL-fCFEPEr9FyajRC7fGE1vcQ_JCOrvqKAXJ6zzJmCAmtQqSWhyd7d63Itx_7v-avsafGcX5I7NTWzYhM",
                "facilitated_booking_available": True,
                "pnr_count": 1,
                "has_airport_change": False,
                "technical_stops": 0,
                "throw_away_ticketing": False,
                "hidden_city_ticketing": False,
                "virtual_interlining": False,
                "local_arrival": "2023-02-11T09:15:00.000Z",
                "utc_arrival": "2023-02-11T03:45:00.000Z",
                "local_departure": "2023-02-11T08:20:00.000Z",
                "utc_departure": "2023-02-11T02:50:00.000Z"
            },
            {
                "id": "071104c24bc6000085d403cd_0",
                "flyFrom": "DEL",
                "flyTo": "LKO",
                "cityFrom": "New Delhi",
                "cityCodeFrom": "DEL",
                "cityTo": "Lucknow",
                "cityCodeTo": "LKO",
                "countryFrom": {
                    "code": "IN",
                    "name": "India"
                },
                "countryTo": {
                    "code": "IN",
                    "name": "India"
                },
                "nightsInDest": "None",
                "quality": 81.33328,
                "distance": 423.95,
                "duration": {
                    "departure": 4200,
                    "return": 0,
                    "total": 4200
                },
                "price": 60,
                "conversion": {
                    "EUR": 60
                },
                "bags_price": {
                    "1": 0
                },
                "baglimit": {
                    "hand_height": 36,
                    "hand_length": 56,
                    "hand_weight": 7,
                    "hand_width": 23,
                    "hold_dimensions_sum": 158,
                    "hold_height": 50,
                    "hold_length": 70,
                    "hold_weight": 15,
                    "hold_width": 38
                },
                "availability": {
                    "seats": 1
                },
                "airlines": [
                    "I5"
                ],
                "route": [
                    {
                        "id": "071104c24bc6000085d403cd_0",
                        "combination_id": "071104c24bc6000085d403cd",
                        "flyFrom": "DEL",
                        "flyTo": "LKO",
                        "cityFrom": "New Delhi",
                        "cityCodeFrom": "DEL",
                        "cityTo": "Lucknow",
                        "cityCodeTo": "LKO",
                        "airline": "I5",
                        "flight_no": 745,
                        "operating_carrier": "I5",
                        "operating_flight_no": "745",
                        "fare_basis": "LNRA000",
                        "fare_category": "M",
                        "fare_classes": "L",
                        "fare_family": "",
                        "return": 0,
                        "bags_recheck_required": False,
                        "vi_connection": False,
                        "guarantee": False,
                        "equipment": "None",
                        "vehicle_type": "aircraft",
                        "local_arrival": "2023-02-10T14:25:00.000Z",
                        "utc_arrival": "2023-02-10T08:55:00.000Z",
                        "local_departure": "2023-02-10T13:15:00.000Z",
                        "utc_departure": "2023-02-10T07:45:00.000Z"
                    }
                ],
                "booking_token": "E3_vkVrlaGYXMBGzcdHe12RYs3jXpmRJHHsGUcBy0P90ezkNYMKZjlvwlxzuAIM-GuH5GNAHjKD7EnUfqFpdC6FLuh91OLR0BXd-N8TnBdbYHLF0FCSm0CysrDLVLs7VRxOCMV76vyzBZEXCVFEZOvA-Bd3BnJkmn3dv3eiFIQOWpm-7SZCzIIwWZPWpsqTJWdU2Jv4ZxU-RtvWbjtcBhHLb7a6T5tP25zi24lBhVd7GTzUlh36HHJ4tj6J6Hc7PkBACXBjPM0_sqBU0NySFemRjkxJb3oniQOlzjYvkUp5mCrBuz1JF0DtSctgQlqsCrgocJtKz6evMZYuc9LqgKnJ4jDX2ikJkRXrd9w975e6ALqskIOvth_GufewwrtBRrR6W6vK0ssPtNuGJ7O8AeqDpv6JuUhtrc48JpaXQ0bvCW3kQ3wHL1KBSJAMghVQrmGUSrqniNioL3fDdRvDXmOthxIcGVn8ovDI1p0iVOHrIr4alP126bymIVw2sWuwictxtUOlF9y7zN_93DUhnYm-ZRJHPYYrdSxt8sssxE23IFgamrFLa_vL0xKt4HNSIWGoA9Mpbl3dmcDSlJiufWdFjpm4Zw1DUk-mBY9b8MnA8=",
                "deep_link": "https://www.kiwi.com/deep?affilid=apoorvflightsearch&currency=EUR&flightsId=071104c24bc6000085d403cd_0&from=DEL&lang=en&passengers=1&to=LKO&booking_token=E9-VnhF2cmJGhxkycL20nBEoUJ5jl3RvkEYn3Aq6yGT8yl4nzU8z1iaecJ4XR-McJhUgSajCYF_jTwH77xfK01fbzTN7-_v8BuAz2at9gnBu-h2Tob6ajZb4Hp9dkncG1hn82QNZ3JABKPIFok626HV1Dewh33PFjLuO365s9GqEllcVOwKIjtXJvQ1HE1F-OLP8UamCu_0K_N3LFvqTD4QveTmz4w8ieHSMLuSxsjskrUWeA2aNtFkyR8JHwhiZL-U3RPr7RCvylB-ELF8dxYFFf3NokeNUmf9J-hA-GhmU9wiqP6FaLTd_UfBwhcdA-zfXIRT4gDuXJi8UXwUZClH3GU4NKrjHopa8RsdRfszF8X6RBDyGSW1vCGQKBF_xFtJiY6PaYvekDc4Rn05hPrN8AAPmkLzmm7vqgLpAiVWDbwsVubgcfFooLGwuSJKGC5L9kAci3R-_rpA2pZjXXtqxMam2oYQVSoTYw4Y-6EHI=",
                "facilitated_booking_available": True,
                "pnr_count": 1,
                "has_airport_change": False,
                "technical_stops": 0,
                "throw_away_ticketing": False,
                "hidden_city_ticketing": False,
                "virtual_interlining": False,
                "local_arrival": "2023-02-10T14:25:00.000Z",
                "utc_arrival": "2023-02-10T08:55:00.000Z",
                "local_departure": "2023-02-10T13:15:00.000Z",
                "utc_departure": "2023-02-10T07:45:00.000Z"
            },
            {
                "id": "071104834bc9000056122ddd_0",
                "flyFrom": "DEL",
                "flyTo": "NAG",
                "cityFrom": "New Delhi",
                "cityCodeFrom": "DEL",
                "cityTo": "Nagpur",
                "cityCodeTo": "NAG",
                "countryFrom": {
                    "code": "IN",
                    "name": "India"
                },
                "countryTo": {
                    "code": "IN",
                    "name": "India"
                },
                "nightsInDest": "None",
                "quality": 85.33327,
                "distance": 854.82,
                "duration": {
                    "departure": 6000,
                    "return": 0,
                    "total": 6000
                },
                "price": 60,
                "conversion": {
                    "EUR": 60
                },
                "bags_price": {
                    "1": 0
                },
                "baglimit": {
                    "hand_height": 38,
                    "hand_length": 57,
                    "hand_weight": 7,
                    "hand_width": 20,
                    "hold_dimensions_sum": 158,
                    "hold_height": 52,
                    "hold_length": 78,
                    "hold_weight": 15,
                    "hold_width": 28
                },
                "availability": {
                    "seats": 2
                },
                "airlines": [
                    "6E"
                ],
                "route": [
                    {
                        "id": "071104834bc9000056122ddd_0",
                        "combination_id": "071104834bc9000056122ddd",
                        "flyFrom": "DEL",
                        "flyTo": "NAG",
                        "cityFrom": "New Delhi",
                        "cityCodeFrom": "DEL",
                        "cityTo": "Nagpur",
                        "cityCodeTo": "NAG",
                        "airline": "6E",
                        "flight_no": 6601,
                        "operating_carrier": "6E",
                        "operating_flight_no": "6601",
                        "fare_basis": "",
                        "fare_category": "M",
                        "fare_classes": "L",
                        "fare_family": "",
                        "return": 0,
                        "bags_recheck_required": False,
                        "vi_connection": False,
                        "guarantee": False,
                        "equipment": "None",
                        "vehicle_type": "aircraft",
                        "local_arrival": "2023-02-13T21:50:00.000Z",
                        "utc_arrival": "2023-02-13T16:20:00.000Z",
                        "local_departure": "2023-02-13T20:10:00.000Z",
                        "utc_departure": "2023-02-13T14:40:00.000Z"
                    }
                ],
                "booking_token": "EoDsRwR-UWSpP6v4e_8vgpcwpKyxaD6yrW-PIHfvxwYas141SMB5GxAGGlUFdV0baTVckTksvzsmP8qftOYwb1wg_NTVAjr06UhIm5HxcWeKjgJ6cqT1cynyg3erDjKQ1e_5UFj5RqGaXTBfrfBiGJ25o8obd3bMmBqMQMLEsaMEDgqtRSCWW6uLsSNsJBn059cSa_3SLOJwVGlIrdk5JHxlqYpyyMuJ2G1DPI1_NxRdDLeCvusul8513mDA65zv_eu46FqbLaZoQmmxTeqPEsw4m9XOH0NrIlbv9_0614zSVv5wkjLx-hCziMcS4dqQ_E79A4hUgnxt_IO4BJGuhCHVC9-6GrUJfbmIpbBHjhwofwGHqWDCy_cyajK2UIKILjeOwWSwBIb942pUQz0Ycuwm4cZRaogpG06na5eDtJIVVBMDzwzzU5fpIH0RSb4KiXrXhaq4nvhGVrJE8Nt98YBeVU2y-1S_zdTrozXDqznTdCqS06qVnGbaDfoHejnQjWQNh508RlfjLuyCaUzLkiHVe9Ar3uGaJBK5dHev7Lmw=",
                "deep_link": "https://www.kiwi.com/deep?affilid=apoorvflightsearch&currency=EUR&flightsId=071104834bc9000056122ddd_0&from=DEL&lang=en&passengers=1&to=NAG&booking_token=EpyanOIXhBB0wjfoaTEYRetN398S7n-UyE4x3NJDS2CYlYox6UvBMqLFMF4wtjHETgiKH7cE-9NR07quUNwYxlMOIi8FCEOUnTE04q6QBpIKVVBedDW9AqPaDvvpx6EUBMFi-X-qwwXIbpG5tM-CqzCKGDc_VL4KV06WbDtC6rzPmcJqVwIC0V4iUigomSMB-umsoE88dh3COuJQvsgyVyZlQ8WIMJB2F9inL_OHFwO5n6LdlNSqI3faHeW_N_sHZOZYE061qBwb8aRROcgSoUVi-imu29k3f8b4Yxwf6zEQvTnAjG2zSDiSJhxqHdvC4NmGDOJqJpOUo5oFS5l7WIkeWOFQOaGzsgUw5uRq4714AxLKJNWzHf7UltwmAWfdgWujj_ff_Jbg22vNvwacg8tYbnCGODVRFR2WCmYYOy_M=",
                "facilitated_booking_available": True,
                "pnr_count": 1,
                "has_airport_change": False,
                "technical_stops": 0,
                "throw_away_ticketing": False,
                "hidden_city_ticketing": False,
                "virtual_interlining": False,
                "local_arrival": "2023-02-13T21:50:00.000Z",
                "utc_arrival": "2023-02-13T16:20:00.000Z",
                "local_departure": "2023-02-13T20:10:00.000Z",
                "utc_departure": "2023-02-13T14:40:00.000Z"
            },
            {
                "id": "071117634bc800008624ef07_0",
                "flyFrom": "DEL",
                "flyTo": "DHM",
                "cityFrom": "New Delhi",
                "cityCodeFrom": "DEL",
                "cityTo": "Dharamshala",
                "cityCodeTo": "DHM",
                "countryFrom": {
                    "code": "IN",
                    "name": "India"
                },
                "countryTo": {
                    "code": "IN",
                    "name": "India"
                },
                "nightsInDest": "None",
                "quality": 85.999935,
                "distance": 408.7,
                "duration": {
                    "departure": 6300,
                    "return": 0,
                    "total": 6300
                },
                "price": 60,
                "conversion": {
                    "EUR": 60
                },
                "bags_price": {
                    "1": 0
                },
                "baglimit": {
                    "hand_height": 36,
                    "hand_length": 54,
                    "hand_weight": 7,
                    "hand_width": 18,
                    "hold_dimensions_sum": 158,
                    "hold_height": 52,
                    "hold_length": 78,
                    "hold_weight": 15,
                    "hold_width": 28
                },
                "availability": {
                    "seats": 2
                },
                "airlines": [
                    "SG"
                ],
                "route": [
                    {
                        "id": "071117634bc800008624ef07_0",
                        "combination_id": "071117634bc800008624ef07",
                        "flyFrom": "DEL",
                        "flyTo": "DHM",
                        "cityFrom": "New Delhi",
                        "cityCodeFrom": "DEL",
                        "cityTo": "Dharamshala",
                        "cityCodeTo": "DHM",
                        "airline": "SG",
                        "flight_no": 2345,
                        "operating_carrier": "SG",
                        "operating_flight_no": "2345",
                        "fare_basis": "USAV",
                        "fare_category": "M",
                        "fare_classes": "U",
                        "fare_family": "",
                        "return": 0,
                        "bags_recheck_required": False,
                        "vi_connection": False,
                        "guarantee": False,
                        "equipment": "None",
                        "vehicle_type": "aircraft",
                        "local_arrival": "2023-02-12T08:40:00.000Z",
                        "utc_arrival": "2023-02-12T03:10:00.000Z",
                        "local_departure": "2023-02-12T06:55:00.000Z",
                        "utc_departure": "2023-02-12T01:25:00.000Z"
                    }
                ],
                "booking_token": "ESAcHmvUG5g0J_vZMGEXNZGexa9-VvBbiFKe6mOXgsscqZfTjUjt7vQbrGm3yFd6eACUSNVj4QF6awBnmD3scD5jJm7ByGqZYs1KsfwTLpLFEx6AVvgRrbkc68_9J1hEzo1tBumaoPJK4engqd1e20wEtRy1EjuU2Wdx4tdarVjtB3EJ04NSFBRDnHGSQKb_9TVMT5-dB0hjexpy4usa6ANNeXJ_mwBtb8FB8x9hmLxhDY2JyKyljsqzY20kUobx4-ZEzLag9lHMlA7ao1HB9Ft9aFq2VZiEITpEmntLEAxNkbbMIJb0whIIE63rEab_flw_Hnzh9MwlE-vlHv4FTGc-S7NBiwoE1XBNuy9Utma-EaA9uiiiwa98IV6NPRmVrCK0oBlrQbcsCDjkcvGf6tQQV3hvMGpy0GLxxDx3rZdIYHjPx6kwpC0n3X8Km3f4SZod55n6AbFfMa0SwH2G4d5-f5DksZS79fA69YwUC7s7YIqP71M8ea-BlZ05XlrwKX3LOKSBk7Z-rVGhiJmKsekFgKnMWts_dBdXgQyfowj0=",
                "deep_link": "https://www.kiwi.com/deep?affilid=apoorvflightsearch&currency=EUR&flightsId=071117634bc800008624ef07_0&from=DEL&lang=en&passengers=1&to=DHM&booking_token=EO1L0_cc1DJGTwAwxPUnM95MFyHT7QAe8aRiqgfx1S-mU4LFKYf-ZRafvTeiJ-vw2Z9qsNnjXc-JMqETXh8TvHBV_0EF5dogdsOOTrhj0g-Uk_nJLmUGTdglewkRIdSNcr_ZoIR3k4Y2lJDa3BHkxZEFoupwf62jpttHifJnHh2r01ULt9XHamKjKI8GsqEzFHJudemhfEIyly0ksDj3R52CnwxG4K3l6ZZQZ3aGzQAM136okfc6yfv7CBfx42gmGShJi6nPdsNIePqUat_s44AvugZ_3h4Ujzqltwi-J-dOXiisefYJw-KvFdkEd0vA-YPZbv3C1uhjckKzs0VWkKLpkPcFwU3hELXZXjbcGdJxulLglrZZS46X5ROaVIvebVH08e_tYR7JTB2YHdGalUh9Rt9U0gLgTv7z5I_fVaQU=",
                "facilitated_booking_available": True,
                "pnr_count": 1,
                "has_airport_change": False,
                "technical_stops": 0,
                "throw_away_ticketing": False,
                "hidden_city_ticketing": False,
                "virtual_interlining": False,
                "local_arrival": "2023-02-12T08:40:00.000Z",
                "utc_arrival": "2023-02-12T03:10:00.000Z",
                "local_departure": "2023-02-12T06:55:00.000Z",
                "utc_departure": "2023-02-12T01:25:00.000Z"
            },
            {
                "id": "071117634bc70000578a6ebb_0",
                "flyFrom": "DEL",
                "flyTo": "DHM",
                "cityFrom": "New Delhi",
                "cityCodeFrom": "DEL",
                "cityTo": "Dharamshala",
                "cityCodeTo": "DHM",
                "countryFrom": {
                    "code": "IN",
                    "name": "India"
                },
                "countryTo": {
                    "code": "IN",
                    "name": "India"
                },
                "nightsInDest": "None",
                "quality": 85.999935,
                "distance": 408.7,
                "duration": {
                    "departure": 6300,
                    "return": 0,
                    "total": 6300
                },
                "price": 60,
                "conversion": {
                    "EUR": 60
                },
                "bags_price": {
                    "1": 0
                },
                "baglimit": {
                    "hand_height": 36,
                    "hand_length": 54,
                    "hand_weight": 7,
                    "hand_width": 18,
                    "hold_dimensions_sum": 158,
                    "hold_height": 52,
                    "hold_length": 78,
                    "hold_weight": 15,
                    "hold_width": 28
                },
                "availability": {
                    "seats": 2
                },
                "airlines": [
                    "SG"
                ],
                "route": [
                    {
                        "id": "071117634bc70000578a6ebb_0",
                        "combination_id": "071117634bc70000578a6ebb",
                        "flyFrom": "DEL",
                        "flyTo": "DHM",
                        "cityFrom": "New Delhi",
                        "cityCodeFrom": "DEL",
                        "cityTo": "Dharamshala",
                        "cityCodeTo": "DHM",
                        "airline": "SG",
                        "flight_no": 2345,
                        "operating_carrier": "SG",
                        "operating_flight_no": "2345",
                        "fare_basis": "USAV",
                        "fare_category": "M",
                        "fare_classes": "U",
                        "fare_family": "",
                        "return": 0,
                        "bags_recheck_required": False,
                        "vi_connection": False,
                        "guarantee": False,
                        "equipment": "None",
                        "vehicle_type": "aircraft",
                        "local_arrival": "2023-02-11T08:40:00.000Z",
                        "utc_arrival": "2023-02-11T03:10:00.000Z",
                        "local_departure": "2023-02-11T06:55:00.000Z",
                        "utc_departure": "2023-02-11T01:25:00.000Z"
                    }
                ],
                "booking_token": "EIaZFEfyiud--u_j7NpdlM8IR6rpIeIPHrHexf0K5zolVaTWdBf3xR6nrNciceo3_P6Hi9TmA9fnZlyYDua0k2IBNLIzgv3cykbQtsNr_uV_BxbCfAOFzFb7yKPObSuEsH9wZDcgTUG7m-LfgFK7G1fY7gDeWXWmUieTQi8LNIfGJ7N8pGAOfaJn-LEIc53mKOaYkM0BnVgnEZ_k_gaNGpZ8i-rLSq-vnKvVkEQvStRuUfolT3d219_mHO2eyzrRTAEBHlOgADG39vy8SSM6WPpzEpyGPdqszb31p2yVQM19_jxtuMHAr9Dqr6vVKBPCBzll3Wd0E_DIt9Jb8RAesiGVHwvHJK1fAq3aUnHngH3Mch93me_ghk_JyDi5m5fRcY09CW_OJyDgP1xh3anzcvdilvF48iEzhr0mZB-Yi879xiLH4t7Dj9zsH1KlNcK2M0B7YnTN2PJbXUTlcUDUo4wEUF6AdErGcyt5qNNLs9rYNSASbCicbzaTMdR7O_WQURpsdSSsr1Mxkokquu_s6Fk3L6p4clRzFdbywxJHcZ9s=",
                "deep_link": "https://www.kiwi.com/deep?affilid=apoorvflightsearch&currency=EUR&flightsId=071117634bc70000578a6ebb_0&from=DEL&lang=en&passengers=1&to=DHM&booking_token=EYEo_O0spykIsrjRFRviVeM-8ZNc_qYadMyvc6k_4Fjg4ZQ67to3xs4DWMUiL17G2k-EGIP_QwYDP2YLYs3EqoXJoE9Xo0Ae3lfl-Xbf-cwUNl_ns85OVkG-82bKWi9elqDK3l_LG4Z3h-7XK8WAupSI3F_ZqZbC7V-q3xTp5rPqGKXlwT3YTxJGRs-XcPIEzwHiPycwE8rrrkaMyUTkARykR-uJcwIYNhSTlbZk42gr_lz9EG0EyYSPKwj_qbpB-j1RAXLZSOaJgooUL-dbQxh8fwTMtM7nPJz9s-DS_nrD1rM-utbS2uB1dkQAwcyEmTJguQdOHRrX8TBMh-Ttur3KHm0HOvJVuhCnIhlcdghTno8q-e-cnVHOJ6z10QyIdN-SQ6NFKmgDNF_E4UWawlB2FSz4LWd_yP8E7DQi1Ep4=",
                "facilitated_booking_available": True,
                "pnr_count": 1,
                "has_airport_change": False,
                "technical_stops": 0,
                "throw_away_ticketing": False,
                "hidden_city_ticketing": False,
                "virtual_interlining": False,
                "local_arrival": "2023-02-11T08:40:00.000Z",
                "utc_arrival": "2023-02-11T03:10:00.000Z",
                "local_departure": "2023-02-11T06:55:00.000Z",
                "utc_departure": "2023-02-11T01:25:00.000Z"
            },
            {
                "id": "07111b744bc9000011f53b78_0",
                "flyFrom": "DEL",
                "flyTo": "BHO",
                "cityFrom": "New Delhi",
                "cityCodeFrom": "DEL",
                "cityTo": "Bhopal",
                "cityCodeTo": "BHO",
                "countryFrom": {
                    "code": "IN",
                    "name": "India"
                },
                "countryTo": {
                    "code": "IN",
                    "name": "India"
                },
                "nightsInDest": "None",
                "quality": 84.333275,
                "distance": 588.1,
                "duration": {
                    "departure": 5100,
                    "return": 0,
                    "total": 5100
                },
                "price": 61,
                "conversion": {
                    "EUR": 61
                },
                "bags_price": {
                    "1": 0
                },
                "baglimit": {
                    "hand_height": 38,
                    "hand_length": 57,
                    "hand_weight": 7,
                    "hand_width": 20,
                    "hold_dimensions_sum": 158,
                    "hold_height": 52,
                    "hold_length": 78,
                    "hold_weight": 15,
                    "hold_width": 28
                },
                "availability": {
                    "seats": 1
                },
                "airlines": [
                    "6E"
                ],
                "route": [
                    {
                        "id": "07111b744bc9000011f53b78_0",
                        "combination_id": "07111b744bc9000011f53b78",
                        "flyFrom": "DEL",
                        "flyTo": "BHO",
                        "cityFrom": "New Delhi",
                        "cityCodeFrom": "DEL",
                        "cityTo": "Bhopal",
                        "cityCodeTo": "BHO",
                        "airline": "6E",
                        "flight_no": 6822,
                        "operating_carrier": "6E",
                        "operating_flight_no": "6822",
                        "fare_basis": "P0IP",
                        "fare_category": "M",
                        "fare_classes": "X",
                        "fare_family": "",
                        "return": 0,
                        "bags_recheck_required": False,
                        "vi_connection": False,
                        "guarantee": False,
                        "equipment": "None",
                        "vehicle_type": "aircraft",
                        "local_arrival": "2023-02-13T15:55:00.000Z",
                        "utc_arrival": "2023-02-13T10:25:00.000Z",
                        "local_departure": "2023-02-13T14:30:00.000Z",
                        "utc_departure": "2023-02-13T09:00:00.000Z"
                    }
                ],
                "booking_token": "EgqCLmH38ZTryMWYcZzH7v_61G0AhbDAf6ZnMs6Pmr8_CsI1J2Am5eYpoqyz-HgAh-4pQ7pSmGQbG6JJ2HiH3cJuIwRPuTrJrIAZXJMdLwGu7IIYkJkJm8x1RP8VE3BeTwUrz_np9IahL842ADsFxa3hXIEBsr0An4Et2y13nm731YfR9YgA8DGZKoY1-7MNsdON55G_1YecDEYuWPWxi-EETFZDMdz6ta843thwJqfRxlTb7HEfe7bG3q5g672ZQKNWaKoXZeTrM2MZVIZs8sWNnyFwYnl5wD_i_LaSlgpa17DBnzLHwrG4rVXpUPhdCLJb3NzzOBfk16HlcMwtmN76tkztolTmhYu8p01n_iKG5dy93_hh2UQqxt0tfF3u5eIl2xePhwLKs-AEl04YJSsdbymGRr5ZWnD545gkOWzQ88kRXeO0hyukvPmjki7X3cUUVNPH-UoENm638lNlTi4pUPu5lJGeysr00Xh0vkO6GY4dlbltcLt3vNROLlap0IPFRSfdnUr_edhWFPK84RYNMfX-TvMK6Lt0ErLDOalM=",
                "deep_link": "https://www.kiwi.com/deep?affilid=apoorvflightsearch&currency=EUR&flightsId=07111b744bc9000011f53b78_0&from=DEL&lang=en&passengers=1&to=BHO&booking_token=EyUF5oFgHd899ftiDbnUKyoP4IdVc5AGMf-9HZjyl4-DZWfsyuM1IYvo8a4tJJqkSvqhZ4MfY6zWMcmglW2BV9qD60ulkoEnCYvKuETGqqEI-WJr05xFcUIt-E5wby_4wpaYaWp4k9xEhBYm1bSo0kdtcwY-ra4IuT2uWdRs2TCwbQ8qO1guhYlmIsEn6easQ5DfO2yGYOn6b6sI4E2h2MUSjrtB64A_Y_MAdOVQ80nGIue_FQjg1xU9chlv2dW8OzYWjQx9jWKUTMXjFxe0bFSfSNoFpDMixaFy-kIgJYZYNbwYWw3iQpRYLRiVgczb5JpHK6YgOzAat6zQH20Dq2u_EABBwfcpwY6UznZWVDxfj6_e_dBN24BsEUaNFEfQGrj5lhykVujKYqJDJmAyL0G-H-i01S83c-AwszQMa82I=",
                "facilitated_booking_available": True,
                "pnr_count": 1,
                "has_airport_change": False,
                "technical_stops": 0,
                "throw_away_ticketing": False,
                "hidden_city_ticketing": False,
                "virtual_interlining": False,
                "local_arrival": "2023-02-13T15:55:00.000Z",
                "utc_arrival": "2023-02-13T10:25:00.000Z",
                "local_departure": "2023-02-13T14:30:00.000Z",
                "utc_departure": "2023-02-13T09:00:00.000Z"
            },
            {
                "id": "07111b744bc70000aa1c7b88_0",
                "flyFrom": "DEL",
                "flyTo": "BHO",
                "cityFrom": "New Delhi",
                "cityCodeFrom": "DEL",
                "cityTo": "Bhopal",
                "cityCodeTo": "BHO",
                "countryFrom": {
                    "code": "IN",
                    "name": "India"
                },
                "countryTo": {
                    "code": "IN",
                    "name": "India"
                },
                "nightsInDest": "None",
                "quality": 85.333275,
                "distance": 588.1,
                "duration": {
                    "departure": 5100,
                    "return": 0,
                    "total": 5100
                },
                "price": 62,
                "conversion": {
                    "EUR": 62
                },
                "bags_price": {
                    "1": 0
                },
                "baglimit": {
                    "hand_height": 38,
                    "hand_length": 57,
                    "hand_weight": 7,
                    "hand_width": 20,
                    "hold_dimensions_sum": 158,
                    "hold_height": 52,
                    "hold_length": 78,
                    "hold_weight": 15,
                    "hold_width": 28
                },
                "availability": {
                    "seats": "None"
                },
                "airlines": [
                    "6E"
                ],
                "route": [
                    {
                        "id": "07111b744bc70000aa1c7b88_0",
                        "combination_id": "07111b744bc70000aa1c7b88",
                        "flyFrom": "DEL",
                        "flyTo": "BHO",
                        "cityFrom": "New Delhi",
                        "cityCodeFrom": "DEL",
                        "cityTo": "Bhopal",
                        "cityCodeTo": "BHO",
                        "airline": "6E",
                        "flight_no": 6822,
                        "operating_carrier": "6E",
                        "operating_flight_no": "6822",
                        "fare_basis": "P0IP",
                        "fare_category": "M",
                        "fare_classes": "P",
                        "fare_family": "",
                        "return": 0,
                        "bags_recheck_required": False,
                        "vi_connection": False,
                        "guarantee": False,
                        "equipment": "None",
                        "vehicle_type": "aircraft",
                        "local_arrival": "2023-02-11T15:55:00.000Z",
                        "utc_arrival": "2023-02-11T10:25:00.000Z",
                        "local_departure": "2023-02-11T14:30:00.000Z",
                        "utc_departure": "2023-02-11T09:00:00.000Z"
                    }
                ],
                "booking_token": "EK264ilnCsRpIk-7XOauxnClSX0YkxMSIuWJOgmF9VAKbtZ-qyGA9EyKMkscOz9t8CrJJdtXpiuSSAOsADkK8vQi4Zl3OrqzcDyPAH8AaRLO8VxwPhIqaip0pf2RiObC705_PrYLUFnEPBrNCQTuogifW3yJ5hI1h2WOMbsNrYpwS-BY9_6u2CrFkBKwMb1syfHskcUbu_PsrpOgPDf9bVv20wM_dtUg5Iz92KjsfPBSUMW0tUh2C3mC4eylB2YBmzD1dQsqf6921VXu3G15i5o3YZ315j1yZQtZb1QaxofEkyqDONWpnZEmt7CeFQyPJlbs_AFu8auAlF7BdjbnRDrIzXfG1xsVuI3h4JjEz9peAh-nj_kETe-m2fe7CA5mdc0RFTaNAi1HvpL2ms4l7wa6_TZ7v-MkiLhhn7J3YaEB_Dnu3vssJuDw59RlQB5lfEKi_oow-3QdhdaYM6CDSd6-ZHMiI-Er7T4ROqSsEqUumJ4gzOSc2eZN3lKnSgaQ3L3CbjnI9Co3XaOp8DKtetbtE-WPRbLDOjOjdrsg7-iBk22O058WXrzZrgLSo_U1XrJtyKaYCAqRFNb6CWstAfrfjNE0Uyxa52wF3gRmAw1s=",
                "deep_link": "https://www.kiwi.com/deep?affilid=apoorvflightsearch&currency=EUR&flightsId=07111b744bc70000aa1c7b88_0&from=DEL&lang=en&passengers=1&to=BHO&booking_token=EQJ8MILLfKtLUV0xxX6CcdVF66xZbC68PVr3SmFhfhkMY8krIBaMOTfBYeuIFrF7f0BoVErrRtPI4P7-y1G30Fbuv9nesDbLba3FSG5HN-HEOtfkizi7wl-oTIxHkvkuV3tQlLyqCUKgRDMBMsiWTIiuhpH7Oy3r-C4ZRPqG6Uk5rqQWGp5NJv2F1XSOKBggHmxx8IRA0O2pzaPqszrJhKNo0on4c3v81_TCzCJKf9xR3OtLO874qHFPdm3e6qDn7JBWxid0Z2Gng5qFHLwGQhHfyj_3T7jBbLdSfUlJf2sCqYA_cSoiV7siuZ2vPb-MwpMKZ1pOGjki6DmQZ2ExyxFuIkiigO95C3OW7u2EKVt8PDS9i82DFUilZGhTejWUt5haPkeF23FSEZ8TM8Sd5Jt3mz8xB_J-fn4bXGFusANX0a-B6slRFB8l0wHld8nQP9qCTg0obblguDblgLui8h4wxq8EiylozI1azedyUcms=",
                "facilitated_booking_available": True,
                "pnr_count": 1,
                "has_airport_change": False,
                "technical_stops": 0,
                "throw_away_ticketing": False,
                "hidden_city_ticketing": False,
                "virtual_interlining": False,
                "local_arrival": "2023-02-11T15:55:00.000Z",
                "utc_arrival": "2023-02-11T10:25:00.000Z",
                "local_departure": "2023-02-11T14:30:00.000Z",
                "utc_departure": "2023-02-11T09:00:00.000Z"
            },
            {
                "id": "071107194bc600002e84c38e_0",
                "flyFrom": "DEL",
                "flyTo": "DED",
                "cityFrom": "New Delhi",
                "cityCodeFrom": "DEL",
                "cityTo": "Dehradun",
                "cityCodeTo": "DED",
                "countryFrom": {
                    "code": "IN",
                    "name": "India"
                },
                "countryTo": {
                    "code": "IN",
                    "name": "India"
                },
                "nightsInDest": "None",
                "quality": 93.66662,
                "distance": 208.74,
                "duration": {
                    "departure": 3000,
                    "return": 0,
                    "total": 3000
                },
                "price": 75,
                "conversion": {
                    "EUR": 75
                },
                "bags_price": {
                    "1": 0
                },
                "baglimit": {
                    "hand_height": 38,
                    "hand_length": 57,
                    "hand_weight": 7,
                    "hand_width": 20,
                    "hold_dimensions_sum": 158,
                    "hold_height": 52,
                    "hold_length": 78,
                    "hold_weight": 15,
                    "hold_width": 28
                },
                "availability": {
                    "seats": 4
                },
                "airlines": [
                    "6E"
                ],
                "route": [
                    {
                        "id": "071107194bc600002e84c38e_0",
                        "combination_id": "071107194bc600002e84c38e",
                        "flyFrom": "DEL",
                        "flyTo": "DED",
                        "cityFrom": "New Delhi",
                        "cityCodeFrom": "DEL",
                        "cityTo": "Dehradun",
                        "cityCodeTo": "DED",
                        "airline": "6E",
                        "flight_no": 2071,
                        "operating_carrier": "6E",
                        "operating_flight_no": "2071",
                        "fare_basis": "V0IP",
                        "fare_category": "M",
                        "fare_classes": "X",
                        "fare_family": "",
                        "return": 0,
                        "bags_recheck_required": False,
                        "vi_connection": False,
                        "guarantee": False,
                        "equipment": "None",
                        "vehicle_type": "aircraft",
                        "local_arrival": "2023-02-10T17:45:00.000Z",
                        "utc_arrival": "2023-02-10T12:15:00.000Z",
                        "local_departure": "2023-02-10T16:55:00.000Z",
                        "utc_departure": "2023-02-10T11:25:00.000Z"
                    }
                ],
                "booking_token": "EPdmZ1Hw9N68Ht18F5EbzwK0yY3lkio2FgpY-UwiAz0GDR6vihBvnBH5Ld-8pMDE0UJbS6QhCukM4K1u1EowEBHoRtAL3pYdygJoJfGH9hjkVzwp65dZiMqjJJRYpDmzeImedRH-WfORCz-jg-X05yyZEKlig9HJR47tGITHxOBJ7JuLSsGkV9OPAf7F1-BwjCnj0-5gtrNftu7UA3jgo24ocqTKvx6Mt1vv4BpgDdwQN7_scbgQlSejAM-S2uBPR385mQpoKeiNMaOv-qwDiOVCuWkfKaYuixXAmEIFOWpDKY0J3qkQ0diYswR7f8JQ6NyHr58Pw_yo2CrKUNLz4A100EonaDxKbWM3zfDiIYvQdnJXX4bW_6uHoTS4vg-2dSB8NyT7HnZtTnEmL0BSOnRxfEkpns9SBzmXgUQntLr_EpE8Yn6LtEfYcKNwkGHDqHKbCMzYo50D38VHiD0Rk_hEu9AaKU9AmvzwaZC6UdOuPh4exK8ZFrOtxOFzJfkY4EQq0l37u5-dfkyIrG8F9ntKim-BKhWwQjYVjuesBNSA=",
                "deep_link": "https://www.kiwi.com/deep?affilid=apoorvflightsearch&currency=EUR&flightsId=071107194bc600002e84c38e_0&from=DEL&lang=en&passengers=1&to=DED&booking_token=EHT5KMAxlkHttfMdCMpJGgrNWFNGIkB6CCFHyF4FVL8aF7dY-5i2xPgfXdXuULSyxMnMyvhybikqcyWNEANoKHMJDrEA7XeCRXgN0EF39mQLnwoGnBKPOb4CMSQ-v0hfBB5OTiJRSUtXmbkW34ly5R3Mfhfvxdz30ZKMtM359coYtY0Q3WkhAdQf_eO79ls7hWOxvGfFgRXTqlgP6q6Isop4Ulp8Cecz-Xmvm-pLwKz7qweBnPt_FTftBmpwD9ZIxL3q5QM0vUkQFnQg06Sarj6Dz2tbhyuoZx_HZjrYjGwibTAH5OGUCyvI_mDxQkprZWiefwZoWmjaCnwDiVLLjeqeRMlsP8K-75gx2uNY_4ptPoHgRiwTgKB_cE7vsB2LDoAaLvyzPZRuEEhjnQ5G8rGXYNbra_gqZFnsJHL9MBuA=",
                "facilitated_booking_available": True,
                "pnr_count": 1,
                "has_airport_change": False,
                "technical_stops": 0,
                "throw_away_ticketing": False,
                "hidden_city_ticketing": False,
                "virtual_interlining": False,
                "local_arrival": "2023-02-10T17:45:00.000Z",
                "utc_arrival": "2023-02-10T12:15:00.000Z",
                "local_departure": "2023-02-10T16:55:00.000Z",
                "utc_departure": "2023-02-10T11:25:00.000Z"
            },
            {
                "id": "071107194bc6000036de4c10_0",
                "flyFrom": "DEL",
                "flyTo": "DED",
                "cityFrom": "New Delhi",
                "cityCodeFrom": "DEL",
                "cityTo": "Dehradun",
                "cityCodeTo": "DED",
                "countryFrom": {
                    "code": "IN",
                    "name": "India"
                },
                "countryTo": {
                    "code": "IN",
                    "name": "India"
                },
                "nightsInDest": "None",
                "quality": 93.66662,
                "distance": 208.74,
                "duration": {
                    "departure": 3000,
                    "return": 0,
                    "total": 3000
                },
                "price": 75,
                "conversion": {
                    "EUR": 75
                },
                "bags_price": {
                    "1": 0
                },
                "baglimit": {
                    "hand_height": 38,
                    "hand_length": 57,
                    "hand_weight": 7,
                    "hand_width": 20,
                    "hold_dimensions_sum": 158,
                    "hold_height": 52,
                    "hold_length": 78,
                    "hold_weight": 15,
                    "hold_width": 28
                },
                "availability": {
                    "seats": 2
                },
                "airlines": [
                    "6E"
                ],
                "route": [
                    {
                        "id": "071107194bc6000036de4c10_0",
                        "combination_id": "071107194bc6000036de4c10",
                        "flyFrom": "DEL",
                        "flyTo": "DED",
                        "cityFrom": "New Delhi",
                        "cityCodeFrom": "DEL",
                        "cityTo": "Dehradun",
                        "cityCodeTo": "DED",
                        "airline": "6E",
                        "flight_no": 2582,
                        "operating_carrier": "6E",
                        "operating_flight_no": "2582",
                        "fare_basis": "V0IP",
                        "fare_category": "M",
                        "fare_classes": "X",
                        "fare_family": "",
                        "return": 0,
                        "bags_recheck_required": False,
                        "vi_connection": False,
                        "guarantee": False,
                        "equipment": "None",
                        "vehicle_type": "aircraft",
                        "local_arrival": "2023-02-10T19:05:00.000Z",
                        "utc_arrival": "2023-02-10T13:35:00.000Z",
                        "local_departure": "2023-02-10T18:15:00.000Z",
                        "utc_departure": "2023-02-10T12:45:00.000Z"
                    }
                ],
                "booking_token": "Ebg65jWI-5efN2-MaSHy5vsKOgu0VZUTr7xIOkPcHqKC6T4S6QpPmNAC8mUSlKfq2_L1SRm8lN-ommrvR6e573MGTJsEt3ijWEP5_AML36GqX9aTaRORU05VbQDS0GqU6H3uIIY0ETd0_3hC5ZQXFXY8a_L7eE38tNyoSQAAlcU2mEko8VzWX3E8KL2YiX2hcCLu2XGS_5D7uktsKynAiUTUVrJREQC_vXtWpfPkKHCxpOsJtN1aBNmZHfaciBomnKw5vg0ut6H0Kot0yUnte2fndCDEuHrJvULqWVE6k360-M9S-l2dFSfroewh7c1vk0KmCHRs9t4ENSWT8Csn72SpLDkcZ-HInddpOq1p4vYin6MsaNkXldfemrR4vUyHj2q0Y4g0ztxbp4EYRIavyuOBcd0kGWiX3bg2Ap1UklKHn73v2-38jm69D6f0GpKEri0h4KaRcv3wBOmFPV9wzNe_-3FPHNd-YEp8HpYB0M58RVeVCeTdKQsh1C-peSZZVihgwugSMv09BQ989HqoM4L1sV5Tqcpx4m__Bvsh_GF3N1cgxMlZFrdr5ufTtiTAO",
                "deep_link": "https://www.kiwi.com/deep?affilid=apoorvflightsearch&currency=EUR&flightsId=071107194bc6000036de4c10_0&from=DEL&lang=en&passengers=1&to=DED&booking_token=ENtMmJfaTzCDWQyx2eyOB3tdnp2kBed7Fish50QiWtuiZ37GLiACLYD3al3dIq5Sl58ukKjTysHwDhTRAe187wFIl-xEGgwzzll7fq8kGlsBwoLvOn67v7aO_PTz_ovleZOdAjriNXZ7Lmh0nkXFbrw5Q98mjGh1WEcxJvUeWfMRyOiweRKu21yVk63csWSjO5dD9cfjsaIN0yuDsQVFndn1LU7CgPzafAhpxLTV3u4lpHIddaFZukFT_w1phxBJqjOwMwDlQfO1i9cQyl5YuJLAJM3_6Jyt77U6meVh7_w9D5AtPc0kHAvEmmDNnB4MDn6BXksPm9TvdfRkv6uSXtj24fOaK4DYzSKUnV9FPMkS5RNBKvSi7de1ba2QfEuTrtFA-huMPhQ9U_bjjGItCBUOQshcyd5UEcSjzT7_MzKhj_phLc3LrqA6sNHAZMaqj",
                "facilitated_booking_available": True,
                "pnr_count": 1,
                "has_airport_change": False,
                "technical_stops": 0,
                "throw_away_ticketing": False,
                "hidden_city_ticketing": False,
                "virtual_interlining": False,
                "local_arrival": "2023-02-10T19:05:00.000Z",
                "utc_arrival": "2023-02-10T13:35:00.000Z",
                "local_departure": "2023-02-10T18:15:00.000Z",
                "utc_departure": "2023-02-10T12:45:00.000Z"
            },
            {
                "id": "071107194bc80000db54aa3c_0",
                "flyFrom": "DEL",
                "flyTo": "DED",
                "cityFrom": "New Delhi",
                "cityCodeFrom": "DEL",
                "cityTo": "Dehradun",
                "cityCodeTo": "DED",
                "countryFrom": {
                    "code": "IN",
                    "name": "India"
                },
                "countryTo": {
                    "code": "IN",
                    "name": "India"
                },
                "nightsInDest": "None",
                "quality": 93.66662,
                "distance": 208.74,
                "duration": {
                    "departure": 3000,
                    "return": 0,
                    "total": 3000
                },
                "price": 75,
                "conversion": {
                    "EUR": 75
                },
                "bags_price": {
                    "1": 0
                },
                "baglimit": {
                    "hand_height": 38,
                    "hand_length": 57,
                    "hand_weight": 7,
                    "hand_width": 20,
                    "hold_dimensions_sum": 158,
                    "hold_height": 52,
                    "hold_length": 78,
                    "hold_weight": 15,
                    "hold_width": 28
                },
                "availability": {
                    "seats": 2
                },
                "airlines": [
                    "6E"
                ],
                "route": [
                    {
                        "id": "071107194bc80000db54aa3c_0",
                        "combination_id": "071107194bc80000db54aa3c",
                        "flyFrom": "DEL",
                        "flyTo": "DED",
                        "cityFrom": "New Delhi",
                        "cityCodeFrom": "DEL",
                        "cityTo": "Dehradun",
                        "cityCodeTo": "DED",
                        "airline": "6E",
                        "flight_no": 2071,
                        "operating_carrier": "6E",
                        "operating_flight_no": "2071",
                        "fare_basis": "V0IP",
                        "fare_category": "M",
                        "fare_classes": "X",
                        "fare_family": "",
                        "return": 0,
                        "bags_recheck_required": False,
                        "vi_connection": False,
                        "guarantee": False,
                        "equipment": "None",
                        "vehicle_type": "aircraft",
                        "local_arrival": "2023-02-12T17:45:00.000Z",
                        "utc_arrival": "2023-02-12T12:15:00.000Z",
                        "local_departure": "2023-02-12T16:55:00.000Z",
                        "utc_departure": "2023-02-12T11:25:00.000Z"
                    }
                ],
                "booking_token": "EU7Lmho6ZTqMhh2ZqISRadG_CGZZW199GjCCEpYcAJ7Np6MSUIZA1Mu14T-GmMvtHM1gumxLU_CMKiJxeBB0cddolEEUVw7ESI3rN7RY3uVWtQ34BI5U1u9rymTTz9gBktYc7HM1agxiGtXxhMyUKeOCl4qNw9Vk4hZ49wMUNYmSmr5owpPTu1DJnu3bK66H6HKFGbEBsjyozD0PT1PBsfUvb_vAV-ME_puOExlMYy8SlNczoTgaldMpFMIkEQF3OpYVVXLoA8D7aY-YtI8xGq59KXjclsnDrV3tOZihoXgXQ-6cHpMtSubN91wqPccklHb0XzOXqmUVjTyMhEJ2Rz0u061a91UcEZPMLFmjUEWTGIGwrgUap51itoqyUoTVgnrKHJumAiSZFrz_MwtA3ORF6z4p9cRzled7flsIkU0Nt96fMIhOh33D1AHok_K8pzpKo7HkIThGwlX69MYR5bZ2cIduG24UYmFsGwaZLUhWdD9g3U4_nQISp8jKY217QvxkyVbkoqHAftZPjOMFniRf9xqWt3f112EoFcsKx2KA=",
                "deep_link": "https://www.kiwi.com/deep?affilid=apoorvflightsearch&currency=EUR&flightsId=071107194bc80000db54aa3c_0&from=DEL&lang=en&passengers=1&to=DED&booking_token=Em33M8v-ciI9wzC1DTZ_V_kqLMf4PB8B4rqMMSPuFNH7NsVTEhPN_Ob4bcCx0Ne0AEPsWeAuJpKp9HHMhv57keSPPiHI2dagHwQbon_Fa2jlB3mUijFyl1-9FOSUYmt8J9n5LqPGwo2DoYW5SEbw1bOeJwei051e1QsLRwndzZWscGrAQfUfmHIZKiAJ9kD1Jjm6hyjQNK5HgTqakN-azjhFB1Gis3jAIAD1KV7wa7ptzqMBu7HMxtFDCxK-7ZsAQpaxqYJYy6q2Ezsdl5i268cgEJ9UffvltUS3vMhoX549ILM0oqqP8Bt9v5q-01hMK1Y6H-VNkpUMcwjlU7UlPVVBYPcXOwjojwqHftu4xKlkCnroWokccYq1DqUogmRNQwcJqdmYSNY0-Vp1uwdCai2GmVIovw6ZgRxmeZ0ulTng=",
                "facilitated_booking_available": True,
                "pnr_count": 1,
                "has_airport_change": False,
                "technical_stops": 0,
                "throw_away_ticketing": False,
                "hidden_city_ticketing": False,
                "virtual_interlining": False,
                "local_arrival": "2023-02-12T17:45:00.000Z",
                "utc_arrival": "2023-02-12T12:15:00.000Z",
                "local_departure": "2023-02-12T16:55:00.000Z",
                "utc_departure": "2023-02-12T11:25:00.000Z"
            }
        ],
        "_results": 117,
        "search_params": {
            "flyFrom_type": "airport",
            "to_type": "city",
            "seats": {
                "passengers": 1,
                "adults": 1,
                "children": 0,
                "infants": 0
            }
        },
        "all_stopover_airports": [

        ],
        "sort_version": 0
    }

    fd = FlightData(fs)
