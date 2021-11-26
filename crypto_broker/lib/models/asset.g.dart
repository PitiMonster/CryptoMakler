// GENERATED CODE - DO NOT MODIFY BY HAND

part of 'asset.dart';

// **************************************************************************
// JsonSerializableGenerator
// **************************************************************************

AssetModel _$AssetModelFromJson(Map<String, dynamic> json) => AssetModel(
      id: json['id'] as int,
      totalValue: (json['total_value'] as num).toDouble(),
      coinAmount: (json['coin_amount'] as num).toDouble(),
      fundPercent: (json['fund_percent'] as num).toDouble(),
      coin: json['coin'] as String,
      fund: json['fund'] as int,
    );

Map<String, dynamic> _$AssetModelToJson(AssetModel instance) =>
    <String, dynamic>{
      'id': instance.id,
      'fund': instance.fund,
      'total_value': instance.totalValue,
      'coin_amount': instance.coinAmount,
      'fund_percent': instance.fundPercent,
      'coin': instance.coin,
    };
