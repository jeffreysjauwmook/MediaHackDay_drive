package com.bosch.myspin.helloworld;

import android.content.Context;
import android.location.Location;
import android.os.Handler;
import android.webkit.JavascriptInterface;
import android.webkit.WebView;
import android.widget.Toast;

public class JsInterface {
    private Context context;
    private Handler handler;
    private WebView webView;
    private Location location;
    private String locationCallback;
    private String gestureCallback;

    public JsInterface(Context context, Handler handler, WebView webView) {
        this.context = context;
        this.handler = handler;
        this.webView = webView;
    }

    @JavascriptInterface
    public double getLat() {
        return location == null ? 0 : location.getLatitude();
    }

    @JavascriptInterface
    public double getLng() {
        return location == null ? 0 : location.getLongitude();
    }

    @JavascriptInterface
    public void setGestureCallback(String callbackName) {
        gestureCallback = callbackName;
    }

    @JavascriptInterface
    public void setLocationCallback(String callbackName) {
        locationCallback = callbackName;
        if (location != null) {
            sendLocation();
        }
    }

    private void loadUrl(final String url) {
        handler.post(new Runnable() {
            @Override
            public void run() {
                webView.loadUrl(url);
            }
        });
    }

    public void callJavascriptCallback(String name) {
        if (name == null) {
            return;
        }
        loadUrl("javascript:" + name + "()");
    }

    public void callJavascriptCallback(String name, Object... params) {
        String paramString = null;

        if (name == null) {
            return;
        }

        for (Object param : params) {
            if (paramString == null) {
                paramString = "";
            } else {
                paramString += ",";
            }

            if (param instanceof Integer || param instanceof Float || param instanceof Double) {
                paramString += param.toString();
            } else if (param instanceof String) {
                paramString += "\"" + ((String) param).replace("\"", "\\\"") + "\"";
            } else {
                throw new RuntimeException("Unsupported parameter type " + param.getClass().getCanonicalName());
            }
        }

        loadUrl("javascript:" + name + "(" + paramString + ")");
    }

    public void setLocation(Location location) {
        this.location = location;
        sendLocation();
    }

    private void sendLocation() {
        callJavascriptCallback(locationCallback, this.location.getLatitude(), this.location.getLongitude());
    }

    public void gesture(String gestureName) {
        callJavascriptCallback(gestureCallback, gestureName);
    }

    @JavascriptInterface
    public void showMessage(String message) {
        Toast.makeText(context, message, Toast.LENGTH_LONG).show();
    }
}
