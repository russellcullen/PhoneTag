package com.phonetag.tasks;

import android.content.Context;
import android.os.AsyncTask;

import com.phonetag.util.Api;
import com.phonetag.util.Globals;

public class JoinGameTask extends AsyncTask<Void, Void, Void> {
    
    public interface JoinGameCallback {
        public void onFinish();
    }
    
    private String game;
    private Context mContext;
    private JoinGameCallback callback;

    public JoinGameTask(Context ctx, String gameName, JoinGameCallback callback) {
        game = gameName;
        mContext = ctx;
        this.callback = callback;
    }

    @Override
    protected Void doInBackground(Void... params) {
        Api.joinGame(mContext, Globals.getInstance().getId(), game);
        return null;
    }
    
    @Override
    protected void onPostExecute(Void result) {
        super.onPostExecute(result);
        callback.onFinish();
    }
}