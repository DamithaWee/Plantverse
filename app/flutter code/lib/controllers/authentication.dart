import 'dart:convert';

import 'package:app/constants/constants.dart';
import 'package:app/views/main_page.dart';
import 'package:flutter/material.dart';
import 'package:get/get.dart';
import 'package:http/http.dart' as http;
import 'package:get_storage/get_storage.dart';

class AuthenticationController extends GetxController {
  final isLoading = false.obs;
  final token = ''.obs;

  final box = GetStorage();

  Future register({
    required String name,
    required String username,
    required String email,
    required String password,
  }) async {
    try {
      isLoading(true);

      var data = {
        'name': name,
        'username': username,
        'email': email,
        'password': password
      };

      var response = await http.post(
        Uri.parse('${url}register'),
        headers: {'Accept': 'application/json'},
        body: data,
      );

      if (response.statusCode == 201) {
        isLoading(false);
        token.value = json.decode(response.body)['token'];
        box.write('token', token.value);
        Get.offAll(() => const MainPage());
      } else {
        isLoading(false);
        Get.snackbar(
          'Error',
          json.decode(response.body)['message'],
          snackPosition: SnackPosition.TOP,
          backgroundColor: Colors.red,
          colorText: Colors.white,
        );
        print(json.decode(response.body));
      }
    } catch (e) {
      print(e.toString());
    }
  }

  Future login({
    required String username,
    required String password,
  }) async {
    try {
      isLoading(true);

      var data = {'username': username, 'password': password};

      var response = await http.post(
        Uri.parse('${url}login'),
        headers: {'Accept': 'application/json'},
        body: data,
      );

      if (response.statusCode == 200) {
        isLoading(false);
        token.value = json.decode(response.body)['token'];
        box.write('token', token.value);
        Get.offAll(() => const MainPage());
      } else {
        isLoading(false);
        Get.snackbar(
          'Error',
          json.decode(response.body)['message'],
          snackPosition: SnackPosition.TOP,
          backgroundColor: Colors.red,
          colorText: Colors.white,
        );
        print(json.decode(response.body));
      }
    } catch (e) {
      print(e.toString());
    }
  }
}
