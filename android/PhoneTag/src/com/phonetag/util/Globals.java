package com.phonetag.util;

import android.content.Context;

import com.phonetag.models.Game;
import com.phonetag.models.User;

import java.util.List;

public class Globals {
    
    private static Globals mInstance;
    
    private static String name;
    private static String id;
    private static String token;
    private static List<Game> games;
    private static List<User> users;
    private static List<User> friends;
    
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

    public void setName(Context ctx, String name) {
        Globals.name = name;
        Storage.save(ctx);
    }

    public String getId() {
        return id;
    }

    public void setId(Context ctx, String id) {
        Globals.id = id;
        Storage.save(ctx);
    }

    public String getToken() {
        return token;
    }

    public void setToken(Context ctx, String token) {
        Globals.token = token;
        Storage.save(ctx);
    }

    public List<Game> getGames() {
        return games;
    }

    public void setGames(Context ctx, List<Game> games) {
        Globals.games = games;
        Storage.save(ctx);
    }

    public List<User> getUsers() {
        return users;
    }

    public void setUsers(Context ctx, List<User> users) {
        Globals.users = users;
        Storage.save(ctx);
    }

    public List<User> getFriends() {
        return friends;
    }

    public void setFriends(Context ctx, List<User> friends) {
        Globals.friends = friends;
        Storage.save(ctx);
    }
    
}
