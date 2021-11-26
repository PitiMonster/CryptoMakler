import 'dart:convert';
import 'package:crypto_client/constants/api.dart';
import 'package:crypto_client/models/investment.dart';
import 'package:http/http.dart' as http;

import 'package:flutter/material.dart';

class InvestmentsProvider with ChangeNotifier {
  String _token = '';
  String get token => _token;
  List<InvestmentModel> investments = [];

  void updateAuth(String token) {
    _token = token;
    notifyListeners();
  }

  Future<void> fetchInvestments() async {
    try {
      final response = await http.get(
        Uri.parse('$apiUrl/investments'),
        headers: {
          'Authorization': 'Bearer $_token',
        },
      );
      if (response.statusCode == 200) {
        final data = json.decode(response.body);
        investments.clear();

        for (final investment in data) {
          investments.add(InvestmentModel.fromJson(investment));
        }

        notifyListeners();
      }
    } catch (error) {
      throw error;
    }
  }
}
