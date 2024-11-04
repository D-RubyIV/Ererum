package com.example.backend.domain.dto;


import com.fasterxml.jackson.annotation.JsonIgnoreProperties;

@JsonIgnoreProperties(ignoreUnknown = true)
public class UserMinDTO {
    private long id;
    private String username;


    public UserMinDTO(long id, String username) {
        this.id = id;
        this.username = username;
    }

    public UserMinDTO() {
    }

    public long getId() {
        return id;
    }

    public void setId(long id) {
        this.id = id;
    }

    public String getUsername() {
        return username;
    }

    public void setUsername(String username) {
        this.username = username;
    }
}
