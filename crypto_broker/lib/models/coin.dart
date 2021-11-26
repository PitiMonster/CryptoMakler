import 'package:json_annotation/json_annotation.dart';

part 'coin.g.dart';

@JsonSerializable()
class CoinModel {
  int id;
  String name;

  CoinModel(this.id, this.name);

  @override
  bool operator ==(dynamic other) => other is CoinModel && id == other.id;

  @override
  int get hashCode => super.hashCode;

  factory CoinModel.fromJson(Map<String, dynamic> json) =>
      _$CoinModelFromJson(json);

  Map<String, dynamic> toJson() => _$CoinModelToJson(this);
}
