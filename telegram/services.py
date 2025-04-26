from models import User
from config_bd import get_session

def record_id_tg(phone: str, tg_id: int):
    """
    Функция для записи id телеграм
    """
    session = get_session()  # Получаем сессию
    user = session.query(User).filter(User.phone == phone).first()

    if user:
        user.tg_id = tg_id  # Обновляем tg_id
        session.commit()   # Фиксируем изменения в базе данны
        session.close()
        return f"Вы успешно зарегистрированы в системе!"
    else:
        session.close()
        return f"Пользователь с таким номером телефона не найден"




