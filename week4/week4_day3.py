import re


def find_numbers(text):
    return re.findall(r"\d+",text)


def find_emails(text):
    return re.findall(r"[\w.+-]+@[\w-]+\.[\w.-]+",text)


def mask_digits(text):
    return re.sub(r"\d","*",text)


def extract_date(text):
    m=re.search(r"\d{4}-\d{2}-\d{2}",text)
    if m:
        return m.group(0)
    else:
        return None



def censor_emails(text):
    text1=re.sub(r"[\w.+-]+@[\w-]+\.[\w.-]+","<email>",text)
    return text1


if __name__ == "__main__":
    sample = "订单A123 于 2026-09-19 提交，邮箱 user01@test.com，备用 anna@example.cn，电话 13812345678"
    print(find_numbers(sample))
    print(find_emails(sample))
    print(mask_digits(sample))
    print(extract_date(sample))
    print(censor_emails(sample))
