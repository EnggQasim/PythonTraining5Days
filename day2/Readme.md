# Streamlit
## Step1 Create->app.py
### Example1:
```
import streamlit as st
st.write('Hello, world!')
```
#### Run program `streamlit run p1.py`
### Example2:
```
import streamlit as st
x = st.slider('x')
st.write(x, 'squared is', x * x)
```

### Exampl3:
```
import streamlit as st
import pandas as pd

# Reuse this data across runs!
read_and_cache_csv = st.cache(pd.read_csv)

BUCKET = "https://streamlit-self-driving.s3-us-west-2.amazonaws.com/"
data = read_and_cache_csv(BUCKET + "labels.csv.gz", nrows=1000)
desired_label = st.selectbox('Filter to:', ['car', 'truck'])
st.write(data[data.label == desired_label]) 
```

## Install 
```
$ pip install --upgrade streamlit 
$ streamlit hello
   You can now view your Streamlit app in your browser.
   Local URL: http://localhost:8501
   Network URL: http://10.0.1.29:8501
```

```
$ pip install --upgrade streamlit opencv-python
$ streamlit run https://raw.githubusercontent.com/streamlit/demo-self-driving/master/streamlit_app.py
```

### Exmaple4:
```
import streamlit as st
import pandas as pd

@st.cache
def load_metadata():
    DATA_URL = "https://streamlit-self-driving.s3-us-west-2.amazonaws.com/labels.csv.gz"
    return pd.read_csv(DATA_URL, nrows=1000)

@st.cache
def create_summary(metadata, summary_type):
    one_hot_encoded = pd.get_dummies(metadata[["frame", "label"]], columns=["label"])
    return getattr(one_hot_encoded.groupby(["frame"]), summary_type)()

# Piping one st.cache function into another forms a computation DAG.
summary_type = st.selectbox("Type of summary:", ["sum", "any"])
metadata = load_metadata()
summary = create_summary(metadata, summary_type)
st.write('## Metadata', metadata, '## Summary', summary)
```