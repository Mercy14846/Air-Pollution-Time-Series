import requests
import csv
from datetime import datetime, timedelta
import pandas as pd

# Define your API key
api_key = '82e3b9e8650260f04ede50fd59e999b2'

# List of coordinates
coordinates = [
    (7.89568, 3.46282),
    (7.91647, 3.5008),
    (7.78714, 3.55136),
    (7.75877, 3.6714),
    (7.78432, 3.47092),
    (7.77991, 3.4691),
    (7.77376, 3.46835),
    (7.90203, 3.47042),
    (7.74637, 3.50085),
    (7.92699, 3.4948),
    (7.68041, 3.33537),
    (7.76204, 3.53187),
    (7.66682, 3.35358),
    (7.7725, 3.64184),
    (7.85129, 3.40102),
    (7.67315, 3.33793),
    (7.78104, 3.32523),
    (7.94464, 3.61565),
    (7.88459, 3.52851),
    (7.97424, 3.4971),
    (7.78122, 3.37344),
    (7.73242, 3.32309),
    (7.90587, 3.50366),
    (7.7891, 3.64858),
    (7.74092, 3.50491),
    (7.85755, 3.62932),
    (7.77808, 3.29804),
    (7.71854, 3.32505),
    (7.87317, 3.47495),
    (7.77706, 3.30339),
    (7.79662, 3.37001),
    (7.94112, 3.48198),
    (7.81532, 3.55727),
    (7.83829, 3.68062),
    (7.92932, 3.5754),
    (7.75041, 3.47271),
    (7.77067, 3.49067),
    (7.90656, 3.51002),
    (7.72534, 3.32645),
    (7.87113, 3.62101),
    (7.93005, 3.66809),
    (7.91308, 3.49709),
    (7.96987, 3.68039),
    (7.7738, 3.46834),
    (7.82244, 3.46086),
    (7.84194, 3.64485),
    (7.89312, 3.46128),
    (7.76215, 3.39021),
    (7.74968, 3.40417),
    (7.9131, 3.49683),
    (7.79654, 3.43528),
    (7.74168, 3.41129),
    (8.03041, 3.53503),
    (7.79564, 3.43504),
    (7.75814, 3.47676),
    (8.02603, 3.65653),
    (7.90151, 3.50416),
    (7.95911, 3.65383),
    (7.81937, 3.72701),
    (7.94493, 3.52349),
    (7.6716, 3.33599),
    (7.96408, 3.50881),
    (7.8064, 3.71265),
    (7.88775, 3.58369),
    (7.74271, 3.41179),
    (8.0332, 3.60346),
    (7.74187, 3.44292),
    (7.83848, 3.6314),
    (7.96411, 3.50967),
    (7.71242, 3.32353),
    (7.77361, 3.50889),
    (7.74757, 3.41253),
    (7.76319, 3.48398),
    (7.91701, 3.69503),
    (7.84198, 3.64488),
    (7.80043, 3.3039),
    (7.68468, 3.40632),
    (7.72534, 3.32645),
    (7.91662, 3.57582),
    (8.02771, 3.59616),
    (7.78227, 3.64454),
    (7.97799, 3.49038),
    (7.80612, 3.71251),
    (8.00417, 3.67437),
    (7.93931, 3.46922),
    (7.85498, 3.68458),
    (7.8996, 3.46876),
    (7.85676, 3.6103),
    (7.84119, 3.64621),
    (7.9467, 3.68137),
    (7.8098, 3.63199),
    (7.96574, 3.67782),
    (8.02843, 3.65422),
    (7.78181, 3.50315),
    (7.98917, 3.54761),
    (7.72507, 3.32474),
    (7.87143, 3.56277),
    (7.76639, 3.38813),
    (8.02671, 3.65572),
    (7.91584, 3.57606),
    (8.00449, 3.61424),
    (7.80971, 3.55601),
    (7.89091, 3.42295),
    (7.8908, 3.42154),
    (7.86393, 3.46803),
    (7.71242, 3.32353),
    (8.02825, 3.65452),
    (7.77208, 3.70653),
    (7.92289, 3.53812),
    (7.68731, 3.38671),
    (8.02554, 3.71088),
    (7.81435, 3.60879),
    (7.95359, 3.5562),
    (7.9392, 3.70018),
    (7.80509, 3.54326),
    (7.99057, 3.54448),
    (7.66682, 3.35358),
    (7.89655, 3.4643),
    (7.7863, 3.35909),
    (7.75893, 3.45726),
    (7.80819, 3.60054),
    (7.91056, 3.61705),
    (7.66363, 3.37102),
    (7.77696, 3.50542),
    (7.97403, 3.68092),
    (7.78809, 3.52591),
    (7.91192, 3.49596),
    (7.73916, 3.50813),
    (7.77269, 3.64202),
    (7.95239, 3.61477),
    (7.74637, 3.50085),
    (7.92141, 3.63123),
    (8.02587, 3.65912),
    (7.72507, 3.32474),
    (7.75834, 3.64816),
    (8.00367, 3.71162),
    (7.89026, 3.5413),
    (7.74932, 3.31295),
    (7.8072, 3.71412),
    (7.77669, 3.37183),
    (7.89871, 3.61023),
    (7.80738, 3.7129),
    (7.68041, 3.33537),
    (7.87723, 3.40678),
    (7.76614, 3.38615),
    (7.76603, 3.38624),
    (7.99224, 3.69048),
    (7.87901, 3.68632),
    (7.88959, 3.70365),
    (7.69135, 3.33597),
    (7.67315, 3.33793),
    (7.87732, 3.41134),
    (7.9818, 3.49253),
    (7.96987, 3.68039),
    (7.88016, 3.4843),
    (7.66362, 3.33814),
    (7.7725, 3.64184),
    (7.88173, 3.53303),
    (7.85129, 3.40102),
    (7.81874, 3.46495),
    (7.90203, 3.47042),
    (7.94114, 3.47456),
    (7.96784, 3.55953),
    (7.73242, 3.32309),
    (7.91901, 3.63047),
    (7.96644, 3.67747),
    (8.01124, 3.7111),
    (7.92141, 3.63123),
    (7.74595, 3.65965),
    (7.77056, 3.50793),
    (7.8605, 3.70855),
    (7.74901, 3.66283),
    (8.0341, 3.52653),
    (7.75147, 3.50111),
    (7.89958, 3.4653),
    (7.89958, 3.4653),
    (8.00631, 3.68033),
    (7.9058, 3.65667),
    (7.91841, 3.52217),
    (7.7891, 3.64858),
    (8.03281, 3.70481),
    (7.80555, 3.54399),
    (8.02592, 3.64494),
    (7.78227, 3.64454),
    (7.87735, 3.41137),
    (7.94647, 3.54655),
    (7.98214, 3.5594),
    (8.02363, 3.55288),
    (7.94453, 3.55391),
    (7.97907, 3.55792),
    (7.87329, 3.59291),
    (7.75457, 3.67119),
    (7.86172, 3.65745),
    (7.98949, 3.69787),
    (7.96644, 3.67747),
    (7.72744, 3.43709),
    (7.84132, 3.64646),
    (7.96297, 3.67673),
    (7.88252, 3.55718),
    (8.00686, 3.68027),
    (7.76766, 3.50744),
    (7.74968, 3.40417),
    (8.03189, 3.59262),
    (8.02444, 3.54851),
    (7.91759, 3.44488),
    (7.92061, 3.53871),
    (7.67593, 3.36564),
    (7.97432, 3.5159),
    (7.87257, 3.47483),
    (7.75332, 3.65985),
    (7.96297, 3.67673),
    (7.86607, 3.46909),
    (8.03295, 3.60405),
    (8.02975, 3.55793),
    (7.87901, 3.68632),
    (7.81099, 3.7278),
    (7.85758, 3.62916),
    (7.86512, 3.47084),
    (7.92858, 3.69791),
    (7.97493, 3.50199),
    (7.74932, 3.31295),
    (7.86622, 3.46887),
    (7.77696, 3.50542),
    (7.9392, 3.70018),
    (7.8513, 3.64532),
    (7.88683, 3.55784),
    (7.87001, 3.55842),
    (8.02291, 3.54896),
    (7.81374, 3.46652),
    (7.93626, 3.69934),
    (7.66362, 3.33814),
    (7.95235, 3.61466),
    (7.99837, 3.60751),
    (7.80924, 3.46884),
    (7.8072, 3.71412),
    (7.71518, 3.32132),
    (7.71618, 3.32071),
    (8.02904, 3.52936),
    (7.92059, 3.63035),
    (8.00533, 3.61248),
    (7.87305, 3.47626),
    (7.872, 3.69186),
    (7.6833, 3.40776),
    (7.94854, 3.58045),
    (7.8064, 3.71265),
    (7.8216, 3.70001),
    (7.91901, 3.63047),
    (7.77538, 3.38294),
    (7.85132, 3.64599),
    (7.79498, 3.67526),
    (7.7252, 3.32303),
    (7.75446, 3.63042),
    (7.94303, 3.58054),
    (8.03369, 3.5265),
    (7.94931, 3.58061),
    (7.8055, 3.54386),
    (7.70913, 3.326),
    (7.91352, 3.63159),
    (7.85789, 3.39153),
    (7.74271, 3.41179),
    (7.90656, 3.51002),
    (7.76264, 3.52996),
    (7.8154, 3.60634),
    (7.83062, 3.58808),
    (7.85135, 3.64772),
    (7.89163, 3.46064),
    (7.78823, 3.65095),
    (7.81073, 3.53567),
    (8.02508, 3.71022),
    (7.91192, 3.49596),
    (7.79654, 3.43528),
    (7.89568, 3.46282),
    (7.76212, 3.63467),
    (7.86507, 3.46822),
    (7.92709, 3.69787),
    (8.00375, 3.71153),
    (7.97344, 3.52663),
    (7.89745, 3.63633),
    (7.76126, 3.53182),
    (7.83952, 3.71236),
    (7.76608, 3.3863),
    (7.91764, 3.6305),
    (7.85495, 3.68453),
    (7.9682, 3.59752),
    (7.78823, 3.65095),
    (8.02785, 3.59614),
    (7.81434, 3.60879),
    (7.90136, 3.6511),
    (8.004, 3.67358),
    (7.77754, 3.37375),
    (7.91568, 3.57611),
(7.91568, 3.57611),
    (7.78181, 3.50315),
    (7.68108, 3.38645),
    (7.91352, 3.63159),
    (8.0076, 3.68471),
    (7.78629, 3.35903),
    (7.81544, 3.63225),
    (7.87723, 3.40678),
    (7.98222, 3.56751),
    (7.82445, 3.64303),
    (8.02417, 3.54853),
    (7.88648, 3.70218),
    (7.94583, 3.54795),
    (7.8996, 3.46876),
    (8.00334, 3.63262),
    (7.92059, 3.63035),
    (7.90587, 3.50366),
    (7.7863, 3.35255),
    (7.93626, 3.61938),
    (7.87793, 3.55657),
    (7.81189, 3.64253),
    (8.00708, 3.68068),
    (7.80047, 3.68936),
    (7.86512, 3.47114),
    (7.86179, 3.61223),
    (7.96406, 3.50977),
    (7.8329, 3.6038),
    (7.75504, 3.65808),
    (7.98882, 3.54795),
    (7.92541, 3.69827),
    (7.97448, 3.58945),
    (8.02434, 3.70997),
    (7.95239, 3.61477),
    (7.76212, 3.63467),
    (7.87732, 3.41134),
    (8.02523, 3.65),
    (7.96785, 3.55953),
    (7.92709, 3.69787),
    (7.98952, 3.69774),
    (7.91713, 3.60537),
    (8.02541, 3.54121),
    (7.73916, 3.50813),
    (7.82521, 3.63734),
    (7.92858, 3.69791),
    (7.94175, 3.67461),
    (7.74757, 3.41253),
    (7.93058, 3.6133),
    (8.02955, 3.63225),
    (7.86208, 3.70498),
    (7.78276, 3.41806),
    (7.84137, 3.6464),
    (7.99968, 3.66225),
    (7.83288, 3.60293),
    (7.73576, 3.28395),
    (8.02295, 3.60061),
    (7.71618, 3.32071),
    (8.02804, 3.53954),
    (7.89312, 3.46128),
    (7.78276, 3.41806),
    (7.96, 3.56602),
    (7.6716, 3.33599),
    (7.96785, 3.55926),
    (7.95039, 3.67888),
    (7.77056, 3.50793),
    (7.76771, 3.48681),
    (7.85126, 3.64661),
    (8.00663, 3.67988),
    (7.78816, 3.53278),
    (8.02198, 3.70791),
    (7.74774, 3.46141),
    (7.74168, 3.41129),
    (7.71518, 3.32132),
    (7.76003, 3.29938),
    (7.85494, 3.68454),
    (7.89692, 3.43051),
    (7.80738, 3.7129),
    (7.89752, 3.64473),
    (7.69135, 3.33597),
    (7.95997, 3.57426),
    (7.98659, 3.602),
    (7.97278, 3.57849),
    (7.96407, 3.5862),
    (7.97029, 3.61395),
    (7.98821, 3.61843),
    (7.99891, 3.58956),
    (8.00102, 3.55261),
    (7.98933, 3.52623),
    (7.96171, 3.53768),
    (7.94715, 3.63896),
    (8.01344, 3.47144),
    (8.01169, 3.48913),
    (8.0358, 3.4901),
    (7.97067, 3.45666),
    (7.91333, 3.54667),
    (7.80485, 3.45005),
    (7.77102, 3.4343),
    (7.81185, 3.39406),
    (7.83327, 3.42601),
    (7.83377, 3.43108),
    (7.82467, 3.43753),
    (7.82634, 3.43077),
    (7.82993, 3.42789),
    (7.83329, 3.43634),
    (7.82312, 3.43714),
    (7.83209, 3.42638),
    (7.8381, 3.43785),
    (7.82159, 3.43739),
    (7.83562, 3.43591),
    (7.82407, 3.43798),
    (7.80135, 3.44947),
    (7.76616, 3.43858),
    (7.74886, 3.44927),
    (7.78735, 3.45297),
    (7.79124, 3.44655),
    (7.80504, 3.45122),
    (7.81437, 3.42925),
    (7.79182, 3.43042),
    (7.78891, 3.43022),
    (7.78658, 3.4518),
    (7.81346, 3.45789),
    (7.80555, 3.45822),
    (7.82269, 3.53503),
    (7.84742, 3.51921),
    (7.8339, 3.52547),
    (7.84841, 3.51393),
    (7.8283, 3.51063),
    (7.84445, 3.50767),
    (7.82335, 3.50272),
    (7.83687, 3.49283),
    (7.83918, 3.52382),
    (7.82302, 3.51624),
    (7.84445, 3.47437),
    (7.84907, 3.47932),
    (7.83324, 3.52118),
    (7.84082, 3.50206),
    (7.85104, 3.54063),
    (7.83225, 3.56404),
    (7.84214, 3.52151),
    (7.8517, 3.54756),
    (7.8339, 3.52547),
    (7.84775, 3.48888),
    (7.85006, 3.55349),
    (7.85401, 3.57723),
    (7.84709, 3.54459),
    (7.84181, 3.51393),
    (7.83291, 3.53668),
    (7.84247, 3.54657),
    (7.84247, 3.54657),
    (7.84478, 3.51921),
    (7.8461, 3.50536),
    (7.85812, 3.5978),
    (7.86267, 3.56408),
    (7.85903, 3.54768),
    (7.84262, 3.5331),
    (7.8408, 3.53492),
    (7.82713, 3.5249),
    (7.85903, 3.48936),
    (7.82349, 3.41828),
    (7.83169, 3.42374),
    (7.83351, 3.4283),
    (7.8727, 3.43286),
    (7.99208, 3.46384),
    (8.01121, 3.48936),
    (7.99025, 3.49756),
    (7.83625, 3.53492),
    (7.83351, 3.53219),
    (7.95461, 3.59361),
    (7.99125, 3.58676),
    (7.88043, 3.5073),
    (7.96117, 3.45227),
    (7.96004, 3.4598),
    (7.86188, 3.53676),
    (7.87545, 3.54315),
    (7.86573, 3.54406),
    (7.85193, 3.53379),
    (7.86912, 3.50707),
    (7.82908, 3.44222),
    (7.82704, 3.41002),
    (7.86324, 3.51849),
    (7.78881, 3.61531),
    (7.8992, 3.67559),
    (7.99487, 3.59864),
    (7.95665, 3.60298),
    (7.9761, 3.60914),
    (7.98401, 3.59019),
    (7.99848, 3.56827),
    (7.99781, 3.57786),
    (8.00504, 3.47213),
    (8.02381, 3.48172),
    (7.9234, 3.64865),
    (7.76596, 3.73314),
    (7.96592, 3.7135),
    (8.03014, 3.4614),
    (7.87591, 3.44816),
    (7.92024, 3.4646),
    (7.97858, 3.65413),
    (7.96637, 3.69706),
    (7.88541, 3.65321),
    (7.89038, 3.49337),
    (7.97406, 3.53904),
    (7.90848, 3.56142),
    (7.86505, 3.58105),
    (7.8189, 3.67787),
    (7.98763, 3.57009),
    (7.98763, 3.72765),
    (7.98085, 3.69569),
    (7.93969, 3.60252),
    (7.89219, 3.47875),
    (7.84378, 3.45775),
    (7.82207, 3.4783),
    (7.74198, 3.36184),
    (7.72025, 3.37006),
    (7.69763, 3.36778)

]

# Date range
start_date = datetime(2023, 11, 1)
end_date = datetime(2024, 3, 30)

# Function to make API request
def fetch_air_pollution_data(lat, lon, start_timestamp, end_timestamp, api_key):
    url = f'http://api.openweathermap.org/data/2.5/air_pollution/history?lat={lat}&lon={lon}&start={start_timestamp}&end={end_timestamp}&appid={api_key}'
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Error: {response.status_code} for {lat}, {lon} from {start_timestamp} to {end_timestamp}")
        return None

# Function to calculate weekly averages
def calculate_weekly_averages(data):
    weekly_sum = {}
    count = 0
    for entry in data['list']:
        count += 1
        for param, value in entry['components'].items():
            weekly_sum[param] = weekly_sum.get(param, 0) + value
    weekly_average = {param: value / count for param, value in weekly_sum.items()}
    return {
        'aqi': weekly_average.get('aqi', None),
        'co': weekly_average.get('co', None),
        'no': weekly_average.get('no', None),
        'no2': weekly_average.get('no2', None),
        'o3': weekly_average.get('o3', None),
        'so2': weekly_average.get('so2', None),
        'pm2_5': weekly_average.get('pm2_5', None),
        'pm10': weekly_average.get('pm10', None),
        'nh3': weekly_average.get('nh3', None)
    }

# Collect data for all coordinates and dates
weekly_averages = {}
current_date = start_date
while current_date <= end_date:
    end_of_week = current_date + timedelta(days=6)
    if end_of_week > end_date:
        end_of_week = end_date

    for lat, lon in coordinates:
        start_timestamp = int(current_date.timestamp())
        end_timestamp = int((end_of_week + timedelta(days=1)).timestamp())
        data = fetch_air_pollution_data(lat, lon, start_timestamp, end_timestamp, api_key)
        if data and 'list' in data:
            weekly_averages[(lat, lon, current_date.strftime('%Y-%m-%d'))] = calculate_weekly_averages(data)

    current_date += timedelta(days=7)

# Save data to CSV
csv_file = 'weekly_All_24_I.csv'
csv_columns = ['latitude', 'longitude', 'start_date', 'end_date', 'aqi', 'co', 'no', 'no2', 'o3', 'so2', 'pm2_5', 'pm10', 'nh3']
try:
    with open(csv_file, 'w', newline='') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=csv_columns)
        writer.writeheader()
        for (lat, lon, start_date), data in weekly_averages.items():
            end_date = (datetime.strptime(start_date, '%Y-%m-%d') + timedelta(days=6)).strftime('%Y-%m-%d')
            writer.writerow({
                'latitude': lat,
                'longitude': lon,
                'start_date': start_date,
                'end_date': end_date,
                'aqi': data['aqi'],
                'co': data['co'],
                'no': data['no'],
                'no2': data['no2'],
                'o3': data['o3'],
                'so2': data['so2'],
                'pm2_5': data['pm2_5'],
                'pm10': data['pm10'],
                'nh3': data['nh3']
            })
    print(f"Data successfully written to {csv_file}")
except IOError:
    print("I/O error")

csv_file_path = 'weekly_All_24_I.csv'

# Load the CSV file into a DataFrame
df = pd.read_csv(csv_file_path)

# Display the first few rows of the DataFrame
print(df.head(100))