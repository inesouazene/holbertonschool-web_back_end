#!/usr/bin/env python3
"""
Module pour gérer le cache Redis
"""
import redis
import uuid
from typing import Union, Callable, Optional
from functools import wraps


def count_calls(method: Callable) -> Callable:
    """
    Décorateur pour compter le nombre d'appels à une méthode
    """
    @wraps(method)
    def wrapper(self, *args, **kwargs):
        """
        Fonction qui incrémente le compteur d'appels puis appelle la méthode
        """
        key = method.__qualname__
        self._redis.incr(key)
        return method(self, *args, **kwargs)
    return wrapper


def call_history(method: Callable) -> Callable:
    """
    Décorateur pour enregistrer l'historique des
    entrées et sorties d'une fonction
    """
    @wraps(method)
    def wrapper(self, *args, **kwargs):
        """
        Fonction qui enregistre les arguments et le résultat de la méthode
        """
        # clés pour les entrées et sorties
        input_key = f"{method.__qualname__}:inputs"
        output_key = f"{method.__qualname__}:outputs"

        # enregistrer les arguments
        self._redis.rpush(input_key, str(args))

        result = method(self, *args, **kwargs)  # exécuter la méthode

        # enregistrer le résultat
        self._redis.rpush(output_key, str(result))

        return result
    return wrapper


def replay(method: Callable) -> None:
    """
    Affiche l'historique des appels d'une méthode
    """
    redis_instance = method.__self__._redis
    # créer les clés pour les entrées et sorties
    method_name = method.__qualname__
    input_key = f"{method_name}:inputs"
    output_key = f"{method_name}:outputs"

    # récupérer le nombre d'appels
    call_count = redis_instance.get(method_name)

    if call_count is None:
        call_count = 0
    else:
        call_count = int(call_count)

    print(f"{method_name} was called {call_count} times:")

    # récupérer les entrées et sorties
    inputs = redis_instance.lrange(input_key, 0, -1)
    outputs = redis_instance.lrange(output_key, 0, -1)

    # parcourir les entrées et sorties et les afficher
    for inp, out in zip(inputs, outputs):
        input_str = inp.decode('utf-8')
        output_str = out.decode('utf-8')
        print(f"{method_name}(*{input_str}) -> {output_str}")


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

    @count_calls
    @call_history
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
