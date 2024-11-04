package com.example.backend.controller.client.user;

import com.example.backend.controller.dto.request.SigningRequestDTO;
import jakarta.validation.Valid;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

@RestController
@RequestMapping(value = "auth")
public class AuthController {
    @PostMapping(value = "login")
    public ResponseEntity<?> login(@Valid @RequestBody SigningRequestDTO dto){

        return ResponseEntity.ok("200");
    }
}
