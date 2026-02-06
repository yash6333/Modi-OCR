# Modi OCR – Character Recognition

A machine learning project to recognize individual **Modi Lipi characters** from images and map them to their corresponding **Marathi / Devanagari characters**.

This project focuses on **character-level OCR** (Optical Character Recognition) as a foundation for future work on full-text recognition and transliteration.

---

## 🎯 Project Goal

The goal of this project is to:

- Build a clean and reliable **image → character** recognition pipeline
- Learn and apply **computer vision + deep learning** concepts
- Create a solid base that can later be extended to:
  - Word-level OCR
  - Sentence-level OCR
  - Transliteration to Devanagari

---

## 🛠 Tech Stack

- **Language**: Python 3
- **Libraries**:
  - PyTorch
  - Torchvision
  - OpenCV
  - NumPy
  - Matplotlib
- **Version Control**: Git + GitHub
- **IDE**: VS Code
- **Environment**: Python Virtual Environment (`venv`)

---

## 📂 Project Structure

modi-ocr/
├── data/
│ └── raw/ # Dataset (NOT tracked by Git)
├── src/
│ ├── dataset.py # Dataset loading logic
│ ├── model.py # Neural network architecture
│ ├── train.py # Training loop
│ └── evaluate.py # Evaluation logic
├── requirements.txt # Python dependencies
├── README.md
└── .gitignore


> Note: The `data/` directory is intentionally excluded from Git to keep the repository lightweight.

---

## 📊 Dataset

This project uses the **Modi Script Character Images Dataset (with Marathi)** from Kaggle.

- **Dataset link**:  
  https://www.kaggle.com/datasets/nileshrugge/modi-script-character-images-dataset-with-marathi

### Dataset Setup Instructions

1. Download the dataset from Kaggle
2. Extract the ZIP file
3. Place the extracted folder inside:

data/raw/modi-script-character-images-dataset-with-marathi/
├── क/
├── ख/
├── ग/
├── ...


Do **not** rename class folders or images.

---

## ⚙️ Setup Instructions

### 1️⃣ Clone the repository

```bash
git clone <your-repo-url>
cd modi-ocr

python -m venv venv
source venv/Scripts/activate   # Windows (Git Bash)

pip install -r requirements.txt
