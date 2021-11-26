// GENERATED CODE - DO NOT MODIFY BY HAND

part of 'fund.dart';

// **************************************************************************
// JsonSerializableGenerator
// **************************************************************************

FundModel _$FundModelFromJson(Map<String, dynamic> json) => FundModel(
      json['id'] as int,
      (json['investors'] as List<dynamic>?)
              ?.map(
                  (e) => FundInvestorModel.fromJson(e as Map<String, dynamic>))
              .toList() ??
          [],
      (json['total_value'] as num).toDouble(),
      json['name'] as String,
      (json['fee'] as num).toDouble(),
      json['broker'] as int,
    );

Map<String, dynamic> _$FundModelToJson(FundModel instance) => <String, dynamic>{
      'id': instance.id,
      'investors': instance.investors,
      'total_value': instance.totalValue,
      'name': instance.name,
      'fee': instance.fee,
      'broker': instance.broker,
    };
