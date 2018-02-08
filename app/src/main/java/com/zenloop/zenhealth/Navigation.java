package com.zenloop.zenhealth;

import android.app.Fragment;
import android.content.Intent;
import android.support.annotation.NonNull;
import android.support.design.widget.BottomNavigationView;
import android.support.v4.app.FragmentTransaction;
import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;
import android.view.MenuItem;

public class Navigation extends AppCompatActivity {

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_navigation);
        if (findViewById(R.id.fragment_container) != null) {

            // However, if we're being restored from a previous state,
            // then we don't need to do anything and should return or else
            // we could end up with overlapping fragments.
            if (savedInstanceState != null) {
                return;
            }

            // Create a new Fragment to be placed in the activity layout
            HomeFragment home = new HomeFragment();

            // In case this activity was started with special instructions from an
            // Intent, pass the Intent's extras to the fragment as arguments
            //home.setArguments(getIntent().getExtras());

            // Add the fragment to the 'fragment_container' FrameLayout
            getSupportFragmentManager().beginTransaction()
                    .add(R.id.fragment_container, home).commit();
        }
        BottomNavigationView navigation = (BottomNavigationView) findViewById(R.id.navigation);
        navigation.setOnNavigationItemSelectedListener(mOnNavigationItemSelectedListener);

    }
    FragmentTransaction transaction;

    private BottomNavigationView.OnNavigationItemSelectedListener mOnNavigationItemSelectedListener
            = new BottomNavigationView.OnNavigationItemSelectedListener() {

        @Override
        public boolean onNavigationItemSelected(@NonNull MenuItem item) {
            switch (item.getItemId()) {
                case R.id.navigation_home:
                    transaction = getSupportFragmentManager().beginTransaction();
                    HomeFragment homeFragment=new HomeFragment();
                    transaction.replace(R.id.fragment_container, homeFragment);
                    transaction.addToBackStack(null);

                    transaction.commit();
                    return true;
                case R.id.navigation_dashboard:
                    transaction = getSupportFragmentManager().beginTransaction();
                    OnboardingFragment onboardingFragment=new OnboardingFragment();
                    transaction.replace(R.id.fragment_container, onboardingFragment);
                    transaction.addToBackStack(null);

                    transaction.commit();
                    return true;
                case R.id.navigation_notifications:
                    transaction = getSupportFragmentManager().beginTransaction();
                    ActivityFragment activityFragment=new ActivityFragment();
                    transaction.replace(R.id.fragment_container, activityFragment);
                    transaction.addToBackStack(null);

                    transaction.commit();
                    return true;
            }
            return false;
        }
    };
}
