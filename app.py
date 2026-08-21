import streamlit as st

# =========================================================
# PAGE CONFIGURATION
# =========================================================

st.set_page_config(
    page_title="Nqabakazi Dyantyi | Research Portfolio",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded"
)

# =========================================================
# CUSTOM STYLING
# =========================================================

st.markdown(
    """
    <style>

    .main {
        background-color: #FFFFFF;
    }

    [data-testid="stSidebar"] {
        background-color: #EAF4FF;
    }

    h1 {
        color: #0E4D92;
    }

    h2 {
        color: #0E4D92;
    }

    h3 {
        color: #1E3A5F;
    }

    .profile-card {
        background-color: #F7FBFF;
        padding: 30px;
        border-radius: 15px;
        border-left: 5px solid #0E4D92;
        margin-bottom: 20px;
    }

    .project-card {
        background-color: #F7FBFF;
        padding: 20px;
        border-radius: 15px;
        border-left: 5px solid #6BB6FF;
        margin-bottom: 15px;
    }

    .skill-card {
        background-color: #F7FBFF;
        padding: 20px;
        border-radius: 12px;
        margin-bottom: 15px;
    }

    </style>
    """,
    unsafe_allow_html=True
)

# =========================================================
# SIDEBAR NAVIGATION
# =========================================================

st.sidebar.title("Nqabakazi Dyantyi")

page = st.sidebar.radio(
    "Navigate",
    [
        "Home",
        "About Me",
        "Projects",
        "Professional Experience",
        "Skills",
        "Contact"
    ]
)

st.sidebar.divider()

st.sidebar.caption(
    "Institutional Research | Data Analytics | Research Communication"
)

# =========================================================
# HOME
# =========================================================

if page == "Home":

    col1, col2 = st.columns([1, 2])

    with col1:

        st.image(
            "profile.jpg",
            width=280
        )

    with col2:

        st.title("NQABAKAZI DYANTYI")

        st.subheader(
            "Institutional Research | Data Analytics | Science Communication"
        )

        st.write(
            """
            Welcome to my professional research portfolio.

            I am a Junior Data Analyst and emerging Institutional
            Research professional with interests in data analytics,
            quantitative research, survey methodology, optimisation
            modelling, dashboard development and research communication.
            """
        )

        st.write(
            """
            This portfolio presents selected academic and professional
            projects that demonstrate how I use data, statistical
            methods and analytical thinking to investigate real-world
            problems and communicate evidence for decision-making.
            """
        )

    st.divider()

    st.header("Research Profile")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.info(
            """
            🌱

            **Operations Research**

            Linear Programming  
            Optimisation  
            Mathematical Modelling
            """
        )

    with col2:
        st.info(
            """
            📊

            **Institutional Research**

            Survey Research  
            Graduate Outcomes  
            Institutional Analytics
            """
        )

    with col3:
        st.info(
            """
            🔬

            **Research Communication**

            Science Communication  
            Public Engagement  
            Research Translation
            """
        )

    st.divider()

    st.header("Selected Projects")

    col1, col2 = st.columns(2)

    with col1:

        st.markdown(
            """
            <div class="project-card">

            <h3>🌱 Farm Resource Allocation</h3>

            Undergraduate Operations Research project applying
            Linear Programming to agricultural resource allocation.

            </div>
            """,
            unsafe_allow_html=True
        )

        st.markdown(
            """
            <div class="project-card">

            <h3>🍷 WineScan Research</h3>

            Scientific research project investigating WineScan
            FTIR spectroscopy and statistical analysis.

            </div>
            """,
            unsafe_allow_html=True
        )

    with col2:

        st.markdown(
            """
            <div class="project-card">

            <h3>📊 Graduate Destination Survey</h3>

            Research project involving survey redesign,
            data quality and Power BI dashboard development.

            </div>
            """,
            unsafe_allow_html=True
        )

        st.markdown(
            """
            <div class="project-card">

            <h3>🔬 Science Communication</h3>

            AIMS science communication and public engagement
            project focused on communicating mathematics research
            to community audiences.

            </div>
            """,
            unsafe_allow_html=True
        )

# =========================================================
# ABOUT ME
# =========================================================

elif page == "About Me":

    st.title("👩🏽‍💻 About Me")

    col1, col2 = st.columns([1, 2])

    with col1:

        st.image(
            "profile.jpg",
            width=250
        )

    with col2:

        st.subheader("Nqabakazi Dyantyi")

        st.write(
            """
            I am a Junior Data Analyst within the Institutional
            Planning Directorate at the Cape Peninsula University
            of Technology.
            """
        )

        st.write(
            """
            My professional interests are centred on Institutional
            Research, data analytics and evidence-based decision-making.
            I am particularly interested in understanding how
            institutional data can be transformed into meaningful
            information that supports planning and decision-making.
            """
        )

    st.divider()

    st.header("Areas of Interest")

    interests = [
        "Institutional Research",
        "Graduate Outcomes Analytics",
        "Survey Methodology",
        "Data Visualisation",
        "Applied Statistics",
        "Operations Research",
        "Optimisation Modelling",
        "Science Communication"
    ]

    for interest in interests:
        st.write(f"• {interest}")

    st.divider()

    st.header("Education")

    st.markdown(
        """
        **Advanced Diploma in Mathematical Sciences**

        **Postgraduate Diploma in Mathematical Sciences**

        **Continuous Professional Development**
        """
    )

# =========================================================
# PROJECTS
# =========================================================

elif page == "Projects":

    st.title("📁 Research Projects")

    st.write(
        """
        Selected academic and research projects demonstrating
        my experience in quantitative research, statistical
        analysis, optimisation, institutional research and
        science communication.
        """
    )

    st.divider()

    # -----------------------------------------------------
    # PROJECT 1
    # -----------------------------------------------------

    st.header("🌱 01 | Farm Resource Allocation")

    st.caption(
        "Undergraduate Research Project | Operations Research"
    )

    st.subheader(
        "Farm Resource Allocation Problem: "
        "A Case Study of a Farm in Queenstown, "
        "Eastern Cape, South Africa"
    )

    st.write(
        """
        This project investigated the application of Linear
        Programming to improve agricultural resource allocation
        under limited land, labour and financial resources.
        """
    )

    st.markdown("### Research Problem")

    st.write(
        """
        Farm managers face the challenge of maximising profit
        while managing constraints relating to income, available
        land, labour and production costs.

        A Linear Programming model was therefore introduced
        to support more effective agricultural resource
        management and decision-making.
        """
    )

    st.markdown("### Research Objectives")

    st.markdown(
        """
        • Investigate the application of Linear Programming
        to enhance resource allocation in agriculture.

        • Identify key variables and constraints for a
        farmer-focused Linear Programming model.

        • Determine essential parameters and data sources
        for effective MATLAB implementation.

        • Develop methods for communicating Linear Programming
        results to farm managers for informed decision-making.
        """
    )

    st.markdown("### Methodology")

    st.write(
        """
        The study formulated an agricultural Linear Programming
        problem and implemented the model using the simplex method
        in MATLAB.
        """
    )

    st.markdown("### Modelled Crops")

    crop_col1, crop_col2, crop_col3 = st.columns(3)

    with crop_col1:
        st.info("🥬 Cabbage")
        st.info("🌿 Spinach")

    with crop_col2:
        st.info("🎃 Butternut")
        st.info("🍅 Tomatoes")

    with crop_col3:
        st.info("🥔 Potatoes")
        st.info("🌽 Maize")

    st.markdown("### Resources Considered")

    st.markdown(
        """
        • Land

        • Labour

        • Fertilizer

        • Chemicals

        • Seed costs

        • Income and expenses
        """
    )

    st.markdown("### Mathematical Model")

    st.latex(
        r"""
        \max Z =
        160000x_1 +
        56000x_2 +
        80000x_3 +
        166975.8813x_4 +
        400000x_5 +
        1200000x_6
        """
    )

    st.write(
        """
        where the decision variables represent the area
        allocated to each crop.
        """
    )

    st.markdown(
        """
        **Decision variables**

        • x₁ = cabbage

        • x₂ = spinach

        • x₃ = butternut

        • x₄ = tomatoes

        • x₅ = potatoes

        • x₆ = maize
        """
    )

    st.info(
        """
        📌 **Results section**

        Detailed optimisation results, resource allocation
        tables and farmer-versus-LP comparisons will be added
        to this portfolio once the final results have been
        verified.
        """
    )

    st.markdown("### Skills Demonstrated")

    st.markdown(
        """
        ✅ Linear Programming  
        ✅ Operations Research  
        ✅ MATLAB  
        ✅ Mathematical Modelling  
        ✅ Optimisation  
        ✅ Quantitative Analysis
        """
    )

    st.divider()

    # -----------------------------------------------------
    # PROJECT 2
    # -----------------------------------------------------

    st.header("🍷 02 | WineScan Research")

    st.caption(
        "Scientific Research Project | Statistical Analysis"
    )

    st.subheader(
        "Investigating WineScan as a Tool for Identifying "
        "Pinking in Wine"
    )

    st.write(
        """
        This research investigated WineScan FTIR spectroscopy
        as a potential analytical tool for identifying pinking
        susceptibility in white wine.
        """
    )

    st.markdown("### Research Focus")

    st.write(
        """
        The study examined the influence of experimental
        conditions and wine characteristics on measured
        absorbance and investigated whether WineScan could
        provide a rapid and non-destructive analytical approach.
        """
    )

    st.markdown("### Statistical Analysis")

    col1, col2 = st.columns(2)

    with col1:
        st.metric(
            "F Statistic",
            "49.42"
        )

    with col2:
        st.metric(
            "p-value",
            "< 2 × 10⁻¹⁶"
        )

    st.write(
        """
        ANOVA was used to investigate differences between
        treatment groups, with Tukey HSD used for post-hoc
        comparisons.
        """
    )

    st.markdown("### Key Findings")

    st.markdown(
        """
        • Ripening stage significantly influenced absorbance.

        • The 25°B treatment showed the highest absorbance.

        • Press method showed minimal effect.

        • Temperature showed limited impact.
        """
    )

    st.success(
        """
        WineScan demonstrated potential as a rapid,
        non-destructive analytical approach for assessing
        pinking susceptibility in wine.
        """
    )

    st.markdown("### Skills Demonstrated")

    st.markdown(
        """
        ✅ ANOVA  
        ✅ Tukey HSD  
        ✅ FTIR Spectroscopy  
        ✅ Experimental Analysis  
        ✅ Statistical Interpretation
        """
    )

    st.divider()

    # -----------------------------------------------------
    # PROJECT 3
    # -----------------------------------------------------

    st.header("📊 03 | Graduate Destination Survey")

    st.caption(
        "Advanced Diploma Research Project | Institutional Research"
    )

    st.subheader(
        "Improving Graduate Outcomes Reporting at CPUT"
    )

    st.write(
        """
        This project focused on improving the Graduate Destination
        Survey through survey redesign, data quality improvement
        and dashboard development.
        """
    )

    st.markdown("### Research Problem")

    st.markdown(
        """
        Existing survey challenges included:

        • Unclear questions

        • Limited validation

        • Inconsistent responses

        • Data quality challenges

        • Limited reporting capability
        """
    )

    st.markdown("### Objectives")

    st.markdown(
        """
        • Improve survey quality.

        • Strengthen the data pipeline.

        • Improve data quality.

        • Enhance graduate outcomes reporting.

        • Develop a dashboard solution.
        """
    )

    st.markdown("### Historical Dataset")

    col1, col2 = st.columns(2)

    with col1:
        st.metric(
            "Original Records",
            "2,491"
        )

    with col2:
        st.metric(
            "Valid Records",
            "1,736"
        )

    st.write(
        """
        Historical records were cleaned and verified before
        being prepared for analysis and survey redesign.
        """
    )

    st.markdown("### Tools Used")

    st.markdown(
        """
        • Excel

        • Microsoft Forms

        • R

        • Power BI
        """
    )

    st.markdown("### Survey Redesign")

    st.markdown(
        """
        New or improved areas included:

        • Salary bands

        • Job relevance

        • Time to employment

        • Reasons for unemployment

        • Further studies

        • Work-integrated learning satisfaction
        """
    )

    st.markdown("### Skills Demonstrated")

    st.markdown(
        """
        ✅ Survey Design  
        ✅ Data Cleaning  
        ✅ Data Validation  
        ✅ Power BI  
        ✅ Institutional Research  
        ✅ Dashboard Development
        """
    )

    st.divider()

    # -----------------------------------------------------
    # PROJECT 4
    # -----------------------------------------------------

    st.header("🔬 04 | Science Communication & Public Engagement")

    st.caption(
        "Africa Scientifique Programme | AIMS South Africa"
    )

    st.subheader(
        "Maths Is NOT The Enemy!"
    )

    st.write(
        """
        This project explored how parents' beliefs about
        mathematics can influence children's confidence
        and attitudes towards mathematics.
        """
    )

    st.markdown("### Project Focus")

    st.write(
        """
        The project translated research and mathematical
        ideas into accessible messages for community audiences.
        """
    )

    st.markdown("### Objectives")

    st.markdown(
        """
        • Promote positive beliefs about mathematics.

        • Engage parents and grandparents.

        • Communicate scientific concepts using accessible language.

        • Encourage positive support for learners.
        """
    )

    st.markdown("### Target Audience")

    st.markdown(
        """
        • Parents

        • Grandparents

        • Community members

        • CPUT staff and campus community
        """
    )

    st.markdown("### Skills Demonstrated")

    st.markdown(
        """
        ✅ Science Communication  
        ✅ Public Engagement  
        ✅ Storytelling  
        ✅ Public Speaking  
        ✅ Community Outreach  
        ✅ Research Translation
        """
    )

# =========================================================
# PROFESSIONAL EXPERIENCE
# =========================================================

elif page == "Professional Experience":

    st.title("🏛️ Professional Experience")

    st.subheader(
        "Institutional Planning | Cape Peninsula University of Technology"
    )

    st.caption(
        "Junior Data Analyst"
    )

    st.write(
        """
        My professional work involves supporting institutional
        analytics, graduate outcomes reporting and evidence-based
        decision-making within a higher education environment.
        """
    )

    st.divider()

    st.header("Institutional Research & Analytics")

    st.markdown(
        """
        ✅ Graduate Outcomes Analysis

        ✅ Data Cleaning

        ✅ Graduate Record Verification

        ✅ Data Quality Checks

        ✅ Survey Analytics

        ✅ Institutional Reporting

        ✅ Data Visualisation

        ✅ Executive Reporting Support

        ✅ Dashboard Development
        """
    )

    st.divider()

    st.header("Graduate Outcomes Reporting")

    col1, col2 = st.columns(2)

    with col1:
        st.metric(
            "Response Rate",
            "22.1%"
        )

    with col2:
        st.metric(
            "Employment Rate",
            "41.7%"
        )

    st.write(
        """
        Graduate Destination Survey information is analysed
        and transformed into reporting outputs that can support
        institutional planning and management decision-making.
        """
    )

    st.divider()

    st.header("Research Interests")

    st.markdown(
        """
        • Institutional Research

        • Student Success

        • Graduate Outcomes

        • Survey Methodology

        • Data Analytics

        • Higher Education Planning

        • Evidence-Based Decision-Making
        """
    )

# =========================================================
# SKILLS
# =========================================================

elif page == "Skills":

    st.title("💡 Skills & Methods")

    col1, col2 = st.columns(2)

    with col1:

        st.header("Data & Analytics")

        st.markdown(
            """
            ✅ Excel

            ✅ Power BI

            ✅ Python

            ✅ R

            ✅ SQL

            ✅ Data Cleaning

            ✅ Data Visualisation

            ✅ Dashboard Development
            """
        )

        st.header("Institutional Research")

        st.markdown(
            """
            ✅ Survey Design

            ✅ Graduate Outcomes Analysis

            ✅ Institutional Analytics

            ✅ Data Quality

            ✅ Executive Reporting

            ✅ Evidence-Based Planning
            """
        )

    with col2:

        st.header("Statistical & Quantitative Methods")

        st.markdown(
            """
            ✅ ANOVA

            ✅ Tukey HSD

            ✅ Statistical Analysis

            ✅ Linear Programming

            ✅ Optimisation

            ✅ Mathematical Modelling
            """
        )

        st.header("Research Communication")

        st.markdown(
            """
            ✅ Research Translation

            ✅ Science Communication

            ✅ Public Speaking

            ✅ Storytelling

            ✅ Stakeholder Engagement

            ✅ Community Outreach
            """
        )

# =========================================================
# CONTACT
# =========================================================

elif page == "Contact":

    st.title("📧 Contact")

    col1, col2 = st.columns([1, 2])

    with col1:

        st.image(
            "profile.jpg",
            width=250
        )

    with col2:

        st.subheader("Nqabakazi Dyantyi")

        st.write(
            """
            Junior Data Analyst

            Institutional Planning Directorate

            Cape Peninsula University of Technology
            """
        )

        st.write(
            """
            **Research interests**

            Institutional Research • Data Analytics •
            Graduate Outcomes • Survey Research •
            Operations Research • Science Communication
            """
        )

    st.divider()

    st.info(
        """
        Thank you for visiting my research portfolio.
        """
    )

# =========================================================
# FOOTER
# =========================================================

st.divider()

st.caption(
    "© Nqabakazi Dyantyi | Research Portfolio"
)
