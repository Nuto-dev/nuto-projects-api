from django.db import models


class WorkSpaceRelation(models.Model):
    class InvitationStatus(models.TextChoices):
        invited = "invited"
        accepted = "accepted"
        denied = "denied"

    class MemberStatusChoices(models.TextChoices):
        owner = 'owner'
        co_owner = 'co_owner'
        admin = 'admin'
        worker = 'worker'

    workspace = models.ForeignKey('workspace.WorkSpace', on_delete=models.CASCADE, related_name='work_relations')
    member = models.ForeignKey('accounts.User', on_delete=models.CASCADE, related_name='work_relations')

    member_status = models.CharField(max_length=12, choices=MemberStatusChoices.choices)
    is_active = models.BooleanField(default=True)

    invitation_status = models.CharField(max_length=12, choices=InvitationStatus.choices, default=InvitationStatus.invited)

    joined_at = models.DateTimeField(auto_now_add=True)

    def accept(self):
        if self.invitation_status != self.InvitationStatus.invited: return False

        self.invitation_status = self.InvitationStatus.accepted
        self.save(update_fields=['invitation_status'])
        return True

    def deny(self):
        if self.invitation_status != self.InvitationStatus.invited: return False

        self.invitation_status = self.InvitationStatus.denied
        self.save(update_fields=['invitation_status'])
        return True

    def active(self):
        self.is_active = True
        self.save(update_fields=['is_active'])

    def deactive(self):
        self.is_active = False
        self.save(update_fields=['is_active'])

    def __str__(self):
        return self.workspace.name + ' -> ' + self.member.name