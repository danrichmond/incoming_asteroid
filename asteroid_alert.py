from email.mime.text import MIMEText
import smtplib
import datetime
import requests

#############################
# User Properties
#############################
smtp_server_name = ""
smtp_port = 
smtp_username = ""
smtp_password = ""
destination_email = ""
api_key = "DEMO_KEY"

#############################
# Function(s)
#############################
def send_alert(message):
    msg = MIMEText(message)
    msg["Subject"] = "Hazardous Asteroid Incoming!"
    msg["From"] = smtp_username
    msg["To"] = destination_email

    smtp = smtplib.SMTP(smtp_server_name, smtp_port)
    smtp.starttls()
    smtp.login(smtp_username, smtp_password)
    smtp.sendmail(smtp_username, destination_email, msg.as_string())
    smtp.quit()

#############################
# Main
#############################
dt = datetime.datetime.now()
today_date = datetime.date(dt.year, dt.month, dt.day)
seven_days_date = today_date + datetime.timedelta(days = 7)

url = "https://api.nasa.gov/neo/rest/v1/feed?start_date=" + str(today_date) + "&end_date=" + str(seven_days_date) + "&api_key=" + api_key

response = requests.get(url)
response_json = response.json()

dates = response_json["near_earth_objects"]

alert_message = ""
hazardous_asteroids = []
for date in dates:
    alert = "\nDate: " + date
    hazardous_count = 0
    for asteroid in dates[date]:
        if(asteroid["is_potentially_hazardous_asteroid"]):
            hazardous_count += 1
            alert += "\n\tName: " + asteroid["name"]
            for data in asteroid["close_approach_data"]:
                alert += "\n\t\tDistance: {:,.2f}".format(float(data["miss_distance"]["miles"])) + " Miles"
                alert += "\n\t\tSpeed: {:,.2f}".format(float(data["relative_velocity"]["miles_per_hour"])) + " MPH"
    if(hazardous_count > 0):
        alert_message += alert
    alert_message += "\n"

send_alert(alert_message)
