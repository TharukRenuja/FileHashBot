import shutil
import os

async def cleanFolder(folderPath):
    try:
        shutil.rmtree(folderPath) # delete folder for user
    except:
        pass
    try:
        os.rmdir(folderPath)
    except:
        pass

async def deleteFile(filePath):
    if os.path.isfile(filePath):
        try:
            os.remove(filePath)
        except:
            pass