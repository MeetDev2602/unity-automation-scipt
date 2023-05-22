from Variable import *


copyDir([projectUnityExportPath+r"\unityLibrary" ,projectUnityExportPath+r"\launcher"], androidProjectPath)

appGradlePath = androidProjectPath+r"\app\build.gradle"
appGradlePropertiesPath = androidProjectPath+r"\gradle.properties"

appLocalPropertiesPath = androidProjectPath+r"\local.properties"
settingGradlePath = androidProjectPath + r"\settings.gradle"

appAndroidMaifestPath = androidProjectPath+r"\app\src\main\AndroidManifest.xml"



def appBuildGradle():
    launcherGradle = open(appGradlePath, 'r')
    new_file_content = ""
    for line in launcherGradle:
        stripped_line = line.strip()
        if "dependencies {" in stripped_line:
            new_line = stripped_line +"\n" +"""
            implementation project(path: ':launcher')
            implementation project(path: ':unityLibrary')
            implementation fileTree(dir: 'libs', includes: ['*.jar'])
            """
      
        else:
            new_line = stripped_line

        new_file_content += new_line +"\n"
            
    launcherGradle.close()

    writing_file = open(appGradlePath, "w")
    writing_file.write(new_file_content)
    writing_file.close()

def appGradlProperties():
    file = open(appGradlePropertiesPath, 'a')
    file.write("\nunityStreamingAssets=.unity3d, google-services-desktop.json, google-services.json, GoogleService-Info.plist")
    file.close()


def localProperties():
    file = open(appLocalPropertiesPath, 'a')
    file.write("\n"+"ndk.dir="+ndkPath)
    file.close()
 
def settingGradle():
    file = open(settingGradlePath, 'a')
    file.write("\n"+"""include ':unityLibrary'\ninclude ':launcher'""")
    file.close()

def appAndroidMaifest():
    androidMaifest = open(appAndroidMaifestPath, 'r')
    new_file_content = ""
    for line in androidMaifest:
        stripped_line = line.strip()
        if "<application" in stripped_line:
            new_line = stripped_line +"\n" +"""
            tools:replace="android:icon,android:theme"
            """
        else:
            new_line = stripped_line

        new_file_content += new_line +"\n"
            
    androidMaifest.close()

    writing_file = open(appAndroidMaifestPath, "w")
    writing_file.write(new_file_content)
    writing_file.close()

appBuildGradle()
appGradlProperties()
localProperties()
settingGradle()
appAndroidMaifest()

commonUnityDir = androidProjectPath+r"\unityLibrary\src\main\java\com\unity3d\player"
copyDir([commonUnityPath],commonUnityDir )