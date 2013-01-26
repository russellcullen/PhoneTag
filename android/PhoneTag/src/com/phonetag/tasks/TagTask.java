package com.phonetag.tasks;

import android.os.AsyncTask;

import com.phonetag.util.Api;
import com.phonetag.util.Globals;

public class TagTask extends AsyncTask<Void, Void, Void> {
    
    private String other;
    private String game;

    public TagTask(String gameId, String otherName) {
        other = otherName;
        game = gameId;
    }

    @Override
    protected Void doInBackground(Void... params) {
        Api.tag(game, Globals.getInstance().getId(), other);
        return null;
    }
}