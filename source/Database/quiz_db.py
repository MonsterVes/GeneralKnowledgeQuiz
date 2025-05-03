from sqlalchemy import Column, Integer, String, ForeignKey, create_engine
from sqlalchemy.orm import declarative_base, relationship
import os


db_folder = os.path.dirname(__file__)  
db_path = os.path.join(db_folder, 'quiz.db')  

engine = create_engine(f'sqlite:///{db_path}')

Base = declarative_base()


class QuestionDB(Base):
    __tablename__ = "questions"
    id = Column(Integer, primary_key=True)
    question_text = Column(String, nullable = False)
    question_type = Column(String, nullable = False)
    category = Column(String, nullable = False)
    difficulty = Column(String, nullable = False)
    true_false = relationship("TrueFalseQuestionDB", back_populates = "question", uselist = False)
    multiple_choice = relationship("MultipleChoiceQuestionDB", back_populates = "question", uselist = False)
    fill_in = relationship("FillInQuestionDB", back_populates = "question", uselist = False)
    short_answer = relationship("ShortAnswerQuestionDB", back_populates = "question", uselist = False)

    def __str__(self):
        return f"ID: {self.id}, Text: {self.question_text}, Type: {self.question_type}, Category: {self.category}"

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


