import nltk

# Ensure you have the necessary NLTK resources
nltk.download('punkt')

def get_tokens(text):
    tokens = text.split()
    tokens = [token.lower() for token in tokens]
    return tokens

def calculate_similarity(answer, correct_answer):
    answer_set = set(get_tokens(answer))
    correct_answer_set = set(get_tokens(correct_answer))
    similarity = 1 - nltk.jaccard_distance(answer_set, correct_answer_set)
    return similarity

def check_answers(correct_answers, student_answers):
    correct_count = 0
    incorrect_count = 0
    unanswered_count = 0
    total_similarity = 0

    for correct, student in zip(correct_answers, student_answers):
        if student == "":
            unanswered_count += 1
        else:
            similarity = calculate_similarity(student, correct)
            total_similarity += similarity
            if similarity == 1:
                correct_count += 1
            else:
                incorrect_count += 1
    
    score = (total_similarity / len(correct_answers)) * 100
    return score, correct_count, incorrect_count, unanswered_count

def main():
    # Prompting user to input correct answers
    correct_answers = []
    num_questions = int(input("Enter the number of questions: "))
    print("Enter the correct answers:")
    for _ in range(num_questions):
        correct_answer = input().strip()
        correct_answers.append(correct_answer)
    
    # Prompting user to input student's answers
    student_answers = []
    print("Enter the student's answers (leave blank if unanswered):")
    for _ in range(num_questions):
        student_answer = input().strip()
        student_answers.append(student_answer)
    
    # Check the answers
    score, correct_count, incorrect_count, unanswered_count = check_answers(correct_answers, student_answers)
    
    # Display results
    print(f"\nStudent's Score: {score:.2f}%")
    print(f"Correct Answers: {correct_count}")
    print(f"Incorrect Answers: {incorrect_count}")
    print(f"Unanswered Questions: {unanswered_count}")

if __name__ == "__main__":
    main()
