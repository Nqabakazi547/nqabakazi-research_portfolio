import streamlit as st

st.set_page_config(
    page_title="Nqabaakazi Didoo Dyantyi | Research Portfolio",
    page_icon="📊",
    layout="wide"
)

# ============================================================
# HOME
# ============================================================

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

st.header("Selected Projects")

st.write(
    "Explore selected research and project work."
)

# ============================================================
# FARM RESOURCES ALLOCATION
# ============================================================

st.header("🌱 Farm Resources Allocation")

st.subheader(
    "Farm Resources Allocation Problem: "
    "A Case Study of a Farm in Queenstown, Eastern Cape, South Africa"
)

st.caption("Undergraduate Research Project")

st.write(
    """
    This project investigated the application of Linear Programming
    to support agricultural resource allocation and improve
    decision-making under limited land, labour and financial resources.
    """
)

with st.expander("Project Overview"):

    st.write(
        """
        Resource allocation is an important challenge in agriculture,
        where farmers must determine how to allocate limited resources
        across competing crop activities while seeking to maximise
        profitability.

        This study investigated the application of Linear Programming
        to a farm in Queenstown, Eastern Cape, South Africa.
        """
    )


with st.expander("Problem Statement"):

    st.write(
        """
        Farm managers face resource allocation challenges while
        attempting to maximise profit under limitations relating to
        income, land and labour.

        A Linear Programming model was therefore introduced to
        investigate how agricultural resources could be allocated
        more effectively.
        """
    )


with st.expander("Research Objectives"):

    st.markdown(
        """
        **1.** Investigate the application of Linear Programming
        to enhance resource allocation in agriculture.

        **2.** Identify key variables and constraints for a
        farmer-focused Linear Programming model.

        **3.** Determine essential parameters and data sources
        required for effective MATLAB implementation.

        **4.** Develop methods for communicating Linear Programming
        results to farm managers for informed decision-making.
        """
    )


with st.expander("Methodology"):

    st.write(
        """
        The study formulated a Linear Programming model to determine
        an optimal allocation of agricultural resources across
        different crop activities.

        The model incorporated resource constraints including:
        """
    )

    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric("Land", "Constraint")
        st.metric("Labour", "Constraint")

    with col2:
        st.metric("Fertilizer", "Constraint")
        st.metric("Chemicals", "Constraint")

    with col3:
        st.metric("Seed Costs", "Constraint")
        st.metric("Income", "Objective")


with st.expander("Decision Variables"):

    st.write(
        "The model defined six decision variables representing "
        "the area allocated to each crop in hectares."
    )

    variables = {
        "Variable": [
            "x₁",
            "x₂",
            "x₃",
            "x₄",
            "x₅",
            "x₆"
        ],
        "Crop": [
            "Cabbage",
            "Spinach",
            "Butternut",
            "Tomatoes",
            "Potatoes",
            "Maize"
        ],
        "Meaning": [
            "Area allocated to cabbage (ha)",
            "Area allocated to spinach (ha)",
            "Area allocated to butternut (ha)",
            "Area allocated to tomatoes (ha)",
            "Area allocated to potatoes (ha)",
            "Area allocated to maize (ha)"
        ]
    }

    st.table(variables)


with st.expander("Linear Programming Model"):

    st.write("### Objective Function")

    st.latex(
        r"""
        \text{Maximise } Z =
        160000x_1 +
        56000x_2 +
        80000x_3 +
        166975.8813x_4 +
        400000x_5 +
        1200000x_6
        """
    )

    st.write("### Resource Constraints")

    st.latex(
        r"""
        x_1+x_2+x_3+x_4+x_5+x_6 \leq 39
        """
    )

    st.latex(
        r"""
        2x_1+2x_2+10x_3+
        22.08675678x_4+
        5x_5+5x_6 \leq 100
        """
    )

    st.latex(
        r"""
        424x_1+424x_2+1770x_3+
        11728.06785x_4+
        885x_5+1770x_6
        \leq 60000
        """
    )

    st.latex(
        r"""
        597x_1+424x_2+2985x_3+
        8790.529x_4+
        1492.5x_5+1492.5x_6
        \leq 50000
        """
    )

    st.latex(
        r"""
        8000x_1+8000x_2+10000x_3+
        27829.31354x_4+
        5000x_5+40000x_6
        \leq 200000
        """
    )

    st.write("### Minimum Allocation Requirements")

    st.latex(r"x_1 \geq 3")

    st.latex(r"x_2 \geq 3")

    st.latex(r"x_4 \geq 1")

    st.latex(r"x_5 \geq 2")

    st.latex(
        r"x_1,x_2,x_3,x_4,x_5,x_6 > 0"
    )


st.info(
    "Results and discussion will be added after verification "
    "against the original research report and presentation."
)


# ============================================================
# OTHER PROJECTS
# ============================================================

st.divider()

st.header("Other Projects")

col1, col2 = st.columns(2)

with col1:

    st.subheader("🍷 Wine Research")

    st.write(
        "Undergraduate research project."
    )

    st.button(
        "Coming Soon",
        key="wine"
    )

    st.subheader("📊 GDS")

    st.write(
        "Advanced Diploma research project."
    )

    st.button(
        "Coming Soon",
        key="gds"
    )


with col2:

    st.subheader("🔬 AIMS Science Communication")

    st.write(
        "Science communication project completed through AIMS."
    )

    st.button(
        "Coming Soon",
        key="aims"
    )

    st.subheader("🏛️ CPUT Institutional Report 2025")

    st.write(
        "Institutional research contribution published in "
        "the 2025 institutional report."
    )

    st.button(
        "Coming Soon",
        key="report"
    )


st.divider()

st.caption(
    "NQABAKAZI DIDOO DYANTYI | Research Portfolio"
)
