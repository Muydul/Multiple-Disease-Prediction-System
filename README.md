# 🫀 Heart Disease Prediction Using Machine Learning

This project predicts the likelihood of heart disease in a patient based on clinical parameters using various machine learning models.

## 🚀 Features

- Trained multiple models including:
  - Logistic Regression (with and without regularization)
  - Support Vector Machine (SVM)
  - Gradient Boosting
  - Stacking Classifier (Logistic Regression, KNN, Decision Tree → SVC)
- Achieved **85% accuracy** with optimized Stacking Classifier
- Model evaluation using precision, recall, F1-score, confusion matrix, and accuracy
- Built an end-to-end prediction pipeline
- Exported final model using `Pickle`
- Streamlit interface for real-time predictions

## 🛠️ Tech Stack

- Python
- Pandas, NumPy
- Scikit-learn
- Matplotlib
- Streamlit

## 📁 Files

| File                        | Description                              |
|-----------------------------|------------------------------------------|
| `Heart_Disease_Prediction.ipynb` | Main model development notebook       |
| `Mul_Disease_pred.py`       | Streamlit script for app UI             |
| `heart.csv`                 | Dataset containing patient health data  |
| `heart_model.sav`           | Final trained and saved ML model        |
| `streamlit run command.txt` | Quick command to launch the app         |
| `README.md`                 | Project overview and instructions       |

## 📊 Model Performance

| Model                      | Accuracy |
|---------------------------|----------|
| Logistic Regression        | 82%      |
| SVM                        | ~82%     |
| Gradient Boosting          | ~84%     |
| **Stacking Classifier**    | **85%**  |

## 🧪 Example Input

```python
input_data = (49, 1, 2, 120, 188, 0, 1, 139, 0, 2, 1, 3, 3)




## 🖥️ Run Locally

1. Clone the repository
2. Install dependencies
   ```bash
   pip install pandas numpy scikit-learn matplotlib streamlit



## 🖥️ Run Locally

1. Clone the repository
2. Install dependencies
   ```bash
   pip install pandas numpy scikit-learn matplotlib streamlit
