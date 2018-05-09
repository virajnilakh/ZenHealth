package com.zenloop.zenhealth;

import android.app.Fragment;
import android.content.Intent;
import android.content.res.Resources;
import android.support.annotation.NonNull;
import android.support.design.widget.BottomNavigationView;
import android.support.v4.app.FragmentTransaction;
import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;
import android.view.MenuItem;
import android.view.View;
import android.widget.ArrayAdapter;
import android.widget.Spinner;
import android.widget.TextView;

import com.zenloop.zenhealth.data.User;

import io.realm.Realm;
import io.realm.RealmResults;

public class Navigation extends AppCompatActivity implements EditTextDialogFragment.EditTextDialogFragmentListener {

    public static final String DIALOG_TAG = "dialog_tag";
    private Realm realm;
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
/*
            View floatingButton = findViewById(R.id.floatingActionButton);
*/
            View sendPDF = findViewById(R.id.sendPDFButton);
            switch (item.getItemId()) {
                case R.id.navigation_home:
/*
                    floatingButton.setVisibility(View.VISIBLE);
*/
                    sendPDF.setVisibility(View.GONE);

                    transaction = getSupportFragmentManager().beginTransaction();
                    HomeFragment homeFragment=new HomeFragment();
                    transaction.replace(R.id.fragment_container, homeFragment);
                    transaction.addToBackStack(null);

                    transaction.commit();
                    return true;
                case R.id.navigation_dashboard:
/*
                    floatingButton.setVisibility(View.GONE);
*/
                    sendPDF.setVisibility(View.GONE);

                    transaction = getSupportFragmentManager().beginTransaction();
                    OnboardingFragment onboardingFragment=new OnboardingFragment();
                    transaction.replace(R.id.fragment_container, onboardingFragment);
                    transaction.addToBackStack(null);

                    transaction.commit();
                    return true;
                case R.id.navigation_notifications:
/*
                    floatingButton.setVisibility(View.VISIBLE);
*/
                    sendPDF.setVisibility(View.VISIBLE);
                    transaction = getSupportFragmentManager().beginTransaction();
                    ActivityFragment activityFragment=new ActivityFragment();
                    transaction.replace(R.id.fragment_container, activityFragment);
                    transaction.addToBackStack(null);

                    transaction.commit();
                    return true;
                case R.id.add_bgl:


                    EditTextDialogFragment editTextDialogFragment=EditTextDialogFragment.newInstance("Enter blood glucose level:","");
                    editTextDialogFragment.show(getSupportFragmentManager(), DIALOG_TAG);
                    return true;

                case R.id.logout:
/*
                    floatingButton.setVisibility(View.GONE);
*/
                    sendPDF.setVisibility(View.GONE);

                    Realm.init(getBaseContext());
                    realm=Realm.getDefaultInstance();
                    realm.beginTransaction();
                    RealmResults<User> result = realm.where(User.class).findAll();
                    result.deleteAllFromRealm();
                    realm.commitTransaction();
                    Intent myIntent = new Intent(Navigation.this, LoginActivity.class);
                    startActivity(myIntent);
                    return true;


            }
            return false;
        }
    };

    public void enterBGL(View view) {
        EditTextDialogFragment editTextDialogFragment=EditTextDialogFragment.newInstance("Enter blood glucose level:","");
        editTextDialogFragment.show(getSupportFragmentManager(), DIALOG_TAG);
    }

    @Override
    public void onEditTextDialogFragmentOK(String newValue, String tag) {
        System.out.println("Value:"+newValue);
        System.out.println("Value:"+newValue);
    }

    public void enableList(View view) {
        String tag = view.getTag().toString();
        Resources res = getResources();
        int id = res.getIdentifier("title"+tag, "id", this.getPackageName());
        TextView title=(TextView) findViewById(id);
        title.setText("Type your choice");
        id = res.getIdentifier("spinner"+tag, "id", this.getPackageName());
        View food= findViewById(id);
        food.setVisibility(View.GONE);
        id = res.getIdentifier("planets_spinner"+tag, "id", this.getPackageName());
        View spinner= findViewById(id);

        spinner.setVisibility(View.VISIBLE);

    }

    public void disableButtons(View view) {
        String tag = view.getTag().toString();
        Resources res = getResources();
        int id = res.getIdentifier("acceptButton"+tag, "id", this.getPackageName());
        View acceptButton=findViewById(id);
        id = res.getIdentifier("denyButton"+tag, "id", this.getPackageName());

        View denyButton=findViewById(id);
        acceptButton.setVisibility(View.GONE);
        denyButton.setVisibility(View.GONE);
    }
}
