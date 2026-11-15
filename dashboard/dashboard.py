import streamlit as st
import sys
from pathlib import Path

PROJECT = Path(__file__).resolve().parent.parent     # the folder above scripts\
sys.path.insert(0, str(PROJECT))

from data.scraper import get_hr



st.write("""
# Running stats
Contents will come...
""")

st.line_chart(get_hr('2026-11-15'))
