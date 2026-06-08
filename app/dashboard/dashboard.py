import streamlit as st
import pandas as pd
import plotly.express as px

from app.utils.file_loader import FileLoader
from app.preprocessing.preprocess import TextPreprocessor
from app.detection.similarity import SimilarityEngine
from app.detection.winnowing import Winnowing
from app.detection.minhash_lsh import MinHash, LSH
from app.utils.report_generator import ReportGenerator
import plotly.graph_objects as go



st.set_page_config(
    page_title="PlagiarismGuard AI",
    page_icon="🛡️",
    layout="wide"
)

st.markdown("""
<style>

/* Sidebar */
[data-testid="stSidebar"] {
    background-color: #1e1e2f;
}

/* Navigation Radio Buttons */
div[role="radiogroup"] > label {
    background: #2d3748;
    border: 1px solid #4a5568;
    border-radius: 12px;
    padding: 12px;
    margin-bottom: 10px;
    transition: all 0.3s ease;
}

/* Hover Effect */
div[role="radiogroup"] > label:hover {
    background: #2563eb;
    border-color: #3b82f6;
    transform: translateX(5px);
}

/* Selected Item */
div[role="radiogroup"] > label[data-selected="true"] {
    background: linear-gradient(
        90deg,
        #2563eb,
        #06b6d4
    );
    border: none;
    color: white;
    font-weight: bold;
}

</style>
""", unsafe_allow_html=True)

st.markdown("""
<style>

.main {
    padding-top: 1rem;
}

[data-testid="metric-container"] {
    background-color: #1e293b;
    border: 1px solid #334155;
    padding: 15px;
    border-radius: 15px;
}

h1 {
    color: #38bdf8;
}

</style>
""", unsafe_allow_html=True)

st.sidebar.title("🛡️ PlagiarismGuard AI")

page = st.sidebar.radio(
    "Navigation",
    [
        "Dashboard",
        "Document Analysis",
        "Reports"
    ]
)
st.markdown("""
<div style="
background: linear-gradient(90deg,#2563eb,#06b6d4);
padding:20px;
border-radius:15px;
text-align:center;
color:white;
">

<h1>🛡️ PlagiarismGuard AI</h1>

<h4>Advanced Document Similarity & Plagiarism Analytics Platform</h4>

</div>
""",
unsafe_allow_html=True)
st.subheader("Advanced Plagiarism Detection Platform")

processor = TextPreprocessor()
similarity_engine = SimilarityEngine()
winnowing = Winnowing()



original_file = st.file_uploader(
    "📄 Upload Original Document",
    type=["txt"]
)

submission_file = st.file_uploader(
    "📄 Upload Submission Document",
    type=["txt"]
)

if original_file and submission_file:

    original_text = original_file.read().decode("utf-8")

    submission_text = submission_file.read().decode("utf-8")

    original = processor.preprocess(original_text)
    submission = processor.preprocess(submission_text)

    similarity_result = similarity_engine.calculate_similarity(
       original["tokens"],
       submission["tokens"]
    )
    
    st.success("✅ Documents analyzed successfully")

    winnow_score = winnowing.similarity_score(
     original["clean_text"],
     submission["clean_text"]
    )

    minhash = MinHash()

    sig1 = minhash.get_signature(
      original["tokens"]
    )

    sig2 = minhash.get_signature(
       submission["tokens"]
    )

    lsh = LSH()

    minhash_score = lsh.similarity(
      sig1,
      sig2
    )

if not (original_file and submission_file):
    st.info("📄 Upload both documents to start analysis")
    st.stop()

# ==========================
# DASHBOARD PAGE
# ==========================

if page == "Dashboard":

    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.metric(
            "📊 Similarity",
            f"{similarity_result['similarity_percentage']}%"
        )

    with col2:
        st.metric(
            "🔍 Winnowing",
            f"{winnow_score}%"
        )

    with col3:
        st.metric(
            "⚡ MinHash",
            f"{minhash_score}%"
    )
    with col4:
          avg_score = (
          similarity_result["similarity_percentage"]
          + winnow_score
          + minhash_score
    ) / 3

    st.metric(
        "🚨 Risk Score",
        f"{avg_score:.1f}%"
    )    


    st.subheader("🎯 Overall Plagiarism Score")

    gauge_fig = go.Figure(
      go.Indicator(
        mode="gauge+number",
        value=similarity_result["similarity_percentage"],
        title={"text": "Similarity Score"},
        gauge={
            "axis": {"range": [0, 100]},
            "bar": {"color": "red"},
            "steps": [
                {"range": [0, 30], "color": "green"},
                {"range": [30, 60], "color": "yellow"},
                {"range": [60, 80], "color": "orange"},
                {"range": [80, 100], "color": "red"}
            ]
        }
      )
   )

    st.plotly_chart(
        gauge_fig,
        use_container_width=True,
        key="gauge_chart"
    )    

    st.subheader("📈 Algorithm Comparison")

    radar_fig = go.Figure()

    radar_fig.add_trace(
      go.Scatterpolar(
        r=[
            similarity_result["similarity_percentage"],
            similarity_result["similarity_percentage"],
            winnow_score,
            minhash_score
        ],
        theta=[
            "KMP",
            "Rabin-Karp",
            "Winnowing",
            "MinHash"
        ],
        fill="toself",
        name="Algorithms"
     )
    )

    radar_fig.update_layout(
            polar=dict(
            radialaxis=dict(
            visible=True,
            range=[0, 100]
        )
    ),
    showlegend=False
    )

    st.plotly_chart(
     radar_fig,
     use_container_width=True,
     key="radar_chart"
    )

    scores = pd.DataFrame({
        "Method": [
            "Similarity",
            "Winnowing",
            "MinHash"
        ],
        "Score": [
            similarity_result["similarity_percentage"],
            winnow_score,
            minhash_score
        ]
    })

    fig = px.bar(
        scores,
        x="Method",
        y="Score",
        text="Score",
        title="Plagiarism Analysis Comparison"
    )

    st.plotly_chart(
        fig,
        use_container_width=True,
        key="dashboard_chart"
    )

    st.subheader("🚨 Risk Assessment")

    avg_score = (
        similarity_result["similarity_percentage"]
        + winnow_score
        + minhash_score
    ) / 3

    if avg_score < 30:
        st.success("🟢 Low Risk")
    elif avg_score < 60:
        st.warning("🟡 Moderate Risk")
    elif avg_score < 80:
        st.warning("🟠 High Risk")
    else:
        st.error("🔴 Critical Risk")

# ==========================
# DOCUMENT ANALYSIS PAGE
# ==========================

elif page == "Document Analysis":

    st.header("📄 Document Analysis")

    st.subheader("Original Document")
    st.text_area(
        "Original Text",
        original_text,
        height=250
    )

    st.subheader("Submission Document")
    st.text_area(
        "Submission Text",
        submission_text,
        height=250
    )

    st.subheader("🔍 Common Matching Words")

    common_words_text = ", ".join(
     similarity_result["common_words"]
    )

    st.text_area(
     "Matched Keywords",
     common_words_text,
     height=120
    )

    

# ==========================
# REPORTS PAGE
# ==========================

elif page == "Reports":

    st.header("📑 Reports Center")

    st.metric(
        "Similarity Score",
        f"{similarity_result['similarity_percentage']}%"
    )

    if st.button("Generate PDF Report"):

        avg_score = (
            similarity_result["similarity_percentage"]
            + winnow_score
            + minhash_score
        ) / 3

        if avg_score < 30:
            risk = "Low Risk"
        elif avg_score < 60:
            risk = "Moderate Risk"
        elif avg_score < 80:
            risk = "High Risk"
        else:
            risk = "Critical Risk"

        ReportGenerator.generate_report(
            "reports/generated_reports/plagiarism_report.pdf",
            similarity_result["similarity_percentage"],
            winnow_score,
            minhash_score,
            risk
        )

        st.success("✅ PDF Report Generated")