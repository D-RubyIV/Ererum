package com.example.backend.security;

import lombok.AllArgsConstructor;
import lombok.Data;
import lombok.NoArgsConstructor;

@AllArgsConstructor
@NoArgsConstructor
@Data
public class TokenObject {
    private String accessTokenUUID;
    private String refreshTokenUUID;
    private String accessToken;
    private String refreshToken;

    public static class Builder {
        private TokenObject data;

        public Builder(){
            data = new TokenObject();
        }
        public Builder accessTokenId(String accessToken){
            data.setAccessToken(accessToken);
            return this;
        }
        public Builder accessTokenUUID(String uuid){
            data.setAccessTokenUUID(uuid);
            return this;
        }
        public Builder refreshToken(String refreshToken){
            data.setRefreshToken(refreshToken);
            return this;
        }
        public Builder refreshTokenUUID(String uuid){
            data.setRefreshTokenUUID(uuid);
            return this;
        }
        public TokenObject build(){
            validate();
            return data;
        }
        private void validate() {
            if (data.getAccessToken() == null) {
                throw new IllegalStateException("Access token is null");
            }
            if (data.getAccessTokenUUID() == null) {
                throw new IllegalStateException("Access token ID is null");
            }
            if (data.getRefreshToken() == null) {
                throw new IllegalStateException("Refresh token is null");
            }
            if (data.getRefreshTokenUUID() == null) {
                throw new IllegalStateException("Refresh token ID is null");
            }
        }
    }
}

