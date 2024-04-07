import 'dart:convert';
import 'package:app/constants/constants.dart';
import 'package:get/get.dart';
import 'package:http/http.dart' as http;
import 'dart:io';

class DetectController extends GetxController {
  Future<void> sendImageToServer(File imageFile) async {
    String base64Image = base64Encode(imageFile.readAsBytesSync());
    String url = '${fastAPI}predict';

    try {
      var response = await http.post(Uri.parse(url),
          body: jsonEncode({'image': base64Image}),
          headers: {'Content-Type': 'application/json'});

      // Handle response from FastAPI server
      print('Response status: ${response.statusCode}');
      print('Response body: ${response.body}');
    } catch (e) {
      print('Error sending image to server: $e');
    }
  }
}
