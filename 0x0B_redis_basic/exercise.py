#!/usr/bin/env python3
"""
Module pour gérer le cache Redis
"""
import redis
import uuid
from typing import Union


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

        Args:
            data (Union[str, bytes, int, float]): Les données à stocker

        Returns:
            str: La clé unique associée aux données stockées
        """
        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return key
