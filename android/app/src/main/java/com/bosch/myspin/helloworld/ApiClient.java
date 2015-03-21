package com.bosch.myspin.helloworld;

import android.location.Location;
import android.os.AsyncTask;
import android.util.Log;

import org.apache.commons.io.IOUtils;
import org.apache.http.HttpResponse;
import org.apache.http.HttpStatus;
import org.apache.http.NameValuePair;
import org.apache.http.StatusLine;
import org.apache.http.client.ClientProtocolException;
import org.apache.http.client.HttpClient;
import org.apache.http.client.entity.UrlEncodedFormEntity;
import org.apache.http.client.methods.HttpGet;
import org.apache.http.client.methods.HttpPost;
import org.apache.http.cookie.Cookie;
import org.apache.http.impl.client.DefaultHttpClient;
import org.apache.http.message.BasicNameValuePair;

import java.io.IOException;
import java.io.InputStream;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

public class ApiClient {
    private final String TAG = ApiClient.class.getCanonicalName();

    private String baseUrl;
    private DefaultHttpClient httpClient;
    private String csrfToken;

    public ApiClient(String baseUrl) {
        this.baseUrl = baseUrl;
        httpClient = new DefaultHttpClient();
    }

    public void login(final String username, final String password, final ApiResponseCallback callback) {
        /* Do a GET first to get the anti-CSRF cookie. */
        get("login/", new ApiResponseCallback() {
            @Override
            public void onError(int responseCode, String response) {
            }

            @Override
            public void onSuccess() {
                post("login/", callback,
                        new BasicNameValuePair("username", username),
                        new BasicNameValuePair("password", password));
            }
        });
    }

    public void updateLocation(Location location) {
        post("api/v1.0/my-location/", null,
                new BasicNameValuePair("lat", Double.toString(location.getLatitude())),
                new BasicNameValuePair("lng", Double.toString(location.getLongitude())),
                new BasicNameValuePair("speed", Float.toString(location.getSpeed())));
    }

    /* Extract the CSRF token from the response Cookies. */
    public void updateCsrfToken() {
        for (Cookie cookie : httpClient.getCookieStore().getCookies()) {
            if (cookie.getName().equals("csrftoken")) {
                csrfToken = cookie.getValue();
            }
        }
    }

    private void get(String url, ApiResponseCallback callback) {
        GetRequestTask task = new GetRequestTask(url, callback);
        task.execute();
    }

    private void post(String url, ApiResponseCallback callback, NameValuePair... params) {
        PostRequestTask task = new PostRequestTask(url, callback, params);
        task.execute();
    }

    private class GetRequestTask extends AsyncTask<Void, Void, Integer> {
        private String url;
        private ApiResponseCallback callback;

        public GetRequestTask(String url, ApiResponseCallback callback) {
            this.url = url;
            this.callback = callback;
        }

        @Override
        protected Integer doInBackground(Void... p) {
            HttpGet httpGet = new HttpGet(baseUrl + url);

            try {
                HttpResponse response = httpClient.execute(httpGet);
                StatusLine statusLine = response.getStatusLine();

                if (statusLine.getStatusCode() != HttpStatus.SC_OK) {
                    InputStream stream = response.getEntity().getContent();
                    String responseData = IOUtils.toString(stream);

                    Log.e(TAG, String.format("GET %s %d", url, statusLine.getStatusCode()));
                    Log.e(TAG, responseData);

                    stream.close();

                    if (callback != null) {
                        callback.onError(statusLine.getStatusCode(), responseData);
                    }

                } else if (callback != null) {
                    updateCsrfToken();
                    callback.onSuccess();
                }

                return statusLine.getStatusCode();
            } catch (ClientProtocolException e) {
                Log.e(TAG, "ClientProtocolException", e);
            } catch (IOException e) {
                Log.e(TAG, "IOException", e);
            }

            return 0;
        }
    }

    private class PostRequestTask extends AsyncTask<Void, Void, Integer> {
        private String url;
        private ApiResponseCallback callback;
        private NameValuePair[] params;

        public PostRequestTask(String url, ApiResponseCallback callback, NameValuePair... params) {
            this.url = url;
            this.callback = callback;
            this.params = params;
        }

        @Override
        protected Integer doInBackground(Void... p) {
            HttpPost httpPost = new HttpPost(baseUrl + url);

            try {
                List<NameValuePair> nameValuePairs = new ArrayList<>(Arrays.asList(params));
                if (csrfToken != null) {
                    nameValuePairs.add(new BasicNameValuePair("csrfmiddlewaretoken", csrfToken));
                }
                httpPost.setEntity(new UrlEncodedFormEntity(nameValuePairs));

                HttpResponse response = httpClient.execute(httpPost);
                StatusLine statusLine = response.getStatusLine();

                if (statusLine.getStatusCode() != HttpStatus.SC_OK) {
                    InputStream stream = response.getEntity().getContent();
                    String responseData = IOUtils.toString(stream);

                    Log.e(TAG, String.format("POST %s %d", url, statusLine.getStatusCode()));
                    Log.e(TAG, responseData);

                    stream.close();

                    if (callback != null) {
                        callback.onError(statusLine.getStatusCode(), responseData);
                    }

                } else if (callback != null) {
                    updateCsrfToken();
                    callback.onSuccess();
                }

                return statusLine.getStatusCode();
            } catch (ClientProtocolException e) {
                Log.e(TAG, "ClientProtocolException", e);
            } catch (IOException e) {
                Log.e(TAG, "IOException", e);
            }

            return 0;
        }
    }
}
