import requests

def emotion_detector(text_to_analyze):
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    myobj = { "raw_document": { "text": text_to_analyze } }
    response = requests.post(url, json = myobj, headers=header)
    
    res = response.json()

    dominant = ""
    score_dominant = 0
    response_emotions = {}
    for i in res['emotionPredictions'][0]['emotion']:
        response_emotions[i] = res['emotionPredictions'][0]['emotion'][i]
        if res['emotionPredictions'][0]['emotion'][i] > score_dominant:
            score_dominant = res['emotionPredictions'][0]['emotion'][i]
            dominant = i
    response_emotions['dominant_emotion'] = dominant

    return response_emotions




