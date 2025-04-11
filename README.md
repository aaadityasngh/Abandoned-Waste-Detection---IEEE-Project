# Abandoned Waste Detection - IEEE Project

This is a YOLOv8-based real-time detection system that segments and logs abandoned waste (plastic bags, bottles, cans, etc.) from video streams.

---

## 📋 Table of Contents

- [Abandoned Waste Detection - IEEE Project](#abandoned-waste-detection---ieee-project)
  - [📋 Table of Contents](#-table-of-contents)
  - [📖 About the Project](#-about-the-project)
  - [✨ Features](#-features)
  - [🚀 Getting Started](#-getting-started)
    - [Prerequisites](#prerequisites)
    - [Installation](#installation)
  - [🔧 How to Run](#-how-to-run)
  - [📂 Project Structure](#-project-structure)
  - [🛠️ Technologies Used](#️-technologies-used)
  - [🤝 Contributing](#-contributing)
  - [📜 License](#-license)
  - [🙏 Acknowledgements](#-acknowledgements)
  - [👨‍💻 Made and Developed By](#-made-and-developed-by)

---

## 📖 About the Project

Abandoned waste is a growing environmental concern. This project leverages the power of YOLOv8 to detect and segment waste in real-time from video streams. The system is designed to assist in waste management and environmental monitoring.

---

## ✨ Features

- **Real-Time Detection**: Detects waste objects like plastic bags, bottles, and cans in real-time.
- **Segmentation**: Segments detected objects for better visualization.
- **Dashboard**: Interactive dashboard to view and analyze results.
- **Logging**: Logs detected waste for further analysis.

---

## 🚀 Getting Started

Follow these instructions to set up and run the project on your local machine.

### Prerequisites

- Python 3.8 or higher
- pip (Python package manager)

### Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/abandoned-waste-detection.git
   cd abandoned-waste-detection
   ```

2. Set up a virtual environment:
   ```bash
   python -m venv venv
   venv\Scripts\activate  # On Windows
   # or
   source venv/bin/activate  # On macOS/Linux
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

---

## 🔧 How to Run

1. **Run Detection**:
   ```bash
   python detect.py
   ```

2. **View Dashboard**:
   ```bash
   streamlit run dashboard.py
   ```

3. **Analyze Results**:
   - Open the Streamlit dashboard in your browser to view and analyze the detection results.

---

## 📂 Project Structure

```
├── dashboard.py         # Streamlit dashboard for visualization
├── detect.py            # Main detection script
├── requirements.txt     # Python dependencies
├── sample_video.mp4     # Sample video for testing
├── utils.py             # Utility functions
├── assets/              # Additional assets
├── model/               # Pre-trained YOLOv8 model
├── runs/                # Detection results
```

---

## 🛠️ Technologies Used

- **YOLOv8**: For object detection and segmentation
- **Streamlit**: For building the interactive dashboard
- **Python**: Core programming language

---

## 🤝 Contributing

Contributions are welcome! If you have suggestions for improvements, please fork the repository and create a pull request.

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

---

## 📜 License

This project is licensed under the MIT License. See the `LICENSE` file for details.

---

## 🙏 Acknowledgements

- [Ultralytics](https://ultralytics.com/) for YOLOv8
- [Streamlit](https://streamlit.io/) for the dashboard framework

---

## 👨‍💻 Made and Developed By

**Aditya Singh**

Feel free to connect with me on [LinkedIn](https://www.linkedin.com/) or check out my other projects on [GitHub](https://github.com/your-username).
