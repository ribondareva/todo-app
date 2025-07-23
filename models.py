from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column, Integer, String, Boolean  # Явный импорт типов

db = SQLAlchemy()


class Task(db.Model):
    __tablename__ = 'task'

    id = Column(Integer, primary_key=True)
    title = Column(String(100), nullable=False)
    done = Column(Boolean, default=False)
    priority = Column(Integer, default=1)

    def __repr__(self):
        return f'<Task {self.id}: {self.title}>'