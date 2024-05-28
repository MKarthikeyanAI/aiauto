import nltk
import difflib

# Ensure you have the necessary NLTK resources
nltk.download('punkt')

# Predefined database of texts
database_texts = [
    "This is a sample document used to check for plagiarism.",
    "Another example text in the database for plagiarism checking.",
    "The quick brown fox jumps over the lazy dog.",
    "Data science is an interdisciplinary field focused on extracting knowledge from data sets.",
    "Machine learning is a method of data analysis that automates analytical model building."
]

def get_tokens(text):
    # Tokenize the text into words and convert to lowercase
    tokens = text.split()
    tokens = [token.lower() for token in tokens]
    return tokens

def calculate_similarity(text1, text2):
    # Calculate similarity ratio using difflib
    seq = difflib.SequenceMatcher(None, text1, text2)
    return seq.ratio() * 100

def check_plagiarism(input_text):
    similarity_results = []
    input_tokens = get_tokens(input_text)
    
    for db_text in database_texts:
        db_tokens = get_tokens(db_text)
        similarity = calculate_similarity(" ".join(input_tokens), " ".join(db_tokens))
        similarity_results.append((similarity, db_text))
    
    return similarity_results

def main():
    # Prompting user to input the text to be checked for plagiarism
    input_text = input("Enter the text to be checked for plagiarism: ").strip()
    
    # Call the check_plagiarism function
    results = check_plagiarism(input_text)
    
    # Display the list of similarity percentages and corresponding texts
    print("\nSimilarity Results:")
    for similarity, db_text in results:
        print(f"Similarity: {similarity:.2f}% with the following text: \n{db_text}\n")

if __name__ == "__main__":
    main()
