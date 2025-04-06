# 🎉 WhatsApp Birthday Reminder Bot

This project is a simple Python-based automation that sends *personalized WhatsApp birthday messages* using the *Twilio API. It reads contact and birthday data from an Excel file and can be deployed for free using **GitHub Actions* to run on a scheduled basis (e.g., daily).

---

## 📌 Features

- Sends WhatsApp birthday wishes automatically
- Reads contact data from an Excel spreadsheet
- Supports manual testing using a Test column
- Hosted as a scheduled GitHub Action (runs daily at specified UTC time)
- Uses Twilio’s WhatsApp messaging API

---

## 🛠 Technologies Used

- *Python 3.10*
- *pandas* for reading Excel data
- *openpyxl* for Excel file compatibility
- *Twilio* for sending WhatsApp messages
- *GitHub Actions* for scheduled automation

---

## 📄 Data Format (Excel)

The Excel file (Birthday.xlsx) should follow this structure:

| Name                  | Mobile        | Date Of Birth | Test |
|-----------------------|---------------|----------------|------|
| Rohan                 | 917893XXXXXX  | 02/03          |      |
| Minnu                 | 917893XXXXXX  | 16-03          |      |
| Roshan                | 919109XXXXXX  | 26-11          | TRUE |
| ...                   | ...           | ...            | ...  |

### Column Details:
- *Name*: Name of the person
- *Mobile*: 10-digit number with country code (e.g., 91XXXXXXXXXX)
- *Date Of Birth*: Can be in formats like DD-MM or DD/MM
- *Test (optional)*: If set to TRUE, the message will be sent immediately, regardless of today's date (used for testing)

> ✅ The script handles dates using pandas.to_datetime() and compares the day and month to the current date.

---

## 🧪 Testing

To test the script without waiting for an actual birthday:
- Add TRUE under the *Test* column for any contact.
- The script will send WhatsApp messages immediately for those rows.

---

## 🚀 Deployment (via GitHub Actions)

This script is deployed using *GitHub Actions* and runs once daily at a scheduled time. The workflow file is located in .github/workflows/birthday-bot.yml.

### Sample Cron Setup
yaml
on:
  schedule:
    - cron: '15 18 * * *'  # Runs daily at 11:45 PM IST
  workflow_dispatch:


### Setup Instructions:
1. Push your code and Birthday.xlsx file to a GitHub repository.
2. Add the following secrets in your GitHub repo settings:
   - TWILIO_SID: Your Twilio Account SID
   - TWILIO_AUTH_TOKEN: Your Twilio Auth Token
3. GitHub Actions will trigger automatically based on the cron schedule or manually via the *"Run workflow"* button.

---

## 📤 WhatsApp Message Sending

This script uses Twilio's [Content API with WhatsApp templates](https://www.twilio.com/docs/content) via:

python
client.messages.create(
    from_='whatsapp:+14155238886',
    to=f'whatsapp:{mobile}',
    content_sid='YOUR_CONTENT_SID',
    content_variables=json.dumps({"person": name})
)


> Replace 'YOUR_CONTENT_SID' with your actual [Twilio Content Template SID](https://www.twilio.com/console/content).

---

## 🔐 Security

Sensitive credentials like Twilio SID and Auth Token are *never hardcoded. They are stored securely using **GitHub Secrets* and accessed via environment variables in the workflow.

---

## 🧾 Requirements

Create a requirements.txt file:

pandas
openpyxl
twilio


Install using:
bash
pip install -r requirements.txt


---

## 👨‍💻 Author

Developed by Hima Hande
Feel free to fork and extend the project!
