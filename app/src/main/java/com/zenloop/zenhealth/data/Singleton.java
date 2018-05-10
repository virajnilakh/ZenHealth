package com.zenloop.zenhealth.data;

/**
 * Created by viraj on 5/9/2018.
 */

public class Singleton {
    private static final Singleton ourInstance = new Singleton();
    private boolean isBgl=false;

    public boolean isBgl() {
        return isBgl;
    }

    public void setBgl(boolean bgl) {
        isBgl = bgl;
    }

    public static Singleton getInstance() {
        return ourInstance;
    }

    private Singleton() {
    }
}
