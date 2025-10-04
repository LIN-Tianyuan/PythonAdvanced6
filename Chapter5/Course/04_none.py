def check_age(age):
    if age > 18:
        return "SUCCESS"
    return None

result = check_age(19)
if not result:
    print("未成年，不可进入")