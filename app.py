import streamlit as st

st.set_page_config(
    page_title="Nqabaakazi Didoo Dyantyi | Research Portfolio",
    page_icon="📊",
    layout="wide"
)

st.title("NQABAKAZI DIDOO DYANTYI")
st.subheader("Institutional Research | Data Analytics | Higher Education Research")

st.write(
    """
    Welcome to my research portfolio.

    This portfolio showcases selected research, data analysis,
    institutional research and science communication projects.
    """
)

st.divider()

st.header("Selected Projects")

col1, col2 = st.columns(2)

with col1:
    st.subheader("🌱 Farm Resource Education")
    st.write("Undergraduate Research Project")
    st.write(
        "A research project completed during my undergraduate studies."
    )
    st.button("View Project", key="farm")

    st.subheader("🍷 Wine Research")
    st.write("Undergraduate Research Project")
    st.write(
        "An undergraduate research project exploring wine-related research."
    )
    st.button("View Project", key="wine")

with col2:
    st.subheader("📊 GDS")
    st.write("Advanced Diploma Project")
    st.write(
        "Research project completed as part of my Advanced Diploma."
    )
    st.button("View Project", key="gds")

    st.subheader("🔬 AIMS Science Communication")
    st.write("Science Communication Project")
    st.write(
        "A science communication project completed through AIMS."
    )
    st.button("View Project", key="aims")

st.divider()

st.header("Institutional Research")

st.subheader("CPUT Institutional Report 2025")

st.write(
    """
    Contribution to the CPUT Institutional Report 2025,
    with my name included among the contributors.
    """
)

st.divider()

st.header("Contact")

st.write("Research • Data Analytics • Institutional Research")
