import pandas as pd

from send_sms import send_sms


if __name__ == '__main__':
    excel_path = 'numbers.xlsx'
    df = pd.read_excel(excel_path)
    
    template = ''
    with open('text.txt') as f:
        template = f.read()

    for _, contact in df.iterrows():
        info = contact.to_dict()

        text = template.replace('[name]', f'{contact["name"]}')

        is_sent = send_sms(
           f'+{contact["number"]}',
           text
        )

        if not is_sent:
            print(f'[ERROR with] {contact}')

        print('Done!')
    
