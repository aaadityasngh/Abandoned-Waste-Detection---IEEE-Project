import streamlit as st
import os
from detect_core import run_detection
from report_generator import generate_pdf
import json
import base64

st.set_page_config(page_title="Waste Detection Demo", layout="wide")
st.title("🧠 Abandoned Waste Detection Dashboard")

video_path = "sample_video.mp4"
output_path = "runs/results/output.mp4"
frame_path = "assets/sample-frame.png"
log_path = "runs/results/log.json"

st.markdown("## 📤 Upload Video for Segmentation")
uploaded_file = st.file_uploader("Upload MP4 Video", type=["mp4"])

if uploaded_file is not None:
    with open(video_path, "wb") as f:
        f.write(uploaded_file.read())
    st.success("✅ Video uploaded successfully!")

    if st.button("▶️ Start Detection"):
        st.info("Running segmentation... please wait ⏳")
        run_detection(video_path, output_path, frame_path, log_path)
        st.success("✅ Segmentation Complete!")

# Show video output
st.subheader("🎥 Segmented Video Output")

if os.path.exists(output_path):
    with open(output_path, "rb") as f:
        video_bytes = f.read()
    st.download_button("📥 Download Output Video", video_bytes, file_name="segmented_output.mp4")
    st.video(video_bytes)
else:
    st.info("No output video yet.")

# Show frame
st.subheader("🖼️ Detected Frame Snapshot")
if os.path.exists(frame_path):
    st.image(frame_path, use_column_width=True)

# Show logs
st.subheader("📜 Detection Logs")
if os.path.exists(log_path):
    with open(log_path) as f:
        logs = json.load(f)
    st.dataframe(logs)

    from collections import Counter
    all_items = [item for log in logs for item in log["detected_items"]]
    st.subheader("📊 Waste Class Summary")
    st.json(dict(Counter(all_items)))

    st.download_button("📥 Download Log JSON", json.dumps(logs), file_name="log.json")

# Report
st.subheader("📄 Generate PDF Report")
if st.button("🖨️ Create Report"):
    report_path = "runs/results/report.pdf"
    if generate_pdf(log_path, report_path):
        with open(report_path, "rb") as f:
            b64 = base64.b64encode(f.read()).decode()
            link = f'<a href="data:application/pdf;base64,{b64}" download="waste_report.pdf">📥 Download Report</a>'
            st.markdown(link, unsafe_allow_html=True)
    else:
        st.error("❌ Failed to generate report.")
