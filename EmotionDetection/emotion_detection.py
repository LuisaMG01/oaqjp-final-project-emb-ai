import requests

def emotion_detector(text_to_analyze):
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    myobj = { "raw_document": { "text": text_to_analyze } }
    
    response = requests.post(url, json=myobj, headers=header)
    
    if response.status_code != 200:
        return {
            'anger': None,
            'disgust': None,
            'fear': None,
            'joy': None,
            'sadness': None,
            'dominant_emotion': None
        }, response.status_code 

    res = response.json()
    dominant = ""
    score_dominant = 0
    response_emotions = {}

    for emotion in res['emotionPredictions'][0]['emotion']:
        response_emotions[emotion] = res['emotionPredictions'][0]['emotion'][emotion]
        if res['emotionPredictions'][0]['emotion'][emotion] > score_dominant:
            score_dominant = res['emotionPredictions'][0]['emotion'][emotion]
            dominant = emotion
    response_emotions['dominant_emotion'] = dominant

    return response_emotions 
