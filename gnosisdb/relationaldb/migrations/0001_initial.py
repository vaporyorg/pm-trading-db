# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-06-27 10:55
from __future__ import unicode_literals

import django.contrib.postgres.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('creation_date_time', models.DateTimeField()),
                ('creation_block', models.PositiveIntegerField()),
                ('address', models.CharField(max_length=40, primary_key=True, serialize=False)),
                ('factory', models.CharField(db_index=True, max_length=40)),
                ('creator', models.CharField(db_index=True, max_length=40)),
                ('collateral_token', models.CharField(db_index=True, max_length=40)),
                ('is_winning_outcome_set', models.BooleanField(default=False)),
                ('outcome', models.DecimalField(decimal_places=0, max_digits=80, null=True)),
                ('redeemed_winnings', models.DecimalField(decimal_places=0, default=0, max_digits=80)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='EventDescription',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.TextField()),
                ('description', models.TextField()),
                ('resolution_date', models.DateTimeField()),
                ('ipfs_hash', models.CharField(max_length=46, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Market',
            fields=[
                ('creation_date_time', models.DateTimeField()),
                ('creation_block', models.PositiveIntegerField()),
                ('address', models.CharField(max_length=40, primary_key=True, serialize=False)),
                ('factory', models.CharField(db_index=True, max_length=40)),
                ('creator', models.CharField(db_index=True, max_length=40)),
                ('market_maker', models.CharField(db_index=True, max_length=40)),
                ('fee', models.PositiveIntegerField()),
                ('funding', models.DecimalField(decimal_places=0, max_digits=80, null=True)),
                ('net_outcome_tokens_sold', django.contrib.postgres.fields.ArrayField(base_field=models.DecimalField(decimal_places=0, max_digits=80), size=None)),
                ('withdrawn_fees', models.DecimalField(decimal_places=0, default=0, max_digits=80)),
                ('stage', models.PositiveIntegerField(choices=[(0, 'MarketCreated'), (1, 'MarketFunded'), (2, 'MarketClosed')], default=0)),
                ('revenue', models.DecimalField(decimal_places=0, max_digits=80)),
                ('collected_fees', models.DecimalField(decimal_places=0, max_digits=80)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Oracle',
            fields=[
                ('creation_date_time', models.DateTimeField()),
                ('creation_block', models.PositiveIntegerField()),
                ('address', models.CharField(max_length=40, primary_key=True, serialize=False)),
                ('factory', models.CharField(db_index=True, max_length=40)),
                ('creator', models.CharField(db_index=True, max_length=40)),
                ('is_outcome_set', models.BooleanField(default=False)),
                ('outcome', models.DecimalField(blank=True, decimal_places=0, max_digits=80, null=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('creation_date_time', models.DateTimeField()),
                ('creation_block', models.PositiveIntegerField()),
                ('sender', models.CharField(db_index=True, max_length=40)),
                ('outcome_token_index', models.PositiveIntegerField()),
                ('outcome_token_count', models.DecimalField(decimal_places=0, max_digits=80)),
                ('net_outcome_tokens_sold', django.contrib.postgres.fields.ArrayField(base_field=models.DecimalField(decimal_places=0, max_digits=80), size=None)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='OutcomeToken',
            fields=[
                ('address', models.CharField(max_length=40, primary_key=True, serialize=False)),
                ('index', models.PositiveIntegerField()),
                ('total_supply', models.DecimalField(decimal_places=0, default=0, max_digits=80)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='OutcomeTokenBalance',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('owner', models.CharField(max_length=40)),
                ('balance', models.DecimalField(decimal_places=0, default=0, max_digits=80)),
                ('outcome_token', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='relationaldb.OutcomeToken')),
            ],
        ),
        migrations.CreateModel(
            name='OutcomeVoteBalance',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', models.CharField(db_index=True, max_length=40)),
                ('balance', models.DecimalField(decimal_places=0, max_digits=80)),
            ],
        ),
        migrations.CreateModel(
            name='BuyOrder',
            fields=[
                ('order_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='relationaldb.Order')),
                ('cost', models.DecimalField(decimal_places=0, max_digits=80)),
            ],
            options={
                'abstract': False,
            },
            bases=('relationaldb.order',),
        ),
        migrations.CreateModel(
            name='CategoricalEvent',
            fields=[
                ('event_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='relationaldb.Event')),
            ],
            options={
                'abstract': False,
            },
            bases=('relationaldb.event',),
        ),
        migrations.CreateModel(
            name='CategoricalEventDescription',
            fields=[
                ('eventdescription_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='relationaldb.EventDescription')),
                ('outcomes', django.contrib.postgres.fields.ArrayField(base_field=models.TextField(), size=None)),
            ],
            bases=('relationaldb.eventdescription',),
        ),
        migrations.CreateModel(
            name='CentralizedOracle',
            fields=[
                ('oracle_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='relationaldb.Oracle')),
                ('owner', models.CharField(db_index=True, max_length=40)),
            ],
            options={
                'abstract': False,
            },
            bases=('relationaldb.oracle',),
        ),
        migrations.CreateModel(
            name='ScalarEvent',
            fields=[
                ('event_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='relationaldb.Event')),
                ('lower_bound', models.DecimalField(decimal_places=0, max_digits=80)),
                ('upper_bound', models.DecimalField(decimal_places=0, max_digits=80)),
            ],
            options={
                'abstract': False,
            },
            bases=('relationaldb.event',),
        ),
        migrations.CreateModel(
            name='ScalarEventDescription',
            fields=[
                ('eventdescription_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='relationaldb.EventDescription')),
                ('unit', models.TextField()),
                ('decimals', models.PositiveIntegerField()),
            ],
            bases=('relationaldb.eventdescription',),
        ),
        migrations.CreateModel(
            name='SellOrder',
            fields=[
                ('order_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='relationaldb.Order')),
                ('profit', models.DecimalField(decimal_places=0, max_digits=80)),
            ],
            options={
                'abstract': False,
            },
            bases=('relationaldb.order',),
        ),
        migrations.CreateModel(
            name='ShortSellOrder',
            fields=[
                ('order_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='relationaldb.Order')),
                ('cost', models.DecimalField(decimal_places=0, max_digits=80)),
            ],
            options={
                'abstract': False,
            },
            bases=('relationaldb.order',),
        ),
        migrations.CreateModel(
            name='UltimateOracle',
            fields=[
                ('oracle_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='relationaldb.Oracle')),
                ('collateral_token', models.CharField(db_index=True, max_length=40)),
                ('spread_multiplier', models.PositiveIntegerField()),
                ('challenge_period', models.DecimalField(decimal_places=0, max_digits=80)),
                ('challenge_amount', models.DecimalField(decimal_places=0, max_digits=80)),
                ('front_runner_period', models.DecimalField(decimal_places=0, max_digits=80)),
                ('forwarded_outcome', models.DecimalField(decimal_places=0, max_digits=80, null=True)),
                ('outcome_set_at_timestamp', models.DecimalField(decimal_places=0, max_digits=80, null=True)),
                ('front_runner', models.DecimalField(decimal_places=0, max_digits=80, null=True)),
                ('front_runner_set_at_timestamp', models.DecimalField(decimal_places=0, max_digits=80, null=True)),
                ('total_amount', models.DecimalField(decimal_places=0, max_digits=80, null=True)),
                ('forwarded_oracle', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='ultimate_oracle_forwarded_oracle', to='relationaldb.Oracle')),
            ],
            options={
                'abstract': False,
            },
            bases=('relationaldb.oracle',),
        ),
        migrations.AddField(
            model_name='outcometoken',
            name='event',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='relationaldb.Event'),
        ),
        migrations.AddField(
            model_name='order',
            name='market',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='relationaldb.Market'),
        ),
        migrations.AddField(
            model_name='market',
            name='event',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='market_oracle', to='relationaldb.Event'),
        ),
        migrations.AddField(
            model_name='event',
            name='oracle',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='event_oracle', to='relationaldb.Oracle'),
        ),
        migrations.AddField(
            model_name='outcomevotebalance',
            name='ultimate_oracle',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='outcome_vote_balance_ultimate_oracle', to='relationaldb.UltimateOracle'),
        ),
        migrations.AddField(
            model_name='centralizedoracle',
            name='event_description',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='relationaldb.EventDescription'),
        ),
    ]
