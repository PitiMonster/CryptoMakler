import 'package:json_annotation/json_annotation.dart';

part 'fund_investor.g.dart';

@JsonSerializable()
class FundInvestorModel {
  String investor;
  @JsonKey(name: 'share_amount')
  double shareAmount;
  @JsonKey(name: 'investment_id')
  int investorId;
  FundInvestorModel(this.investor, this.shareAmount, this.investorId);

  factory FundInvestorModel.fromJson(Map<String, dynamic> json) =>
      _$FundInvestorModelFromJson(json);

  Map<String, dynamic> toJson() => _$FundInvestorModelToJson(this);
}
