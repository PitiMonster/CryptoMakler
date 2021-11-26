import 'package:crypto_client/models/fund_investor.dart';
import 'package:json_annotation/json_annotation.dart';

part 'fund.g.dart';

@JsonSerializable()
class FundModel {
  int id;
  @JsonKey(defaultValue: [])
  List<FundInvestorModel> investors;
  @JsonKey(name: 'total_value')
  double totalValue;
  String name;
  double fee;
  int broker;

  FundModel(this.id, this.investors, this.totalValue, this.name, this.fee,
      this.broker);

  factory FundModel.fromJson(Map<String, dynamic> json) =>
      _$FundModelFromJson(json);

  Map<String, dynamic> toJson() => _$FundModelToJson(this);
}
