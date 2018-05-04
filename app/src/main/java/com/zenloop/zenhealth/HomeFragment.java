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


/**
 * A simple {@link Fragment} subclass.
 */
public class HomeFragment extends Fragment {


    public HomeFragment() {
        // Required empty public constructor
    }


    @Override
    public View onCreateView(LayoutInflater inflater, ViewGroup container,
                             Bundle savedInstanceState) {
        // Inflate the layout for this fragment
        View v=inflater.inflate(R.layout.fragment_home, container, false);
        for(int i=1;i<=3;i++){
            Resources res = getResources();

            int id = res.getIdentifier("planets_spinner"+i, "id", getContext().getPackageName());
            AutoCompleteTextView auto=(AutoCompleteTextView) v.findViewById(id);
            //Spinner spinner = (Spinner) v.findViewById(R.id.planets_spinner);
// Create an ArrayAdapter using the string array and a default spinner layout
            ArrayAdapter<CharSequence> adapter = ArrayAdapter.createFromResource(this.getActivity(),
                    R.array.planets_array, android.R.layout.simple_spinner_item);

// Specify the layout to use when the list of choices appears
            adapter.setDropDownViewResource(android.R.layout.simple_spinner_dropdown_item);
            auto.setAdapter(adapter);
            auto.setThreshold(2);
// Apply the adapter to the spinner
            //spinner.setAdapter(adapter);
        }

        return v;
    }


}
