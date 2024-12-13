import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base() # todas las tablas reiben esta base

    # aqui definimos las columnas para la tabla personas 
class User(Base):
    __tablename__ = 'user'
    # esta columna recibe como parametro el tipo de datos(integer) que almacenara que es de tipo entero
    # y le pasamos el primary_key=True)  que hace referencia a que sera nuestra clave primaria 
    id = Column(Integer , primary_key=True) 
    # definimos una col username con tipo de dato string y de cantindad de caracteres seran 250max
    # el nullable nos indica si esa col puede ser o no null y la idea es que no sea vacia entonces es false, si quiero que sea null seria true
    username = Column(String(250), nullable=False)
    firstname = Column(String(250), nullable=False)
    lastname = Column(String(250), nullable=False)
    email = Column(String(250), nullable=False)



class Post(Base): 
    __tablename__ = 'post'
    # aqui definimos las columnas.
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.id')) # hacemos referencia a la columna de los id de los usuarios 
    post = relationship(User) # hacemos la conexion con la tabla 6Y75Y7T

class Media(Base):
      __tablename__ = 'base'
      id = Column(Integer , primary_key=True)
      type = Column(String(250),nullable=False)
      url = Column(String(250),nullable=False)
      post_id = Column(Integer, ForeignKey('post.id'))
      media = relationship(Post)

class Comment(Base):
      __tablename__ = 'comment'
      id = Column(Integer , primary_key=True)
      commrnet_text = Column(String(250),nullable=False)
      author_id = Column(Integer, ForeignKey('user.id'))
      post_id = Column(Integer, ForeignKey('post.id'))
      Comment = relationship(User, Post)



class Like(Base):
      __tablename__ = 'like'
      id = Column(Integer , primary_key=True)
      commrnet_text = Column(String(250),nullable=False)
      author_id = Column(Integer, ForeignKey('user.id'))
      post_id = Column(Integer, ForeignKey('post.id'))
      like = relationship (User, Post)



class Follow(Base):
      __tablename__ = 'follow'
      id =  Column(Integer , primary_key=True)
      user_from_id = Column(Integer, ForeignKey('user.id'))
      user_to_id = Column(Integer, ForeignKey('user.id'))
      like = relationship (User)



   # def to_dict(self):
        # return {}

## Draw from SQLAlchemy base
try:
    result = render_er(Base, 'diagram.png')
    print("Success! Check the diagram.png file")
except Exception as e:
    print("There was a problem genering the diagram")
    raise e
