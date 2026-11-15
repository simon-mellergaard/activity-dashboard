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
    sleep = client.get_daily_sleep("2026-08-24")
    steps = client.get_daily_steps("2026-08-20", "2026-08-24")

print(token)