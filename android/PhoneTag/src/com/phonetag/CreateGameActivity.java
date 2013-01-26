package com.phonetag;

import android.app.Activity;
import android.os.Bundle;
import android.util.Log;
import android.view.View;
import android.view.View.OnClickListener;
import android.widget.Button;
import android.widget.EditText;

import com.phonetag.tasks.NewGameTask;
import com.phonetag.tasks.NewGameTask.NewGameCallback;
import com.phonetag.util.Globals;

public class CreateGameActivity extends Activity implements NewGameCallback {
    
    private EditText mName;
    
    @Override
    public void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        
        setContentView(R.layout.start_activity);
        
        getActionBar().hide();
        
        mName = (EditText) findViewById(R.id.fridge);
        mName.setHint("Enter game name");
        
        Button go = (Button) findViewById(R.id.start);
        go.setOnClickListener(new OnClickListener() {
            
            @Override
            public void onClick(View v) {
                String name = mName.getText().toString();
                NewGameTask task = new NewGameTask(CreateGameActivity.this, name, CreateGameActivity.this);
                task.execute();
            }
        });
        
    }

    @Override
    public void onFinish() {
        this.finish();
    }
}
