package com.example.backend.repo.user;

import com.example.backend.domain.entity.UserDomain;
import org.springframework.data.domain.Page;
import org.springframework.data.domain.Pageable;
import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.data.jpa.repository.Query;
import org.springframework.stereotype.Repository;

import java.util.Optional;

@Repository
public interface UserRepo extends JpaRepository<UserDomain, Long> {
    @Query(
            value = """
                    SELECT u FROM UserDomain u where u.deleted = :deleted
                    """
    )
    Page<UserDomain> findAllWithPage(Pageable pageable);

    @Query(
            value = """
                    SELECT u FROM UserDomain u
                    JOIN GroupDomain gd
                    ON u.id = gd.user.id
                    WHERE u.deleted = :deleted
                    AND gd.id = : groupId
                    """
    )
    Page<UserDomain> findAllWithPageByGroup(int groupId, Pageable pageable);

    Optional<UserDomain> findByIdAndDeleted(Long id, int deleted);




}
