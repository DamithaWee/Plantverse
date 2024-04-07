import 'package:app/views/detect_disease.dart';
import 'package:app/views/detect_pest.dart';
import 'package:flutter/material.dart';
import 'package:google_fonts/google_fonts.dart';
// ignore: depend_on_referenced_packages
import 'package:get/get.dart';

class DetectPage extends StatefulWidget {
  const DetectPage({super.key});

  @override
  State<DetectPage> createState() => _DetectPageState();
}

class _DetectPageState extends State<DetectPage> {
  @override
  Widget build(BuildContext context) {
    var deviceWidth = MediaQuery.of(context).size.width;
    var deviceHeight = MediaQuery.of(context).size.height;

    return Scaffold(
      appBar: AppBar(
        title: Center(
          child: Text(
            'ANALYZE IAMGES',
            style: GoogleFonts.poppins(
              fontWeight: FontWeight.w800,
              fontSize: deviceWidth * 0.057,
              color: const Color.fromARGB(255, 51, 51, 51),
            ),
          ),
        ),
        backgroundColor: const Color.fromARGB(255, 242, 255, 242),
      ),
      body: Center(
        child: Column(
          mainAxisAlignment: MainAxisAlignment.center,
          crossAxisAlignment: CrossAxisAlignment.center,
          children: [
            Container(
              padding: EdgeInsetsDirectional.only(
                top: deviceHeight * 0.01,
                start: deviceWidth * 0.025,
                end: deviceWidth * 0.025,
              ),
              child: SizedBox(
                width: double.infinity,
                height: deviceHeight * 0.18,
                child: ElevatedButton.icon(
                  onPressed: () {
                    Get.to(() => const DetectDisease());
                  },
                  icon: Image.asset(
                    'assets/images/logo.png',
                    color: Colors.redAccent,
                    height: deviceWidth * 0.1,
                  ),
                  label: Text(
                    'Detect Crop Diseases',
                    style: GoogleFonts.poppins(
                      fontWeight: FontWeight.w600,
                      fontSize: deviceWidth * 0.070,
                      color: const Color.fromRGBO(51, 51, 51, 1),
                    ),
                  ),
                  style: ElevatedButton.styleFrom(
                    backgroundColor: const Color.fromRGBO(221, 255, 209, 1),
                    elevation: 0,
                    shape: RoundedRectangleBorder(
                      borderRadius: BorderRadius.circular(8.0),
                    ),
                  ),
                ),
              ),
            ),
            SizedBox(
              height: deviceHeight * 0.15,
            ),
            Container(
              padding: EdgeInsetsDirectional.only(
                top: deviceHeight * 0.01,
                start: deviceWidth * 0.025,
                end: deviceWidth * 0.025,
              ),
              child: SizedBox(
                width: double.infinity,
                height: deviceHeight * 0.18,
                child: ElevatedButton.icon(
                  onPressed: () {
                    Get.to(() => const DetectPest());
                  },
                  icon: Image.asset(
                    'assets/images/logo.png',
                    color: Colors.blueAccent,
                    height: deviceWidth * 0.1,
                  ),
                  label: Text(
                    'Detect Crop Pests',
                    style: GoogleFonts.poppins(
                      fontWeight: FontWeight.w600,
                      fontSize: deviceWidth * 0.070,
                      color: const Color.fromRGBO(51, 51, 51, 1),
                    ),
                  ),
                  style: ElevatedButton.styleFrom(
                    backgroundColor: const Color.fromRGBO(221, 255, 209, 1),
                    elevation: 0,
                    shape: RoundedRectangleBorder(
                      borderRadius: BorderRadius.circular(8.0),
                    ),
                  ),
                ),
              ),
            ),
          ],
        ),
      ),
    );
  }
}
