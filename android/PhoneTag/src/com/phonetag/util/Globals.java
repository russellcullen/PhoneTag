package com.phonetag.util;

import android.content.Context;
import android.content.SharedPreferences;

public class Globals {
    
    private static Globals mInstance;
    
    private static String name;
    private static String id;
    
    private Globals() {}
    
    public static Globals getInstance() {
        if (mInstance == null) {
            mInstance = new Globals();
        }
        return mInstance;
    }
    
    public String getName() {
        return name;
    }

    public void setName(Context context, String name) {
        Globals.name = name;
    }

    public String getId() {
        return id;
    }

    public void setId(Context context, String id) {
        Globals.id = id;
    }
    
//    public Globals loadGlobals(Context context) {
//        SharedPreferences prefs = context.getSharedPreferences(
//                "com.phonetag", Context.MODE_PRIVATE);
//        prefs.getString("com.fridgi.name", null);
//    }
//    
//    public void saveFridge(Context context) {
//        SharedPreferences prefs = context.getSharedPreferences(
//                "com.phonetag", Context.MODE_PRIVATE);
//        prefs.edit().putString("com.fridgi.name", ).commit();
//    }

}
