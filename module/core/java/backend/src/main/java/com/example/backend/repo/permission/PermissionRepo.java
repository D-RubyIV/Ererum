package com.example.backend.repo.permission;

import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.data.jpa.repository.Query;
import org.springframework.stereotype.Repository;

import java.security.Permission;
import java.util.List;

@Repository
public interface PermissionRepo extends JpaRepository<Permission, Long> {
    @Query(
            value = """
                    SELECT p FROM PermissionDomain p where p.deleted = :deleted
                    """
    )
    List<Permission> findAllPermission(boolean deleted);

    @Query(
            value = """
                    SELECT p FROM PermissionDomain p
                    join GroupDomain gd
                    on p.id = gd.permission.id
                    where p.deleted = :deleted
                    and gd.id = :groupId
                    """
    )
    List<Permission> findAllPermissionByGroup(boolean deleted, int groupId);
}
