import cv2
import streamlit as st
import numpy as np
import tempfile

# ---------------- PAGE CONFIG ----------------
st.set_page_config(
    page_title="Para Sports Recommendation",
    page_icon="🏅",
    layout="centered"
)

st.title("🏅 Para Sports Recommendation System")
st.caption("AI-inspired rule-based system (MediaPipe-free, Python compatible)")

# ---------------- SPORTS DATABASE ----------------
sports_recommendations = {
    "no_arms": [
        "Para Swimming",
        "Wheelchair Racing",
        "Para Athletics (Track)"
    ],
    "no_legs": [
        "Archery",
        "Shooting",
        "Boccia",
        "Table Tennis (Wheelchair)"
    ],
    "one_leg": [
        "Para Cycling",
        "Badminton (Standing)",
        "Para Canoe"
    ],
    "one_arm": [
        "Para Rowing",
        "Archery",
        "Cycling"
    ],
    "all_active": [
        "Para Athletics",
        "Para Triathlon",
        "Rowing",
        "Para Cycling"
    ]
}

# ---------------- CORE LOGIC ----------------
def analyze_body(image):
    """
    Simple OpenCV-based body region analysis
    Determines presence of upper and lower body
    """

    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    blur = cv2.GaussianBlur(gray, (5, 5), 0)

    _, thresh = cv2.threshold(
        blur, 60, 255, cv2.THRESH_BINARY_INV
    )

    contours, _ = cv2.findContours(
        thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE
    )

    height, width = image.shape[:2]
    upper_body = False
    lower_body = False

    for cnt in contours:
        area = cv2.contourArea(cnt)
        if area < 2000:
            continue

        x, y, w, h = cv2.boundingRect(cnt)

        # Upper body region
        if y < height * 0.5:
            upper_body = True

        # Lower body region
        if y >= height * 0.5:
            lower_body = True

    if not upper_body and lower_body:
        return "no_arms"
    elif upper_body and not lower_body:
        return "no_legs"
    elif upper_body and lower_body:
        return "all_active"
    else:
        return None

def process_image(image):
    return analyze_body(image)

def process_video(video_path):
    cap = cv2.VideoCapture(video_path)
    detected = []

    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break

        category = analyze_body(frame)
        if category:
            detected.append(category)

    cap.release()

    if detected:
        return max(set(detected), key=detected.count)
    return None

# ---------------- INPUT UI ----------------
input_type = st.radio("Select Input Type", ["Image", "Video"])
category = None

if input_type == "Image":
    img_file = st.file_uploader(
        "Upload an Image",
        type=["jpg", "jpeg", "png"]
    )

    if img_file:
        image = cv2.imdecode(
            np.frombuffer(img_file.read(), np.uint8), 1
        )
        st.image(image, caption="Uploaded Image", channels="BGR")
        category = process_image(image)

elif input_type == "Video":
    vid_file = st.file_uploader(
        "Upload a Video",
        type=["mp4", "avi", "mov"]
    )

    if vid_file:
        temp_file = tempfile.NamedTemporaryFile(delete=False)
        temp_file.write(vid_file.read())
        category = process_video(temp_file.name)

# ---------------- OUTPUT ----------------
st.divider()

if category:
    st.success("🎯 Recommended Para Sports:")
    for sport in sports_recommendations[category]:
        st.write("✅", sport)
else:
    st.info("Please upload a clear full-body image or video.")
