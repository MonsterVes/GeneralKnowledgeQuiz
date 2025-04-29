from sqlalchemy import Column, Integer, String, ForeignKey, create_engine
from sqlalchemy.orm import declarative_base


engine = create_engine('sqlite:///quiz.db')

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
    a = Column(String, nullable = False)
    b = Column(String, nullable = False)
    c = Column(String, nullable = False)
    d = Column(String, nullable = False)
    answer = Column(String, nullable = False)

class FillInQuestionDB(QuestionDB):
    __tablename__ = "fill_in_questions"
    id = Column(Integer, ForeignKey("questions.id"), primary_key = True)
    answer = Column(String, nullable = False)

class ShortAnswerQuestionDB(QuestionDB):
    __tablename__ = "short_answer_questions"
    id = Column(Integer, ForeignKey("questions.id"), primary_key = True)
    answer = Column(String, nullable = False)


Base.metadata.create_all(engine)


