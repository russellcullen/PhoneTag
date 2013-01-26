package com.phonetag.tasks;

import android.os.AsyncTask;

import com.phonetag.util.Api;
import com.phonetag.util.Globals;

public class UpdateTask extends AsyncTask<Void, Void, Void> {
    
    private double lat;
    private double lng;

    public UpdateTask(double lat, double lng) {
        this.lat = lat;
        this.lng = lng;
    }

    @Override
    protected Void doInBackground(Void... params) {
        Api.updateLoc(Globals.getInstance().getId(), lat, lng);
        return null;
    }
}