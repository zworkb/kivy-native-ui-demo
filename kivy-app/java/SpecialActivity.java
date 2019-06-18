
package org.kivy.android;

import java.io.InputStream;
import java.io.FileInputStream;
import java.io.FileOutputStream;
import java.io.FileWriter;
import java.io.File;
import java.io.IOException;
import java.lang.reflect.InvocationTargetException;
import java.lang.UnsatisfiedLinkError;
import java.util.ArrayList;
import java.util.Collections;
import java.util.Iterator;
import java.util.List;
import java.util.Timer;
import java.util.TimerTask;

import android.app.Activity;
import android.content.Context;
import android.content.Intent;
import android.content.pm.ActivityInfo;
import android.content.pm.PackageManager;
import android.content.pm.ApplicationInfo;
import android.graphics.Bitmap;
import android.graphics.BitmapFactory;
import android.graphics.Color;
import android.graphics.PixelFormat;
import android.Manifest;
import android.os.AsyncTask;
import android.os.Bundle;
import android.os.PowerManager;
import android.util.Log;
import android.view.SurfaceHolder;
import android.view.SurfaceView;
import android.view.View;
import android.view.ViewGroup;
import android.view.Window;
import android.view.WindowManager;
import android.widget.ImageView;
import android.widget.Toast;

import org.libsdl.app.SDL;
import org.libsdl.app.SDLActivity;

import org.kivy.android.PythonUtil;
import org.kivy.android.launcher.Project;

import org.renpy.android.ResourceManager;
import org.renpy.android.AssetExtract;

import org.kivy.android.PythonActivity;

// import at.forstservice.forstservice.timberremoval.TimberRemovalActivity;
import org.kivy.nativeuidemo.MainActivity;

public class SpecialActivity extends PythonActivity {
    private static final String TAG = "SpecialActivity";


    @Override
    protected void onCreate(Bundle savedInstanceState) {
        Log.v(TAG, "SpecialActivity onCreate running!!");

        Log.v(TAG, "About to do super onCreate");
        super.onCreate(savedInstanceState);
        Log.v(TAG, "Did super onCreate");
        // startKotlinActivity();
    }

    public void startKotlinActivity() {
        Log.v(TAG, "startKotlinActivity");
        Intent intent = new Intent(this, MainActivity.class);
        this.startActivity(intent);
    }

}
