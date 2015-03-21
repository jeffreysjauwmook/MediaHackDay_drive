package com.bosch.myspin.helloworld;

public interface ApiResponseCallback {
    public void onError(int responseCode, String response);
    public void onSuccess();
}
