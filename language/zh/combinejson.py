import json
import glob


def combine_jsons():
    """
    Combine all json files in current folder. Generate result.json.
    :return: True
    """
    d = {}
    l = []
    read_files = glob.glob("*.json")

    for file in read_files:
        f = open(file, 'rb')
        d = json.load(f)
        l += d['data']
    d['data'] = l
    result = json.dumps((d))

    with open("result.json", 'w') as outfile:
        outfile.write(result)
    return True

if __name__ == "__main__":
    combine_jsons()
