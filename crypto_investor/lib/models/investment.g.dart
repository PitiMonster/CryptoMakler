// GENERATED CODE - DO NOT MODIFY BY HAND

part of 'investment.dart';

// **************************************************************************
// JsonSerializableGenerator
// **************************************************************************

InvestmentModel _$InvestmentModelFromJson(Map<String, dynamic> json) =>
    InvestmentModel(
      json['fund'] as String,
      (json['total_value'] as num).toDouble(),
    );

Map<String, dynamic> _$InvestmentModelToJson(InvestmentModel instance) =>
    <String, dynamic>{
      'fund': instance.fund,
      'total_value': instance.totalValue,
    };
