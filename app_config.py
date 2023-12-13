from sentiment_analysis_service.sentiment_analysis import analyze
from word_count_service.word_count import count
from entity_recognition_service.entity_recognition import recognize


SERVICES = {
    
    'sentiment_analysis': analyze,
    'word_count': count,
    'entity_recognition': recognize

    # Add other services and functions here
}