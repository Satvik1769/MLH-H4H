import streamlit as st
import pandas as pd
import numpy as np
import altair as alt

st.set_page_config(
    page_icon=":watch:",
    page_title="App",
    layout="wide",
)

st.header("Habit Tracker")
st.markdown("The Habit Tracker falls under the **Habitual** and **Awareness** categories of Green IoT Techniques", help="[Green IoT: An Investigation on Energy Saving Practices for 2020 and Beyond](https://www.researchgate.net/publication/318797858_Green_IoT_An_Investigation_on_Energy_Saving_Practices_for_2020_and_Beyond)")
st.markdown("Do you see any spikes in energy usage? Can you see any patterns in your energy usage? The appliances are the greatest energy consumers are the largest circles, and the tallest bars in the left and right graphs respectively. If you cannot see the points properly, please expand the graphs to full screen. The appliances are in different colours, as shown in the legend.<br><br>", unsafe_allow_html=True)

if 'appliance' not in st.session_state or not st.session_state.appliance:
    st.write("Please enter the appliance usage in the [Resource Budgeter](./Resource_Budgeter). These are mock values.")
    df = pd.DataFrame(abs(np.random.randn(20, 2)*10), columns=['Appliance_ID', 'Expenditure'])
    c1, c2 = st.columns([1, 1], gap="large")
    with c1:
        c = alt.Chart(df).mark_circle().encode(x='Appliance_ID', y='Expenditure', size='Expenditure', color='Appliance_ID', tooltip=['Expenditure', 'Appliance_ID'])
        st.altair_chart(c, use_container_width=True)
    with c2:
        st.line_chart(df, x='Appliance_ID', y='Expenditure', use_container_width=True)
    
    st.write("Appliance with max usage: ", df['Expenditure'].idxmax(), " with", round(df['Expenditure'].max(), 2), "`kwh`")

else:
    df = pd.DataFrame(st.session_state.appliance, columns=['Appliances', 'Expenditure'])
    c1, c2 = st.columns([1, 1], gap="large")
    with c1:
        c = alt.Chart(df).mark_circle().encode(x='Appliances', y='Expenditure', size='Expenditure', color='Appliances', tooltip=['Expenditure', 'Appliances'])
        st.altair_chart(c, use_container_width=True)
    with c2:
        st.line_chart(df, x='Appliances', y='Expenditure', use_container_width=True)

    st.write("Appliance with max usage: `", df['Appliances'][df['Expenditure'].idxmax()], "` with", round(df['Expenditure'].max(), 2), "`kwh`")