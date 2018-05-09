package com.zenloop.zenhealth;

import android.content.Intent;
import android.support.annotation.NonNull;
import android.support.design.widget.BottomNavigationView;
import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;
import android.view.MenuItem;
import android.view.View;

public class Onboarding extends AppCompatActivity {
    /*private Intent myIntent;
    private BottomNavigationView.OnNavigationItemSelectedListener mOnNavigationItemSelectedListener
            = new BottomNavigationView.OnNavigationItemSelectedListener() {

        @Override
        public boolean onNavigationItemSelected(@NonNull MenuItem item) {
            switch (item.getItemId()) {
                case R.id.navigation_home:
                    myIntent = new Intent(Onboarding.this, HomeActivity.class);
                    startActivity(myIntent);
                    return true;
                case R.id.navigation_dashboard:
                    myIntent = new Intent(Onboarding.this, Onboarding.class);
                    startActivity(myIntent);
                    return true;
                case R.id.navigation_notifications:
                    myIntent = new Intent(Onboarding.this, ActivityPage.class);
                    startActivity(myIntent);
                    return true;
            }
            return false;
        }
    };*/
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.fragment_onboarding);
        /*BottomNavigationView navigation = (BottomNavigationView) findViewById(R.id.navigation);
        navigation.setOnNavigationItemSelectedListener(mOnNavigationItemSelectedListener);*/
    }
    public void goToLogin(View view) {
        Intent myIntent = new Intent(Onboarding.this, LoginActivity.class);
        startActivity(myIntent);
    }
}
