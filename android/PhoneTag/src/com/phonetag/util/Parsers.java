package com.phonetag.util;

import com.google.gson.Gson;
import com.phonetag.models.User;

import org.json.JSONObject;

public abstract class Parsers {
    
    public static User parseUser(JSONObject obj) {
        return new Gson().fromJson(obj.toString(), User.class);
    }
    
//    public static User parseUser(JSONObject obj) {
//        return new Gson().fromJson(obj.toString(), User.class);
//    }
//    
}