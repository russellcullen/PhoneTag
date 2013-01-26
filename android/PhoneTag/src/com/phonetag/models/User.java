package com.phonetag.models;

import java.util.List;

public class User {
    
   
    private String phoneID;
    private String name;
    private float latitude;
    private float longitude;
    private List<String> friends;
    private List<String> games;
    
    public String getPhoneID() {
        return phoneID;
    }
    public void setPhoneID(String phoneID) {
        this.phoneID = phoneID;
    }
    public String getName() {
        return name;
    }
    public void setName(String name) {
        this.name = name;
    }
    public float getLatitude() {
        return latitude;
    }
    public void setLatitude(float latitude) {
        this.latitude = latitude;
    }
    public float getLongitude() {
        return longitude;
    }
    public void setLongitude(float longitude) {
        this.longitude = longitude;
    }
    public List<String> getFriends() {
        return friends;
    }
    public void setFriends(List<String> friends) {
        this.friends = friends;
    }
    public List<String> getGames() {
        return games;
    }
    public void setGames(List<String> games) {
        this.games = games;
    }

}
