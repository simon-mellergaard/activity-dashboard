# activity-dashboard
Contains a dashboard solution for sport activities such as running and cycling.

The idea is to make a dashboard with using [Streamlit](https://streamlit.io/) that visualizes running data which is gathered by a seperate script.

The data getter makes use of the [garmin API](https://developer.garmin.com/gc-developer-program/personal/personal-api/), which allows to get data from garmin activities.

## Quick guide

Run a streamlit app with `streamlit run dashbaord/dashboard.py`

## References used in project
* [connect-personal-api-python](https://github.com/garmin/connect-personal-api-python)
* [Streamlit documentation](https://docs.streamlit.io/)