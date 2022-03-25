import pandas
import json

if __name__ == '__main__':
    file = "/home/zhou/guoqiang/faces/new_faces_female/female_good_faces/tags.xlsx"
    xlsx_data = pandas.read_excel(file, sheet_name=0)
    json_data = []
    for i in range(xlsx_data.shape[0]):
        value = xlsx_data.loc[i].values
        location = value[1].replace("[", "").replace("]", "").replace(" ", "").split(",")
        if len(location) >= 4:
            json_data.append({"img_name": value[0], "box": (int(location[0]), int(location[1]),int( location[2]), int(location[3]))})

    fileName = "./faceJson.json"

    with open(fileName, 'w') as f:
        json.dump({"faces": json_data}, f)
