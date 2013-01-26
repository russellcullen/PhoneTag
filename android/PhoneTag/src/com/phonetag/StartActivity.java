package com.phonetag;

import android.app.Activity;
import android.content.Intent;
import android.os.Bundle;
import android.view.View;
import android.view.View.OnClickListener;
import android.widget.Button;
import android.widget.EditText;

import com.phonetag.util.Globals;
import com.phonetag.util.Storage;

public class StartActivity extends Activity {
    
    private EditText mName;
    
    @Override
    public void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        Storage.load(this);
        if (Globals.getInstance().getName() != null) {
            startMain();
            return;
        }
        
        setContentView(R.layout.start_activity);
        
        getActionBar().hide();
        
        mName = (EditText) findViewById(R.id.fridge);
        
        Button go = (Button) findViewById(R.id.start);
        go.setOnClickListener(new OnClickListener() {
            
            @Override
            public void onClick(View v) {
                String name = mName.getText().toString();
                Globals.getInstance().setName(StartActivity.this, name);
                startMain();
            }
        });
        
    }
    
    public void startMain() {
        Intent i = new Intent(this, MainActivity.class);
        startActivity(i);
        finish();
    }
}
