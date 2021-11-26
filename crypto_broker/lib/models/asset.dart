import 'package:json_annotation/json_annotation.dart';

part 'asset.g.dart';

@JsonSerializable()
class AssetModel {
  final int id;
  final int fund;
  @JsonKey(name: 'total_value')
  double totalValue;
  @JsonKey(name: 'coin_id')
  int coinId;
  @JsonKey(name: 'coin_amount')
  double coinAmount;
  @JsonKey(name: 'fund_percent')
  double fundPercent;
  String coin;

  AssetModel(
      {required this.id,
      required this.totalValue,
      required this.coinAmount,
      required this.fundPercent,
      required this.coin,
      required this.coinId,
      required this.fund});

  factory AssetModel.fromJson(Map<String, dynamic> json) =>
      _$AssetModelFromJson(json);

  Map<String, dynamic> toJson() => _$AssetModelToJson(this);
}
