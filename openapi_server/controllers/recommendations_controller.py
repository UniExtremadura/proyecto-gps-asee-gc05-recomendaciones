import connexion
from typing import Dict, Tuple, Union, List
from collections import Counter # Importante para el algoritmo

from openapi_server.models.like import Like
from openapi_server.models.play import Play
from openapi_server.models.track import Track
from openapi_server.models.comment import Comment
from openapi_server.models.rating import Rating
from openapi_server import util

# Cuando tengas la BD real, importarás:
# from pymongo import MongoClient

# ==============================================================================
#  BASE DE DATOS TEMPORAL (MEMORIA RAM)
# ==============================================================================
_PLAYS_DB = []
_LIKES_DB = []
_COMMENTS_DB = []
_RATINGS_DB = []


# ==============================================================================
#  BLOQUE 1: REGISTRO DE ACTIVIDAD (PLAYS Y LIKES)
# ==============================================================================

def add_play(body):  
    """Registrar una reproducción"""
    if connexion.request.is_json:
        play_obj = body 
        
        # ----------------------------------------------------------------------
        # TODO: CÓDIGO PARA MONGODB (FUTURO)
        # client = MongoClient('mongodb://localhost:27017/')
        # db = client['microservicio_recomendaciones']
        # db.plays.insert_one(play_obj.to_dict())
        # ----------------------------------------------------------------------

        # FUNCIONALIDAD ACTUAL (MEMORIA):
        _PLAYS_DB.append(play_obj)
        print(f"--> Play registrada: User {play_obj.user_id}")
        
    return "Play registered successfully", 201

def add_play(body):  
    """Registrar una reproducción"""
    if connexion.request.is_json:
        # El body ya es el diccionario Python que contiene los datos del Play
        play_obj = body 
        
        # ----------------------------------------------------------------------
        # TODO: CÓDIGO PARA MONGODB (FUTURO)
        # Aquí es donde, en el futuro, harías:
        # db.plays.insert_one(play_obj)
        # ----------------------------------------------------------------------
        
        # FUNCIONALIDAD ACTUAL (MEMORIA):
        _PLAYS_DB.append(play_obj)
        
        # Corrección: Acceder con corchetes ['user_id']
        print(f"--> [RECIBIDO] Play registrada en Python: User {play_obj['user_id']}")

    return "Play registered successfully", 201

def add_like(body): 
    """Registrar un like"""
    # Importamos connexion aquí si no está al inicio
    import connexion 
    
    if connexion.request.is_json:
        like_obj = body
        
        # ----------------------------------------------------------------------
        # TODO: CÓDIGO PARA MONGODB (FUTURO)
        # db.likes.insert_one(like_obj)
        # ----------------------------------------------------------------------
        
        # FUNCIONALIDAD ACTUAL (MEMORIA):
        _LIKES_DB.append(like_obj)
        
        # IMPORTANTE: Usamos corchetes para acceder a los datos
        print(f"--> [RECIBIDO] Like registrado en Python: User {like_obj['user_id']}")

    return "Like registered successfully", 201

def get_user_plays(id_user): 
    """Obtener reproducciones de usuario"""
    # ----------------------------------------------------------------------
    # TODO: CÓDIGO PARA MONGODB (FUTURO)
    # cursor = db.plays.find({"user_id": id_user})
    # return [Play.from_dict(doc) for doc in cursor]
    # ----------------------------------------------------------------------
    return [p for p in _PLAYS_DB if p.user_id == id_user]


def get_user_likes(id_user): 
    """Obtener likes de usuario"""
    # ----------------------------------------------------------------------
    # TODO: CÓDIGO PARA MONGODB (FUTURO)
    # cursor = db.likes.find({"user_id": id_user})
    # return [Like.from_dict(doc) for doc in cursor]
    # ----------------------------------------------------------------------
    return [l for l in _LIKES_DB if l.user_id == id_user]


def get_track_plays(id_track):
    """Obtener reproducciones por canción"""
    # ----------------------------------------------------------------------
    # TODO: CÓDIGO PARA MONGODB (FUTURO)
    # cursor = db.plays.find({"track_id": id_track})
    # return [Play.from_dict(doc) for doc in cursor]
    # ----------------------------------------------------------------------
    return [p for p in _PLAYS_DB if p.track_id == id_track]


def get_track_likes(id_track):
    """Obtener likes por canción"""
    # ----------------------------------------------------------------------
    # TODO: CÓDIGO PARA MONGODB (FUTURO)
    # cursor = db.likes.find({"track_id": id_track})
    # return [Like.from_dict(doc) for doc in cursor]
    # ----------------------------------------------------------------------
    return [l for l in _LIKES_DB if l.track_id == id_track]


# ==============================================================================
#  BLOQUE 2: CRUD DE COMENTARIOS Y VALORACIONES (CON MODERACIÓN)
# ==============================================================================

def add_comment(body):
    """Añadir un comentario (entra como 'pending')"""
    if connexion.request.is_json:
        comment_obj = Comment.from_dict(body)
        comment_obj.status = 'pending'
        
        # ----------------------------------------------------------------------
        # TODO: CÓDIGO PARA MONGODB (FUTURO)
        # db.comments.insert_one(comment_obj.to_dict())
        # ----------------------------------------------------------------------

        _COMMENTS_DB.append(comment_obj)
        print(f"--> Comentario pendiente: {comment_obj.content}")
        
    return "Comment added successfully. Pending moderation.", 201


def get_track_comments(id_track):
    """Obtener comentarios (Solo approved)"""
    # ----------------------------------------------------------------------
    # TODO: CÓDIGO PARA MONGODB (FUTURO)
    # cursor = db.comments.find({"track_id": id_track, "status": "approved"})
    # return [Comment.from_dict(doc) for doc in cursor]
    # ----------------------------------------------------------------------
    return [c for c in _COMMENTS_DB if c.track_id == id_track and c.status == 'approved']


def moderate_comment(id_comment, action):
    """Moderar comentario (Admin)"""
    # ----------------------------------------------------------------------
    # TODO: CÓDIGO PARA MONGODB (FUTURO)
    # new_status = 'approved' if action == 'approve' else 'rejected'
    # result = db.comments.update_one({"id": id_comment}, {"$set": {"status": new_status}})
    # ----------------------------------------------------------------------

    for comment in _COMMENTS_DB:
        if comment.id == id_comment:
            if action == 'approve':
                comment.status = 'approved'
                return "Comment approved", 200
            elif action == 'reject':
                comment.status = 'rejected'
                return "Comment rejected", 200
    return "Comment not found", 404


def delete_comment(id_comment):
    """Eliminar comentario"""
    # ----------------------------------------------------------------------
    # TODO: CÓDIGO PARA MONGODB (FUTURO)
    # db.comments.delete_one({"id": id_comment})
    # ----------------------------------------------------------------------
    global _COMMENTS_DB
    initial_len = len(_COMMENTS_DB)
    _COMMENTS_DB = [c for c in _COMMENTS_DB if c.id != id_comment]
    
    if len(_COMMENTS_DB) < initial_len:
        return "Comment deleted", 200
    return "Comment not found", 404


def add_rating(body):
    """Añadir valoración (1-5)"""
    if connexion.request.is_json:
        rating_obj = Rating.from_dict(body)
        if rating_obj.score < 1 or rating_obj.score > 5:
            return "Score must be 1-5", 400

        # ----------------------------------------------------------------------
        # TODO: CÓDIGO PARA MONGODB (FUTURO)
        # db.ratings.insert_one(rating_obj.to_dict())
        # ----------------------------------------------------------------------
        
        _RATINGS_DB.append(rating_obj)
    return "Rating added", 201


def get_track_ratings(id_track):
    """Obtener valoraciones"""
    # ----------------------------------------------------------------------
    # TODO: CÓDIGO PARA MONGODB (FUTURO)
    # cursor = db.ratings.find({"track_id": id_track})
    # return [Rating.from_dict(doc) for doc in cursor]
    # ----------------------------------------------------------------------
    return [r for r in _RATINGS_DB if r.track_id == id_track]


# ==============================================================================
#  BLOQUE 3: ALGORITMOS DE RECOMENDACIÓN Y MÉTRICAS
# ==============================================================================

def get_top_tracks():
    """
    Devuelve el TOP 10 de canciones más escuchadas globalmente.
    """
    # ----------------------------------------------------------------------
    # TODO: CÓDIGO PARA MONGODB (FUTURO)
    # pipeline = [
    #     {"$group": {"_id": "$track_id", "count": {"$sum": 1}}},
    #     {"$sort": {"count": -1}},
    #     {"$limit": 10}
    # ]
    # aggregation_result = list(db.plays.aggregate(pipeline))
    # ... mapeo de resultados a objetos Track ...
    # ----------------------------------------------------------------------

    # FUNCIONALIDAD ACTUAL (MEMORIA):
    all_ids = [p.track_id for p in _PLAYS_DB]
    if not all_ids: return []
    
    counts = Counter(all_ids).most_common(10)
    
    result = []
    for tid, count in counts:
        # Simulamos recuperar título (esto vendría del MS Contenidos)
        result.append(Track(id=tid, title=f"Hit Global ({count} plays)"))
    return result


def get_recommended_tracks(id_user, type=None):
    """
    Algoritmo de recomendación personalizado.
    """
    recs = []
    print(f"Calculando recomendaciones tipo '{type}' para {id_user}")
    
    if type == 'like':
        # 1. Obtener likes del usuario
        user_likes = [l.track_id for l in _LIKES_DB if l.user_id == id_user]
        
        if user_likes:
            # ------------------------------------------------------------------
            # TODO: MONGODB + LOGICA DE NEGOCIO
            # Buscar canciones con tags/géneros similares a las liked_tracks
            # ------------------------------------------------------------------
            recs.append(Track(id="rec_sim_1", title="Similar a tus likes 1"))
            recs.append(Track(id="rec_sim_2", title="Similar a tus likes 2"))
        else:
            return get_top_tracks() # Fallback si no hay likes
            
    elif type == 'genre':
        # ----------------------------------------------------------------------
        # TODO: MONGODB
        # Analizar historial -> Obtener género top -> Buscar tracks de ese género
        # ----------------------------------------------------------------------
        recs.append(Track(id="gen_rock_1", title="Top Rock para ti"))
        
    elif type == 'subscription':
        # ----------------------------------------------------------------------
        # TODO: LLAMADA A MICROSERVICIO USUARIOS
        # Obtener artistas seguidos -> Buscar novedades de esos artistas
        # ----------------------------------------------------------------------
        recs.append(Track(id="sub_artist_1", title="Novedad de Artista seguido"))
        
    else:
        return get_top_tracks()
        
    return recs


def get_artist_top_tracks(id_artist):
    """
    Canciones más escuchadas de un artista específico.
    """
    # ----------------------------------------------------------------------
    # TODO: CÓDIGO PARA MONGODB (FUTURO)
    # pipeline = [
    #     {"$match": {"artist_id": id_artist}},
    #     {"$group": {"_id": "$track_id", "count": {"$sum": 1}}},
    #     {"$sort": {"count": -1}}
    # ]
    # ----------------------------------------------------------------------

    # FUNCIONALIDAD ACTUAL (MEMORIA):
    return [
        Track(id=f"{id_artist}_1", title="Hit 1 Artista"),
        Track(id=f"{id_artist}_2", title="Hit 2 Artista")
    ]


# STUBS RESTANTES (Funciones vacías para completar la interfaz)
def get_artist_plays(id_artist): return []