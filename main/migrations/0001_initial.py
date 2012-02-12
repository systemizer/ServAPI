# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding model 'Survey'
        db.create_table('main_survey', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(default='Untitled', max_length=128)),
            ('created', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('deleted', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('creator', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='authored_surveys', null=True, to=orm['auth.User'])),
        ))
        db.send_create_signal('main', ['Survey'])

        # Adding model 'Question'
        db.create_table('main_question', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('survey', self.gf('django.db.models.fields.related.ForeignKey')(related_name='questions', to=orm['main.Survey'])),
            ('text', self.gf('django.db.models.fields.TextField')()),
        ))
        db.send_create_signal('main', ['Question'])

        # Adding model 'TextQuestion'
        db.create_table('main_textquestion', (
            ('question_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['main.Question'], unique=True, primary_key=True)),
        ))
        db.send_create_signal('main', ['TextQuestion'])

        # Adding model 'BooleanQuestion'
        db.create_table('main_booleanquestion', (
            ('question_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['main.Question'], unique=True, primary_key=True)),
        ))
        db.send_create_signal('main', ['BooleanQuestion'])

        # Adding model 'MultipleChoiceQuestion'
        db.create_table('main_multiplechoicequestion', (
            ('question_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['main.Question'], unique=True, primary_key=True)),
            ('choices', self.gf('django.db.models.fields.TextField')()),
        ))
        db.send_create_signal('main', ['MultipleChoiceQuestion'])

        # Adding model 'MultipleCheckboxQuestion'
        db.create_table('main_multiplecheckboxquestion', (
            ('multiplechoicequestion_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['main.MultipleChoiceQuestion'], unique=True, primary_key=True)),
        ))
        db.send_create_signal('main', ['MultipleCheckboxQuestion'])


    def backwards(self, orm):
        
        # Deleting model 'Survey'
        db.delete_table('main_survey')

        # Deleting model 'Question'
        db.delete_table('main_question')

        # Deleting model 'TextQuestion'
        db.delete_table('main_textquestion')

        # Deleting model 'BooleanQuestion'
        db.delete_table('main_booleanquestion')

        # Deleting model 'MultipleChoiceQuestion'
        db.delete_table('main_multiplechoicequestion')

        # Deleting model 'MultipleCheckboxQuestion'
        db.delete_table('main_multiplecheckboxquestion')


    models = {
        'auth.group': {
            'Meta': {'object_name': 'Group'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        'auth.permission': {
            'Meta': {'ordering': "('content_type__app_label', 'content_type__model', 'codename')", 'unique_together': "(('content_type', 'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['contenttypes.ContentType']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        'auth.user': {
            'Meta': {'object_name': 'User'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Group']", 'symmetrical': 'False', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'main.booleanquestion': {
            'Meta': {'object_name': 'BooleanQuestion', '_ormbases': ['main.Question']},
            'question_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['main.Question']", 'unique': 'True', 'primary_key': 'True'})
        },
        'main.multiplecheckboxquestion': {
            'Meta': {'object_name': 'MultipleCheckboxQuestion', '_ormbases': ['main.MultipleChoiceQuestion']},
            'multiplechoicequestion_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['main.MultipleChoiceQuestion']", 'unique': 'True', 'primary_key': 'True'})
        },
        'main.multiplechoicequestion': {
            'Meta': {'object_name': 'MultipleChoiceQuestion', '_ormbases': ['main.Question']},
            'choices': ('django.db.models.fields.TextField', [], {}),
            'question_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['main.Question']", 'unique': 'True', 'primary_key': 'True'})
        },
        'main.question': {
            'Meta': {'object_name': 'Question'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'survey': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'questions'", 'to': "orm['main.Survey']"}),
            'text': ('django.db.models.fields.TextField', [], {})
        },
        'main.survey': {
            'Meta': {'object_name': 'Survey'},
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'creator': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'authored_surveys'", 'null': 'True', 'to': "orm['auth.User']"}),
            'deleted': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'default': "'Untitled'", 'max_length': '128'})
        },
        'main.textquestion': {
            'Meta': {'object_name': 'TextQuestion', '_ormbases': ['main.Question']},
            'question_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['main.Question']", 'unique': 'True', 'primary_key': 'True'})
        }
    }

    complete_apps = ['main']
