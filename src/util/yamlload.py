import yaml
import sys ,os
class YamlLoad:
    
    
    def fileload(self,filepath=r"data/testlogindata.yaml"):

        with open(file=filepath,mode="r",encoding="utf-8") as file:
            result=yaml.load(stream=file.read(),Loader=yaml.FullLoader)
        return result
    


if __name__=="__main__":
    print(YamlLoad().fileload()["logindata"])
    print(sys.path.append(os.path.abspath("./")))
    print(os.getcwd())