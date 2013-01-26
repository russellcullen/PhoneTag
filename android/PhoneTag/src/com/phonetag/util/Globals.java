package com.phonetag.util;

import android.content.Context;
import android.util.Log;

import com.phonetag.models.Game;
import com.phonetag.models.User;

import java.util.List;

public class Globals {
    
    private static Globals mInstance;
    
    private String name;
    private String id;
    private String token;
    private List<Game> games;
    private List<User> users;
    private List<User> friends;
    
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
        this.name = name;
        Storage.save(ctx);
    }

    public String getId() {
        return id;
    }

    public void setId(Context ctx, String id) {
        this.id = id;
        Storage.save(ctx);
    }

    public String getToken() {
        return token;
    }

    public void setToken(Context ctx, String token) {
        this.token = token;
        Log.e("SETTING", "SETing TOKEN");
        Storage.save(ctx);
    }

    public List<Game> getGames() {
        return games;
    }

    public void setGames(Context ctx, List<Game> games) {
        this.games = games;
        Storage.save(ctx);
    }

    public List<User> getUsers() {
        return users;
    }

    public void setUsers(Context ctx, List<User> users) {
        this.users = users;
        Storage.save(ctx);
    }

    public List<User> getFriends() {
        return friends;
    }

    public void setFriends(Context ctx, List<User> friends) {
        this.friends = friends;
        Storage.save(ctx);
    }
    
}
