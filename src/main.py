from model import DailyReportModel, UserModel, DeviceModel, WeatherDataModel
from datetime import datetime

# User value intiallised
current_user = 'user_1'
current_device = 'DT002'

# Shows how to initiate and search in the users collection based on a username
user_coll = UserModel(current_user)

user_document = user_coll.find_by_username(current_user)
print("\nIs username based query possible for 'admin'?")
if (user_document == -1):
    print(user_coll.latest_error)

# Shows a successful attempt on how to insert a user
# if user_document.username
user_document = user_coll.insert('test_3', 'test_3@example.com', 'default')
print(f"\nCan '{current_user}' add a new user?")
if (user_document == -1):
    print(user_coll.latest_error)
else:
    print(user_document)

# Shows how to initiate and search in the devices collection based on a device id
device_coll = DeviceModel(current_user)
print(f"\nCan '{current_user}' access device {current_device}?")
device_document = device_coll.find_by_device_id(current_device)
if (device_document):
    print(device_document)

# Shows a successful attempt on how to insert a new device
device_document = device_coll.insert('DT002', 'Temperature Sensor', 'Temperature', 'Acme')
print(f"\nCan '{current_user}' access device?")
if (device_document == -1):
    print(device_coll.latest_error)
else:
    print(device_document)


# Shows how to initiate and search in the weather_data collection based on a device_id and timestamp
wdata_coll = WeatherDataModel(current_user)
print(f"\nCan '{current_user}' read weather data?")
wdata_document = wdata_coll.find_by_device_id_and_timestamp('DT002', datetime(2020, 12, 2, 13, 30, 0))
if (wdata_document):
    print(wdata_document)

# Shows a failed attempt on how to insert a new data point
wdata_document = wdata_coll.insert('DT002', 12, datetime(2020, 12, 2, 13, 30, 0))
print(f"\nCan '{current_user}' write weather data?")
if (wdata_document == -1):
    print(wdata_coll.latest_error)
else:
    print(wdata_document)


### New daily_reports collection 
reports_coll = DailyReportModel(current_user)
print(f"\nCan '{current_user}' read daily report?")
wdata_document = reports_coll.find_by_device_id_and_timestamp('DT001', datetime(2020, 12, 1))
if (wdata_document):
    print(wdata_document)

# Shows a failed attempt on how to insert a new data point
wdata_document = reports_coll.insert('DT002', 12, 6, 15, datetime(2020, 12, 2))
print(f"\nCan '{current_user}' write daily report?")
if (wdata_document == -1):
    print(reports_coll.latest_error)
else:
    print(wdata_document)

# Shows a failed attempt on how to insert a new data point
# wdata_document = reports_coll.insertMultiple('DT002', 12, 6, 15, datetime(2020, 12, 2))
# print(f"\nCan '{current_user}' write daily report?")
# if (wdata_document == -1):
#     print(reports_coll.latest_error)
# else:
#     print(wdata_document)