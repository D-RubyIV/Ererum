package com.example.backend.security;

import com.auth0.jwt.algorithms.Algorithm;
import com.example.backend.common.Constants;
import com.example.backend.domain.dto.UserMinDTO;
import lombok.extern.slf4j.Slf4j;
import org.springframework.security.authentication.UsernamePasswordAuthenticationToken;
import org.springframework.security.core.Authentication;
import java.security.interfaces.RSAPrivateKey;
import java.security.interfaces.RSAPublicKey;
import java.util.UUID;

@Slf4j
public class TokenProvider {
    private KeyPairProvider keyPairProvider;

    public TokenObject generateToken(String issuer, Authentication authentication){
        long userId;
        String username;

        TokenObject.Builder builder = new TokenObject.Builder();

        RSAPublicKey publicKey = keyPairProvider.getRsaPublicKey();
        RSAPrivateKey privateKey = keyPairProvider.getRsaPrivateKey();

        Long accessTokenExpireTime = 3000 * 60L;
        Long refreshTokenExpireTime = 3000 * 60L * 10;

        String accessTokenUUID = UUID.randomUUID().toString();
        String refreshTokenUUID = UUID.randomUUID().toString();

        Algorithm algorithm = Algorithm.RSA256(publicKey, privateKey);
        if (authentication instanceof UsernamePasswordAuthenticationToken){
            UsernamePasswordAuthenticationToken authenticationToken = (UsernamePasswordAuthenticationToken) authentication;

            UserMinDTO userPrincipal = (UserMinDTO) authenticationToken.getPrincipal();
            userId = userPrincipal.getId();
            username = userPrincipal.getUsername();

        } else {
            throw new RuntimeException("Authentication of type '"
                    + authentication.getClass().getSimpleName() + "' is not supported");
        }
        String accessToken = SecUtil.createJwtToken(
                issuer,
                accessTokenExpireTime,
                username,
                username,
                userId,
                Constants.CLAIM_SCOPE_ACCESS_TOKEN,
                algorithm,
                accessTokenUUID
                );
        String refreshToken = SecUtil.createJwtToken(
                issuer,
                refreshTokenExpireTime,
                username,
                username,
                userId,
                Constants.CLAIM_SCOPE_REFRESH_TOKEN,
                algorithm,
                refreshTokenUUID
        );
    }
}
