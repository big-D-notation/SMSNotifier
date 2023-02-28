def send_sms(number, text) -> bool:
    try:
        from twilio.rest import Client
        import config

        client = Client(config.account_sid, config.auth_token)

        message = client.messages.create(
            body=text,
            from_=config.number,
            to=number
        )
    except:
        return False
    
    return True
