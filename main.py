from transformers import pipeline
import question_generator
import jpg_url_to_lines

nlp = pipeline(
    "document-question-answering",
    model="impira/layoutlm-document-qa",
)

def get_answers(questions, image_url):
    answers = {}
    for question in questions:
        answers[question] = nlp(
            image_url,
            question,
        )
    return answers


# def main():
#     # from a jpg on the internet, generate lines of text
#     jpg_lines = jpg_url_to_lines.extract_text_from_image("https://images.squarespace-cdn.com/content/v1/601db7e8f17bd81808046163/1613164899105-QOEOYAF5NCHXHTAMHBGN/2021_MJ_Offen_Resume-P1.jpg")
#     print(jpg_lines)
    
#     # get the context only questions from the lines
#     questions = question_generator.get_questions(jpg_lines)
#     print(questions)

#     # answer the questions
#     for question in questions:
#         print(nlp(
#             "https://images.squarespace-cdn.com/content/v1/601db7e8f17bd81808046163/1613164899105-QOEOYAF5NCHXHTAMHBGN/2021_MJ_Offen_Resume-P1.jpg",
#             question,
#         ))

# if __name__ == "__main__":
#     main()
