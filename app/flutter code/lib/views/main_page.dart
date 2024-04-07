import 'package:app/views/chatbot_page.dart';
import 'package:app/views/detect_page.dart';
import 'package:app/views/home_page.dart';
import 'package:app/views/forum_page.dart';
import 'package:flutter/material.dart';
import 'package:google_fonts/google_fonts.dart';
// ignore: depend_on_referenced_packages
import 'package:curved_navigation_bar/curved_navigation_bar.dart';

class MainPage extends StatefulWidget {
  const MainPage({super.key});

  @override
  State<MainPage> createState() => _MainPageState();
}

class _MainPageState extends State<MainPage> {
  int currentIndex = 0;
  final screens = [
    const HomePage(),
    const DetectPage(),
    const ForumPage(),
    const ChatbotPage(),
  ];

  void changeIndex(int newIndex) {
    setState(() {
      currentIndex = newIndex;
    });
  }

  @override
  Widget build(BuildContext context) {
    var deviceWidth = MediaQuery.of(context).size.width;
    // ignore: unused_local_variable
    var deviceHeight = MediaQuery.of(context).size.height;

    return Scaffold(
      appBar: AppBar(
        title: Container(
          child: Row(
            mainAxisAlignment: MainAxisAlignment.center,
            crossAxisAlignment: CrossAxisAlignment.center,
            children: [
              SizedBox(
                width: deviceWidth * 0,
              ),
              Image.asset(
                'assets/images/logo.png',
                height: deviceWidth * 0.1,
              ),
              SizedBox(
                width: deviceWidth * 0.03,
              ),
              Text(
                'PLANTVERSE',
                style: GoogleFonts.poppins(
                  fontWeight: FontWeight.w800,
                  fontSize: deviceWidth * 0.070,
                  color: const Color.fromRGBO(51, 51, 51, 1),
                ),
              ),
            ],
          ),
        ),
        backgroundColor: const Color.fromRGBO(212, 255, 197, 1),
        elevation: 0,
        centerTitle: true,
      ),
      body: screens[currentIndex],
      bottomNavigationBar: CurvedNavigationBar(
        backgroundColor: Colors.white,
        animationDuration: Duration(milliseconds: 250),
        animationCurve: Curves.easeInOut,
        color: Color.fromRGBO(46, 73, 37, 1),
        index: currentIndex,
        onTap: (newIndex) => {
          setState(() {
            currentIndex = newIndex;
          })
        },
        items: [
          const Icon(
            Icons.home_filled,
            color: Colors.white,
          ),
          Container(
            child: Image.asset(
              'assets/icons/main.png',
              height: deviceWidth * 0.069,
            ),
          ),
          const Icon(
            Icons.forum,
            color: Colors.white,
          ),
          Container(
            child: Image.asset(
              'assets/icons/chatbot.png',
              height: deviceWidth * 0.085,
            ),
          )
        ],
      ),
    );
  }
}
