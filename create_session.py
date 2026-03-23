import os
import datetime
if not os.path.exists("session"):
    os.makedirs("session")
try:
    from telethon import TelegramClient, sync, events, functions, types
    import sqlite3
    from time import sleep
    from telethon.errors import *
except:
    os.system("pip install telethon")
def tao_session():
    phone = input("Nhập số điện thoại đăng nhập Telegram (+84....) >>> ")
    try:
        api_id = 2182338
        api_hash = 'fa411eff2ec7dcf61bdfadd2478e07bb'
        current_time = datetime.datetime.now().strftime("%m-%d-%Y %H:%M")
        client = TelegramClient("session/"+phone,api_id,api_hash)
        client.connect()
        if not client.is_user_authorized():
            try:
                client.send_code_request(phone)
                client.sign_in(phone,input("Nhập code : "))
                print ("Tạo thành công session "+phone)
                with open("list_session_success.txt", "a") as file:
                    file.write(current_time + ' ' + phone + "\n")
                client.disconnect()
            except SessionPasswordNeededError:
                client.start(phone,input('Nhập mật khẩu 2FA:'))
                print ("Tạo thành công session "+phone)
                with open("list_session_success.txt","a") as file:
                    file.write(current_time+ '|| ' + phone +"\n")
                client.disconnect()
            except PhoneNumberBannedError:
                print ("Tài khoản bị band")
                client.disconnect()
        else:
            print("Đã có sẵn session từ trước")
            client.disconnect()
    except (sqlite3.DatabaseError, sqlite3.OperationalError):
        print("Lỗi session, xóa file session cũ và tạo mới đi")
    except Exception as e:
        print(e)
print("CTRL C để tắt tool")
while(True):
    tao_session()