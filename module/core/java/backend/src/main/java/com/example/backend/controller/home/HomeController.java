package com.example.backend.controller.home;

import org.springframework.http.ResponseEntity;
import org.springframework.security.access.prepost.PreAuthorize;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

@RestController
@RequestMapping(value = "home")
public class HomeController {
    @GetMapping(value = "")
    @PreAuthorize("hasPermission()")
    public ResponseEntity<?> home(){
        return ResponseEntity.ok("200");
    }
}
