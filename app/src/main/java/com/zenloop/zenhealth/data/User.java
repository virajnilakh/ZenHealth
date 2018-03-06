package com.zenloop.zenhealth.data;

import io.realm.RealmObject;
import io.realm.annotations.PrimaryKey;

/**
 * Created by viraj on 3/4/2018.
 */

public class User extends RealmObject {
    @PrimaryKey
    private String username=null;

    public User() {
    }

    public String getUsername() {
        return username;
    }

    public void setUsername(String username) {
        this.username = username;
    }

    public User(String username) {
        this.username = username;
    }
}
