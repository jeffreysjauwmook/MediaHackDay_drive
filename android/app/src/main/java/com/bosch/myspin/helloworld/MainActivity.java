package com.bosch.myspin.helloworld;

import android.content.Intent;
import android.location.Location;
import android.location.LocationListener;
import android.location.LocationManager;
import android.os.Build;
import android.os.Bundle;
import android.os.Handler;
import android.support.v7.app.ActionBarActivity;
import android.util.Log;
import android.view.KeyEvent;
import android.view.Menu;
import android.view.MenuItem;
import android.view.Window;
import android.webkit.WebView;
import android.webkit.WebViewClient;
import android.widget.Toast;

import com.bosch.myspin.serversdk.MySpinException;
import com.bosch.myspin.serversdk.MySpinServerSDK;
import com.thalmic.myo.AbstractDeviceListener;
import com.thalmic.myo.Hub;
import com.thalmic.myo.Myo;
import com.thalmic.myo.Pose;
import com.thalmic.myo.scanner.ScanActivity;


public class MainActivity extends ActionBarActivity {
    private final static String TAG = MainActivity.class.getCanonicalName();

    private final String EMULATOR_URL = "http://10.0.2.2/~p.hooijenga/mediahackday/";
    private final String URL = "http://mediahackday.gehekt.nl/";
    private final String API_URL = "http://backend.mediahackday.gehekt.nl/";

    private Handler handler;
    private WebView webView;
    private JsInterface jsInterface;
    private boolean usingMyo;
    private boolean usingMySpin;
    private LocationManager locationManager;
    private ApiClient apiClient;
    private boolean loggedIn;

    private AbstractDeviceListener myoDeviceListener = new AbstractDeviceListener() {
        @Override
        public void onConnect(Myo myo, long timestamp) {
            Toast.makeText(MainActivity.this, "Myo Connected!", Toast.LENGTH_SHORT).show();
        }

        @Override
        public void onDisconnect(Myo myo, long timestamp) {
            Toast.makeText(MainActivity.this, "Myo Disconnected!", Toast.LENGTH_SHORT).show();
        }

        @Override
        public void onPose(Myo myo, long timestamp, Pose pose) {
            Toast.makeText(MainActivity.this, "Pose: " + pose, Toast.LENGTH_SHORT).show();

            jsInterface.gesture(pose.name());
        }
    };

    private LocationListener locationListener = new LocationListener() {
        public void onLocationChanged(Location location) {
            Log.i(TAG, String.format("LocationListener.onLocationChanged location=%s", location.toString()));
            jsInterface.setLocation(location);

            if (loggedIn) {
                apiClient.updateLocation(location);
            }
        }

        public void onStatusChanged(String provider, int status, Bundle extras) {
            Log.i(TAG, String.format("LocationListener.onStatusChanged provider=%s, status=%d", provider, status));
        }

        public void onProviderEnabled(String provider) {
            Log.i(TAG, String.format("LocationListener.onProviderEnabled provider=%s", provider));
        }

        public void onProviderDisabled(String provider) {
            Log.i(TAG, String.format("LocationListener.onProviderDisabled provider=%s", provider));
        }
    };

    public static boolean isEmulator() {
        Log.i(TAG, Build.FINGERPRINT);
        return Build.FINGERPRINT.startsWith("generic");
    }

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        getWindow().requestFeature(Window.FEATURE_NO_TITLE);

        super.onCreate(savedInstanceState);

        setContentView(R.layout.activity_main);

        handler = new Handler();

        webView = (WebView)findViewById(R.id.webView);
        webView.getSettings().setJavaScriptEnabled(true);
        webView.setWebViewClient(new WebViewClient() {
            @Override
            public boolean shouldOverrideUrlLoading(WebView view, String url) {
                view.loadUrl(url);
                return true;
            }
        });

        jsInterface = new JsInterface(this, handler, webView);
        webView.addJavascriptInterface(jsInterface, "app");

        webView.loadUrl((isEmulator() ? EMULATOR_URL : URL) + "login.html");

        loggedIn = false;
        apiClient = new ApiClient(API_URL);

        initMyo();
        initMySpin();
        initLocation();
    }

    public void login(String username, String password) {
        apiClient.login(username, password, new ApiResponseCallback() {
            @Override
            public void onError(int responseCode, String response) {
            }

            @Override
            public void onSuccess() {
                loggedIn = true;
                handler.post(new Runnable() {
                    @Override
                    public void run() {
                        webView.loadUrl(isEmulator() ? EMULATOR_URL : URL);
                    }
                });
            }
        });
    }

    private void initMySpin() {
        try {
            MySpinServerSDK.sharedInstance().registerApplication(this.getApplication());
        } catch (MySpinException e) {
            Log.e(TAG, "Unable to register application with MySpinServerSDK", e);
            usingMySpin = false;
        }

        usingMySpin = MySpinServerSDK.sharedInstance().isConnected();
    }

    private void initMyo() {
        Hub hub = Hub.getInstance();
        usingMyo = hub.init(this);

        if (usingMyo) {
            hub.attachToAdjacentMyo();
            hub.addListener(myoDeviceListener);
        } else {
            Log.e(TAG, "Could not initialize the Hub.");
            Toast.makeText(this, "Myo not supported.", Toast.LENGTH_LONG).show();
        }
    }

    private void initLocation() {
        locationManager = (LocationManager)this.getSystemService(LOCATION_SERVICE);

        try {
            locationManager.requestLocationUpdates(LocationManager.NETWORK_PROVIDER, 500, 0, locationListener);
        } catch (IllegalArgumentException e) {
            Log.e(TAG, "requestLocationUpdates NETWORK_PROVIDER", e);
        }

        try {
            locationManager.requestLocationUpdates(LocationManager.GPS_PROVIDER, 500, 0, locationListener);
        } catch (IllegalArgumentException e) {
            Log.e(TAG, "requestLocationUpdates GPS_PROVIDER", e);
        }

        Location l = locationManager.getLastKnownLocation(LocationManager.GPS_PROVIDER);
        if (l == null) {
            l = locationManager.getLastKnownLocation(LocationManager.NETWORK_PROVIDER);
        }
        if (l != null) {
            locationListener.onLocationChanged(l);
        }
    }

    @Override
    protected void onPause() {
        super.onPause();

        if (usingMyo) {
            Hub.getInstance().removeListener(myoDeviceListener);
        }

        locationManager.removeUpdates(locationListener);
    }

    @Override
    protected void onResume() {
        super.onResume();
        initLocation();
    }

    @Override
    public boolean onKeyDown(final int keyCode, final KeyEvent event) {
        if ((keyCode == KeyEvent.KEYCODE_BACK) && webView.canGoBack()) {
            webView.goBack();
            return true;
        }
        return super.onKeyDown(keyCode, event);
    }

    @Override
    public boolean onCreateOptionsMenu(Menu menu) {
        // Inflate the menu; this adds items to the action bar if it is present.
        getMenuInflater().inflate(R.menu.menu_main, menu);
        return true;
    }

    @Override
    public boolean onOptionsItemSelected(MenuItem item) {
        // Handle action bar item clicks here. The action bar will
        // automatically handle clicks on the Home/Up button, so long
        // as you specify a parent activity in AndroidManifest.xml.
        int id = item.getItemId();

        switch (id) {
            case R.id.action_settings:
                return true;

            case R.id.action_scan_myo:
                Intent intent = new Intent(this, ScanActivity.class);
                startActivity(intent);
                return true;

            default:
                return super.onOptionsItemSelected(item);
        }
    }
}
