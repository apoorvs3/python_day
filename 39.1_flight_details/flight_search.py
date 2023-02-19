import requests
from datetime import datetime, timedelta


class FlightSearch:
    # This class is responsible for talking to the Flight Search API.
    def __init__(self, fly_to: str):
        self.FLIGHT_API_KEY = 'NM8Y87WP24zVyQgjfiGAWv8nrCyfh2Rd'
        self.fly_from = 'DEL'
        self.fly_to = fly_to

        self.body = {
            'fly_from': f'{self.fly_from}',
            'fly_to': f'{self.fly_to}',
            'date_from': f'{((datetime.today() + timedelta(days=2)).strftime("%d/%m/%Y"))}',
            'date_to': f'{(datetime.today() + timedelta(days=30 * 6)).strftime("%d/%m/%Y")}',
            'locale': 'en',
            'limit': 18
        }
        self.end_point = 'https://api.tequila.kiwi.com/v2/search'
        self.HEADER = {
            'accept': 'application/json',
            'apikey': self.FLIGHT_API_KEY
        }

    def search_flight_price(self):
        response = requests.get(url=self.end_point, params=self.body, headers=self.HEADER).json()
        # response = {
        #     "search_id": "9112d332-b26c-9454-1551-c941519c3e20",
        #     "currency": "EUR",
        #     "fx_rate": 1,
        #     "data": [
        #         {
        #             "id": "071110db4bcb000077a95b06_0|071110db4bcb000077a95b06_1|10db1cb24bcb00003ef6ba51_0",
        #             "flyFrom": "DEL",
        #             "flyTo": "BVA",
        #             "cityFrom": "New Delhi",
        #             "cityCodeFrom": "DEL",
        #             "cityTo": "Paris",
        #             "cityCodeTo": "PAR",
        #             "countryFrom": {
        #                 "code": "IN",
        #                 "name": "India"
        #             },
        #             "countryTo": {
        #                 "code": "FR",
        #                 "name": "France"
        #             },
        #             "nightsInDest": 'null',
        #             "quality": 472.999515,
        #             "distance": 6596.09,
        #             "duration": {
        #                 "departure": 81900,
        #                 "return": 0,
        #                 "total": 81900
        #             },
        #             "price": 279,
        #             "conversion": {
        #                 "EUR": 279
        #             },
        #             "fare": {
        #                 "adults": 279,
        #                 "children": 279,
        #                 "infants": 279
        #             },
        #             "bags_price": {
        #                 "1": 113.033
        #             },
        #             "baglimit": {
        #                 "hand_height": 36,
        #                 "hand_length": 55,
        #                 "hand_weight": 7,
        #                 "hand_width": 20,
        #                 "hold_dimensions_sum": 158,
        #                 "hold_height": 50,
        #                 "hold_length": 75,
        #                 "hold_weight": 15,
        #                 "hold_width": 33
        #             },
        #             "availability": {
        #                 "seats": 4
        #             },
        #             "airlines": [
        #                 "FR",
        #                 "XY"
        #             ],
        #             "route": [
        #                 {
        #                     "id": "071110db4bcb000077a95b06_0",
        #                     "combination_id": "071110db4bcb000077a95b06",
        #                     "flyFrom": "DEL",
        #                     "flyTo": "RUH",
        #                     "cityFrom": "New Delhi",
        #                     "cityCodeFrom": "DEL",
        #                     "cityTo": "Riyadh",
        #                     "cityCodeTo": "RUH",
        #                     "airline": "XY",
        #                     "flight_no": 330,
        #                     "operating_carrier": "XY",
        #                     "operating_flight_no": "330",
        #                     "fare_basis": "DCI2I",
        #                     "fare_category": "M",
        #                     "fare_classes": "D",
        #                     "fare_family": "",
        #                     "return": 0,
        #                     "bags_recheck_required": False,
        #                     "vi_connection": False,
        #                     "guarantee": False,
        #                     "equipment": 'null',
        #                     "vehicle_type": "aircraft",
        #                     "local_arrival": "2023-02-15T07:30:00.000Z",
        #                     "utc_arrival": "2023-02-15T04:30:00.000Z",
        #                     "local_departure": "2023-02-15T04:10:00.000Z",
        #                     "utc_departure": "2023-02-14T22:40:00.000Z"
        #                 },
        #                 {
        #                     "id": "071110db4bcb000077a95b06_1",
        #                     "combination_id": "071110db4bcb000077a95b06",
        #                     "flyFrom": "RUH",
        #                     "flyTo": "AMM",
        #                     "cityFrom": "Riyadh",
        #                     "cityCodeFrom": "RUH",
        #                     "cityTo": "Amman",
        #                     "cityCodeTo": "AMM",
        #                     "airline": "XY",
        #                     "flight_no": 251,
        #                     "operating_carrier": "XY",
        #                     "operating_flight_no": "251",
        #                     "fare_basis": "ACI2I",
        #                     "fare_category": "M",
        #                     "fare_classes": "A",
        #                     "fare_family": "",
        #                     "return": 0,
        #                     "bags_recheck_required": False,
        #                     "vi_connection": False,
        #                     "guarantee": False,
        #                     "equipment": 'null',
        #                     "vehicle_type": "aircraft",
        #                     "local_arrival": "2023-02-15T12:25:00.000Z",
        #                     "utc_arrival": "2023-02-15T09:25:00.000Z",
        #                     "local_departure": "2023-02-15T09:45:00.000Z",
        #                     "utc_departure": "2023-02-15T06:45:00.000Z"
        #                 },
        #                 {
        #                     "id": "10db1cb24bcb00003ef6ba51_0",
        #                     "combination_id": "10db1cb24bcb00003ef6ba51",
        #                     "flyFrom": "AMM",
        #                     "flyTo": "BVA",
        #                     "cityFrom": "Amman",
        #                     "cityCodeFrom": "AMM",
        #                     "cityTo": "Paris",
        #                     "cityCodeTo": "PAR",
        #                     "airline": "FR",
        #                     "flight_no": 9734,
        #                     "operating_carrier": "",
        #                     "operating_flight_no": "",
        #                     "fare_basis": "",
        #                     "fare_category": "M",
        #                     "fare_classes": "",
        #                     "fare_family": "",
        #                     "return": 0,
        #                     "bags_recheck_required": True,
        #                     "vi_connection": True,
        #                     "guarantee": True,
        #                     "equipment": 'null',
        #                     "vehicle_type": "aircraft",
        #                     "local_arrival": "2023-02-15T22:25:00.000Z",
        #                     "utc_arrival": "2023-02-15T21:25:00.000Z",
        #                     "local_departure": "2023-02-15T19:05:00.000Z",
        #                     "utc_departure": "2023-02-15T16:05:00.000Z"
        #                 }
        #             ],
        #             "booking_token": "Esmcn7GAQr7cW0bEccPtniCtd0Exf23JF_C_01yDy2DOriKLCV-HJwsY7nr4WNSH4pAZdfaUIjcEPshhFFxua373bI8r5r7eqv3H4O2IhqxQ5cgSBOubeaI8nc2HTLutR7iaO7kVc9e23Hx5cKUUxzje94osKSUSpmWR-rtKX_TW9PczrXld8j_qvXlHylBY_vGSUi2q2GhKnQJz1BV8xaOSQzEnJO_7k2lqRl9N1oGcnl1P_kYQl2qcTn0F_FhH76_OGC28Ij0qL-d3sg65JuVC5c3-rj-aMDdDpgXfJmjpZd3_3auD36NZb_UZog5GYBcnzH-K5TnWI9o2Pyi2Dd0vZT8grvfn1-7NdHFxNlEuLa6DXnlu-Fiie05iHJGKwDtrB-Fx2Qzpt2xBeZgLzvaG5i9yAbzdw9yFSgJPSHdDPqD0SIgSbnpgcsvkPVNqmmia5LVKqR5sUWcAXg-znkdW_na5RaooQzb02ansdsl7iSNYVPx4EkJ_MA1bodxgzDWm0bSUsd7eVWJ0p5uULS5M3OeB2OBgHGO5ALn7wEDa69TiFaEkD0GF1oI_fS238Epk0hplGI2C712LxiMPZtLYvTiI1acI55xKhiBVdoYrK4bQfiCVVuyBGNdOpNCtIVS6IuiB4FOEPYJHvwr5Z0Q0fYCF1FM03iuy31Fb6FqgWqZ6MRStUywCv4Lng3WqloCw568xx4Vb9ib3nahHVUQ==",
        #             "deep_link": "https://www.kiwi.com/deep?affilid=apoorvflightsearch&currency=EUR&flightsId=071110db4bcb000077a95b06_0%7C071110db4bcb000077a95b06_1%7C10db1cb24bcb00003ef6ba51_0&from=DEL&lang=en&passengers=1&to=BVA&booking_token=Eh99G7Z7GcywnfCbSOomSyvl_wbQtqXPJOYa1mYaZNwYXfURd5JdbncDuwiO4OpvFjr1T-j4QhllCDhLgA72VXHmkhNdgF8j4YkDlECz-9D6I06mdPwLlB3kBi5p4dJ9W9gAald2yEUttegLEhALddc2EZzKvRySNqbb50fauK60wAh_6otTQ97lzMiPBhlUr5PJdjg0ikJopvDxukn5fH-XZ4Czm9CI2o7gUheuuSAvswQveUfVfSimPMt9cKrs-vT3bNaJkGHv2hSG3SYDLuJ5ocF_HmjASwHV76xUg-bVRRq1zOEZck6Sio9s726PsaEbUVlG51gxdIYcx5zN---n7hsQZB-8pOY7kULMlu0nPLc1F_-dkOGLqxCjZEqHlgNwN9cl8CpwK-1N9z4IyyxxTCfKN6dXhwRA6M9pd-NrzzFheLudK_gwYoZHbDON54YUwfD7nraRJ8YJ9WR3CZtFJCXydauH3tLgf_DhyD5qvgagIj-RA1ad9UTX4UCkObb71AiGFo1QHPtHtNxko6bMisby0CwYauTwqLIUo9DJ9BaUy9TlhLvJx0fl1hfVWRFeM2qDklOxDLwNzBcbllQ==",
        #             "facilitated_booking_available": False,
        #             "pnr_count": 2,
        #             "has_airport_change": False,
        #             "technical_stops": 0,
        #             "throw_away_ticketing": False,
        #             "hidden_city_ticketing": False,
        #             "virtual_interlining": True,
        #             "local_arrival": "2023-02-15T22:25:00.000Z",
        #             "utc_arrival": "2023-02-15T21:25:00.000Z",
        #             "local_departure": "2023-02-15T04:10:00.000Z",
        #             "utc_departure": "2023-02-14T22:40:00.000Z"
        #         },
        #         {
        #             "id": "071110db4bc8000069733ce3_0|071110db4bc8000069733ce3_1|10db1cb24bc8000043fbbc4c_0",
        #             "flyFrom": "DEL",
        #             "flyTo": "BVA",
        #             "cityFrom": "New Delhi",
        #             "cityCodeFrom": "DEL",
        #             "cityTo": "Paris",
        #             "cityCodeTo": "PAR",
        #             "countryFrom": {
        #                 "code": "IN",
        #                 "name": "India"
        #             },
        #             "countryTo": {
        #                 "code": "FR",
        #                 "name": "France"
        #             },
        #             "nightsInDest": 'null',
        #             "quality": 503.33285,
        #             "distance": 6596.09,
        #             "duration": {
        #                 "departure": 81600,
        #                 "return": 0,
        #                 "total": 81600
        #             },
        #             "price": 310,
        #             "conversion": {
        #                 "EUR": 310
        #             },
        #             "fare": {
        #                 "adults": 310,
        #                 "children": 310,
        #                 "infants": 310
        #             },
        #             "bags_price": {
        #                 "1": 88.383
        #             },
        #             "baglimit": {
        #                 "hand_height": 36,
        #                 "hand_length": 55,
        #                 "hand_weight": 7,
        #                 "hand_width": 20,
        #                 "hold_dimensions_sum": 158,
        #                 "hold_height": 50,
        #                 "hold_length": 75,
        #                 "hold_weight": 15,
        #                 "hold_width": 33
        #             },
        #             "availability": {
        #                 "seats": 6
        #             },
        #             "airlines": [
        #                 "FR",
        #                 "XY"
        #             ],
        #             "route": [
        #                 {
        #                     "id": "071110db4bc8000069733ce3_0",
        #                     "combination_id": "071110db4bc8000069733ce3",
        #                     "flyFrom": "DEL",
        #                     "flyTo": "RUH",
        #                     "cityFrom": "New Delhi",
        #                     "cityCodeFrom": "DEL",
        #                     "cityTo": "Riyadh",
        #                     "cityCodeTo": "RUH",
        #                     "airline": "XY",
        #                     "flight_no": 330,
        #                     "operating_carrier": "XY",
        #                     "operating_flight_no": "330",
        #                     "fare_basis": "DCI2I",
        #                     "fare_category": "M",
        #                     "fare_classes": "D",
        #                     "fare_family": "",
        #                     "return": 0,
        #                     "bags_recheck_required": False,
        #                     "vi_connection": False,
        #                     "guarantee": False,
        #                     "equipment": 'null',
        #                     "vehicle_type": "aircraft",
        #                     "local_arrival": "2023-02-12T07:30:00.000Z",
        #                     "utc_arrival": "2023-02-12T04:30:00.000Z",
        #                     "local_departure": "2023-02-12T04:10:00.000Z",
        #                     "utc_departure": "2023-02-11T22:40:00.000Z"
        #                 },
        #                 {
        #                     "id": "071110db4bc8000069733ce3_1",
        #                     "combination_id": "071110db4bc8000069733ce3",
        #                     "flyFrom": "RUH",
        #                     "flyTo": "AMM",
        #                     "cityFrom": "Riyadh",
        #                     "cityCodeFrom": "RUH",
        #                     "cityTo": "Amman",
        #                     "cityCodeTo": "AMM",
        #                     "airline": "XY",
        #                     "flight_no": 251,
        #                     "operating_carrier": "XY",
        #                     "operating_flight_no": "251",
        #                     "fare_basis": "ACI2I",
        #                     "fare_category": "M",
        #                     "fare_classes": "A",
        #                     "fare_family": "",
        #                     "return": 0,
        #                     "bags_recheck_required": False,
        #                     "vi_connection": False,
        #                     "guarantee": False,
        #                     "equipment": 'null',
        #                     "vehicle_type": "aircraft",
        #                     "local_arrival": "2023-02-12T12:25:00.000Z",
        #                     "utc_arrival": "2023-02-12T09:25:00.000Z",
        #                     "local_departure": "2023-02-12T09:45:00.000Z",
        #                     "utc_departure": "2023-02-12T06:45:00.000Z"
        #                 },
        #                 {
        #                     "id": "10db1cb24bc8000043fbbc4c_0",
        #                     "combination_id": "10db1cb24bc8000043fbbc4c",
        #                     "flyFrom": "AMM",
        #                     "flyTo": "BVA",
        #                     "cityFrom": "Amman",
        #                     "cityCodeFrom": "AMM",
        #                     "cityTo": "Paris",
        #                     "cityCodeTo": "PAR",
        #                     "airline": "FR",
        #                     "flight_no": 9734,
        #                     "operating_carrier": "",
        #                     "operating_flight_no": "",
        #                     "fare_basis": "",
        #                     "fare_category": "M",
        #                     "fare_classes": "",
        #                     "fare_family": "",
        #                     "return": 0,
        #                     "bags_recheck_required": True,
        #                     "vi_connection": True,
        #                     "guarantee": True,
        #                     "equipment": 'null',
        #                     "vehicle_type": "aircraft",
        #                     "local_arrival": "2023-02-12T22:20:00.000Z",
        #                     "utc_arrival": "2023-02-12T21:20:00.000Z",
        #                     "local_departure": "2023-02-12T19:00:00.000Z",
        #                     "utc_departure": "2023-02-12T16:00:00.000Z"
        #                 }
        #             ],
        #             "booking_token": "EZncxASXentbUzgK5RIdWpJFD1e1ZIZefkxvRCGIM2tnNrozhdZAQTO_7PpWlN37kKaUNoXSp4XUM29dlSFsXCuuXTPLQnsofvvZvzL-DzDFaUYnfzCP6ysmnf34C6Iy_SLp1g2E986FWXz20iqrRyIC1USdWpNBMYtwDaWneRHMszYXFqr-9bY14oabRu_79cZv9CTi1_vj8MmIG0iPM96jR7pZzu9F90mscg667eJfIIebb9sGTRHfBS22Wnw_HwfC_UdKCpo2SSZIuPrUojJqPHTPa8bCs86KB2pqoLKyps34lf-V6gtrSDLmpAPqgq2UV_jCqZ2ymxxK5EnL5k7RiBK3BGdZpoFUEKB3_NDVULH5SeRSgWR99DqOuVVShLEi0C7zgmHoxZ-yAZISG3yK88Jxkn93iyoOYGllsvZtKEsizEFBLA7XY6Cd7rwVR7kC4SPggOZuhPRf8kqOoSE495D2jn6GQXZXDCvNXsCUtUt6Z2QejqVeqnjHbIs1hvXY5b1nkAXefDj4M8X12PZ17uPlf0do7lhrSKQGTuKRMYQRUAfF4oz0Qv0BO0wg3HYpdUH2TJlB5V13pCE748DblwoFzE3jCXOAku9Yag1ccRjSUCVQXBTUkrrGGkoqEmXeRNPhbgooXuwha4V6Rjw==",
        #             "deep_link": "https://www.kiwi.com/deep?affilid=apoorvflightsearch&currency=EUR&flightsId=071110db4bc8000069733ce3_0%7C071110db4bc8000069733ce3_1%7C10db1cb24bc8000043fbbc4c_0&from=DEL&lang=en&passengers=1&to=BVA&booking_token=E91KXY58DSHrxq5wuSacqspele6MdKkgjZuVQFf2tmrR0MWoLcghbv_1jXKL9hoxenTCwLeem2loIEg9-qRyzdQWpQxRWgdPvd_XNkaUuqcTFs5XKJm3lV88S4WMYtrm4spGlrxX_TYKghoWX22OePksOdby2H2AgoSEbLc8XeNYQQm9OcW74pVkeIMrugXsEGiJYTEsEx0oRfWgSRdUyfVzND-xM6YjxMWB9ePvdSetKhZzW8Byk_Oev1GcpGVYYpjqFdr77wCYsjnbKgHwPO_v7dZdLaGed3iCas44WdHr5wHSDvj8grlIcK9Oc4N2xAPdNTRyLZ5ZWT8aBpWp04En5APHKsGCrDVNYhmUwIJCuX-owAPUQUECmGtNlyTQd_eJzmeeBhbEDm8g3GF1S9O_U6vI7r97A4jKJDtrcOt3xVjBGoJs0lPf-KQDt0OB9SarAfnPn139fHVgCwJe9XYQ7vVlL9Gn_H8wlXFMdIjxuWDCe3A0DVWT4HKp2Nwf3cRAgJlpHjcgvxpkVO2H_zHVO2h1IKqqe0aqXVteprq4=",
        #             "facilitated_booking_available": False,
        #             "pnr_count": 2,
        #             "has_airport_change": False,
        #             "technical_stops": 0,
        #             "throw_away_ticketing": False,
        #             "hidden_city_ticketing": False,
        #             "virtual_interlining": True,
        #             "local_arrival": "2023-02-12T22:20:00.000Z",
        #             "utc_arrival": "2023-02-12T21:20:00.000Z",
        #             "local_departure": "2023-02-12T04:10:00.000Z",
        #             "utc_departure": "2023-02-11T22:40:00.000Z"
        #         },
        #         {
        #             "id": "071103214bc700002cd5339a_0|03210a7c4bc800003f0fad96_0|03210a7c4bc800003f0fad96_1",
        #             "flyFrom": "DEL",
        #             "flyTo": "ORY",
        #             "cityFrom": "New Delhi",
        #             "cityCodeFrom": "DEL",
        #             "cityTo": "Paris",
        #             "cityCodeTo": "PAR",
        #             "countryFrom": {
        #                 "code": "IN",
        #                 "name": "India"
        #             },
        #             "countryTo": {
        #                 "code": "FR",
        #                 "name": "France"
        #             },
        #             "nightsInDest": 'null',
        #             "quality": 497.66624,
        #             "distance": 6590.14,
        #             "duration": {
        #                 "departure": 71400,
        #                 "return": 0,
        #                 "total": 71400
        #             },
        #             "price": 327,
        #             "conversion": {
        #                 "EUR": 327
        #             },
        #             "fare": {
        #                 "adults": 327,
        #                 "children": 327,
        #                 "infants": 327
        #             },
        #             "bags_price": {
        #                 "1": 106.955
        #             },
        #             "baglimit": {
        #                 "hand_height": 35,
        #                 "hand_length": 55,
        #                 "hand_weight": 8,
        #                 "hand_width": 20,
        #                 "hold_dimensions_sum": 158,
        #                 "hold_height": 52,
        #                 "hold_length": 78,
        #                 "hold_weight": 20,
        #                 "hold_width": 28
        #             },
        #             "availability": {
        #                 "seats": 1
        #             },
        #             "airlines": [
        #                 "AI",
        #                 "PC"
        #             ],
        #             "route": [
        #                 {
        #                     "id": "071103214bc700002cd5339a_0",
        #                     "combination_id": "071103214bc700002cd5339a",
        #                     "flyFrom": "DEL",
        #                     "flyTo": "BAH",
        #                     "cityFrom": "New Delhi",
        #                     "cityCodeFrom": "DEL",
        #                     "cityTo": "Bahrain Island",
        #                     "cityCodeTo": "BAH",
        #                     "airline": "AI",
        #                     "flight_no": 939,
        #                     "operating_carrier": "AI",
        #                     "operating_flight_no": "939",
        #                     "fare_basis": "UOWDLBH",
        #                     "fare_category": "M",
        #                     "fare_classes": "U",
        #                     "fare_family": "",
        #                     "return": 0,
        #                     "bags_recheck_required": False,
        #                     "vi_connection": False,
        #                     "guarantee": False,
        #                     "equipment": 'null',
        #                     "vehicle_type": "aircraft",
        #                     "local_arrival": "2023-02-11T21:20:00.000Z",
        #                     "utc_arrival": "2023-02-11T18:20:00.000Z",
        #                     "local_departure": "2023-02-11T19:10:00.000Z",
        #                     "utc_departure": "2023-02-11T13:40:00.000Z"
        #                 },
        #                 {
        #                     "id": "03210a7c4bc800003f0fad96_0",
        #                     "combination_id": "03210a7c4bc800003f0fad96",
        #                     "flyFrom": "BAH",
        #                     "flyTo": "SAW",
        #                     "cityFrom": "Bahrain Island",
        #                     "cityCodeFrom": "BAH",
        #                     "cityTo": "Istanbul",
        #                     "cityCodeTo": "IST",
        #                     "airline": "PC",
        #                     "flight_no": 825,
        #                     "operating_carrier": "PC",
        #                     "operating_flight_no": "825",
        #                     "fare_basis": "IWEBBYD2",
        #                     "fare_category": "M",
        #                     "fare_classes": "I",
        #                     "fare_family": "",
        #                     "return": 0,
        #                     "bags_recheck_required": True,
        #                     "vi_connection": True,
        #                     "guarantee": True,
        #                     "equipment": 'null',
        #                     "vehicle_type": "aircraft",
        #                     "local_arrival": "2023-02-12T06:35:00.000Z",
        #                     "utc_arrival": "2023-02-12T03:35:00.000Z",
        #                     "local_departure": "2023-02-12T02:20:00.000Z",
        #                     "utc_departure": "2023-02-11T23:20:00.000Z"
        #                 },
        #                 {
        #                     "id": "03210a7c4bc800003f0fad96_1",
        #                     "combination_id": "03210a7c4bc800003f0fad96",
        #                     "flyFrom": "SAW",
        #                     "flyTo": "ORY",
        #                     "cityFrom": "Istanbul",
        #                     "cityCodeFrom": "IST",
        #                     "cityTo": "Paris",
        #                     "cityCodeTo": "PAR",
        #                     "airline": "PC",
        #                     "flight_no": 1133,
        #                     "operating_carrier": "PC",
        #                     "operating_flight_no": "1133",
        #                     "fare_basis": "IWEBBYD2",
        #                     "fare_category": "M",
        #                     "fare_classes": "I",
        #                     "fare_family": "",
        #                     "return": 0,
        #                     "bags_recheck_required": False,
        #                     "vi_connection": False,
        #                     "guarantee": False,
        #                     "equipment": 'null',
        #                     "vehicle_type": "aircraft",
        #                     "local_arrival": "2023-02-12T10:30:00.000Z",
        #                     "utc_arrival": "2023-02-12T09:30:00.000Z",
        #                     "local_departure": "2023-02-12T08:35:00.000Z",
        #                     "utc_departure": "2023-02-12T05:35:00.000Z"
        #                 }
        #             ],
        #             "booking_token": "EyGs3ANwOLvnRjrgh6K2Zn0EuJToK3S31ELvVJ8H70jxpFCHIlIrDJptbB8_b3kAiKkaSzQ3fdZdu_XrRmBxAq8X7-qel8d-ToaJf5sA6glVi2i_Od1ODkqiaYuQcebz99O25gF8vqxCR42vQwZVh8GRtU2yS34Qwyfp2FLrnMtVU-lAiifyiep_R8rFVRf8XyrxtMltTsTxbdj01yM2FD0OC9ECdoG-VfEQlf3xylDQNJeAeILOabfmnwRa9pWrM_I6Rx93ONF-aj-PFPaE8PGxW7tDb9-a3ODLJP22TI7-dkrqe6GkfO-mzM2OeXkelnnwnxbZFJUpAbZUSbLQBy6gQcBwzhORHYw9Yj2RmKOPRTLmoflRTE0NAVVBJ7KvEGsRYs6xEXQrR1e2EAr6Df8EjcOBfAX3N0baf0zU68_wBdHmWtUvajCX7uM_dbY3aGVgmZ0S8rorx6AJtD9ae3P50mXILkiP72J18tCduZVZxkqe8zHQDhgrBkCsmnBeAv7WV197P-wlwrLxyVemtQrlkotKjJzgI6FG9UH6YPz_smQbhtkBRngT4mJJeWbOhDBZboGeMBOIZ84KMRzNL9zmgfs0r0XfqZCQEzXmWtJFxXgsrjn1BXkDH2IPjxyvzk0xiS_1ZsbynPb2x7fwEkj8Zx_C31vifvzws-1RICBkmHdwXtKwHBft9Q_f6R_ro",
        #             "deep_link": "https://www.kiwi.com/deep?affilid=apoorvflightsearch&currency=EUR&flightsId=071103214bc700002cd5339a_0%7C03210a7c4bc800003f0fad96_0%7C03210a7c4bc800003f0fad96_1&from=DEL&lang=en&passengers=1&to=ORY&booking_token=Ej04JMxOsSDJkxVaYQGetMWFiESE2W5pGt5XsERTKAGNWzhLJma3ffx2vGZ-97LX820NWX9jy7051U05nwjXm4WZjU6ri4CT1eiRDZhRO4txRudLwmCErmgp2MHWh2k6t3J10nJQXnmXyuKvK-CZkqdeA74RSsGqcSGqwrcOf6XS7pXPd2k26UYIRjw3dFF9w7EwtdXXi3YS6lUBh2Wtlv9xWmRtDn0jJbpTUdatO4ws2gRPWpmtxENp0gtUdezo3aMui0Y2vWFr9unO2p8pQubzThsqRPJXf8TIKIVNHLH0-0L192bdetkXD9YJFm-i9hCtuE1ZpSRpcz8kf7y-qu9DhKT_3bgUIwkd_1rf2aH0fVGtuRfx-cPvWm9FS4YaW824bc75mD1w9XM-MU1R6USQBFcHQyFJIstO7vFR1i2dKW2H-DXtJh5XP34rg-uyHhh2ySzuLG15wUAdWps2217OGR30fnhx6y-CArYVMRlSQohdibvzuuiY2LZhorCNOeQzHp88AfxDKc0lAPZ6oee6tVHjpA14RZ7T7EvUls1O1BXAsaWge8Jv4j85ohqZr5NuFcVehHoS5FVJU8NIiSA==",
        #             "facilitated_booking_available": True,
        #             "pnr_count": 2,
        #             "has_airport_change": False,
        #             "technical_stops": 0,
        #             "throw_away_ticketing": False,
        #             "hidden_city_ticketing": False,
        #             "virtual_interlining": True,
        #             "local_arrival": "2023-02-12T10:30:00.000Z",
        #             "utc_arrival": "2023-02-12T09:30:00.000Z",
        #             "local_departure": "2023-02-11T19:10:00.000Z",
        #             "utc_departure": "2023-02-11T13:40:00.000Z"
        #         },
        #         {
        #             "id": "071110db4bc8000069733ce3_0|071110db4bc8000069733ce3_1|10db0a7c4bc80000a1fe52aa_0",
        #             "flyFrom": "DEL",
        #             "flyTo": "ORY",
        #             "cityFrom": "New Delhi",
        #             "cityCodeFrom": "DEL",
        #             "cityTo": "Paris",
        #             "cityCodeTo": "PAR",
        #             "countryFrom": {
        #                 "code": "IN",
        #                 "name": "India"
        #             },
        #             "countryTo": {
        #                 "code": "FR",
        #                 "name": "France"
        #             },
        #             "nightsInDest": 'null',
        #             "quality": 521.666235,
        #             "distance": 6590.14,
        #             "duration": {
        #                 "departure": 72300,
        #                 "return": 0,
        #                 "total": 72300
        #             },
        #             "price": 349,
        #             "conversion": {
        #                 "EUR": 349
        #             },
        #             "fare": {
        #                 "adults": 349,
        #                 "children": 349,
        #                 "infants": 349
        #             },
        #             "bags_price": {
        #                 "1": 95.2
        #             },
        #             "baglimit": {
        #                 "hand_height": 35,
        #                 "hand_length": 55,
        #                 "hand_weight": 7,
        #                 "hand_width": 23,
        #                 "hold_dimensions_sum": 158,
        #                 "hold_height": 50,
        #                 "hold_length": 75,
        #                 "hold_weight": 15,
        #                 "hold_width": 33
        #             },
        #             "availability": {
        #                 "seats": 6
        #             },
        #             "airlines": [
        #                 "TO",
        #                 "XY"
        #             ],
        #             "route": [
        #                 {
        #                     "id": "071110db4bc8000069733ce3_0",
        #                     "combination_id": "071110db4bc8000069733ce3",
        #                     "flyFrom": "DEL",
        #                     "flyTo": "RUH",
        #                     "cityFrom": "New Delhi",
        #                     "cityCodeFrom": "DEL",
        #                     "cityTo": "Riyadh",
        #                     "cityCodeTo": "RUH",
        #                     "airline": "XY",
        #                     "flight_no": 330,
        #                     "operating_carrier": "XY",
        #                     "operating_flight_no": "330",
        #                     "fare_basis": "DCI2I",
        #                     "fare_category": "M",
        #                     "fare_classes": "D",
        #                     "fare_family": "",
        #                     "return": 0,
        #                     "bags_recheck_required": False,
        #                     "vi_connection": False,
        #                     "guarantee": False,
        #                     "equipment": 'null',
        #                     "vehicle_type": "aircraft",
        #                     "local_arrival": "2023-02-12T07:30:00.000Z",
        #                     "utc_arrival": "2023-02-12T04:30:00.000Z",
        #                     "local_departure": "2023-02-12T04:10:00.000Z",
        #                     "utc_departure": "2023-02-11T22:40:00.000Z"
        #                 },
        #                 {
        #                     "id": "071110db4bc8000069733ce3_1",
        #                     "combination_id": "071110db4bc8000069733ce3",
        #                     "flyFrom": "RUH",
        #                     "flyTo": "AMM",
        #                     "cityFrom": "Riyadh",
        #                     "cityCodeFrom": "RUH",
        #                     "cityTo": "Amman",
        #                     "cityCodeTo": "AMM",
        #                     "airline": "XY",
        #                     "flight_no": 251,
        #                     "operating_carrier": "XY",
        #                     "operating_flight_no": "251",
        #                     "fare_basis": "ACI2I",
        #                     "fare_category": "M",
        #                     "fare_classes": "A",
        #                     "fare_family": "",
        #                     "return": 0,
        #                     "bags_recheck_required": False,
        #                     "vi_connection": False,
        #                     "guarantee": False,
        #                     "equipment": 'null',
        #                     "vehicle_type": "aircraft",
        #                     "local_arrival": "2023-02-12T12:25:00.000Z",
        #                     "utc_arrival": "2023-02-12T09:25:00.000Z",
        #                     "local_departure": "2023-02-12T09:45:00.000Z",
        #                     "utc_departure": "2023-02-12T06:45:00.000Z"
        #                 },
        #                 {
        #                     "id": "10db0a7c4bc80000a1fe52aa_0",
        #                     "combination_id": "10db0a7c4bc80000a1fe52aa",
        #                     "flyFrom": "AMM",
        #                     "flyTo": "ORY",
        #                     "cityFrom": "Amman",
        #                     "cityCodeFrom": "AMM",
        #                     "cityTo": "Paris",
        #                     "cityCodeTo": "PAR",
        #                     "airline": "TO",
        #                     "flight_no": 8051,
        #                     "operating_carrier": "TO",
        #                     "operating_flight_no": "8051",
        #                     "fare_basis": "NBATO",
        #                     "fare_category": "M",
        #                     "fare_classes": "N",
        #                     "fare_family": "",
        #                     "return": 0,
        #                     "bags_recheck_required": True,
        #                     "vi_connection": True,
        #                     "guarantee": True,
        #                     "equipment": 'null',
        #                     "vehicle_type": "aircraft",
        #                     "local_arrival": "2023-02-12T19:45:00.000Z",
        #                     "utc_arrival": "2023-02-12T18:45:00.000Z",
        #                     "local_departure": "2023-02-12T16:30:00.000Z",
        #                     "utc_departure": "2023-02-12T13:30:00.000Z"
        #                 }
        #             ],
        #             "booking_token": "ExkD8bK-8WURjCaaNNlgQjq4WHeU8x1wd80skYl9smextsg39ZXrCQDNi1wzM5zBVlbeORjPM_hDLsVHfhy0xdJykLTDiFECyNhu15xFJsVWzQBGtH2L3tJeoWXGSauW9F3VpauUeZt-PIx52uKhmnMDVDFhv5nMQnzLm1MLbmC8HIAR5sg07HUANly9AHHkRSVbfV9iC6bh3nVtH_a9BG3c6gVtZ6_z05TbiV9EcNqnDhroy70a3h_hO8c_-vwspLchY3a3O1AsvRogkXoirwUjLLlXmpYw8HpXJjVCTogN9yOXDB-gHsD-iQX0h8naqRhy-fvTiXDEoVxPN5lKCwgghhzRWpj-MR1EtU821IYULvck7su-wxQNoMMtg1ndYiIyI_jM519Kvg9fErAX_3-UV82fGJbqGJ9FYwN8FNZcz9jEpm-2M2AjmUuvDGLTWuZzDEZOIaoax_ypH-cK6PgsRQBtWRuPbP-mJBr79jsRaEln62-K6IXmqtMmil8yGBcg-LGdVjAfXv9fq6nGsybmDyvjjpxYSg6-CyPgqqyTwOEOxkG0NN8qQe5FBbusHKcR72OC03wNQh0qahQ0_oXpERxsd1PvEMuPY6HNBmUYPLFTZJ2nKCC7N9htHnKIJ24exmW1stzwhWJuWwyZwJy6VsKPYQQ5YucCOzl9qkzs=",
        #             "deep_link": "https://www.kiwi.com/deep?affilid=apoorvflightsearch&currency=EUR&flightsId=071110db4bc8000069733ce3_0%7C071110db4bc8000069733ce3_1%7C10db0a7c4bc80000a1fe52aa_0&from=DEL&lang=en&passengers=1&to=ORY&booking_token=EprHeyTWYIcI_LxEJ4D9elS66L7x_ClazyPuf5s2aSIzjtdOSvFmJcneOG63Gs_WyzOM5Kecd0MZ4SaRU5vgaph4nPu1-_l8vBgwY7NQq-7etzFoC1hnJdy33w_vgE-yv6U6Lcr9QyivywdRgQtcibmkF0-7EUIWf9CQ1hqc0x1qP4Wu50oTMyLHuZGOKrTFxe86GFm9bMMXRZMRTNjWfRXD4Cf8huA5jkjYQ28zo84PRU_qUh4YcLkPhVem_WSYhe603Evr88ltDBoQLSMtQ4cvqMDc7-QXShZ9XRuXn7wEYjfbmLjgU8xS63Kp2Zd_x5_mLk0yFhYxf8yN7cA-OOuhKDfx-2mEtHD6mGEkTC08E2wwCv6iMh4SyjHWCTHACESZYTfyl2qUd-XnwzyY6CtDFnxabX6YkiOt1XRf9pwu6EpgYPLMl3Ac2WWZ31bS1dBy665yFYtc9Tdz3IYx3VCDSZx23_TEUEoG_kFMXr4zIZwRhD7VQjWCMsNMgPst7O83_0pKxf7A9hXHJaOdE4ykO6-Gp6oja912HOEfnmaY1acqqrAgH98Kb2mLg7EY5",
        #             "facilitated_booking_available": True,
        #             "pnr_count": 2,
        #             "has_airport_change": False,
        #             "technical_stops": 0,
        #             "throw_away_ticketing": False,
        #             "hidden_city_ticketing": False,
        #             "virtual_interlining": True,
        #             "local_arrival": "2023-02-12T19:45:00.000Z",
        #             "utc_arrival": "2023-02-12T18:45:00.000Z",
        #             "local_departure": "2023-02-12T04:10:00.000Z",
        #             "utc_departure": "2023-02-11T22:40:00.000Z"
        #         },
        #         {
        #             "id": "071125c34bc800001df1ebf0_0",
        #             "flyFrom": "DEL",
        #             "flyTo": "CDG",
        #             "cityFrom": "New Delhi",
        #             "cityCodeFrom": "DEL",
        #             "cityTo": "Paris",
        #             "cityCodeTo": "PAR",
        #             "countryFrom": {
        #                 "code": "IN",
        #                 "name": "India"
        #             },
        #             "countryTo": {
        #                 "code": "FR",
        #                 "name": "France"
        #             },
        #             "nightsInDest": 'null',
        #             "quality": 476.66645,
        #             "distance": 6572.81,
        #             "duration": {
        #                 "departure": 33600,
        #                 "return": 0,
        #                 "total": 33600
        #             },
        #             "price": 390,
        #             "conversion": {
        #                 "EUR": 390
        #             },
        #             "fare": {
        #                 "adults": 390,
        #                 "children": 390,
        #                 "infants": 390
        #             },
        #             "bags_price": {
        #                 "1": 0,
        #                 "2": 0
        #             },
        #             "baglimit": {
        #                 "hand_height": 35,
        #                 "hand_length": 55,
        #                 "hand_weight": 8,
        #                 "hand_width": 25,
        #                 "hold_dimensions_sum": 158,
        #                 "hold_height": 52,
        #                 "hold_length": 78,
        #                 "hold_weight": 23,
        #                 "hold_width": 28,
        #                 "personal_item_height": 20,
        #                 "personal_item_length": 40,
        #                 "personal_item_weight": 5,
        #                 "personal_item_width": 10
        #             },
        #             "availability": {
        #                 "seats": 1
        #             },
        #             "airlines": [
        #                 "AI"
        #             ],
        #             "route": [
        #                 {
        #                     "id": "071125c34bc800001df1ebf0_0",
        #                     "combination_id": "071125c34bc800001df1ebf0",
        #                     "flyFrom": "DEL",
        #                     "flyTo": "CDG",
        #                     "cityFrom": "New Delhi",
        #                     "cityCodeFrom": "DEL",
        #                     "cityTo": "Paris",
        #                     "cityCodeTo": "PAR",
        #                     "airline": "AI",
        #                     "flight_no": 143,
        #                     "operating_carrier": "AI",
        #                     "operating_flight_no": "143",
        #                     "fare_basis": "ULOWCDG",
        #                     "fare_category": "M",
        #                     "fare_classes": "U",
        #                     "fare_family": "",
        #                     "return": 0,
        #                     "bags_recheck_required": False,
        #                     "vi_connection": False,
        #                     "guarantee": False,
        #                     "equipment": 'null',
        #                     "vehicle_type": "aircraft",
        #                     "local_arrival": "2023-02-12T17:55:00.000Z",
        #                     "utc_arrival": "2023-02-12T16:55:00.000Z",
        #                     "local_departure": "2023-02-12T13:05:00.000Z",
        #                     "utc_departure": "2023-02-12T07:35:00.000Z"
        #                 }
        #             ],
        #             "booking_token": "EncjoHb8qVb7Xlb8cs3pzKjFYYlvQ5IYLTrTyBWysAipdqia4QpHUW9HCOaxZDNqpaXmBqYwJj6I0RmRw-GEO1UIfJC7jTQZHoKT6xkrdSyh5d7CaHL97HSzbZT4dA0uDiEIOXdMAAlXTAYsCnDXBiwAyOtmdXtLRNMHcdYyPwym3Uyepzdu2sYGTdWBJ4kflIoqXKcffowONBmwfmBX-fLiFaJXpXefX8Jl3vjss526WlzssG9RoBO462CECQw1Q6LPrdc6UTyggzqKroYk6E17l8Q0oh5ddBYo2xVYnnoVZQuKTIMfX5RACen7Iu6ezdQSQ9rluSTgyOvGK5rBayvmKSWTLpsrtnLPInprrtkzNs2zqZzALDy7wLlVSLrWJ6kyjvvzZ39uRwpHCKlCKhCeV8Ix8-dPUT4yYkbB4-OdlX9bOIWDfD2RzJkVNbG2PIZ8xpAllzKCbHeX2IBRL72EXR63IwYELm63kfV0AbRJWO0Syh_gI8W9oSH5qdXRl1TMUmkeaVqsgOWIcfsR8XmQ1ZRXWqJso-aNbMXuIXpv3v73tHVZwkUFLgwa01B0M0FzDgxnZTh-ClOZID7tYEKf7FC2OYGvOjSdcAIj9__Y=",
        #             "deep_link": "https://www.kiwi.com/deep?affilid=apoorvflightsearch&currency=EUR&flightsId=071125c34bc800001df1ebf0_0&from=DEL&lang=en&passengers=1&to=CDG&booking_token=EQhuMcrpfztIafs2lfoOxXqGJ6YuWltZZei_oampvnfjHN9HmYI8lPA7Q13C6r7xsn43NE8H652OUX51x8IiDaoiRpoTbbnTELABeAt4ZDwis_9e7ldUuU9rrGinMEwnAib8FNT_VszbWSKbI-gC9UyUl6YQf7FIre3lE-La_V6hGKk99168HI0edUf-UD8my-OcwLtjgb_3hUpQ3CX3zmG0p9awTVOBGVOzmyckyQh9a23Mqha9iRhs_PrfYL0nutMVXHa_49Z_4wfoLSMFRX7NktMth5tkhj0f_B5GpN-X7xK10MTOk_XeC76SzeR_YfqU-e_FAyB3ePPi2LcDSJup0jQYaECBPLx4SoJfj5rFx6MV4KOGWgfNctg8-amTjZ_qWRW-xAGwGWFUeTFvYt7UC1y_8lJZQHS2Axa7R-81Lnd4ZFMuhgVro4FP4HO3-RRfeagpUAGozwLkvZgU1ug==",
        #             "facilitated_booking_available": True,
        #             "pnr_count": 1,
        #             "has_airport_change": False,
        #             "technical_stops": 0,
        #             "throw_away_ticketing": False,
        #             "hidden_city_ticketing": False,
        #             "virtual_interlining": False,
        #             "local_arrival": "2023-02-12T17:55:00.000Z",
        #             "utc_arrival": "2023-02-12T16:55:00.000Z",
        #             "local_departure": "2023-02-12T13:05:00.000Z",
        #             "utc_departure": "2023-02-12T07:35:00.000Z"
        #         },
        #         {
        #             "id": "071125c34bc70000c195b920_0",
        #             "flyFrom": "DEL",
        #             "flyTo": "CDG",
        #             "cityFrom": "New Delhi",
        #             "cityCodeFrom": "DEL",
        #             "cityTo": "Paris",
        #             "cityCodeTo": "PAR",
        #             "countryFrom": {
        #                 "code": "IN",
        #                 "name": "India"
        #             },
        #             "countryTo": {
        #                 "code": "FR",
        #                 "name": "France"
        #             },
        #             "nightsInDest": 'null',
        #             "quality": 479.333115,
        #             "distance": 6572.81,
        #             "duration": {
        #                 "departure": 33900,
        #                 "return": 0,
        #                 "total": 33900
        #             },
        #             "price": 392,
        #             "conversion": {
        #                 "EUR": 392
        #             },
        #             "fare": {
        #                 "adults": 392,
        #                 "children": 392,
        #                 "infants": 392
        #             },
        #             "bags_price": {
        #                 "1": 0,
        #                 "2": 0
        #             },
        #             "baglimit": {
        #                 "hand_height": 40,
        #                 "hand_length": 55,
        #                 "hand_weight": 7,
        #                 "hand_width": 20,
        #                 "hold_dimensions_sum": 158,
        #                 "hold_height": 52,
        #                 "hold_length": 78,
        #                 "hold_weight": 23,
        #                 "hold_width": 28,
        #                 "personal_item_height": 30,
        #                 "personal_item_length": 40,
        #                 "personal_item_weight": 3,
        #                 "personal_item_width": 15
        #             },
        #             "availability": {
        #                 "seats": 'null'
        #             },
        #             "airlines": [
        #                 "UK"
        #             ],
        #             "route": [
        #                 {
        #                     "id": "071125c34bc70000c195b920_0",
        #                     "combination_id": "071125c34bc70000c195b920",
        #                     "flyFrom": "DEL",
        #                     "flyTo": "CDG",
        #                     "cityFrom": "New Delhi",
        #                     "cityCodeFrom": "DEL",
        #                     "cityTo": "Paris",
        #                     "cityCodeTo": "PAR",
        #                     "airline": "UK",
        #                     "flight_no": 21,
        #                     "operating_carrier": "UK",
        #                     "operating_flight_no": "21",
        #                     "fare_basis": "Q0NINYV",
        #                     "fare_category": "M",
        #                     "fare_classes": "Q",
        #                     "fare_family": "",
        #                     "return": 0,
        #                     "bags_recheck_required": False,
        #                     "vi_connection": False,
        #                     "guarantee": False,
        #                     "equipment": 'null',
        #                     "vehicle_type": "aircraft",
        #                     "local_arrival": "2023-02-11T18:40:00.000Z",
        #                     "utc_arrival": "2023-02-11T17:40:00.000Z",
        #                     "local_departure": "2023-02-11T13:45:00.000Z",
        #                     "utc_departure": "2023-02-11T08:15:00.000Z"
        #                 }
        #             ],
        #             "booking_token": "EGpiDu0CkVXVYU7qCslFtjuivabqD46xoZQcTxQ-SWnAaMSaFowEDwjfatyxxRqocNXJMgQCs0572wM_IqnyF1kSSWM06cGDqUxpqVS_BIj9JQf-zZd5Fhl-zfgr6xx7RAzXipPF33R0u8HlOFPVcMMQyODKmUD6qovdjmo45_gYaadI_RNqiE123pwdRLjH6Tbt_TOOHNY0Ni_2bS3fL13eeghBIzo-mcIGs3fPFH0r7iwinBpErXKWfNTidLhQzgCjteS250gToPE5ypG7q57ALoXRQgZUgOzA4yujx-8s9GsQSGZTK923fT9nCaCyV4vZ9VY8jzDZSG51yrR-iqULFy9v7p4_VbeXqg-Uerk1RBZQBarrUHEFkqSJN5o3eO9gzZ-KG1PymISTEf7CSuTbBkWU-_XFtlMazG8Wuj0bEkJU2u0HRYYPWTaAIyyo_VbU-xr5-jlz5QoIgYt3G0_aHfERZgoyou5C7uAoZ_l-1mvWPIowwvGlQ1XN0-1lNo9X7PQM6nRoQLd1igL0azwN-e3ftc9PlK2T8CxqX8Vo6wPDa8fTjSgEVce5GwL5yqnTWI814CX1SZWCIeZdniGOomCqVZthjVa21cVNE5kY=",
        #             "deep_link": "https://www.kiwi.com/deep?affilid=apoorvflightsearch&currency=EUR&flightsId=071125c34bc70000c195b920_0&from=DEL&lang=en&passengers=1&to=CDG&booking_token=ES0-eYcLN3Z9FbJSNpeiXRDNaDsLsttLaxDFExv5lMczFvg5tTbOmM7dzssLPFQPXqTzffAfoHVzArwYZdNymc1lxbIwJBudVXn-De5ImQYlTkyI-6hWV6PV3nZMn_B2bdmfoeuyuAzLpruzmGnF6mXnpKRhsPTF-ybpRvgPEUj3gckV4xb8oeSlzxj83tR9AR0w6VmMuPLpe2q65e3PZkFUWSFx3_ouypWapd97zNFsmpt9eEGf2SqK7i86NCbX2MJLmV9waR_wIHC_DmqNc9LmM61gTNi7P0N9pew-GOirlYM7Sp4mCgFQuA1uC6PaG65190YHdww6p_s5ng1RJlMTvlXl5lY4iszEq3jRpAJz8keujO0TW0aPOmPLXjtwNNe9HHm9AF7NwPfuEQb1984Km0YCzZS5HwFvfaUBGmE_d7UwNWNYoyOniwb7E0LUxtbJ3zmMV4vn4sDPWzLJlYQSg8KQNn8EHOa3SVeax8qU=",
        #             "facilitated_booking_available": True,
        #             "pnr_count": 1,
        #             "has_airport_change": False,
        #             "technical_stops": 0,
        #             "throw_away_ticketing": False,
        #             "hidden_city_ticketing": False,
        #             "virtual_interlining": False,
        #             "local_arrival": "2023-02-11T18:40:00.000Z",
        #             "utc_arrival": "2023-02-11T17:40:00.000Z",
        #             "local_departure": "2023-02-11T13:45:00.000Z",
        #             "utc_departure": "2023-02-11T08:15:00.000Z"
        #         },
        #         {
        #             "id": "071125c34bc80000fdf5547d_0",
        #             "flyFrom": "DEL",
        #             "flyTo": "CDG",
        #             "cityFrom": "New Delhi",
        #             "cityCodeFrom": "DEL",
        #             "cityTo": "Paris",
        #             "cityCodeTo": "PAR",
        #             "countryFrom": {
        #                 "code": "IN",
        #                 "name": "India"
        #             },
        #             "countryTo": {
        #                 "code": "FR",
        #                 "name": "France"
        #             },
        #             "nightsInDest": 'null',
        #             "quality": 479.333115,
        #             "distance": 6572.81,
        #             "duration": {
        #                 "departure": 33900,
        #                 "return": 0,
        #                 "total": 33900
        #             },
        #             "price": 392,
        #             "conversion": {
        #                 "EUR": 392
        #             },
        #             "fare": {
        #                 "adults": 392,
        #                 "children": 392,
        #                 "infants": 392
        #             },
        #             "bags_price": {
        #                 "1": 0,
        #                 "2": 0
        #             },
        #             "baglimit": {
        #                 "hand_height": 40,
        #                 "hand_length": 55,
        #                 "hand_weight": 7,
        #                 "hand_width": 20,
        #                 "hold_dimensions_sum": 158,
        #                 "hold_height": 52,
        #                 "hold_length": 78,
        #                 "hold_weight": 23,
        #                 "hold_width": 28,
        #                 "personal_item_height": 30,
        #                 "personal_item_length": 40,
        #                 "personal_item_weight": 3,
        #                 "personal_item_width": 15
        #             },
        #             "availability": {
        #                 "seats": 5
        #             },
        #             "airlines": [
        #                 "UK"
        #             ],
        #             "route": [
        #                 {
        #                     "id": "071125c34bc80000fdf5547d_0",
        #                     "combination_id": "071125c34bc80000fdf5547d",
        #                     "flyFrom": "DEL",
        #                     "flyTo": "CDG",
        #                     "cityFrom": "New Delhi",
        #                     "cityCodeFrom": "DEL",
        #                     "cityTo": "Paris",
        #                     "cityCodeTo": "PAR",
        #                     "airline": "UK",
        #                     "flight_no": 21,
        #                     "operating_carrier": "UK",
        #                     "operating_flight_no": "21",
        #                     "fare_basis": "Q0NINYV",
        #                     "fare_category": "M",
        #                     "fare_classes": "Q",
        #                     "fare_family": "",
        #                     "return": 0,
        #                     "bags_recheck_required": False,
        #                     "vi_connection": False,
        #                     "guarantee": False,
        #                     "equipment": 'null',
        #                     "vehicle_type": "aircraft",
        #                     "local_arrival": "2023-02-12T18:40:00.000Z",
        #                     "utc_arrival": "2023-02-12T17:40:00.000Z",
        #                     "local_departure": "2023-02-12T13:45:00.000Z",
        #                     "utc_departure": "2023-02-12T08:15:00.000Z"
        #                 }
        #             ],
        #             "booking_token": "Eq2uzp75TS20hQKu3XcDg76RoG70qBguPynfp5pSX4USIUjrZ3cP1zFfincrtYl58uF_EtjmBF1WlZvYEtlwB0QtBiQeCvPfhrDb1mdy9ph3KNUKvF-GfhKR1_uoPLIJ6Gu9DUjaEPFcBS0o2R2XGQJtIITY4QSZBoPIn0g_8qUfI1RXtSW9AWfYHyaiQMak1EiIku98m9HouacTsfGuagAELPcMma-7NSPIdQsnDxewxjkSA-IS9k6v-uUP6sFSJTsea8HGpN8VADC1f4J6vehRazINtSXplWrVu9M9tIKBeMdFf6BL4BQw8ImVvWqZLW9Y-LlUcpJMnJaptK9PyJq_IQTY1P7bCnnlIPpMV9RX2Og7FPtd_Y3ImVTWGTVETDR_KoxTZg7vyqRhE8RXugqkAB687U5_v3-Fml1GQAl86BKtxxSoHPTJKfwDbN6LRQrw-uX1YJCq9Hb8hptgqK61XCoAh4zO_2_U3ivz5gozyXWh51F9hQVnmF9S41UfdniWfVuK8blZZD7kySj0qV8e4H74B4Yvb5FxKyXrwYc_55wwxM6bNmDXhgNPCZSxF97_PiJ5Ue1206gsiNAZJfS5bjJFn-WNtKhdfDUBJrpE=",
        #             "deep_link": "https://www.kiwi.com/deep?affilid=apoorvflightsearch&currency=EUR&flightsId=071125c34bc80000fdf5547d_0&from=DEL&lang=en&passengers=1&to=CDG&booking_token=EyHFF_vSzTuhXz6GaOI0L4qN5p2q0rH-1EiPdUWJziWkWi4afwFz6HuUUfnvT0YaIuYr54_R0feRVeLJCsdK5ph_jWSRXUbGSr5K-fIvAPo2fvWkl3aSGj908i2JfLWH-y61Uw6VsbKqYXaD3yfXf2xtqvigoVeQlBe0YhMr2dGxbrRYVhuwO2wVWcx1xW8hpNiehFDMkJtEQ9acLLEpZlvPfSFJGAW7NKdpRo56FKvLR7DoLJkXRpcUl8RQBtfL_mClwK_fYJwj8BCHRwCXE_c_fpVq5iC36VZ9a8rfMzx5-2IDRbVQe0b6SUbEsB6lY450yn4kZ7MgVlvzOOHMgjgc3P0Ycowc8AmrUw4of1rr7XG7zqzPcYhZnY5bfdcw8xNOpWv6x8G9UrIcdBFHCKQTXHiNyIHQ_evEwBiGPNcWmwUwjHS_j9aJTAGqm0ZwPcRJv7vpA6V0twslMUsH8xBbUGp_DA9TzlnZMTQyy8B4=",
        #             "facilitated_booking_available": True,
        #             "pnr_count": 1,
        #             "has_airport_change": False,
        #             "technical_stops": 0,
        #             "throw_away_ticketing": False,
        #             "hidden_city_ticketing": False,
        #             "virtual_interlining": False,
        #             "local_arrival": "2023-02-12T18:40:00.000Z",
        #             "utc_arrival": "2023-02-12T17:40:00.000Z",
        #             "local_departure": "2023-02-12T13:45:00.000Z",
        #             "utc_departure": "2023-02-12T08:15:00.000Z"
        #         },
        #         {
        #             "id": "071125c34bca000022593798_0",
        #             "flyFrom": "DEL",
        #             "flyTo": "CDG",
        #             "cityFrom": "New Delhi",
        #             "cityCodeFrom": "DEL",
        #             "cityTo": "Paris",
        #             "cityCodeTo": "PAR",
        #             "countryFrom": {
        #                 "code": "IN",
        #                 "name": "India"
        #             },
        #             "countryTo": {
        #                 "code": "FR",
        #                 "name": "France"
        #             },
        #             "nightsInDest": 'null',
        #             "quality": 491.66645,
        #             "distance": 6572.81,
        #             "duration": {
        #                 "departure": 33600,
        #                 "return": 0,
        #                 "total": 33600
        #             },
        #             "price": 405,
        #             "conversion": {
        #                 "EUR": 405
        #             },
        #             "fare": {
        #                 "adults": 405,
        #                 "children": 405,
        #                 "infants": 405
        #             },
        #             "bags_price": {
        #                 "1": 0,
        #                 "2": 0
        #             },
        #             "baglimit": {
        #                 "hand_height": 35,
        #                 "hand_length": 55,
        #                 "hand_weight": 8,
        #                 "hand_width": 25,
        #                 "hold_dimensions_sum": 158,
        #                 "hold_height": 52,
        #                 "hold_length": 78,
        #                 "hold_weight": 23,
        #                 "hold_width": 28,
        #                 "personal_item_height": 20,
        #                 "personal_item_length": 40,
        #                 "personal_item_weight": 5,
        #                 "personal_item_width": 10
        #             },
        #             "availability": {
        #                 "seats": 1
        #             },
        #             "airlines": [
        #                 "AI"
        #             ],
        #             "route": [
        #                 {
        #                     "id": "071125c34bca000022593798_0",
        #                     "combination_id": "071125c34bca000022593798",
        #                     "flyFrom": "DEL",
        #                     "flyTo": "CDG",
        #                     "cityFrom": "New Delhi",
        #                     "cityCodeFrom": "DEL",
        #                     "cityTo": "Paris",
        #                     "cityCodeTo": "PAR",
        #                     "airline": "AI",
        #                     "flight_no": 143,
        #                     "operating_carrier": "AI",
        #                     "operating_flight_no": "143",
        #                     "fare_basis": "ULOWCDG",
        #                     "fare_category": "M",
        #                     "fare_classes": "U",
        #                     "fare_family": "",
        #                     "return": 0,
        #                     "bags_recheck_required": False,
        #                     "vi_connection": False,
        #                     "guarantee": False,
        #                     "equipment": 'null',
        #                     "vehicle_type": "aircraft",
        #                     "local_arrival": "2023-02-14T17:55:00.000Z",
        #                     "utc_arrival": "2023-02-14T16:55:00.000Z",
        #                     "local_departure": "2023-02-14T13:05:00.000Z",
        #                     "utc_departure": "2023-02-14T07:35:00.000Z"
        #                 }
        #             ],
        #             "booking_token": "EIIyudV5WmeWiWyZyHX4K9EjB4vSjKaS5GcOBM0NHR7qoDElf4T9vYGyBryn_WfnVgFqFXb8X3D6y8rrVvii3T4_mU8YXh4ekiBuI6pDh5C21KZKKstXhJNwTsfLRZA27gBTguW6hHQlytgG5Pkfs30PjaXMmKPoesH-uRHUid5LlVsKHG-zuZPxVSZ_TcKmkVcSbIbRbDEBXZwMALgj9q2YTnCJsEAG_TB6LmoMq_ZvElC5JVjARz1552lspC5ut3rnM_w_gg4vN0VYGpZdhnJ0ZBC5j-Ok2S7mXWgviVuYonTRBF41mBYeLS6luaGIWNoqFE1mXMmkZVziuSmbXwXsdMQWMYHQfSt8ZskZ8PFaVur3Xt0awuRoptA00UQ7zmB3blGvWAfkAbVc02eIThMIbJUqL38lt5qGCuDmc7wABPvbR-7jWmi3zUQzAIR3H76sPn05f3gZLREITu3E95IK9RwIwjnM1PGhEWbwg9l8lSaJGcgwQiacyBI9PrSMnPkFrSWP-EiCre3zVz7K63HWnH7lPLoqlRqr0Q7A52bX_D_A4a9jD10C7A4GzNNH5p8D9PjPved7jD8mkjyOpfuJrZHSDrsLWvVd82gJa2Dk=",
        #             "deep_link": "https://www.kiwi.com/deep?affilid=apoorvflightsearch&currency=EUR&flightsId=071125c34bca000022593798_0&from=DEL&lang=en&passengers=1&to=CDG&booking_token=EKgri-bdO_CrI8VT_IMv9BC0UNy4BugD7rslUeXK_Fno4w8E9EDeTyOUWid8BsU9k8Xcts4cL6-G_bI9RmHa3veMD93so_D-SOs7mXjIibATJRYzLad88lgc4MJ560cCe4Pyu9wyPYuBa1Tg1ZF_SLN5DZRgfsoSZEFiPoNOL0_1Bo8Nnd_vImgpeXs241E4vDP2q44iGJGE7LL4DVId0-yOP0S8PgSDe61PApmiXBZTJ80DYarDhwstAU9Aw_x_FhotXOD1wYaMnY4rqwZN6wCYz8hyhwA11jKmu_FWzmFw5fYeob3zL22AoeEsP_XuKHG3z6hGjFdtegQfj-2naFr6rSB9zdCHkp7v6AOpXKJQiNNPBSMRXj3dDrA3SlkIQ458zQTeLIZD9RV7HmutZzy35I8kgLeE2nbEKE1gQbODxwviflxGRCycsNFVJi8lfmgMg0448kk_t93Y2XjGTTA==",
        #             "facilitated_booking_available": True,
        #             "pnr_count": 1,
        #             "has_airport_change": False,
        #             "technical_stops": 0,
        #             "throw_away_ticketing": False,
        #             "hidden_city_ticketing": False,
        #             "virtual_interlining": False,
        #             "local_arrival": "2023-02-14T17:55:00.000Z",
        #             "utc_arrival": "2023-02-14T16:55:00.000Z",
        #             "local_departure": "2023-02-14T13:05:00.000Z",
        #             "utc_departure": "2023-02-14T07:35:00.000Z"
        #         },
        #         {
        #             "id": "071125c34bcb000065f7fcf3_0",
        #             "flyFrom": "DEL",
        #             "flyTo": "CDG",
        #             "cityFrom": "New Delhi",
        #             "cityCodeFrom": "DEL",
        #             "cityTo": "Paris",
        #             "cityCodeTo": "PAR",
        #             "countryFrom": {
        #                 "code": "IN",
        #                 "name": "India"
        #             },
        #             "countryTo": {
        #                 "code": "FR",
        #                 "name": "France"
        #             },
        #             "nightsInDest": 'null',
        #             "quality": 494.333115,
        #             "distance": 6572.81,
        #             "duration": {
        #                 "departure": 33900,
        #                 "return": 0,
        #                 "total": 33900
        #             },
        #             "price": 407,
        #             "conversion": {
        #                 "EUR": 407
        #             },
        #             "fare": {
        #                 "adults": 407,
        #                 "children": 407,
        #                 "infants": 407
        #             },
        #             "bags_price": {
        #                 "1": 0,
        #                 "2": 0
        #             },
        #             "baglimit": {
        #                 "hand_height": 40,
        #                 "hand_length": 55,
        #                 "hand_weight": 7,
        #                 "hand_width": 20,
        #                 "hold_dimensions_sum": 158,
        #                 "hold_height": 52,
        #                 "hold_length": 78,
        #                 "hold_weight": 23,
        #                 "hold_width": 28,
        #                 "personal_item_height": 30,
        #                 "personal_item_length": 40,
        #                 "personal_item_weight": 3,
        #                 "personal_item_width": 15
        #             },
        #             "availability": {
        #                 "seats": 1
        #             },
        #             "airlines": [
        #                 "UK"
        #             ],
        #             "route": [
        #                 {
        #                     "id": "071125c34bcb000065f7fcf3_0",
        #                     "combination_id": "071125c34bcb000065f7fcf3",
        #                     "flyFrom": "DEL",
        #                     "flyTo": "CDG",
        #                     "cityFrom": "New Delhi",
        #                     "cityCodeFrom": "DEL",
        #                     "cityTo": "Paris",
        #                     "cityCodeTo": "PAR",
        #                     "airline": "UK",
        #                     "flight_no": 21,
        #                     "operating_carrier": "UK",
        #                     "operating_flight_no": "21",
        #                     "fare_basis": "Q0NINYV",
        #                     "fare_category": "M",
        #                     "fare_classes": "Q",
        #                     "fare_family": "",
        #                     "return": 0,
        #                     "bags_recheck_required": False,
        #                     "vi_connection": False,
        #                     "guarantee": False,
        #                     "equipment": 'null',
        #                     "vehicle_type": "aircraft",
        #                     "local_arrival": "2023-02-15T18:40:00.000Z",
        #                     "utc_arrival": "2023-02-15T17:40:00.000Z",
        #                     "local_departure": "2023-02-15T13:45:00.000Z",
        #                     "utc_departure": "2023-02-15T08:15:00.000Z"
        #                 }
        #             ],
        #             "booking_token": "EfOaTYG10XFy_rkh7w-IonNXxf_yOrX1k4ohAgaaEv8pQJY-LyPcT6toPa_y4-6rNu2FihpxXZC1mniDYGA63F79YNkMia5zvMMByBoO_L52cr3gDrvr4irf1VdayTBBOelq_j-GvH--Nxe98-R3RNSz6T3zBZkCVPclTlMjU-aMsFM8Qu1p8Qy7lHztc_iE2heeFuREk25rdfJV8nFV1AQz5fHte9C3SadQFaNYqDwrS6rveFV6RoRTqpE4T-PHnS7BVqV17X7y7tRkhMmoOJ9ecjLTxPW5bZXK_qPJZ7j1rrg-8ikapcEtaMDVLqG2jXBgcp-IbW464G5uBld4LnG0NrYT60ILSxqSAVJZB8MDeeS42u0bP5rITO8qdwY0CelGalDR8ndcHUoA_Bz2i8Pdyn8Bxd3zDDapL9isc4Ry_Y65QNf6Ki2i7S1YYHfJ_7c5LvqAtD1vw70iGzwxwXerBhPLAtxV25Wv4sa8WoSgKU7dgefhmMDRBBLPI58v_-u8Q8cRahO-yEOe3x4QjPa6a4Ai9U2cfc073BjSqGWh6BoOmlBmoqevGLRJHdqKk",
        #             "deep_link": "https://www.kiwi.com/deep?affilid=apoorvflightsearch&currency=EUR&flightsId=071125c34bcb000065f7fcf3_0&from=DEL&lang=en&passengers=1&to=CDG&booking_token=EfRDtaEEU9KC7-682CuqM1Wn4oy2TzPcNZpl-3gaFH-WMBYepTGyIefV9QHpC3ZV359yJWuSEBMWlURzQjtpRBT3Djez-n7aAGmeU6-SHfga6EdW_zWSQ5yiq4LnFFJ8x1dpbcbbLPrJT8xpYpJ3kZ_-Dyxvjp1W1v9cbbTdenDXGAKfxZdRZDHissDiApgYw3XpT3Wsm3fs0Vjt3zvu98fl0VpXZq4a2vzxGW-pdzgUWhWy0Y6MGZ50RmZyuAAZM1VaWC-XtIXVqzmYgcowQJy-VncxFk1ezMf1h4KhBqrNPw8erFPxi4080L6D4qE4ywtwMeR_GmA6w7I-RPinPG01DsoNpHi0Ven0mnXh8h2sFmzTtOx8WPG-fPZTl778K6GTOliy9yBDjtsiR1_KrK24RkXKSUkGVpk8Ueky7Z7bj6iLsgOPfShXy9Az7bInST6zs9D8GFXBGR4aDSf6bwQ==",
        #             "facilitated_booking_available": True,
        #             "pnr_count": 1,
        #             "has_airport_change": False,
        #             "technical_stops": 0,
        #             "throw_away_ticketing": False,
        #             "hidden_city_ticketing": False,
        #             "virtual_interlining": False,
        #             "local_arrival": "2023-02-15T18:40:00.000Z",
        #             "utc_arrival": "2023-02-15T17:40:00.000Z",
        #             "local_departure": "2023-02-15T13:45:00.000Z",
        #             "utc_departure": "2023-02-15T08:15:00.000Z"
        #         },
        #         {
        #             "id": "071125c34bc900007e1c18e9_0",
        #             "flyFrom": "DEL",
        #             "flyTo": "CDG",
        #             "cityFrom": "New Delhi",
        #             "cityCodeFrom": "DEL",
        #             "cityTo": "Paris",
        #             "cityCodeTo": "PAR",
        #             "countryFrom": {
        #                 "code": "IN",
        #                 "name": "India"
        #             },
        #             "countryTo": {
        #                 "code": "FR",
        #                 "name": "France"
        #             },
        #             "nightsInDest": 'null',
        #             "quality": 494.333115,
        #             "distance": 6572.81,
        #             "duration": {
        #                 "departure": 33900,
        #                 "return": 0,
        #                 "total": 33900
        #             },
        #             "price": 407,
        #             "conversion": {
        #                 "EUR": 407
        #             },
        #             "fare": {
        #                 "adults": 407,
        #                 "children": 407,
        #                 "infants": 407
        #             },
        #             "bags_price": {
        #                 "1": 0,
        #                 "2": 0
        #             },
        #             "baglimit": {
        #                 "hand_height": 40,
        #                 "hand_length": 55,
        #                 "hand_weight": 7,
        #                 "hand_width": 20,
        #                 "hold_dimensions_sum": 158,
        #                 "hold_height": 52,
        #                 "hold_length": 78,
        #                 "hold_weight": 23,
        #                 "hold_width": 28,
        #                 "personal_item_height": 30,
        #                 "personal_item_length": 40,
        #                 "personal_item_weight": 3,
        #                 "personal_item_width": 15
        #             },
        #             "availability": {
        #                 "seats": 'null'
        #             },
        #             "airlines": [
        #                 "UK"
        #             ],
        #             "route": [
        #                 {
        #                     "id": "071125c34bc900007e1c18e9_0",
        #                     "combination_id": "071125c34bc900007e1c18e9",
        #                     "flyFrom": "DEL",
        #                     "flyTo": "CDG",
        #                     "cityFrom": "New Delhi",
        #                     "cityCodeFrom": "DEL",
        #                     "cityTo": "Paris",
        #                     "cityCodeTo": "PAR",
        #                     "airline": "UK",
        #                     "flight_no": 21,
        #                     "operating_carrier": "UK",
        #                     "operating_flight_no": "21",
        #                     "fare_basis": "Q0NINYV",
        #                     "fare_category": "M",
        #                     "fare_classes": "Q",
        #                     "fare_family": "",
        #                     "return": 0,
        #                     "bags_recheck_required": False,
        #                     "vi_connection": False,
        #                     "guarantee": False,
        #                     "equipment": 'null',
        #                     "vehicle_type": "aircraft",
        #                     "local_arrival": "2023-02-13T18:40:00.000Z",
        #                     "utc_arrival": "2023-02-13T17:40:00.000Z",
        #                     "local_departure": "2023-02-13T13:45:00.000Z",
        #                     "utc_departure": "2023-02-13T08:15:00.000Z"
        #                 }
        #             ],
        #             "booking_token": "EnYbB9LZ0TWCYPYeHuToxdOSB988VU_PlTvlTwKkGKouMZ3S1fzuY_VD6d_We7Jj0MzvmG4gnW13Nb06ShTy0cqoS9iRKE31uT6ODK37kLRnPraQ1Qvsrnc9jCFp53BZQF5Xr6xsEcxtI6D4kytbwFize8it8-CyFHakTh5NdQaLrLsFP73kIPADUtLPq6T7laVYbky7513iVvE4DhGW_Eb5CkVhooilXHHXAqLYAsRRv00GkqHmr2GQmfVsFE_u1dIoAifQ2WOz6OYugzKSx6suLXOPXe0hRMG2AK6tOOXMRM_sbCIyL0i2b5eXGv3ntRO_PRfNSQe--fXwNC-QY8XwXV5ypiT_WwblzkJZ0Z0fyUOU_xhLH5663bi8JYJCmidOJaEVVMnKPaGFUvVYsVaieH8jrda3Bb06Qc96DF0IDhW2EKLra8vNst16uzLkqWvgJAJefw99QWS4rBEbq_NHqgml8vrj7P4piLR4hX6dXrQR1uz1tdEPUE89UVKcsa2wkwZlar0OjbRj0f-MnUpa5FMf-KucFbu_bjWk8ih2y4dqU-y7WINR14KUYSLQCao_n-trcmi_4D5nXWh7wO68OsdYMPU_zAGQX59A8ybs=",
        #             "deep_link": "https://www.kiwi.com/deep?affilid=apoorvflightsearch&currency=EUR&flightsId=071125c34bc900007e1c18e9_0&from=DEL&lang=en&passengers=1&to=CDG&booking_token=E447XR9Gf_eXzm8guR7RrP6XAZvnewmWsOu6v-Z7k3LAWFZT1UK9dXE8BzlbqUOED5XjLiynsr-5jpuog7yK9RuiuMzKotRN80_QIIHnuGKwl_bOkCRcODqvgsAjHjfV6l1XN7DIOLXFXYg8s7HTQgWy0OsIVIhC8Oo4bhEufrMH9tjbBV51CHSZ9Xp360l62_4roHgQcHPln1ow8RAGDtKKjKZAqCnHmbphOVl8Vo5YL8a1QIm4YvTDQkoK2QvY4F_sHdGLzxU2VKpkcAw8j2jjDicWpm59jZfoIkV8quTClELsP86d7soWz-VNIPMY0POQLQBemvhFhrsr1NEqZUtH6iwlLsYhXOQuyvhN_y3ovmqnURj1PG2tfjILj8GkScnr8VATyc6mjgDPLOdh-HgDgCZzZwM5iehHz-v-csuLDNRbP8FieG5e-wa4Abt9e2gckLJhKi7xEz-dBYySDEPph4pfS2ZU6r3cOjnxo-H05RA1mGnWkGe4o6DGMQaK6",
        #             "facilitated_booking_available": True,
        #             "pnr_count": 1,
        #             "has_airport_change": False,
        #             "technical_stops": 0,
        #             "throw_away_ticketing": False,
        #             "hidden_city_ticketing": False,
        #             "virtual_interlining": False,
        #             "local_arrival": "2023-02-13T18:40:00.000Z",
        #             "utc_arrival": "2023-02-13T17:40:00.000Z",
        #             "local_departure": "2023-02-13T13:45:00.000Z",
        #             "utc_departure": "2023-02-13T08:15:00.000Z"
        #         }
        #     ],
        #     "_results": 27,
        #     "search_params": {
        #         "flyFrom_type": "airport",
        #         "to_type": "airport",
        #         "seats": {
        #             "passengers": 1,
        #             "adults": 1,
        #             "children": 0,
        #             "infants": 0
        #         }
        #     },
        #     "all_stopover_airports": [
        #
        #     ],
        #     "sort_version": 0
        # }
        return response['data'][0]['price']
