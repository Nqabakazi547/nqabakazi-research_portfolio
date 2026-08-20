import streamlit as st

# Page configuration
st.set_page_config(
    page_title="Nqabaakazi Didoo Dyantyi | Research Portfolio",
    page_icon="📊",
    layout="wide"
)

# -------------------------
# HEADER
# -------------------------

st.title("NQABAKAZI DIDOO DYANTYI")

st.subheader(
    "Institutional Research | Data Analytics | Higher Education Research"
)

st.write(
    """
    Welcome to my professional research portfolio.

    This portfolio showcases selected research, analytical,
    institutional and science communication projects completed
    throughout my academic and professional journey.
    """
)

st.divider()

# -------------------------
# ABOUT
# -------------------------

st.header("About Me")

st.write(
    """
    I am an emerging Institutional Research and Data Analytics
    professional with an interest in using research, institutional
    data and evidence-based analysis to support decision-making
    in higher education.
    """
)

st.divider()

# -------------------------
# SELECTED PROJECTS
# -------------------------

st.header("Selected Projects")

st.write(
    "Explore selected research and project work from my academic "
    "and professional journey."
)

col1, col2 = st.columns(2)

with col1:

    st.subheader("🌱 Farm Resource Education")

    st.write(
        "Undergraduate research project exploring Farm Resource Education."
    )

    st.button(
        "View Project",
        key="farm"
    )

    st.subheader("🍷 Wine Research")

    st.write(
        "Undergraduate research project focusing on wine-related research."
    )

    st.button(
        "View Project",
        key="wine"
    )


with col2:

    st.subheader("📊 GDS")

    st.write(
        "Research project completed as part of my Advanced Diploma."
    )

    st.button(
        "View Project",
        key="gds"
    )

    st.subheader("🔬 AIMS Science Communication")

    st.write(
        "Science communication project completed through AIMS."
    )

    st.button(
        "View Project",
        key="aims"
    )

st.divider()

# -------------------------
# INSTITUTIONAL RESEARCH
# -------------------------

st.header("Institutional Research")

st.subheader("CPUT Institutional Report 2025")

st.write(
    """
    Contribution to the CPUT Institutional Report 2025,
    with my name included among the contributors.
    """
)

st.divider()

# -------------------------
# FOOTER
# -------------------------

st.caption(
    "NQABAKAZI DIDOO DYANTYI | Research Portfolio"
)
