// GENERATED CODE - DO NOT MODIFY BY HAND

part of 'fund_investor.dart';

// **************************************************************************
// JsonSerializableGenerator
// **************************************************************************

FundInvestorModel _$FundInvestorModelFromJson(Map<String, dynamic> json) =>
    FundInvestorModel(
      json['investor'] as String,
      (json['share_amount'] as num).toDouble(),
    );

Map<String, dynamic> _$FundInvestorModelToJson(FundInvestorModel instance) =>
    <String, dynamic>{
      'investor': instance.investor,
      'share_amount': instance.shareAmount,
    };
