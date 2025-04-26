import streamlit as st
import numpy as np

st.title("Container")

# Menggunakan container
with st.container():
    st.write("Element Inside Container")
    st.line_chart(np.random.randn(48, 4))

st.write("Element Outside Container")


# Container Tidak Berurutan (Out of Order Container)
import streamlit as st
import numpy as np

st.title("Out of Order Container")

# Defining Containers
container_one = st.container()

st.write("Element Outside Container")

with container_one:
    st.write("Element Inside Container")

# Now insert few more elements in the container_one
container_one.write("More Element Inside Container")
container_one.line_chart(np.random.randn(40, 4))

#  Empty Containers
import streamlit as st
import time

# Empty Container
with st.empty():
    for seconds in range(5):
        st.write(f"{seconds + 1} seconds have passed")
        time.sleep(1)
    st.write("⏰ Time's up!")

# Sidebar
import streamlit as st

st.sidebar.title("Sidebar")
st.sidebar.radio("Are you a New User?", ["Yes", "No"])
st.sidebar.slider("Select a Number", 0, 10)

# Multipage
import streamlit as st

st.title("Main page")
st.write("This is Main Page")

st.title("# page 2")
st.write("You have navigated to page one")

st.title("# Page 3")
st.write("you have navigated to pahe one")


# Alert Box

# st.success("Successful")
# st.warning('Warning')
# st.info('Info')
# st.error('Error')
# st.exception(' Its as exception')

import streamlit as st

st.success("Successful")
st.warning("Warning")
st.info("Info")
st.error("Error")

try:
    1 / 0  # Contoh error
except Exception as e:
    st.exception(e)  # Ini akan menampilkan traceback errornya
