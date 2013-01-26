
package com.phonetag;

import android.app.Activity;
import android.content.Context;
import android.location.Criteria;
import android.location.Location;
import android.location.LocationListener;
import android.location.LocationManager;
import android.os.Bundle;
import android.util.Log;
import android.view.Menu;

import com.google.android.gcm.GCMRegistrar;
import com.phonetag.tasks.UpdateTask;
import com.phonetag.util.Api;
import com.phonetag.util.Globals;
import com.phonetag.util.Storage;

public class MainActivity extends Activity implements LocationListener {

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
        
        setContentView(R.layout.activity_main);
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
    }
    
    @Override
    protected void onResume() {
        super.onResume();
        LocationManager locationManager = (LocationManager)getSystemService(Context.LOCATION_SERVICE);
        locationManager.requestLocationUpdates(               
                LocationManager.GPS_PROVIDER,1 * 60 * 1000,10, this);
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

}
