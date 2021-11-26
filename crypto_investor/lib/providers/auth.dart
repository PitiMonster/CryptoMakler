import 'dart:convert';
import 'package:crypto_client/constants/api.dart';
import 'package:http/http.dart' as http;

import 'package:flutter/material.dart';

class AuthProvider with ChangeNotifier {
  String _token = '';
  String get token => _token;

  Future<int> signIn(
      {required String username, required String password}) async {
    var url = Uri.parse('$apiUrl/auth/token/');
    try {
      final response = await http.post(
        url,
        headers: {
          'Content-Type': 'application/json; charset=UTF-8',
        },
        body: jsonEncode(<String, String>{
          'username': username,
          'password': password,
        }),
      );
      final responseData = json.decode(response.body);
      _token = responseData['access'];
      notifyListeners();
      return response.statusCode;
    } catch (error) {
      print(error);
      return 500;
    }
  }

  Future<int> signUp({
    required String username,
    required String email,
    required String password,
  }) async {
    var url = Uri.parse('$apiUrl/auth/register/');
    try {
      final response = await http.post(
        url,
        body: {
          'username': username,
          'password': password,
          'email': email,
          'role': 'INV',
        },
      );

      return response.statusCode;
    } catch (error) {
      print(error);
      return 500;
    }
  }

  Future<void> logout() async {
    _token = '';
    notifyListeners();
  }
}
