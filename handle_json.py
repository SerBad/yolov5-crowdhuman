import json


## https://note.youdao.com/ynoteshare/index.html?id=f8826c94b9c5c8e2e7e4ccf9ae87f901&type=note&_time=1648181348569

def collectionJson():
    # fileName1 = "/home/zhou/guoqiang/faces/face_male/face_male_average/scoreJson.json"
    # fileName2 = "/home/zhou/guoqiang/faces/face_male/face_male_good/scoreJson.json"
    # fileName3 = "/home/zhou/guoqiang/faces/face_male/face_male_poor/scoreJson.json"

    fileName1 = "/home/zhou/guoqiang/faces/new_faces_female/female_good_faces/faceJson.json"
    fileName2 = "/home/zhou/guoqiang/faces/new_faces_female/female_average_faces/faceJson.json"
    fileName3 = "/home/zhou/guoqiang/faces/new_faces_female/female_poor_faces/faceJson.json"

    data1 = json.load(open(fileName1))
    data2 = json.load(open(fileName2))
    data3 = json.load(open(fileName3))

    # extand
    data1["faces"].extend(data2["faces"])
    data1["faces"].extend(data3["faces"])


    fileName = "/home/zhou/guoqiang/faces/new_faces_female/faceJson.json"
    with open(fileName, 'w') as f:
        json.dump(data1, f)

def collectionHeadJson():
    # fileName1 = "/home/zhou/guoqiang/faces/face_male/face_male_average/scoreJson.json"
    # fileName2 = "/home/zhou/guoqiang/faces/face_male/face_male_good/scoreJson.json"
    # fileName3 = "/home/zhou/guoqiang/faces/face_male/face_male_poor/scoreJson.json"

    fileName1 = "/home/zhou/guoqiang/faces/new_faces_female/female_good_faces/faceJson.json"
    fileName2 = "/home/zhou/guoqiang/faces/new_faces_female/female_average_faces/faceJson.json"
    fileName3 = "/home/zhou/guoqiang/faces/new_faces_female/female_poor_faces/faceJson.json"

    data1 = json.load(open(fileName1))
    data2 = json.load(open(fileName2))
    data3 = json.load(open(fileName3))

    # extand
    data1["heads"].extand(data2["heads"])
    data1["heads"].extand(data3["heads"])

    fileName = "/home/zhou/guoqiang/faces/new_faces_female/faceJson.json"
    with open(fileName, 'w') as f:
        json.dump(data1, f)


def handle_json():
    # fileName = "/home/zhou/guoqiang/faces/face_male/face_male_poor/scoreJson.json"
    # fileName = "/home/zhou/guoqiang/faces/new_faces_female/female_good_faces/faceJson.json"
    fileName = "/home/zhou/guoqiang/faces/new_faces_female/female_average_faces/faceJson.json"
    # fileName = "/home/zhou/guoqiang/faces/new_faces_female/female_poor_faces/faceJson.json"
    data = json.load(open(fileName))

    for face in (data["heads"]):
        face["sex"] = "female"
        face["scores"] = [{"score": 2}]

    with open(fileName, 'w') as f:
        json.dump(data, f)


# def handle_heads_json():
    # fileName = "/home/zhou/guoqiang/faces/face_male/face_male_poor/scoreJson.json"
    # fileName = "/home/zhou/guoqiang/faces/new_faces_female/female_good_faces/faceJson.json"
    fileName = "/home/zhou/guoqiang/faces/new_faces_female/female_average_faces/faceJson.json"
    # fileName = "/home/zhou/guoqiang/faces/new_faces_female/female_poor_faces/faceJson.json"
    data = json.load(open(fileName))

    for face in (data["heads"]):
        face["sex"] = "female"
        face["scores"] = [{"score": 2}]

    with open(fileName, 'w') as f:
        json.dump(data, f)





if __name__ == '__main__':
    # handle_json()
    # handle_heads_json()
    collectionJson()
