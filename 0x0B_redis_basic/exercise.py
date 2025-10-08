#!/usr/bin/env python3
"""
Module pour gérer le cache Redis
"""
import redis
import uuid
from typing import Union, Callable, Optional


class Cache:
    """
    Classe Cache pour stocker des données dans Redis
    """

    def __init__(self):
        """
        Initialise une instance Redis et vide la base de données
        """
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: Union[str, bytes, int, float]) -> str:
        """
        Stocke les données dans Redis et retourne une clé unique
        """
        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return key

    def get(self, key: str, fn: Optional[Callable] =
            None) -> Union[str, bytes, int, float, None]:
        """
        Récupère les données liées à une clé et
        applique une fonction de conversion si fournie
        """
        data = self._redis.get(key)
        if data is None:
            return None
        if fn:
            return fn(data)
        return data

    def get_str(self, key: str) -> Optional[str]:
        """
        Récupère les données sous forme de chaîne de caractères
        """
        data = self._redis.get(key)
        if data is None:
            return None
        return data.decode('utf-8')

    def get_int(self, key: str) -> Optional[int]:
        """
        Récupère les données sous forme d'entier
        """
        data = self._redis.get(key)
        if data is None:
            return None
        try:
            return int(data)
        except ValueError:
            return None
