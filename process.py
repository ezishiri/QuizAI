

def grade_answers(answers, questions):
    """Grade the user's answers to the questions.

    Args:
        answers (list): The user's answers to the questions.
        questions (list): The questions to be answered.

    Returns:
        int: The number of correct answers.
    """
    # Create a variable to store the number of correct answers
    score = 0
    # Loop through each question in the questions list
    for answer in answers:
        score += 1 #for now, just add 1 to the score for each question
    # Return the score
    return score
