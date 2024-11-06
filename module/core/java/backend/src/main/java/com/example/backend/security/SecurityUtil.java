package com.example.backend.security;


import com.auth0.jwt.JWT;
import com.auth0.jwt.algorithms.Algorithm;

import com.example.backend.common.Constants;
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;

import java.util.Date;

public class SecurityUtil {
    public static synchronized void writeCorsHeaders(HttpServletRequest request, HttpServletResponse response) {
        response.setHeader("Access-Control-Allow-Origin", request.getHeader("Origin"));
        response.setHeader("Access-Control-Allow-Credentials", "true");
        response.setHeader("Access-Control-Allow-Methods",
                "ACL, CANCELUPLOAD, CHECKIN, CHECKOUT, COPY, DELETE, GET, HEAD, LOCK, MKCALENDAR, MKCOL, MOVE, " +
                        "OPTIONS, POST, PROPFIND, PROPPATCH, PUT, REPORT, SEARCH, UNCHECKOUT, UNLOCK, UPDATE, VERSION-CONTROL");
        response.setHeader("Access-Control-Max-Age", "3600");
        response.setHeader("Access-Control-Allow-Headers",
                "Origin, X-Requested-With, Content-Type, Accept, Key, Authorization, api_key");
    }

    //public static String createJwtToken(UsernamePasswordAuthenticationToken token, String issuer, long expSeconds,
    //                                    Algorithm algorithm, String scope) {
    //    Long userId = (Long) token.getDetails();
    //    String username = (String) token.getPrincipal();
    //    return createJwtToken(issuer, expSeconds, username, username, userId, scope, algorithm);
    //}

    public static synchronized String createJwtToken(
            String issuer,
            long expSeconds,
            String subject,
            String username,
            long userId,
            String scope,
            Algorithm algorithm,
            String tokenId
    ) {
        return JWT.create()
                .withIssuer(issuer)
                .withExpiresAt(new Date(System.currentTimeMillis() + (expSeconds * 1000)))
                .withJWTId(tokenId)
                .withSubject(subject)
                .withClaim(Constants.CLAIM_USERNAME, username)
                .withClaim(Constants.CLAIM_USER_ID, userId)
                .withClaim(Constants.CLAIM_SCOPE, scope)
                .sign(algorithm);
    }
}
