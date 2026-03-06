🏅 Para Sports Recommendation System using Pose Estimation

An AI-based system that analyzes human body posture from images and videos and recommends suitable para sports based on limb functionality. The system uses pose estimation to detect body landmarks and determine physical capability, promoting inclusive participation in sports.

📌 Features

Human pose detection using MediaPipe Pose Landmarker

Extracts 33 body landmarks

Skeleton and joint visualization

Supports image and video input

Para sports recommendation based on limb activity

Interactive Streamlit web application

🛠️ Tech Stack

Python

MediaPipe

OpenCV

Streamlit

NumPy

Computer Vision

🧠 How It Works

User uploads an image or video

MediaPipe Pose Landmarker detects human body landmarks

Limb visibility and joint connections are analyzed

Physical capability is classified (e.g., one_leg, one_arm, all_active)

Suitable para sports are recommended

📂 Project Structure
para-sports-recommendation/
│
├── app.py
├── pose_landmarker_lite.task
├── requirements.txt
└── README.md
▶️ How to Run the Project
1️⃣ Clone the repository
git clone https://github.com/your-username/para-sports-recommendation.git
2️⃣ Navigate to project folder
cd para-sports-recommendation
3️⃣ Create virtual environment
python -m venv venv

Activate environment:

venv\Scripts\activate
4️⃣ Install dependencies
pip install -r requirements.txt
5️⃣ Run Streamlit app
streamlit run app.py
📊 Output

The system provides:

Pose skeleton visualization

Limb activity analysis

Recommended para sports list


🎓 Academic Purpose

This project was developed as part of a final year academic project focusing on AI, Computer Vision, and assistive technology for inclusive sports.
