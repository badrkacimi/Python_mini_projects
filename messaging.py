from twilio.rest import Client
# put your own credentials here
account_sid = "ACd36bc65909a9e412fd8cbb216e4ba5af"
auth_token = "896b837ff4a02cccd8e277bef0faea95"
client = Client(account_sid, auth_token)
client.messages.create(
  to="+212634302482",
  from_="+14158141829",
  body="khbark")
