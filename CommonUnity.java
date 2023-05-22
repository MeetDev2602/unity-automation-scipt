package com.unity3d.player;

import android.content.Context;
import android.view.View;

public class CommonUnity {
    public UnityPlayer mUnityPlayer;
    public Context context;

    public CommonUnity(Context context) {
        this.context = context;
        mUnityPlayer = new UnityPlayer(context);
    }

    public View getUnityView(){
        return mUnityPlayer.getView();
    }

    public void unityResume(){
        mUnityPlayer.resume();
    }

    public void unityPause(){
        mUnityPlayer.pause();
    }
    public void unityDestroy(){
        mUnityPlayer.quit();
    }

    public void setConfig(){
        mUnityPlayer.requestFocus();
        mUnityPlayer.windowFocusChanged(true);
    }
    public void sendMessageUnity(String unityGameObjectName,String unityFunctionName,String parameter){
        UnityPlayer.UnitySendMessage(unityGameObjectName, unityFunctionName,parameter);
    }
}