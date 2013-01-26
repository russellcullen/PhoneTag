
package com.phonetag;

import android.app.Activity;
import android.content.BroadcastReceiver;
import android.content.Context;
import android.content.Intent;
import android.content.IntentFilter;
import android.location.Criteria;
import android.location.Location;
import android.location.LocationListener;
import android.location.LocationManager;
import android.os.Bundle;
import android.util.Log;
import android.view.Menu;
import android.view.MenuItem;
import android.widget.Toast;

import com.google.android.gcm.GCMRegistrar;
import com.google.android.gms.maps.CameraUpdateFactory;
import com.google.android.gms.maps.GoogleMap;
import com.google.android.gms.maps.GoogleMap.OnInfoWindowClickListener;
import com.google.android.gms.maps.MapFragment;
import com.google.android.gms.maps.model.BitmapDescriptorFactory;
import com.google.android.gms.maps.model.LatLng;
import com.google.android.gms.maps.model.Marker;
import com.google.android.gms.maps.model.MarkerOptions;
import com.phonetag.models.Game;
import com.phonetag.models.User;
import com.phonetag.tasks.TagTask;
import com.phonetag.tasks.UpdateTask;
import com.phonetag.util.Api;
import com.phonetag.util.Globals;

import java.util.HashSet;
import java.util.List;

public class MainActivity extends Activity implements LocationListener, OnInfoWindowClickListener {
    
    private GoogleMap mMap;
    private Location best;
    private HashSet<String> its;
    private int updatedNum  = 0;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        LocationManager locationManager = (LocationManager)getSystemService(LOCATION_SERVICE);
        GCMRegistrar.checkDevice(this);
        GCMRegistrar.checkManifest(this);
        final String regId = GCMRegistrar.getRegistrationId(this);
        if (regId.equals("")) {
          GCMRegistrar.register(this, "343246241155");
        } else {
          Globals.getInstance().setId(this, regId);
          Log.v("HERE", "Already registered: " + regId);
          
          Criteria criteria = new Criteria();
          String bestProvider = locationManager.getBestProvider(criteria, false);
          best = locationManager.getLastKnownLocation(bestProvider);
          
          if (best != null) {
              UpdateTask task = new UpdateTask(best.getLatitude(), best.getLongitude());
              task.execute();
          }
          
        }
        
        locationManager.requestLocationUpdates(               
                LocationManager.GPS_PROVIDER,1 * 60 * 1000,10, this);
        
        setContentView(R.layout.basic_demo);
        setUp();
    }

    @Override
    public boolean onCreateOptionsMenu(Menu menu) {
        // Inflate the menu; this adds items to the action bar if it is present.
        getMenuInflater().inflate(R.menu.activity_main, menu);
        return true;
    }
    
    @Override
    public boolean onOptionsItemSelected(MenuItem item) {
        Intent intent = null;
        switch(item.getItemId()) {
            case R.id.create_game:
                intent = new Intent(this, CreateGameActivity.class);
                break;
            case R.id.join_game:
                intent = new Intent(this, JoinGameActivity.class);
                break;
        }
        startActivity(intent);
        return super.onOptionsItemSelected(item);
    }
    
    @Override
    protected void onPause() {
        super.onPause();
        LocationManager locationManager = (LocationManager)getSystemService(Context.LOCATION_SERVICE);
        locationManager.removeUpdates(this);
        this.unregisterReceiver(mUpdateReceiver);
    }
    
    @Override
    protected void onResume() {
        super.onResume();
//        IntentFilter filter = new IntentFilter("com.phonetag.update");
        this.registerReceiver(mUpdateReceiver, new IntentFilter("com.phonetag.update"));
        LocationManager locationManager = (LocationManager)getSystemService(Context.LOCATION_SERVICE);
        locationManager.requestLocationUpdates(               
                LocationManager.GPS_PROVIDER,1 * 60 * 1000,10, this);
        setUp();
    }
    
    private void setUp() {
        // Do a null check to confirm that we have not already instantiated the map.
        if (mMap == null) {
            // Try to obtain the map from the SupportMapFragment.
            mMap = ((MapFragment) getFragmentManager().findFragmentById(R.id.map)).getMap();
            // Check if we were successful in obtaining the map.
            if (mMap != null) {
                mMap.moveCamera(CameraUpdateFactory.zoomTo(16));
                setUpMap();
            }
        } else {
            setUpMap();
        }
    }
    
    private void setUpMap() {
        mMap.setMyLocationEnabled(true);
        mMap.setOnInfoWindowClickListener(this);
        float zoom = mMap.getCameraPosition().zoom;
        mMap.moveCamera(CameraUpdateFactory.zoomTo(zoom));
        if (best != null) {
            mMap.moveCamera(
                    CameraUpdateFactory.newLatLngZoom(new LatLng(best.getLatitude(), best.getLongitude()), 10));
        }
        mMap.clear();
        mMap.moveCamera(CameraUpdateFactory.zoomTo(zoom));
        List<Game> games = Globals.getInstance().getGames();
        its = new HashSet<String>();
        if (games != null) {
            for (Game g : games) {
                if (g.getIt().equals(Globals.getInstance().getId())) {
                  its.add(g.getName());
               }
            }
        }
//            for (int i = 0; i < games.size(); i++) {
//                int color = i * 360 / games.size();
                List<User> users = Globals.getInstance().getUsers();
//                List<String> players = games.get(i).getUsers();
                if (users != null) {
                    for (User u : users) {
//                        if (players.contains(u.getPhoneID()) && !u.getPhoneID().equals(Globals.getInstance().getId())) {
                        if (!u.getPhoneID().equals(Globals.getInstance().getId())) {
                            mMap.addMarker(new MarkerOptions().position(new LatLng(u.getLatitude(), u.getLongitude()))
                                    .title(u.getName())
                                    .icon(BitmapDescriptorFactory.defaultMarker(BitmapDescriptorFactory.HUE_GREEN)));
                        }
                    }
                }
//                if (games.get(i).getIt().equals(Globals.getInstance().getId())) {
//                    its.add(games.get(i).getName());
//                }
//            }
//        }
        mMap.moveCamera(CameraUpdateFactory.zoomTo(zoom));
    }

    @Override
    public void onLocationChanged(Location location) {
        Log.e("LOCATION", "LOC CHANGED");
        Api.updateLoc(Globals.getInstance().getId(), location.getLatitude(), location.getLongitude());
    }

    @Override
    public void onProviderDisabled(String provider) {
        Log.e("LOCATION", "PROVIDER DISABLED");
        // TODO Auto-generated method stub
        
    }

    @Override
    public void onProviderEnabled(String provider) {
        Log.e("LOCATION", "PROVIDER ENABLED");
        // TODO Auto-generated method stub
        
    }

    @Override
    public void onStatusChanged(String provider, int status, Bundle extras) {
        // TODO Auto-generated method stub
        Log.e("LOCATION", "STATUS CHANGED");
    }
    
    private BroadcastReceiver mUpdateReceiver = new BroadcastReceiver() {        

        @Override
        public void onReceive(Context context, Intent intent) {
            setUp();
        }
    };

    @Override
    public void onInfoWindowClick(Marker marker) {
        Location loc = new Location(LocationManager.NETWORK_PROVIDER);
        loc.setLatitude(marker.getPosition().latitude);
        loc.setLongitude(marker.getPosition().longitude);
        List<Game> games = Globals.getInstance().getGames();
        List<User> users = Globals.getInstance().getUsers();
        User curruser = null;
        for (User u : users) {
            if (u.getName().equals(marker.getTitle())) {
                curruser = u;
            }
        }
        for (Game g : games) {
            if (its.contains(g.getName())) {
                List<String> players = g.getUsers();
                if (players.contains(curruser.getPhoneID()) && best.distanceTo(loc) < 200) {
                    TagTask task = new TagTask(g.getName(), marker.getTitle());
                    task.execute();
                    Toast.makeText(this, "TAGGED!", Toast.LENGTH_SHORT).show();
                    its.remove(g.getName());
                } else if (best.distanceTo(loc) >= 200) {
                    Toast.makeText(this, "Too far to tag!", Toast.LENGTH_SHORT).show();
                }
            }
        }
    }

}
