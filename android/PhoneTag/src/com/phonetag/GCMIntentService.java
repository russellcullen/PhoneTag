package com.phonetag;

import android.app.Notification;
import android.app.NotificationManager;
import android.app.PendingIntent;
import android.content.Context;
import android.content.Intent;
import android.location.Location;
import android.location.LocationManager;
import android.support.v4.app.NotificationCompat;
import android.util.Log;

import com.google.android.gcm.GCMBaseIntentService;
import com.phonetag.models.Game;
import com.phonetag.models.User;
import com.phonetag.util.Api;
import com.phonetag.util.Globals;
import com.phonetag.util.Parsers;

import org.json.JSONArray;
import org.json.JSONException;
import org.json.JSONObject;

import java.util.ArrayList;
import java.util.List;

public class GCMIntentService extends GCMBaseIntentService {

    @Override
    protected void onError(Context arg0, String arg1) {
        // TODO Auto-generated method stub
        
    }

    @Override
    protected void onMessage(Context arg0, Intent intent) {
        // Prepare intent which is triggered if the
        // notification is selected
        if (intent.hasExtra("users")) {
            String usersJson = intent.getStringExtra("users");
            ArrayList<User> users = new ArrayList<User>();
            try {
                JSONArray userObjs = new JSONArray(usersJson);
                for (int i=0; i < userObjs.length(); i++) {
                    JSONObject jsonIngredient = userObjs.getJSONObject(i);
                    users.add(Parsers.parseUser(jsonIngredient));
                }
            } catch (JSONException e) {
                e.printStackTrace();
            }
            
            Globals.getInstance().setUsers(arg0, users);
            Intent broadcast = new Intent("com.phonetag.update");
            sendBroadcast(broadcast);
            // TODO: Do something with users
        }
        if (intent.hasExtra("it")) {
            String itID = intent.getStringExtra("it");
            String gameID = intent.getStringExtra("gameID");
            List<Game> games = Globals.getInstance().getGames();
            if (games != null) {
                for (int i = 0; i < games.size(); i++) {
                    if (games.get(i).getName().equals(gameID)) {
                        Game g = games.get(i);
                        g.setIt(itID);
                    }
                }
            }
            if (itID.equals(Globals.getInstance().getId())) {
                Intent openIntent = new Intent(this, MainActivity.class);
                PendingIntent pIntent = PendingIntent.getActivity(this, 0, openIntent, 0);
           
                // Build notification
                // Actions are just fake
                Notification noti = new NotificationCompat.Builder(this)
                        .setContentTitle("You're It")
                        .setContentText("No tag backs!").setSmallIcon(R.drawable.ic_launcher)
                        .setContentIntent(pIntent)
                        .build();
                     
                   
                NotificationManager notificationManager = 
                  (NotificationManager) getSystemService(NOTIFICATION_SERVICE);
            
                // Hide the notification after its selected
                noti.flags |= Notification.FLAG_AUTO_CANCEL;
            
                notificationManager.notify(0, noti); 
            }
            
            // TODO: Update for everyone
        }
    }

    @Override
    protected void onRegistered(Context ctx, String id) {
        Globals.getInstance().setId(ctx, id);
        Api.register(ctx, id, "coolbrow");
        Globals.getInstance().setName(this, "coolbrow");
        LocationManager locationManager = (LocationManager)getSystemService(Context.LOCATION_SERVICE);
        Location location = locationManager.getLastKnownLocation(LocationManager.GPS_PROVIDER);
        if (location != null) {
            Api.updateLoc(id, location.getLatitude(), location.getLongitude());
        }
        Api.newGame(ctx, id, "yoloswag");
    }

    @Override
    protected void onUnregistered(Context arg0, String arg1) {
        // TODO Auto-generated method stub
    }
}
