projectUnityExportPath = r"C:\Users\Apricot\AndroidStudioProjects\PathCreatorExport"
androidProjectPath = r"C:\Users\Apricot\AndroidStudioProjects\PathCreatorApp"
commonUnityPath = r"C:\Users\Apricot\AndroidStudioProjects\UniDroidDataPass\unityLibrary\src\main\java\com\unity3d\player\CommonUnity.java"
isunityProjectDifferentPC = False
unityNDKPath = "C\:/Program Files/Unity/Hub/Editor/2021.3.6f1/Editor/Data/PlaybackEngines/AndroidPlayer/NDK"
ndkPath = "C\:/Users/Apricot/AppData/Local/Android/Sdk/ndk/21.3.6528147"

import pythoncom
from win32com.shell import shell, shellcon

def copyDir(src_files,dst_folder):      
    pfo = pythoncom.CoCreateInstance(shell.CLSID_FileOperation,None,pythoncom.CLSCTX_ALL,shell.IID_IFileOperation)
    pfo.SetOperationFlags(shellcon.FOF_NOCONFIRMATION)
    dst = shell.SHCreateItemFromParsingName(dst_folder,None,shell.IID_IShellItem)

    for f in src_files:
        src = shell.SHCreateItemFromParsingName(f,None,shell.IID_IShellItem)
        pfo.CopyItem(src,dst)
    success = pfo.PerformOperations()
    aborted = pfo.GetAnyOperationsAborted()
    return success and not aborted