import json


def collectionJson():
    fileName1 = "/home/zhou/guoqiang/faces/faces_female/female_average_faces/scoreJson.json"
    fileName2 = "/home/zhou/guoqiang/faces/faces_female/female_good_faces/scoreJson.json"
    fileName3 = "/home/zhou/guoqiang/faces/faces_female/female_poor_faces/scoreJson.json"
    data1 = json.load(open(fileName1))
    data2 = json.load(open(fileName2))
    data3 = json.load(open(fileName3))

    data1["faces"].append(data2["faces"])
    data1["faces"].append(data3["faces"])

    fileName  = "/home/zhou/guoqiang/faces/faces_female/scoreJson.json"
    with open(fileName, 'w') as f:
        json.dump(data1, f)



def handle_json():
    fileName = "/home/zhou/guoqiang/faces/faces_female/female_average_faces/scoreJson.json"
    data = json.load(open(fileName))

    for face in (data["faces"]):
        face["sex"] = "female"
        face["scores"] = [{"score": 2}]

    with open(fileName, 'w') as f:
        json.dump(data, f)


if __name__ == '__main__':
    # handle_json()
    collectionJson()
