from src.dao.base import BaseDAO
from src.models.models import Fact


class FactDAO(BaseDAO):
    model = Fact
