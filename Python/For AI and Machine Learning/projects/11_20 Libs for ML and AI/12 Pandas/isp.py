import requests

# Make a request to the IP geolocation API
response = requests.get('https://ipapi.co/json')

# Check if the request was successful
if response.status_code == 200:
    # Retrieve the ISP details from the response
    isp_data = response.json()

    # Extract the ISP information
    isp_name = isp_data['org']
    isp_city = isp_data['city']
    isp_region = isp_data['region']
    isp_country = isp_data['country_name']

    # Display the ISP details
    print("ISP Name:", isp_name)
    print("City:", isp_city)
    print("Region:", isp_region)
    print("Country:", isp_country)
else:
    print("Error retrieving ISP details. Status Code")
