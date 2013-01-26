package com.phonetag.models;

import java.util.List;

public class Game {
    
    private List<String> users;
    private String it;
    private String name;
    private boolean finished;
    
    public List<String> getUsers() {
        return users;
    }
    public void setUsers(List<String> users) {
        this.users = users;
    }
    public String getIt() {
        return it;
    }
    public void setIt(String it) {
        this.it = it;
    }
    public String getName() {
        return name;
    }
    public void setName(String name) {
        this.name = name;
    }
    public boolean isFinished() {
        return finished;
    }
    public void setFinished(boolean finished) {
        this.finished = finished;
    }

}
