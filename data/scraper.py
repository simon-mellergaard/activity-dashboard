from garmin_personal_api import (
    GarminPersonalApiClient,
    PersonalApiAuthenticator,
)

def get_secret(file_name: str) -> str:
    with open(file_name, "r") as f:
        content = f.read()
        # print(content)
        return content

api_key = get_secret("api.txt")
with PersonalApiAuthenticator() as authenticator:
    token = authenticator.obtain_token(api_key)

with GarminPersonalApiClient(token.access_token) as client:
    # sleep = client.get_daily_sleep("2026-08-15")
    steps = client.get_daily_steps("2026-11-15", "2026-11-15")
    hr = client.get_daily_heart_rate("2026-11-15")
    print(hr)

def get_hr(date: str) -> list:
    with GarminPersonalApiClient(token.access_token) as client:
        hr = client.get_daily_heart_rate(date)
    hr_values = hr['heartRateValues']
    hr_values = [x[1] for x in hr_values]

    return hr_values


# print(token)