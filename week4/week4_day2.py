import csv
import os


def make_dir(path):
    os.makedirs(path,exist_ok=True)


def write_scores(path, data):
    with open(path,"w",encoding="utf-8",newline="") as f:
        writer=csv.writer(f)
        writer.writerow(["name","score"])
        writer.writerows(data)


def read_scores(path):
    with open(path,"r",encoding="utf-8") as f:
        reader=csv.DictReader(f)
        lists=[]
        for row in reader:
            lists.append((row['name'],int(row['score'])))
        return lists

def list_files(path):
    #return os.listdir(path)   
    file=os.listdir(path)
    file1=[]
    for i in file:
        if  os.path.isfile(os.path.join(path,i)):
            file1.append(i)
            
    return sorted(file1)



def file_size(path):

    return os.path.getsize(path)


if __name__ == "__main__":
    make_dir("week4_data")
    write_scores("week4_data/scores.csv", [["小明", 90], ["小红", 85], ["小刚", 78]])
    print(read_scores("week4_data/scores.csv"))
    print(list_files("week4_data"))
    print(file_size("week4_data/scores.csv"))
