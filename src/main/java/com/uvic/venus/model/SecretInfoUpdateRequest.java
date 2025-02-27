package com.uvic.venus.model;

public class SecretInfoUpdateRequest {

    private String newName;
    private String newData;
    private String username;
    private Long id;

    public SecretInfoUpdateRequest(String newName, String newData, String username, Long id) {
        this.newName = newName;
        this.newData = newData;
        this.username = username;
        this.id = id;
    }
    
    public Long getId() {
        return id;
    }

    public void setId(Long id) {
        this.id = id;
    }

    public String getNewName() {
        return newName;
    }

    public void setNewName(String newName) {
        this.newName = newName;
    }

    public String getNewData() {
        return newData;
    }

    public void setNewData(String newData) {
        this.newData = newData;
    }

    public String getUsername() {
        return username;
    }

    public void setUsername(String username) {
        this.username = username;
    }    
}
