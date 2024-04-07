import 'dart:convert';
import 'dart:io';

import 'package:app/constants/constants.dart';
import 'package:flutter/material.dart';
import 'package:google_fonts/google_fonts.dart';
import 'package:image_picker/image_picker.dart';
import 'package:http/http.dart' as http;
import 'package:app/controllers/dectect_controller.dart';

class DetectPest extends StatefulWidget {
  const DetectPest({super.key});

  @override
  State<DetectPest> createState() => _DetectPestState();
}

class _DetectPestState extends State<DetectPest> {
  final DetectController detectController = DetectController();
  File? _image;
  String? _predictionResult;

  final picker = ImagePicker();

  Future getImage() async {
    final pickedFile = await picker.getImage(source: ImageSource.gallery);

    setState(() {
      if (pickedFile != null) {
        _image = File(pickedFile.path);
      } else {
        print('No image selected.');
      }
    });
  }

  String formatToTwoDecimals(double n) {
    return n.toStringAsFixed(2);
  }

  Future<void> sendImageToServer(String route) async {
    if (_image == null) return;

    String apiUrl = '$fastAPI$route';

    // Create multipart request
    var request = http.MultipartRequest('POST', Uri.parse(apiUrl));
    request.files.add(await http.MultipartFile.fromPath('file', _image!.path));

    try {
      var response = await request.send();

      if (response.statusCode == 200) {
        var jsonResponse = await response.stream.bytesToString();
        var data = jsonDecode(jsonResponse);
        setState(() {
          _predictionResult =
              "Result: ${data['class']}, \nConfidence: ${formatToTwoDecimals(data['confidence'] * 100)}%";
        });
      } else {
        print('Request failed with status: ${response.statusCode}');
      }
    } catch (e) {
      print('Error sending image to server: $e');
    }
  }

  @override
  Widget build(BuildContext context) {
    var deviceWidth = MediaQuery.of(context).size.width;
    var deviceHeight = MediaQuery.of(context).size.height;
    return Scaffold(
      appBar: AppBar(
        title: Text(
          'Analyze your image\nfor pests',
          style: GoogleFonts.poppins(
            fontWeight: FontWeight.w600,
            fontSize: deviceWidth * 0.070,
            color: const Color.fromRGBO(51, 51, 51, 1),
          ),
          textAlign: TextAlign.center,
        ),
      ),
      body: Center(
        child: Column(
          mainAxisAlignment: MainAxisAlignment.center,
          children: <Widget>[
            Container(
              height: deviceHeight * 0.3,
              child: _image == null
                  ? const Text('No image selected.')
                  : Image.file(_image!),
            ),
            const SizedBox(height: 20),
            _predictionResult == null
                ? Padding(
                    padding: const EdgeInsets.symmetric(horizontal: 15),
                    child: Center(
                      child: Text(
                        'Tap on the image icon and upload your image',
                        style: GoogleFonts.poppins(
                          fontWeight: FontWeight.w600,
                          fontSize: deviceWidth * 0.050,
                          color: const Color.fromRGBO(51, 51, 51, 1),
                        ),
                        textAlign: TextAlign.center,
                      ),
                    ),
                  )
                : Padding(
                    padding: const EdgeInsets.symmetric(horizontal: 15),
                    child: Center(
                      child: Text(
                        _predictionResult!,
                        style: GoogleFonts.poppins(
                          fontWeight: FontWeight.w600,
                          fontSize: deviceWidth * 0.050,
                          color: const Color.fromRGBO(51, 51, 51, 1),
                        ),
                        textAlign: TextAlign.center,
                      ),
                    ),
                  )
          ],
        ),
      ),
      floatingActionButton: SizedBox(
        height: deviceHeight * 0.09,
        width: deviceWidth * 0.2,
        child: FloatingActionButton(
          onPressed: () async {
            await getImage();
            await sendImageToServer("predict");
          },
          tooltip: 'Pick Image',
          backgroundColor: Colors.green,
          child: Icon(
            Icons.add_a_photo,
            color: Colors.white,
            size: deviceHeight * 0.06,
          ),
        ),
      ),
    );
  }
}
