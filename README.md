# 🚦 Traffic Violation Detection using YOLOv8 & YOLOv11

An intelligent computer vision system that detects traffic violations by identifying whether riders are wearing helmets and extracting license plate information using state-of-the-art YOLO models.

---

## 📌 Overview

This project leverages deep learning-based object detection to automate traffic monitoring. It classifies riders into:

- ✅ **With Helmet (SAFE)**
- ❌ **Without Helmet (PENALTY)**
- 🔢 **License Plate Detection**

Additionally, a comparative study between **YOLOv8** and **YOLOv11** is performed to evaluate real-world performance.

---

## 🎯 Features

- 🚀 Real-time object detection using YOLO
- 🪖 Helmet vs No-Helmet classification
- 🔍 License plate detection
- ⚖️ SAFE vs PENALTY decision system
- 🌐 Streamlit-based web interface
- 📊 Model comparison (YOLOv8 vs YOLOv11)
- 📈 Evaluation using PR curves, mAP, Precision, Recall

---

## 🧠 Models Used

- **YOLOv8**
- **YOLOv11**

Both models were trained under identical conditions for fair comparison.

---

## 📊 Results

| Model   | Precision | Recall | mAP@0.5 | mAP@0.5:0.95 |
|--------|----------|--------|---------|-------------|
| YOLOv8 | 0.836    | 0.819  | 0.864   | 0.520       |
| YOLOv11| 0.816    | 0.757  | 0.827   | 0.489       |

### 🔍 Key Insights
- YOLOv8 outperformed YOLOv11 across all metrics  
- License plate detection achieved highest accuracy  
- “Without Helmet” class remains challenging due to occlusion and variability  

---

## 📈 Evaluation Metrics

The models were evaluated using:

- Precision  
- Recall  
- mAP@0.5  
- mAP@0.5:0.95  
- Confusion Matrix  
- Precision-Recall Curve  

---

## 🖥️ Web Application (Streamlit)

A simple and interactive web interface allows users to:

- Upload traffic images  
- Detect violations in real-time  
- View annotated outputs  

### ▶️ Run the App

```bash
pip install -r requirements.txt
streamlit run app.py
