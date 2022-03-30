from fastapi import APIRouter

router = APIRouter()


@router.post('/v1/classify_text/', tags=['main'])
def analysis_from_text():
    """Отправка текста в чистом виде"""
    return ''


@router.post('/v1/classify_url/', tags=['main'])
def analysis_from_url():
    """Вытаскивание текста из адреса"""
    return ''
