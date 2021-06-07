from phone import Phone

if __name__ == "__main__":
    phoneNum = '18588840107'
    info = Phone().find(phoneNum)
    print(info)
    try:
        phone = info['phone']
        province = info['province']
        city = info['city']
        zip_code = info['zip_code']
        area_code = info['area_code']
        phone_type = info['phone_type']
    except:
        print('none')
