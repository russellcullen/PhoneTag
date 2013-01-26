package com.phonetag.util;

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.net.HttpURLConnection;
import java.net.URL;

public class Api {
    
    private static String URL_REGISTER = "http://phone-tag.herokuapp.com/newUser";
//    private static String URL_REGISTER = "http://128.237.125.40:5000/newUser";
    private static String URL_UPDATE = "http://phone-tag.herokuapp.com/udpate";
    private static String URL_TAG = "http://phone-tag.herokuapp.com/tag";
    
    public static void register(String id, String name) {
        StringBuilder sb = new StringBuilder();
        sb.append(URL_REGISTER);
        sb.append("?phoneID=");
        sb.append(id);
        sb.append("&name=");
        sb.append(name);
        getHttpResponse(sb.toString());
    }
    
    public static void tag(String myName, String taggedName) {
        StringBuilder sb = new StringBuilder();
        sb.append(URL_TAG);
        sb.append("?name=");
        sb.append(myName);
        sb.append("&tagged=");
        sb.append(taggedName);
        getHttpResponse(sb.toString());
    }
    
    public static void updateLoc(String name, float lat, float lng) {
        StringBuilder sb = new StringBuilder();
        sb.append(URL_UPDATE);
        sb.append("?name=");
        sb.append(name);
        sb.append("&lat=");
        sb.append(lat);
        sb.append("&lng=");
        sb.append(lng);
        getHttpResponse(sb.toString());
    }
    
    private static void getHttpResponse(String url) {
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
        } catch (Exception e) {
            e.printStackTrace();
        }
    }
}
