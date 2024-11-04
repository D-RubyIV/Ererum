package com.example.backend.config;


import com.fasterxml.jackson.databind.module.SimpleModule;

public class StringTrimModule extends SimpleModule {

    public StringTrimModule() {
        addDeserializer(String.class, new StringTrimDeserializer()); // đăng ký trim cho string
    }
}