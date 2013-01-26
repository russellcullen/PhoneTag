package com.phonetag.util;

import android.content.Context;
import android.util.Log;

import com.phonetag.models.Game;

import org.json.JSONException;
import org.json.JSONObject;

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.net.HttpURLConnection;
import java.net.URL;
import java.util.ArrayList;
import java.util.List;

public class Api {
    
    private static String URL_BASE = "http://128.237.244.183:5000";
    private static String URL_REGISTER = URL_BASE + "/newUser";
    private static String URL_UPDATE = URL_BASE + "/updateUser";
    private static String URL_TAG = URL_BASE + "/tag";
    private static String URL_REMOVE = URL_BASE + "/remove";
    private static String URL_NEW_GAME = URL_BASE + "/newGame";
    private static String URL_JOIN_GAME = URL_BASE + "/joinGame";
    
    public static void register(Context ctx, String id, String name) {
        StringBuilder sb = new StringBuilder();
        sb.append(URL_REGISTER);
        sb.append("?phoneID=");
        sb.append(id);
        sb.append("&name=");
        sb.append(name);
        String token = getHttpResponse(sb.toString());
        Globals.getInstance().setToken(ctx, token);
    }
    
    public static void tag(String gameId, String myId, String taggedName) {
        StringBuilder sb = new StringBuilder();
        sb.append(URL_TAG);
        sb.append("?phoneID=");
        sb.append(myId);
        sb.append("&tagName=");
        sb.append(taggedName);
        sb.append("&gameName=");
        sb.append(gameId);
        sb.append(token());
        getHttpResponse(sb.toString());
    }
    
    public static void updateLoc(String id, double lat, double lng) {
        StringBuilder sb = new StringBuilder();
        sb.append(URL_UPDATE);
        sb.append("?phoneID=");
        sb.append(id);
        sb.append("&latitude=");
        sb.append(lat);
        sb.append("&longitude=");
        sb.append(lng);
        sb.append(token());
        getHttpResponse(sb.toString());
    }
    
    public static void newGame(Context ctx, String id, String name) {
        StringBuilder sb = new StringBuilder();
        sb.append(URL_NEW_GAME);
        sb.append("?phoneID=");
        sb.append(id);
        sb.append("&gameName=");
        sb.append(name);
        sb.append(token());
        String gameJson = getHttpResponse(sb.toString());
        List<Game> games = Globals.getInstance().getGames();
        if (games == null) {
            games = new ArrayList<Game>();
        }
        try {
            games.add(Parsers.parseGame(new JSONObject(gameJson)));
        } catch (JSONException e) {
            // TODO Auto-generated catch block
            e.printStackTrace();
        }
        Game g;
        try {
            g = Parsers.parseGame(new JSONObject(gameJson));
        } catch (JSONException e) {
            // TODO Auto-generated catch block
            e.printStackTrace();
        }
        
        Globals.getInstance().setGames(ctx, games);
    }
    
    public static void joinGame(Context ctx, String id, String name) {
        StringBuilder sb = new StringBuilder();
        sb.append(URL_JOIN_GAME);
        sb.append("?phoneID=");
        sb.append(id);
        sb.append("&gameName=");
        sb.append(name);
        sb.append(token());
        String gameJson = getHttpResponse(sb.toString());
        List<Game> games = Globals.getInstance().getGames();
        if (games == null) {
            games = new ArrayList<Game>();
        }
        try {
            games.add(Parsers.parseGame(new JSONObject(gameJson)));
        } catch (JSONException e) {
            // TODO Auto-generated catch block
            e.printStackTrace();
        }
        Globals.getInstance().setGames(ctx, games);
    }
    
    public static void remove(String id) {
        StringBuilder sb = new StringBuilder();
        sb.append(URL_REMOVE);
        sb.append("?name=");
        sb.append(id);
        sb.append(token());
        getHttpResponse(sb.toString());
    }
    
    private static String getHttpResponse(String url) {
        URL serverAddress;
        try {
            serverAddress = new URL(url);
      
            HttpURLConnection connection = (HttpURLConnection)serverAddress.openConnection();
            connection.setRequestMethod("GET");
            BufferedReader reader = new BufferedReader(new InputStreamReader(connection.getInputStream()));
            StringBuilder stringBuilder = new StringBuilder();

            String line = null;
            while ((line = reader.readLine()) != null)
            {
              stringBuilder.append(line + "\n");
            }
            reader.close();
            return stringBuilder.toString();
        } catch (Exception e) {
            e.printStackTrace();
            return null;
        }
    }
    
    private static String token() {
        return "&token=" + Globals.getInstance().getToken();
    }
}
