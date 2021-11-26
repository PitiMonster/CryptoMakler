import 'package:json_annotation/json_annotation.dart';

part 'investment.g.dart';

@JsonSerializable()
class InvestmentModel {
  String fund;
  @JsonKey(name: 'total_value')
  double totalValue;

  InvestmentModel(this.fund, this.totalValue);

  factory InvestmentModel.fromJson(Map<String, dynamic> json) =>
      _$InvestmentModelFromJson(json);

  Map<String, dynamic> toJson() => _$InvestmentModelToJson(this);
}
