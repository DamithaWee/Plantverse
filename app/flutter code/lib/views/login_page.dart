import 'package:app/controllers/authentication.dart';
import 'package:app/views/register_page.dart';
import 'package:flutter/material.dart';
import 'package:google_fonts/google_fonts.dart';
import 'package:get/get.dart';
import 'package:animate_do/animate_do.dart';
import './widgets/input_widget.dart';

class LoginPage extends StatefulWidget {
  const LoginPage({super.key});

  @override
  State<LoginPage> createState() => _LoginPageState();
}

class _LoginPageState extends State<LoginPage> {
  final TextEditingController _usernameController = TextEditingController();
  final TextEditingController _passwordController = TextEditingController();
  final AuthenticationController _authenticationController =
      Get.put(AuthenticationController());

  @override
  Widget build(BuildContext context) {
    final width = MediaQuery.of(context).size.width;
    final height = MediaQuery.of(context).size.height;
    return Scaffold(
      backgroundColor: Colors.white,
      body: SingleChildScrollView(
        child: Column(
          crossAxisAlignment: CrossAxisAlignment.start,
          children: <Widget>[
            Container(
              height: height * 0.37,
              child: Stack(
                children: <Widget>[
                  Positioned(
                    top: -40,
                    height: height * 0.37,
                    width: width,
                    child: FadeInUp(
                        duration: const Duration(milliseconds: 450),
                        child: Container(
                          decoration: const BoxDecoration(
                              image: DecorationImage(
                                  image: AssetImage(
                                      'assets/images/background.png'),
                                  fit: BoxFit.fill)),
                        )),
                  ),
                  Positioned(
                    height: height * 0.37,
                    width: width + 20,
                    child: FadeInUp(
                        duration: const Duration(milliseconds: 500),
                        child: Container(
                          decoration: const BoxDecoration(
                              image: DecorationImage(
                                  image: AssetImage(
                                      'assets/images/background-2.png'),
                                  fit: BoxFit.fill)),
                        )),
                  )
                ],
              ),
            ),
            Padding(
              padding: const EdgeInsets.symmetric(horizontal: 40),
              child: Column(
                crossAxisAlignment: CrossAxisAlignment.start,
                children: <Widget>[
                  FadeInUp(
                      duration: const Duration(milliseconds: 600),
                      child: Text(
                        "LOGIN",
                        style: GoogleFonts.poppins(
                          fontSize: width * 0.087,
                          fontWeight: FontWeight.bold,
                          color: const Color.fromRGBO(41, 79, 39, 1),
                        ),
                      )),
                  SizedBox(
                    height: height * 0.045,
                  ),
                  FadeInUp(
                      duration: const Duration(milliseconds: 650),
                      child: Container(
                        decoration: BoxDecoration(
                            borderRadius: BorderRadius.circular(10),
                            color: Colors.white,
                            border: Border.all(
                                color:
                                    const Color.fromRGBO(144, 198, 135, 0.298)),
                            boxShadow: const [
                              BoxShadow(
                                color: Color.fromRGBO(149, 198, 135, 0.298),
                                blurRadius: 20,
                                offset: Offset(0, 10),
                              )
                            ]),
                        child: Column(
                          children: <Widget>[
                            InputWidget(
                                hintText: "Username",
                                controller: _usernameController,
                                obscureText: false),
                            InputWidget(
                                hintText: "Password",
                                controller: _passwordController,
                                obscureText: true),
                          ],
                        ),
                      )),
                  SizedBox(
                    height: height * 0.05,
                  ),
                  FadeInUp(
                      duration: const Duration(milliseconds: 750),
                      child: MaterialButton(
                        onPressed: () async {
                          await _authenticationController.login(
                              username: _usernameController.text.trim(),
                              password: _passwordController.text.trim());
                        },
                        color: const Color.fromRGBO(41, 79, 39, 1),
                        shape: RoundedRectangleBorder(
                          borderRadius: BorderRadius.circular(50),
                        ),
                        height: height * 0.065,
                        child: Center(
                          child: Text(
                            "LOGIN",
                            style: GoogleFonts.poppins(
                              fontSize: width * 0.05,
                              fontWeight: FontWeight.w500,
                              color: Colors.white,
                            ),
                          ),
                        ),
                      )),
                  FadeInUp(
                      duration: const Duration(milliseconds: 800),
                      child: Center(
                          child: TextButton(
                              onPressed: () {
                                Get.to(() => const RegisterPage());
                              },
                              child: Text(
                                "Create Account",
                                style: GoogleFonts.poppins(
                                  fontSize: width * 0.035,
                                  color: const Color.fromRGBO(41, 79, 39, 1),
                                ),
                              )))),
                ],
              ),
            )
          ],
        ),
      ),
    );
  }
}
