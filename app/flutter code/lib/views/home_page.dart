import 'package:app/views/forum_page.dart';
import 'package:app/views/main_page.dart';
import 'package:flutter/material.dart';
// ignore: depend_on_referenced_packages
import 'package:curved_navigation_bar/curved_navigation_bar.dart';
import 'package:app/views/chatbot_page.dart';
import 'package:app/views/detect_page.dart';
import 'package:google_fonts/google_fonts.dart';

class HomePage extends StatefulWidget {
  const HomePage({super.key});

  @override
  State<HomePage> createState() => _HomePageState();
}

class _HomePageState extends State<HomePage> {
  final navigationKey = GlobalKey<CurvedNavigationBarState>();
  final MainPageController = new MainPage();
  final screens = [
    HomePage(),
    DetectPage(),
    ForumPage(),
    ChatbotPage(),
  ];

  @override
  Widget build(BuildContext context) {
    var deviceWidth = MediaQuery.of(context).size.width;
    var deviceHeight = MediaQuery.of(context).size.height;

    return Scaffold(
      body: SingleChildScrollView(
        child: Column(
          children: [
            SizedBox(
              height: deviceHeight * 0.01,
            ),
            Padding(
              padding: const EdgeInsets.symmetric(horizontal: 10),
              child: Container(
                decoration: BoxDecoration(
                  color: const Color.fromARGB(255, 198, 242, 200),
                  borderRadius: BorderRadius.circular(10),
                ),

                // height: deviceHeight * 0.05,
                child: Padding(
                  padding: const EdgeInsets.symmetric(horizontal: 10),
                  child: Column(
                    children: [
                      const SizedBox(
                        height: 5,
                      ),
                      Text(
                        'Analyze crops & fight\ndiseases/pests!',
                        style: GoogleFonts.poppins(
                          fontSize: deviceWidth * 0.1,
                          fontWeight: FontWeight.bold,
                        ),
                        textAlign: TextAlign.center,
                      ),
                      const SizedBox(height: 10.0),
                      Text(
                        'The all-in-one app for healthy crops.',
                        style: GoogleFonts.poppins(
                          fontSize: deviceWidth * 0.05,
                          color: Colors.grey,
                        ),
                        textAlign: TextAlign.center,
                      ),
                      SizedBox(
                        height: deviceHeight * 0.03,
                      ),
                      Column(
                        mainAxisAlignment: MainAxisAlignment.spaceEvenly,
                        crossAxisAlignment: CrossAxisAlignment.center,
                        children: [
                          GestureDetector(
                            onTap: () {},
                            child: SizedBox(
                              child: Center(
                                child: Container(
                                  // color: Color.fromARGB(255, 239, 243, 238),
                                  height: deviceHeight * 0.2,
                                  width: deviceWidth * 0.5,
                                  decoration: BoxDecoration(
                                    color: const Color.fromARGB(
                                        255, 239, 243, 238),
                                    borderRadius: BorderRadius.circular(10),
                                  ),
                                  child: Padding(
                                    padding: const EdgeInsets.all(10.0),
                                    child: Column(
                                      mainAxisAlignment:
                                          MainAxisAlignment.center,
                                      crossAxisAlignment:
                                          CrossAxisAlignment.center,
                                      children: [
                                        Image.asset(
                                          'assets/images/logo.png',
                                          color: Colors.green,
                                          height: deviceWidth * 0.12,
                                        ),
                                        const SizedBox(height: 5.0),
                                        Text(
                                          'Image Analysis',
                                          style: GoogleFonts.poppins(
                                            fontSize: deviceHeight * 0.02,
                                            fontWeight: FontWeight.bold,
                                          ),
                                        ),
                                        const SizedBox(height: 5.0),
                                        Text(
                                          'Identify diseases & pests',
                                          style: GoogleFonts.poppins(
                                            fontSize: deviceHeight * 0.015,
                                            color: Colors.grey,
                                          ),
                                        ),
                                      ],
                                    ),
                                  ),
                                ),
                              ),
                            ),
                          ),
                          SizedBox(
                            height: deviceHeight * 0.02,
                          ),
                          GestureDetector(
                            onTap: () {},
                            child: SizedBox(
                              child: Center(
                                child: Container(
                                  // color: Color.fromARGB(255, 239, 243, 238),
                                  height: deviceHeight * 0.2,
                                  width: deviceWidth * 0.5,
                                  decoration: BoxDecoration(
                                    color: Color.fromARGB(255, 239, 243, 238),
                                    borderRadius: BorderRadius.circular(10),
                                  ),
                                  child: Padding(
                                    padding: const EdgeInsets.all(10.0),
                                    child: Column(
                                      mainAxisAlignment:
                                          MainAxisAlignment.center,
                                      crossAxisAlignment:
                                          CrossAxisAlignment.center,
                                      children: [
                                        Icon(
                                          Icons.forum,
                                          size: deviceHeight * 0.05,
                                          color: Colors.green,
                                        ),
                                        const SizedBox(height: 5.0),
                                        Text(
                                          'Community Forum',
                                          style: GoogleFonts.poppins(
                                            fontSize: deviceHeight * 0.02,
                                            fontWeight: FontWeight.bold,
                                          ),
                                        ),
                                        const SizedBox(height: 5.0),
                                        Text(
                                          'Connect with other farmers',
                                          style: GoogleFonts.poppins(
                                            fontSize: deviceHeight * 0.015,
                                            color: Colors.grey,
                                          ),
                                        ),
                                      ],
                                    ),
                                  ),
                                ),
                              ),
                            ),
                          ),
                          SizedBox(
                            height: deviceHeight * 0.02,
                          ),
                          GestureDetector(
                            onTap: () {},
                            child: SizedBox(
                              child: Center(
                                child: Container(
                                  // color: Color.fromARGB(255, 239, 243, 238),
                                  height: deviceHeight * 0.2,
                                  width: deviceWidth * 0.5,
                                  decoration: BoxDecoration(
                                    color: const Color.fromARGB(
                                        255, 239, 243, 238),
                                    borderRadius: BorderRadius.circular(10),
                                  ),
                                  child: Padding(
                                    padding: const EdgeInsets.all(10.0),
                                    child: Column(
                                      mainAxisAlignment:
                                          MainAxisAlignment.center,
                                      crossAxisAlignment:
                                          CrossAxisAlignment.center,
                                      children: [
                                        Image.asset(
                                          'assets/icons/chatbot.png',
                                          height: deviceHeight * 0.065,
                                          color: Colors.green,
                                        ),
                                        const SizedBox(height: 5.0),
                                        Text(
                                          'Chatbot Assistant',
                                          style: GoogleFonts.poppins(
                                            fontSize: deviceHeight * 0.02,
                                            fontWeight: FontWeight.bold,
                                          ),
                                        ),
                                        const SizedBox(height: 5.0),
                                        Text(
                                          'Get quick answers',
                                          style: GoogleFonts.poppins(
                                            fontSize: deviceHeight * 0.015,
                                            color: Colors.grey,
                                          ),
                                        ),
                                      ],
                                    ),
                                  ),
                                ),
                              ),
                            ),
                          ),
                          SizedBox(
                            height: deviceHeight * 0.02,
                          ),
                        ],
                      ),
                    ],
                  ),
                ),
              ),
            )
          ],
        ),
      ),
    );
  }
}
