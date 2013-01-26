package com.phonetag.util;

import android.content.Context;
import android.util.Log;

import com.google.gson.Gson;

import org.json.JSONArray;
import org.json.JSONException;
import org.json.JSONObject;

import java.io.BufferedReader;
import java.io.FileInputStream;
import java.io.FileOutputStream;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.List;

public class Storage {
    
    private static String USERS_FILE = "users.json";
    private static String FRIENDS_FILE = "friends.json";
    private static String GAMES_FILE = "games.json";
    private static String TOKEN_FILE = "token.txt";
    private static String ID_FILE = "id.txt";
    private static String NAME_FILE = "name.txt";
    
    
    public static void save(Context ctx) {
        FileOutputStream fos;
        try {
            // Save users
            if (Globals.getInstance().getUsers() != null) {
                fos = ctx.openFileOutput(USERS_FILE, Context.MODE_PRIVATE);
                String users = objectsToJSONArray(Globals.getInstance().getUsers()).toString();
                fos.write(users.getBytes());
                fos.close();
            }
            
            // Save friends
            if (Globals.getInstance().getFriends() != null) {
                fos = ctx.openFileOutput(FRIENDS_FILE, Context.MODE_PRIVATE);
                String friends = objectsToJSONArray(Globals.getInstance().getFriends()).toString();
                fos.write(friends.getBytes());
                fos.close();
            }
            
            // Save games
            if (Globals.getInstance().getGames() != null) {
                fos = ctx.openFileOutput(GAMES_FILE, Context.MODE_PRIVATE);
                String games = objectsToJSONArray(Globals.getInstance().getGames()).toString();
                fos.write(games.getBytes());
                fos.close();
            }
            
            // Save token
            if (Globals.getInstance().getToken() != null) {
                fos = ctx.openFileOutput(TOKEN_FILE, Context.MODE_PRIVATE);
                fos.write(Globals.getInstance().getToken().getBytes());
                fos.close();
            }
            
            // Save id
            if (Globals.getInstance().getId() != null) {
                fos = ctx.openFileOutput(ID_FILE, Context.MODE_PRIVATE);
                fos.write(Globals.getInstance().getId().getBytes());
                fos.close();
            }
            
            // Save name
            if (Globals.getInstance().getName() != null) {
                fos = ctx.openFileOutput(NAME_FILE, Context.MODE_PRIVATE);
                fos.write(Globals.getInstance().getName().getBytes());
                fos.close();
            }
        } catch (Exception e) {
            // TODO Auto-generated catch block
            e.printStackTrace();
        }
    }
    
    public static void load(Context ctx) {
        FileInputStream fis;
        InputStreamReader inputStreamReader;
        BufferedReader bufferedReader;
        StringBuilder sb;
        String line;
        Globals g = Globals.getInstance();
        // Loads into Globals
        try {
            // Load users
            fis = ctx.openFileInput(USERS_FILE);
            inputStreamReader = new InputStreamReader(fis);
            bufferedReader = new BufferedReader(inputStreamReader);
            sb = new StringBuilder();
            while ((line = bufferedReader.readLine()) != null) {
                sb.append(line);
            }
            g.setUsers(ctx, Parsers.parseUserArray(new JSONArray(sb.toString())));
            fis.close();
        } catch (Exception e) {
            Log.e("ERROR", "OPENING USERS FILE");
        }
        try {
            // Load friends
            fis = ctx.openFileInput(FRIENDS_FILE);
            inputStreamReader = new InputStreamReader(fis);
            bufferedReader = new BufferedReader(inputStreamReader);
            sb = new StringBuilder();
            while ((line = bufferedReader.readLine()) != null) {
                sb.append(line);
            }
            g.setFriends(ctx, Parsers.parseUserArray(new JSONArray(sb.toString())));
            fis.close();
        } catch (Exception e) {
            Log.e("ERROR", "OPENING FRIENDS FILE");
        }
        try {
            // Load games
            fis = ctx.openFileInput(GAMES_FILE);
            inputStreamReader = new InputStreamReader(fis);
            bufferedReader = new BufferedReader(inputStreamReader);
            sb = new StringBuilder();
            while ((line = bufferedReader.readLine()) != null) {
                sb.append(line);
            }
            g.setGames(ctx, Parsers.parseGameArray(new JSONArray(sb.toString())));
            fis.close();
        } catch (Exception e) {
            Log.e("ERROR", "OPENING GAMES FILE");
        }
        try {
            // Load token
            fis = ctx.openFileInput(TOKEN_FILE);
            inputStreamReader = new InputStreamReader(fis);
            bufferedReader = new BufferedReader(inputStreamReader);
            sb = new StringBuilder();
            while ((line = bufferedReader.readLine()) != null) {
                sb.append(line);
            }
            g.setToken(ctx, sb.toString());
            fis.close();
        } catch (Exception e) {
            Log.e("ERROR", "OPENING TOKEN FILE");
        }
        try {
            // Load id
            fis = ctx.openFileInput(ID_FILE);
            inputStreamReader = new InputStreamReader(fis);
            bufferedReader = new BufferedReader(inputStreamReader);
            sb = new StringBuilder();
            while ((line = bufferedReader.readLine()) != null) {
                sb.append(line);
            }
            g.setId(ctx, sb.toString());
            fis.close();
        } catch (Exception e) {
            Log.e("ERROR", "OPENING ID FILE");
        }
        try {
            // Load name
            fis = ctx.openFileInput(NAME_FILE);
            inputStreamReader = new InputStreamReader(fis);
            bufferedReader = new BufferedReader(inputStreamReader);
            sb = new StringBuilder();
            while ((line = bufferedReader.readLine()) != null) {
                sb.append(line);
            }
            g.setName(ctx, sb.toString());
            fis.close();
        } catch (Exception e) {
            Log.e("ERROR", "OPENING NAME FILE");
        }
    }
    
    private static JSONArray objectsToJSONArray(List<?> objs) throws JSONException {
        Gson gson = new Gson();
        List<JSONObject> list = new ArrayList<JSONObject>();
        for ( Object o : objs) {
            list.add(new JSONObject(gson.toJson(o)));
        }
        return new JSONArray(list);
    }
}
