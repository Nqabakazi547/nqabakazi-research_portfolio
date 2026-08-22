import streamlit as st
import os

# ============================================================
# PAGE CONFIGURATION
# ============================================================

st.set_page_config(
    page_title="Nqabakazi Dyantyi | Research Portfolio",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ============================================================
# CUSTOM CSS
# ============================================================

st.markdown(
    """
    <style>

    /* Main background */
    .stApp {
        background-color: #F7FBFF;
    }

    /* Sidebar */
    [data-testid="stSidebar"] {
        background-color: #EAF4FF;
    }

    /* Main headings */
    h1 {
        color: #0E4D92;
        font-weight: 700;
    }

    h2 {
        color: #0E4D92;
        font-weight: 650;
    }

    h3 {
        color: #1E3A5F;
    }

    /* Horizontal line */
    hr {
        border: none;
        border-top: 1px solid #D7E8F7;
    }

    /* Project cards */
    .project-card {
        background-color: white;
        padding: 25px;
        border-radius: 15px;
        border: 1px solid #DCEAF7;
        margin-bottom: 20px;
        box-shadow: 0px 3px 12px rgba(14, 77, 146, 0.06);
    }

    .project-number {
        color: #6BAED6;
        font-size: 14px;
        font-weight: 700;
        letter-spacing: 1px;
    }

    .project-title {
        color: #0E4D92;
        font-size: 24px;
        font-weight: 700;
        margin-top: 5px;
    }

    .project-description {
        color: #444444;
        font-size: 16px;
        line-height: 1.6;
    }

    /* Small tag */
    .tag {
        display: inline-block;
        background-color: #EAF4FF;
        color: #0E4D92;
        padding: 6px 12px;
        border-radius: 20px;
        margin-right: 5px;
        margin-bottom: 5px;
        font-size: 13px;
    }

    /* Hero section */
    .hero {
        background-color: white;
        padding: 35px;
        border-radius: 18px;
        border: 1px solid #DCEAF7;
        box-shadow: 0px 4px 15px rgba(14, 77, 146, 0.06);
    }

    /* Footer */
    .footer {
        text-align: center;
        color: #6B7280;
        padding: 30px;
        font-size: 13px;
    }

    </style>
    """,
    unsafe_allow_html=True
)

# ============================================================
# SIDEBAR NAVIGATION
# ============================================================

st.sidebar.title("Research Portfolio")

st.sidebar.markdown(
    """
    **Nqabakazi Dyantyi**

    Institutional Research | Data Analytics
    """
)

st.sidebar.divider()

page = st.sidebar.radio(
    "Explore",
    [
        "Home",
        "🌱 Farm Resource Allocation",
        "🍷 WineScan Research",
        "📊 Graduate Destination Survey",
        "🔬 Science Communication"
    ]
)

st.sidebar.divider()

st.sidebar.caption(
    "Selected academic and applied research projects"
)

# ============================================================
# HOME PAGE
# ============================================================

if page == "Home":

    # --------------------------------------------------------
    # HERO
    # --------------------------------------------------------

    st.markdown('<div class="hero">', unsafe_allow_html=True)

    col1, col2 = st.columns([1, 2.2])

    with col1:

        if os.path.exists("profile.jpeg"):
            st.image(
                "profile.jpeg",
                use_container_width=True
            )
        else:
            st.info(
                "Upload your graduation photograph to the repository "
                "and name it **profile.jpeg**."
            )

    with col2:

        st.markdown(
            "# NQABAKAZI DYANTYI"
        )

        st.markdown(
            "### Institutional Research | Data Analytics | Applied Research"
        )

        st.write(
            """
            Welcome to my research portfolio.

            This portfolio presents selected academic and applied
            projects that have shaped my development across
            mathematical modelling, statistical analysis,
            institutional research, data analytics and
            science communication.
            """
        )

    st.markdown("</div>", unsafe_allow_html=True)

    st.write("")

    # --------------------------------------------------------
    # ABOUT
    # --------------------------------------------------------

    st.header("About")

    st.write(
        """
        My work sits at the intersection of research, data and
        decision-making. I am particularly interested in using
        quantitative methods to understand problems, analyse
        evidence and communicate findings in ways that can support
        informed decisions.
        """
    )

    st.divider()

    # --------------------------------------------------------
    # PROJECTS
    # --------------------------------------------------------

    st.header("Research & Project Portfolio")

    st.write(
        "Selected projects from my academic and research journey."
    )

    # --------------------------------------------------------
    # PROJECT 1
    # --------------------------------------------------------

    st.markdown(
        """
        <div class="project-card">

        <div class="project-number">01 — OPERATIONS RESEARCH</div>

        <div class="project-title">
        🌱 Farm Resource Allocation
        </div>

        <p class="project-description">
        <b>Farm Resource Allocation Problem: A Case Study of a Farm
        in Queenstown, Eastern Cape, South Africa.</b>
        </p>

        <p class="project-description">
        An undergraduate Operations Research project investigating
        the application of Linear Programming to agricultural
        resource allocation and decision-making under resource
        constraints.
        </p>

        <span class="tag">Linear Programming</span>
        <span class="tag">MATLAB</span>
        <span class="tag">Optimisation</span>
        <span class="tag">Mathematical Modelling</span>

        </div>
        """,
        unsafe_allow_html=True
    )

    # --------------------------------------------------------
    # PROJECT 2
    # --------------------------------------------------------

    st.markdown(
        """
        <div class="project-card">

        <div class="project-number">02 — SCIENTIFIC RESEARCH</div>

        <div class="project-title">
        🍷 WineScan Research
        </div>

        <p class="project-description">
        A scientific research project investigating the use of
        WineScan FTIR spectroscopy and statistical analysis in
        the study of wine characteristics and pinking susceptibility.
        </p>

        <span class="tag">FTIR Spectroscopy</span>
        <span class="tag">Statistical Analysis</span>
        <span class="tag">ANOVA</span>
        <span class="tag">Research</span>

        </div>
        """,
        unsafe_allow_html=True
    )

    # --------------------------------------------------------
    # PROJECT 3
    # --------------------------------------------------------

    st.markdown(
        """
        <div class="project-card">

        <div class="project-number">03 — INSTITUTIONAL RESEARCH</div>

        <div class="project-title">
        📊 Graduate Destination Survey
        </div>

        <p class="project-description">
        An Advanced Diploma research project focused on improving
        Graduate Destination Survey reporting through survey
        redesign, data quality improvement and Power BI dashboard
        development.
        </p>

        <span class="tag">Survey Research</span>
        <span class="tag">Data Analytics</span>
        <span class="tag">Power BI</span>
        <span class="tag">Institutional Research</span>

        </div>
        """,
        unsafe_allow_html=True
    )

    # --------------------------------------------------------
    # PROJECT 4
    # --------------------------------------------------------

    st.markdown(
        """
        <div class="project-card">

        <div class="project-number">04 — SCIENCE COMMUNICATION</div>

        <div class="project-title">
        🔬 Maths Is NOT The Enemy!
        </div>

        <p class="project-description">
        A science communication and public engagement project
        focused on communicating research around mathematical
        beliefs, confidence and learning to community audiences.
        </p>

        <span class="tag">Science Communication</span>
        <span class="tag">Public Engagement</span>
        <span class="tag">Research Translation</span>

        </div>
        """,
        unsafe_allow_html=True
    )

    st.divider()

    st.markdown(
        """
        <div class="footer">
        © Nqabakazi Dyantyi | Research Portfolio
        </div>
        """,
        unsafe_allow_html=True
    )


# ============================================================
# FARM RESOURCE ALLOCATION
# ============================================================

elif page == "🌱 Farm Resource Allocation":

    st.title("🌱 Farm Resource Allocation Problem")

    st.caption(
        "Undergraduate Research Project | Operations Research"
    )

    st.subheader(
        "A Case Study of a Farm in Queenstown, "
        "Eastern Cape, South Africa"
    )

    st.divider()

    st.header("Project Overview")

    st.write(
        """
        Resource allocation is a significant challenge in
        agriculture. Farmers must make decisions about how to
        allocate limited resources while seeking to improve
        economic outcomes.
        """
    )

    st.header("Research Problem")

    st.write(
        """
        Farm managers face resource allocation challenges while
        attempting to maximise profit under limitations involving
        income, land and labour.

        This project introduced a Linear Programming model,
        implemented using the simplex method in MATLAB, to
        investigate agricultural resource allocation.
        """
    )

    st.header("Objectives")

    st.markdown(
        """
        - Investigate the application of Linear Programming
          to enhance resource allocation in agriculture.
        - Identify key variables and constraints for a
          farmer-focused Linear Programming model.
        - Determine essential parameters and data sources
          for MATLAB implementation.
        - Develop methods for communicating Linear Programming
          results to farm managers for informed decision-making.
        """
    )

    st.header("Methodology")

    st.write(
        """
        The project formulated an agricultural Linear Programming
        problem in which crop areas were treated as decision
        variables. The model incorporated constraints relating
        to land, labour, fertilizer, chemical and seed resources.
        """
    )

    st.markdown(
        """
        **Decision variables**

        - x₁ — cabbage
        - x₂ — spinach
        - x₃ — butternut
        - x₄ — tomatoes
        - x₅ — potatoes
        - x₆ — maize
        """
    )

    # --------------------------------------------------------
    # PROJECT EVIDENCE
    # --------------------------------------------------------

    st.header("Project Evidence")

    st.write(
        """
        The original project presentation provides supporting
        evidence of the research process, mathematical formulation,
        optimisation results and conclusions.
        """
    )

    if os.path.exists("farm_resource_allocation.pptx"):

        with open("farm_resource_allocation.pptx", "rb") as file:
            farm_presentation = file.read()

        st.download_button(
            label="📥 View / Download Farm Resource Allocation Presentation",
            data=farm_presentation,
            file_name="farm_resource_allocation.pptx",
            mime="application/vnd.openxmlformats-officedocument.presentationml.presentation"
        )

    st.divider()

    st.caption(
        "Project: Farm Resource Allocation Problem"
    )


# ============================================================
# WINESCAN
# ============================================================

elif page == "🍷 WineScan Research":

    st.title("🍷 WineScan Research")

    st.caption(
        "Scientific Research Project | Statistical Analysis"
    )

    st.divider()

    st.header("Project Overview")

    st.write(
        """
        This project investigated WineScan FTIR spectroscopy
        as an analytical approach within wine research.
        """
    )

    st.header("Research Focus")

    st.write(
        """
        The study examined factors associated with wine samples
        and used statistical analysis to investigate differences
        between experimental conditions.
        """
    )

    st.header("Statistical Analysis")

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

    st.header("Methods & Tools")

    st.markdown(
        """
        - FTIR / WineScan spectroscopy
        - ANOVA
        - Tukey HSD
        - Statistical analysis
        - Data interpretation
        """
    )

    # --------------------------------------------------------
    # PROJECT EVIDENCE
    # --------------------------------------------------------

    st.header("Project Evidence")

    st.write(
        """
        The original research presentation is provided as
        supporting evidence of the WineScan research process
        and statistical analysis.
        """
    )

    if os.path.exists("winescan_research.pptx"):

        with open("winescan_research.pptx", "rb") as file:
            winescan_presentation = file.read()

        st.download_button(
            label="📥 View / Download WineScan Research Presentation",
            data=winescan_presentation,
            file_name="winescan_research.pptx",
            mime="application/vnd.openxmlformats-officedocument.presentationml.presentation"
        )


# ============================================================
# GRADUATE DESTINATION SURVEY
# ============================================================

elif page == "📊 Graduate Destination Survey":

    st.title("📊 Graduate Destination Survey")

    st.caption(
        "Advanced Diploma Research Project | Institutional Research"
    )

    st.subheader(
        "Improving Graduate Outcomes Reporting at "
        "Cape Peninsula University of Technology"
    )

    st.write(
        """
        A case study in survey redesign and dashboard development.
        """
    )

    st.divider()

    # --------------------------------------------------------
    # PROJECT OVERVIEW
    # --------------------------------------------------------

    st.header("Project Overview")

    st.write(
        """
        This project focused on improving Graduate Destination
        Survey reporting through survey redesign, data quality
        improvement and dashboard development.
        """
    )

    # --------------------------------------------------------
    # RESEARCH PROBLEM
    # --------------------------------------------------------

    st.header("Research Problem")

    st.markdown(
        """
        The project identified several challenges in the existing
        Graduate Destination Survey:

        - Unclear questions
        - No validation or logic
        - Inconsistent responses
        - Weak data quality
        """
    )

    # --------------------------------------------------------
    # OBJECTIVES
    # --------------------------------------------------------

    st.header("Objectives")

    st.markdown(
        """
        - Strengthen the data pipeline through pilot testing.
        - Improve survey quality.
        - Enhance reporting capacity through dashboard development.
        """
    )

    # --------------------------------------------------------
    # METHODOLOGY
    # --------------------------------------------------------

    st.header("Methodology")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.subheader("Data Sources")
        st.write(
            """
            Historical GDS dataset

            Pilot survey using Microsoft Forms
            """
        )

    with col2:
        st.subheader("Tools")
        st.write(
            """
            Excel

            R

            Power BI
            """
        )

    with col3:
        st.subheader("Workflow")
        st.write(
            """
            Data cleaning

            Pilot testing

            Analysis

            Dashboard development
            """
        )

    # --------------------------------------------------------
    # HISTORICAL DATA
    # --------------------------------------------------------

    st.header("Historical Dataset")

    col1, col2 = st.columns(2)

    with col1:
        st.metric(
            "Original Records",
            "2,491"
        )

    with col2:
        st.metric(
            "Valid Graduate Records",
            "1,736"
        )

    st.write(
        """
        The historical dataset contained 2,491 records and
        68 variables. After cleaning, 1,736 valid graduate
        records remained, with 19 relevant variables retained.
        Records were verified against HEMIS.
        """
    )

    # --------------------------------------------------------
    # PILOT DATA
    # --------------------------------------------------------

    st.header("Pilot Survey")

    st.metric(
        "Pilot Responses",
        "19"
    )

    st.write(
        """
        The redesigned pilot survey was conducted using
        Microsoft Forms and was used to test logic, clarity,
        validation and survey flow.
        """
    )

    # --------------------------------------------------------
    # REDESIGNED GDS
    # --------------------------------------------------------

    st.header("Redesigned Graduate Destination Survey")

    st.write(
        """
        The redesigned instrument introduced additional themes
        to strengthen graduate outcomes reporting.
        """
    )

    col1, col2, col3 = st.columns(3)

    with col1:
        st.markdown("**Employment & Career**")
        st.write(
            """
            • Time-to-employment

            • Job relevance

            • Reasons for unemployment
            """
        )

    with col2:
        st.markdown("**Further Development**")
        st.write(
            """
            • Further study details

            • Salary bands
            """
        )

    with col3:
        st.markdown("**Student Experience**")
        st.write(
            """
            • WIL satisfaction

            • CPUT satisfaction
            """
        )

    # --------------------------------------------------------
    # DASHBOARD
    # --------------------------------------------------------

    st.header("Power BI Dashboard")

    st.write(
        """
        The project proposed a Power BI dashboard to provide
        graduate outcomes insights and modernise reporting.
        """
    )

    st.markdown(
        """
        **Dashboard indicators included:**

        - Response Rate
        - Employment Status
        - Salary
        - Sector
        - Further Studies
        - WIL & CPUT Satisfaction
        - Qualification vs Employment
        """
    )

    # --------------------------------------------------------
    # LIMITATIONS
    # --------------------------------------------------------

    st.header("Limitations")

    st.warning(
        """
        The pilot contained only 19 responses, limiting
        generalisability. The sample was also too small for
        inferential statistics or reliability testing.
        Findings therefore remained preliminary pending
        full-scale rollout.
        """
    )

    # --------------------------------------------------------
    # CONCLUSION
    # --------------------------------------------------------

    st.header("Conclusion & Recommendations")

    st.write(
        """
        The project concluded that the redesigned GDS could
        improve clarity while the dashboard could enable
        more timely insights.
        """
    )

    st.markdown(
        """
        **Recommendations**

        - Full rollout of the redesigned GDS
        - Annual GDS implementation
        - Strengthen WIL partnerships
        - Link GDS to HEMIS
        - Continue updating the dashboard with relevant variables
        """
    )

    # --------------------------------------------------------
    # INSTITUTIONAL SIGNIFICANCE
    # --------------------------------------------------------

    st.header("From Academic Research to Institutional Application")

    st.info(
        """
        This project demonstrates how an academic research
        project can contribute to institutional reporting,
        graduate outcomes analysis and evidence-informed
        decision-making.
        """
    )

    # --------------------------------------------------------
    # PROJECT EVIDENCE
    # --------------------------------------------------------

    st.header("Project Evidence")

    st.write(
        """
        The original Graduate Destination Survey presentation
        is provided as supporting evidence of the academic
        research project.
        """
    )

    if os.path.exists("graduate_destination_survey.pptx"):

        with open("graduate_destination_survey.pptx", "rb") as file:
            gds_presentation = file.read()

        st.download_button(
            label="📥 View / Download Graduate Destination Survey Presentation",
            data=gds_presentation,
            file_name="graduate_destination_survey.pptx",
            mime="application/vnd.openxmlformats-officedocument.presentationml.presentation"
        )

    # --------------------------------------------------------
    # INSTITUTIONAL OUTPUT
    # --------------------------------------------------------

    st.subheader("Institutional Output")

    st.write(
        """
        The Graduate Destination Survey work also extended
        beyond the academic research project into an
        institutional reporting context.
        """
    )

    if os.path.exists("gds_institutional_output.JPG"):

    st.image(
        "gds_institutional_output.JPG",
        caption="Figure: Graduate Destination Survey — Institutional Output",
        use_container_width=True
    )

    st.caption(
        "Source: CPUT Office of the Vice-Chancellor (OVC) Report 2025, p. 43."
    )
    else:

        st.warning(
            "The institutional output image could not be found."
        )


# ============================================================
# SCIENCE COMMUNICATION
# ============================================================

elif page == "🔬 Science Communication":

    st.title("🔬 Science Communication")

    st.caption(
        "AIMS / Africa Scientifique | Research Communication"
    )

    st.subheader(
        "Maths Is NOT The Enemy!"
    )

    st.divider()

    st.header("Project Overview")

    st.write(
        """
        A science communication project focused on translating
        ideas about mathematics, beliefs and confidence into
        accessible conversations with community audiences.
        """
    )

    st.header("Focus")

    st.markdown(
        """
        - Science communication
        - Public engagement
        - Research translation
        - Community outreach
        """
    )

    # --------------------------------------------------------
    # PROJECT EVIDENCE
    # --------------------------------------------------------

    st.header("Project Evidence")

    st.write(
        """
        The project report provides documentation of the science
        communication project, while the photographs provide
        evidence of project delivery and public engagement.
        """
    )

    # --------------------------------------------------------
    # REPORT
    # --------------------------------------------------------

    st.subheader("Project Report")

    if os.path.exists("maths_is_not_the_enemy.docx"):

        with open("maths_is_not_the_enemy.docx", "rb") as file:
            maths_report = file.read()

        st.download_button(
            label="📄 View / Download Maths Is NOT The Enemy Report",
            data=maths_report,
            file_name="maths_is_not_the_enemy.docx",
            mime="application/vnd.openxmlformats-officedocument.wordprocessingml.document"
        )

    else:

        st.warning(
            "The Maths Is NOT The Enemy report could not be found."
        )

    # --------------------------------------------------------
    # PROJECT DELIVERY
    # --------------------------------------------------------

    st.subheader("Project Delivery")

    if os.path.exists("maths_is_not_the_enemy_delivery.jpeg"):

        st.image(
            "maths_is_not_the_enemy_delivery.jpeg",
            caption="Maths Is NOT The Enemy! — Project Delivery",
            use_container_width=True
        )

    else:

        st.warning(
            "The project delivery image could not be found."
        )


# ============================================================
# FOOTER
# ============================================================

st.divider()

st.markdown(
    """
    <div class="footer">
        Nqabakazi Dyantyi · Research Portfolio
    </div>
    """,
    unsafe_allow_html=True
)
