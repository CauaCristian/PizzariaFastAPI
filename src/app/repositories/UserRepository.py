import os
import sys

from sqlalchemy.exc import SQLAlchemyError

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from src.app.models.UserModel import UserModel
from src.core.database.Database import init_session

def get_user_by_email(email: str):
    session = init_session()
    try :
        return session.query(UserModel).filter_by(email=email).first()
    except SQLAlchemyError as e:
        session.rollback()
        raise SQLAlchemyError(f"Erro ao buscar usuário por email: {e}")
    finally:
        session.close()

def save_user(user: UserModel):
    session = init_session()
    try:
        session.add(user)
        session.commit()
        session.refresh(user)
        return user
    except SQLAlchemyError as e:
        session.rollback()
        raise SQLAlchemyError(f"Erro ao salvar usuário: {e}")
    finally:
        session.close()

def update_user(user: UserModel):
    session = init_session()
    try:
        session.merge(user)
        session.commit()
        session.refresh(user)
        return user
    except SQLAlchemyError as e:
        session.rollback()
        raise SQLAlchemyError(f"Erro ao atualizar usuário: {e}")
    finally:
        session.close()

def delete_user(user: UserModel):
    session = init_session()
    try:
        session.delete(user)
        session.commit()
    except SQLAlchemyError as e:
        session.rollback()
        raise SQLAlchemyError(f"Erro ao deletar usuário: {e}")
    finally:
        session.close()