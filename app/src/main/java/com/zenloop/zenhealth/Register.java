package com.zenloop.zenhealth;

import android.content.Intent;
import android.provider.DocumentsContract;
import android.support.annotation.NonNull;
import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;
import android.util.Log;
import android.view.View;
import android.widget.TextView;

import com.google.android.gms.tasks.Continuation;
import com.google.android.gms.tasks.OnCompleteListener;
import com.google.android.gms.tasks.Task;
import com.mongodb.stitch.android.StitchClient;
import com.mongodb.stitch.android.auth.anonymous.AnonymousAuthProvider;
import com.mongodb.stitch.android.services.mongodb.MongoClient;

import org.bson.Document;

import java.util.List;

public class Register extends AppCompatActivity {

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_register);

    }

    public void connectDb(View view) {
        final TextView fname=(TextView) findViewById(R.id.fname);
        final TextView lname=(TextView) findViewById(R.id.lname);
        final TextView email=(TextView) findViewById(R.id.email);
        final TextView password=(TextView) findViewById(R.id.password);
        final String fnamestr=fname.getText().toString();
        final String lnamestr=lname.getText().toString();
        final String emailstr=email.getText().toString();
        final String passwordstr=password.getText().toString();
        final StitchClient stitchClient = new StitchClient(view.getContext(), "zenhealth-ycmlc");
        final MongoClient mongoClient = new MongoClient(stitchClient, "mongodb-atlas");
        final MongoClient.Database db = mongoClient.getDatabase("ZenHealth");

        stitchClient.logInWithProvider(new AnonymousAuthProvider()).continueWithTask(
                new Continuation<String, Task<Document>>() {
                    @Override
                    public Task<Document> then(@NonNull Task<String> task) throws Exception {
                        final Document updateDoc = new Document("owner_id",task.getResult());

                        /*updateDoc.put("fname", fname.getText());
                        updateDoc.put("lname", lname.getText());
                        updateDoc.put("email", email.getText());
                        updateDoc.put("password", password.getText());*/
                        updateDoc.put("fname", fnamestr);
                        updateDoc.put("lname", lnamestr);
                        updateDoc.put("email", emailstr);
                        updateDoc.put("password", passwordstr);
                        return db.getCollection("Users").insertOne(updateDoc);
                    }
                }
        ).continueWithTask(new Continuation<Document, Task<List<Document>>>() {
            @Override
            public Task<List<Document>> then(@NonNull Task<Document> task) throws Exception {
                if (!task.isSuccessful()) {
                    throw task.getException();
                }
                return db.getCollection("Users").find(
                        new Document("owner_id", stitchClient.getUserId()),
                        100
                );
            }
        }).addOnCompleteListener(new OnCompleteListener<List<Document>>() {
            @Override
            public void onComplete(@NonNull Task<List<Document>> task) {
                if (task.isSuccessful()) {
                    Log.d("STITCH", task.getResult().toString());
                    Intent myIntent = new Intent(Register.this, LoginActivity.class);
                    startActivity(myIntent);
                    return;
                }
                Log.e("STITCH", task.getException().toString());
            }
        });

    }
}