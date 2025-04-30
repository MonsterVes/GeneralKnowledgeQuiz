from sqlalchemy import Column, Integer, String, ForeignKey, create_engine
from sqlalchemy.orm import declarative_base, relationship
import os

# cwd = os.path()
# print(cwd)

db_folder = os.path.dirname(__file__)  # This gets the current file's directory
db_path = os.path.join(db_folder, 'quiz.db')  # Create the full path to quiz.db

# Create the SQLite engine with the correct path
engine = create_engine(f'sqlite:///{db_path}')

Base = declarative_base()


class QuestionDB(Base):
    __tablename__ = "questions"
    id = Column(Integer, primary_key=True)
    question_text = Column(String, nullable = False)
    question_type = Column(String, nullable = False)
    category = Column(String, nullable = False)
    true_false = relationship("TrueFalseQuestionDB", back_populates = "question", uselist = False)
    multiple_choice = relationship("MultipleChoiceQuestionDB", back_populates = "question", uselist = False)
    fill_in = relationship("FillInQuestionDB", back_populates = "question", uselist = False)
    short_answer = relationship("ShortAnswerQuestionDB", back_populates = "question", uselist = False)

class TrueFalseQuestionDB(Base):
    __tablename__ = "true_false" 
    id = Column(Integer, primary_key = True)
    answer = Column(String, nullable = False)
    question_id = Column(Integer, ForeignKey("questions.id"), nullable = False)
    question = relationship("QuestionDB", back_populates = "true_false")

class MultipleChoiceQuestionDB(Base):
    __tablename__ = "multiple_choice"
    id = Column(Integer, primary_key = True)
    a = Column(String, nullable = False)
    b = Column(String, nullable = False)
    c = Column(String, nullable = False)
    d = Column(String, nullable = False)
    answer = Column(String, nullable = False)
    question_id = Column(Integer, ForeignKey("questions.id"), nullable = False)
    question = relationship("QuestionDB", back_populates = "multiple_choice")


class FillInQuestionDB(Base):
    __tablename__ = "fill_in_questions"
    id = Column(Integer,  primary_key = True)
    answer = Column(String, nullable = False)
    question_id = Column(Integer, ForeignKey("questions.id"), nullable = False)
    question = relationship("QuestionDB", back_populates = "fill_in")

class ShortAnswerQuestionDB(Base):
    __tablename__ = "short_answer_questions"
    id = Column(Integer, primary_key = True)
    answer = Column(String, nullable = False)
    question_id = Column(Integer, ForeignKey("questions.id"), nullable = False)
    question = relationship("QuestionDB", back_populates = "short_answer")


Base.metadata.create_all(engine)


