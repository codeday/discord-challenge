from db.models import session_creator, ChallengeUser


class ChallengeUsersService:
    @staticmethod
    def complete_challenge(member_id):
        """adds one completed challenge to a user"""
        session = session_creator()
        user = session.query(ChallengeUser).filter(ChallengeUser.member_id == str(member_id)).first()
        if not user:
            user = ChallengeUser(member_id=str(member_id),
                                 challenges_completed=0)
            session.add(user)
            session.commit()
            session.close()
        else:
            user.challenges_completed += 1
            session.commit()
            session.close()
