# pip install streamlit-pandas-profiling
import pandas as pd
import pandas_profiling
import streamlit as st

from streamlit_pandas_profiling import st_profile_report

def installation():
    st.header("Installation")
    st.markdown("""
    # 📈 Streamlit Pandas Profiling

[![GitHub][github_badge]][github_link] [![PyPI][pypi_badge]][pypi_link] 

## Installation

```sh
pip install streamlit-pandas-profiling
```

## Getting started

```python
import pandas as pd
import pandas_profiling
import streamlit as st

from streamlit_pandas_profiling import st_profile_report

df = pd.read_csv("https://storage.googleapis.com/tf-datasets/titanic/train.csv")
pr = df.profile_report()

st_profile_report(pr)
```           
    """)

def pandas_profiler():
    installation()
    st.title("Pandas Profiler")
    df = pd.read_csv("https://storage.googleapis.com/tf-datasets/titanic/train.csv")
    pr = df.profile_report(explorative=True)

    st_profile_report(pr)
    return 