from sqlalchemy.orm import sessionmaker
import csv
import quiz_db as qdb

# Create a session
Session = sessionmaker(bind=qdb.engine)
session = Session()

# # Export the "questions" table to a CSV file
# output_questions = "questions.csv"
# with open(output_questions, "w", newline="", encoding="utf-8") as csvfile:
#     writer = csv.writer(csvfile)
#     # Write the header
#     writer.writerow(["id", "question_text", "question_type", "category"])
#     # Write the data
#     questions = session.query(qdb.QuestionDB).all()
#     for question in questions:
#         writer.writerow([question.id, question.question_text, question.question_type, question.category])

# print(f"Table 'questions' exported to {output_questions}")


# output_questions = "true_false.csv"
# with open(output_questions, "w", newline="", encoding="utf-8") as csvfile:
#     writer = csv.writer(csvfile)
#     # Write the header
#     writer.writerow(["id", "answer", "question_id"])
#     # Write the data
#     questions = session.query(qdb.TrueFalseQuestionDB).all()
#     for question in questions:
#         writer.writerow([question.id, question.answer, question.question_id])

# print(f"Table 'true_false' exported to {output_questions}")


# output_questions = "multiple_choice.csv"
# with open(output_questions, "w", newline="", encoding="utf-8") as csvfile:
#     writer = csv.writer(csvfile)
#     # Write the header
#     writer.writerow(["id", "a", "b", "c", "d", "answer" "question_id"])
#     # Write the data
#     questions = session.query(qdb.MultipleChoiceQuestionDB).all()
#     for question in questions:
#         writer.writerow([question.id, question.a, question.b, question.c, question.d, question.answer, question.question_id])

# print(f"Table 'multiple_choice' exported to {output_questions}")


# output_questions = "fill_in_questions.csv"
# with open(output_questions, "w", newline="", encoding="utf-8") as csvfile:
#     writer = csv.writer(csvfile)
#     # Write the header
#     writer.writerow(["id", "answer", "question_id"])
#     # Write the data
#     questions = session.query(qdb.FillInQuestionDB).all()
#     for question in questions:
#         writer.writerow([question.id, question.answer, question.question_id])

# print(f"Table 'fill_in_questions' exported to {output_questions}")


# output_questions = "short_answer_questions.csv"
# with open(output_questions, "w", newline="", encoding="utf-8") as csvfile:
#     writer = csv.writer(csvfile)
#     # Write the header
#     writer.writerow(["id", "answer", "question_id"])
#     # Write the data
#     questions = session.query(qdb.ShortAnswerQuestionDB).all()
#     for question in questions:
#         writer.writerow([question.id, question.answer, question.question_id])

# print(f"Table 'short_answer_questions' exported to {output_questions}")

# # Close the session
# session.close()



# Path to the CSV file
csv_questions_path = "c:/Users/vesi/Desktop/Python/Course/Projects/GeneralKnowledgeQuiz/source/Database/questions.csv"
csv_true_false_path = "c:/Users/vesi/Desktop/Python/Course/Projects/GeneralKnowledgeQuiz/source/Database/true_false.csv"
csv_multiple_choice_path = "c:/Users/vesi/Desktop/Python/Course/Projects/GeneralKnowledgeQuiz/source/Database/multiple_choice.csv"
csv_fill_in_path = "c:/Users/vesi/Desktop/Python/Course/Projects/GeneralKnowledgeQuiz/source/Database/fill_in_questions.csv"
csv_short_answer_path = "c:/Users/vesi/Desktop/Python/Course/Projects/GeneralKnowledgeQuiz/source/Database/short_answer_questions.csv"

# Import the CSV data into the questions table
# with open(csv_questions_path, "r", encoding="utf-8") as csvfile:
#     reader = csv.DictReader(csvfile)  # Use DictReader to map column names to values
#     for row in reader:
#         # Create a QuestionDB object for each row
#         question = qdb.QuestionDB(
#             id=int(row["id"]),
#             question_text=row["question_text"],
#             question_type=row["question_type"],
#             category=row["category"],
#             difficulty=row["difficulty"]
#         )
#         session.add(question)  # Add the object to the session

# # Commit the session to save the data to the database
# session.commit()


# with open(csv_true_false_path, "r", encoding="utf-8") as csvfile:
#     reader = csv.DictReader(csvfile)  # Use DictReader to map column names to values
#     for row in reader:
#         # Create a QuestionDB object for each row
#         question = qdb.TrueFalseQuestionDB(
#             id=int(row["id"]),
#             answer=row["answer"],
#             question_id=row["question_id"]
#         )
#         session.add(question)  # Add the object to the session

# # Commit the session to save the data to the database
# session.commit()
# print("Data imported successfully!")



# with open(csv_multiple_choice_path, "r", encoding="utf-8") as csvfile:
#     reader = csv.DictReader(csvfile)  # Use DictReader to map column names to values
#     for row in reader:
#         # Create a QuestionDB object for each row
#         question = qdb.MultipleChoiceQuestionDB(
#             id=int(row["id"]),
#             a=row["a"],
#             b=row["b"],
#             c=row["c"],
#             d=row["d"],
#             answer=row["answer"],
#             question_id=row["question_id"]
#         )
#         session.add(question)  # Add the object to the session

# # Commit the session to save the data to the database
# session.commit()
# print("Data imported successfully!")



# with open(csv_fill_in_path, "r", encoding="utf-8") as csvfile:
#     reader = csv.DictReader(csvfile)  # Use DictReader to map column names to values
#     for row in reader:
#         # Create a QuestionDB object for each row
#         question = qdb.FillInQuestionDB(
#             id=int(row["id"]),
#             answer=row["answer"],
#             question_id=row["question_id"]
#         )
#         session.add(question)  # Add the object to the session

# # Commit the session to save the data to the database
# session.commit()
# print("Data imported successfully!")



# with open(csv_short_answer_path, "r", encoding="utf-8") as csvfile:
#     reader = csv.DictReader(csvfile)  # Use DictReader to map column names to values
#     for row in reader:
#         # Create a QuestionDB object for each row
#         question = qdb.ShortAnswerQuestionDB(
#             id=int(row["id"]),
#             answer=row["answer"],
#             question_id=row["question_id"]
#         )
#         session.add(question)  # Add the object to the session

# # Commit the session to save the data to the database
# session.commit()
# print("Data imported successfully!")

# # Close the session
# session.close()