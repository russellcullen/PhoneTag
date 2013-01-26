
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

import com.google.android.gcm.GCMRegistrar;
import com.google.android.gms.maps.GoogleMap;
import com.google.android.gms.maps.GoogleMap.OnMarkerClickListener;
import com.google.android.gms.maps.MapFragment;
import com.google.android.gms.maps.model.LatLng;
import com.google.android.gms.maps.model.Marker;
import com.google.android.gms.maps.model.MarkerOptions;
import com.phonetag.models.User;
import com.phonetag.tasks.TagTask;
import com.phonetag.tasks.UpdateTask;
import com.phonetag.util.Api;
import com.phonetag.util.Globals;
import com.phonetag.util.Storage;

import java.util.List;

public class MainActivity extends Activity implements LocationListener, OnMarkerClickListener {
    
    private GoogleMap mMap;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        Storage.load(this);
        LocationManager locationManager = (LocationManager)getSystemService(LOCATION_SERVICE);
//        Globals.getInstance().setName(this, "coolbrow");
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
          Location location = locationManager.getLastKnownLocation(bestProvider);
          
          if (location != null) {
              UpdateTask task = new UpdateTask(location.getLatitude(), location.getLongitude());
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
    protected void onPause() {
        super.onPause();
        LocationManager locationManager = (LocationManager)getSystemService(Context.LOCATION_SERVICE);
        locationManager.removeUpdates(this);
//        this.unregisterReceiver(mUpdateReceiver);
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
            mMap = ((MapFragment) getFragmentManager().findFragmentById(R.id.map))
                    .getMap();
            // Check if we were successful in obtaining the map.
            if (mMap != null) {
                setUpMap();
            }
        } else {
            setUpMap();
        }
    }
    
    private void setUpMap() {
        mMap.setOnMarkerClickListener(this);
        List<User> users = Globals.getInstance().getUsers();
        if (users != null) {
            mMap.clear();
            for (User u : users) {
                mMap.addMarker(new MarkerOptions().position(new LatLng(u.getLatitude(), u.getLongitude())).title(u.getName()));
            }
        }
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
    public boolean onMarkerClick(Marker marker) {
        TagTask task = new TagTask("yoloswag", marker.getTitle());
        return false;
    }

}
