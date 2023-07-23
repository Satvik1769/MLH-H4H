import streamlit as st

st.set_page_config(
    page_icon=":sun:",
    page_title="App",
    layout="wide",
)

st.header("Solar Suitability")

st.markdown("""
When it comes to alternate forms of energy, solar energy is the most popular. Solar panels are a great way to reduce your carbon footprint, and save money on electricity bills. However, they are not suitable for every household. This component helps you determine if solar panels are a good fit for your home. This does not cover all aspects, so please do your research before investing in solar panels.<br>
The metrics and guidlines are taken from the article [Is My House a Good Candidate for Solar?](https://www.ecowatch.com/solar/worth-it)<br><br>
            """,
            unsafe_allow_html=True)

q1, q2 = st.columns([1, 1], gap="small")

with q1:
    costs = st.checkbox("High Electricity Costs", value=False, key="costs", help="&gt; 500kwh per Month", on_change=None,disabled=False, label_visibility="visible")
    sun = st.checkbox("Installation Area receives Sunlight throughout the Day", value=False, key="sun", on_change=None,disabled=False, label_visibility="visible")
    area = st.checkbox("Sufficient Surface Area", value=False, key="area", help="&ge; 100sqft per kW", on_change=None,disabled=False, label_visibility="visible")
with q2:
    cardinal = st.checkbox("Installation Area faces South or West", value=False, key="cardinal", on_change=None,disabled=False, label_visibility="visible")
    unsubsidized = st.checkbox("Electricity is **not** subsidized", value=False, key="unsubsidized", on_change=None,disabled=False, label_visibility="visible")
    income = st.checkbox("Available Investable Income", value=False, key="income", help="Can you cover the installation costs in 15 months?", on_change=None,disabled=False, label_visibility="visible")

suitability = st.button("Calculate Suitability")

if suitability:
    if costs and sun and area and cardinal and unsubsidized and income:
        st.success("Solar Panels might be a great fit for you!")
    if not costs and not sun and not area and not cardinal and not unsubsidized and not income:
        st.error("Solar Panels might not be a good fit for you.")
    else:
        if not income or not unsubsidized or not costs:
            st.warning("Solar Panels may still be a viable option, but you need to consider ROI.")
        if not cardinal or not area or not sun:
            st.warning("Solar Panels may still be a viable option, but they would operated with reduced efficiency.")
    
    if not costs:
        st.write("Solar Power is generally not reccomended for those who spend less than 500kwh per month on electricity due to the cost of installation and maintenance. You could look into alternative solar products like solar batteries, or solar appliances.")
    if not sun:
        st.write("Solar Panels are most efficient when they receive sunlight throughout the day. If your installation area is shaded by trees or other buildings, you should look into other areas for installation.")
    if not area:
        st.write("Solar Panels require a large surface area for installation. If you do not have enough space, you could look into alternative solar products.")
    if not cardinal:
        st.write("Solar Panels are most efficient when they face South or West, where they receive direct sunlight when it is strongest. If your installation area faces North or East, you should look into other areas for installation.")
    if not unsubsidized:
        st.write("While Solar Panels are a great investment, they might not have a good ROI for those who receive subsidized electricity. It would be more cost effective to get your energy from the grid.")
    if not income:
        st.write("Solar Panels are a great investment, but they require a large upfront cost. If you cannot cover the cost within 15 months, it would be advisible to look into other solar products.")