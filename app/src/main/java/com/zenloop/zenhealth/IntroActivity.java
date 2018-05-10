package com.zenloop.zenhealth;

import android.content.Intent;
import android.content.res.Resources;
import android.graphics.Color;
import android.graphics.Typeface;
import android.graphics.drawable.Drawable;
import android.support.annotation.DrawableRes;
import android.support.annotation.Nullable;
import android.support.v4.app.Fragment;
import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;

import com.github.paolorotolo.appintro.AppIntro;
import com.github.paolorotolo.appintro.AppIntroFragment;
import com.github.paolorotolo.appintro.model.SliderPage;
import com.zenloop.zenhealth.data.User;

import io.realm.Realm;

public class IntroActivity extends AppIntro {
    private Realm realm;

    @Override
    protected void onCreate(@Nullable Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        Realm.init(this);
        realm=Realm.getDefaultInstance();
        User user=realm.where(User.class).findFirst();
        if(user!=null){
            Intent myIntent = new Intent(IntroActivity.this, Navigation.class);
            startActivity(myIntent);
        }
        // Note here that we DO NOT use setContentView();

        // Add your slide fragments here.
        // AppIntro will automatically generate the dots indicator and buttons.
       /* addSlide(firstFragment);
        addSlide(secondFragment);
        addSlide(thirdFragment);
        addSlide(fourthFragment);*/
        SliderPage sliderPage1 = new SliderPage();
        sliderPage1.setTitle("Are you a diabetic?");
        sliderPage1.setDescription("Do you think twice before deciding what to eat?");
        sliderPage1.setImageDrawable(R.drawable.dinner);
        sliderPage1.setBgColor(Color.TRANSPARENT);


        addSlide(AppIntroFragment.newInstance(sliderPage1));
        SliderPage sliderPage2 = new SliderPage();
        sliderPage2.setTitle("You are in the right place!");
        sliderPage2.setDescription("Just register into our app and enter your blood glucose level.");
        sliderPage2.setImageDrawable(R.drawable.lunch);
        sliderPage2.setBgColor(Color.TRANSPARENT);
        addSlide(AppIntroFragment.newInstance(sliderPage2));

        SliderPage sliderPage3 = new SliderPage();
        sliderPage3.setTitle("And we will do that for you!");
        sliderPage3.setDescription("We will provide you food recommendations and monitor the blood glucose level.");
        sliderPage3.setImageDrawable(R.drawable.graph);
        sliderPage3.setBgColor(Color.TRANSPARENT);
        addSlide(AppIntroFragment.newInstance(sliderPage3));


        // OPTIONAL METHODS
        // Override bar/separator color.
        setBarColor(Color.parseColor("#3F51B5"));
        setSeparatorColor(Color.parseColor("#2196F3"));

        // Hide Skip/Done button.
        showSkipButton(true);
        setProgressButtonEnabled(true);

        // Turn vibration on and set intensity.
        // NOTE: you will probably need to ask VIBRATE permission in Manifest.
        /*setVibrate(true);
        setVibrateIntensity(30);*/
    }

    @Override
    public void onSkipPressed(Fragment currentFragment) {
        super.onSkipPressed(currentFragment);
        // Do something when users tap on Skip button.
        Intent myIntent = new Intent(IntroActivity.this, LoginActivity.class);
        startActivity(myIntent);
        finish();
    }

    @Override
    public void onDonePressed(Fragment currentFragment) {
        super.onDonePressed(currentFragment);
        // Do something when users tap on Done button.
        Intent myIntent = new Intent(IntroActivity.this, LoginActivity.class);
        startActivity(myIntent);
        finish();
    }

    @Override
    public void onSlideChanged(@Nullable Fragment oldFragment, @Nullable Fragment newFragment) {
        super.onSlideChanged(oldFragment, newFragment);
        // Do something when the slide changes.
    }
}
