package com.phonetag.util;

import android.content.Context;

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.net.HttpURLConnection;
import java.net.URL;

public class Api {
    
    private static String URL_BASE = "http://128.237.125.40:5000";
    private static String URL_REGISTER = URL_BASE + "/newUser";
    private static String URL_UPDATE = URL_BASE + "/udpateUser";
    private static String URL_TAG = URL_BASE + "/tag";
    private static String URL_REMOVE = URL_BASE + "/remove";
    
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
    
    public static void tag(String gameId, String myId, String taggedId) {
        StringBuilder sb = new StringBuilder();
        sb.append(URL_TAG);
        sb.append("?name=");
        sb.append(myId);
        sb.append("&tagged=");
        sb.append(taggedId);
        sb.append(token());
        getHttpResponse(sb.toString());
    }
    
    public static void updateLoc(String id, float lat, float lng) {
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
