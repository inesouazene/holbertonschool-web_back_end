# Session Authentication

## Description

Ce projet implémente un système d'authentification par session pour une API REST Flask. Il s'agit d'un projet éducatif qui guide à travers chaque étape du mécanisme d'authentification par session pour en comprendre le fonctionnement interne.

**⚠️ Note importante :** En production, il est recommandé d'utiliser des modules ou frameworks existants (comme Flask-HTTPAuth) plutôt que d'implémenter son propre système d'authentification.

## Objectifs d'apprentissage

À la fin de ce projet, vous devriez être capable d'expliquer :

- Ce que signifie l'authentification
- Ce qu'est l'authentification par session
- Ce que sont les Cookies
- Comment envoyer des Cookies
- Comment parser les Cookies

## Technologies utilisées

- **Langage :** Python 3.9
- **Framework :** Flask
- **Environnement :** Ubuntu 20.04 LTS
- **Style de code :** pycodestyle (version 2.5)

## Structure du projet

```
Session_authentication/
├── README.md
├── api/
│   └── v1/
│       ├── app.py
│       ├── auth/
│       │   ├── auth.py
│       │   └── session_auth.py
│       └── views/
│           ├── __init__.py
│           ├── users.py
│           └── session_auth.py
└── models/
    └── user.py
```

## Fonctionnalités implémentées

### 1. Authentification basique étendue (Task 0)
- Ajout de l'endpoint `GET /users/me` pour récupérer l'utilisateur authentifié
- Support du paramètre spécial `me` dans les routes utilisateur

### 2. Classe SessionAuth (Task 1)
- Création d'une classe `SessionAuth` héritant de `Auth`
- Système de commutation d'authentification via la variable d'environnement `AUTH_TYPE`

### 3. Création de sessions (Task 2)
- Méthode `create_session()` pour générer des ID de session uniques
- Stockage en mémoire des associations user_id ↔ session_id

### 4. Récupération d'utilisateur par session (Task 3)
- Méthode `user_id_for_session_id()` pour retrouver un user_id depuis un session_id

### 5. Gestion des cookies (Task 4)
- Méthode `session_cookie()` pour extraire la valeur du cookie de session
- Support de la variable d'environnement `SESSION_NAME`

### 6. Validation des requêtes (Task 5)
- Mise à jour du middleware `before_request`
- Validation de l'autorisation par cookie ou header

### 7. Identification utilisateur par session (Task 6)
- Méthode `current_user()` pour récupérer un utilisateur via son cookie de session

### 8. Endpoint de connexion (Task 7)
- Route `POST /api/v1/auth_session/login` pour l'authentification
- Validation des credentials et création de session
- Définition automatique du cookie de session

### 9. Endpoint de déconnexion (Task 8)
- Route `DELETE /api/v1/auth_session/logout` pour la déconnexion
- Méthode `destroy_session()` pour supprimer les sessions

## Auteur

Projet réalisé dans le cadre de la formation Holberton School par Inès O.