package com.phonetag.tasks;

import android.content.Context;
import android.os.AsyncTask;

import com.phonetag.util.Api;
import com.phonetag.util.Globals;

public class NewGameTask extends AsyncTask<Void, Void, Void> {
    
    public interface NewGameCallback {
        public void onFinish();
    }
    
    private String game;
    private Context mContext;
    private NewGameCallback callback;

    public NewGameTask(Context ctx, String gameName, NewGameCallback callback) {
        game = gameName;
        mContext = ctx;
        this.callback = callback;
    }

    @Override
    protected Void doInBackground(Void... params) {
        Api.newGame(mContext, Globals.getInstance().getId(), game);
        return null;
    }
    
    @Override
    protected void onPostExecute(Void result) {
        super.onPostExecute(result);
        callback.onFinish();
    }
}