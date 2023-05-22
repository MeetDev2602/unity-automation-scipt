from Variable import *

androidManifestPath = projectUnityExportPath+r"\unityLibrary\src\main\AndroidManifest.xml"
launcherPath = projectUnityExportPath+r"\launcher\build.gradle"
unityLibrarypath = projectUnityExportPath+r"\unityLibrary\build.gradle"
gradlePropertiesPath = projectUnityExportPath+r"\gradle.properties"
localPropertiesPath = projectUnityExportPath+r"\local.properties"

def launcherBuildGradle():
   
    launcherGradle = open(launcherPath, 'r')
    replaceElementList = ["bundle {", "language {",
    "enableSplit = false",
    "density {",
    "enableSplit = false",
    "abi {",
    "enableSplit = true"]

    new_file_content = ""
    endcorner = False
    lastEndCorner = False
    for line in launcherGradle:
        stripped_line = line.strip()
        if "com.android.application" in stripped_line:
            new_line = stripped_line.replace("com.android.application", "com.android.library")
        elif "buildToolsVersion" in stripped_line:
            new_line = ""
        elif "applicationId" in stripped_line:
            new_line = ""
        elif stripped_line in replaceElementList:
            if "abi {" in replaceElementList:
                lastEndCorner = True
            new_line = ""
            endcorner = True
        elif "}" in stripped_line and endcorner:
            new_line = ""
            endcorner = False
        elif lastEndCorner:
            new_line = ""
            lastEndCorner = False
        else:
            new_line = stripped_line

        new_file_content += new_line +"\n"
            
    launcherGradle.close()

    writing_file = open(launcherPath, "w")
    writing_file.write(new_file_content)
    writing_file.close()


def unityLibraryBuildGradle():
    
    unityLibraryGradle = open(unityLibrarypath, 'r')

    new_file_content = ""
    for line in unityLibraryGradle:
        stripped_line = line.strip()
    
        if "buildToolsVersion" in stripped_line:
            new_line = ""
        else:
            new_line = stripped_line

        new_file_content += new_line +"\n"
            
    unityLibraryGradle.close()

    writing_file = open(unityLibrarypath, "w")
    writing_file.write(new_file_content)
    writing_file.close()

def gradleProperties():
    gradleProperties = open(gradlePropertiesPath, 'r')

    new_file_content = ""
    for line in gradleProperties:
        stripped_line = line.strip()
        if "unityStreamingAssets" in stripped_line:
            new_line = "unityStreamingAssets=.json"
        elif "android.enableR8" in stripped_line:
            new_line = ""
        else:
            new_line = stripped_line

        new_file_content += new_line +"\n"

    gradleProperties.close()

    writing_file = open(gradlePropertiesPath, "w")
    writing_file.write(new_file_content)
    writing_file.close()


def unityLibraryAndroidManifest():
    androidManifest = open(androidManifestPath, 'r')
    replaceElementList = [
        "<intent-filter>",
        """<action android:name="android.intent.action.MAIN" />""",
        """<category android:name="android.intent.category.LAUNCHER" />""",
        "</intent-filter>",
    ]
    new_file_content = ""
    for line in androidManifest:
        stripped_line = line.strip()
    
        if "com.unity3d.player.UnityPlayerActivity" in stripped_line:
            new_line =  stripped_line.replace(">","""\nandroid:process=":unityplayer">""")
        elif stripped_line in replaceElementList:
            new_line = ""
        else:
            new_line = stripped_line

        new_file_content += new_line +"\n"

    androidManifest.close()

    writing_file = open(androidManifestPath, "w")
    writing_file.write(new_file_content)
    writing_file.close()


def localProperties():
    file = open(localPropertiesPath, 'a')
    file.write("\n"+"ndk.dir="+unityNDKPath)
    file.close()

unityLibraryAndroidManifest()
launcherBuildGradle()
unityLibraryBuildGradle()
gradleProperties()  
if isunityProjectDifferentPC:
    localProperties()