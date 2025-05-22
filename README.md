# 🐶 Dog Emotion Prediction Using Deep Learning

This project uses a **transfer learning model** (MobileNetV2) to classify **dog emotions** from images. It predicts whether a dog looks **happy**, **angry**, **sad**, or **relaxed**. A simple **Streamlit** web interface allows users to upload an image and get real-time predictions.

---

## 🚀 Features

- ✅ Image classification using MobileNetV2 (pretrained on ImageNet)
- ✅ Achieved ~70% validation accuracy with real-world dog emotion data
- ✅ Image augmentation to improve generalization
- ✅ Streamlit UI for image upload and prediction
- ✅ Displays predicted emotion and confidence score

---

## 📁 Project Structure

``` 
📦Dog Emotion Prediction/
├── app.py # Streamlit web app
├── dog_emotion_model.h5 # Trained model (or .keras)
├── dog_emotion.ipynb # Model training and evaluation notebook
├── requirements.txt # Python dependencies
├── README.md # Project documentation
└── ...
```

---

## 🎓 Emotions Detected

The model can predict the following emotions:

- 😠 Angry  
- 😃 Happy  
- 😌 Relaxed  
- 😢 Sad  

---

## 🧠 Model Training Summary

- **Base Model**: MobileNetV2 (frozen layers)
- **Input Size**: 224x224 RGB images
- **Augmentation**: rotation, zoom, shift, shear, flip
- **Optimizer**: Adam  
- **Loss**: Categorical Crossentropy  
- **Accuracy**: ~70% (validation)  
- **Format**: Saved in `.h5` or `.keras` for deployment

---

## 🔧 Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/dog-emotion-predictor.git
cd dog-emotion-predictor
```

### 2. Run the Streamlit App
```bash
streamlit run app.py
```
In terminal or cmd.

---

## 📸 Using the App

1. Upload a dog image (JPG/PNG).

2. Click the Check Emotion button.

3. The app will display:

 - 🎯 Predicted emotion

 - 📊 Confidence score

---

## 🧪 Example Output

| Input Image | Predicted Emotion | Confidence |
| ----------- | ----------------- | ---------- |
| 🐶          | Happy             | 0.92       |

---

## 📦 Requirements

- **tensorflow**
- **numpy**
- **streamlit**
- **Pandas**

---

## 📄 License
This project is licensed under the MIT License — feel free to use, modify, and share!

--- 
Feel Free to make changes and if you want to add more features on this.



