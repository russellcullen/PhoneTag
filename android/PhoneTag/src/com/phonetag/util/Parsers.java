package com.phonetag.util;

import com.google.gson.Gson;
import com.phonetag.models.Game;
import com.phonetag.models.User;

import org.json.JSONArray;
import org.json.JSONException;
import org.json.JSONObject;

import java.util.ArrayList;

public abstract class Parsers {
    
    public static User parseUser(JSONObject obj) {
        return new Gson().fromJson(obj.toString(), User.class);
    }
    
    public static Game parseGame(JSONObject obj) {
        return new Gson().fromJson(obj.toString(), Game.class);
    }
    
    public static ArrayList<User> parseUserArray(JSONArray objs) {
        ArrayList<User> users = new ArrayList<User>();
        try {
            for (int i=0; i < objs.length(); i++) {
                JSONObject jsonUser = objs.getJSONObject(i);
                users.add(parseUser(jsonUser));
            }
        } catch (JSONException e) {
            e.printStackTrace();
        }
        return users;
    }
    
    public static ArrayList<Game> parseGameArray(JSONArray objs) {
        ArrayList<Game> games = new ArrayList<Game>();
        try {
            for (int i=0; i < objs.length(); i++) {
                JSONObject jsonGame = objs.getJSONObject(i);
                games.add(parseGame(jsonGame));
            }
        } catch (JSONException e) {
            e.printStackTrace();
        }
        return games;
    }
}