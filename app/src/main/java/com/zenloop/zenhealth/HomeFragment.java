package com.zenloop.zenhealth;


import android.content.Context;
import android.content.res.Resources;
import android.os.Bundle;
import android.support.v4.app.Fragment;
import android.view.LayoutInflater;
import android.view.View;
import android.view.ViewGroup;
import android.widget.ArrayAdapter;
import android.widget.AutoCompleteTextView;
import android.widget.Spinner;

import com.zenloop.zenhealth.data.Singleton;
import com.zenloop.zenhealth.data.User;

import java.util.Arrays;

import io.realm.Realm;


/**
 * A simple {@link Fragment} subclass.
 */
public class HomeFragment extends Fragment implements EditTextDialogFragment.EditTextDialogFragmentListener  {


    private Realm realm;

    public HomeFragment() {
        // Required empty public constructor
    }
    String[][] items;
    /*String[][] items={{"Poached Egg on Toast with Chipotle Mayonnaise, Bacon and Avocado", "Ham Egg Cheese Breakfast Pizza", "Avocado Baked Eggs", "Guiltless Egg and Bacon Sandwich", "Full English Breakfast Traybake", "Crepe"},
            {"Quinoa Kale Pesto Bowls with Poached Eggs", "Crispy Hash Browns", "Perfect Hard Boiled Eggs", "Avocado Toast with Sunny Side Egg", "Scrambled Tofu", "Easy Spinach Pepper Egg Muffins"},
            {"Beef & Bean Chimichanga", "Mutton Biryani", "Easy Chicken & Cheese Quesadillas", "Borani Banjan", "Strawberry and Balsamic Grilled Chicken Salad", "Chili Mango Chicken Quesadillas"},
            {"Zucchini and Green Peas Coconut Curry", "Crispy & Chewy Sesame Shiitake", "Maple Glazed Baked Salmon", "Asian Garlic Tofu", "Moroccan Inspired Vegan Quinoa Chili"}};
//            items= new String[][]{{"Please Enter Blood Glucose Level"}, {"Please Enter Blood Glucose Level"}, {"Please Enter Blood Glucose Level"}};
*/
    @Override
    public View onCreateView(LayoutInflater inflater, ViewGroup container,
                             Bundle savedInstanceState) {
        // Inflate the layout for this fragment
        View v=inflater.inflate(R.layout.fragment_home, container, false);
        /*Realm.init(getContext());
        realm=Realm.getDefaultInstance();
        User user=realm.where(User.class).findFirst();*/
        if(true){
            items= new String[][]{{"Poached Egg on Toast with Chipotle Mayonnaise, Bacon and Avocado", "Ham Egg Cheese Breakfast Pizza", "Avocado Baked Eggs", "Guiltless Egg and Bacon Sandwich", "Full English Breakfast Traybake", "Crepe"},
                    {"Quinoa Kale Pesto Bowls with Poached Eggs", "Crispy Hash Browns", "Perfect Hard Boiled Eggs", "Avocado Toast with Sunny Side Egg", "Scrambled Tofu", "Easy Spinach Pepper Egg Muffins"},
                    {"Beef & Bean Chimichanga", "Mutton Biryani", "Easy Chicken & Cheese Quesadillas", "Borani Banjan", "Strawberry and Balsamic Grilled Chicken Salad", "Chili Mango Chicken Quesadillas"},
                    {"Zucchini and Green Peas Coconut Curry", "Crispy & Chewy Sesame Shiitake", "Maple Glazed Baked Salmon", "Asian Garlic Tofu", "Moroccan Inspired Vegan Quinoa Chili"}};
        }else{
            items= new String[][]{{"Please Enter Blood Glucose Level"}, {"Please Enter Blood Glucose Level"}, {"Please Enter Blood Glucose Level"}};

        }
        for(int i=1;i<=3;i++){
            Resources res = getResources();

            int id = res.getIdentifier("spinner"+i, "id", getContext().getPackageName());
            Spinner dropdown =(Spinner) v.findViewById(id);

            //String[] items = new String[]{"Quinoa Kale Pesto Bowls with Poached Eggs", "Crispy Hash Browns", "Perfect Hard Boiled Eggs", "Avocado Toast with Sunny Side Egg", "Scrambled Tofu", "Easy Spinach Pepper Egg Muffins"};
            //String[] items = new String[]{"Please Enter Blood Glucose Level."};

            ArrayAdapter<String> adapter1 = new ArrayAdapter<>(getContext(), android.R.layout.simple_spinner_dropdown_item, items[i-1]);
            dropdown.setAdapter(adapter1);
            dropdown.setSelection(0);

            id = res.getIdentifier("planets_spinner"+i, "id", getContext().getPackageName());

            AutoCompleteTextView auto=(AutoCompleteTextView) v.findViewById(id);
            //Spinner spinner = (Spinner) v.findViewById(R.id.planets_spinner);
// Create an ArrayAdapter using the string array and a default spinner layout
            ArrayAdapter<String> adapter =new ArrayAdapter<String>(
                    getContext(),
                    android.R.layout.simple_dropdown_item_1line,items[i-1]);

// Specify the layout to use when the list of choices appears
            adapter.setDropDownViewResource(android.R.layout.simple_spinner_dropdown_item);
            auto.setAdapter(adapter);
            auto.setThreshold(2);
// Apply the adapter to the spinner
            //spinner.setAdapter(adapter);
        }

        return v;
    }


    @Override
    public void onEditTextDialogFragmentOK(String newValue, String tag) {
        System.out.println("Value:"+newValue);
        System.out.println("Value:"+newValue);
    }
}
