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
    try:
        headers = table.__table__.columns.keys()
        query = session.query(*[getattr(table, col) for col in headers]).all()
        file_path =os.path.join(export_folder, filename)
        with open(file_path, "w", newline = "", encoding = "utf-8") as file:
            writer = csv.writer(file)
            writer.writerow(headers)
            writer.writerows(query)

            print(f"{table.__tablename__} exported to {file_path}")

        print(f"\n{filename} was exported successfully!\n")
    except Exception as e:
        print(f"Error while exporting {filename}:\n{e}.")
    finally:
        session.close()
        
# export_table_to_csv(qdb.QuestionDB,"questions.csv")
# export_table_to_csv(qdb.TrueFalseQuestionDB,"true_false.csv")
# export_table_to_csv(qdb.MultipleChoiceQuestionDB,"multiple_choice.csv")
# export_table_to_csv(qdb.FillInQuestionDB,"fill_in_questions.csv")
# export_table_to_csv(qdb.ShortAnswerQuestionDB,"short_answer.csv")



import_folder = "c:/Users/vesi/Desktop/Python/Course/Projects/GeneralKnowledgeQuiz/source/Database/DB_imports"

def import_table_from_csv(table, filename):
    """Imports csv file from DB_Imports to respective table in 'quiz.db'"""
    try:
        csv_file_path = os.path.join(import_folder, filename)
        headers = table.__table__.columns.keys()
        with open(csv_file_path, "r", encoding = "utf-8") as file:
            reader = csv.DictReader(file)
            for row in reader:
                table_row = table(**{col:row[col] for col in headers})
                session.add(table_row)
                
                session.commit()
        print(f"{filename} imported successfully into {table.__tablename__}! ")
    except Exception as e:
        print(f"Error while importing data from {filename} into {table.__tablename__}!:\n{e}.")
        session.rollback()
    finally:
        session.close()


# import_table_from_csv(qdb.QuestionDB, "questions.csv")
# import_table_from_csv(qdb.TrueFalseQuestionDB,"true_false.csv")
# import_table_from_csv(qdb.MultipleChoiceQuestionDB,"multiple_choice.csv")
# import_table_from_csv(qdb.FillInQuestionDB,"fill_in_questions.csv")
# import_table_from_csv(qdb.ShortAnswerQuestionDB,"short_answer.csv")






