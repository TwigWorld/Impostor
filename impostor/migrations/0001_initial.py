# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'ImpostorLog'
        db.create_table(u'impostor_impostorlog', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('impostor', self.gf('django.db.models.fields.related.ForeignKey')(related_name='impostor', to=orm['customuser.User'])),
            ('imposted_as', self.gf('django.db.models.fields.related.ForeignKey')(related_name='imposted_as', to=orm['customuser.User'])),
            ('impostor_ip', self.gf('django.db.models.fields.IPAddressField')(max_length=15, null=True, blank=True)),
            ('logged_in', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('logged_out', self.gf('django.db.models.fields.DateTimeField')(null=True, blank=True)),
            ('token', self.gf('django.db.models.fields.CharField')(db_index=True, max_length=32, blank=True)),
        ))
        db.send_create_signal(u'impostor', ['ImpostorLog'])


    def backwards(self, orm):
        # Deleting model 'ImpostorLog'
        db.delete_table(u'impostor_impostorlog')


    models = {
        u'account.account': {
            'Meta': {'object_name': 'Account'},
            'account_size': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['account.AccountSize']", 'null': 'True', 'blank': 'True'}),
            'account_type': ('django.db.models.fields.CharField', [], {'default': "'school'", 'max_length': '20'}),
            'contact_details': ('contactfield.fields.ContactField', [], {'default': "{'school': {'last_name': '', 'notes': '', 'postal_code': '', 'full_name': '', 'salutation': '', 'maiden_name': '', 'first_name': '', 'state': '', 'middle_names': '', 'do_not_email': '', 'company_name': '', 'do_not_call': '', 'email': '', 'job_title': '', 'website': '', 'fax': '', 'city': '', 'phone': '', 'building': '', 'mobile': '', 'country': '', 'region': '', 'address_4': '', 'address_5': '', 'address_6': '', 'address_7': '', 'address_1': '', 'address_2': '', 'address_3': '', 'address_8': '', 'address_9': '', 'street_address': ''}, 'contact': {'last_name': '', 'notes': '', 'postal_code': '', 'full_name': '', 'salutation': '', 'maiden_name': '', 'first_name': '', 'state': '', 'middle_names': '', 'do_not_email': '', 'company_name': '', 'do_not_call': '', 'email': '', 'job_title': '', 'website': '', 'fax': '', 'city': '', 'phone': '', 'building': '', 'mobile': '', 'country': '', 'region': '', 'address_4': '', 'address_5': '', 'address_6': '', 'address_7': '', 'address_1': '', 'address_2': '', 'address_3': '', 'address_8': '', 'address_9': '', 'street_address': ''}, 'business': {'last_name': '', 'notes': '', 'postal_code': '', 'full_name': '', 'salutation': '', 'maiden_name': '', 'first_name': '', 'state': '', 'middle_names': '', 'do_not_email': '', 'company_name': '', 'do_not_call': '', 'email': '', 'job_title': '', 'website': '', 'fax': '', 'city': '', 'phone': '', 'building': '', 'mobile': '', 'country': '', 'region': '', 'address_4': '', 'address_5': '', 'address_6': '', 'address_7': '', 'address_1': '', 'address_2': '', 'address_3': '', 'address_8': '', 'address_9': '', 'street_address': ''}, 'billing': {'last_name': '', 'notes': '', 'postal_code': '', 'full_name': '', 'salutation': '', 'maiden_name': '', 'first_name': '', 'state': '', 'middle_names': '', 'do_not_email': '', 'company_name': '', 'do_not_call': '', 'email': '', 'job_title': '', 'website': '', 'fax': '', 'city': '', 'phone': '', 'building': '', 'mobile': '', 'country': '', 'region': '', 'address_4': '', 'address_5': '', 'address_6': '', 'address_7': '', 'address_1': '', 'address_2': '', 'address_3': '', 'address_8': '', 'address_9': '', 'street_address': ''}}"}),
            'created_on': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'deactivated_by': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'accounts_deactivated'", 'null': 'True', 'to': u"orm['customuser.User']"}),
            'home_user_limit_override': ('django.db.models.fields.PositiveIntegerField', [], {'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_trial': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'status': ('model_utils.fields.StatusField', [], {'default': "'in_use'", 'max_length': '100', u'no_check_for_status': 'True'}),
            'student_limit_override': ('django.db.models.fields.PositiveIntegerField', [], {'null': 'True', 'blank': 'True'}),
            'teacher_limit_override': ('django.db.models.fields.PositiveIntegerField', [], {'null': 'True', 'blank': 'True'}),
            'territory': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['territory.Territory']"}),
            'trial_expiry_date': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'})
        },
        u'account.accountsize': {
            'Meta': {'unique_together': "(('territory', 'account_type', 'account_size'),)", 'object_name': 'AccountSize'},
            'account_size': ('django.db.models.fields.CharField', [], {'default': "'medium'", 'max_length': '20'}),
            'account_type': ('django.db.models.fields.CharField', [], {'default': "'school'", 'max_length': '20'}),
            'home_user_limit': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'student_limit': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0'}),
            'teacher_limit': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0'}),
            'territory': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['territory.Territory']"})
        },
        u'auth.group': {
            'Meta': {'object_name': 'Group'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        u'auth.permission': {
            'Meta': {'ordering': "(u'content_type__app_label', u'content_type__model', u'codename')", 'unique_together': "((u'content_type', u'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['contenttypes.ContentType']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'customuser.user': {
            'Meta': {'object_name': 'User'},
            '_username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '40', 'db_column': "'username'"}),
            'account': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['account.Account']", 'null': 'True', 'blank': 'True'}),
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'default_locale': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'locale_default'", 'null': 'True', 'to': u"orm['territory.Locale']"}),
            'deleted_by': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'deleted_users'", 'null': 'True', 'to': u"orm['customuser.User']"}),
            'email': ('django.db.models.fields.EmailField', [], {'db_index': 'True', 'max_length': '255', 'unique': 'True', 'null': 'True', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "u'user_set'", 'blank': 'True', 'to': u"orm['auth.Group']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_account_administrator': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_admin': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'non_osm_id': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0', 'null': 'True', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'status': ('model_utils.fields.StatusField', [], {'default': "'pending'", 'max_length': '100', u'no_check_for_status': 'True'}),
            'status_changed': ('model_utils.fields.MonitorField', [], {'default': 'datetime.datetime.now', u'monitor': "u'status'"}),
            'type': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "u'user_set'", 'blank': 'True', 'to': u"orm['auth.Permission']"})
        },
        u'impostor.impostorlog': {
            'Meta': {'object_name': 'ImpostorLog'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'imposted_as': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'imposted_as'", 'to': u"orm['customuser.User']"}),
            'impostor': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'impostor'", 'to': u"orm['customuser.User']"}),
            'impostor_ip': ('django.db.models.fields.IPAddressField', [], {'max_length': '15', 'null': 'True', 'blank': 'True'}),
            'logged_in': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'logged_out': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'token': ('django.db.models.fields.CharField', [], {'db_index': 'True', 'max_length': '32', 'blank': 'True'})
        },
        u'territory.locale': {
            'Meta': {'ordering': "('site_order', 'pk')", 'object_name': 'Locale'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'language_code': ('django.db.models.fields.CharField', [], {'default': "'en'", 'max_length': '50', 'db_index': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'site_order': ('django.db.models.fields.IntegerField', [], {'default': '1'}),
            'tag': ('django.db.models.fields.CharField', [], {'max_length': '50', 'db_index': 'True'}),
            'unix_code': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'territory.territory': {
            'Meta': {'object_name': 'Territory'},
            'address_fields_csv': ('django.db.models.fields.TextField', [], {'default': "'building, street_address, city, region, postal_code'"}),
            'caption_locales': ('django.db.models.fields.related.ManyToManyField', [], {'blank': 'True', 'related_name': "'territory_captions'", 'null': 'True', 'symmetrical': 'False', 'to': u"orm['territory.Locale']"}),
            'code': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '3'}),
            'default_locale': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'territory_default'", 'to': u"orm['territory.Locale']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'locales': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'territories'", 'symmetrical': 'False', 'to': u"orm['territory.Locale']"}),
            'staff_members': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "'territories'", 'blank': 'True', 'to': u"orm['customuser.User']"}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        }
    }

    complete_apps = ['impostor']