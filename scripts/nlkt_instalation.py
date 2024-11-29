import nltk

# Path to download nltk_data inside the venv
nltk_data_path = r'C:\Users\camii\Documents\U\Term 1\Term 1\Data Analytics\Project\Airplane_Accidents_Analytics\venv\nltk_data'

# Download required resources
nltk.download('punkt', download_dir=nltk_data_path)
nltk.download('stopwords', download_dir=nltk_data_path)

print("NLTK data has been successfully installed inside the venv.")
