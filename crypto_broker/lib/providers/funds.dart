import 'dart:convert';
import 'package:crypto_client/constants/api.dart';
import 'package:crypto_client/models/asset.dart';
import 'package:crypto_client/models/coin.dart';
import 'package:crypto_client/models/fund.dart';
import 'package:http/http.dart' as http;

import 'package:flutter/material.dart';

class FundsProvider with ChangeNotifier {
  String _token = '';
  String get token => _token;
  List<FundModel> funds = [];
  List<CoinModel> coins = [];
  List<AssetModel> assets = [];

  void updateAuth(String token) {
    _token = token;
    notifyListeners();
  }

  Future<void> fetchFunds() async {
    try {
      final response = await http.get(
        Uri.parse('$apiUrl/funds/'),
        headers: {
          'Authorization': 'Bearer $_token',
        },
      );
      if (response.statusCode == 200) {
        final data = json.decode(response.body);
        funds.clear();

        for (final fund in data) {
          funds.add(FundModel.fromJson(fund));
        }

        notifyListeners();
      }
    } catch (error) {
      throw error;
    }
  }

  Future<void> getAllCoins() async {
    try {
      final response = await http.get(Uri.parse('$apiUrl/coins/'), headers: {
        'Authorization': 'Bearer $_token',
      });

      print(response.body);
      if (response.statusCode == 200) {
        final data = json.decode(response.body);
        coins.clear();

        for (final coin in data) {
          coins.add(CoinModel.fromJson(coin));
        }

        notifyListeners();
      }
    } catch (error) {
      print(error);
      throw error;
    }
  }

  Future<void> getAssetsOfFund(int fundId) async {
    try {
      final response = await http.get(
        Uri.parse('$apiUrl/funds/$fundId/assets/'),
        headers: {
          'Authorization': 'Bearer $_token',
        },
      );
      if (response.statusCode == 200) {
        final data = json.decode(response.body);
        assets.clear();

        for (final asset in data) {
          print(asset);
          assets.add(AssetModel.fromJson(asset));
        }

        notifyListeners();
      }
    } catch (error) {
      throw error;
    }
  }

  Future<void> updateAssets(int fundId, List<AssetModel> newAssets) async {
    try {
      print({
        "coins": {
          json.encode(newAssets
              .map((asset) => {
                    'id': asset.id,
                    'percent': asset.fundPercent,
                  })
              .toList()),
        }
      });
      final response = await http.put(
        Uri.parse('$apiUrl/funds/$fundId/assets/'),
        headers: {
          'Authorization': 'Bearer $_token',
        },
        body: json.encode({
          "coins": newAssets
              .map((asset) => {
                    'id': asset.id,
                    'percent': asset.fundPercent,
                  })
              .toList()
        }),
      );
      print(response.body);
      if (response.statusCode == 200) {
        final data = json.decode(response.body);
        assets.clear();

        for (final asset in data) {
          assets.add(AssetModel.fromJson(asset));
        }

        notifyListeners();
      }
    } catch (error) {
      throw error;
    }
  }

  Future<int> createFund({required String name, required double fee}) async {
    try {
      final response = await http.post(
        Uri.parse("$apiUrl/funds/"),
        headers: {
          'Authorization': 'Bearer $_token',
        },
        body: {
          'name': name,
          'fee': fee.toString(),
        },
      );

      if (response.statusCode == 201) {
        final data = json.decode(response.body);
        final fund = FundModel.fromJson(data);
        funds.add(fund);
        notifyListeners();
      }

      return response.statusCode;
    } catch (error) {
      print(error);
      return 500;
    }
  }

  Future<int> inviteUserToFund(
      {required String username, required int fund}) async {
    print("$apiUrl/funds/$fund/invitations/");
    try {
      final response = await http.post(
        Uri.parse("$apiUrl/funds/$fund/invitations/"),
        headers: {
          'Authorization': 'Bearer $_token',
        },
        body: {
          'username': username,
        },
      );
      print(response.body);
      return response.statusCode;
    } catch (error) {
      print(error);
      return 500;
    }
  }
}
