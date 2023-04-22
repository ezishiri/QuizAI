from transformers import AutoTokenizer, AutoModelForSeq2SeqLM

model_name = "voidful/context-only-question-generator"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForSeq2SeqLM.from_pretrained(model_name)



def get_questions(lines): 
    # Create an empty list to store the questions
    questions = []
    # Loop through each line in the list of lines
    for line in lines:
        # Encode the line using the tokenizer
        input_ids = tokenizer.encode(line, return_tensors="pt")
        # Generate the questions using the model
        generated_questions = model.generate(input_ids=input_ids)
        # Loop through each question
        for question in generated_questions:
            # Decode the question and add it to the list
            questions.append(tokenizer.decode(question, skip_special_tokens=True))
    # Return the list of questions
    return questions


# instead of a list of questions, return a dictionary of questions with the line as the key
def get_questions_dict(lines): 
    # Create an empty list to store the questions
    questions = {}
    # Loop through each line in the list of lines
    for line in lines:
        # Encode the line using the tokenizer
        input_ids = tokenizer.encode(line, return_tensors="pt")
        # Generate the questions using the model
        generated_questions = model.generate(input_ids=input_ids)
        # Loop through each question
        for question in generated_questions:
            # Decode the question and add it to the list
            questions[line] = tokenizer.decode(question, skip_special_tokens=True)
    # Return the list of questions
    return questions


