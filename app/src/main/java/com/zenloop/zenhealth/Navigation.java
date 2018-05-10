package com.zenloop.zenhealth;

import android.content.Intent;
import android.content.res.Resources;
import android.graphics.pdf.PdfDocument;
import android.os.Bundle;
import android.support.annotation.NonNull;
import android.support.constraint.ConstraintLayout;
import android.support.design.widget.BottomNavigationView;
import android.support.design.widget.Snackbar;
import android.support.v4.app.FragmentTransaction;
import android.support.v7.app.AppCompatActivity;
import android.view.MenuItem;
import android.view.View;
import android.widget.TextView;

import com.zenloop.zenhealth.data.Singleton;
import com.zenloop.zenhealth.data.User;

import java.io.File;
import java.io.FileOutputStream;
import java.io.IOException;
import java.io.OutputStream;
import java.text.SimpleDateFormat;
import java.util.Calendar;

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
            View sendPdf = findViewById(R.id.sendPDFButton);
            switch (item.getItemId()) {
                case R.id.navigation_home:
/*
                    floatingButton.setVisibility(View.VISIBLE);
*/
                    sendPdf.setVisibility(View.GONE);

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
                    sendPdf.setVisibility(View.GONE);

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
                    sendPdf.setVisibility(View.VISIBLE);
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
                    sendPdf.setVisibility(View.GONE);

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
        Singleton.getInstance().setBgl(true);
        /*Realm.init(this);
        realm=Realm.getDefaultInstance();
        User user=realm.where(User.class).findFirst();
        user.setBgl(true);
        *//*try {
            realm.beginTransaction();
            realm.copyToRealm(new User(DUMMY_CREDENTIALS.get(0).split(":")[0]));
            realm.commitTransaction();
        } catch (Exception e) {
            realm.cancelTransaction();
            e.printStackTrace();
        }*/
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


    public void createPdf(View view) {
        final ConstraintLayout constraintLayout = (ConstraintLayout) view.findViewById(R.id.constraint);

        PdfDocument document = new PdfDocument();

        // repaint the user's text into the page
        TextView text=new TextView(view.getContext());
        text.setText("hii");
        View content = text;

        // crate a page description
        int pageNumber = 1;
        PdfDocument.PageInfo pageInfo = new PdfDocument.PageInfo.Builder(100,
                100, pageNumber).create();

        // create a new page from the PageInfo
        PdfDocument.Page page = document.startPage(pageInfo);

        content.draw(page.getCanvas());

        // do final processing of the page
        document.finishPage(page);

        SimpleDateFormat sdf = new SimpleDateFormat("ddMMyyyyhhmmss");
        String pdfName = "pdfdemo"
                + sdf.format(Calendar.getInstance().getTime()) + ".pdf";

        File outputFile = new File("/sdcard/", pdfName);

        try {
            outputFile.createNewFile();
            OutputStream out = new FileOutputStream(outputFile);
            document.writeTo(out);
            document.close();
            out.close();
            /*Snackbar snackbar = Snackbar
                    .make(constraintLayout, "Pdf created!!", Snackbar.LENGTH_LONG);
            snackbar.show();*/
        } catch (IOException e) {
            e.printStackTrace();
        }

    }
}
