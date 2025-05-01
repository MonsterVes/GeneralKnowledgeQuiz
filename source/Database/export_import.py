from sqlalchemy.orm import sessionmaker
import os
import csv
import quiz_db as qdb


Session = sessionmaker(bind=qdb.engine)
session = Session()

export_folder = "c:/Users/vesi/Desktop/Python/Course/Projects/GeneralKnowledgeQuiz/source/Database/DB_exports"
os.makedirs(export_folder, exist_ok=True)


def export_table_to_csv(table, filename):
    """Exports any given table from 'quiz.db' to an scv file, saved in DB_exports folder"""
    headers = table.__table__.columns.keys()
    query = session.query(*[getattr(table, col) for col in headers]).all()
    file_path =os.path.join(export_folder, filename)

    with open(file_path, "w", newline = "", encoding = "utf-8") as file:
        writer = csv.writer(file)
        writer.writerow(headers)
        writer.writerows(query)

        print(f"{table.__tablename__} exported to {file_path}")

session.close()

# export_table_to_csv(qdb.QuestionDB,"questions.csv")




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