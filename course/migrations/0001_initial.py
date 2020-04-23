# Generated by Django 3.0.5 on 2020-04-20 11:21

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('cno', models.CharField(max_length=128, primary_key=True, serialize=False, unique=True)),
                ('name', models.CharField(max_length=128)),
                ('credit', models.IntegerField(default=0)),
                ('outline', models.CharField(default='略', max_length=2048)),
                ('references', models.CharField(default='略', max_length=1024)),
                ('mean_score', models.FloatField(default=0)),
                ('fail_rate', models.FloatField(default=0)),
            ],
            options={
                'verbose_name': '课程',
                'verbose_name_plural': '课程',
                'ordering': ['-cno'],
            },
        ),
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('tno', models.CharField(max_length=128, primary_key=True, serialize=False, unique=True)),
                ('name', models.CharField(max_length=128)),
                ('title', models.CharField(max_length=128)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('sex', models.CharField(choices=[('male', '男'), ('female', '女')], max_length=32)),
                ('institute', models.CharField(choices=[('chuan_jian', '船舶海洋与建筑工程学院'), ('ji_dong', '机械动力与工程学院'), ('dian_yuan', '电子信息与电气工程学院'), ('cai_liao', '材料科学与工程学院'), ('shu_xue', '数学科学学院'), ('wu_li', '物理与天文学院'), ('hua_xue', '化学化工学院'), ('sheng_ming', '生命科学技术学院'), ('sheng_yi_gong', '生物医学工程学院'), ('an_tai', '安泰经济与管理学院'), ('qi_ta', '其它')], max_length=256)),
                ('department', models.CharField(default='--', max_length=256)),
                ('address', models.CharField(default='--', max_length=256)),
                ('resume', models.CharField(default='略', max_length=2048)),
                ('course', models.ManyToManyField(to='course.Course', verbose_name='课程')),
            ],
            options={
                'verbose_name': '教师',
                'verbose_name_plural': '教师',
                'ordering': ['-tno'],
            },
        ),
    ]
