import time

# Mobile app data
mobile_data = {"name": "Akshaya", "age": 20}

# Web service data
web_data = {"name": "Akshaya", "age": 19}

print("Mobile App Data:", mobile_data)
print("Web Service Data:", web_data)

# Synchronization
print("\nSynchronizing data...")
time.sleep(2)

web_data.update(mobile_data)

print("\nSynchronization Completed!")
print("Updated Web Service Data:", web_data)

# Check synchronization
if mobile_data == web_data:
    print("Data synchronized successfully")
else:
    print("Synchronization failed")
