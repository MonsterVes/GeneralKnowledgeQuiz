from sqlalchemy import Column, Integer, String, ForeignKey, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()

class QuestionDB(Base):
    __tablename__ = "questions"
    id = Column(Integer, primary_key=True)
    question_text = Column(String, nullable = False)
    question_type = Column(String, nullable = False)
    category = Column(String, nullable = False)

class TrueFalseQuestionDB(QuestionDB):
    __tablename__ = "t_f_questions" 
    id = Column(Integer, ForeignKey("questions.id"), primary_key = True)
    answer = Column(String, nullable = False)

class MultipleChoiceQuestionDB(QuestionDB):
    __tablename__ = "multiple_choice"
    id = Column(Integer, ForeignKey("questions.id"), primary_key = True)


