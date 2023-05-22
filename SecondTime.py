import shutil
from Variable import *

launcherDir =androidProjectPath+r"\launcher" 
unityLibraryDir = androidProjectPath+r"\unityLibrary" 

shutil.rmtree(launcherDir)
shutil.rmtree(unityLibraryDir)

copyDir([projectUnityExportPath+r"\unityLibrary" ,projectUnityExportPath+r"\launcher"], androidProjectPath)


commonUnityDir = androidProjectPath+r"\unityLibrary\src\main\java\com\unity3d\player"
copyDir([commonUnityPath],commonUnityDir )