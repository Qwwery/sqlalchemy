# valerysite06@gmail.com - почта
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


def send_email():
    # Заполните эти поля вашими данными
    sender_email = "valerysite06@gmail.com"
    receiver_email = "valerysite06@gmail.com"  # кому
    password = " "  # наш пароль
    subject = "Subject of the email"
    body = "проверка"

    # Создание объекта сообщения
    message = MIMEMultipart()
    message['From'] = sender_email
    message['To'] = receiver_email
    message['Subject'] = subject

    # Добавление тела письма
    message.attach(MIMEText(body, 'plain'))

    # Создание объекта сессии SMTP
    session = smtplib.SMTP('smtp.gmail.com', 587)  # Укажите здесь свой SMTP сервер
    session.starttls()  # Активация шифрования
    session.login(sender_email, password)  # Авторизация на сервере

    # Отправка сообщения
    session.sendmail(sender_email, receiver_email, message.as_string())
    session.quit()

    print("Email sent successfully.")


send_email()
